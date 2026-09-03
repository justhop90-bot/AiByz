# AEGIS Layer 1 — Final Quality-Control Audit of the 89% Handoff

**Date:** 2026-09-03
**Scope:** Final investigation handoff and public repository consistency
**Disposition:** ACCEPTED WITH EXPLICIT LIMITATIONS
**Layer 1 position:** **89% — investigation closed / completion gate not satisfied**

## Executive finding

The 89% handoff is substantively defensible. It is not a claim that 89% of the executable has been reverse engineered, nor a claim that 89% of all native subsystems are understood. It is a project-progress position against the project's predictive-machine-understanding standard.

The handoff is credible because the remaining uncertainty is explicit, bounded, and concentrated in implementation-level causal edges. The repository does not need to pretend those edges were solved in order to be useful to the next engineer.

## 1. What the final QC confirms

The repository now has a coherent top-level navigation path from `README.md` through `RESEARCH_INDEX.md`, final project status, the final Layer 1 handoff, predictive standard, evidence matrix, native archaeology/QC records, `.pdata` function geometry, open native questions, and atomic knowledge ledgers.

The final handoff identifies the controlled executable by version, size, SHA-256, image base, and architecture. Native conclusions are therefore build-scoped rather than silently generalized across game versions.

The public documentation intentionally redacts the user's local installation path while retaining the information necessary to reproduce the identity check on an authorized machine.

## 2. The most important methodological achievement

The investigation progressed from vocabulary-first research to a mechanically bounded native coordinate system.

The `.pdata` record provides 166,730 non-zero runtime-function ranges from 166,741 physical 12-byte slots, with 11 trailing zero slots. Valid starts are unique and monotonically ordered, with no overlaps in the tested image. Aggregate interval coverage is approximately 88.88% of raw `.text` size.

This does not create a semantic function inventory. It creates a bounded search substrate for native code. That distinction is now central to the project methodology.

The practical consequence is that future archaeology can proceed as:

`verified function geometry -> validated instruction body -> state/data access -> branch/call relationship -> mutation -> consumer -> runtime consequence`

rather than:

`interesting string -> guessed owner -> guessed semantics`.

## 3. Final PDB finding and its correct interpretation

