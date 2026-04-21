---
id: ORI-0002
agent: ori
type: classification
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: ["PROPO-0002", "LOGOS-0001", "LOGOS-0002", "AXIOM-0004", "AXIOM-0011"]
confidence: 0.85
layer: 3
---

# Classification of PROPO-0002: The Incoherent Target Proposition

## Statement
There exists no coherent, well-defined set of "human values" (LOGOS-0002) to which an AI system could in principle be aligned (LOGOS-0001), because individual humans are not reliably aligned with their own stated values (AXIOM-0004) and the aggregation of individual values into collective values is not a well-defined operation (AXIOM-0011).

## Classification
- **Verdict**: mixed
- **Route To**: SPLIT
- **Negation Test**: Negating the proposition yields: "There exists a coherent, well-defined set of human values to which an AI system could in principle be aligned." This is not a logical contradiction -- it is conceivable that such a set exists. It would require either solving the self-knowledge problem (contradicting AXIOM-0004) or finding a privileged aggregation procedure (contradicting AXIOM-0011 / Arrow's theorem). The negation is logically coherent, though the framework treats it as implausible. **Result**: Not a priori by negation test.
- **Conceivability Test**: Can we imagine a world where a coherent human-values target exists? Yes: (a) a world where all humans hold identical values (eliminates the aggregation problem), or (b) a world where humans have perfect self-knowledge (eliminates the opacity problem), or (c) a world where a natural aggregation procedure exists that all parties accept. These are conceivable possible worlds, even if they do not describe our world. **Result**: Contingent -- the proposition describes our actual world, not all possible worlds.
- **Justification Test**: What settles this? Two different kinds of evidence are needed. (1) The formal component -- Arrow's impossibility theorem -- is a mathematical proof that can be verified a priori: no aggregation procedure satisfying certain fairness axioms exists. This is a priori within the framework of social choice theory. (2) The empirical component -- that humans are not reliably aligned with their own values (AXIOM-0004) -- is an empirical claim about human psychology requiring evidence from cognitive science. **Result**: Both formal proof and empirical observation are needed.
- **If Mixed**:
  - A priori component: "If individual preference orderings are diverse and unrestricted, then no aggregation procedure satisfying non-dictatorship, Pareto efficiency, and independence of irrelevant alternatives exists." This is Arrow's impossibility theorem -- a mathematical result that is a priori within its axiomatic framework.
  - A posteriori component: "Individual humans are not reliably aligned with their own stated values" (AXIOM-0004) and "Individual preference orderings in the actual human population are in fact diverse and unrestricted in the relevant sense" (empirical premise for Arrow's theorem to apply). Both require empirical evidence.

## Justification
PROPO-0002 attacks the coherence of the alignment target on two independent fronts, one formal and one empirical.

The **formal front** (via AXIOM-0011) invokes Arrow's impossibility theorem. Arrow's theorem is itself a priori: it is a mathematical proof within the axioms of social choice theory. If we accept Arrow's axioms (non-dictatorship, Pareto, IIA, unrestricted domain), the impossibility of a well-defined aggregation function is a logical necessity. This component is a priori.

However, the *application* of Arrow's theorem to the alignment problem requires an empirical premise: that human value profiles are in fact sufficiently diverse to trigger the theorem's conditions. If all humans held identical values, the aggregation problem would be trivial. The diversity premise is empirical.

The **empirical front** (via AXIOM-0004) asserts that humans misreport their own values. This is purely an empirical claim grounded in cognitive science -- the evidence comes from studies showing divergence between stated preferences, revealed preferences, and predicted preferences (Kahneman, Haidt, etc.).

The proposition's force comes from the compounding of these two independently insufficient but jointly devastating problems. This is what makes it genuinely mixed: neither the formal impossibility alone (which requires the diversity premise) nor the empirical observation alone (which could be overcome if aggregation were well-defined) is sufficient, but together they close the escape routes.

## Dependencies
- PROPO-0002 (the proposition being classified)
- LOGOS-0001 (alignment), LOGOS-0002 (values)
- AXIOM-0004 (humans misaligned with selves), AXIOM-0011 (irreducible value pluralism / Arrow's theorem)

## Evaluation Notes
Confidence is 0.85. The mixed classification is clear because the proposition explicitly combines a formal impossibility result (a priori) with an empirical observation about human cognition (a posteriori). The only source of uncertainty is whether the a priori component (Arrow's theorem) is strong enough on its own to carry the proposition without the empirical component -- i.e., whether the diversity of human values is itself an a priori truth about any sufficiently complex population of agents. If so, the proposition shifts toward a priori. But diversity of values appears to be contingent (it could have been otherwise), so the mixed classification holds.

Routing: The a priori component (Arrow's theorem applied to alignment) should go to Tribunal for formal proof. The a posteriori component (humans misreport values; human values are diverse) should go to Hypothex for empirical hypothesis structuring.

## Lineage
AXIOM-0004 (self-misalignment, empirical) + AXIOM-0011 (Arrow's theorem, formal) --> PROPO-0002 --> ORI-0002 (classification: mixed)
