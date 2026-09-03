# Layer 1 Independent Re-entry Examination — Final Handoff

**Final investigation position:** 89%  
**Investigation phase:** CLOSED / HANDOFF  
**Completion certification:** NOT SATISFIED

This examination is the archival quality gate for machine knowledge. A future engineer should be able to answer these questions using repository evidence without consulting the original conversation. It is also the final re-entry checklist for resuming the bounded native frontier.

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
11. Explain persistence, temporal hysteresis, and the unresolved fact-freshness question.
12. Explain why observation, inference, intent, authorization, execution, verification, and recovery are separate architectural stages.
13. Identify examples of contextual range differences.

## Section D — Interface typing

14. Distinguish concrete unit IDs, unit-line IDs, and unit-class IDs.
15. Explain the `knight-line` incident and what it teaches about identifier domains.
16. Explain why integer validity does not establish semantic validity.
17. Describe what a complete UP API ledger must contain.
18. Explain why XS is machine archaeology only and is not a ByzBot implementation or Layer 1 completion dependency.

## Section E — Execution

19. Distinguish feasibility, command issuance, execution success, world-state change, postcondition verification, and strategic success.
20. Explain pending-object state and resource reservation as distinct concepts.
21. Explain target lifetime and stale-plan risk.
22. Explain action idempotence and why recovery depends on it.
23. Explain validator/runtime divergence.

## Section F — Reverse engineering

24. Describe the evolution from string-first archaeology to `.pdata`-bounded function-first analysis.
25. Explain why decompiler output is not automatically authoritative.
26. Explain the significance of Ghidra function-body repair noise and the 1800-second controlled headless timeout.
27. Identify the negative source/reference-recovery results and their epistemic meaning.
28. Explain the native/source and public/private evidence boundaries.
29. Explain why metadata proximity plus a valid function pointer did not prove XS API ownership.
30. Explain the significance of the embedded CodeView PDB GUID/age and why filename matching is insufficient.

## Section G — Research methodology

31. Describe the evidence hierarchy.
32. Explain how contradictory evidence and failed experiments are preserved.
33. Explain evidence decay and build/version fingerprinting.
34. Explain what constitutes a reproducible investigation bundle.
35. Explain how causal claims differ from correlations observed in replays.
36. Explain why zero direct references eliminate only the tested representation, not the underlying subsystem.

## Section H — Architecture

37. State the ownership/authority model.
38. Explain why consequential state should have declared ownership.
39. Describe the command/postcondition model.
40. Describe the machine invariants catalog.
41. Explain the machine capability ceiling.
42. Explain architecture-to-machine compilation.
43. Identify the final unresolved implementation frontier: persistent-fact mutation/freshness, scheduler state mutation, rule-to-action bridge, `CurrentOrder -> CurrentAction`, failure propagation, required identity lifecycle edges, and one predictive end-to-end path.
44. Explain the promotion test for the next native edge: `read -> condition -> write -> consumer -> observable consequence`.

## Pass criterion

A candidate passes only if answers are grounded in repository evidence and correctly label `CONFIRMED`, `PROBABLE`, `PLAUSIBLE`, `UNCERTAIN`, `OBSOLETE`, `ENGINE_SPECIFIC`, `DISPROVEN`, and `HISTORICAL` claims. Confident but unsupported answers constitute failure.

## Six-month recovery entry point

Start with `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`, then `RESEARCH_INDEX.md`, the final project status, predictive standard, completion control, evidence matrix, machine monograph, native archaeology/QC records, atomic facts/history, and the final open-question register. The authoritative investigation position is 89% until new evidence demonstrates otherwise.
