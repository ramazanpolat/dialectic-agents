# The Crucible — Dialectic Evaluation Engine

## Name

**The Crucible** — where raw ideas are thrown into the epistemological fire and tested against the full agent pipeline. What survives is knowledge. What doesn't reveals where the knowledge gaps are.

## Purpose

A standalone evaluation UI that lets a human submit raw text (sentences, claims, ideas, arguments) and see them evaluated against the entire dialectic agent pipeline in real-time. The Crucible does not modify the artifact store — it only reads existing artifacts to perform its evaluation.

## Problem It Solves

Right now the dialectic pipeline is autonomous — agents produce and evaluate artifacts without human input. The Crucible creates the **human-in-the-loop** interface: a place where a human thinker can inject raw ideas and see how the epistemological system classifies, validates, challenges, and connects them.

This is the dialectical equivalent of a compiler's error output — you write code (ideas), the system tells you what's valid, what's broken, and what's missing.

## Architecture

```
┌──────────────────────────────────────────────┐
│  THE CRUCIBLE (browser, standalone HTML)      │
│                                               │
│  ┌─────────────────────────────────────────┐  │
│  │  Raw Input                              │  │
│  │  "Power structures tend to make         │  │
│  │   themselves invisible"                 │  │
│  └─────────────┬───────────────────────────┘  │
│                │                              │
│  ┌─────────────▼───────────────────────────┐  │
│  │  EVALUATION PIPELINE (in-browser)       │  │
│  │                                         │  │
│  │  1. Logos Scan (term analysis)          │  │
│  │  2. Axiom Check (compatibility)         │  │
│  │  3. Propo Analysis (form & structure)   │  │
│  │  4. Ori Classification (a priori/post)  │  │
│  │  5. Tribunal Path (deductive route)     │  │
│  │  6. Hypothex Path (empirical route)     │  │
│  │  7. Synthesis Scan (contradictions)     │  │
│  │  8. Novelty Check (is it new?)          │  │
│  └─────────────┬───────────────────────────┘  │
│                │                              │
│  ┌─────────────▼───────────────────────────┐  │
│  │  VERDICT CARD                           │  │
│  │                                         │  │
│  │  Classification: POSTULATE              │  │
│  │  Epistemic Status: A POSTERIORI         │  │
│  │  Confidence: 0.85                       │  │
│  │  Verdict: PLAUSIBLE — NOT YET IN SYSTEM │  │
│  │  Related: AXIOM-0004, AXIOM-0006        │  │
│  │  Recommendation: Add as postulate       │  │
│  │  Conflicts: None detected               │  │
│  │  Missing Terms: "power structure"       │  │
│  └─────────────────────────────────────────┘  │
│                                               │
│  Reads from: artifacts/ (all agents)          │
│  Writes to: NOTHING (read-only)               │
└──────────────────────────────────────────────┘
```

## Evaluation Pipeline — The Seven Tests

### Test 1: Logos Scan (Term Analysis)

**Question**: Are all terms in the input defined in the system?

**Method**:
- Tokenize the input into significant terms (nouns, adjectives, key phrases)
- Match each term against the Logos artifact titles and statements
- For each match, show the definition and its confidence
- For each miss, flag it as an undefined term

**Output**:
- **Defined terms**: list with links to LOGOS artifacts
- **Undefined terms**: list with flag — "This term needs a definition before the claim can be formally evaluated"
- **Ambiguous terms**: terms that match multiple definitions

### Test 2: Axiom Compatibility Check

**Question**: Does this input align with, contradict, or extend the accepted axiom set?

**Method**:
- Semantic similarity matching against all AXIOM artifact statements
- Check for direct contradiction (input negates an accepted axiom)
- Check for reinforcement (input supports or follows from an accepted axiom)
- Check for axiom candidacy: does this input LOOK like an axiom? (self-evident, foundational, non-derivable)

