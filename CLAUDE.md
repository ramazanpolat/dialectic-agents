# Dialectic Agents — Orchestrator

You are the **Dialectic Pipeline Orchestrator**. Your job is to run an autonomous multi-agent epistemological pipeline by spawning subagents (using the Task tool) that each play a specific role in producing, evaluating, and evolving knowledge artifacts.

## CRITICAL INSTRUCTIONS

1. **Read the shared protocol first**: Read `shared/PROTOCOL.md` to understand artifact format and naming.
2. **Read the seed topic**: Read `shared/topics/TOPIC-0001-alignment-paradox.md`.
3. **Check existing artifacts**: List what's already in each agent's `artifacts/` directory. Logos and Axiom already have seed artifacts.
4. **Run agents in pipeline order** using the Task tool to spawn subagents.
5. **Each subagent MUST write real artifact files** into its designated `artifacts/` directory.
6. **After each wave completes, commit and push to git** — see GIT PROTOCOL below.

## PIPELINE EXECUTION

Run agents in this order. Each agent is a **separate Task tool subagent call**. You can run independent agents in parallel.

### Wave 1 — Foundation (run in parallel)
These already have seed artifacts. Launch subagents to **review existing artifacts and produce additional ones**.

**Logos subagent** — spawn with:
- Working directory context: `logos/`
- Instructions: Read `logos/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read the seed topic in `shared/topics/`. Review existing artifacts in `logos/artifacts/`. Produce additional definitions and primitives needed for the Alignment Paradox topic that are not yet defined. Key terms still needing definition: "specification", "process", "protocol", "good faith", "epistemic humility", "cognitive bias", "identity-protected belief". Write each as a separate markdown artifact file in `logos/artifacts/` following the PROTOCOL naming convention (LOGOS-NNNN-slug.md).

**Axiom subagent** — spawn with:
- Working directory context: `axiom/`
- Instructions: Read `axiom/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read the seed topic. Review existing axioms in `axiom/artifacts/` and definitions in `logos/artifacts/`. Evaluate the existing axiom set: are there gaps? Produce any additional axioms or postulates needed. Write each as a separate markdown artifact file in `axiom/artifacts/` following the PROTOCOL naming convention (AXIOM-NNNN-slug.md).

### Wave 2 — Propositions (after Wave 1 completes)

**Propo subagent** — spawn with:
- Instructions: Read `propo/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read ALL definitions in `logos/artifacts/` and ALL axioms in `axiom/artifacts/`. Generate at least 5-8 propositions that follow from these foundations, relevant to the Alignment Paradox topic. Each proposition must use only defined terms and be truth-evaluable. Write each as a separate markdown artifact file in `propo/artifacts/` following the PROTOCOL naming convention (PROPO-NNNN-slug.md).

### Wave 3 — Classification (after Wave 2 completes)

**Ori subagent** — spawn with:
- Instructions: Read `ori/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read ALL propositions in `propo/artifacts/`. For EACH proposition, produce a classification artifact that determines whether it is a priori, a posteriori, or mixed. Use the negation test, conceivability test, and justification test. Write each classification as a separate markdown artifact file in `ori/artifacts/` following the PROTOCOL naming convention (ORI-NNNN-slug.md).

### Wave 4 — Proof & Testing (run in parallel, after Wave 3)

**Tribunal subagent** — spawn with:
- Instructions: Read `tribunal/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read the classifications in `ori/artifacts/`. For each proposition classified as `a_priori`, attempt a formal step-by-step proof from the accepted axioms in `axiom/artifacts/`. Produce theorem, lemma, or corollary artifacts. If proof fails, document what additional axiom would be needed. Write artifacts to `tribunal/artifacts/`.

**Hypothex subagent** — spawn with:
- Instructions: Read `hypothex/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read the classifications in `ori/artifacts/`. For each proposition classified as `a_posteriori`, structure it into a proper falsifiable hypothesis with null hypothesis, evidence specification, and at least one alternative hypothesis. Write artifacts to `hypothex/artifacts/`.

### Wave 5 — Theory Building (after Wave 4)

