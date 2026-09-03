# Layer 1 Native Pass — Retrospective QC Amendment

**Date:** 2026-09-02  
**Scope:** Quality-control review of the UnitAI control-loop/reference-recovery pass  
**Authority:** Research/evidence record only; no implementation authority

## 1. Executive QC finding

The previous UnitAI pass contained substantially more information than its headline conclusions conveyed. This amendment preserves the useful discoveries while tightening several claims that could otherwise become stronger than their evidence.

The principal result is not merely that direct references were absent. The combination of positive native vocabulary, negative direct-reference experiments, and the structure of the API signature region changes the correct archaeological strategy.

The investigation has crossed a methodological boundary:

```text
before: locate names and follow obvious references
now: recover representation, ownership, mutation, and dispatch mechanisms
```

That is a real advancement, but the machine is not yet sufficiently traced to declare Layer 1 complete.

## 2. Critical distinction: two different negative searches

The pass contains two separate negative experiments and they must remain separate in the permanent record.

### A. Absolute-pointer scan

The selected target virtual addresses were searched as exact little-endian 64-bit values.

Result: zero exact occurrences for the tested targets.

This rejects only the hypothesis that those target addresses appear directly in the scanned representation as embedded absolute 64-bit pointers.

### B. RIP-relative instruction scan

Capstone decoded the complete known `.text` range and tested RIP-relative memory operands whose effective address resolved to the selected API strings, the widened API signature region, or selected UnitAI diagnostic strings.

Result: zero direct RIP-relative hits for the tested targets.

This rejects the hypothesis that ordinary decoded RIP-relative instructions in the tested `.text` representation directly address those targets.

### QC rule

Neither result means “nothing references the strings.” Future documentation must never use that shorthand without specifying the representation and search mechanism actually tested.

## 3. What the zero-reference result means architecturally

The result is stronger than a failed search but weaker than proof of indirection.

The surviving possibilities include:

- indirect registration tables;
- pointers to tables rather than strings;
- relative offsets reconstructed at initialization;
- hashes or ordinals;
- generated indices;
- runtime-built maps;
- pointer-to-pointer structures;
- another module containing the actual consumer;
- code that computes an address rather than embedding the target reference;
- diagnostic metadata that is not used in ordinary execution.

Therefore the correct conclusion is:

> The tested direct-reference representation is not currently the shortest path to implementation recovery.

The next experiment should discriminate among surviving representations rather than repeat the rejected one.

## 4. The API signature region is a structured archaeological target

The strongest positive observation is the repeated pairing of API names with typed signature strings, for example:

```text
xsGetUnitObjectId
int xsGetUnitObjectId(int32_t unitId)

xsGetUnitCopyId
int xsGetUnitCopyId(int32_t unitId)

xsGetObjectCopyId
int xsGetObjectCopyId(int32_t playerId, int32_t objectId)
```

This establishes a rich native vocabulary and a meaningful co-location pattern.

It does **not** establish a C/C++ structure layout, registration-table implementation, or function-pointer relationship.

The next structural test should therefore examine the region as a candidate record system:

```text
entry boundary
alignment
field widths
relative offsets
pointer-like values
index-like values
hash-like values
neighbor relationships
initialization consumers
```

The highest-value discovery would be a consumer that takes information from this region and produces an executable dispatch decision.

## 5. UnitAI evidence is richer than the headline model

The native vocabulary supports at least these distinct conceptual state families:

```text
ORDER
  currentOrder
  currentOrderPriority
  OrderQueue

ACTION
  CurrentAction
  action failure/invalidation/search-required state

TARGET
  currentTargetID
  currentTargetType
  currentTargetValue
  CurrentTarget
  CurrentTargetPosition
  DefendTarget
  DesiredTargetDistance

NOTIFICATION
  NotifyQueueSize
  processNotify

SEARCH
  LOS
  searchRadius
  object-interest filters
  relationship classification
  candidate validation
  BESTUNITTOATTACK

PROCESSING
  processIdle
  processNotify
  order/action processing
```

The important insight is the **orthogonality** of these vocabularies. They should not be collapsed into one generic “AI state” merely because their exact owning class has not yet been recovered.

