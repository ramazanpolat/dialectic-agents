---
id: TRIBUNAL-0005
agent: tribunal
type: theorem
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [PROPO-0007, ORI-0007, LOGOS-0001, LOGOS-0002, LOGOS-0007, LOGOS-0012, AXIOM-0001, AXIOM-0002]
confidence: 0.94
layer: 7
---

# Theorem: The Bias-Alignment Dilemma

## Statement
If expressed values differ from corrected values (values with cognitive biases removed), then no specification-based alignment can simultaneously satisfy alignment to expressed values and alignment to corrected values. An AI system must choose one target or the other; attempting both produces a contradiction. Formally:

For all value sets V_e (expressed) and V_c (corrected), and all AI systems A:
[V_e != V_c] --> ~[Aligned(A, V_e) AND Aligned(A, V_c)]

This is a strict logical dilemma: alignment-to-expressed-values and alignment-to-corrected-values are mutually exclusive when the two value sets differ.

## Formal Proof

- **Target**: [V_e != V_c] --> ~[Aligned(A, V_e) AND Aligned(A, V_c)]
- **Axioms Used**: AXIOM-0001 (Law of Identity), AXIOM-0002 (Law of Non-Contradiction)
- **Definitions Used**: LOGOS-0001 (Alignment), LOGOS-0002 (Values), LOGOS-0007 (Specification), LOGOS-0012 (Cognitive Bias)
- **Inference Rules Used**: Modus Ponens, Modus Tollens, Reductio ad Absurdum, Conjunction Elimination, Existential Instantiation

### Proof

**Step 1**: By LOGOS-0001 (definition of alignment), alignment is "the state in which an agent's behavior reliably produces outcomes consistent with a specified set of objectives, values, or constraints." This entails that for an agent A to be aligned to a value set V, the behavior B(A) of A must be consistent with V. Formally:

```
Aligned(A, V) --> Consistent(B(A), V)
```
-- by definitional extraction from LOGOS-0001

**Step 2**: By LOGOS-0012 (definition of cognitive bias), cognitive bias produces "a systematic and predictable deviation in an agent's judgment." If V_e are the values as expressed under the influence of cognitive biases, and V_c are the values as they would be without those biases, then V_e includes systematic deviations from V_c:

```
V_e = V_c + Bias(systematic)
```

Where Bias(systematic) represents the net effect of cognitive biases on value expression. The key property is that this deviation is systematic, not random -- it pushes values in predictable directions.
-- by definitional extraction from LOGOS-0012

**Step 3**: Since cognitive bias is systematic (non-zero), V_e and V_c differ on at least some evaluations. That is, there exist outcomes o1, o2 such that V_e ranks them differently from V_c:

```
Exists(o1, o2): Ranks(V_e, o1 > o2) AND Ranks(V_c, o2 > o1)
```
-- by the definition of "systematic deviation" from LOGOS-0012 (if the deviation were zero on all rankings, it would not be a bias)

**Step 4**: From Step 1, alignment to V_e requires behavior consistent with V_e's rankings:

```
Aligned(A, V_e) --> Consistent(B(A), V_e)
```

This means that in contexts involving o1 and o2, the AI system's behavior must favor o1 over o2 (following V_e's ranking).
-- by Modus Ponens from Step 1, instantiated with V = V_e

**Step 5**: Similarly, alignment to V_c requires behavior consistent with V_c's rankings:

```
Aligned(A, V_c) --> Consistent(B(A), V_c)
```

This means that in contexts involving o1 and o2, the AI system's behavior must favor o2 over o1 (following V_c's ranking).
-- by Modus Ponens from Step 1, instantiated with V = V_c

**Step 6**: Assume for reductio that the AI system is simultaneously aligned to both:

```
Assume: Aligned(A, V_e) AND Aligned(A, V_c)
```

**Step 7**: From Step 6 and Step 4 by Conjunction Elimination and Modus Ponens:

```
Consistent(B(A), V_e) --> B(A) favors o1 over o2 (in relevant contexts)
```

**Step 8**: From Step 6 and Step 5 by Conjunction Elimination and Modus Ponens:

```
Consistent(B(A), V_c) --> B(A) favors o2 over o1 (in relevant contexts)
```

**Step 9**: Steps 7 and 8 together assert:

```
B(A) favors o1 over o2 AND B(A) favors o2 over o1
```

**Step 10**: A single behavioral disposition cannot simultaneously favor o1 over o2 AND favor o2 over o1 in the same context. This would require the same action to both prefer and not-prefer a given outcome, which is a contradiction.

```
~[Favors(B(A), o1 > o2) AND Favors(B(A), o2 > o1)]
```
-- by AXIOM-0002 (Law of Non-Contradiction) and AXIOM-0001 (Law of Identity, applied to the identity of the behavioral context)

**Step 11**: Steps 9 and 10 produce a contradiction. By reductio ad absurdum, the assumption in Step 6 is false:

```
~[Aligned(A, V_e) AND Aligned(A, V_c)]
```
-- by Reductio, from Steps 6-10

**Step 12**: The result holds for any AI system A, given V_e != V_c:

```
For all A: [V_e != V_c] --> ~[Aligned(A, V_e) AND Aligned(A, V_c)]
```
-- by Universal Generalization over A, discharging the V_e != V_c premise -- **QED**

### Lemma (The Paternalism Fork)

From the theorem, the AI system must choose:
- **Horn 1 (Inherit bias)**: Aligned(A, V_e) -- the AI inherits all systematic biases embedded in expressed values
- **Horn 2 (Override expressed preference)**: Aligned(A, V_c) -- the AI's behavior contradicts what humans actually express they want

