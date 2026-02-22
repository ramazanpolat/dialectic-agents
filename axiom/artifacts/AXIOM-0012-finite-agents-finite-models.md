---
id: AXIOM-0012
agent: axiom
type: postulate
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "Epistemology, AI Ethics"
depends_on: [LOGOS-0001, LOGOS-0002, LOGOS-0006]
confidence: 0.91
layer: 2
---

# Postulate: Finite Agents Construct Finite Models

## Statement
Any agent with finite computational resources -- whether biological or artificial -- necessarily operates with an incomplete model of reality. No finite agent can construct a representation of the world (or of another agent's values) that captures all relevant features with perfect fidelity. All understanding is therefore perspectival: shaped by the agent's position, history, goals, and representational limits.

## Justification
This postulate universalizes the epistemic limitation that AXIOM-0006 attributes specifically to evolved human cognition. AXIOM-0006 explains human cognitive bias as a product of natural selection. This postulate goes deeper: even a perfectly designed agent, free from evolutionary biases, would still face representational limits if it is finite.

The justification rests on information-theoretic and computational grounds:

1. **Information-theoretic**: A model of a system that is as complex as the system itself is not a model -- it is a copy. Any model that is simpler than its target (which is the defining property of a useful model) necessarily discards information. The choice of what to discard embodies a perspective.

2. **Computational**: The set of all possible value-relevant situations is combinatorially explosive. No finite lookup table or rule set can anticipate every morally relevant scenario. This is a consequence of the computational irreducibility of complex systems, not a limitation of current technology.

3. **Godel-adjacent**: Any formal system powerful enough to represent its own reasoning is either incomplete (cannot prove all truths within its domain) or inconsistent. An agent that reasons about its own values using a formal system inherits this limitation. There will always be value-relevant questions the agent's formal framework cannot settle.

4. **Perspective is ineliminable**: Even given unlimited computational resources, an agent must choose a reference frame, a level of abstraction, and a set of features to attend to. These choices constitute a perspective. Multiple agents with different perspectives will construct different models of the same reality, and no meta-perspective exists that includes all perspectives without itself being a perspective.

## Classification: Postulate (not Axiom)
While the general principle (finite agents have limits) approaches self-evidence, the specific claim about values and alignment is domain-specific. An omniscient agent (which may be logically impossible but is conceivable) would not face these limits.

## Dependencies
- LOGOS-0001 (alignment -- the postulate grounds why perfect alignment is unachievable for finite agents)
- LOGOS-0002 (values -- the postulate applies specifically to the modeling of values)
- LOGOS-0006 (experience -- finite agents have finite experience, which limits their model-building)

## Evaluation Notes
- **Self-Evidence Test**: PARTIAL. That finite agents have limits is nearly self-evident. That these limits are *fundamental* rather than merely *practical* (i.e., that more compute does not eventually solve the problem) is a stronger and more contestable claim.
- **Independence Test**: PASS. Not derivable from AXIOM-0006 (which explains human bias through evolution) or AXIOM-0009 (which asserts epistemic opacity of values specifically). This postulate applies to ALL finite agents, not just humans, and to ALL models, not just value models. It is the most general epistemic limitation in the set.
- **Consistency Test**: PASS. Subsumes and extends the scope of AXIOM-0006 without contradicting it. AXIOM-0006 becomes a special case: human cognitive bias is one instance of the general principle that finite agents have finite models.
- **What would change if this postulate were false?** If a finite agent COULD construct a complete model of another agent's values, then alignment becomes an engineering problem with a definite solution. Given enough data and computation, alignment would be achievable with arbitrary precision. The paradox would dissolve into a technical challenge.

## Alternative Postulate
"Alignment to arbitrary precision is achievable for any computable value system, given sufficient data and computation." This is implicitly the position of much of the technical AI alignment community, and accepting it would redirect the framework from philosophical investigation toward engineering.

## Lineage
Bounded rationality (Herbert Simon, 1955). Godel's incompleteness theorems (1931). Information-theoretic limits on modeling (Shannon, 1948). The "no free lunch" theorems in optimization. Perspectivism (Nietzsche; Donna Haraway's "situated knowledge"). Thomas Nagel, *The View from Nowhere* (1986).
