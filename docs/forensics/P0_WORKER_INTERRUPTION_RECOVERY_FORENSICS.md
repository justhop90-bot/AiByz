# P0 Worker Interruption / Recovery Forensics

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Authoritative corpus:** untouched stock `resources\\_common\\ai\\Promisory` on the project machine  
**Status:** Forensic evidence captured; no AEGIS runtime changes made.

## Executive finding

The stock civilian substrate contains explicit worker interruption/recovery logic. It does not reduce worker validity to a single `idle` flag. Instead it evaluates combinations of target identity, order, action, carry state, and target status, then issues `action-stop` to workers judged to have invalid or stale orders so they can re-enter normal tasking.

This proves that individual worker assignment is a lifecycle with validity and recovery, not a one-shot role assignment.

## Exact evidence: gatherers.per ~4416-4456

The stock code first constructs a villager working set. It excludes explorers, the boar lurer, and tree-targeting workers, then inspects individual objects.

A recovery rule tests:

- `object-data-target-id == -1`
- order is `orderid-attack`, `orderid-build`, `orderid-repair`, or `orderid-enter`

Its action is:

- `up-target-point 0 action-stop -1 -1`

The adjacent comment identifies the purpose as retasking a "buggy villager."

A second recovery rule tests:

- `object-data-target-id == -1`
- order is `orderid-gather` or `orderid-hunt`

and likewise issues `action-stop`.

The explicit `object-data-idling` and `object-data-carry` tests in these recovery rules are commented out. Therefore the stock implementation is not simply `idling == true -> retask`; it uses order/target consistency as a principal validity signal.

## Builder-specific recovery

A separate rule tests:

- `object-data-order == orderid-build`
- `object-data-target-id != -1`
- target object's `object-data-status != status-pending`

and then issues `action-stop`.

This is strong evidence that construction state is represented through the relationship between builder order, target identity, and target status. A builder with a build order does not automatically represent valid construction; the target must be in the expected pending state.

## Pending infrastructure is a first-class substrate state

Additional stock evidence in `gatherers.per`, `general.per`, and `interaction.per` repeatedly uses `status-pending` with `up-find-status-local` / `up-find-status-remote`.

Observed examples include mining camps, mills, Town Center foundations, and defensive/construction searches.

Therefore:

`building count > 0` is not equivalent to `building operational > 0`.

AEGIS construction state must preserve at least pending/foundation versus completed/operational distinctions.

## Revised worker lifecycle model

The evidence supports this model:

```text
worker identity
    + role/accounting state
    + action
    + order
    + target
    + target status
    + carry state
    + spatial relationship
            |
            v
       TASK VALIDITY
        /          \\
     valid        invalid
       |             |
   continue       stop/cleanup
                     |
                     v
               reassignment pool
```

Worker role is therefore an accounting/intent layer. Physical task validity is independently observed from engine state.

## Architectural implication for AEGIS

The AEGIS Worker Assignment Service should not treat command issuance as successful assignment. Minimum lifecycle:

```text
REQUEST
 -> CANDIDATE
 -> ELIGIBILITY
 -> SOURCE SELECTED
 -> DROPSITE RELATIONSHIP VALID
 -> ORDER ISSUED
 -> TARGET VALID
 -> TASK ACTIVE
 -> PRODUCTIVE
```

Failure exits include:

- target lost
- source depleted
- dropsite invalid
- order invalid
- builder target invalid
- worker interrupted
- worker threatened
- incompatible carry state
- worker death

These should converge on:

```text
TASK INVALID
 -> STOP / CLEANUP
 -> RECLASSIFY
 -> REASSIGN
```

## Important negative finding

The evidence does **not** prove that stock has one centralized worker recovery manager. Recovery appears distributed, especially across `gatherers.per`, with related infrastructure-state handling in `general.per` and `interaction.per`.

AEGIS may centralize task validity/recovery as an architectural improvement while retaining engine-native state queries and action primitives.

## P0 status

Proven:

1. civilian policy -> integer allocation -> individual tasking is multi-stage;
2. worker task validity is independently checked after assignment;
3. invalid orders can be explicitly stopped and returned to retasking;
4. construction uses target status as part of validity;
5. pending infrastructure is a first-class query state;
6. role/accounting state and physical task state must remain separate.

Not yet proven:

- exact source-depletion reassignment behavior for each food source;
- dropsite disappearance/invalidation recovery;
- threat-driven worker evacuation/reassignment;
- worker-death accounting latency;
- farm regeneration/reassignment;
- fishing recovery;
- full relationship between `action-default` and persistent task recognition.

## Next forensic target

Trace resource-source failure and reassignment across sheep/herdables, boar, deer, forage, farms, wood, gold, stone, and fishing. Determine the exact trigger, candidate selection, spatial constraints, and recovery path for each source class before implementing the AEGIS Resource Acquisition Service.
