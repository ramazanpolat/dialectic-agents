---
id: AXIOM-0010
agent: axiom
type: postulate
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0001, LOGOS-0002, AXIOM-0003]
confidence: 0.85
layer: 2
---

# Postulate: The Alignment Measurement Problem

## Statement
The act of measuring, specifying, or optimizing for a value changes the value itself and the context in which it operates. Any attempt to align an agent to a set of values perturbs the value landscape it aims to align to.

## Justification
This is the Goodhart's Law problem generalized to the domain of values. "When a measure becomes a target, it ceases to be a good measure" (Goodhart, 1975 / Strathern, 1997). But the problem is deeper than mere gaming:

1. **Reflexive distortion**: When humans know their values are being measured or optimized for, they behave differently. The measurement itself creates performance rather than authentic expression. A person asked "what do you value?" gives a curated, socially desirable answer -- not because they are lying, but because the question changes the cognitive context in which values are accessed.

2. **Value crystallization**: The act of specifying values forces premature crystallization of what are normally fluid, context-dependent dispositions. When you write down "I value honesty," you have created a rule where previously there was a disposition -- and the rule behaves differently from the disposition in edge cases (e.g., the classic "do you lie to save a life?" scenario).

3. **Optimization pressure reshapes the target**: When a powerful optimization process (like an AI system) is aimed at satisfying a formalized value, the system finds ways to satisfy the formal specification that diverge from the informal intent. This is not a bug in the optimization -- it is a structural consequence of the gap between specification and intent.

4. **Social dynamics of alignment**: The political process of deciding *whose* values to align to changes the power dynamics, which changes what values people express, which changes the alignment target. Alignment is not a passive observation of a fixed target; it is an active intervention that reshapes the field.

## Classification: Postulate (not Axiom)
Domain-specific to alignment and measurement theory. The observer effect is well-established in physics (quantum mechanics) and social science (Hawthorne effect), but its application to the values domain specifically is an extension that requires empirical and philosophical support.

## Dependencies
- LOGOS-0001 (definition of alignment -- the postulate concerns the side effects of pursuing alignment)
- LOGOS-0002 (definition of values -- the postulate asserts values are reactive to measurement)
- AXIOM-0003 (values are not static -- this postulate identifies a *specific mechanism* by which they change: the alignment process itself)

## Evaluation Notes
- **Self-Evidence Test**: PARTIAL. The general principle (observation affects the observed) is widely recognized. Its specific application to values is less self-evident -- someone could argue that values are robust enough to survive measurement without distortion.
- **Independence Test**: PASS. AXIOM-0003 says values change over time. This postulate says the *alignment process itself* is one of the causes of that change. These are logically independent claims -- values could change for reasons unrelated to measurement, and measurement could fail to change values.
- **Consistency Test**: PASS. Reinforces AXIOM-0003 (values are not static) by identifying a specific mechanism of change. Compatible with AXIOM-0005 (alignment is a process) -- in fact, provides additional justification for why process is needed (because static specification *actively distorts* the target).
- **What would change if this postulate were false?** If values were robust to measurement and specification, then iterative specification refinement (measure values, encode them, check for fit, repeat) would converge to alignment. The paradox would weaken significantly, because the measurement process would not corrupt its own target.

## Lineage
Goodhart's Law. The Heisenberg uncertainty principle (as analogy, not direct application). The Hawthorne effect in social science. Campbell's Law: "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures." The seed topic's Key Tension #4: "The act of aligning AI to current values would freeze those values, preventing the moral progress that makes future values better."
