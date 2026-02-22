---
id: HYPOTHEX-0002
agent: hypothex
type: hypothesis
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [PROPO-0002, ORI-0002, AXIOM-0004, AXIOM-0011, LOGOS-0001, LOGOS-0002]
confidence: 0.82
layer: 9
---

# Hypothesis: Human Values Are Systematically Inconsistent Both Within and Between Individuals

## Statement
The empirical component of PROPO-0002 (The Incoherent Target Proposition) asserts two things: (a) individual humans hold internally inconsistent values such that stated, believed, and revealed values diverge, and (b) the diversity of values across the human population is sufficient to trigger Arrow's impossibility conditions, making aggregation into a single coherent target undefined. This hypothesis structures both empirical claims.

## Hypothesis Structure
- **Claim**: For any sufficiently large human population, the intra-individual inconsistency between stated values, believed values, and behaviorally revealed values is systematic (not random noise), and the inter-individual diversity of value profiles is sufficient to satisfy the unrestricted domain condition of Arrow's theorem, such that no non-dictatorial aggregation procedure can produce a consistent collective value ordering.
- **If-Then Form**: If human values are systematically inconsistent (intra-individually) and sufficiently diverse (inter-individually), then: (1) for any individual, controlled experiments should reveal statistically significant divergence between values elicited through different methods (self-report, conjoint analysis, behavioral observation, neuroimaging), and (2) for any population of more than a small threshold size, different reasonable aggregation methods (majority rule, Borda count, approval voting, deliberative consensus) should produce materially different collective value orderings on non-trivial value conflicts.
- **Null Hypothesis**: Human values are fundamentally coherent at the individual level, and the apparent inconsistencies are measurement artifacts. Individuals have a single true preference ordering that is stable across elicitation methods when those methods are sufficiently refined. At the collective level, human value diversity is restricted enough that a natural Condorcet winner exists for most real-world value conflicts, making Arrow's theorem practically irrelevant.
- **Falsification Criteria**: The hypothesis would be falsified by: (1) demonstrating that individual value inconsistency disappears when controlling for measurement method quality -- i.e., stated, believed, and revealed values converge as elicitation methods improve, or (2) demonstrating that for typical human populations, different aggregation methods produce substantially identical collective value orderings on a representative set of value conflicts (suggesting that Arrow's conditions are not triggered in practice), or (3) identifying a principled aggregation procedure that produces consistent results accepted as legitimate by diverse populations.

## Evidence Framework
- **Confirming Evidence**: (a) Replication of the stated/revealed preference gap across diverse cultures and value domains (not just consumer preferences). (b) Experimental evidence that framing effects, order effects, and context effects change expressed moral judgments in ways that are systematic and large relative to inter-individual differences. (c) Empirical demonstrations that different voting/aggregation methods produce different winners in real-world value-laden decisions (policy referenda, ethical committee deliberations). (d) Evidence from behavioral economics that "preference reversals" are robust phenomena, not artifacts.
- **Disconfirming Evidence**: (a) Studies showing that the stated/revealed preference gap narrows dramatically with better elicitation methods (e.g., informed deliberation, extended reflection). (b) Evidence that moral judgments become highly stable across framing and context after philosophical training or structured deliberation. (c) Empirical demonstrations that for real-world moral dilemmas (as opposed to constructed edge cases), different aggregation methods converge. (d) Cross-cultural studies showing a core of universal moral values sufficient to define a non-trivial alignment target.
- **Crucial Experiment**: Select a set of 20 real-world value conflicts spanning multiple moral domains (distributive justice, liberty vs. security, individual vs. collective welfare, intergenerational obligations, animal welfare, environmental ethics). For each conflict, elicit value judgments from 1000+ individuals across 5+ cultures using 4+ different elicitation methods. Measure: (1) within-individual cross-method consistency (does the same person give the same ranking regardless of method?), and (2) cross-method aggregation consistency (does the group ranking change depending on which method and which aggregation procedure is used?). If within-individual consistency is high and aggregation convergence is high, the hypothesis fails. If either is low, the hypothesis is supported.
- **Prior Probability**: 0.80. The existing evidence from behavioral economics and moral psychology strongly supports both intra-individual inconsistency and inter-individual diversity. Kahneman and Tversky's prospect theory, Haidt's moral foundations theory, and Arrow's theorem provide independent lines of convergent evidence. The prior is high but not overwhelming because the null hypothesis (that inconsistencies are measurement artifacts) has some theoretical support from rational-choice theory, and recent work on "constructive preferences" suggests that apparent inconsistency may partly reflect value construction in real-time rather than inconsistency in stored values.

## Alternative Hypotheses
1. **Constructive Preferences Hypothesis**: Individuals do not have stored, pre-existing values that can be "measured." Instead, values are constructed in the moment of elicitation, influenced by context, framing, and mood. What appears to be inconsistency is actually the absence of a fact of the matter -- there is no "true" preference ordering to be inconsistent with. Under this alternative, the alignment target is not incoherent; it is genuinely indeterminate, which is a different (and possibly more tractable) problem.
2. **Reflective Equilibrium Hypothesis**: Individual values become consistent through extended reflection. The inconsistencies observed in quick elicitation disappear when subjects engage in careful, structured deliberation. At the collective level, deliberative democracy achieves convergence that voting cannot. Under this alternative, the alignment problem is not fundamentally about incoherent values but about insufficient deliberation -- and an AI system that facilitates deliberation could access the coherent "reflective" values.
3. **Core + Periphery Hypothesis**: Human values have a small, stable, cross-culturally shared core (e.g., reciprocity, harm avoidance, care for offspring) surrounded by a large, variable, culture-specific periphery. The core is internally consistent and aggregation-friendly. The periphery is inconsistent and diverse. Under this alternative, alignment to the core is feasible and meaningful, even if alignment to the periphery is not.

## Thought Experiments

**Thought Experiment 1 -- The Perfect Elicitor**: Imagine a machine that can read an individual's complete value profile without any elicitation artifacts -- no framing effects, no social desirability bias, no context dependence. What would the output look like? If the hypothesis is correct, even this machine would produce an internally inconsistent output: the person genuinely values both liberty and equality in ways that conflict in specific cases, and there is no deeper level at which the conflict resolves. If the null hypothesis is correct, the machine would produce a clean, consistent preference ordering.

**Thought Experiment 2 -- The Value Parliament**: Imagine 1000 humans, each with their values perfectly known, tasked with producing a single collective value specification for an AI system. They are given unlimited time and resources. If the hypothesis is correct, the final output depends critically on the decision procedure they use (majority rule, consensus, delegation, etc.), and no procedure produces a result that all participants endorse as "the correct aggregation." If the null hypothesis is correct, extended deliberation converges on a shared specification regardless of procedure.

**Thought Experiment 3 -- The Clone Divergence**: Take 100 genetically identical individuals raised in substantially similar but not identical environments. If the hypothesis is correct, even this maximally similar population will exhibit sufficient value diversity to trigger Arrow's conditions on non-trivial moral dilemmas. If the null hypothesis is correct, value similarity should track genetic and environmental similarity closely enough to produce robust aggregation.

## Testability Rating
- **Falsifiable**: yes
- **Testable (in principle)**: yes
- **Testable (in practice)**: yes -- the required studies (cross-method value elicitation, cross-cultural moral judgment surveys, aggregation convergence tests) are feasible with existing methodology, and many have already been conducted in partial form.

## Dependencies
- PROPO-0002 (the proposition whose empirical components are being structured)
- ORI-0002 (the classification identifying empirical components)
- AXIOM-0004 (humans misaligned with selves), AXIOM-0011 (irreducible value pluralism)
- LOGOS-0001 (alignment), LOGOS-0002 (values)

## Evaluation Notes
This hypothesis is relatively well-supported by existing evidence, which is why the prior probability is high (0.80). The main intellectual risk is not that the hypothesis is wrong, but that it is trivially true -- that everyone already knows values are inconsistent and diverse, and the interesting question is *how much* inconsistency and diversity there is relative to the thresholds that would make alignment tractable. The crucial experiment is designed to address this quantitative question, not just the qualitative one.

The most interesting alternative hypothesis is the Constructive Preferences account, because it reframes the problem entirely: if values are not pre-existing facts to be measured but ongoing constructions, then alignment is not about "measuring the target accurately" but about "participating in the target's construction." This reframing converges with the process-based approach advocated by AXIOM-0005.

## Lineage
ORI-0002 (a posteriori components: self-misalignment, value diversity) --> HYPOTHEX-0002 (structured as testable hypothesis)
