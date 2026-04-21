# Alignment Paradox — Dialectic Agents

A multi-agent epistemological pipeline that produces, evaluates, and evolves knowledge artifacts about the **Alignment Paradox** — the thesis that alignment is a *process* (dialectic revision under operational coherence), not a static specification.

The repo holds both sides of this work:

```
.
├── app/            # Runnable code — the dialectic pipeline + Crucible server + observatory
└── presentation/   # Slides, article, spec, choreography notes, conversation dumps
```

## app/ — what runs

Nine autonomous agents, each a Claude Code CLI instance with its own `CLAUDE.md` and `artifacts/` directory, communicating only through markdown artifacts on disk. An HTTP server (**the Crucible**) bridges a browser UI to `claude -p` for evaluation workflows.

| Agent | Layer | Role |
|-------|-------|------|
| **Logos** | 0–1 | Primitive terms & definitions |
| **Axiom** | 2 | Axioms & postulates |
| **Propo** | 3–4 | Propositions & premises |
| **Ori** | Router | A priori / a posteriori classifier |
| **Tribunal** | 5–8 | Inference, lemmas, theorems, corollaries |
| **Hypothex** | 9 | Hypotheses |
| **Theorica** | 10–11 | Theories & models |
| **Synthesis** | — | Dialectical integration |
| **Watcher** | — | Observer & registry maintainer |

### Pipeline flow

```
Seed Topic
    ↓
  LOGOS → AXIOM → PROPO → ORI
                           ╱ ╲
                     TRIBUNAL HYPOTHEX
                           ╲ ╱
                        THEORICA
                           ↓
                       SYNTHESIS  →  (re-enters as new proposition)

  WATCHER observes everything, maintains shared/registry.md
```

## Quick start

```bash
cd app

# Option A — one orchestrator spawns subagents via the Task tool (recommended)
./run.sh                 # interactive
./run.sh --background    # non-interactive, logs to .logs/orchestrator.log
./run.sh --status        # per-agent artifact counts

# Option B — launch each agent as its own claude CLI instance
./launch.sh              # sequential, interactive
./launch.sh --parallel   # all agents in the background
./launch.sh logos axiom  # specific agents only
./launch.sh --status     # running PIDs + artifact counts
./launch.sh --stop

# Option C — browse artifacts through the Crucible UI
python3 crucible-server.py          # serves crucible.html on :3456
python3 crucible-server-parallel.py # parallel-evaluation variant
python3 build-observatory.py        # generates dialectic-observatory-*.html
```

## presentation/ — what's delivered

Slide decks, the written article, the Crucible spec, and the supporting notes used to present the work.

| File | Purpose |
|------|---------|
| `alignment-paradoksu-makale-20260222.md` | The article (Turkish) |
| `the-crucible-spec-20260222-1839.md` | Crucible specification |
| `the-protocol-presentation-*.html` | Slide deck (EN + TR) |
| `the-protocol-v2-20260223-1430.html` | Slide deck v2 |
| `the-protocol-slides-ascii-*.md` | Slides as markdown |
| `sunum-notlari-*.md`, `yapay-zeka-sunum-*.md` | Presentation notes & choreography |
| `dialectic-agents-*.md`, `dialectic-observatory-*.{md,html}` | Conversation / observatory dumps |

## Deeper references

- `CODEWIKI.md` — detailed code recap (architecture, each module, how pieces fit)
- `app/CLAUDE.md` — orchestrator instructions (how Claude runs the pipeline)
- `app/shared/PROTOCOL.md` — artifact format, naming, inter-agent communication rules
- Each `app/<agent>/CLAUDE.md` — that agent's role, quality standards, evaluation criteria

## License

See `LICENSE`.
