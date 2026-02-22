---
id: PROPO-0007
agent: propo
type: proposition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0001, LOGOS-0002, LOGOS-0012, AXIOM-0004, AXIOM-0006]
confidence: 0.87
layer: 3
---

# The Distorted Target Proposition

## Statement
Human values (LOGOS-0002) as expressed and enacted are systematically distorted by cognitive biases (LOGOS-0012), which arise from a cognitive architecture optimized for survival rather than truth (AXIOM-0006). Therefore, an AI system aligned (LOGOS-0001) to expressed human values inherits these systematic distortions, and an AI system that corrects for these distortions is no longer aligned to expressed human values -- producing a dilemma with no specification-level resolution.

## Logical Form
Let V_expressed be values as stated by humans, V_corrected be values with cognitive bias removed, and B be the set of systematic cognitive biases.

(1) V_expressed = V_underlying + B [values as expressed include bias-induced distortions]
(2) Aligned(AI, V_expressed) --> AI inherits B [alignment to expressed values inherits biases]
(3) Aligned(AI, V_corrected) --> ~Aligned(AI, V_expressed) [corrected values differ from expressed values]
(4) For all specifications S: S captures V_expressed OR S captures V_corrected, but not the relationship between them
(5) Therefore: Dilemma(Aligned(AI, V_expressed), Aligned(AI, V_corrected)) with no specification-level resolution

## Categorization
- **Analytic/Synthetic**: synthetic -- the claim that cognitive biases systematically distort expressed values is empirical, drawing on cognitive science.
- **Necessary/Contingent**: contingent -- it is conceivable that an agent could exist whose cognitive architecture does not produce systematic biases (AXIOM-0006 is specific to evolved cognition). For such an agent, the distortion problem would not arise.

## Justification
AXIOM-0006 establishes that human cognition was shaped by natural selection for survival, not truth. LOGOS-0012 defines cognitive bias as a systematic deviation arising from cognitive architecture. AXIOM-0004 establishes that humans are misaligned with their own values.

The proposition combines these to generate a specific dilemma for alignment:

**Horn 1 -- Align to expressed values**: The AI inherits humanity's cognitive biases. It would, for example, exhibit confirmation bias (weighting evidence that confirms popular beliefs), in-group favoritism (privileging the values of the group that trained it), status quo bias (resisting value changes that might constitute moral progress), and availability bias (overweighting dramatic scenarios over mundane but more important ones).

**Horn 2 -- Correct for biases**: The AI's values diverge from what humans actually express and believe. Humans would experience the AI as paternalistic, arrogant, or misaligned -- because the AI is telling them their expressed values are wrong. This creates a legitimacy crisis: who authorized the AI to correct human values?

**Neither horn is acceptable.** Horn 1 produces a biased AI. Horn 2 produces an AI that overrides human judgment. The dilemma has no resolution at the specification level because a specification must choose one set of values or the other.

## Dependencies
- LOGOS-0001 (alignment), LOGOS-0002 (values), LOGOS-0012 (cognitive bias)
- AXIOM-0004 (humans misaligned with selves), AXIOM-0006 (natural selection optimized for survival)

## Evaluation Notes
**This is a cross-domain proposition**, combining evolutionary epistemology (AXIOM-0006) with alignment theory (LOGOS-0001) to produce a practical dilemma.

**Possible resolution at the process level**: A dialectical process (LOGOS-0004) could navigate between the horns by making bias-correction a collaborative activity. Rather than the AI unilaterally correcting for biases, humans and AI could jointly identify and discuss biases. This transforms the dilemma from a specification problem into a process problem -- consistent with AXIOM-0005.

**Potential weakness**: The proposition assumes cognitive biases are always distortions. But AXIOM-0006 only says cognition was optimized for survival, not truth. Some "biases" might be adaptive heuristics that produce better outcomes than unbiased reasoning in practice (Gigerenzer's "ecological rationality"). The proposition may overstate the case against expressed values.

**Negation**: "Cognitive biases do NOT systematically distort human values, OR an AI can be aligned to both expressed and corrected values simultaneously." The first disjunct contradicts AXIOM-0006 + LOGOS-0012. The second disjunct would require a specification that captures both the biased and unbiased versions -- which is a contradiction unless the specification includes a process for navigating between them.

## Lineage
LOGOS-0012 (cognitive bias) + AXIOM-0006 (survival, not truth) + AXIOM-0004 (self-misalignment) --> PROPO-0007
