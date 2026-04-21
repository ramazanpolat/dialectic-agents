#!/usr/bin/env python3
"""The Crucible — Local evaluation server bridging browser to claude -p.

Uses agentic Claude: runs claude -p in the project directory so it can
search and read artifact files directly. Streams progress to terminal.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 3456
BASE = Path(__file__).resolve().parent
ARTIFACTS_ROOT = BASE / "dialectic-agents"
CLAUDE_BIN = shutil.which("claude") or str(Path.home() / ".local/bin/claude")

# Env: strip nesting blockers + API key so claude uses subscription
CLEAN_ENV = {
    k: v for k, v in os.environ.items()
    if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "ANTHROPIC_API_KEY")
}


def log(msg: str) -> None:
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


# ---------------------------------------------------------------------------
# Frontmatter parser (for /api/artifacts endpoint)
# ---------------------------------------------------------------------------

TITLE_STRIP = re.compile(
    r"^(?:Definition|Primitive|Axiom|Postulate|Proposition|Theorem|Lemma|"
    r"Corollary|Hypothesis|Theory|Model|Synthesis|Classification of [A-Z]+-\d+"
    r"|Classification):\s+",
    re.IGNORECASE,
)

DESC_PATTERNS = [
    re.compile(r"##[ \t]+Statement[ \t]*\r?\n([\s\S]*?)(?=\n##[ \t]|$)"),
    re.compile(r"##[ \t]+Executive Summary[ \t]*\r?\n([\s\S]*?)(?=\n##[ \t]|$)"),
    re.compile(r"##[ \t]+Dialectical Synthesis[ \t]*\r?\n([\s\S]*?)(?=\n##[ \t]|$)"),
    re.compile(r"##[ \t]+Hypothesis Structure[ \t]*\r?\n([\s\S]*?)(?=\n##[ \t]|$)"),
    re.compile(r"##[ \t]+Theory Structure[ \t]*\r?\n([\s\S]*?)(?=\n##[ \t]|$)"),
    re.compile(r"##[ \t]+Summary[ \t]*\r?\n([\s\S]*?)(?=\n##[ \t]|$)"),
]


def parse_frontmatter(text: str) -> tuple[dict | None, str]:
    m = re.match(r"^---[ \t]*\r?\n([\s\S]*?)\r?\n---[ \t]*\r?\n", text)
    if not m:
        return None, text
    fm: dict = {}
    for line in m.group(1).split("\n"):
        colon = line.find(":")
        if colon < 0:
            continue
        key = line[:colon].strip()
        val = line[colon + 1 :].strip()
        if not key or key.startswith("#"):
            continue
        if (val.startswith('"') and val.endswith('"')) or (
            val.startswith("'") and val.endswith("'")
        ):
            val = val[1:-1]
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            val = (
                [s.strip().strip("\"'") for s in inner.split(",") if s.strip()]
                if inner
                else []
            )
        else:
            try:
                val = float(val) if "." in val else int(val)
            except ValueError:
                pass
        fm[key] = val
    return fm, text[m.end() :]


def extract_title(body: str) -> str:
    m = re.search(r"^#[ \t]+(.+)$", body, re.MULTILINE)
    if not m:
        return ""
    t = m.group(1).strip()
    t = TITLE_STRIP.sub("", t)
    t = re.sub(r"^The\s+", "", t)
    return t[:80].strip()


def extract_desc(body: str) -> str:
    section = ""
    for pat in DESC_PATTERNS:
        m = pat.search(body)
        if m and m.group(1).strip():
            section = m.group(1)
            break
    if not section:
        m = re.search(r"^#[ \t]+.+$\n([\s\S]*?)(?=\n#+|$)", body, re.MULTILINE)
        section = m.group(1) if m else ""
    text = ""
    for p in re.split(r"\n\n+", section):
        pt = p.strip()
        if not pt or pt.startswith("#") or pt.startswith("|"):
            continue
        if re.match(r"^[-*] ", pt):
            if not text:
                text = re.sub(r"^[-*]\s+", "", pt.split("\n")[0])
            continue
        text = pt
        break
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()[:400]


def parse_artifact(path: Path) -> dict | None:
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception:
        return None
    fm, body = parse_frontmatter(raw)
    if not fm:
        return None
    aid = str(fm.get("id", "")).strip()
    if not aid:
        return None
    agent = str(fm.get("agent", path.parent.parent.name)).lower()
    depends = fm.get("depends_on", [])
    if not isinstance(depends, list):
        depends = []
    conf = fm.get("confidence", 0.8)
    try:
        conf = float(conf)
    except (ValueError, TypeError):
        conf = 0.8
    layer = fm.get("layer", 0)
    try:
        layer = int(round(float(layer)))
    except (ValueError, TypeError):
        layer = 0
    return {
        "id": aid,
        "agent": agent,
        "type": str(fm.get("type", "unknown")),
        "status": str(fm.get("status", "draft")),
        "title": extract_title(body),
        "confidence": conf,
        "layer": layer,
        "depends": depends,
        "domain": str(fm.get("domain", "unknown")),
        "desc": extract_desc(body),
    }


_artifact_cache: list[dict] | None = None


def load_artifacts(force: bool = False) -> list[dict]:
    global _artifact_cache
    if _artifact_cache is not None and not force:
        return _artifact_cache
    arts: list[dict] = []
    for md in sorted(ARTIFACTS_ROOT.glob("*/artifacts/*.md")):
        a = parse_artifact(md)
        if a:
            arts.append(a)
    _artifact_cache = arts
    return arts


# ---------------------------------------------------------------------------
# Evaluation prompt — minimal, tells Claude to search files itself
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are The Crucible, an epistemic evaluation engine for the Alignment Paradox \
project. You evaluate claims through 7 agent lenses against a knowledge base \
of philosophical artifacts.

You are running in the alignment-paradox project directory. The knowledge base \
lives at dialectic-agents/*/artifacts/*.md (75 artifacts across 9 agents: \
logos, axiom, propo, ori, tribunal, hypothex, theorica, synthesis, watcher).

Each artifact has YAML frontmatter with: id, agent, type, status, confidence, \
layer, depends_on, domain. The body has structured sections.

You MUST search and read the relevant artifacts to ground your evaluation. \
Use Glob and Read tools to explore the KB before evaluating.

Your final response MUST be ONLY a valid JSON object matching the required \
schema — no markdown fences, no commentary before or after."""

JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "tests": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "num": {"type": "integer"},
                    "name": {"type": "string"},
                    "agent": {"type": "string"},
                    "status": {"type": "string", "enum": ["pass", "warn", "fail"]},
                    "label": {"type": "string"},
                    "body_html": {"type": "string"},
                    "summary": {"type": "string"},
                },
                "required": ["num", "name", "agent", "status", "label", "body_html", "summary"],
            },
            "minItems": 7,
            "maxItems": 7,
        },
        "classification": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "label": {"type": "string"},
                "desc": {"type": "string"},
            },
            "required": ["type", "label", "desc"],
        },
        "epistemic_status": {
            "type": "object",
            "properties": {
                "verdict": {"type": "string"},
                "route": {"type": "string"},
            },
            "required": ["verdict", "route"],
        },
        "confidence": {"type": "number"},
        "validity": {"type": "string"},
        "related_artifacts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "agent": {"type": "string"},
                    "score": {"type": "number"},
                },
                "required": ["id", "title", "agent", "score"],
            },
        },
        "recommendation": {"type": "string"},
        "missing_infrastructure": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "tests", "classification", "epistemic_status", "confidence",
        "validity", "related_artifacts", "recommendation", "missing_infrastructure",
    ],
}


def build_prompt(claim: str) -> str:
    return f"""\
Evaluate the following claim through 7 epistemic agent lenses.

STEP 1: Search the knowledge base.
- Use Glob to list dialectic-agents/*/artifacts/*.md
- Read the most relevant artifacts (definitions from logos, axioms from axiom, \
propositions from propo, etc.) to ground your analysis.
- You don't need to read all 75 — focus on the ones relevant to the claim's terms and concepts.

STEP 2: Run 7 tests with real philosophical analysis:

Test 1 — Term Analysis (Agent: Logos)
Which terms have definitions in the KB (logos agent)? Which are undefined? Coverage?

Test 2 — Axiom Compatibility (Agent: Axiom)
Compatible with KB axioms? Contradictions? Does it have axiomatic character?

Test 3 — Proposition Form (Agent: Propo)
Truth-evaluable? Logical form? Scope? Analytic vs synthetic? Modality?

Test 4 — Epistemic Classification (Agent: Ori)
A priori, a posteriori, or mixed? Negation/conceivability/justification tests.

Test 5 — Deductive Assessment (Agent: Tribunal)
If a priori/mixed: derivable from KB axioms? If a posteriori: status "warn", label "Routed to Hypothex".

Test 6 — Empirical Assessment (Agent: Hypothex)
If a posteriori/mixed: falsifiable? Null hypothesis? If a priori: status "warn", label "Routed to Tribunal".

Test 7 — System Integration (Agent: Synthesis)
Relation to existing KB? Novelty (0-1)? Contradictions? Integration potential?

STEP 3: Produce the JSON result.

For each test's body_html, use these CSS classes:
- <div class="finding"><span class="finding-label">Label:</span> content</div>
- <span class="term-tag term-defined">word -> ARTIFACT-ID</span>
- <span class="term-tag term-undefined">word</span>
- <span class="term-tag term-partial">word ~ near-match</span>

classification.type: postulate | definition | theorem-candidate | hypothesis | proposition
validity: valid | plausible | contradicted | not evaluable
epistemic_status.verdict: a_priori | a_posteriori | mixed

CLAIM TO EVALUATE:
"{claim}"
"""


