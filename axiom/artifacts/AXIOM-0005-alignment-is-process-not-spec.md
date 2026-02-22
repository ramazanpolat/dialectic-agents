---
id: AXIOM-0005
agent: axiom
type: postulate
status: accepted
created: 2026-02-22T15:19:00Z
updated: 2026-02-22T15:19:00Z
domain: ai-ethics
depends_on: [LOGOS-0001, LOGOS-0004, AXIOM-0003, AXIOM-0004]
confidence: 0.82
layer: 2
---

# Postulate: Alignment Is a Process Problem, Not a Specification Problem

## Statement
Because human values are not static (AXIOM-0003) and humans are not reliably aligned with their own values (AXIOM-0004), AI alignment cannot be achieved by encoding a fixed set of values into a system. Alignment must instead be achieved through a continuous process of dialectical value discovery where humans and AI reason together.

## Justification
If the target moves (values evolve) and the map is unreliable (humans misreport their own values), then no static specification can solve the problem. The only viable approach is a protocol — a process that can continuously track, correct, and evolve. The dialectical protocol is proposed as that process.

## Classification: Postulate (not Axiom)
This is the central thesis of the TCP/IP Dialectics framework. It is derived from AXIOM-0003 and AXIOM-0004 but also makes a constructive claim (dialectics is the answer) that goes beyond what those postulates strictly entail.

## Self-Evidence Test
**FAIL as axiom, PASS as derived postulate** — This is not self-evident. It is a conclusion drawn from the prior postulates plus the additional claim that dialectics is the right process. Someone could accept AXIOM-0003 and AXIOM-0004 but propose a different solution.

## Independence Test
**PARTIAL** — Partially derivable from AXIOM-0003 + AXIOM-0004 (the "not specification" part). The "dialectics is the answer" part is independent.

## What Changes If This Postulate Is False
If alignment CAN be achieved by specification (despite evolving values and human self-misalignment), then:
- The dialectical infrastructure is unnecessary overhead
- A sufficiently good snapshot of values, with a correction mechanism, might suffice
- RLHF-style approaches might be adequate after all

## Alternative Postulate
"Alignment can be achieved through iterative specification refinement (RLHF, constitutional AI) without requiring full dialectical infrastructure." This is the mainstream AI safety position.

## Dependencies
- LOGOS-0001 (alignment), LOGOS-0004 (dialectics)
- AXIOM-0003, AXIOM-0004

## Evaluation Notes
Confidence 0.82 — lower than the prior postulates because this makes a constructive claim (proposing a solution) rather than just identifying a problem. The problem diagnosis (AXIOM-0003, 0004) is stronger than the proposed solution.

## Lineage
TCP/IP Dialectics framework — "Alignment is not a specification problem; it is a process problem."
