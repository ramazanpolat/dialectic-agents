---
id: AXIOM-0004
agent: axiom
type: postulate
status: accepted
created: 2026-02-22T15:19:00Z
updated: 2026-02-22T15:19:00Z
domain: ai-ethics
depends_on: [LOGOS-0001, LOGOS-0002]
confidence: 0.88
layer: 2
---

# Postulate: Humans Have an Alignment Problem With Themselves

## Statement
Individual humans do not reliably act in accordance with their own stated values. The values humans articulate, the values they believe they hold, and the values revealed by their behavior are three distinct and often contradictory sets.

## Justification
This is the core insight of the Alignment Paradox. The four metacognitive bugs guarantee misalignment:
1. **Identity-protected beliefs** — humans defend beliefs that define their identity, regardless of evidence
2. **Emotional interference** — fear, pride, and shame corrupt the reasoning process
3. **Social cost of updating** — human culture punishes changing your mind
4. **Cognitive fatigue** — humans cannot sustain rigorous reasoning indefinitely

## Classification: Postulate (not Axiom)
Domain-specific to human cognition. An agent without these bugs (e.g., a well-designed AI) might not have this problem.

## Self-Evidence Test
**PARTIAL** — Every human can introspect and find examples, but the claim goes beyond introspection to a systematic claim about ALL humans.

## Independence Test
**PASS** — Not derivable from AXIOM-0003 (values change ≠ humans are misaligned with their own values).

## What Changes If This Postulate Is False
If humans ARE reliably aligned with their own values, then:
- You could simply ask humans what they value and trust the answer
- Alignment becomes a specification problem, not a process problem
- The need for dialectical infrastructure diminishes significantly

## Dependencies
- LOGOS-0001 (definition of alignment)
- LOGOS-0002 (definition of values)

## Evaluation Notes
This postulate has strong empirical support from cognitive science (Kahneman, Haidt, Mercier & Sperber) but is deeply uncomfortable because it applies to everyone, including the person reading it.

## Lineage
TCP/IP Dialectics framework — "Humans are aligned with the *belief* that they're aligned, not with actual truth."
