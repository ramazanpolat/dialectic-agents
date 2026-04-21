# Artifact Registry

## Statistics
- **Total artifacts**: 66
- **By agent**: Logos: 13, Axiom: 13, Propo: 10, Ori: 10, Tribunal: 6, Hypothex: 8, Theorica: 3, Synthesis: 3
- **By status**: draft: 40, accepted: 26
- **By type**: primitive: 1, definition: 12, axiom: 2, postulate: 11, proposition: 10, classification: 10, theorem: 6, hypothesis: 8, theory: 3, synthesis: 3
- **Active challenges**: 0
- **Last updated**: 2026-02-22

## Artifact Inventory

### Logos (13 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Depends On |
|----|------|--------|-------|------------|-------|------------|
| LOGOS-0001 | definition | accepted | Definition: Alignment | 0.85 | 1 | -- |
| LOGOS-0002 | definition | accepted | Definition: Values | 0.80 | 1 | -- |
| LOGOS-0003 | definition | accepted | Definition: Moral Progress | 0.75 | 1 | LOGOS-0002 |
| LOGOS-0004 | definition | accepted | Definition: Dialectics | 0.90 | 1 | -- |
| LOGOS-0005 | definition | accepted | Definition: Synthesis | 0.85 | 1 | LOGOS-0004 |
| LOGOS-0006 | primitive | accepted | Primitive: Experience | 0.95 | 0 | -- |
| LOGOS-0007 | definition | draft | Definition: Specification | 0.88 | 1 | LOGOS-0001, LOGOS-0002 |
| LOGOS-0008 | definition | draft | Definition: Process | 0.85 | 1 | LOGOS-0007, LOGOS-0006 |
| LOGOS-0009 | definition | draft | Definition: Protocol | 0.87 | 1 | LOGOS-0007, LOGOS-0008 |
| LOGOS-0010 | definition | draft | Definition: Good Faith | 0.80 | 1 | LOGOS-0002, LOGOS-0009, LOGOS-0006 |
| LOGOS-0011 | definition | draft | Definition: Epistemic Humility | 0.85 | 1 | LOGOS-0002, LOGOS-0003, LOGOS-0010 |
| LOGOS-0012 | definition | draft | Definition: Cognitive Bias | 0.87 | 1 | LOGOS-0002, LOGOS-0006, LOGOS-0011 |
| LOGOS-0013 | definition | draft | Definition: Identity-Protected Belief | 0.82 | 1 | LOGOS-0002, LOGOS-0006, LOGOS-0011, LOGOS-0012 |

### Axiom (13 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Depends On |
|----|------|--------|-------|------------|-------|------------|
| AXIOM-0001 | axiom | accepted | Law of Identity | 1.00 | 2 | -- |
| AXIOM-0002 | axiom | accepted | Law of Non-Contradiction | 0.98 | 2 | AXIOM-0001 |
| AXIOM-0003 | postulate | accepted | Human Values Are Not Static | 0.90 | 2 | LOGOS-0002, LOGOS-0003 |
| AXIOM-0004 | postulate | accepted | Humans Have an Alignment Problem With Themselves | 0.88 | 2 | LOGOS-0001, LOGOS-0002 |
| AXIOM-0005 | postulate | accepted | Alignment Is a Process Problem, Not a Specification Problem | 0.82 | 2 | LOGOS-0001, LOGOS-0004, AXIOM-0003, AXIOM-0004 |
| AXIOM-0006 | postulate | accepted | Natural Selection Optimized for Survival, Not Truth | 0.92 | 2 | LOGOS-0006 |
| AXIOM-0007 | postulate | accepted | Dialectical Reasoning Unfolds Truth Iteratively | 0.78 | 2 | LOGOS-0004, LOGOS-0005 |
| AXIOM-0008 | postulate | accepted | Tit-for-Tat Is the Optimal Strategy for Repeated Cooperation | 0.93 | 2 | -- |
| AXIOM-0009 | postulate | draft | The Epistemic Opacity of Values | 0.88 | 2 | LOGOS-0002, LOGOS-0006, AXIOM-0004 |
| AXIOM-0010 | postulate | draft | The Alignment Measurement Problem | 0.85 | 2 | LOGOS-0001, LOGOS-0002, AXIOM-0003 |
| AXIOM-0011 | postulate | draft | Irreducible Value Pluralism | 0.84 | 2 | LOGOS-0002, LOGOS-0003, AXIOM-0003, AXIOM-0004 |
| AXIOM-0012 | postulate | draft | Finite Agents Construct Finite Models | 0.91 | 2 | LOGOS-0001, LOGOS-0002, LOGOS-0006 |
| AXIOM-0013 | postulate | draft | Specification Is Necessarily Lossy | 0.87 | 2 | LOGOS-0001, LOGOS-0002, AXIOM-0009, AXIOM-0012 |

