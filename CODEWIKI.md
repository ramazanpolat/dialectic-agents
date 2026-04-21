# CODEWIKI — Dialectic Agents

A technical recap of the `app/` codebase. Explains what each piece is, how the pieces fit together, and where the seams are.

---

## 1. Architecture at a glance

Three coordinated layers:

| Layer | What it is | Where |
|-------|-----------|-------|
| **Agents** | Nine autonomous Claude Code instances, each with its own `CLAUDE.md` and `artifacts/` directory | `app/<agent>/` |
| **Orchestration** | Two launch modes — single-orchestrator-with-subagents, or N-separate-Claude-CLIs | `app/run.sh`, `app/launch.sh` |
| **Evaluation UI** | A local HTTP server that bridges a browser to `claude -p`, plus static observatory snapshots | `app/crucible-server*.py`, `app/crucible*.html`, `app/dialectic-observatory-*.html`, `app/build-observatory.py` |

Communication is **file-based only**. Agents read each other's `artifacts/` directories and write to their own. There is no direct messaging, no shared process memory, no runtime coordinator. Git commits are the persistence and synchronization substrate.

---

## 2. Directory layout (`app/`)

```
app/
├── CLAUDE.md                   # Orchestrator prompt (read by run.sh's Claude session)
├── run.sh                      # Single-process orchestrator (spawns subagents via Task tool)
├── launch.sh                   # Multi-process launcher (one Claude CLI per agent)
│
├── crucible-server.py          # Local HTTP server, port 3456 — browser ↔ claude -p
├── crucible-server-parallel.py # Variant that parallelizes evaluation
├── crucible.html               # Crucible browser UI
├── crucible-live.html          # Live-streaming variant
├── crucible-live-parallel.html # Live + parallel variant
├── dashboard.html              # Artifact dashboard
│
├── build-observatory.py            # Renders observatory HTML from artifact tree
├── dialectic-observatory-live.html # Live observatory view
├── dialectic-observatory-v2.html   # Observatory v2
│
├── shared/
│   ├── PROTOCOL.md             # Artifact format, naming, communication rules
│   ├── commit-artifact.sh      # Per-artifact git commit+push helper
│   ├── topics/                 # Seed topics (input to the pipeline)
│   └── registry.md             # Master artifact registry (maintained by Watcher)
│
├── logos/     ├── axiom/     ├── propo/     ├── ori/      ├── tribunal/
├── hypothex/  ├── theorica/  ├── synthesis/ └── watcher/
│   Each agent dir contains:
│     CLAUDE.md   — agent-specific role, standards, evaluation criteria
│     artifacts/  — markdown artifacts produced by this agent
│
└── docs/                       # Specs and supplementary docs
```

---

## 3. Agent anatomy

An "agent" is not a long-running process. It is a **directory shape** interpreted by a Claude Code instance:

1. The agent's directory contains a `CLAUDE.md` — this becomes the agent's system prompt when Claude is launched in that directory.
2. The agent's `artifacts/` directory is where it writes output, and where downstream agents read from.
3. The agent is identified by directory name (`logos`, `axiom`, …). The artifact naming convention (`LOGOS-NNNN-slug.md`) carries the agent identity.

Each agent operates on exactly one input-output contract:

| Agent | Reads from | Writes to | Artifact types |
|-------|-----------|-----------|----------------|
| Logos | `shared/topics/` | `logos/artifacts/` | `primitive`, `definition` |
| Axiom | `logos/artifacts/`, `shared/topics/` | `axiom/artifacts/` | `axiom`, `postulate` |
| Propo | `logos/`, `axiom/` | `propo/artifacts/` | `proposition`, `premise` |
| Ori | `propo/artifacts/` | `ori/artifacts/` | `classification` |
| Tribunal | `ori/` (a priori), `axiom/` | `tribunal/artifacts/` | `inference-rule`, `lemma`, `theorem`, `corollary` |
| Hypothex | `ori/` (a posteriori) | `hypothex/artifacts/` | `hypothesis` |
| Theorica | `tribunal/`, `hypothex/` | `theorica/artifacts/` | `theory`, `model` |
| Synthesis | all agents | `synthesis/artifacts/` | `synthesis` |
| Watcher | all agents | `watcher/artifacts/`, `shared/registry.md` | `observation` |

