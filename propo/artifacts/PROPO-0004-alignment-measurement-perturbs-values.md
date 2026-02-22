---
id: PROPO-0004
agent: propo
type: proposition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0001, LOGOS-0002, LOGOS-0007, AXIOM-0009, AXIOM-0010, AXIOM-0013]
confidence: 0.86
layer: 3
---

# The Alignment Heisenberg Proposition

## Statement
Any attempt to measure, formalize, or specify (LOGOS-0007) the values (LOGOS-0002) of a human agent for the purpose of alignment (LOGOS-0001) changes the values it seeks to capture, such that the resulting specification is a specification of the values-as-measured rather than the values-as-lived, and these two are not identical.

## Logical Form
Let V_lived be values as actually operative in an agent's behavior, V_measured be values as captured by a measurement process M, and spec(V_measured) be the resulting specification.

For all agents a, for all measurement processes M:
M(V_lived(a)) = V_measured(a) AND V_measured(a) != V_lived(a)

Therefore:
spec(V_measured(a)) != spec(V_lived(a)) -- even if specification were not lossy (AXIOM-0013), the input is already distorted.

## Categorization
- **Analytic/Synthetic**: synthetic -- the claim that measurement changes values is an empirical claim about the relationship between observation and human cognition, not derivable from definitions alone.
- **Necessary/Contingent**: contingent -- it is conceivable that values could be measured without perturbation (e.g., through purely behavioral observation with no awareness by the subject). The proposition claims this is not achievable in practice for alignment-relevant measurement.

## Justification
This proposition synthesizes two axioms into a specific claim about the alignment process:

1. **AXIOM-0009 (Epistemic Opacity)**: Values are partially tacit and not fully accessible to any observer. This means any measurement process must rely on proxies (stated preferences, revealed preferences, behavioral patterns). These proxies are not the values themselves.

2. **AXIOM-0010 (Alignment Measurement Problem)**: The act of measuring or specifying values changes them. The reflexive distortion, value crystallization, and optimization pressure described in AXIOM-0010 all operate to create a gap between values-as-lived and values-as-measured.

3. **AXIOM-0013 (Specification Is Lossy)**: Even if the measurement were perfect, the specification would lose information. But this proposition makes the stronger claim: the measurement is not perfect to begin with, because measurement itself perturbs the target.

The compound effect: values are opaque (hard to see), reactive (change when observed), and resist formalization (lose information when specified). Each of these three barriers is independently sufficient to prevent perfect alignment-by-specification; together, they make it structurally impossible.

## Dependencies
- LOGOS-0001 (alignment), LOGOS-0002 (values), LOGOS-0007 (specification)
- AXIOM-0009 (epistemic opacity), AXIOM-0010 (measurement problem), AXIOM-0013 (specification is lossy)

## Evaluation Notes
**Strength**: This proposition identifies a triple barrier to alignment-by-specification that is stronger than any single barrier alone. Even if one barrier were overcome (e.g., if values became fully transparent), the other two would remain.

**Potential weakness**: The proposition may be unfalsifiable in practice. If any measurement of values is claimed to change those values, how could we ever verify whether the pre-measurement values existed as claimed? The proposition needs to be careful not to make an empirically vacuous claim.

**Empirical testable implication**: If this proposition is true, then alignment systems trained on stated preferences (e.g., RLHF) should systematically diverge from alignment systems trained on revealed preferences (behavioral data), and both should diverge from alignment judgments made by the same humans in novel situations. This divergence is empirically testable.

**Negation**: "Values can be measured without perturbation, such that a specification based on measurement accurately captures values-as-lived." This would require a measurement process that is invisible to the agent being measured and that captures tacit values without requiring articulation.

## Lineage
AXIOM-0009 (opacity) + AXIOM-0010 (measurement perturbation) + AXIOM-0013 (lossy specification) --> PROPO-0004
