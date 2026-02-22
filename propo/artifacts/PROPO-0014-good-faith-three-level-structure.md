---
id: PROPO-0014
agent: propo
type: proposition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [SYNTHESIS-0002, LOGOS-0010, LOGOS-0011, LOGOS-0013, AXIOM-0008, TRIBUNAL-0002]
confidence: 0.75
layer: 3
---

# The Three-Level Good Faith Proposition

## Statement
Good faith (LOGOS-0010) in alignment processes exists on three functionally distinct levels: Level 1 -- behavioral good faith (mechanism-producible through protocol design and incentive structures per AXIOM-0008), Level 2 -- epistemic good faith (cultivatable through sustained practice of Level 1, involving genuine internalization of cooperative norms), and Level 3 -- constitutive good faith (requiring deep epistemic transformation per LOGOS-0011 such that even identity-proximate beliefs per LOGOS-0013 become revisable). Mechanism design can substitute for Level 1 but not for Levels 2 or 3. The three levels form a developmental sequence in which well-designed mechanisms scaffold the emergence of genuine dispositions, and the dialectical ceiling's (TRIBUNAL-0002) height for a given population is determined by the distribution of agents across these three levels.

## Logical Form
Let GF1 be behavioral good faith, GF2 be epistemic good faith, GF3 be constitutive good faith, MD be mechanism design, DC be the dialectical ceiling height, Pop be a population of agents.

(1) GF = GF1 OR GF2 OR GF3 [good faith is tripartite]
(2) MD can produce GF1 [mechanism design suffices for behavioral compliance]
(3) MD cannot produce GF2 OR GF3 [genuine internalization cannot be engineered]
(4) GF1 scaffolds GF2 scaffolds GF3 [developmental sequence]
(5) DC(Pop) is proportional to distribution of Pop across {GF1, GF2, GF3}
(6) Pop at GF1: low DC (procedural compliance only)
(7) Pop at GF2: moderate DC (synthesis except on identity-protected beliefs)
(8) Pop at GF3: maximum DC (limited only by irreducible tragic conflicts per AXIOM-0011)

## Categorization
- **Analytic/Synthetic**: mixed -- the three-level structure is derivable conceptually from the definitions of good faith (LOGOS-0010), epistemic humility (LOGOS-0011), and identity-protected belief (LOGOS-0013). The developmental sequence claim (Level 1 scaffolds Level 2 scaffolds Level 3) is a posteriori -- it is an empirical claim about how dispositions develop through practice.
- **Necessary/Contingent**: contingent -- the developmental sequence is an empirical claim that could be falsified (behavioral compliance might never produce genuine internalization). The tripartite structure itself is more robust, as it follows from the conceptual distinctions already present in the definitions.

## Justification
SYNTHESIS-0002 resolved the binary opposition between "good faith is necessary for alignment" (thesis: TRIBUNAL-0002) and "mechanism design can substitute for good faith" (antithesis: HYPOTHEX-0003) by showing that both are correct about different levels of a graduated phenomenon.

The three levels correspond to progressively deeper forms of the disposition:
- **Level 1** involves behavioral compliance without internalization. The agent follows rules because defection is costly, not because it values the shared goal. This is sufficient for basic protocol functioning but insufficient for genuine synthesis.
- **Level 2** involves internalization of cooperative norms. Through repeated positive interactions (as predicted by AXIOM-0008's tit-for-tat dynamics in iterated settings), the agent develops genuine dispositions to engage honestly. This is sufficient for dialectical synthesis on most topics.
- **Level 3** involves the conjunction of good faith and deep epistemic humility -- the agent holds even identity-constitutive beliefs with enough tentativeness to engage dialectically about them. This is the threshold at which the dialectical ceiling approaches its maximum.

The connection to the dialectical ceiling (TRIBUNAL-0002) provides the key empirical implication: the ceiling's height is not a fixed property of the alignment system but a function of participants' good-faith distribution. This means the ceiling is expandable through cultivation of higher-level good faith, but the expansion has diminishing returns and a hard limit at irreducible tragic conflicts.

## Dependencies
- SYNTHESIS-0002 (source: the Emergent Good Faith Thesis)
- LOGOS-0010 (good faith -- the disposition being graduated)
- LOGOS-0011 (epistemic humility -- the component that distinguishes Level 3)
- LOGOS-0013 (identity-protected belief -- the barrier that Level 3 addresses)
- AXIOM-0008 (tit-for-tat cooperation -- the mechanism that bootstraps Level 1)
- TRIBUNAL-0002 (dialectical ceiling -- the constraint whose height depends on the level distribution)

## Evaluation Notes
**Strength**: This proposition dissolves the binary good-faith debate and provides an actionable framework: design for Level 1, cultivate toward Level 2, aspire to Level 3. It also provides a metric (dialectical ceiling height as a function of level distribution) that could in principle be measured.

**Critical weakness -- the Level 2 emergence gap**: The proposition claims that Level 1 scaffolds Level 2, but provides no mechanism for this emergence. It is possible that behavioral compliance never produces genuine internalization -- that agents who cooperate only because defection is costly never develop genuine cooperative dispositions. The psychological literature on cognitive dissonance and habit formation provides some support (behavior shapes attitude over time), but the evidence is not conclusive for the specific case of alignment processes.

**Second weakness -- Level 3 accessibility**: The proposition provides no mechanism for cultivating Level 3 beyond "sustained practice of Level 2." For many agents and many beliefs, Level 3 may be permanently inaccessible, making the maximum dialectical ceiling a theoretical upper bound with little practical relevance.

**Negation**: "Good faith is NOT graduated but binary -- an agent either operates in good faith or does not, and mechanism design either suffices as a substitute or it does not." This would be true if the behavioral/epistemic/constitutive distinctions are not functionally significant for the alignment process.

## Lineage
TRIBUNAL-0002 (dialectical ceiling) + HYPOTHEX-0003 (mechanism design alternative) --> SYNTHESIS-0002 (three-level good faith resolution) --> PROPO-0014 (three-level good faith proposition for Epoch 2)