The executable contains CodeView `RSDS` identity for a PDB with GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d` and age `1`, with an embedded build-system path ending in `AoE2DE_s.pdb`.

No matching PDB was established locally. Therefore the PDB is a future lead only. A future file becomes evidence only after GUID/age authentication against the exact controlled executable. Filename coincidence is insufficient.

This distinction should remain permanent because an apparently authoritative symbol file could otherwise contaminate the entire native evidence chain.

## 4. Final negative evidence

The direct-reference experiments found no RIP-relative references to seven selected AI diagnostic/source anchors and no exact executable-wide 64-bit absolute-pointer occurrences for those addresses.

The result is valid as bounded negative evidence for those representations. It does not prove that AI code is absent or that the strings are unused. Indirect, indexed, encoded, table-mediated, generated, or otherwise transformed references remain possible.

The correct engineering response is therefore not to conclude absence, but to change search strategy toward verified function bodies and data flow.

## 5. Final false-positive lesson

A metadata-area pointer resolved to a valid `.pdata` function at `0x1417FF3E0`. Direct examination showed cleanup/destructor-like behavior, so the proposed XS API ownership association was rejected.

This experiment is a positive methodological result because it demonstrates that three apparently strong observations can still be insufficient:

`metadata proximity + valid pointer + valid function boundary != semantic ownership`.

Ownership requires independent caller/callee, data-flow, state-effect, registration, or equivalent evidence.

## 6. AIExpert: final knowledge boundary

The investigation has strong native vocabulary for rule loading, lexical/preprocessor handling, constants, facts, actions, rule elements, rule debug metadata, persistent-fact evaluation, rule navigation, breakpoints, and semantic game-state queries.

The remaining implementation questions are deliberately narrower:

- which verified function evaluates persistent facts;
- where its result is stored;
- whether that result is cached;
- how long it remains valid;
- which scheduler boundary refreshes it;
- which rule-evaluation function consumes it;
- how handler/action output crosses into native control.

The strongest missing causal edge remains:

`fact source -> evaluator -> result mutation -> rule consumer`.

## 7. UnitAI: final knowledge boundary

The investigation has strong native vocabulary for CurrentOrder, CurrentAction, CurrentState, CurrentTarget, CurrentTargetType, target position, OrderQueue, NotifyQueue, search, retryable orders, retargeting, action completion, failure, invalidation, and search-required conditions.

The remaining implementation target is one verified mutation chain, preferably:

`CurrentOrder -> transition -> CurrentAction`

or:

`action failure/invalidation -> recovery/search -> target/action replacement`.

The goal is not to reconstruct every UnitAI function. One verified causal transition followed by its consumer would materially advance predictive understanding.

## 8. Temporal model remains a hypothesis

The project has a useful but explicitly unproven multiple-cadence hypothesis: strategic rule/fact state, tactical UnitAI state, and simulation state may advance at different temporal granularities.

This hypothesis has practical explanatory power for stale observations, command latency, asynchronous recovery, and durable orders, but it must not be promoted to machine fact without scheduler/state-mutation evidence or a discriminating runtime experiment.

## 9. Practical ByzBot implications

The final handoff supports a strategic-over-tactical architecture:

`observation -> belief -> Byzantine strategic intent -> tactical request -> native validation/acceptance -> execution -> observed result -> reconciliation`.

This is a design recommendation, not a recovered class diagram.

ByzBot should own strategic valuation, opportunity cost, long-horizon planning, opponent modeling, Byzantine doctrine, composition, timing, and conflict arbitration. Native capabilities such as feasibility, tactical search, pathing, target management, action execution, and local recovery should be reused when they meet requirements rather than duplicated reflexively.

The most important implementation discipline is explicit assumption isolation: unresolved Layer 1 behavior must sit behind replaceable interfaces and be labeled as unresolved rather than silently encoded as fact.

## 10. What the 11% actually means

The remaining 11% is qualitatively different from the preceding 89%. It is not a list of hundreds of missing vocabulary items. It is a small set of high-leverage implementation boundaries:

1. rule-loader/parser implementation boundary;
2. rule representation ownership and mutation;
3. persistent-fact result storage/freshness;
4. scheduler comparator/interval transition;
5. rule/handler-to-native-action bridge;
6. CurrentOrder-to-CurrentAction mutation;
7. action failure/completion propagation;
8. required identity/lifecycle edges;
9. one runtime-predictive end-to-end `.per` path.

These are difficult because each can materially change the behavior of an AI built above the machine.

## 11. Why 89% is the correct stopping position

The project deliberately refuses percentage inflation based on documentation volume, repeated vocabulary, plausible architecture, pointer proximity, decompiler labels, replay interpretation, or validator behavior.

A percentage increase requires new demonstrated machine knowledge.

Therefore the correct final statement is:

**Layer 1 is 89% complete as a project-progress estimate against the predictive standard; the investigation phase is closed; the completion gate is not satisfied.**

## 12. Six-month recovery test

A future AI or engineer should be able to recover the project by reading, in order:

1. `README.md`;
2. `RESEARCH_INDEX.md`;
3. `docs/PROJECT_STATUS_2026-09-02.md`;
4. this final investigation handoff;
5. `docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`;
6. `docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md`;
7. `docs/LAYER1_MACHINE_KNOWLEDGE.md`;
8. native archaeology/QC documents;
9. AIExpert/UnitAI and persistent-fact passes;
10. `.pdata`/PDB/RIP findings;
11. object identity dossier;
12. open native questions;
13. atomic knowledge ledgers and investigation history.

The engineer should emerge knowing what is fact, what is inference, what was experimentally rejected, what remains unknown, why 89% is correct, and exactly where to resume.

## 13. Final repository consistency audit

The final audit found the major governing documents aligned on the same disposition: Layer 1 investigation closed at 89%, completion gate unsatisfied, remaining work concentrated in implementation-level causal closure, XS excluded from both ByzBot implementation dependency and completion gating, and the `.pdata` method retained as the preferred structural substrate.

The research index already exposes the final handoff, predictive standard, evidence matrix, native archaeology passes, `.pdata` findings, open-question register, and atomic ledgers in a coherent recovery sequence.

The repository is therefore **handoff-ready for the current investigation state**. It should not be described as history-certified-clean or native-complete; those are separate claims and remain explicitly bounded elsewhere.

## Final disposition

**TRUE 89% HANDOFF: ACCEPTED.**

The project has reached the appropriate investigation stopping point: mature machine model, strong evidence discipline, explicit uncertainty, durable institutional memory, practical architectural consequences, and a sharply defined remaining native frontier.

The next AI should not restart the investigation from scratch. It should not collect more vocabulary for the sake of completeness. It should either implement the next project layer with explicit assumptions or, if native work resumes, attack the smallest remaining causal edge using the `.pdata`-bounded methodology and promote only demonstrated transitions.