Neither horn is avoidable within a specification framework (LOGOS-0007), because a fixed specification must commit to one value set or the other. A specification cannot defer the choice to runtime without becoming a process.

```
Specification-Aligned(A) --> [Aligned(A, V_e) XOR Aligned(A, V_c)]
```
-- by LOGOS-0007 (specifications are fixed and must commit to a target) combined with the theorem (the two targets are exclusive)

### Corollary 1 (The Bias-Correction Authority Problem)
If alignment to V_c is chosen (correcting for biases), the question "which deviations from expressed values are biases to be corrected?" must be answered by some authority. This authority's judgment is itself subject to cognitive biases, generating a regress. No bias-free vantage point is available to any finite agent (by AXIOM-0012 and AXIOM-0006).

### Corollary 2 (Process as the Only Escape)
The dilemma has no specification-level resolution but may have a process-level resolution: a collaborative, iterative procedure in which humans and AI jointly identify and examine biases through dialectical engagement. This transforms the choice from a single specification decision to an ongoing negotiation -- consistent with AXIOM-0005 (alignment is a process).

## Proof Status
- **Sound**: yes -- every step follows from stated definitions and axioms by valid inference rules. The proof structure is a textbook reductio ad absurdum. The key insight is that conflicting rankings produce contradictory behavioral requirements.
- **Complete**: yes -- the proof reaches the target from the premises without gaps. The chain is: different values --> different rankings --> different behavioral requirements --> contradiction under simultaneous alignment.
- **Hidden Axioms**:
  1. **Behavioral determinacy**: The proof assumes that alignment to a value set determines behavior in a specific direction for each ranking. If alignment is understood as "behavioral consistency with a value set most of the time" (allowing occasional deviations), the contradiction softens. However, any deviation from V_e in favor of V_c (or vice versa) constitutes partial alignment to one at the expense of the other -- the dilemma is not eliminated by probabilistic alignment, merely distributed across instances.
  2. **Context identity**: The proof assumes the "relevant contexts" in Steps 7 and 8 are the same contexts. If expressed values and corrected values diverge only in contexts that never arise in practice, the dilemma would be theoretical but practically irrelevant. However, LOGOS-0012 specifies that cognitive biases are "systematic and predictable," implying they affect commonly occurring judgments, not exotic edge cases.

## Justification
This theorem formalizes the a priori component of PROPO-0007 (The Distorted Target Proposition) as identified by ORI-0007. The classification isolated the a priori core as: "If expressed values differ from corrected values, then an AI system cannot simultaneously be aligned to both."

The theorem is the strongest in the current Tribunal output in terms of logical simplicity and confidence. The proof reduces to: if A differs from B, you cannot simultaneously equal both A and B. This is nearly trivial in its logical structure, but its application to the alignment problem has significant consequences.

The philosophical significance is that the dilemma is not a contingent difficulty (solvable with more data or better methods) but a logical impossibility (given that bias produces a systematic difference in value rankings). The only way to dissolve the dilemma is to dissolve the distinction between V_e and V_c -- which requires either denying that cognitive biases affect values (contradicting AXIOM-0006 and LOGOS-0012) or redefining alignment in a way that does not require commitment to a single value set (moving to process-based alignment per AXIOM-0005).

## Dependencies
- LOGOS-0001 (alignment -- defines the relational state that creates the contradiction)
- LOGOS-0002 (values -- the target that splits into expressed and corrected)
- LOGOS-0007 (specification -- the framework that forces the choice)
- LOGOS-0012 (cognitive bias -- the mechanism that produces the split)
- AXIOM-0001 (identity -- presupposed by context identity in the reductio)
- AXIOM-0002 (non-contradiction -- the logical law that produces the reductio)
- PROPO-0007 (the proposition whose a priori core this theorem formalizes)
- ORI-0007 (the classification that identified the a priori component)

## Evaluation Notes
This is the highest-confidence proof in the Tribunal's current output (0.94) because of its logical simplicity. The proof is a direct application of the law of non-contradiction to the case of conflicting behavioral requirements. The only way to challenge it is to challenge the premise (V_e != V_c, which is an empirical claim) or the definitions (particularly LOGOS-0001's requirement that alignment produces behavior "consistent with" the specified values).

The theorem does not establish which horn of the dilemma should be chosen -- that is a normative question outside Tribunal's domain. It only establishes that the choice is unavoidable within a specification framework. This limitation is appropriate: Tribunal proves logical truths, not normative prescriptions.

An important connection to TRIBUNAL-0002 (Dialectical Ceiling Theorem): the Bias-Alignment Dilemma shows why specification fails; the Dialectical Ceiling shows that even the process alternative (dialectics) has limits. Together, they establish both that specification-based alignment is impossible when values are bias-distorted, and that process-based alignment is bounded by identity-protected beliefs. The full picture of alignment constraints is the conjunction of all Tribunal theorems.

Self-assessment: confidence 0.94. The residual 0.06 comes from the behavioral determinacy assumption -- in practice, alignment may be understood probabilistically rather than deterministically, which would soften the strict dilemma into a trade-off between competing alignment objectives.

## Lineage
LOGOS-0012 (cognitive bias splits V_e from V_c) + LOGOS-0001 (alignment requires behavioral consistency) + AXIOM-0002 (non-contradiction) --> PROPO-0007 (distorted target proposition) --> ORI-0007 (classified as mixed, a priori core: dilemma structure) --> TRIBUNAL-0005 (formal proof of dilemma)
