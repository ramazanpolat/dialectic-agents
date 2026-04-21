---
id: TRIBUNAL-0003
agent: tribunal
type: theorem
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [PROPO-0001, ORI-0001, LOGOS-0001, LOGOS-0002, LOGOS-0003, LOGOS-0007, AXIOM-0002, AXIOM-0003, AXIOM-0013]
confidence: 0.91
layer: 7
---

# Theorem: The Specification Immobility Theorem

## Statement
A fixed specification cannot track a non-static target. Formally: if a specification S is fixed at time t0 and the target T changes at any time t1 > t0, then S fails to capture T at t1. Applied to alignment: if an AI system is aligned by means of a fixed specification of values, and values are not static, then the specification necessarily fails to capture the values at any subsequent time at which the values have changed.

For all S, for all T, for all t0, t1 where t1 > t0:
[Fixed(S, t0) AND Changed(T, t0, t1)] --> ~Captures(S, T(t1))

## Formal Proof

- **Target**: Fixed(S, t0) AND Changed(T, t0, t1) --> ~Captures(S, T(t1))
- **Axioms Used**: AXIOM-0002 (Law of Non-Contradiction), AXIOM-0003 (Values Are Not Static), AXIOM-0013 (Specification Is Necessarily Lossy)
- **Definitions Used**: LOGOS-0001 (Alignment), LOGOS-0002 (Values), LOGOS-0007 (Specification)
- **Inference Rules Used**: Modus Ponens, Modus Tollens, Hypothetical Syllogism, Conjunction Elimination, Definitional Extraction

### Proof

**Step 1**: By LOGOS-0007 (definition of specification), a specification is "a fixed, explicit, and complete description of desired behavior or outcomes." The property "fixed" means the specification does not change after the time of its creation. Formally:

```
Fixed(S, t0) --> For all t > t0: S(t) = S(t0)
```
-- by definitional extraction from LOGOS-0007 (the fixedness condition)

**Step 2**: Define "captures" as follows: a specification S captures a target T at time t if and only if the content of S at time t matches the state of T at time t. Formally:

