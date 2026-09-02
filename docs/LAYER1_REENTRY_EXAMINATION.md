# Layer 1 Independent Re-entry Examination

This examination is the archival quality gate for machine knowledge. A future engineer should be able to answer these questions using repository evidence without consulting the original conversation.

## Section A — Runtime

1. Identify the exact target executable, version/product metadata, and SHA-256.
2. Explain the relationship between `.ai` bootstrap files and `.per` rule source.
3. Describe the loader graph and identify which edges are proven versus inferred.
4. Identify the role of `loadExpertRules` and the limits of the evidence.

## Section B — Rule machine

5. Define a rule, trigger, handler, rule group, priority, minimum interval, and maximum interval.
6. Describe the hypothesized rule lifecycle from construction through execution.
7. Explain which scheduler properties remain unproven.
8. Explain why source order must not automatically be assumed to equal execution order.
9. Explain the distinction between trigger interpretation failure and handler interpretation/execution failure.

## Section C — State

10. Distinguish facts, goals, strategic numbers, timers, beliefs, and hypotheses.
11. Explain persistence and temporal hysteresis.
12. Explain why observation, inference, intent, authorization, execution, verification, and recovery are separate architectural stages.
13. Identify examples of contextual range differences.

## Section D — Interface typing

14. Distinguish concrete unit IDs, unit-line IDs, and unit-class IDs.
15. Explain the `knight-line` incident and what it teaches about identifier domains.
16. Explain why integer validity does not establish semantic validity.
17. Describe what a complete UP API ledger must contain.
18. Describe the evidence standard for adding an XS capability.

## Section E — Execution

19. Distinguish feasibility, command issuance, execution success, world-state change, postcondition verification, and strategic success.
20. Explain pending-object state and resource reservation as distinct concepts.
21. Explain target lifetime and stale-plan risk.
22. Explain action idempotence and why recovery depends on it.
23. Explain validator/runtime divergence.

## Section F — Reverse engineering

24. Describe the string → xref → function → call graph → data flow → hypothesis → validation process.
25. Explain why decompiler output is not automatically authoritative.
26. Explain the significance of Ghidra function-body repair noise.
27. Identify the negative source-recovery results and their epistemic meaning.
28. Explain the native/source boundary policy.

## Section G — Research methodology

29. Describe the evidence hierarchy.
30. Explain how contradictory evidence is preserved.
31. Explain evidence decay and build/version fingerprinting.
32. Explain what constitutes a reproducible investigation bundle.
33. Explain how causal claims differ from correlations observed in replays.

## Section H — Architecture

34. State the ownership/authority model.
35. Explain why consequential state should have declared ownership.
36. Describe the command/postcondition registry.
37. Describe the machine invariants catalog.
38. Explain the machine capability ceiling.
39. Explain architecture-to-machine compilation.
40. Identify the next unresolved native question and propose a falsifiable experiment.

## Pass criterion

A candidate passes only if answers are grounded in repository evidence and correctly label `CONFIRMED`, `PROBABLE`, `PLAUSIBLE`, `UNCERTAIN`, `OBSOLETE`, `ENGINE_SPECIFIC`, and `DISPROVEN` claims. Confident but unsupported answers constitute failure.
