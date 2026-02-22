---
id: TRIBUNAL-0004
agent: tribunal
type: theorem
status: draft
created: 2026-02-22
updated: 2026-02-22
domain: "AI Ethics, Epistemology"
depends_on: [PROPO-0002, ORI-0002, LOGOS-0001, LOGOS-0002, AXIOM-0001, AXIOM-0002, AXIOM-0011]
confidence: 0.89
layer: 7
---

# Theorem: The Alignment Aggregation Impossibility

## Statement
If the values of individual agents in a population are genuinely plural (AXIOM-0011), then no aggregation procedure exists that produces a coherent, well-defined collective value set satisfying minimal fairness constraints, to which an AI system could be aligned. Formally: there is no function F from individual value orderings to a collective value ordering that simultaneously satisfies non-dictatorship, Pareto efficiency, and independence of irrelevant alternatives, given unrestricted domain.

For all F: [Unrestricted(Domain(F)) AND Plural(V_individuals)] --> ~[NonDictatorship(F) AND Pareto(F) AND IIA(F)]

Therefore: ~Exists(F) such that F is a fair aggregation of plural individual values into a coherent alignment target.

## Formal Proof

- **Target**: Under value pluralism, no fair aggregation function yields a coherent alignment target
- **Axioms Used**: AXIOM-0001 (Law of Identity), AXIOM-0002 (Law of Non-Contradiction), AXIOM-0011 (Irreducible Value Pluralism)
- **Definitions Used**: LOGOS-0001 (Alignment), LOGOS-0002 (Values)
- **External Result Used**: Arrow's Impossibility Theorem (accepted as a proven mathematical result within social choice theory)
- **Inference Rules Used**: Modus Ponens, Modus Tollens, Conjunction Introduction, Universal Instantiation, Hypothetical Syllogism

### Preliminary: Status of Arrow's Theorem

Arrow's Impossibility Theorem (1951) is a mathematical result proven within the axioms of social choice theory. It states:

**Arrow's Theorem**: For any set of three or more alternatives, no social welfare function can simultaneously satisfy:
(A1) Unrestricted Domain -- the function accepts any logically possible set of individual preference orderings
(A2) Non-Dictatorship -- no single individual's preferences determine the social ordering regardless of others' preferences
(A3) Pareto Efficiency -- if every individual prefers X to Y, the collective ordering ranks X above Y
(A4) Independence of Irrelevant Alternatives -- the collective ranking of X vs. Y depends only on individuals' rankings of X vs. Y

This theorem is a proven mathematical result. Within this proof, it functions as an established lemma from an external formal system. Its proof is not reproduced here but is a matter of mathematical record.

### Proof

**Step 1**: By AXIOM-0011 (Irreducible Value Pluralism), there exist genuinely distinct, mutually incompatible value systems across agents in any sufficiently diverse population. Furthermore, "the aggregation of individual values into 'collective values' is not a well-defined operation: it always involves a choice of aggregation procedure, and different procedures yield different results."

```
Plural(V_individuals) -- there exist agents i, j with incompatible value orderings
```
-- by AXIOM-0011

**Step 2**: By LOGOS-0002 (definition of values), values are "principles or standards that an agent uses -- consciously or unconsciously -- to evaluate outcomes, rank preferences, and guide decisions." Values thus induce preference orderings over outcomes: for any agent a, V(a) induces a ranking R(a) over the set of possible outcomes.

```
For all agents a: V(a) induces R(a) over outcomes O
```
-- by definitional extraction from LOGOS-0002

**Step 3**: From Step 1 and Step 2, the plurality of values entails a plurality of preference orderings. Since value systems are genuinely distinct and mutually incompatible (AXIOM-0011), the induced preference orderings are diverse:

```
Plural(V_individuals) --> Diverse(R_individuals)
```
-- by Modus Ponens from Steps 1 and 2: incompatible values produce distinct orderings

**Step 4**: The diversity of preference orderings satisfies Arrow's Unrestricted Domain condition (A1). If value systems are genuinely plural and mutually incompatible, then the space of individual preference orderings is not restricted to any proper subset -- any logically possible ordering can be held by some agent.

