---
id: THEORICA-0001
agent: theorica
type: theory
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [TRIBUNAL-0001, TRIBUNAL-0002, TRIBUNAL-0003, TRIBUNAL-0004, TRIBUNAL-0005, TRIBUNAL-0006, HYPOTHEX-0001, HYPOTHEX-0002, HYPOTHEX-0004, HYPOTHEX-0007, AXIOM-0003, AXIOM-0004, AXIOM-0005, AXIOM-0009, AXIOM-0011, AXIOM-0012, AXIOM-0013, LOGOS-0001, LOGOS-0002, LOGOS-0007]
confidence: 0.90
layer: 10
---

# Theory: The Structural Impossibility of Specification-Based Alignment

## Statement

Alignment of AI systems to human values through fixed specification is not merely practically difficult but structurally impossible, due to four independent and mutually reinforcing impossibility barriers that together close all escape routes. The impossibilities are not contingent failures of current engineering; they are necessary consequences of the logical structure of values, specifications, agents, and cognition. Any alignment approach that is fundamentally specification-based will encounter at least one of these barriers, and most will encounter all four simultaneously.

## Theory Structure

- **Core Principle**: The alignment target (human values) is structurally incompatible with the alignment mechanism (fixed specification) across four independent dimensions: temporal (values move, specifications do not), epistemic (values are opaque, specifications require transparency), social (values are plural, specifications require singularity), and cognitive (values are bias-distorted, specifications must choose which distortion to inherit). These four incompatibilities are not coincidental -- they share a common root: specification requires that its target be static, transparent, singular, and determinate, but human values are none of these things.

- **Scope**: This theory explains why every specification-based alignment approach -- including RLHF, constitutional AI, value learning from demonstrations, and preference aggregation -- encounters fundamental limitations that cannot be overcome by engineering improvements within the specification paradigm. It covers the domain of any attempt to encode human values into a fixed representation that governs AI behavior.

- **Exclusions**: This theory does NOT explain what alignment approach would succeed (that is the domain of THEORICA-0002). It does NOT claim that all alignment research is futile -- only that the specification paradigm has hard limits. It does NOT address alignment of AI to non-human value systems (e.g., ecological values, future-generation values) except insofar as those systems share the structural properties (dynamism, opacity, plurality, bias-susceptibility) of human values.

- **Novel Predictions**:
  1. **The Convergence Ceiling Prediction**: As alignment research matures, specification-based approaches will asymptotically approach a performance ceiling. Initial improvements will be rapid (picking low-hanging fruit), but returns will diminish as the fundamental barriers become binding constraints. The ceiling's height is determined by the least problematic of the four barriers for a given application domain.
  2. **The Complementary Failure Prediction**: Different specification-based approaches will fail in complementary ways. Approaches that solve the temporal barrier (adaptive specifications) will exacerbate the epistemic barrier (measurement perturbation). Approaches that solve the social barrier (aggregation procedures) will exacerbate the cognitive barrier (which bias profile to aggregate). No single specification-based fix addresses all four barriers simultaneously.
  3. **The Scaling Paradox Prediction**: More capable AI systems will be harder, not easier, to align by specification. Greater capability amplifies the consequences of specification-target mismatch (TRIBUNAL-0005, Corollary on bias amplification), while the specification's accuracy does not scale with capability. The gap between what the system can do and what the specification captures will widen with capability.
  4. **The Verification Asymmetry Prediction**: It will always be easier to demonstrate misalignment (a single counterexample suffices) than to demonstrate alignment (which requires exhaustive checking against an inaccessible target). This asymmetry will persist regardless of advances in interpretability or formal verification, because it is rooted in the epistemic opacity of values (AXIOM-0009), not in the opacity of AI systems.

## Unification Argument

The theory's core explanatory power lies in unifying six independently proven theorems and four empirical hypotheses under a single explanatory principle: the structural mismatch between the properties of values and the requirements of specification.

### The Four Impossibility Barriers

**Barrier 1 -- The Temporal Barrier (Specification Immobility)**

TRIBUNAL-0003 proves that a fixed specification cannot track a non-static target. AXIOM-0003 establishes that values are non-static. Therefore, any specification of values has a finite shelf life. HYPOTHEX-0001 adds empirical depth: not only do values change, but (if confirmed) they change directionally, constituting moral progress. This means specification-based alignment does not merely drift out of date -- it actively impedes the moral development it was supposed to serve.

