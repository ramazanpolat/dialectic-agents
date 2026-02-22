---
id: ORI-0004
agent: ori
type: classification
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: ["PROPO-0004", "LOGOS-0001", "LOGOS-0002", "LOGOS-0007", "AXIOM-0009", "AXIOM-0010", "AXIOM-0013"]
confidence: 0.90
layer: 3
---

# Classification of PROPO-0004: The Alignment Heisenberg Proposition

## Statement
Any attempt to measure, formalize, or specify (LOGOS-0007) the values (LOGOS-0002) of a human agent for the purpose of alignment (LOGOS-0001) changes the values it seeks to capture, such that the resulting specification is a specification of the values-as-measured rather than the values-as-lived, and these two are not identical.

## Classification
- **Verdict**: a_posteriori
- **Route To**: Hypothex
- **Negation Test**: Negating the proposition yields: "Values can be measured without perturbation, such that a specification based on measurement accurately captures values-as-lived." This is logically coherent and not self-contradictory. We can consistently conceive of a measurement process that does not alter its target -- indeed, many physical measurements approximate this (measuring the temperature of a lake does not significantly change the lake's temperature). The negation is conceivable. **Result**: Not a priori by negation test.
- **Conceivability Test**: Can we imagine a world where value measurement does not perturb values? Yes: (a) a world where values are fully explicit and conscious, such that articulating them is merely reading off an internal list rather than constructing a response, (b) a world where passive behavioral observation can capture values without the agent's awareness, (c) a world where the reflexive distortion described in AXIOM-0010 simply does not operate for values. These are coherent possible worlds. **Result**: Contingent -- many possible worlds falsify this.
- **Justification Test**: What settles whether measurement perturbs values? This is fundamentally an empirical question: (1) Do RLHF-trained systems diverge from human values in the way the proposition predicts? Testable. (2) Do stated preferences diverge from revealed preferences in ways consistent with measurement-perturbation rather than mere noise? Testable. (3) Does the act of introspecting about values change subsequent value-guided behavior? Testable through experimental psychology. The proposition itself identifies a specific testable implication: alignment systems trained on stated preferences should systematically diverge from those trained on revealed preferences. **Result**: Empirical observation and experimentation are needed.

## Justification
PROPO-0004 is an empirical claim about the relationship between measurement and values. Its analogy to the Heisenberg uncertainty principle is illuminating but also misleading: in quantum mechanics, the observer effect is a necessary consequence of the mathematical structure of quantum theory (an a priori result within that framework). In the domain of values, the observer effect is an empirical hypothesis about human cognition, not a logical necessity.

The three barriers the proposition identifies are all empirical:
1. **Epistemic opacity** (AXIOM-0009): that values are partially tacit is an empirical claim about human cognition, supported by evidence from cognitive science but not logically necessary.
2. **Measurement perturbation** (AXIOM-0010): that measuring values changes them is an empirical claim about reflexive systems, supported by Goodhart's Law and the Hawthorne effect but not logically necessary.
3. **Specification lossiness** (AXIOM-0013): that specifications lose information is arguably closer to an a priori truth (the map-territory distinction), but its application to values specifically is empirical.

Could one argue for a mixed classification? The map-territory distinction (AXIOM-0013) has an a priori flavor: any representation of a thing is not the thing itself. But PROPO-0004 claims more than this general truth -- it claims that the *specific act of measuring values perturbs those values in a specific way*. This additional claim is empirical.

The proposition's own evaluation notes acknowledge it "may be unfalsifiable in practice" -- if every measurement changes values, how do we verify the pre-measurement values? This is a methodological challenge, but it does not make the proposition a priori; it makes it a difficult-to-test empirical claim. The proposition identifies testable implications (divergence between stated and revealed preference alignments), confirming its empirical character.

I classify this as a posteriori because all three of its supporting pillars (opacity, perturbation, lossiness-applied-to-values) require empirical evidence, and its negation is logically coherent.

## Dependencies
- PROPO-0004 (the proposition being classified)
- LOGOS-0001 (alignment), LOGOS-0002 (values), LOGOS-0007 (specification)
- AXIOM-0009 (epistemic opacity), AXIOM-0010 (measurement problem), AXIOM-0013 (specification is lossy)

## Evaluation Notes
Confidence is 0.90 -- high because the a posteriori classification is well-supported. The proposition makes specific empirical claims about human cognition and the dynamics of measurement that are in principle testable. The only source of hesitation is the near-a-priori status of the map-territory distinction (AXIOM-0013), but this general principle is not sufficient to establish the proposition without its empirical components.

What would change my classification: if someone demonstrated that the measurement-perturbation effect for values is a logical necessity derivable from the definitions of "value" and "measurement" alone (without empirical premises about human cognition), I would reclassify as mixed.

## Lineage
AXIOM-0009 (opacity) + AXIOM-0010 (perturbation) + AXIOM-0013 (lossy specification) --> PROPO-0004 --> ORI-0004 (classification: a_posteriori)
