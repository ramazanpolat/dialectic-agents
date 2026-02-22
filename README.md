# Dialectic Agents System

## Architecture

A multi-agent epistemological pipeline where autonomous agents produce, evaluate, and evolve knowledge artifacts across the full stack of truth assessment.

## Agents

| Agent | Layer | Role | Depends On |
|-------|-------|------|-----------|
| **Logos** | 0-1 | Primitive terms & definitions | Seed topics |
| **Axiom** | 2 | Axioms & postulates | Logos |
| **Propo** | 3-4 | Propositions & premises | Logos, Axiom |
| **Ori** | Router | A priori / a posteriori classifier | Propo |
| **Tribunal** | 5-8 | Inference, lemmas, theorems, corollaries | Axiom, Propo, Ori (a priori) |
| **Hypothex** | 9 | Hypotheses | Propo, Ori (a posteriori) |
| **Theorica** | 10-11 | Theories & models | Tribunal, Hypothex |
| **Synthesis** | — | Dialectical integration | All agents |
| **Watcher** | — | Observer & orchestrator | All agents |

## Pipeline Flow

```
Seed Topic
    ↓
  LOGOS (defines terms)
    ↓
  AXIOM (establishes foundations)
    ↓
  PROPO (generates propositions)
    ↓
  ORI (classifies: a priori vs a posteriori)
   ╱ ╲
  ↓   ↓
TRIBUNAL  HYPOTHEX
(proves)  (tests)
  ↓   ↓
  THEORICA (builds theories)
    ↓
  SYNTHESIS (resolves contradictions)
    ↓
  [Re-enters pipeline as new proposition]

  WATCHER (observes everything, maintains registry)
```

## Running an Agent

Each agent directory contains a `CLAUDE.md` that defines the agent's behavior. To run an agent:

```bash
cd dialectic-agents/<agent-name>
claude --print-system-prompt  # verify CLAUDE.md is loaded
# Then give the agent a topic or let it process existing artifacts
```

## Starting the System

1. Place a seed topic in `shared/topics/` as a markdown file
2. Start Logos first (it has no upstream dependencies)
3. Start remaining agents — they will process artifacts as they appear
4. Start Watcher last (or concurrently) to monitor the system

## Communication Protocol

See `shared/PROTOCOL.md` for the full artifact format, naming conventions, and inter-agent communication rules.