# ---------------------------------------------------------------------------
# Call Claude with Popen streaming for real-time progress logging
# ---------------------------------------------------------------------------

def call_claude(claim: str) -> dict:
    prompt = build_prompt(claim)
    schema_str = json.dumps(JSON_SCHEMA)

    log(f"EVALUATE: \"{claim[:80]}{'...' if len(claim) > 80 else ''}\"")
    log(f"  Prompt: {len(prompt):,} chars (no KB dump — Claude will search files)")

    cmd = [
        CLAUDE_BIN,
        "-p",
        prompt,
        "--output-format", "stream-json",
        "--system-prompt", SYSTEM_PROMPT,
        "--json-schema", schema_str,
        "--no-session-persistence",
    ]

    log(f"  Starting claude -p (stream-json, cwd={BASE.name}/)")
    t0 = time.time()
    tool_calls = 0
    text_chunks = 0
    final_result = None
    last_activity = time.time()

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(BASE),
        env=CLEAN_ENV,
    )

    # Stream stderr in background thread for error capture
    stderr_lines: list[str] = []

    def drain_stderr():
        for line in proc.stderr:
            line = line.rstrip()
            if line:
                stderr_lines.append(line)

    stderr_thread = threading.Thread(target=drain_stderr, daemon=True)
    stderr_thread.start()

    # Ticker thread: prints elapsed every 10s while waiting
    stop_ticker = threading.Event()

    def ticker():
        while not stop_ticker.is_set():
            stop_ticker.wait(10)
            if not stop_ticker.is_set():
                elapsed = time.time() - t0
                log(f"  ... {elapsed:.0f}s elapsed | {tool_calls} tool calls | {text_chunks} text chunks")

    ticker_thread = threading.Thread(target=ticker, daemon=True)
    ticker_thread.start()

    try:
        for raw_line in proc.stdout:
            raw_line = raw_line.rstrip()
            if not raw_line:
                continue
            last_activity = time.time()

            try:
                event = json.loads(raw_line)
            except json.JSONDecodeError:
                log(f"  [unparseable line] {raw_line[:120]}")
                continue

            etype = event.get("type", "")

            if etype == "system":
                subtype = event.get("subtype", "")
                log(f"  [system] {subtype}")

            elif etype == "assistant":
                msg = event.get("message", {})
                content_blocks = msg.get("content", [])
                for block in content_blocks:
                    btype = block.get("type", "")
                    if btype == "tool_use":
                        tool_calls += 1
                        tool_name = block.get("name", "?")
                        inp = block.get("input", {})
                        # Show what Claude is doing
                        if tool_name == "Glob":
                            log(f"  [tool {tool_calls}] Glob: {inp.get('pattern', '?')}")
                        elif tool_name == "Read":
                            fp = inp.get("file_path", "?")
                            # Shorten path for display
                            short = fp.replace(str(BASE) + "/", "")
                            log(f"  [tool {tool_calls}] Read: {short}")
                        elif tool_name == "Grep":
                            log(f"  [tool {tool_calls}] Grep: \"{inp.get('pattern', '?')}\" in {inp.get('path', '.')}")
                        else:
                            log(f"  [tool {tool_calls}] {tool_name}")
                    elif btype == "text":
                        text_chunks += 1
                        snippet = block.get("text", "")[:80].replace("\n", " ")
                        if text_chunks <= 3 or text_chunks % 5 == 0:
                            log(f"  [text #{text_chunks}] {snippet}...")

            elif etype == "result":
                final_result = event
                subtype = event.get("subtype", "")
                cost = event.get("total_cost_usd", event.get("cost_usd", 0))
                turns = event.get("num_turns", 0)
                elapsed = time.time() - t0
                log(f"  [result] {subtype} | {elapsed:.1f}s | {turns} turns | ${cost:.4f} | {tool_calls} tool calls")

        proc.wait(timeout=10)

    except Exception as e:
        proc.kill()
        raise RuntimeError(f"Error reading claude stream: {e}")
    finally:
        stop_ticker.set()
        ticker_thread.join(timeout=2)

    elapsed = time.time() - t0
    log(f"  Process exited: code={proc.returncode} | total={elapsed:.1f}s")

    if stderr_lines:
        log(f"  stderr: {' | '.join(stderr_lines[:5])}")

    if proc.returncode != 0:
        raise RuntimeError(
            f"claude exited {proc.returncode}: {' '.join(stderr_lines[:3])}"
        )

    if not final_result:
        raise RuntimeError("No result event received from claude stream")

    # Extract evaluation JSON from result
    # With --json-schema, Claude uses StructuredOutput tool -> "structured_output" field
    # Without it, the response text is in "result" field
    structured = final_result.get("structured_output")
    response_text = final_result.get("result", "")

    if structured:
        # structured_output is already a parsed dict/object
        if isinstance(structured, dict):
            log(f"  Got structured_output (dict, keys: {list(structured.keys())})")
            evaluation = structured
        elif isinstance(structured, str):
            log(f"  Got structured_output (string, {len(structured):,} chars)")
            evaluation = json.loads(structured)
        else:
            log(f"  Got structured_output (type: {type(structured).__name__})")
            evaluation = json.loads(str(structured))
    elif response_text:
        log(f"  Got result text: {len(response_text):,} chars")
        try:
            evaluation = json.loads(response_text)
            log(f"  Parsed JSON OK: {list(evaluation.keys())}")
        except json.JSONDecodeError:
            m = re.search(r"```(?:json)?\s*\n([\s\S]*?)\n```", response_text)
            if m:
                evaluation = json.loads(m.group(1))
                log(f"  Extracted from fences OK")
            else:
                log(f"  PARSE FAIL — first 500 chars: {response_text[:500]}")
                raise RuntimeError(f"Failed to parse evaluation JSON: {response_text[:300]}")
    else:
        log(f"  No result data. Keys: {list(final_result.keys())}")
        # Log any other fields that might contain data
        for k in ("structured_output", "result", "content"):
            v = final_result.get(k)
            if v:
                log(f"  field '{k}': {str(v)[:200]}")
        raise RuntimeError(f"Empty result. Keys: {list(final_result.keys())}")

    return evaluation


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------


class CrucibleHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/crucible-live.html"
            log("GET / -> serving crucible-live.html")
            return super().do_GET()
        if self.path == "/api/artifacts":
            arts = load_artifacts(force=True)
            log(f"GET /api/artifacts -> {len(arts)} artifacts")
            return self._json_response(arts)
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/evaluate":
            return self._handle_evaluate()
        self.send_error(404)

    def _handle_evaluate(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
        except (ValueError, json.JSONDecodeError):
            log("POST /api/evaluate -> 400 invalid JSON body")
            return self._json_response({"error": "Invalid JSON body"}, 400)

        claim = body.get("claim", "").strip()
        if not claim:
            log("POST /api/evaluate -> 400 missing claim")
            return self._json_response({"error": "Missing 'claim' field"}, 400)

        log(f"POST /api/evaluate -> claim: \"{claim[:60]}\" ({len(claim)} chars)")
        try:
            result = call_claude(claim)
            tests_summary = " ".join(
                f"T{t['num']}:{t['status']}" for t in result.get("tests", [])
            )
            log(f"  DONE: {result.get('classification', {}).get('label', '?')} "
                f"| {result.get('validity', '?')} "
                f"| conf={result.get('confidence', 0):.0%} "
                f"| [{tests_summary}]")
            return self._json_response(result)
        except subprocess.TimeoutExpired:
            log("  TIMEOUT: claude exceeded time limit")
            return self._json_response(
                {"error": "Claude evaluation timed out"}, 504
            )
        except FileNotFoundError:
            log(f"  ERROR: claude CLI not found at {CLAUDE_BIN}")
            return self._json_response(
                {"error": f"claude CLI not found at {CLAUDE_BIN}"}, 500
            )
        except RuntimeError as e:
            log(f"  ERROR (502): {e}")
            return self._json_response({"error": str(e)}, 502)
        except Exception as e:
            log(f"  ERROR (500): {type(e).__name__}: {e}")
            return self._json_response({"error": f"Unexpected error: {e}"}, 500)

    def _json_response(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, fmt, *args):
        pass  # suppress default HTTP logs, we have our own


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import signal

    if not Path(CLAUDE_BIN).exists() and not shutil.which("claude"):
        print(f"WARNING: claude CLI not found at {CLAUDE_BIN}", file=sys.stderr)

    arts = load_artifacts()
    log(f"Loaded {len(arts)} artifacts from {ARTIFACTS_ROOT}")
    log(f"Server: http://localhost:{PORT}")
    log(f"Claude: {CLAUDE_BIN}")
    log(f"CWD for claude: {BASE}")
    log("Press Ctrl+C to stop\n")

    def force_exit(sig, frame):
        log("Ctrl+C — killing all child processes and exiting")
        # Kill any running claude subprocesses
        import subprocess as _sp
        _sp.run(["pkill", "-P", str(os.getpid())], capture_output=True)
        os._exit(0)

    signal.signal(signal.SIGINT, force_exit)
    signal.signal(signal.SIGTERM, force_exit)

    server = HTTPServer(("", PORT), CrucibleHandler)
    server.serve_forever()
