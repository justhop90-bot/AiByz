# Open Native Questions — Layer 1

These are not defects in the operational contract. They are the highest-value unresolved native questions after the preservation QC passes and the latest `.per`-first structural investigation.

## `.per` implementation frontier

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
15. Loader call graph from AI selection to rule registration.
16. Parser/interpreter boundary for `.per` constructs.
17. Native error propagation from failed action to scheduler state.
18. Environment-dependent behavior of the AI runtime.
19. Whether machine behavior is deterministic under identical world-state inputs.
20. UnitAI state ownership: which native object/module owns `CurrentAction`, order state, target state, and notification queues, and which functions mutate them.
21. UnitAI invalidation path: what event/condition converts a valid action into the observed failed/invalidated/search-required state.
22. Search-to-target mutation boundary: whether native search directly writes target state or returns a candidate to a separate selection/execution layer.
23. AIExpert rule-list ownership: what native object owns `listId`, `ruleElementsPtr`, indexed rule elements, and rule debug metadata.
24. Fact/action registration timing: whether fact and action IDs are assigned during lexical parsing, semantic construction, registration, or game initialization.
25. Persistent-fact cadence: when persistent facts are evaluated and what state snapshot or cache they observe.
26. Rule navigation state: how jumps, `Next Rule`, and breakpoints interact with sorted-rule scheduling and current-rule state.
27. Rule-to-UnitAI bridge: which native path turns a rule/handler result into an action or order request.
28. Action-result feedback: which native path carries completion, failure, invalidation, or search-required results back into UnitAI and/or the rule scheduler.
29. Search ownership: whether `ai::search` is a shared service or a UnitAI-owned subsystem in the target build.
30. Rule-state mutation: which verified native function reads, branches on, and writes rule scheduler state.
31. Persistent-fact state mutation: which verified native function produces and stores the evaluated fact result.
32. UnitAI action/order mutation: one verified read → transition → write → consumer chain for `CurrentAction` or `CurrentOrder`.
33. Action conflict resolution: what happens when multiple rule handlers issue competing requests within one evaluation window.
34. Runtime feedback: which state becomes script-visible after native action completion, failure, or invalidation.

## Research priority

Prioritize questions by architectural leverage. Scheduler determinism, parser/rule construction, persistent-fact evaluation, action atomicity, resource reservation, target lifetime, the rule-to-UnitAI bridge, and concrete UnitAI mutation chains have the highest downstream impact because they constrain virtually every future ByzBot subsystem.

## Native archaeology only — outside ByzBot implementation scope

XS and XS qualification are explicitly excluded from the ByzBot implementation and from the Layer 1 completion gate. They may be investigated when useful for general machine understanding, but they are not implementation dependencies.

The prior XS questions remain preserved as historical archaeology rather than active implementation priorities: metadata record geometry, metadata consumers, identifier-to-handler resolution, symbol-table lookup, syscall registration, function-entry/code-offset semantics, activation-record PC transitions, and related runtime internals.

## Methodological boundary

The latest pass revalidated the PE section mapping: `.rdata` uses RVA `0x313c000` with raw pointer `0x313ac00`. Direct RIP-relative scanning of selected AIExpert and UnitAI diagnostic strings produced zero references for the tested instruction representation. This is negative evidence only for that representation.

Source/debug string adjacency is therefore not an admissible function locator. Future work should begin from verified `.pdata` function boundaries, compact state structures, constants/IDs, native reads/writes, and runtime falsification experiments.

## Next discriminating work

The next investigation should recover one structural `.per` edge rather than another vocabulary inventory. Preferred order: persistent-fact state mutation, rule-state mutation, UnitAI `CurrentAction`/`CurrentOrder` mutation, then the rule-to-action bridge.