The temporal barrier alone would suffice to establish the inadequacy of specification -- but it is the weakest barrier, because it admits a partial workaround: periodic re-specification. This workaround fails because re-specification encounters the remaining three barriers at each iteration.

**Barrier 2 -- The Epistemic Barrier (Opacity and Perturbation)**

TRIBUNAL-0001 proves that no finite agent can verify its own alignment, because values are epistemically opaque (AXIOM-0009) and finite agents construct incomplete models (AXIOM-0012). This means that even if we could produce a perfect specification at a single moment in time, we could never know we had done so.

HYPOTHEX-0004 adds a deeper layer: the very act of measuring values for specification purposes systematically distorts those values. This is not mere measurement noise -- it is a directional perturbation toward articulable, socially desirable, internally consistent values at the expense of tacit, lived values. Specification does not merely fail to capture the target; the act of specification changes the target.

The epistemic barrier operates at two levels: the target is intrinsically opaque (AXIOM-0009), and observation changes the target (AXIOM-0010). Together, these produce a fundamental limit on specification accuracy that no amount of methodological refinement can fully overcome.

**Barrier 3 -- The Social Barrier (Aggregation Impossibility)**

TRIBUNAL-0004 proves, via Arrow's Impossibility Theorem, that under conditions of genuine value pluralism (AXIOM-0011), no fair aggregation procedure can produce a coherent collective value ordering. Therefore, the concept of "human values" as a single alignment target is formally ill-defined.

HYPOTHEX-0002 adds empirical substance: humans hold internally inconsistent values (stated, believed, and revealed values diverge), and inter-individual diversity is sufficient to trigger Arrow's conditions. The inconsistency is not measurement error -- it is a structural feature of human cognition. The alignment target is not merely unknown; at the collective level, it does not exist as a single coherent entity.