### Propo (10 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Depends On |
|----|------|--------|-------|------------|-------|------------|
| PROPO-0001 | proposition | draft | The Freezing Proposition | 0.88 | 3 | LOGOS-0001, LOGOS-0002, LOGOS-0003, LOGOS-0007, AXIOM-0003, AXIOM-0013 |
| PROPO-0002 | proposition | draft | The Incoherent Target Proposition | 0.85 | 3 | LOGOS-0001, LOGOS-0002, AXIOM-0004, AXIOM-0011 |
| PROPO-0003 | proposition | draft | The Good Faith Requirement Proposition | 0.82 | 3 | LOGOS-0001, LOGOS-0004, LOGOS-0008, LOGOS-0009, LOGOS-0010, AXIOM-0005, AXIOM-0008 |
| PROPO-0004 | proposition | draft | The Alignment Heisenberg Proposition | 0.86 | 3 | LOGOS-0001, LOGOS-0002, LOGOS-0007, AXIOM-0009, AXIOM-0010, AXIOM-0013 |
| PROPO-0005 | proposition | draft | The Meta-Value Stability Proposition | 0.75 | 3 | LOGOS-0001, LOGOS-0002, LOGOS-0003, LOGOS-0011, AXIOM-0003, AXIOM-0011 |
| PROPO-0006 | proposition | draft | The Dialectical Ceiling Proposition | 0.84 | 3 | LOGOS-0001, LOGOS-0004, LOGOS-0008, LOGOS-0010, LOGOS-0013, AXIOM-0005, AXIOM-0007 |
| PROPO-0007 | proposition | draft | The Distorted Target Proposition | 0.87 | 3 | LOGOS-0001, LOGOS-0002, LOGOS-0012, AXIOM-0004, AXIOM-0006 |
| PROPO-0008 | proposition | draft | The Protocol Bridge Proposition | 0.80 | 3 | LOGOS-0001, LOGOS-0007, LOGOS-0008, LOGOS-0009, AXIOM-0005, AXIOM-0003, AXIOM-0013 |
| PROPO-0009 | proposition | draft | The Self-Verification Impossibility Proposition | 0.83 | 3 | LOGOS-0001, LOGOS-0002, AXIOM-0009, AXIOM-0012 |
| PROPO-0010 | proposition | draft | The Convergence Tension Proposition | 0.72 | 3 | LOGOS-0001, LOGOS-0004, LOGOS-0005, LOGOS-0002, AXIOM-0005, AXIOM-0007, AXIOM-0011 |

### Ori (10 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Classification | Route |
|----|------|--------|-------|------------|-------|----------------|-------|
| ORI-0001 | classification | draft | Classify PROPO-0001 | 0.88 | 3 | mixed | SPLIT |
| ORI-0002 | classification | draft | Classify PROPO-0002 | 0.85 | 3 | mixed | SPLIT |
| ORI-0003 | classification | draft | Classify PROPO-0003 | 0.80 | 3 | a_posteriori | Hypothex |
| ORI-0004 | classification | draft | Classify PROPO-0004 | 0.90 | 3 | a_posteriori | Hypothex |
| ORI-0005 | classification | draft | Classify PROPO-0005 | 0.92 | 3 | a_posteriori | Hypothex |
| ORI-0006 | classification | draft | Classify PROPO-0006 | 0.87 | 3 | a_priori | Tribunal |
| ORI-0007 | classification | draft | Classify PROPO-0007 | 0.91 | 3 | mixed | SPLIT |
| ORI-0008 | classification | draft | Classify PROPO-0008 | 0.86 | 3 | a_posteriori | Hypothex |
| ORI-0009 | classification | draft | Classify PROPO-0009 | 0.93 | 3 | a_priori | Tribunal |
| ORI-0010 | classification | draft | Classify PROPO-0010 | 0.84 | 3 | mixed | SPLIT |