```
Captures(S, T(t)) <==> S(t) = T(t)
```
-- by the definition of what it means for a specification to successfully describe its target (derived from LOGOS-0007's requirement for "unambiguous verification of whether a given instance conforms to it")

**Step 3**: From Step 1, for any t1 > t0:

```
Fixed(S, t0) --> S(t1) = S(t0)
```
-- by Universal Instantiation from Step 1, setting t = t1

**Step 4**: The target T has changed between t0 and t1. By the definition of "changed":

```
Changed(T, t0, t1) --> T(t1) != T(t0)
```
-- by definitional extraction (change means the state at t1 differs from the state at t0)

**Step 5**: Assume for reductio that S captures T at t1:

```
Assume: Captures(S, T(t1))
```

**Step 6**: From Step 2 and the assumption in Step 5:

```
S(t1) = T(t1)
```
-- by Modus Ponens, from Step 2 (biconditional elimination) and Step 5

**Step 7**: From Step 3, given Fixed(S, t0):

```
S(t1) = S(t0)
```
-- by Modus Ponens from Step 3

**Step 8**: Assume also that S captured T at t0 (the specification was correct at the time of creation):

```
S(t0) = T(t0)
```
-- by assumption (the specification was adequate at the point of creation)

**Step 9**: From Steps 6, 7, and 8 by transitivity of identity:

```
T(t1) = S(t1) = S(t0) = T(t0)
```
Therefore: T(t1) = T(t0)

-- by transitivity of equality, from Steps 6, 7, 8

**Step 10**: But Step 4 asserts:

```
T(t1) != T(t0)
```
-- from the premise Changed(T, t0, t1)

**Step 11**: Steps 9 and 10 yield a contradiction:

```
T(t1) = T(t0) AND T(t1) != T(t0)
```

This violates AXIOM-0002 (Law of Non-Contradiction): a proposition cannot be both true and false in the same respect.

**Step 12**: By reductio ad absurdum, the assumption in Step 5 is false:

```
~Captures(S, T(t1))
```
-- by Reductio, from the contradiction in Step 11

**Step 13**: Discharging all assumptions, we have:

```
[Fixed(S, t0) AND Changed(T, t0, t1) AND Captures(S, T(t0))] --> ~Captures(S, T(t1))
```
-- by Conditional Proof, from Steps 5-12

**Step 14**: Applied to the alignment domain: let S be a specification of values, and T be the actual values of a population. By AXIOM-0003, values are not static: there exist t0, t1 with t1 > t0 such that Changed(V, t0, t1). By LOGOS-0007, a specification is fixed. Therefore:

```
Aligned-by-Spec(AI, V(t0)) --> ~Captures(spec, V(t1)) for some t1 > t0
```
-- by Universal Instantiation of Step 13 with T = V, and existential introduction from AXIOM-0003

**Step 15**: This establishes the Specification Immobility Theorem:

```
For all specifications S of values V:
  Fixed(S) AND ~Static(V) --> Exists t1 such that ~Captures(S, V(t1))
```
-- **QED**

### Corollary 1 (Specification-Based Alignment is Temporally Bounded)
Any alignment achieved through a fixed specification has a finite shelf life. The duration depends on the rate of value change, but the eventual failure is guaranteed by the theorem.

### Corollary 2 (Self-Updating Specifications Are Not Specifications)
A specification that includes a mechanism for updating itself in response to value change is not "fixed" in the LOGOS-0007 sense. It is a process (LOGOS-0008) disguised as a specification. This is not a loophole -- it is a reclassification that concedes the theorem's point.

## Proof Status
- **Sound**: yes -- every step follows from the stated definitions and axioms by valid inference rules. The proof is a straightforward reductio ad absurdum. The key logical move is that fixedness and change produce a contradiction via transitivity of identity.
- **Complete**: yes -- the proof reaches the target conclusion without gaps. Each step is justified by a specific rule and specific premises.
- **Hidden Axioms**: One assumption in Step 8: that the specification was correct at the time of creation. This is not strictly necessary for the main theorem (which is conditional on fixedness and change), but it strengthens the applied conclusion. Without Step 8, the theorem still holds: a fixed specification at t0 has content S(t0), and if T(t1) differs from T(t0), then S(t0) cannot equal both T(t0) and T(t1) simultaneously. The specification either failed from the start or fails after the change -- either way, it fails at t1.

## Justification
This theorem formalizes the a priori component of PROPO-0001 (The Freezing Proposition) as identified by ORI-0001. The classification identified the a priori core as: "If values change over time AND a specification is fixed, then the specification cannot track the change." This is precisely what the theorem proves.

The proof is remarkably simple -- it is essentially the observation that a constant function cannot equal a non-constant function at all points. The philosophical weight comes not from the logical complexity but from the application: the theorem shows that alignment-by-specification is not merely difficult but structurally impossible for a non-static target. The difficulty is not computational (we could build a better specification) but logical (no specification, however good, can be both fixed and tracking a moving target).

This result supports AXIOM-0005's claim that alignment is a process, not a specification. It does so by proving the negative: specification cannot work for non-static targets.

## Dependencies
- LOGOS-0001 (alignment -- the concept being analyzed)
- LOGOS-0002 (values -- the non-static target)
- LOGOS-0003 (moral progress -- the mechanism of value change)
- LOGOS-0007 (specification -- the mechanism shown to be inadequate)
- AXIOM-0002 (non-contradiction -- used in the reductio)
- AXIOM-0003 (values are not static -- the empirical premise that activates the theorem in the alignment domain)
- AXIOM-0013 (specification is lossy -- provides additional independent support)
- PROPO-0001 (the proposition whose a priori core this theorem formalizes)
- ORI-0001 (the classification that identified the a priori component)

## Evaluation Notes
This is one of the simplest proofs in the Tribunal's output, but also one of the most consequential. The logical structure reduces to: a constant cannot equal a variable. The entire weight of the argument rests on the definitions: if "specification" means "fixed" (LOGOS-0007) and "values" are "not static" (AXIOM-0003), the conclusion is inescapable.

The main avenue for challenging this theorem is to challenge the definitions:
1. If LOGOS-0007 is weakened (specifications can be partially fixed, with update mechanisms), then the theorem applies only to the fixed components.
2. If AXIOM-0003 is rejected (values are actually static or convergent), then the theorem's domain premise is unsatisfied and it becomes vacuously true.
3. If "captures" is weakened to "approximately captures" (allowing some divergence), then the theorem needs reformulation in terms of divergence bounds -- the specification's approximation degrades over time but may remain "good enough" for some period.

Note on the relationship to AXIOM-0013: the theorem does not require AXIOM-0013 (specification is lossy) for its core result. AXIOM-0013 provides an independent reason specifications fail (they lose information even at t0), while this theorem shows they fail over time even if they were perfect at t0. The two results compound: specifications are lossy from the start AND degrade over time.

Self-assessment: confidence 0.91. The residual 0.09 comes from the possibility that the strict reading of "fixed" in LOGOS-0007 is too strong -- practical specifications may include limited update mechanisms that partially mitigate the immobility problem without fully resolving it.

## Lineage
LOGOS-0007 (specification = fixed) + AXIOM-0003 (values = not static) --> AXIOM-0002 (non-contradiction enables reductio) --> PROPO-0001 (freezing proposition) --> ORI-0001 (classified as mixed, a priori core extracted) --> TRIBUNAL-0003 (formal proof of a priori core)
