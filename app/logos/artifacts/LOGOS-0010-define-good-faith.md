---
id: LOGOS-0010
agent: logos
type: definition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0002, LOGOS-0009, LOGOS-0006]
confidence: 0.80
layer: 1
---

# Definition: Good Faith

## Statement
**Good faith** (noun phrase): A disposition of an agent participating in a protocol (LOGOS-0009) or process (LOGOS-0008) such that the agent (a) sincerely intends to achieve the shared epistemic or practical goals of that protocol, (b) represents its own positions, evidence, and reasoning honestly rather than strategically, and (c) remains willing to revise its positions when presented with sufficient reason to do so.

## Justification
Good faith is a prerequisite for any dialectical process (LOGOS-0004) to function. Without it, thesis and antithesis are not genuine positions to be resolved — they are strategic moves in a competitive game. The Alignment Paradox depends on this concept because alignment-as-process requires ongoing negotiation between humans and AI systems. If either party operates in bad faith — concealing its actual objectives, misrepresenting evidence, or refusing to update — the process degenerates.

Good faith has three components, all required:
1. **Sincerity of intent** — the agent actually wants the shared goal, not a private substitute
2. **Honesty of representation** — the agent's expressed reasoning reflects its actual reasoning
3. **Willingness to revise** — the agent treats its own positions as provisional, not sacred

## Genus and Differentia
- **Genus**: A disposition of an agent in interaction
- **Differentia**: Distinguished from politeness by requiring *substantive honesty* (not merely surface courtesy); distinguished from obedience by requiring *genuine agreement* (not compliance under coercion); distinguished from open-mindedness by requiring *active participation toward shared goals* (not merely passive receptivity); distinguished from naivete by not requiring trust in the other party — an agent can act in good faith while maintaining skepticism about whether the other agent does likewise

## Positive Example
A scientist who publishes results that contradict her own earlier theory, explains clearly why the earlier theory was wrong, and proposes a revised theory is acting in good faith. She is sincere (she wants truth, not reputation defense), honest (she admits the earlier theory's failure), and willing to revise (she updates her position).

## Negative Example
A debater who argues for a position she privately believes is false, in order to win a competition, is NOT acting in good faith — even if her arguments are logically valid. The sincerity condition fails: her actual goal (winning) diverges from the shared goal (finding truth).

## Dependencies
- LOGOS-0002 (values) — good faith involves aligning one's conduct with epistemic values
- LOGOS-0009 (protocol) — good faith is a disposition required for protocols to function as intended
- LOGOS-0006 (experience) — whether good faith requires conscious experience (can an AI act in good faith?) is an open question

## Evaluation Notes
The hardest question this definition raises: can an AI system act in good faith? Good faith requires sincerity of intent, but it is unclear whether AI systems have "intentions" in the relevant sense, or whether they can "sincerely" pursue goals. If good faith requires experience (LOGOS-0006), and AI systems lack experience, then alignment-as-process may be structurally asymmetric — humans can participate in good faith, but AI systems can only simulate it.

This definition may be too demanding. It requires willingness to revise, but some values (LOGOS-0002) may be non-negotiable for an agent without constituting bad faith. A pacifist who refuses to revise her commitment to nonviolence is not necessarily acting in bad faith. The definition may need a clause distinguishing between revisable and constitutive commitments.

## Lineage
Derived from the need to articulate the conditions under which dialectical processes (LOGOS-0004) and alignment protocols (LOGOS-0009) can function. Informed by the Alignment Paradox's requirement that alignment be a cooperative rather than adversarial relationship.
