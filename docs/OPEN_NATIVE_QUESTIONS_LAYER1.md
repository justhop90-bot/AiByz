# Open Native Questions — Layer 1

These are not defects in the operational contract. They are the highest-value unresolved native questions after the preservation QC passes.

1. Exact scheduler ordering comparator and tie-breakers.
2. Exact minimum/maximum interval units and boundary behavior.
3. Fairness/starvation behavior among eligible rules.
4. Exact group/rule synchronization timing.
5. Trigger versus handler execution boundaries.
6. Intra-handler state visibility and action atomicity.
7. Resource reservation timing relative to feasibility and command issuance.
8. Pending-object lifecycle and cancellation semantics.
9. Target-handle lifetime and invalidation behavior.
10. Search result ordering and stability.
11. Fact cache/freshness semantics.
12. AI evaluation tick boundary relative to simulation updates.
13. Hidden scheduler/interpreter state not exposed to scripts.
14. Exact validator/runtime semantic divergences.
15. Exact XS capability qualification surface on the target build.
16. Loader call graph from AI selection to rule registration.
17. Parser/interpreter boundary for `.per` constructs.
18. Native error propagation from failed action to scheduler state.
19. Environment-dependent behavior of the AI runtime.
20. Whether machine behavior is deterministic under identical world-state inputs.

## Research priority

Prioritize questions by architectural leverage rather than curiosity. Scheduler determinism, action atomicity, resource reservation, target lifetime, and loader/execution closure have the highest downstream impact because they constrain virtually every future subsystem.
