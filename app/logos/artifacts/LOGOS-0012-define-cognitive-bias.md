---
id: LOGOS-0012
agent: logos
type: definition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0002, LOGOS-0006, LOGOS-0011]
confidence: 0.87
layer: 1
---

# Definition: Cognitive Bias

## Statement
**Cognitive bias** (noun phrase): A systematic and predictable deviation in an agent's judgment, reasoning, or decision-making from what would be produced by logically valid inference from the available evidence, arising from the architecture of the agent's cognitive system rather than from random error, incomplete information, or rational strategy.

## Justification
Cognitive bias is essential to the Alignment Paradox for a precise reason: human values (LOGOS-0002) are partly the product of cognitive biases. If an AI system is aligned to human values *as expressed*, it inherits the biases embedded in those values. If it is aligned to human values *as they would be without bias*, it must correct for biases — but then it is no longer aligned to actual human preferences, and the question of who decides which biases to correct becomes a new alignment problem.

The definition emphasizes three features:
1. **Systematic** — biases are not random noise; they are structured, repeatable patterns
2. **Predictable** — biases can be anticipated and catalogued; they follow from the architecture of the cognitive system
3. **Architectural** — biases arise from *how the system is built* (e.g., heuristics, evolutionary adaptations, training data distributions), not from what information it has

## Genus and Differentia
- **Genus**: A deviation in judgment or reasoning
- **Differentia**: Distinguished from *ignorance* by being systematic (ignorance is about missing information; bias distorts available information); distinguished from *error* by being predictable (errors are random; biases are patterned); distinguished from *rational strategy* by being involuntary or unrecognized (a deliberate simplification for computational efficiency, if recognized and chosen, is a heuristic, not a bias — though heuristics can produce biases); distinguished from *cultural difference* by being architectural (cultural values may differ without any party being biased — bias implies deviation from a norm of valid inference, not merely deviation from another culture's norms)

## Positive Example
Confirmation bias: an agent exposed to evidence both supporting and contradicting a belief systematically recalls, weights, and seeks out supporting evidence more than contradicting evidence. This is systematic (it operates the same way across topics), predictable (it can be demonstrated experimentally), and architectural (it arises from how human memory and attention systems work, not from a strategic choice).

## Negative Example
A doctor who misdiagnoses a rare disease because she has never encountered it before is NOT exhibiting cognitive bias — she is exhibiting ignorance. Her error stems from missing information, not from systematically distorting available information. However, if she dismisses a colleague's suggestion of the rare disease *because she has already committed to a diagnosis* (anchoring bias), that IS cognitive bias.

## Dependencies
- LOGOS-0002 (values) — cognitive biases shape the formation and expression of values
- LOGOS-0006 (experience) — many cognitive biases operate on or through experience (e.g., the availability heuristic depends on what experiences are easily recalled)
- LOGOS-0011 (epistemic humility) — recognition of one's own cognitive biases is a form of epistemic humility; failure to recognize them is a failure of epistemic humility

## Evaluation Notes
A difficult boundary case: are AI systems subject to cognitive bias? If an AI system trained on biased data produces biased outputs, is the AI "biased" in the same sense? Under this definition, the answer depends on architecture. If the bias arises from the architecture of the AI system (e.g., the structure of its training process, its loss function, its inductive biases), then yes. If it merely reflects biased inputs, then it is an instance of a different phenomenon — perhaps "inherited bias" or "data bias" — which may need its own definition.

Open question for downstream agents: if alignment requires correcting for cognitive biases in human values, who determines which deviations from "valid inference" are biases to be corrected and which are legitimate value differences? This is a deep instance of the Alignment Paradox.

## Lineage
Derived from the Alignment Paradox's observation that humans "are not aligned with themselves — individuals hold contradictory values simultaneously." Cognitive bias is one of the primary mechanisms by which such contradictions arise and persist.