---

## 4. Artifact format

Every artifact is a markdown file with YAML frontmatter. Schema (from `shared/PROTOCOL.md`):

```yaml
---
id: <AGENT>-<NNNN>        # e.g., AXIOM-0001
agent: <agent_name>
type: <artifact_type>     # from the table above
status: draft | evaluated | accepted | challenged | rejected | superseded
created: <ISO-8601>
updated: <ISO-8601>
domain: <topic_domain>
depends_on: []            # artifact IDs this derives from
confidence: <0.0-1.0>
layer: <0-13>
---

# <Title>

## Statement
## Justification
## Dependencies
## Evaluation Notes
## Lineage
```

**File naming:** `<agent>-<NNNN>-<slug>.md` (e.g., `PROPO-0005-good-faith-requires-revision-capacity.md`).

**Challenge protocol:** any agent can emit a `challenge`-type artifact against any other artifact by adding the target to `depends_on`. The challenged agent must respond with either a `superseded` update or a defense `evaluation`.

**Status lifecycle:** `draft → evaluated → accepted | challenged → superseded|rejected`.

---

## 5. Launch modes

### 5.1 `run.sh` — single orchestrator (recommended)

Starts **one** `claude` session in `app/` with `--dangerously-skip-permissions`. That session reads `app/CLAUDE.md` — the orchestrator prompt — and spawns subagents for each wave using Claude's `Task` tool. Each subagent is briefed with the exact `CLAUDE.md` + `PROTOCOL.md` paths to read before producing artifacts.

Modes:
- `./run.sh` — interactive
- `./run.sh --background` — `--print --max-turns 200`, logs to `.logs/orchestrator.log`, PID in `.pids/orchestrator.pid`
- `./run.sh --status` — counts artifacts per agent
- `./run.sh --stop` — kills the background orchestrator

The orchestrator prompt tells Claude: "This is epoch 1 unless `.logs/epoch.txt` exists with a higher number." Epoch counter is a soft convention; no hard enforcement.

### 5.2 `launch.sh` — N separate Claude instances

Launches **each agent as its own `claude` CLI process**, `cd`'d into that agent's directory (so it picks up `<agent>/CLAUDE.md` as system prompt). Each agent gets a hand-written prompt from `get_agent_prompt()` telling it what to read and what to produce.

Modes:
- `./launch.sh` — sequential interactive (one terminal, agents one-by-one)
- `./launch.sh <agent> [agent…]` — specific agents only
- `./launch.sh --parallel` — all agents as backgrounded processes, logs in `.logs/<agent>.log`, PIDs in `.pids/<agent>.pid`
- `./launch.sh --status` — PID + artifact counts per agent
- `./launch.sh --stop` — sends SIGTERM to all PID files

Parallel mode flags: `--print --dangerously-skip-permissions --max-turns 50 --verbose`.

### 5.3 When to use which

