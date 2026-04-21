#!/usr/bin/env python3
"""The Crucible — Parallel subagent evaluation server.

Runs 7 agent tests as parallel claude -p subprocesses grouped into waves.
Results stream back to the browser via Server-Sent Events (SSE) as each
agent finishes, so tests appear progressively.

Wave 1 (parallel): T1 Logos, T2 Axiom, T3 Propo, T4 Ori, T7 Synthesis
Wave 2 (parallel): T5 Tribunal, T6 Hypothex (need Ori's verdict)
Wave 3 (single):   Classification + verdict synthesis
"""

import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 3457
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
# Frontmatter parser (reused from crucible-server.py)
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
# Agent schemas
# ---------------------------------------------------------------------------

AGENT_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["pass", "warn", "fail"]},
        "label": {"type": "string"},
        "body_html": {"type": "string"},
        "summary": {"type": "string"},
    },
    "required": ["status", "label", "body_html", "summary"],
}

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
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
        "classification", "epistemic_status", "confidence",
        "validity", "related_artifacts", "recommendation", "missing_infrastructure",
    ],
}


# ---------------------------------------------------------------------------
# CSS class reference (shared across agent prompts)
# ---------------------------------------------------------------------------

HTML_CLASSES = """\
Use these CSS classes in body_html for rich formatting:
- <div class="finding"><span class="finding-label">Label:</span> content</div>
- <span class="term-tag term-defined">word -> ARTIFACT-ID</span>
- <span class="term-tag term-undefined">word</span>
- <span class="term-tag term-partial">word ~ near-match</span>"""


# ---------------------------------------------------------------------------
# 7 Agent definitions
# ---------------------------------------------------------------------------

