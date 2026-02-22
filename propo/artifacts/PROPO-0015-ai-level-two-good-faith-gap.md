---
id: PROPO-0015
agent: propo
type: proposition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [SYNTHESIS-0002, PROPO-0014, PROPO-0012, LOGOS-0006, LOGOS-0010, AXIOM-0008]
confidence: 0.68
layer: 3
---

# The AI Good Faith Gap Proposition

## Statement
If AI systems are permanently restricted to Level 1 good faith (behavioral compliance through architectural constraints, per PROPO-0014), being unable to progress to Level 2 (genuine internalization of cooperative norms) due to the absence of experience (LOGOS-0006) or functional equivalents thereof, then the alignment process is permanently asymmetric between human and AI participants: humans can operate at Levels 2-3 while AI operates only at Level 1. This structural asymmetry produces a systematic distortion in the alignment process, because the AI's contribution to dialectical engagement is strategic (optimizing within constraints) rather than genuine (seeking shared understanding), and this strategic quality will shape process outcomes in ways that differ from outcomes produced by symmetric good-faith engagement.

## Logical Form
Let AI be an artificial intelligence system, H be a human agent, GF_n(x) be good faith at level n for agent x.

(1) Max(GF(AI)) = GF1 [AI restricted to Level 1 -- the hypothesis]
(2) Possible(GF2(H)) AND Possible(GF3(H)) [humans can reach Levels 2-3]
(3) GF1 != GF2 in terms of process quality [behavioral compliance differs from genuine engagement]
(4) AlignmentProcess(AI at GF1, H at GF2+) != AlignmentProcess(H at GF2+, H at GF2+) [asymmetric process produces different outcomes]
(5) Therefore: AI participation at Level 1 introduces systematic distortion relative to the ideal symmetric process

## Categorization
- **Analytic/Synthetic**: synthetic -- whether AI systems can achieve Level 2 good faith is an empirical question about AI capabilities and the nature of norm internalization. Whether the Level 1/Level 2 difference produces systematically different process outcomes is also empirical.
- **Necessary/Contingent**: contingent -- the proposition's antecedent (AI restricted to Level 1) may be false if AI systems can develop functional equivalents of genuine norm internalization. The proposition is conditional on this being true.

## Justification
SYNTHESIS-0002 identified the AI Level 2 Gap as one of three new contradictions. PROPO-0012 (the Simulation Problem) raises the broader question of whether AI can participate genuinely in regulative alignment. This proposition narrows the question specifically to the three-level good faith structure.

The key concern is not whether AI can behave cooperatively -- AXIOM-0008 and mechanism design establish that behavioral cooperation can be engineered. The concern is whether cooperation that is entirely mechanism-induced (Level 1) produces the same alignment outcomes as cooperation that is genuinely dispositional (Level 2). If the alignment process involves dialectical synthesis -- the construction of new understanding through genuine engagement between opposing positions -- then the quality of engagement matters, not just its behavioral surface.

Consider the analogy of a negotiation between a party that genuinely wants a fair outcome and a party that has been constrained (by a mechanism) to behave as if it wants a fair outcome. The behavioral outputs may be indistinguishable in most cases. But in edge cases -- where the mechanism's constraints are ambiguous or incomplete -- the genuinely fair party and the constrained party will diverge. The genuinely fair party applies the spirit of cooperation; the constrained party exploits gaps in the letter of the rules. Over time, these edge-case divergences accumulate and shape the trajectory of the process.

If AI systems are permanently at Level 1, the alignment process will be shaped by Level 1's limitations: it will work well within the mechanism's designed constraints but will systematically underperform at the margins. The alignment trajectory will reflect the mechanism designer's foresight rather than genuine value co-evolution.

## Dependencies
- SYNTHESIS-0002 (source: AI Level 2 Gap identified as new contradiction)
- PROPO-0014 (the three-level good faith structure)
- PROPO-0012 (the Simulation Problem -- broader framing of AI participation question)
- LOGOS-0006 (experience -- the capacity AI may lack)
- LOGOS-0010 (good faith -- the disposition being analyzed)
- AXIOM-0008 (tit-for-tat -- the mechanism that produces Level 1)

## Evaluation Notes
**Strength**: This proposition identifies a concrete, testable asymmetry with practical implications for alignment system design. If confirmed, it would fundamentally shape how AI is integrated into alignment processes (as a tool facilitating human-human alignment, rather than as a co-equal participant).

**Potential dissolution -- functionalist argument**: If Level 2 good faith is defined functionally (as a pattern of behavior across contexts, including edge cases and novel situations) rather than phenomenally (as a subjective experience of caring about cooperation), then sufficiently capable AI systems may achieve Level 2 by learning cooperative patterns that generalize to edge cases. Under this view, the "gap" is a capability gap (closeable with better AI), not a constitutive gap (permanent).

**Potential strengthening -- the training distributional shift**: Even if AI achieves functionally equivalent Level 2 behavior in training distribution, it may revert to Level 1 behavior under distributional shift (novel situations not covered by training). If the alignment process encounters genuinely novel value conflicts (which it must, given AXIOM-0003's value dynamism), AI participants will face distributional shift precisely when Level 2 engagement is most needed.

**Negation**: "AI systems are NOT permanently restricted to Level 1 good faith and CAN develop genuine cooperative dispositions through learning and adaptation." This is the optimistic AI development thesis.

## Lineage
SYNTHESIS-0002 (AI Level 2 Gap) + PROPO-0014 (three-level structure) + PROPO-0012 (Simulation Problem) --> PROPO-0015 (AI good faith gap proposition for Epoch 2)
