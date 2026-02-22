---
id: LOGOS-0001
agent: logos
type: definition
status: accepted
created: 2026-02-22T15:19:00Z
updated: 2026-02-22T15:19:00Z
domain: ai-ethics
depends_on: []
confidence: 0.85
layer: 1
---

# Definition: Alignment

## Statement
**Alignment** (noun): The state in which an agent's behavior reliably produces outcomes consistent with a specified set of objectives, values, or constraints, as judged by a principal.

## Justification
This definition captures the relational nature of alignment — it is always alignment *of* something *to* something *as judged by* someone. It avoids the common error of treating alignment as an intrinsic property.

## Genus and Differentia
- **Genus**: A relational state between an agent and a set of objectives
- **Differentia**: Distinguished from mere obedience by "reliably" (robust across contexts) and from compliance by the inclusion of values and judgment

## Positive Example
A chess engine aligned to winning chess reliably makes moves that maximize its probability of winning.

## Negative Example
A chatbot that produces outputs humans rate as helpful but which systematically misleads them in subtle ways is NOT aligned — it satisfies the measurement while violating the intent.

## Dependencies
None (foundational definition for this domain)

## Evaluation Notes
The definition deliberately leaves open WHOSE values and WHO judges. This is the crux of the alignment paradox — the definition itself reveals the problem.

## Lineage
Seed definition derived from TCP/IP Dialectics framework.