AGENTS = {
    1: {
        "name": "Logos",
        "test_name": "Term Analysis",
        "wave": 1,
        "system": (
            "You are Agent Logos, guardian of definitions and terminology for the "
            "Alignment Paradox project. You analyze whether the key terms in a claim "
            "have formal definitions in the knowledge base. You are running in the "
            "alignment-paradox project directory and can search files with Glob/Read/Grep."
        ),
        "prompt": """\
Analyze the following claim's terminology against the knowledge base.

STEP 1: Search for definitions.
- Use Glob to list dialectic-agents/logos/artifacts/*.md
- Also check dialectic-agents/*/artifacts/*.md for relevant definitions
- Read the most relevant definition files (focus on terms in the claim)

STEP 2: For each key term in the claim, classify it:
- DEFINED: Has a formal definition in the KB
- UNDEFINED: No definition found
- PARTIAL: Loosely related definition exists

STEP 3: Produce your evaluation JSON.
- status: "pass" if most key terms are defined, "warn" if mixed, "fail" if mostly undefined
- label: Brief coverage like "6/8 defined" or "3/5 terms covered"
- body_html: Rich HTML output using these CSS classes:
  {html_classes}
  Show each term with its status and link to artifact ID if found.
- summary: One sentence summarizing term coverage (e.g. "6 of 8 terms have KB definitions")

CLAIM TO EVALUATE:
"{claim}"
""",
    },
    2: {
        "name": "Axiom",
        "test_name": "Axiom Compatibility",
        "wave": 1,
        "system": (
            "You are Agent Axiom, keeper of foundational assumptions for the "
            "Alignment Paradox project. You check whether claims are compatible with "
            "the axioms in the knowledge base. You are running in the "
            "alignment-paradox project directory and can search files with Glob/Read/Grep."
        ),
        "prompt": """\
Check this claim against the axioms in the knowledge base.

STEP 1: Search for axioms.
- Use Glob to list dialectic-agents/axiom/artifacts/*.md
- Read the axiom files to understand foundational assumptions

STEP 2: Analyze compatibility.
- Is the claim compatible with existing axioms?
- Does it contradict any axiom?
- Does the claim itself have axiomatic character (self-evident, foundational)?

STEP 3: Produce your evaluation JSON.
- status: "pass" if compatible with axioms, "warn" if partially compatible or unclear, "fail" if contradicts axioms
- label: Brief like "Compatible" or "Contradicts AX-003" or "Axiomatic character"
- body_html: Rich HTML using these CSS classes:
  {html_classes}
  List each relevant axiom with compatibility assessment.
- summary: One sentence on axiom compatibility

CLAIM TO EVALUATE:
"{claim}"
""",
    },
    3: {
        "name": "Propo",
        "test_name": "Proposition Form",
        "wave": 1,
        "system": (
            "You are Agent Propo, analyst of propositional and logical form for the "
            "Alignment Paradox project. You assess the logical structure of claims. "
            "You are running in the alignment-paradox project directory and can search "
            "files with Glob/Read/Grep."
        ),
        "prompt": """\
Analyze the logical and propositional form of this claim.

STEP 1: Search for relevant propositions.
- Use Glob to list dialectic-agents/propo/artifacts/*.md
- Read relevant proposition files for comparison

STEP 2: Analyze the claim's form.
- Is it truth-evaluable? (Can it be true or false?)
- What is its logical form? (Universal, existential, conditional, etc.)
- What is its scope? (Universal, particular, singular?)
- Is it analytic or synthetic?
- What modality? (Necessary, contingent, possible?)

STEP 3: Produce your evaluation JSON.
- status: "pass" if well-formed truth-evaluable proposition, "warn" if ambiguous form, "fail" if not truth-evaluable
- label: Brief like "Universal syllogism" or "Synthetic a posteriori" or "Not truth-evaluable"
- body_html: Rich HTML using these CSS classes:
  {html_classes}
  Show logical form analysis with findings.
- summary: One sentence on propositional form (e.g. "Valid universal syllogism with necessary conclusion")

CLAIM TO EVALUATE:
"{claim}"
""",
    },
    4: {
        "name": "Ori",
        "test_name": "Epistemic Classification",
        "wave": 1,
        "system": (
            "You are Agent Ori, epistemic classifier for the Alignment Paradox project. "
            "You determine whether claims are a priori, a posteriori, or mixed using "
            "rigorous philosophical tests. You are running in the alignment-paradox "
            "project directory and can search files with Glob/Read/Grep."
        ),
        "prompt": """\
Classify the epistemic status of this claim.

STEP 1: Search for epistemic classifications.
- Use Glob to list dialectic-agents/ori/artifacts/*.md
- Read relevant classification files for methodology

STEP 2: Apply epistemic tests.
- Negation test: Can you conceive of its negation without contradiction?
- Conceivability test: Is it knowable through pure thought alone?
- Justification test: What kind of evidence/reasoning supports it?
- Is it a priori (knowable through reason alone)?
- Is it a posteriori (requires empirical evidence)?
- Or mixed (has both rational and empirical components)?

STEP 3: Produce your evaluation JSON.
- status: "pass" if classification is clear, "warn" if ambiguous, "fail" if unclassifiable
- label: "A priori" or "A posteriori" or "Mixed"
- body_html: Rich HTML using these CSS classes:
  {html_classes}
  Show each test result as a finding.
- summary: IMPORTANT — your summary MUST begin with the classification word: "a_priori", "a_posteriori", or "mixed" followed by a brief explanation. Example: "a_priori — derivable through logical deduction alone"

CLAIM TO EVALUATE:
"{claim}"
""",
    },
    5: {
        "name": "Tribunal",
        "test_name": "Deductive Assessment",
        "wave": 2,
        "system": (
            "You are Agent Tribunal, deductive assessor for the Alignment Paradox "
            "project. You evaluate whether claims can be derived from axioms through "
            "deductive reasoning. You are running in the alignment-paradox project "
            "directory and can search files with Glob/Read/Grep."
        ),
        "prompt": """\
Assess the deductive validity of this claim.

Ori classified this claim as: {ori_context}

If the classification is a_priori or mixed:
- Search dialectic-agents/axiom/artifacts/*.md and dialectic-agents/tribunal/artifacts/*.md
- Can this claim be derived from the KB axioms through valid deduction?
- What inference steps would be needed?
- Are there gaps in the derivation?

If the classification is a_posteriori:
- This claim is empirical, not deductive
- Set status to "warn" and label to "Routed to Hypothex"
- Briefly explain why deductive assessment doesn't apply

Produce your evaluation JSON.
- status: "pass" if derivable, "warn" if partially derivable or routed, "fail" if not derivable
- label: Brief like "Derivable from AX-001, AX-003" or "Routed to Hypothex"
- body_html: Rich HTML using these CSS classes:
  {html_classes}
- summary: One sentence on deductive status

CLAIM TO EVALUATE:
"{claim}"
""",
    },
    6: {
        "name": "Hypothex",
        "test_name": "Empirical Assessment",
        "wave": 2,
        "system": (
            "You are Agent Hypothex, empirical assessor for the Alignment Paradox "
            "project. You evaluate the empirical testability and falsifiability of "
            "claims. You are running in the alignment-paradox project directory and "
            "can search files with Glob/Read/Grep."
        ),
        "prompt": """\
Assess the empirical testability of this claim.

Ori classified this claim as: {ori_context}

If the classification is a_posteriori or mixed:
- Search dialectic-agents/hypothex/artifacts/*.md for related hypotheses
- Is this claim falsifiable? What would falsify it?
- What is the null hypothesis?
- What evidence would support or refute it?

If the classification is a_priori:
- This claim is purely rational, not empirical
- Set status to "warn" and label to "Routed to Tribunal"
- Briefly explain why empirical assessment doesn't apply

Produce your evaluation JSON.
- status: "pass" if falsifiable with clear test criteria, "warn" if partially testable or routed, "fail" if unfalsifiable
- label: Brief like "Falsifiable" or "Routed to Tribunal" or "Unfalsifiable"
- body_html: Rich HTML using these CSS classes:
  {html_classes}
- summary: One sentence on empirical status

CLAIM TO EVALUATE:
"{claim}"
""",
    },
    7: {
        "name": "Synthesis",
        "test_name": "System Integration",
        "wave": 1,
        "system": (
            "You are Agent Synthesis, system integrator for the Alignment Paradox "
            "project. You assess how claims relate to the existing knowledge base "
            "as a whole. You are running in the alignment-paradox project directory "
            "and can search files with Glob/Read/Grep."
        ),
        "prompt": """\
Assess how this claim integrates with the existing knowledge base.

STEP 1: Search broadly across the KB.
- Use Glob to list dialectic-agents/*/artifacts/*.md
- Read artifacts that seem related to the claim's concepts
- Check dialectic-agents/synthesis/artifacts/*.md for existing syntheses

STEP 2: Analyze integration.
- How does this claim relate to existing artifacts?
- Novelty score (0.0 = fully covered, 1.0 = completely novel)?
- Does it contradict anything in the KB?
- What is its integration potential?
- What artifacts would it connect to?

STEP 3: Produce your evaluation JSON.
- status: "pass" if integrates well, "warn" if partially novel, "fail" if contradicts existing KB
- label: Brief like "Novelty 0.3 — extends existing" or "Novel — no precedent"
- body_html: Rich HTML using these CSS classes:
  {html_classes}
  List related artifacts and integration analysis.
- summary: One sentence on system integration status

CLAIM TO EVALUATE:
"{claim}"
""",
    },
}

