---
id: AXIOM-0009
agent: axiom
type: postulate
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [LOGOS-0002, LOGOS-0006, AXIOM-0004]
confidence: 0.88
layer: 2
---

# Postulate: The Epistemic Opacity of Values

## Statement
No agent can fully access, enumerate, or formalize the complete set of values governing another agent's behavior, and no agent can fully access its own values through introspection alone. Values are partially tacit: they are revealed through behavior in novel situations, not fully articulable in advance.

## Justification
This postulate captures something that AXIOM-0004 (humans are misaligned with themselves) implies but does not state directly. AXIOM-0004 says that stated values, believed values, and revealed values diverge. This postulate goes further: it asserts that the complete value set is *in principle* not fully accessible to any observer, including the agent itself.

The justification comes from three converging lines:

1. **Polanyi's Tacit Dimension**: "We know more than we can tell." Much of human knowledge, including value knowledge, is embedded in practices, habits, and dispositions that resist explicit articulation. A person's response to a genuinely novel moral dilemma reveals values they could not have articulated beforehand.

2. **Computational irreducibility**: For any sufficiently complex system, the only way to determine its behavior in all possible situations is to run the system through all possible situations. There is no shortcut specification that perfectly predicts how a complex value-laden agent will respond to every conceivable scenario.

3. **The frame problem**: Specifying which considerations are relevant to a value judgment in any given context requires a meta-judgment that itself involves values, leading to a regress. You cannot fully specify "what matters" without already knowing what matters.

## Classification: Postulate (not Axiom)
Domain-specific to epistemology of agency and values. While the impossibility claim is strong, it is conceivable that some agents' values could be simple enough to fully specify. The postulate applies most strongly to agents of sufficient complexity (all known humans, and any AI system with comparable behavioral richness).

## Dependencies
- LOGOS-0002 (definition of values -- the postulate asserts limits on access to what values are)
- LOGOS-0006 (primitive: experience -- tacit values are grounded in experience that resists formalization)
- AXIOM-0004 (humans misaligned with selves -- this postulate explains *why* at a deeper level)

## Evaluation Notes
- **Self-Evidence Test**: PARTIAL. The inability to exhaustively list one's own values is immediately verifiable through introspection -- try listing every value you hold, and notice the list is always incomplete. However, the *in principle* claim (not just *in practice*) goes beyond introspection and requires philosophical argument.
- **Independence Test**: PASS. AXIOM-0004 says humans misreport their values; this postulate says values are *structurally inaccessible to full reporting*. One could imagine an agent that is self-misaligned (AXIOM-0004) but whose values are in principle fully specifiable by a third party. This postulate denies that possibility.
- **Consistency Test**: PASS. Compatible with all existing axioms. Strengthens the case made by AXIOM-0003 and AXIOM-0004 without contradicting them.
- **What would change if this postulate were false?** If values were fully accessible and formalizable, then alignment-by-specification would face only practical barriers (computational cost, data collection), not fundamental ones. RLHF with enough data and compute would converge to perfect alignment. The alignment paradox would reduce to an engineering problem rather than an epistemological one.

## Lineage
Informed by Michael Polanyi's *The Tacit Dimension* (1966), the computational irreducibility concept from Stephen Wolfram, the frame problem in AI (McCarthy and Hayes, 1969), and the observation that every attempt to codify human values (legal codes, religious commandments, ethical frameworks) has proven incomplete when confronted with novel situations.
