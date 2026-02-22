---
id: PROPO-0002
agent: propo
type: proposition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0001, LOGOS-0002, AXIOM-0004, AXIOM-0011]
confidence: 0.85
layer: 3
---

# The Incoherent Target Proposition

## Statement
There exists no coherent, well-defined set of "human values" (LOGOS-0002) to which an AI system could in principle be aligned (LOGOS-0001), because individual humans are not reliably aligned with their own stated values (AXIOM-0004) and the aggregation of individual values into collective values is not a well-defined operation (AXIOM-0011).

## Logical Form
Let HV be "human values" as a single coherent target, A(i) be the actual values of individual i, S(i) be the stated values of individual i, and Agg be any aggregation function.

(1) For all i: A(i) != S(i) [from AXIOM-0004]
(2) For all Agg: ~WellDefined(Agg({A(i) for all i})) [from AXIOM-0011, Arrow's theorem]
(3) Therefore: ~Exists(HV such that HV is coherent AND HV is well-defined AND Aligned(AI, HV) is evaluable)

## Categorization
- **Analytic/Synthetic**: synthetic -- the claim combines an empirical observation about human self-knowledge with a formal impossibility result about preference aggregation.
- **Necessary/Contingent**: necessary (conditional) -- given the truth of AXIOM-0004 and AXIOM-0011, the conclusion follows necessarily. The contingency lies in whether AXIOM-0004 and AXIOM-0011 hold.

## Justification
The proposition attacks the very concept of "aligning AI to human values" by showing the target is ill-defined in two independent ways:

1. **The individual level** (AXIOM-0004): Each human's "true values" are not accessible through their stated values. The values humans articulate, believe they hold, and reveal through behavior are three distinct sets. So even if we could align to one human's values, we do not know what those values are.

2. **The collective level** (AXIOM-0011): Even if we could perfectly know each individual's values, combining them into a single "human values" set is formally impossible without an arbitrary choice of aggregation procedure, and different procedures yield incompatible results (Arrow's impossibility theorem).

These two problems are independent and compound: the first means the inputs to aggregation are unreliable; the second means aggregation is undefined even with perfect inputs.

## Dependencies
- LOGOS-0001 (alignment -- the concept being problematized)
- LOGOS-0002 (values -- the supposed alignment target)
- AXIOM-0004 (humans misaligned with themselves -- undermines individual-level input)
- AXIOM-0011 (irreducible value pluralism -- undermines collective-level aggregation)

## Evaluation Notes
**Potential counterexample**: One could argue that "human values" need not be perfectly coherent to serve as an alignment target -- approximate alignment to an imperfect target may be better than no alignment at all. This is a pragmatic objection, and it has force. The proposition claims there is no coherent target *in principle*, but practical alignment may not require principled coherence.

**Potential weakness**: The proposition may prove too much. If there is no coherent target, then the very concept of alignment (LOGOS-0001) is meaningless in the human-values domain. But we seem to have intuitive judgments about which AI behaviors are "more aligned" and "less aligned." The proposition may need to be refined: perhaps the target is not a point but a region, and alignment means staying within the region rather than hitting a point.

**Negation**: "There exists a coherent, well-defined set of human values to which an AI system could in principle be aligned." This would require either (a) solving the self-knowledge problem (contradicting AXIOM-0004) or (b) finding a privileged aggregation procedure (contradicting AXIOM-0011 / Arrow's theorem).

## Lineage
LOGOS-0001 + LOGOS-0002 --> AXIOM-0004 + AXIOM-0011 --> PROPO-0002