# Metadata for test display (maps agent num to display info)
TEST_META = {
    1: {"name": "Term Analysis", "agent": "Logos"},
    2: {"name": "Axiom Compatibility", "agent": "Axiom"},
    3: {"name": "Proposition Form", "agent": "Propo"},
    4: {"name": "Epistemic Classification", "agent": "Ori"},
    5: {"name": "Deductive Assessment", "agent": "Tribunal"},
    6: {"name": "Empirical Assessment", "agent": "Hypothex"},
    7: {"name": "System Integration", "agent": "Synthesis"},
}


# ---------------------------------------------------------------------------
# Extract structured output from claude stream result
# ---------------------------------------------------------------------------

def extract_structured(final_result: dict, agent_label: str) -> dict:
    """Extract the JSON output from a claude stream-json result event."""
    structured = final_result.get("structured_output")
    response_text = final_result.get("result", "")

    if structured:
        if isinstance(structured, dict):
            log(f"  [{agent_label}] Got structured_output (dict)")
            return structured
        elif isinstance(structured, str):
            log(f"  [{agent_label}] Got structured_output (string, {len(structured)} chars)")
            return json.loads(structured)
        else:
            log(f"  [{agent_label}] Got structured_output ({type(structured).__name__})")
            return json.loads(str(structured))
    elif response_text:
        log(f"  [{agent_label}] Got result text: {len(response_text)} chars")
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            m = re.search(r"```(?:json)?\s*\n([\s\S]*?)\n```", response_text)
            if m:
                return json.loads(m.group(1))
            raise RuntimeError(f"[{agent_label}] Failed to parse JSON: {response_text[:300]}")
    else:
        raise RuntimeError(f"[{agent_label}] Empty result. Keys: {list(final_result.keys())}")


# ---------------------------------------------------------------------------
# Call a single agent subprocess
# ---------------------------------------------------------------------------

