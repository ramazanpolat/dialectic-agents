---
id: AXIOM-0002
agent: axiom
type: axiom
status: accepted
created: 2026-02-22T15:19:00Z
updated: 2026-02-22T15:19:00Z
domain: universal
depends_on: [AXIOM-0001]
confidence: 0.98
layer: 2
---

# Axiom: Law of Non-Contradiction

## Statement
A proposition cannot be both true and false at the same time and in the same respect. (¬(P ∧ ¬P))

## Justification
If contradictions are permitted, then any proposition can be proven true (ex falso quodlibet), and the entire system collapses into triviality. Without non-contradiction, no distinction between true and false is possible.

## Self-Evidence Test
**PASS** — Accepting contradictions makes all reasoning trivial.

## Independence Test
**PASS** — While related to the Law of Identity, it is not derivable from it alone. Identity says A=A; non-contradiction says you cannot assert both P and ¬P.

## Consistency Test
**PASS** — It is the axiom that makes consistency itself possible.

## Alternative
Paraconsistent logics weaken this axiom, allowing some contradictions without explosion. This is a legitimate alternative axiom set for specific domains (e.g., modeling inconsistent databases), but it comes at the cost of deductive power.

## Dependencies
- AXIOM-0001 (Law of Identity — identity is presupposed by the concept of "the same proposition")

## Evaluation Notes
Confidence 0.98 rather than 1.0 because paraconsistent logics demonstrate that weakening this axiom is coherent in some contexts. The axiom is near-universal but not absolutely without alternative.

## Lineage
Classical logic. Aristotle, Metaphysics IV.
