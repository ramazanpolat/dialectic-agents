---
id: ORI-0007
agent: ori
type: classification
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: ["PROPO-0007", "LOGOS-0001", "LOGOS-0002", "LOGOS-0012", "AXIOM-0004", "AXIOM-0006"]
confidence: 0.91
layer: 3
---

# Classification of PROPO-0007: The Distorted Target Proposition

## Statement
Human values (LOGOS-0002) as expressed and enacted are systematically distorted by cognitive biases (LOGOS-0012), which arise from a cognitive architecture optimized for survival rather than truth (AXIOM-0006). Therefore, an AI system aligned to expressed human values inherits these systematic distortions, and an AI system that corrects for these distortions is no longer aligned to expressed human values -- producing a dilemma with no specification-level resolution.

## Classification
- **Verdict**: mixed
- **Route To**: SPLIT
- **Negation Test**: Negating the proposition yields: "Cognitive biases do NOT systematically distort human values, OR an AI can be aligned to both expressed and corrected values simultaneously." The first disjunct is empirically conceivable (cognitive biases might be benign with respect to value formation). The second disjunct is logically conceivable (a specification capturing both biased and unbiased values might exist). Neither disjunct is self-contradictory. **Result**: Negation is coherent -- not purely a priori.
- **Conceivability Test**: Can we imagine a world where the distorted-target dilemma does not arise? Yes: (a) a world where cognitive architecture is optimized for truth rather than survival (negating AXIOM-0006), producing no systematic bias in values, or (b) a world where biases happen to cancel out at the population level, producing expressed values that approximate bias-free values. These are coherent possible worlds. **Result**: Contingent.
- **Justification Test**: What settles this? Two distinct types of justification are needed. (1) The dilemma's logical structure -- that aligning to X and aligning to corrected-X cannot both be achieved simultaneously when X differs from corrected-X -- is analytically true. If A differs from B, you cannot be aligned to both A and B (assuming alignment requires consistency). This is a priori. (2) The premise that cognitive biases *actually do* systematically distort values is empirical, requiring evidence from cognitive science and evolutionary psychology. **Result**: Both logical analysis and empirical evidence are needed.
- **If Mixed**:
  - A priori component: "If expressed values differ from corrected values, then an AI system cannot simultaneously be aligned to both." This is a logical truth following from the definition of alignment (LOGOS-0001) and the law of non-contradiction. If V_expressed is not identical to V_corrected, then Aligned(AI, V_expressed) AND Aligned(AI, V_corrected) is a contradiction (given that alignment requires behavioral consistency with a *specified* set of values).
  - A posteriori component: "Cognitive biases systematically distort expressed values such that V_expressed differs from V_corrected." This is an empirical claim about human cognition, grounded in AXIOM-0006 (evolution optimized for survival) and supported by decades of cognitive science research (Kahneman, Tversky, Haidt, etc.).

## Justification
PROPO-0007 has a clean decomposition into a priori and a posteriori components, making it a textbook case of a mixed proposition.

**The a priori component** is a dilemma structure:
1. V_expressed and V_corrected are distinct (premise).
2. An AI aligned to V_expressed inherits whatever systematic features V_expressed contains (from the definition of alignment as behavioral consistency with a specified target).
3. An AI aligned to V_corrected is, by definition, not aligned to V_expressed (if the two differ).
4. Therefore, the AI must choose one target or the other; it cannot satisfy both.

This dilemma structure is valid regardless of whether cognitive biases actually exist. If V_expressed differs from V_corrected *for any reason*, the dilemma holds. The logical form is: if A is not B, alignment to A precludes alignment to B. This is a priori.

**The a posteriori component** is the empirical claim that cognitive biases are the *mechanism* by which V_expressed differs from V_corrected:
- AXIOM-0006 (evolutionary optimization for survival) provides the causal story.
- LOGOS-0012 (cognitive bias) provides the mechanism description.
- AXIOM-0004 (human self-misalignment) provides the phenomenological evidence.

These are all empirical claims about actual human cognition. They require evidence from cognitive science, evolutionary psychology, and behavioral economics. They are contingent -- a different cognitive architecture would not produce the same biases.

The proposition's final claim -- that there is "no specification-level resolution" -- also has both components. The logical part: a specification must choose one target. The empirical part: no specification has been found that bridges the gap, and the gap is plausibly unbridgeable in practice.

## Dependencies
- PROPO-0007 (the proposition being classified)
- LOGOS-0001 (alignment), LOGOS-0002 (values), LOGOS-0012 (cognitive bias)
- AXIOM-0004 (humans misaligned with selves), AXIOM-0006 (natural selection optimized for survival)

## Evaluation Notes
Confidence is 0.91. The mixed classification is well-supported because the proposition clearly combines a formal dilemma (a priori) with empirical premises about cognitive bias (a posteriori). The decomposition is clean and unambiguous.

Routing recommendation:
- **Tribunal** should attempt to prove the a priori component: that alignment to V and alignment to V' where V differs from V' is impossible within the specification framework (using LOGOS-0001, LOGOS-0007, and AXIOM-0001/0002).
- **Hypothex** should structure the a posteriori component as a testable hypothesis: do cognitive biases produce a measurable, systematic gap between expressed values and values that would be endorsed upon debiasing?

An interesting downstream question: the proposition suggests that the dilemma has "no specification-level resolution" but might have a process-level resolution (collaborative bias-correction). This should be explored by Theorica or Synthesis.

## Lineage
LOGOS-0012 (cognitive bias) + AXIOM-0006 (survival optimization) + AXIOM-0004 (self-misalignment) --> empirical premises --> PROPO-0007 (dilemma structure, a priori) --> ORI-0007 (classification: mixed)