def call_agent(num: int, claim: str, ori_context: str | None = None) -> dict:
    """Run a single agent as a claude -p subprocess. Returns the agent's JSON output."""
    agent = AGENTS[num]
    agent_label = f"T{num} {agent['name']}"

    # Build prompt
    prompt_text = agent["prompt"].format(
        claim=claim,
        html_classes=HTML_CLASSES,
        ori_context=ori_context or "unknown",
    )

    schema_str = json.dumps(AGENT_SCHEMA)

    cmd = [
        CLAUDE_BIN,
        "-p",
        prompt_text,
        "--output-format", "stream-json",
        "--system-prompt", agent["system"],
        "--json-schema", schema_str,
        "--no-session-persistence",
    ]

    log(f"  [{agent_label}] Starting claude -p (cwd={BASE.name}/)")
    t0 = time.time()
    tool_calls = 0
    final_result = None

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(BASE),
        env=CLEAN_ENV,
    )

    # Drain stderr in background
    stderr_lines: list[str] = []

    def drain_stderr():
        for line in proc.stderr:
            line = line.rstrip()
            if line:
                stderr_lines.append(line)

    stderr_thread = threading.Thread(target=drain_stderr, daemon=True)
    stderr_thread.start()

    try:
        for raw_line in proc.stdout:
            raw_line = raw_line.rstrip()
            if not raw_line:
                continue

            try:
                event = json.loads(raw_line)
            except json.JSONDecodeError:
                continue

            etype = event.get("type", "")

            if etype == "assistant":
                for block in event.get("message", {}).get("content", []):
                    if block.get("type") == "tool_use":
                        tool_calls += 1
                        tool_name = block.get("name", "?")
                        inp = block.get("input", {})
                        if tool_name == "Glob":
                            log(f"  [{agent_label}] Glob: {inp.get('pattern', '?')}")
                        elif tool_name == "Read":
                            fp = inp.get("file_path", "?")
                            short = fp.replace(str(BASE) + "/", "")
                            log(f"  [{agent_label}] Read: {short}")
                        elif tool_name == "Grep":
                            log(f"  [{agent_label}] Grep: \"{inp.get('pattern', '?')}\"")
                        else:
                            log(f"  [{agent_label}] {tool_name}")

            elif etype == "result":
                final_result = event
                cost = event.get("total_cost_usd", event.get("cost_usd", 0))
                elapsed = time.time() - t0
                log(f"  [{agent_label}] Done: {elapsed:.1f}s | ${cost:.4f} | {tool_calls} tools")

        proc.wait(timeout=10)

    except Exception as e:
        proc.kill()
        raise RuntimeError(f"[{agent_label}] Stream error: {e}")

    if stderr_lines:
        log(f"  [{agent_label}] stderr: {' | '.join(stderr_lines[:3])}")

    if proc.returncode != 0:
        raise RuntimeError(
            f"[{agent_label}] claude exited {proc.returncode}: {' '.join(stderr_lines[:3])}"
        )

    if not final_result:
        raise RuntimeError(f"[{agent_label}] No result event received")

    return extract_structured(final_result, agent_label)


# ---------------------------------------------------------------------------
# Verdict synthesis agent
# ---------------------------------------------------------------------------

VERDICT_SYSTEM = """\
You are the Verdict Synthesizer for the Alignment Paradox Crucible. You receive \
the results of 7 epistemic agent tests and synthesize them into a final verdict. \
Do NOT search any files. Produce your answer from the provided test results only."""


def build_verdict_prompt(claim: str, results: dict[int, dict]) -> str:
    """Build the verdict agent's prompt from accumulated test results."""
    lines = [f'Synthesize the final verdict for this claim: "{claim}"', "", "TEST RESULTS:"]
    for num in sorted(results.keys()):
        meta = TEST_META[num]
        r = results[num]
        lines.append(
            f"T{num} {meta['agent']} ({meta['name']}): "
            f"status={r.get('status', '?')} | label={r.get('label', '?')} | "
            f"summary={r.get('summary', '?')}"
        )
        # Include body_html so verdict agent can find artifact references
        body = r.get("body_html", "")
        if body:
            lines.append(f"  body_excerpt: {body[:500]}")
    lines.append("")
    lines.append(
        "Produce the final verdict JSON with:\n"
        "- classification.type: one of postulate, definition, theorem-candidate, hypothesis, proposition\n"
        "- classification.label: SHORT uppercase label (e.g. 'POSTULATE', 'THEOREM-CANDIDATE')\n"
        "- classification.desc: one sentence description\n"
        "- epistemic_status.verdict: a_priori, a_posteriori, or mixed\n"
        "- epistemic_status.route: which agent pipeline applies (e.g. 'Tribunal' for a_priori)\n"
        "- confidence: 0.0-1.0 overall confidence\n"
        "- validity: valid, plausible, contradicted, or not evaluable\n"
        "- related_artifacts: list of {id, title, agent, score} extracted from the test results above\n"
        "- recommendation: what should happen next with this claim\n"
        "- missing_infrastructure: list of KB elements that should exist but don't"
    )
    return "\n".join(lines)