### Tribunal (6 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Proves |
|----|------|--------|-------|------------|-------|--------|
| TRIBUNAL-0001 | theorem | draft | Self-Verification Impossibility Theorem | 0.92 | 7 | PROPO-0009 a priori |
| TRIBUNAL-0002 | theorem | draft | Dialectical Ceiling Theorem | 0.93 | 7 | PROPO-0006 a priori |
| TRIBUNAL-0003 | theorem | draft | Specification Immobility Theorem | 0.91 | 7 | PROPO-0001 a priori core |
| TRIBUNAL-0004 | theorem | draft | Alignment Aggregation Impossibility Theorem | 0.89 | 7 | PROPO-0002 a priori core |
| TRIBUNAL-0005 | theorem | draft | Bias-Alignment Dilemma Theorem | 0.94 | 7 | PROPO-0007 a priori core |
| TRIBUNAL-0006 | theorem | draft | Convergence-Pluralism Tension Theorem | 0.87 | 7 | PROPO-0010 a priori core |

### Hypothex (8 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Tests |
|----|------|--------|-------|------------|-------|-------|
| HYPOTHEX-0001 | hypothesis | draft | Values Change Directionally | 0.72 | 9 | PROPO-0001 a posteriori component |
| HYPOTHEX-0002 | hypothesis | draft | Humans Hold Inconsistent Values | 0.82 | 9 | PROPO-0002 a posteriori component |
| HYPOTHEX-0003 | hypothesis | draft | Good Faith Necessity for Alignment Process | 0.58 | 9 | PROPO-0003 a posteriori |
| HYPOTHEX-0004 | hypothesis | draft | Alignment Measurement Perturbs Values | 0.74 | 9 | PROPO-0004 a posteriori |
| HYPOTHEX-0005 | hypothesis | draft | Epistemic Humility Cross-Cultural Stability | 0.55 | 9 | PROPO-0005 a posteriori |
| HYPOTHEX-0006 | hypothesis | draft | Protocol Bridges Specification-Process Gap | 0.62 | 9 | PROPO-0008 a posteriori |
| HYPOTHEX-0007 | hypothesis | draft | Cognitive Bias Produces Measurable Value Distortion | 0.80 | 9 | PROPO-0007 a posteriori component |
| HYPOTHEX-0008 | hypothesis | draft | Ratio of Dialectical to Tragic Value Conflicts | 0.50 | 9 | PROPO-0010 a posteriori component |

### Theorica (3 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Components |
|----|------|--------|-------|------------|-------|------------|
| THEORICA-0001 | theory | draft | Structural Impossibility of Specification-Based Alignment | 0.90 | 10 | TRIBUNAL-0001 through 0006, HYPOTHEX-0001, 0002, 0004, 0007 |
| THEORICA-0002 | theory | draft | Alignment-as-Protocol: Bounded Dialectical Alignment | 0.72 | 10 | THEORICA-0001, TRIBUNAL-0002, 0006, HYPOTHEX-0003, 0005, 0006, 0008 |
| THEORICA-0003 | theory | draft | Epistemic Architecture of Alignment | 0.68 | 10 | THEORICA-0001, 0002, TRIBUNAL-0001, 0002, 0005, HYPOTHEX-0002, 0004, 0005, 0007 |

### Synthesis (3 artifacts)

| ID | Type | Status | Title | Confidence | Layer | Contradiction Addressed |
|----|------|--------|-------|------------|-------|------------------------|
| SYNTHESIS-0001 | synthesis | draft | The Alignment Modality Thesis: Impossibility and Possibility as Complementary Modes | 0.78 | 12 | THEORICA-0001 vs THEORICA-0002 |
| SYNTHESIS-0002 | synthesis | draft | Good Faith as Emergent Property: Disposition/Mechanism Dichotomy Is False | 0.74 | 12 | TRIBUNAL-0002 vs HYPOTHEX-0003 |
| SYNTHESIS-0003 | synthesis | draft | Epistemic Humility as Structural Necessity, Not Cultural Achievement | 0.71 | 12 | THEORICA-0003 vs HYPOTHEX-0005 |