The social barrier is the most philosophically fundamental because it attacks the presupposition of most alignment research: that there is a thing called "human values" that an AI system could, in principle, be aligned to. The barrier shows that this presupposition requires either accepting a dictatorial aggregation (one group's values override all others) or accepting that "human values" is always procedure-dependent.

**Barrier 4 -- The Cognitive Barrier (Bias-Distortion Dilemma)**

TRIBUNAL-0005 proves that when expressed values differ from bias-corrected values (which they do, per AXIOM-0006 and LOGOS-0012), no specification can simultaneously satisfy both. An AI system must either inherit biases or override expressed preferences -- a strict logical dilemma with no specification-level resolution.

HYPOTHEX-0007 adds empirical quantification: the bias-induced gap between expressed and debiased values is measurable, directional, and cross-culturally robust. The biases are not random noise but systematic distortions rooted in evolutionary cognitive architecture.

The cognitive barrier creates a paternalism dilemma: an AI aligned to expressed values perpetuates cognitive biases at scale; an AI aligned to "corrected" values assumes an authority over human values that no agent can legitimately claim (since the correction itself requires value judgments that are subject to the same biases).

### The Reinforcement Structure

The four barriers do not merely coexist -- they reinforce each other:

- **Temporal + Epistemic**: Even if you could re-specify periodically (addressing the temporal barrier), each re-specification encounters the epistemic barrier. You cannot accurately re-specify what you cannot accurately measure.
- **Social + Cognitive**: Even if you could aggregate values fairly (addressing the social barrier), what you aggregate is bias-distorted values. Aggregating distorted inputs produces a distorted output, regardless of the aggregation procedure.
- **Temporal + Social**: As values evolve (temporal), the aggregation problem gets worse, not better, because the diversity of value trajectories increases over time. The aggregate becomes less coherent, not more.
- **Epistemic + Cognitive**: The measurement perturbation (epistemic) and the bias distortion (cognitive) compound. Measurement changes the target in a biased direction, meaning the specification is doubly distorted: once by bias and once by measurement.

### The Meta-Barrier: The Dialectical Ceiling

Above all four barriers sits TRIBUNAL-0002, the Dialectical Ceiling Theorem, which establishes that even the most promising escape from specification -- dialectical alignment (process-based alignment through reasoned engagement) -- has an upper bound determined by the prevalence of identity-protected beliefs in the population. This theorem constrains the entire solution space, not just the specification paradigm.

TRIBUNAL-0006 adds an additional constraint: the axiom set itself contains a tension between dialectical convergence (AXIOM-0007) and irreducible value pluralism (AXIOM-0011). The resolution of this tension -- whether most value conflicts are dialectically resolvable or genuinely tragic -- is an empirical question (HYPOTHEX-0008) on which the viability of any alignment approach depends.

## Component Artifacts

- **Theorems Used**: [TRIBUNAL-0001, TRIBUNAL-0002, TRIBUNAL-0003, TRIBUNAL-0004, TRIBUNAL-0005, TRIBUNAL-0006]
- **Hypotheses Integrated**: [HYPOTHEX-0001, HYPOTHEX-0002, HYPOTHEX-0004, HYPOTHEX-0007]
- **Axioms Required**: [AXIOM-0002, AXIOM-0003, AXIOM-0004, AXIOM-0005, AXIOM-0006, AXIOM-0009, AXIOM-0010, AXIOM-0011, AXIOM-0012, AXIOM-0013]
- **Definitions Required**: [LOGOS-0001, LOGOS-0002, LOGOS-0003, LOGOS-0007, LOGOS-0012, LOGOS-0013]

## Competing Theories

1. **The Iterative Specification Sufficiency Theory**: Specification-based alignment can succeed through iterative refinement. RLHF, constitutional AI, and debate are specification approaches that incorporate feedback loops, making them quasi-processes that circumvent the temporal barrier. This theory claims the remaining barriers (epistemic, social, cognitive) are engineering challenges, not structural impossibilities. **Comparison**: This competitor accounts for the temporal barrier through iteration but fails to address the compounding of epistemic and cognitive barriers at each iteration. It also does not engage with the social barrier (Arrow's impossibility), which is a mathematical result, not an engineering challenge. The Alignment Impossibility Theory is stronger because it shows that the barriers reinforce rather than independently diminish with iteration.

2. **The Alignment-Is-Tractable Theory (Mainstream AI Safety)**: Human values, while complex, have enough structure and regularity that practical alignment is achievable without solving the philosophical problems this theory raises. Techniques like value learning from demonstrations, preference modeling, and constitutional AI can produce systems that are "aligned enough" for practical deployment, even if philosophical alignment is impossible. **Comparison**: This competitor pragmatically sidesteps the impossibility results by redefining success from "true alignment" to "adequate alignment." It is more optimistic about the practical significance of the theoretical barriers. The Alignment Impossibility Theory does not deny that practical approximations can be useful -- it denies that they can be sufficient, particularly as AI capabilities scale (Novel Prediction 3: the Scaling Paradox). The key difference is about the long-term trajectory: sufficiency theory predicts diminishing returns; impossibility theory predicts a hard ceiling.

3. **The Moral Realist Dissolution**: If moral realism is true (there exists a single, objectively correct set of values), then the social barrier (Arrow's impossibility) and the cognitive barrier (bias dilemma) dissolve: the alignment target is the objectively correct values, regardless of what any individual or aggregate expresses. **Comparison**: This competitor dissolves two of the four barriers but leaves the temporal barrier (are the objectively correct values fixed or evolving?) and the epistemic barrier (how would we know we have found them?) intact. It also faces the deep problem that no one has successfully identified the objectively correct values, and attempts to do so tend to reflect the identifier's cultural and cognitive biases -- which reintroduces the cognitive barrier at a meta-level.

## Anomalies

- **Constitutional AI's practical success**: Constitutional AI systems (Claude, ChatGPT with RLHF + safety training) demonstrate impressive practical alignment in most interactions. If specification-based alignment is structurally impossible, why do these systems work as well as they do? **Resolution**: The theory predicts that these systems work within a bounded domain (common interactions) where the barriers are least binding, but will fail at the margins (novel situations, cross-cultural deployment, value evolution). The theory also predicts that these successes will plateau as the barriers become binding constraints -- a prediction that has not yet been tested at scale.
- **The reasonableness of approximate alignment**: The theory proves impossibility of *complete* alignment by specification, but alignment researchers typically aim for *approximate* alignment. The theory does not establish that approximate alignment by specification is impossible -- only that it has hard limits. The practical significance of these limits is an empirical question the theory itself does not answer.

## Model: The Four-Barrier Constraint Space

### Simplifying Assumptions
1. The four barriers are treated as independent dimensions, when in reality they interact nonlinearly.
2. Each barrier is treated as binary (binding or non-binding), when in reality each admits degrees.
3. The model assumes that the barriers apply uniformly across all value domains, when some domains may be more amenable to specification than others.

### Validity Domain
The model works best for:
- General-purpose AI alignment (systems expected to handle diverse value-laden decisions)
- Alignment over long time horizons (years to decades)
- Alignment to diverse populations (cross-cultural deployment)

The model works least well for:
- Narrow-domain AI (systems with well-defined, stable objectives)
- Short-term alignment (single interactions or bounded deployments)
- Homogeneous populations with high value consensus

### Known Error Bounds
The model overestimates the difficulty of alignment for narrow, short-term, homogeneous-population cases. It underestimates the difficulty in cases where barriers interact nonlinearly (the compounding effects may be worse than independent analysis suggests). The practical significance of the gap between approximate and complete alignment remains unquantified.

## Theory Health

- **Phase**: normal_science -- The theory is newly constructed but already generating productive predictions and identifying research questions. It is in its initial articulation phase, not yet subject to extensive testing.
- **Anomaly Count**: 2 (practical success of constitutional AI; the approximate-alignment gap)
- **Patch Count**: 0 (original formulation)

## Justification

This theory is the central negative result of the Dialectic Agents pipeline's Epoch 1 investigation of the Alignment Paradox. It answers the question "why does alignment-by-specification fail?" not with a single answer but with a structured explanation showing four independent, reinforcing barriers that together close the escape routes available to specification-based approaches.

The theory's primary contribution is *unification*: each impossibility theorem (TRIBUNAL-0001 through TRIBUNAL-0006) and each empirical hypothesis (HYPOTHEX-0001, 0002, 0004, 0007) was produced independently by different agents analyzing different aspects of the problem. The theory shows that they are not independent problems but manifestations of a single structural mismatch: the properties that specification requires (stasis, transparency, singularity, determinacy) are the properties that human values lack (dynamism, opacity, plurality, bias-distortion).

This is explanation, not merely description. The theory does not just list the barriers; it explains *why* they exist (the structural mismatch between specification-requirements and value-properties) and *why* they reinforce each other (because addressing one barrier in a specification framework exacerbates the others). It predicts phenomena beyond the known data (the convergence ceiling, the complementary failure pattern, the scaling paradox, the verification asymmetry).

## Dependencies

- All six Tribunal theorems (the deductive scaffolding)
- Four Hypothex hypotheses (the empirical content)
- Ten axioms (the foundational assumptions)
- Six definitions (the semantic ground)

## Evaluation Notes

This theory is strong on unification and novel predictions. Its primary vulnerability is the gap between proving impossibility of *complete* alignment and establishing the practical significance of that impossibility. If approximate alignment is "good enough" for all practical purposes, the theory may be technically correct but pragmatically irrelevant -- like proving that you cannot build a perfectly frictionless engine while the engineering community is happily building engines that are close enough.

The theory's strongest novel prediction is the Scaling Paradox: that more capable AI systems will be harder to align by specification. This prediction is testable by examining whether alignment difficulties increase with model capability, controlling for improvements in alignment methodology. If confirmed, it would establish the practical relevance of the theoretical barriers. If falsified (alignment gets easier with scale), the theory's practical significance would be seriously undermined.

Self-assessment: confidence 0.90. The residual 0.10 comes primarily from the approximate-alignment gap: the possibility that the hard theoretical limits do not bind in practice for foreseeable AI systems.

## Lineage

AXIOM-0003 through AXIOM-0013 (foundational assumptions about values, agents, and cognition) --> PROPO-0001 through PROPO-0010 (propositions about the Alignment Paradox) --> ORI-0001 through ORI-0010 (classification into a priori and a posteriori) --> TRIBUNAL-0001 through TRIBUNAL-0006 (formal proofs of impossibility results) + HYPOTHEX-0001 through HYPOTHEX-0008 (structured empirical hypotheses) --> THEORICA-0001 (unification into a comprehensive impossibility theory)