def call_verdict_agent(claim: str, results: dict[int, dict]) -> dict:
    """Run the verdict synthesis as a claude -p subprocess."""
    prompt = build_verdict_prompt(claim, results)
    schema_str = json.dumps(VERDICT_SCHEMA)

    cmd = [
        CLAUDE_BIN,
        "-p",
        prompt,
        "--output-format", "stream-json",
        "--system-prompt", VERDICT_SYSTEM,
        "--json-schema", schema_str,
        "--no-session-persistence",
        "--max-turns", "1",
    ]

    log("  [Verdict] Starting synthesis (no tool use)")
    t0 = time.time()
    final_result = None

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(BASE),
        env=CLEAN_ENV,
    )

    stderr_lines: list[str] = []

    def drain_stderr():
        for line in proc.stderr:
            line = line.rstrip()
            if line:
                stderr_lines.append(line)

    stderr_thread = threading.Thread(target=drain_stderr, daemon=True)
    stderr_thread.start()

    try:
        for raw_line in proc.stdout:
            raw_line = raw_line.rstrip()
            if not raw_line:
                continue
            try:
                event = json.loads(raw_line)
            except json.JSONDecodeError:
                continue

            if event.get("type") == "result":
                final_result = event
                cost = event.get("total_cost_usd", event.get("cost_usd", 0))
                elapsed = time.time() - t0
                log(f"  [Verdict] Done: {elapsed:.1f}s | ${cost:.4f}")

        proc.wait(timeout=10)

    except Exception as e:
        proc.kill()
        raise RuntimeError(f"[Verdict] Stream error: {e}")

    if proc.returncode != 0:
        raise RuntimeError(f"[Verdict] claude exited {proc.returncode}")

    if not final_result:
        raise RuntimeError("[Verdict] No result event received")

    return extract_structured(final_result, "Verdict")


# ---------------------------------------------------------------------------
# Error fallback for failed agents
# ---------------------------------------------------------------------------

def error_result(num: int, error_msg: str) -> dict:
    """Produce a fallback test result when an agent fails."""
    return {
        "status": "fail",
        "label": "Agent error",
        "body_html": (
            f'<div class="finding"><span class="finding-label">Error:</span> '
            f'{error_msg}</div>'
        ),
        "summary": f"Agent failed: {error_msg[:100]}",
    }


# ---------------------------------------------------------------------------
# Evaluation generator — yields SSE events
# ---------------------------------------------------------------------------