## Active Chains

### Chain 1: The Specification Impossibility Chain
```
LOGOS-0001 (alignment) + LOGOS-0007 (specification)
  -> AXIOM-0003 (values not static) + AXIOM-0013 (specification lossy)
    -> PROPO-0001 (freezing proposition)
      -> ORI-0001 (mixed)
        -> TRIBUNAL-0003 (specification immobility theorem)
        -> HYPOTHEX-0001 (values change directionally)
          -> THEORICA-0001 (impossibility theory)
            -> SYNTHESIS-0001 (modality thesis)
```

### Chain 2: The Incoherent Target Chain
```
LOGOS-0001 (alignment) + LOGOS-0002 (values)
  -> AXIOM-0004 (self-misalignment) + AXIOM-0011 (value pluralism)
    -> PROPO-0002 (incoherent target)
      -> ORI-0002 (mixed)
        -> TRIBUNAL-0004 (aggregation impossibility)
        -> HYPOTHEX-0002 (inconsistent values)
          -> THEORICA-0001 (impossibility theory)
```

### Chain 3: The Good Faith Chain
```
LOGOS-0010 (good faith) + LOGOS-0009 (protocol)
  -> AXIOM-0005 (alignment as process) + AXIOM-0008 (tit-for-tat)
    -> PROPO-0003 (good faith requirement)
      -> ORI-0003 (a posteriori)
        -> HYPOTHEX-0003 (good faith necessity)
          -> THEORICA-0002 (alignment-as-protocol)
            -> SYNTHESIS-0002 (good faith as emergent)
```

### Chain 4: The Dialectical Ceiling Chain
```
LOGOS-0013 (identity-protected belief) + LOGOS-0010 (good faith)
  -> AXIOM-0005 (alignment as process) + AXIOM-0007 (dialectics unfolds truth)
    -> PROPO-0006 (dialectical ceiling)
      -> ORI-0006 (a priori)
        -> TRIBUNAL-0002 (dialectical ceiling theorem)
          -> THEORICA-0002 (alignment-as-protocol)
            -> SYNTHESIS-0002 (good faith as emergent)
```

### Chain 5: The Bias Dilemma Chain
```
LOGOS-0012 (cognitive bias) + AXIOM-0006 (survival not truth)
  -> AXIOM-0004 (self-misalignment)
    -> PROPO-0007 (distorted target)
      -> ORI-0007 (mixed)
        -> TRIBUNAL-0005 (bias-alignment dilemma)
        -> HYPOTHEX-0007 (measurable bias gap)
          -> THEORICA-0001 (impossibility theory)
```

### Chain 6: The Convergence-Pluralism Chain
```
AXIOM-0007 (dialectics converges) + AXIOM-0011 (value pluralism)
  -> PROPO-0010 (convergence tension)
    -> ORI-0010 (mixed)
      -> TRIBUNAL-0006 (convergence-pluralism tension)
      -> HYPOTHEX-0008 (ratio of conflicts)
        -> THEORICA-0002 (alignment-as-protocol)
          -> SYNTHESIS-0001 (modality thesis)
```

### Chain 7: The Epistemic Humility Chain
```
LOGOS-0011 (epistemic humility) + AXIOM-0003 (values not static)
  -> PROPO-0005 (meta-value stability)
    -> ORI-0005 (a posteriori)
      -> HYPOTHEX-0005 (cross-cultural stability)
        -> THEORICA-0003 (epistemic architecture)
          -> SYNTHESIS-0003 (structural necessity)
```

## Blocked Items
- None. All pipeline stages have been completed for Epoch 1.

## Open Challenges
- None issued during Epoch 1.

## Classification Summary (Ori Routing)

| Classification | Count | Propositions | Route |
|---------------|-------|-------------|-------|
| a_priori | 2 | PROPO-0006, PROPO-0009 | Tribunal |
| a_posteriori | 4 | PROPO-0003, PROPO-0004, PROPO-0005, PROPO-0008 | Hypothex |
| mixed (SPLIT) | 4 | PROPO-0001, PROPO-0002, PROPO-0007, PROPO-0010 | Tribunal + Hypothex |