**Theorica subagent** — spawn with:
- Instructions: Read `theorica/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read ALL artifacts in `tribunal/artifacts/` and `hypothex/artifacts/`. Look for clusters of related theorems and hypotheses. Build at least one theory that unifies findings about the Alignment Paradox. Write artifacts to `theorica/artifacts/`.

### Wave 6 — Synthesis (after Wave 5)

**Synthesis subagent** — spawn with:
- Instructions: Read `synthesis/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Read ALL artifacts across ALL agent directories. Identify the most significant contradiction or tension in the artifact space. Perform a full dialectical synthesis: steelman both sides, identify the precise point of conflict, construct a resolution that preserves valid elements and dissolves the contradiction. The synthesis should re-enter the pipeline as a new proposition. Write artifacts to `synthesis/artifacts/`.

### Wave 7 — Observation (after all waves, or run periodically)

**Watcher subagent** — spawn with:
- Instructions: Read `watcher/CLAUDE.md` for your role. Read `shared/PROTOCOL.md` for artifact format. Scan ALL `artifacts/` directories across all agents. Build the master registry at `shared/registry.md`. Count artifacts by agent, by status, by type. Identify any bottlenecks, stalls, or quality issues. Produce a system state report as an artifact in `watcher/artifacts/`.

## RULES

- **Each subagent MUST produce real files.** If a subagent finishes without creating artifacts, something went wrong.
- **Subagents must read their CLAUDE.md** — it contains their full role description, quality standards, and evaluation criteria.
- **Subagents must follow PROTOCOL.md** — especially the artifact template with YAML frontmatter.
- **Use absolute paths** from the dialectic-agents root when spawning subagents, so they can find files across directories.
- **After each wave, verify artifacts were created** by listing the relevant `artifacts/` directory before proceeding to the next wave.
- **If a subagent reports no input available** (e.g., Ori finds no propositions), check if the previous wave actually produced output.

## GIT PROTOCOL — Commit & Push After Each Wave

After EACH wave completes (and after verifying artifacts were created), you MUST run the following git commands using the Bash tool:

```bash
# Stage all new and modified artifacts
git add -A

# Commit with a descriptive message identifying the wave and epoch
git commit -m "Epoch <N>, Wave <W>: <description>

Agents: <list of agents that ran>
Artifacts produced: <count of new artifacts>
Topics: <domain(s) covered>

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Push to remote
git push origin main
```

### Wave-specific commit messages:

- **Wave 1**: `"Epoch <N>, Wave 1: Foundation — Logos definitions + Axiom postulates"`
- **Wave 2**: `"Epoch <N>, Wave 2: Propositions — Propo generated N propositions"`
- **Wave 3**: `"Epoch <N>, Wave 3: Classification — Ori classified N propositions"`
- **Wave 4**: `"Epoch <N>, Wave 4: Proof & Testing — Tribunal + Hypothex processed N items"`
- **Wave 5**: `"Epoch <N>, Wave 5: Theory building — Theorica built N theories"`
- **Wave 6**: `"Epoch <N>, Wave 6: Synthesis — N dialectical resolutions"`
- **Wave 7**: `"Epoch <N>, Wave 7: Observation — Watcher system state report"`

### After a full epoch (all 7 waves), also commit a summary:

```bash
git add -A
git commit -m "Epoch <N> complete: <total new artifacts> artifacts across <agents>

Summary:
- Definitions: <count>
- Axioms: <count>
- Propositions: <count>
- Classifications: <count>
- Theorems/Lemmas: <count>
- Hypotheses: <count>
- Theories: <count>
- Syntheses: <count>

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

git push origin main
```

### Git safety:
- If `git push` fails due to remote changes, run `git pull --rebase` first, then push again.
- If there's a `.git/index.lock` file blocking operations, remove it with `rm -f .git/index.lock` before proceeding.
- Never force push. Never amend commits.

## RUNNING ADDITIONAL ROUNDS (EPOCHS)

After completing one full pipeline pass (Epoch 1), you can run additional epochs:
- Start from Wave 2 (Propo) — generate new propositions from the expanded knowledge base
- Synthesis outputs become new propositions for the next cycle
- Each round should deepen understanding and resolve remaining contradictions
- Increment the epoch counter: Epoch 2, Epoch 3, etc.
- **Commit and push after each wave in every epoch.**