This is enough to justify separate research tracks for order, action, target, notification, and search state.

## 6. New hypothesis: intent and execution are different state domains

The distinction between `currentOrder` and `CurrentAction` is one of the highest-value findings in the pass.

Current evidence supports:

```text
ORDER = requested/selected work context
ACTION = current mechanical execution state
```

The exact semantics and lifetime remain unproven.

This suggests a deeper invariant worth testing:

> An order can remain meaningful while its current action becomes invalid and must be replaced.

If runtime/native evidence demonstrates that invariant, it becomes a foundational machine contract for the eventual ByzBot executor.

## 7. New hypothesis: target state is not equivalent to target identity

The presence of ID, type, value, position, defend-target, and desired-distance concepts indicates that a target context contains more information than an object handle alone.

A future target model should therefore distinguish:

```text
identity
classification
strategic value
spatial reference
relationship/role constraint
execution constraints
```

This is especially important because a target may remain strategically relevant while its machine-level object representation changes.

No claim is made here that these fields belong to one native structure. That is precisely one of the next questions to resolve.

## 8. New hypothesis: search may be state reconstruction

The search diagnostics are compatible with two interpretations:

1. search is primarily target acquisition; or
2. search is a broader state-repair operation invoked when the current execution context is insufficient.

The explicit “failed / invalidated / requires a search” vocabulary makes interpretation 2 substantially more interesting, but it remains a hypothesis.

A discriminating experiment should compare:

```text
search with valid current target
vs.
search after target invalidation
vs.
search after path invalidation
```

If the same search machinery reconstructs execution state in multiple failure modes, the state-repair interpretation becomes much stronger.

## 9. New hypothesis: queues represent different causal directions

`OrderQueue` and `NotifyQueue` are unlikely to be semantically interchangeable.

The useful working abstraction is:

```text
OrderQueue  = internalized future work
NotifyQueue = incoming information about change
```

The important unresolved questions are:

- who writes each queue;
- whether queues are FIFO or priority-ordered;
- whether processing can recursively enqueue more work;
- whether notifications can invalidate queued orders;
- whether order processing can generate notifications;
- whether either queue survives an update boundary.

These questions matter because they determine whether the native controller is merely periodic or genuinely event-reactive.

## 10. Closed-loop control interpretation

The strongest current architectural interpretation is a feedback controller:

```text
DESIRED WORK
    ↓
ORDER
    ↓
ACTION
    ↓
EXECUTION
    ↓
WORLD RESPONSE
    ↓
OBSERVATION / NOTIFICATION
    ↓
VALIDATION
    ↓
SEARCH / REPAIR
    ↓
NEW ACTION
```

This is not yet a recovered native call graph.

It is nevertheless a high-value hypothesis because it changes what must be measured. If the machine is a closed-loop controller, then measuring only decision issuance misses a large portion of its intelligence.

The future runtime instrumentation should therefore capture state before and after invalidation, not merely commands emitted.

## 11. Programmer-intent QC

The previous pass's programmer-intent section is directionally useful but must be read as reconstruction from engineering constraints rather than historical fact.

The strongest defensible statement is:

> The observed separation of order/action/target/notification vocabulary is consistent with a design that must reconcile persistent requested work against changing simulation state.

The weaker and currently unsupported statement would be:

> The original programmer intentionally designed a specific hierarchical reactive architecture.

We do not possess enough implementation-level evidence to make the latter historical claim.

The repository should continue using implementation structure, data ownership, lifetime, error handling, repeated patterns, and runtime behavior as the basis for programmer-intent reconstruction.

## 12. Revised predictive test

The original target-loss experiment should be expanded into a **state-divergence matrix**.

| Perturbation | Initial state | Question | High-value observation |
|---|---|---|---|
| Target disappears | order + action + target | Does action invalidate? | transition and recovery path |
| Target changes owner | order + target | Is target revalidated? | ownership-driven transition |
| Path becomes unavailable | movement action | Does action invalidate or search? | path-recovery mechanism |
| Better target appears | active combat | Is current target replaced? | retarget comparator/policy |
| Order interrupted | queued/current work | What happens to current action? | queue/state arbitration |
| Notification arrives during action | active execution | Is action preempted? | notification priority/atomicity |