- **`run.sh`** — when you want one coherent trajectory through the pipeline, with the orchestrator enforcing wave ordering.
- **`launch.sh`** — when you want genuine parallelism (e.g., Wave 4's Tribunal + Hypothex), or you want to rerun a single agent without restarting the whole pipeline.

---

## 6. The Crucible (`crucible-server.py`)

A stdlib HTTP server (`http.server.HTTPServer`) on **port 3456**. Bridges a browser frontend (`crucible.html`, `crucible-live.html`) to `claude -p` running in the project directory so Claude can read artifacts directly while evaluating.

Key behaviors from the source:

- **Environment scrubbing:** strips `CLAUDECODE`, `CLAUDE_CODE_ENTRYPOINT`, and `ANTHROPIC_API_KEY` from the subprocess env. This prevents nesting issues (running `claude` from inside a Claude session) and forces use of the user's subscription rather than a pay-per-call API key.
- **Artifacts endpoint (`/api/artifacts`):** parses YAML frontmatter + known section patterns (`Statement`, `Executive Summary`, `Dialectical Synthesis`, `Hypothesis Structure`, `Theory Structure`, `Summary`) out of every artifact file and returns them as JSON for the UI to render.
- **Evaluation endpoint:** runs `claude -p` as a subprocess in the project root so it can `Grep`/`Read` the artifact tree, and streams progress back to the terminal (not the browser) via `log()`.
- **Static files:** uses `SimpleHTTPRequestHandler` for everything else — the HTML frontends are served straight from `app/`.

`crucible-server-parallel.py` is the parallel-evaluation variant (runs multiple `claude -p` subprocesses concurrently so multiple artifacts can be evaluated in parallel). Same port bridge pattern; different concurrency model.

---

## 7. The Observatory

Static HTML views over the artifact tree.

- **`build-observatory.py`** — scans `app/<agent>/artifacts/` and renders `dialectic-observatory-*.html`. Produces a browsable snapshot of the knowledge graph as it stands.
- **`dialectic-observatory-live.html`** — live view that fetches from the Crucible server.
- **`dialectic-observatory-v2.html`** — a second iteration of the observatory layout.
- **`dashboard.html`** — artifact-focused dashboard variant.

The observatory is read-only. It does not mutate artifacts. It exists to make the graph of produced artifacts legible during a pipeline run.

---

## 8. Shared utilities (`app/shared/`)

### `PROTOCOL.md`

The single source of truth for artifact format, naming, dependency chains, status transitions, and the challenge protocol. Every agent is instructed to read this before producing artifacts.

### `commit-artifact.sh`

Per-artifact git helper. Invoked by agents after writing each artifact file:

```bash
bash shared/commit-artifact.sh <path-to-artifact> <agent-name> "<short description>"
```

Produces a commit with the structured message:

```
[AGENT] Short description

Artifact: AGENT-NNNN-slug.md
Agent: agent-name

Co-Authored-By: ...
```

Uses `.git/dialectic.lock` to serialize concurrent git operations across parallel agents, and auto-runs `git pull --rebase` on push rejection. Never force-pushes, never amends.

### `topics/`

Seed topics. Each is a markdown file describing the thesis the pipeline should reason about. The canonical seed for this project is `TOPIC-0001-alignment-paradox.md`.

### `registry.md`

Master artifact registry. Written by the Watcher agent. Counts artifacts by agent, by status, by type. Surfaces bottlenecks (e.g., Ori has fewer classifications than Propo has propositions).

---

## 9. Git protocol

The pipeline treats git as part of its state machine, not as afterthought versioning:

1. **One commit per artifact.** Agents commit and push immediately after writing each artifact, via `shared/commit-artifact.sh`. This creates a fine-grained history where each commit maps to one unit of epistemic work.
2. **Concurrent safety.** The lock file + rebase-on-reject makes concurrent agents safe. Parallel launches don't collide.
3. **Epoch summaries.** After all seven waves complete, the orchestrator emits a summary commit with per-type counts (definitions, axioms, propositions, classifications, theorems, hypotheses, theories, syntheses).
4. **No force push, no amend.** Hard rule in `CLAUDE.md` and `PROTOCOL.md`.

---

## 10. Configuration & environment

- **Python:** stdlib-only for the Crucible server (no external deps).
- **Shell:** launch/run scripts are Bash 3 compatible (Apple's default `/bin/bash`) — no associative arrays, no `${VAR^^}`.
- **Claude CLI:** resolved via `shutil.which("claude")` or falls back to `~/.local/bin/claude`.
- **Ports:** Crucible server is hard-coded to 3456.
- **Runtime state:** `.pids/` and `.logs/` (both gitignored).

---

## 11. Where to start reading

If you're new to this repo, read in this order:

1. `app/CLAUDE.md` — the orchestrator prompt explains the whole pipeline in the language of waves and subagent spawns.
2. `app/shared/PROTOCOL.md` — the artifact format and communication rules.
3. One agent's `CLAUDE.md` (e.g., `app/logos/CLAUDE.md`) — to see what an agent role looks like.
4. `app/run.sh` — to see how the orchestrator is actually launched.
5. `app/crucible-server.py` — to see the browser-bridge shape.
6. `presentation/the-crucible-spec-20260222-1839.md` — the written specification.