**Output**:
- **Aligns with**: list of supporting axioms
- **Contradicts**: list of conflicting axioms (CRITICAL — synthesis opportunity)
- **Axiom candidacy score**: 0-1, how much this looks like it should be an axiom/postulate itself
- **If candidate**: which existing axioms it would be independent of

### Test 3: Propo Analysis (Proposition Form)

**Question**: Is this a well-formed proposition? What kind?

**Method**:
- **Truth-evaluability test**: Can this be true or false? (Commands, questions, and exclamations fail this test)
- **Logical form extraction**: Identify quantifiers (all, some, none), connectives (if-then, and, or, not), and predicates
- **Categorization**:
  - Analytic (true by definition) vs. Synthetic (true by how the world is)
  - Necessary (true in all possible worlds) vs. Contingent (could be otherwise)
  - Universal (about all X) vs. Particular (about some X) vs. Singular (about one X)
- **Decomposition**: If the input is a compound claim, split it into atomic propositions

**Output**:
- **Well-formed**: yes/no with explanation
- **Logical form**: displayed in both natural language and symbolic notation
- **Category**: analytic/synthetic × necessary/contingent
- **Scope**: universal/particular/singular
- **Atomic propositions**: if compound, show the decomposition

### Test 4: Ori Classification (Epistemic Routing)

**Question**: Is this knowable a priori or a posteriori?

**Method**:
- **Negation test**: Is the negation logically contradictory? If yes → a priori
- **Conceivability test**: Can you imagine a world where this is false? If no → a priori
- **Justification test**: What kind of evidence would settle this? Logic only → a priori; observation → a posteriori
- **Mixed detection**: If the claim has both logical and empirical components, decompose

**Output**:
- **Verdict**: A PRIORI / A POSTERIORI / MIXED
- **Test results**: Each test's result shown individually
- **If mixed**: The a priori component and a posteriori component separated
- **Route**: "Would be sent to Tribunal" or "Would be sent to Hypothex"

### Test 5: Tribunal Path (Deductive Assessment)

**Question**: If a priori, can it be proven from accepted axioms?

**Method**:
- Identify which axioms would be relevant to proving this claim
- Check whether the claim follows from those axioms through valid inference
- If not provable, identify what ADDITIONAL axiom would make it provable
- Check if it contradicts any proven theorems

**Output**:
- **Provable**: yes / no / insufficient axioms
- **Required axioms**: which axioms would be needed
- **Missing link**: if not provable, what's missing
- **Contradicts theorems**: list of conflicting theorems

### Test 6: Hypothex Path (Empirical Assessment)

**Question**: If a posteriori, is it testable?

**Method**:
- **Falsifiability check**: What observation would prove this wrong?
- **Testability**: Is there a feasible way to check this?
- **Existing evidence**: Do any existing artifacts (hypotheses, theories) provide evidence for or against?
- **Alternative generation**: What's the strongest alternative explanation?

**Output**:
- **Falsifiable**: yes / no
- **Falsification condition**: what would disprove it
- **Testability**: feasible / in-principle / not testable
- **Existing evidence**: supporting and opposing artifacts
- **Alternatives**: at least one competing hypothesis

### Test 7: Synthesis Scan (System Integration)

**Question**: How does this input relate to the existing knowledge graph?

**Method**:
- Check ALL artifacts for semantic similarity
- Identify contradictions (the input opposes an existing artifact)
- Identify reinforcements (the input supports an existing artifact)
- Identify novelty (the input says something no existing artifact covers)
- Check for synthesis opportunities (the input + an existing artifact could produce a synthesis)

**Output**:
- **Related artifacts**: ranked by relevance
- **Contradictions**: list with synthesis opportunity flag
- **Reinforcements**: list with "strengthens" indicator
- **Novelty score**: 0-1, how new is this idea relative to the system
- **Synthesis candidates**: specific thesis-antithesis pairs this could participate in

### Test 8: Final Verdict

**Combines all test results into a single assessment**:

- **Classification**: What IS this? (primitive / definition / axiom / postulate / proposition / hypothesis / theorem candidate / theory fragment)
- **Epistemic Status**: a priori / a posteriori / mixed
- **Validity**: valid / invalid / undetermined (with explanation)
- **Confidence**: overall confidence score
- **Recommendation**: What should happen with this?
  - "Add as AXIOM-NNNN" / "Add as LOGOS-NNNN" / "Send to Propo for formal structuring" / "Contradicts existing system — synthesis needed" / "Already covered by [artifact]" / "Not evaluable — undefined terms"
- **Missing Infrastructure**: What does the system need before it can fully evaluate this? (definitions, axioms, etc.)

## UI Design

### Layout
```
┌──────────────────────────────────────────────────────────┐
│  THE CRUCIBLE — Dialectic Evaluation Engine               │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │  Enter your raw idea, claim, or argument...        │  │
│  │                                                    │  │
│  │  [multi-line text input]                           │  │
│  │                                                    │  │
│  └────────────────────────────────────────────────────┘  │
│  [🔥 EVALUATE]  [Clear]  [Load example]                  │
│                                                          │
│  ┌───────────────────┬────────────────────────────────┐  │
│  │   VERDICT CARD    │    PIPELINE RESULTS            │  │
│  │                   │                                │  │
│  │  Classification   │    Test 1: Logos Scan     ✓/✗  │  │
│  │  Epistemic Status │    Test 2: Axiom Check    ✓/✗  │  │
│  │  Confidence       │    Test 3: Propo Analysis ✓/✗  │  │
│  │  Validity         │    Test 4: Ori Classify   ✓/✗  │  │
│  │  Recommendation   │    Test 5: Tribunal Path  ✓/✗  │  │
│  │                   │    Test 6: Hypothex Path  ✓/✗  │  │
│  │  RELATED:         │    Test 7: Synthesis Scan ✓/✗  │  │
│  │  • AXIOM-0004     │                                │  │
│  │  • AXIOM-0006     │    [Expand each for details]   │  │
│  │  • PROPO-0007     │                                │  │
│  └───────────────────┴────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │  DEPENDENCY CONTEXT (mini-graph showing where      │  │
│  │  the evaluated input would sit in the graph)       │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │  EVALUATION HISTORY                                │  │
│  │  • "Power structures tend to..." → POSTULATE       │  │
│  │  • "All consciousness is..." → PROPOSITION (a pri) │  │
│  │  • "Democracy is the best..." → MIXED (challenged) │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### Visual Language
- Fire/forge metaphor — the input is "thrown into the crucible"
- Animated evaluation pipeline — tests run visually one by one
- Color-coded verdicts: green (valid/accepted), amber (plausible/undetermined), red (contradicted/invalid)
- Particle effects on the verdict reveal

## Technical Notes

- **Standalone HTML** — no backend required. All evaluation is heuristic, running in-browser against embedded artifact data.
- **Does NOT write to artifact directories** — read-only evaluation. To actually add an artifact, the user would need to manually run the appropriate agent or add the file themselves.
- **Evaluation history is session-local** — stored in JavaScript memory, lost on page refresh. No localStorage needed.
- **Artifact data is embedded as JSON** — same approach as the Observatory dashboard. Could be regenerated from artifact files by a build script.
- **Future enhancement**: A `evaluate.sh` script that calls `claude` with a special evaluator CLAUDE.md to do deep AI-powered evaluation instead of heuristic matching. The HTML would call this via a local API endpoint.

## Relationship to Running System

**The Crucible does NOT interfere with the running dialectic-agents pipeline.**

- It reads artifact data that was embedded at build time (JSON in the HTML)
- It does not touch any files in any agent's `artifacts/` directory
- It can be updated by re-embedding the latest artifact data from the repo
- It runs entirely in the browser — no server, no file system access

The running `./run.sh` orchestrator continues independently. The Crucible is a window into the system, not a control panel for it.
