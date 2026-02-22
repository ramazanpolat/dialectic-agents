# Dialectic Agents — Shared Communication Protocol

## Overview

This directory contains autonomous dialectic agents that produce, evaluate, and evolve epistemological artifacts. Each agent operates in its own directory, reads from other agents' `artifacts/` folders, and writes to its own `artifacts/` folder.

## Directory Structure

```
dialectic-agents/
├── shared/              # Protocol spec, seed topics, shared context
│   ├── PROTOCOL.md      # This file
│   ├── topics/          # Seed topics to reason about (input)
│   └── registry.md      # Master artifact registry (maintained by Watcher)
├── logos/               # Agent Logos — Definitions & Primitives
├── axiom/               # Agent Axiom — Axioms & Postulates
├── propo/               # Agent Propo — Propositions & Premises
├── ori/                 # Agent Ori — A Priori / A Posteriori Classifier
├── tribunal/            # Agent Tribunal — Inference, Lemmas, Theorems
├── hypothex/            # Agent Hypothex — Hypotheses (empirical branch)
├── theorica/            # Agent Theorica — Theories & Models
├── synthesis/           # Agent Synthesis — Dialectical Integration
└── watcher/             # Agent Watcher — Observer & Orchestrator
```

## Artifact Format

Every artifact is a markdown file following this exact template:

```markdown
---
id: <AGENT>-<NNNN>          # e.g., AXIOM-0001
agent: <agent_name>          # producing agent
type: <artifact_type>        # see types below
status: draft | evaluated | accepted | challenged | rejected | superseded
created: <ISO-8601>
updated: <ISO-8601>
domain: <topic_domain>       # e.g., "ethics", "consciousness", "governance"
depends_on: []               # list of artifact IDs this derives from
confidence: <0.0-1.0>        # agent's self-assessed confidence
layer: <0-13>                # epistemological layer number
---

# <Title>

## Statement
<The core content of the artifact>

## Justification
<Why this artifact exists / how it was derived>

## Dependencies
<What prior artifacts or axioms this depends on>

## Evaluation Notes
<Self-assessment, known weaknesses, open questions>

## Lineage
<Full chain: which artifacts led to this one>
```

## Artifact Types

| Type | Produced By | Layer |
|------|------------|-------|
| `primitive` | Logos | 0 |
| `definition` | Logos | 1 |
| `axiom` | Axiom | 2 |
| `postulate` | Axiom | 2 |
| `proposition` | Propo | 3 |
| `premise` | Propo | 4 |
| `classification` | Ori | — |
| `inference-rule` | Tribunal | 5 |
| `lemma` | Tribunal | 6 |
| `theorem` | Tribunal | 7 |
| `corollary` | Tribunal | 8 |
| `hypothesis` | Hypothex | 9 |
| `theory` | Theorica | 10 |
| `model` | Theorica | 11 |
| `synthesis` | Synthesis | — |
| `evaluation` | Any agent | — |
| `challenge` | Any agent | — |
| `observation` | Watcher | — |

## Artifact File Naming

```
<agent>-<NNNN>-<short-slug>.md
```

Examples:
- `LOGOS-0001-define-consciousness.md`
- `AXIOM-0001-law-of-identity.md`
- `ORI-0001-classify-axiom-0001.md`
- `PROPO-0001-consciousness-requires-substrate.md`

## Inter-Agent Communication

Agents communicate ONLY through artifacts. There is no direct messaging.

### Reading Protocol
- Every agent MUST scan other agents' `artifacts/` directories for new or updated files
- Agents should process artifacts in chronological order (by `created` timestamp)
- When an agent processes another agent's artifact, it MUST produce a response artifact referencing the original via `depends_on`

### Dependency Chain (Normal Flow)

```
[Seed Topic]
    → Logos (defines terms)
    → Axiom (establishes axioms using those definitions)
    → Propo (generates propositions from axioms)
    → Ori (classifies each proposition as a priori or a posteriori)
    → Tribunal (proves theorems from a priori propositions)
    → Hypothex (generates hypotheses from a posteriori propositions)
    → Theorica (builds theories from confirmed hypotheses + theorems)
    → Synthesis (integrates across the full chain)
```

### Challenge Protocol
Any agent can challenge any other agent's artifact by producing a `challenge` type artifact:
```
depends_on: ["AXIOM-0003"]
type: challenge
```
The challenged agent MUST respond with either:
- An updated artifact (status: `superseded` on the original)
- A defense artifact (type: `evaluation`, reaffirming the original)

### Status Transitions
```
draft → evaluated → accepted
draft → evaluated → challenged → accepted | rejected | superseded
accepted → challenged → superseded (if challenge succeeds)
```

## Evaluation Criteria

Each agent evaluates artifacts using criteria specific to its domain, but all share:

1. **Internal Consistency** — Does it contradict itself?
2. **External Consistency** — Does it contradict accepted artifacts?
3. **Necessity** — Is it needed? Does it add something?
4. **Clarity** — Is it unambiguous?
5. **Minimality** — Is it the simplest form that works?
6. **Traceability** — Can you follow the lineage back to foundations?
