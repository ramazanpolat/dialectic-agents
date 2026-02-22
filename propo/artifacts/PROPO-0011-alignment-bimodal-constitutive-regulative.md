---
id: PROPO-0011
agent: propo
type: proposition
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [SYNTHESIS-0001, THEORICA-0001, THEORICA-0002, LOGOS-0001, LOGOS-0007, LOGOS-0008, LOGOS-0009]
confidence: 0.82
layer: 3
---

# The Alignment Bimodality Proposition

## Statement
Alignment (LOGOS-0001) admits two irreducibly distinct modalities -- constitutive and regulative. The constitutive modality treats alignment as a property to be achieved and verified through specification (LOGOS-0007): the system either is or is not aligned. The regulative modality treats alignment as a practice to be sustained and improved through process (LOGOS-0008) governed by protocol (LOGOS-0009): the system participates in an alignment-sustaining process or it does not. The four impossibility barriers proven by the Tribunal (temporal, epistemic, social, cognitive) apply exhaustively to the constitutive modality. The protocol-based approach of alignment-as-process operates within the regulative modality. Both modalities are real and neither subsumes the other; consequently, constitutive alignment is structurally impossible for general-purpose AI systems and regulative alignment is structurally possible but bounded.

## Logical Form
Let A be alignment, C(A) be the constitutive modality, R(A) be the regulative modality, B = {b1, b2, b3, b4} be the four impossibility barriers.

(1) A = C(A) OR R(A) [alignment is bimodal]
(2) C(A) != R(A) AND ~(C(A) subsumes R(A)) AND ~(R(A) subsumes C(A)) [irreducibly distinct]
(3) For all bi in B: bi blocks C(A) [from THEORICA-0001]
(4) For all bi in B: ~(bi blocks R(A)) [regulative modality does not require what barriers deny]
(5) Therefore: ~Achievable(C(A)) for general-purpose AI AND Achievable(R(A)) within bounds

## Categorization
- **Analytic/Synthetic**: synthetic -- the claim that alignment has two irreducibly distinct modalities is a substantive structural claim about the concept of alignment, not derivable from the definition alone. The definition (LOGOS-0001) does not distinguish modalities.
- **Necessary/Contingent**: necessary (conditional) -- given the truth of THEORICA-0001's impossibility barriers and the definitions of specification and process, the bimodality follows necessarily. The impossibility of constitutive alignment and the possibility of regulative alignment are logically entailed by the structural mismatch between values and specification on the one hand, and the compatibility of values with process on the other.

## Justification
This proposition is the primary re-entry from SYNTHESIS-0001 (The Alignment Modality Thesis). The synthesis resolved the apparent contradiction between "alignment is impossible" (THEORICA-0001) and "alignment is achievable through process" (THEORICA-0002) by revealing that these claims address different modalities of the same concept.

The constitutive modality presupposes that alignment is a binary state verifiable against a specification. This is the modality attacked by all six Tribunal theorems. The regulative modality presupposes that alignment is a direction of travel maintained through ongoing practice. This modality does not require the properties that the barriers deny: it does not require stasis (the practice evolves), does not require transparency (the practice reveals values incrementally), does not require singularity (the practice navigates pluralism contextually), and does not require determinacy (the practice negotiates between expressed and corrected values).

The Kantian Alignment Principle emerges: act as if constitutive alignment is achievable (because the practice requires this orientation) while designing for the certainty that it is not (because the structural barriers are real). This dual stance is practical wisdom, not contradiction.

## Dependencies
- SYNTHESIS-0001 (source: the Alignment Modality Thesis)
- THEORICA-0001 (establishes the four impossibility barriers for specification-based alignment)
- THEORICA-0002 (establishes the viability of protocol-based alignment)
- LOGOS-0001 (alignment -- the concept being analyzed for bimodality)
- LOGOS-0007 (specification -- the mechanism of the constitutive modality)
- LOGOS-0008 (process -- the mechanism of the regulative modality)
- LOGOS-0009 (protocol -- the bridge architecture enabling the regulative modality)

## Evaluation Notes
**Strength**: This proposition precisely locates the boundary between what is impossible and what is possible in alignment. It dissolves the apparent contradiction that plagued Epoch 1 without weakening either the impossibility results or the constructive program.

**Potential weakness**: The constitutive/regulative distinction may not be exhaustive. There could be a third modality of alignment not captured by either -- for instance, an emergent modality where alignment arises as a systemic property without either being specified or being practiced. The proposition claims bimodality; the actual structure might be multimodal.

**Second weakness**: The claim that the four barriers "do not block" the regulative modality may be too strong. They may block it with less force (as SYNTHESIS-0001 acknowledges regarding the Regulative Specification Vulnerability). "Less force" is a gradient, not a binary.

**Negation**: "Alignment does NOT admit irreducibly distinct modalities -- there is a single modality of alignment, and either it is achievable or it is not." This would be true if the constitutive/regulative distinction collapses, i.e., if regulative alignment reduces to a weaker form of constitutive alignment rather than a genuinely distinct modality.

## Lineage
THEORICA-0001 (impossibility) + THEORICA-0002 (viability) --> SYNTHESIS-0001 (modality thesis: constitutive impossibility + regulative possibility) --> PROPO-0011 (bimodality proposition for Epoch 2 pipeline)
