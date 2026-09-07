# P0 Resource-Source Failure / Reassignment Forensics

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Authoritative corpus:** untouched stock `resources\\_common\\ai\\Promisory` on the project machine  
**Status:** Forensic evidence captured; no AEGIS runtime changes made.

## Executive finding

Stock resource acquisition is not a simple `find resource -> assign villager` operation. It maintains resource-source state, task load, source status, dropsite distance, and worker eligibility. Food sources have materially different lifecycle controllers.

The strongest new evidence is that the engine exposes **resource task load** (`object-data-tasks-count`) and stock actively uses it to avoid overloading sources and to detect whether a source is currently being served.

## Wood-source allocation

In `gatherers.per` around lines 2958-3042, stock:

1. resets search state;
2. filters resource status to active/ready states;
3. searches for wood resources with `up-find-resource`;
4. reads `object-data-tasks-count` on candidate resources;
5. prefers/limits candidates based on task load;
6. finds local villagers;
7. excludes workers with enter/build/tree-target conflicts;
8. selects a resource by distance/order;
9. issues `action-default`.

This proves that resource selection is a **capacity/load-aware allocation problem**, not merely nearest-resource selection.

## Farm-source management

Around lines 3375-3417, stock searches farms and reads `object-data-tasks-count`. It then uses worker target state (`object-data-target == forage-food` or `sheep-food`) and current shepherd/forager counts to redirect workers.

This demonstrates that the stock food system can deliberately transform a worker's existing food-source role into another food-source role. A worker is therefore not permanently classified as a shepherd/forager; the role is operational and reassigned according to current source conditions and aggregate counts.

## Boar-source lifecycle

`boarhunting.per` contains a substantially richer source state machine.

Before committing to `current-boar`, stock validates the object by ID and checks status. If the target is no longer suitable, it clears `current-boar`, `found-boar`, and related state and disables the reset timer.

A second validation checks:

- current boar is valid;
- carry state has not crossed the computed threshold;
- reset timer has not expired in the relevant condition;
- boar is not too far from the live-boar/dropsite relationship;
- current action is still appropriate.

If these conditions fail, stock clears the active boar state and allows the hunting controller to re-enter selection.

## Boar task-load arbitration

Before assigning hunters, stock checks `object-data-tasks-count` on the current boar. It then searches eligible villagers, excludes incompatible workers, removes candidates with an existing `boar-food` target, sorts by precise distance, limits the candidate set, and issues `action-default`.

Thus boar hunting has explicit source-side concurrency control:

```text
boar identity
 -> source status
 -> source task load
 -> worker eligibility
 -> spatial filtering
 -> distance ordering
 -> task assignment
```

## `action-default` finding

`action-default` is not itself sufficient evidence of a persistent assignment abstraction. It is repeatedly used as the physical order-issuance primitive after stock has already selected a worker and target. Persistence is represented by the resulting engine object state: order/action/target/task-load, which later recovery logic reads back.

Therefore AEGIS should model:

```text
COMMAND ISSUED != TASK CONFIRMED
```

Confirmation requires subsequent observation of target/order/task state.

## Dropsite coupling

Stock repeatedly gates resource policy and source selection on `dropsite-min-distance`. This is not merely a strategic heuristic; it is part of the resource-acquisition substrate. The same resource can therefore be operationally unacceptable when its drop path exceeds configured constraints.

AEGIS resource records must consequently distinguish:

- source exists;
- source has usable status;
- source has available capacity;
- source is spatially serviceable;
- suitable dropsite exists;
- worker can reach/service source;
- source is strategically desirable.

## New Resource Acquisition Service model

The evidence supports:

```text
RESOURCE DISCOVERY
 -> SOURCE VALIDATION
 -> CAPACITY / TASK-LOAD CHECK
 -> DROPSITE VALIDATION
 -> WORKER CANDIDATE SET
 -> ELIGIBILITY FILTERS
 -> SPATIAL / DISTANCE RANKING
 -> COMMAND ISSUED
 -> ENGINE STATE OBSERVED
 -> PRODUCTIVE
```

Failure should return to discovery rather than blindly reissue the same command:

```text
source invalid/depleted
OR dropsite invalid
OR task load unsuitable
OR worker invalid
OR command loses target
        ↓
TASK INVALID
        ↓
RELEASE / STOP AS NEEDED
        ↓
RESELECT SOURCE / WORKER
```

## Important negative finding

The present evidence does not yet prove the exact depletion trigger for every resource class. In particular, sheep, deer, farms, fishing, wood, gold, and stone may use different source-status transitions and different recovery timing.

It also does not prove a universal centralized stock resource manager. Evidence continues to favor distributed per-resource controllers.

## P0 status after this pass

Proven:

1. resource sources expose task-load state;
2. stock uses source task load during allocation;
3. source status is queried before assignment;
4. dropsite distance participates in resource-service decisions;
5. food roles can be deliberately reassigned between source types;
6. boar hunting has explicit source validation and reset behavior;
7. command issuance is followed by observable engine state rather than assumed success;
8. resource acquisition is a feedback loop, not a one-shot command.

Still required:

- exact source-depletion behavior for sheep/deer/forage/farms;
- woodline exhaustion behavior;
- gold/stone mine depletion behavior;
- fishing-source/boat recovery;
- threat-driven evacuation and reassignment;
- worker-death accounting latency;
- construction interruption and builder replacement;
- complete source-status enum semantics relevant to each resource class.

## Architectural consequence

AEGIS Resource Acquisition must be designed as a **closed-loop service**. It must own neither strategic policy nor worker identity, but it must own the operational transaction from a valid resource demand to a verified productive source assignment and recovery when the transaction becomes invalid.

This reinforces the project-level separation:

```text
Strategy        = what resource pressure is needed
Economy         = how much capacity is needed
Escrow          = what resources are reserved
Resource Service= where/how workers acquire it
Execution       = whether the engine command is authorized
Verification    = whether the assignment actually exists
Recovery        = what to do when it does not
```

## Next forensic target

Continue source-class-specific depletion/recovery, beginning with sheep/deer/forage/farms, then wood/gold/stone and fishing. In parallel, trace threat-driven civilian evacuation and worker-death accounting so the Resource Acquisition Service can define its failure taxonomy from evidence rather than design preference.