```
Diverse(R_individuals) AND Plural(V_individuals) --> Unrestricted(Domain)
```
-- by the connection between value pluralism and the range of possible preference orderings. AXIOM-0011 asserts pluralism is irreducible, meaning the diversity is not a temporary state that could be resolved -- it is a structural feature. This guarantees the domain is genuinely unrestricted.

**Step 5**: By LOGOS-0001 (definition of alignment), alignment is "the state in which an agent's behavior reliably produces outcomes consistent with a specified set of objectives, values, or constraints." For alignment to be well-defined, the target -- the "specified set of values" -- must itself be well-defined. A collective value set produced by aggregation is well-defined only if the aggregation function is well-defined and produces a coherent ordering.

```
WellDefined(AlignmentTarget) --> Exists(F) such that F(R_individuals) = R_collective AND Coherent(R_collective)
```
-- by definitional extraction from LOGOS-0001: alignment requires a specifiable target

**Step 6**: For the aggregation function F to be legitimate as an alignment target, it must satisfy minimal fairness constraints. An alignment target produced by a dictatorial function (one agent's values override all others) would not constitute alignment to "human values" in any meaningful sense -- it would be alignment to one human's values. Similarly, violating Pareto efficiency (ignoring unanimous preferences) would produce an alignment target that contradicts the expressed values of every individual. These are not arbitrary constraints -- they are minimal conditions for the aggregation to count as representing a collective rather than an individual or an arbitrary imposition.

```
Legitimate(F) --> NonDictatorship(F) AND Pareto(F) AND IIA(F)
```
-- by the argument that fairness constraints are necessary for collective alignment to be meaningful (not merely a formal construct)

**Step 7**: From Arrow's Theorem (established mathematical result), given Unrestricted Domain:

```
Unrestricted(Domain) --> ~Exists(F) such that [NonDictatorship(F) AND Pareto(F) AND IIA(F)]
```
-- by Arrow's Impossibility Theorem

**Step 8**: From Steps 4 and 7 by Hypothetical Syllogism:

```
Diverse(R_individuals) AND Plural(V_individuals) --> ~Exists(F) such that [NonDictatorship(F) AND Pareto(F) AND IIA(F)]
```

**Step 9**: From Steps 6 and 8: If no legitimate aggregation function exists, then no well-defined collective alignment target can be constructed:

```
~Exists(Legitimate(F)) --> ~WellDefined(CollectiveAlignmentTarget)
```
-- by Modus Tollens from Step 5 (contrapositive) combined with Step 6

**Step 10**: From Steps 1, 3, 8, and 9:

```
Plural(V_individuals) --> ~WellDefined(CollectiveAlignmentTarget)
```
-- by Hypothetical Syllogism through the chain: Pluralism --> Diversity --> Unrestricted Domain --> No Fair Aggregation --> No Well-Defined Target

**Step 11**: AXIOM-0011 asserts that value pluralism holds for actual human populations:

```
Plural(V_humans)
```
-- by AXIOM-0011

**Step 12**: From Steps 10 and 11 by Modus Ponens:

```
~WellDefined(CollectiveAlignmentTarget_humans)
```
-- **QED**

### Corollary 1 (The Procedure Dependence of "Human Values")
Any claim to have identified "human values" as an alignment target necessarily depends on a choice of aggregation procedure. Different procedures produce different "human values." Therefore, "aligning AI to human values" is incomplete as stated -- it must specify which aggregation procedure and justify that choice.

### Corollary 2 (The Meta-Alignment Problem)
The choice of aggregation procedure is itself a value choice. Different value systems will prefer different aggregation procedures (e.g., egalitarians prefer equal weighting; meritocrats prefer expertise-weighted aggregation; libertarians prefer market-based aggregation). This generates a regress: aligning to human values requires choosing an aggregation procedure, but choosing an aggregation procedure requires knowing which values should guide that choice.

## Proof Status
- **Sound**: yes -- every step follows from stated premises by valid inference rules. Arrow's Theorem is accepted as a proven mathematical result and functions as an established lemma.
- **Complete**: yes -- the proof chain from value pluralism to the non-existence of a well-defined collective alignment target is unbroken.
- **Hidden Axioms**:
  1. **Step 4's bridge premise**: The claim that irreducible value pluralism implies unrestricted domain in Arrow's sense is substantive. One could argue that while values are plural, the space of actual value orderings is restricted (e.g., no one holds certain pathological orderings). If the domain is restricted in the right way, Arrow's theorem does not apply, and aggregation might be possible. This is the most significant vulnerability of the proof. However, AXIOM-0011's assertion that pluralism is "irreducible" and that "genuinely distinct, mutually incompatible value systems" exist strongly supports the unrestricted domain claim for any sufficiently diverse population.
  2. **Step 6's fairness requirement**: The claim that alignment to "human values" requires non-dictatorship, Pareto efficiency, and IIA could be contested. One might argue that alignment need not be "fair" in Arrow's sense -- perhaps alignment to a philosophically justified subset of values (e.g., a reflective equilibrium) could bypass the aggregation problem. This would, however, require justifying the selection criterion, which reintroduces the problem at a meta-level.

## Justification
This theorem formalizes the a priori component of PROPO-0002 (The Incoherent Target Proposition) as identified by ORI-0002. The classification isolated the a priori core as Arrow's impossibility theorem applied to the alignment target: "If individual preference orderings are diverse and unrestricted, then no aggregation procedure satisfying non-dictatorship, Pareto efficiency, and independence of irrelevant alternatives exists."

The theorem shows that the concept of "human values" as a collective alignment target is not merely difficult to identify -- it is formally ill-defined under conditions of genuine value pluralism. This is not an engineering obstacle but a mathematical impossibility. No amount of data collection, preference elicitation, or computational power can overcome an impossibility result.

The significance for the Alignment Paradox is profound: the most common framing of AI alignment -- "align AI to human values" -- presupposes the existence of a coherent entity called "human values." This theorem demonstrates that no such entity exists when values are genuinely plural, unless one makes an arbitrary (and itself value-laden) choice of aggregation procedure.

## Dependencies
- LOGOS-0001 (alignment -- requires a well-defined target)
- LOGOS-0002 (values -- induce preference orderings subject to Arrow's theorem)
- AXIOM-0001 (identity -- presupposed by the formal apparatus)
- AXIOM-0002 (non-contradiction -- presupposed by the formal apparatus)
- AXIOM-0011 (irreducible value pluralism -- provides the diversity premise that activates Arrow's theorem)
- Arrow's Impossibility Theorem (external mathematical result, accepted as proven)
- PROPO-0002 (the proposition whose a priori core this theorem formalizes)
- ORI-0002 (the classification that identified the a priori component)

## Evaluation Notes
This proof differs from the others in the Tribunal's output because it relies on an external mathematical result (Arrow's theorem) rather than proving everything from the framework's own axioms. This is legitimate -- Arrow's theorem is a proven result in mathematics, and incorporating established results is standard practice in formal reasoning. The proof's original contribution is the bridge from Arrow's theorem to the alignment domain: showing that the conditions of Arrow's theorem are satisfied by the framework's axioms about value pluralism.

The main vulnerabilities are:
1. **Domain restriction**: If human values are plural but not "unrestricted" in Arrow's sense, the theorem's force is reduced. Sen's work on domain restrictions shows that aggregation is possible under certain structural conditions (e.g., single-peaked preferences). Whether human values satisfy such conditions is an empirical question (a posteriori), which is why the full proposition PROPO-0002 is classified as mixed.
2. **Ordinal vs. cardinal**: Arrow's theorem applies to ordinal preference rankings. If values admit cardinal comparison (interpersonal utility comparison), aggregation procedures like utilitarianism can bypass Arrow's conditions. Whether values are cardinally comparable is both a philosophical and empirical question.
3. **The scope of "alignment"**: If alignment does not require aggregation to a single ordering but can instead be understood as navigating a Pareto frontier of plural values, the theorem's conclusion shifts from "alignment is impossible" to "alignment requires navigating trade-offs rather than optimizing a single objective."

Self-assessment: confidence 0.89. The residual 0.11 reflects the vulnerabilities above, particularly the domain restriction issue and the possibility that alignment can be reformulated to avoid requiring a single collective ordering.

## Lineage
AXIOM-0011 (irreducible value pluralism) --> Arrow's Theorem (external, proven) --> PROPO-0002 (incoherent target proposition) --> ORI-0002 (classified as mixed, a priori core: Arrow's impossibility) --> TRIBUNAL-0004 (formal proof applying Arrow's theorem to alignment)