def run_evaluation(claim: str):
    """Generator that yields (event_type, event_data) tuples as agents complete."""
    results: dict[int, dict] = {}
    total_t0 = time.time()

    log(f"EVALUATE: \"{claim[:80]}{'...' if len(claim) > 80 else ''}\"")

    with ThreadPoolExecutor(max_workers=5) as pool:
        # ---- Wave 1: T1, T2, T3, T4, T7 in parallel ----
        log("  Wave 1: T1 Logos, T2 Axiom, T3 Propo, T4 Ori, T7 Synthesis")
        wave1_nums = [1, 2, 3, 4, 7]
        futures = {
            pool.submit(call_agent, num, claim): num
            for num in wave1_nums
        }

        for future in as_completed(futures):
            num = futures[future]
            meta = TEST_META[num]
            try:
                result = future.result()
                results[num] = result
                log(f"  Wave 1 complete: T{num} {meta['agent']} -> {result.get('status', '?')}")
            except Exception as e:
                log(f"  Wave 1 FAILED: T{num} {meta['agent']} -> {e}")
                result = error_result(num, str(e))
                results[num] = result

            yield ("test", {
                "num": num,
                "name": meta["name"],
                "agent": meta["agent"],
                "status": result["status"],
                "label": result["label"],
                "body_html": result["body_html"],
                "summary": result["summary"],
            })

        wave1_elapsed = time.time() - total_t0
        log(f"  Wave 1 done: {wave1_elapsed:.1f}s")

        # ---- Wave 2: T5, T6 (need Ori's verdict) ----
        ori_summary = results.get(4, {}).get("summary", "unknown")
        # Extract classification keyword from Ori's summary
        ori_context = ori_summary
        log(f"  Wave 2: T5 Tribunal, T6 Hypothex (Ori says: {ori_context[:60]})")

        futures2 = {
            pool.submit(call_agent, 5, claim, ori_context=ori_context): 5,
            pool.submit(call_agent, 6, claim, ori_context=ori_context): 6,
        }

        for future in as_completed(futures2):
            num = futures2[future]
            meta = TEST_META[num]
            try:
                result = future.result()
                results[num] = result
                log(f"  Wave 2 complete: T{num} {meta['agent']} -> {result.get('status', '?')}")
            except Exception as e:
                log(f"  Wave 2 FAILED: T{num} {meta['agent']} -> {e}")
                result = error_result(num, str(e))
                results[num] = result

            yield ("test", {
                "num": num,
                "name": meta["name"],
                "agent": meta["agent"],
                "status": result["status"],
                "label": result["label"],
                "body_html": result["body_html"],
                "summary": result["summary"],
            })

        wave2_elapsed = time.time() - total_t0
        log(f"  Wave 2 done: {wave2_elapsed:.1f}s total")

    # ---- Wave 3: Verdict synthesis (single call, outside pool) ----
    log("  Wave 3: Verdict synthesis")
    try:
        verdict = call_verdict_agent(claim, results)
        log(f"  Verdict: {verdict.get('classification', {}).get('label', '?')} | "
            f"{verdict.get('validity', '?')} | conf={verdict.get('confidence', 0):.0%}")
    except Exception as e:
        log(f"  Verdict FAILED: {e}")
        verdict = {
            "classification": {"type": "unknown", "label": "ERROR", "desc": str(e)},
            "epistemic_status": {"verdict": "mixed", "route": "unknown"},
            "confidence": 0.0,
            "validity": "not evaluable",
            "related_artifacts": [],
            "recommendation": f"Verdict synthesis failed: {e}",
            "missing_infrastructure": [],
        }

    yield ("verdict", verdict)

    total_elapsed = time.time() - total_t0
    log(f"  TOTAL: {total_elapsed:.1f}s")

    yield ("done", {})


# ---------------------------------------------------------------------------
# HTTP handler
# ---------------------------------------------------------------------------

class CrucibleHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE), **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/crucible-live-parallel.html"
            log("GET / -> serving crucible-live-parallel.html")
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

        log(f"POST /api/evaluate -> SSE stream for: \"{claim[:60]}\"")

        # Send SSE headers
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        try:
            for event_type, event_data in run_evaluation(claim):
                msg = f"event: {event_type}\ndata: {json.dumps(event_data, ensure_ascii=False)}\n\n"
                self.wfile.write(msg.encode("utf-8"))
                self.wfile.flush()
        except BrokenPipeError:
            log("  Client disconnected during SSE stream")
        except Exception as e:
            log(f"  SSE stream error: {type(e).__name__}: {e}")
            # Try to send error event
            try:
                err_msg = f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"
                self.wfile.write(err_msg.encode("utf-8"))
                self.wfile.flush()
            except Exception:
                pass

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
    # Use ThreadingHTTPServer so SSE streaming doesn't block other requests
    from http.server import ThreadingHTTPServer

    if not Path(CLAUDE_BIN).exists() and not shutil.which("claude"):
        print(f"WARNING: claude CLI not found at {CLAUDE_BIN}", file=sys.stderr)

    arts = load_artifacts()
    log(f"Loaded {len(arts)} artifacts from {ARTIFACTS_ROOT}")
    log(f"Server: http://localhost:{PORT}")
    log(f"Claude: {CLAUDE_BIN}")
    log(f"CWD for claude: {BASE}")
    log(f"Mode: PARALLEL (7 agents, 3 waves)")
    log("Press Ctrl+C to stop\n")

    def force_exit(sig, frame):
        log("Ctrl+C — killing all child processes and exiting")
        import subprocess as _sp
        _sp.run(["pkill", "-P", str(os.getpid())], capture_output=True)
        os._exit(0)

    signal.signal(signal.SIGINT, force_exit)
    signal.signal(signal.SIGTERM, force_exit)

    server = ThreadingHTTPServer(("", PORT), CrucibleHandler)
    server.serve_forever()