For each perturbation the required trace is:

```text
PRECONDITION
→ TRIGGER
→ DISPATCH
→ PROCESSING
→ READ
→ DECISION/CONDITION
→ WRITE
→ CONSUMER
→ EXECUTION
→ POSTCONDITION
```

The critical addition is **READ → WRITE → CONSUMER**. That is the missing bridge between vocabulary and causal implementation.

## 13. Identity and UnitAI must eventually converge

The UnitAI and identity investigations are not independent.

A target state containing `currentTargetID` cannot be fully understood until the meaning and lifetime of that ID are known.

Therefore the eventual end-to-end trace should connect:

```text
UnitAI target state
      ↓
identifier interpretation
      ↓
native object lookup
      ↓
object validity/lifecycle
      ↓
action validation
      ↓
search/retarget/recovery
```

This is a major leverage point. Solving identity may unlock UnitAI state semantics; solving UnitAI mutation may reveal how identity is consumed.

The next investigation should deliberately look for this intersection rather than treating the two dossiers as isolated topics.

## 14. What should not be inferred from the pass

The following remain explicitly unproven:

- exact UnitAI class hierarchy;
- exact owner of each state field;
- exact update frequency;
- exact scheduler ordering;
- exact queue ordering;
- exact search-stage ordering;
- exact target scoring function;
- exact invalidation trigger;
- exact API registration record layout;
- exact API dispatch mechanism;
- equality or conversion among unit ID, object ID, copy ID, `obj->id`, `uniqueID`, and replay references;
- exact runtime identity lifetime;
- exact relationship between UnitAI and script-rule scheduling.

## 15. Repository QC correction

The prior pass updated the status, index, and open-question register, which was correct. This amendment is additionally required because the quantity of architectural interpretation in the pass could otherwise outrun its evidence annotations.

The amendment therefore adds three permanent rules:

1. **State-bearing is safer than universally persistent** until write/reset/lifetime traces exist.
2. **Reactive controller is a hypothesis** until scheduler and notification ordering are recovered.
3. **Search decomposition is conceptual** until instruction-level control flow demonstrates the stages.

These rules should be applied retroactively whenever the older pass is cited.

## 16. Layer 1 impact assessment

The pass should be considered a significant advancement because it narrows the problem from broad discovery to two concrete implementation bridges:

### Bridge A — metadata → dispatch

```text
API metadata
    ↓
consumer
    ↓
identifier/index
    ↓
dispatch
    ↓
native handler
```

### Bridge B — state → mutation

```text
UnitAI state
    ↓
read
    ↓
condition
    ↓
write
    ↓
next consumer
```

A third bridge connects them to simulation identity:

### Bridge C — target → object lifecycle

```text
target reference
    ↓
ID interpretation
    ↓
object lookup
    ↓
validity/lifecycle
    ↓
execution consequence
```

Layer 1 will become substantially more complete when these bridges are traced with native implementation evidence.

## 17. Next-pass mandate

Do not perform another broad string census.

Do not treat the current diagrams as recovered call graphs.

Do not implement the strategic framework yet.

Instead:

1. characterize the API signature region structurally;
2. locate candidate initialization consumers;
3. search for indirect/relative/indexed relationships;
4. identify one concrete UnitAI state owner;
5. recover one actual state write;
6. follow its subsequent consumer;
7. connect target-state usage to identity/lifecycle where possible;
8. run the state-divergence experiment when instrumentation is available;
9. update the atomic evidence ledger with every promotion or falsification.

## Final assessment

The previous pass was valuable precisely because it exposed the architecture's likely shape while simultaneously demonstrating that the obvious archaeological breadcrumb path is insufficient.

The correct response is not to weaken the findings. It is to **grade them more precisely and attack the remaining bridges directly**.

The machine is now understood well enough to formulate high-leverage predictions about the native controller, but not yet well enough to claim predictive implementation-level closure.

**Layer 1 remains active.**
