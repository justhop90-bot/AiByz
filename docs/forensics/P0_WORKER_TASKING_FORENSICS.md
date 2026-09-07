# P0 Worker Tasking Forensics

**Project:** AEGIS-BYZ
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** Forensic extraction; implementation deliberately deferred

## Executive finding

The stock civilian system does not convert `wood-villagers` or similar goals directly into a single worker-assignment command. Instead, the observed implementation uses worker-role populations, object searches, eligibility filters, spatial searches, and `action-default` tasking to close the loop.

The critical newly proven execution boundary is the villager production path:

```text
trainvillager goal
 -> up-can-train escrow-state villager
 -> up-train escrow-state villager
 -> pending villager
 -> completed villager
```

Therefore `trainvillager` is a policy/authorization state, not the physical production operation.

## 1. Villager production execution

Target-build `Promisory/units.per` contains two active execution rules around lines 12093-12111.

Rule 1 requires:

```text
(goal trainvillager yes)
(up-can-train escrow-state c: villager)
```

and issues:

```text
(up-train escrow-state c: villager)
```

Rule 2 uses the same authorization and additionally considers pending-villager state / food-drop timing / multiple-TC state before issuing another `up-train`.

This establishes three separate concepts:

1. production policy (`trainvillager`);
2. economic/engine authorization (`up-can-train` with `escrow-state`);
3. physical queue command (`up-train`).

AEGIS must preserve this separation.

## 2. Worker-role goals are intermediate accounting state

`dawn.per` owns integer goals including:

- `sum-villagers`;
- `wood-villagers`;
- `food-villagers`;
- `gold-villagers`;
- `stone-villagers`.

The forensic search shows these goals are mutated during allocation and consumed by downstream logic as targets/thresholds. They are not themselves worker commands.

Examples include:

```text
(unit-type-count villager-wood g:<= wood-villagers)
```

followed by a spatial worker search and eventual `up-target-objects ... action-default ...`.

This means the system compares desired role population against actual role population and only then performs task selection.

## 3. Actual wood tasking pipeline

The stock lumberjack path observed in `gatherers.per` is substantially more sophisticated than a role-count setter.

When actual `villager-wood` is below the desired `wood-villagers`, stock:

1. selects nearby lumber camps;
2. obtains the camp position;
3. establishes a local spatial search;
4. filters workers by class;
5. excludes workers entering buildings;
6. excludes workers already assigned to trees;
7. excludes workers carrying resources;
8. cleans candidates by distance;
9. searches for wood resources;
10. filters resource status/task load;
11. selects an appropriate tree;
12. targets workers using `action-default`.

The relevant observed sequence includes:

```text
(up-find-remote c: lumber-camp c: 3)
(up-set-target-object search-remote c: 0)
(up-get-point position-object saved-point-x)
(up-set-target-point saved-point-x)
(up-filter-distance c: -1 c: 6)
(up-filter-exclude -1 actionid-attack orderid-build -1)
(up-find-local c: villager-class g: villagercount)
(up-remove-objects search-local object-data-action == actionid-enter)
(up-remove-objects search-local object-data-order == orderid-enter)
(up-remove-objects search-local object-data-target == tree-class)
(up-remove-objects search-local object-data-carry >= 1)
(up-clean-search search-local object-data-distance search-order-asc)
```

The next phase searches wood resources and removes candidates whose task count is already high, then ultimately issues:

```text
(up-target-objects 0 action-default -1 -1)
```

## 4. Meaning of this discovery

The stock worker allocator is therefore a constrained assignment system, not a percentage-to-command converter.

Conceptually:

```text
DesiredRoleCount
      ↓
ActualRoleCount
      ↓
Deficit
      ↓
CandidateWorkerSet
      ↓
EligibilityFilters
      ↓
SpatialInfrastructureRelationship
      ↓
ResourceCandidateSet
      ↓
Load/Status/Distance Filtering
      ↓
Worker → Task assignment
```

This is a much stronger substrate model for AEGIS.

## 5. Tasking is spatially coupled

The lumberjack path establishes that worker selection is related to the location of the relevant dropsite/infrastructure and the resource itself.

The same structural pattern appears in the observed mining and forage paths. Stock first establishes the relevant dropsite/structure relationship, searches workers around it, and then searches the appropriate resource class.

Thus an AEGIS worker task should not be represented merely as:

```text
worker -> wood
```

but as something closer to:

```text
worker
 -> source
 -> dropsite
 -> spatial relationship
 -> expected task validity
```

## 6. Role identity is emergent operational state

The evidence also changes how `villager-wood`, `villager-forager`, `villager-gold`, etc. should be modeled.

They should not be treated as immutable worker classes. They are observed operational-role states that arise from the worker's current task/targeting behavior.

Therefore AEGIS should maintain:

```text
worker identity
worker eligibility
current task
current source
current dropsite
current role
role confidence/freshness
```

rather than permanently converting a villager into a role object.

## 7. Interruption and reassignment implication

Because stock explicitly excludes workers by current action/order/target/carry state before reassignment, reassignment is not a blind overwrite.

The minimum AEGIS state machine should therefore be:

```text
Assigned
  ↓
Task Valid
  ↓
Productive
  ↓
Task Invalid / Interrupted
  ↓
Candidate for reassignment
  ↓
Eligibility + cause classification
  ↓
New assignment
  ↓
Productive
```

A worker carrying resources should not be treated as equivalent to an idle worker. A worker entering a building should not be treated as an ordinary reassignment candidate. A worker already gathering the desired resource should not be reassigned merely because the aggregate role target changed by one unit.

## 8. New AEGIS substrate requirement

The civilian operating system needs an explicit **Worker Assignment Service** between economic allocation and raw engine tasking.

Proposed contract:

```text
WORKER_ASSIGN_REQUEST
  generation
  worker/role target
  resource/source type
  source constraints
  dropsite constraints
  urgency
  priority
  reason

WORKER_ASSIGN_RESULT
  generation
  worker identity
  selected source
  selected dropsite
  command/evidence stage
  failure reason
```

This service should own candidate filtering and assignment execution. The economic scheduler should request capacity; it should not directly manipulate individual workers.

## 9. Critical negative finding

We have **not** yet proven that every role transition in stock is represented by one centralized worker-assignment service. The evidence currently shows distributed per-resource tasking logic in `gatherers.per`, plus dedicated systems such as `boarhunting.per`.

Therefore the AEGIS architecture should be centralized even if the stock implementation is distributed.

## 10. Next forensic target

The remaining P0 gap is the complete interruption/recovery lifecycle:

1. identify every generic idle-worker detector;
2. identify how stock distinguishes idle from busy/carrying/entering/building;
3. identify what happens when a source disappears;
4. identify what happens when a dropsite disappears or becomes invalid;
5. identify threat-driven worker evacuation/reassignment;
6. identify construction interruption and builder recovery;
7. identify whether worker death updates role accounting immediately or through periodic recomputation;
8. trace boar/deer/farm/fishing reassignment paths;
9. extract civ-specific deviations;
10. determine the exact relationship between `action-default`, resource targets, and role-state recognition.

## Verdict

**P0 worker tasking is now partially proven.**

The civilian substrate is best modeled as a closed-loop constrained assignment system. The next layer is not another economic percentage analysis; it is **failure, interruption, and recovery of individual civilian tasks**.
