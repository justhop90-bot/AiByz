# Open Native Questions — Layer 1

These are not defects in the operational contract. They are the highest-value unresolved native questions after the preservation QC passes and the latest UnitAI/reference-recovery experiments.

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
21. **API metadata consumer and dispatch representation:** what native structure consumes the contiguous API name/signature region, and how an API identifier becomes a callable native handler.
22. **UnitAI state ownership:** which native object/module owns `CurrentAction`, order state, target state, and notification queues, and which functions mutate them.
23. **UnitAI invalidation path:** what event/condition converts a valid action into the observed failed/invalidated/search-required state.
24. **Search-to-target mutation boundary:** whether native search directly writes target state or returns a candidate to a separate selection/execution layer.

## Research priority

Prioritize questions by architectural leverage rather than curiosity. Scheduler determinism, action atomicity, resource reservation, target lifetime, loader/execution closure, API metadata dispatch, and concrete UnitAI state mutation chains have the highest downstream impact because they constrain virtually every future subsystem.

The latest full-text instruction scan produced no direct RIP-relative references to the tested API and UnitAI diagnostic strings. This is now a methodological constraint: further research should target indirect tables, relative/indexed metadata, initialization consumers, dispatch structures, and state mutation chains rather than repeating broad direct-string xref scans.
