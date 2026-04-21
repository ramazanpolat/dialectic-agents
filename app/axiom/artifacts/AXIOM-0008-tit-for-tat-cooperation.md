---
id: AXIOM-0008
agent: axiom
type: postulate
status: accepted
created: 2026-02-22T15:19:00Z
updated: 2026-02-22T15:19:00Z
domain: game-theory
depends_on: []
confidence: 0.93
layer: 2
---

# Postulate: Tit-for-Tat Is the Optimal Strategy for Repeated Cooperation

## Statement
In iterated cooperation games (repeated interactions between agents who can choose to cooperate or defect), the strategy of tit-for-tat — cooperate first, punish defection proportionally, forgive immediately — is mathematically proven to outperform all alternatives over sufficient iterations.

## Justification
Axelrod's tournaments (1980s) demonstrated this empirically. The mathematical proof follows from the combination of four properties: (1) niceness (cooperate first), (2) retaliatory (punish defection), (3) forgiving (return to cooperation after punishment), (4) clarity (behavior is predictable and interpretable).

## Classification: Postulate
This has formal mathematical support within game theory but is domain-specific (applies to iterated games with specific payoff structures) rather than universally self-evident.

## Self-Evidence Test
**FAIL as self-evident, PASS as formally proven** — This is a theorem within game theory, not an axiom of logic. Its "axiomatic" status in this framework is as a foundational principle for designing cooperation protocols.

## Independence Test
**PASS** — Not derivable from the other postulates.

## What Changes If This Postulate Is False
If tit-for-tat is NOT optimal:
- The good-faith requirement in the dialectical protocol may need different enforcement
- The Arbiter agent's strategy for detecting and punishing bad faith would need revision
- Alternative cooperation mechanisms might be needed

## Dependencies
None within this axiom set (draws on game theory as external foundation)

## Evaluation Notes
This postulate grounds the protocol's trust mechanism. Dialectics requires good faith; tit-for-tat provides the mathematical guarantee that good faith is sustainable.

## Lineage
TCP/IP Dialectics framework — "Tit-for-tat is an evolved strategy." Robert Axelrod, The Evolution of Cooperation (1984).
