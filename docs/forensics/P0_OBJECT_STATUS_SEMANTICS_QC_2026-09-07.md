# P0 Object Status Semantics QC — 2026-09-07

**Project:** AEGIS-BYZ  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Corpus:** untouched stock `resources\_common\ai\Promisory` on Weebo  
**Purpose:** QC and refinement of the civilian failure/recovery findings.

## Executive result

The previous civilian failure findings survive direct reinspection. This pass resolves an important ambiguity: stock explicitly defines the object-status constants and the `object-data-status` field semantics.

From `Promisory/defaultConstants.per`:

```text
status-pending  = 0
status-ready    = 2
status-resource = 3
status-down     = 4
status-gather   = 5
```

The same file defines:

```text
object-data-status = 19
```

with the stock comment:

```text
0: incomplete, 2: active, 3: resource, >=4: inactive
```

It also defines:

```text
object-data-tasks-count = 32
```

and documents it as internal tasks performed on an object, with the warning that the count may be greater than one per event.

## 1. Status 2 is both `status-ready` and object-data "active"

The earlier reports used phrases such as “active/ready status.” That wording is now formally qualified.

Stock assigns the same numeric value, `2`, to `status-ready`, while the object-data comment calls status 2 “active.” These are not two separately established states in the ABI evidence; they are two names/descriptions for the same status value in this corpus.

Therefore AEGIS documentation should use:

```text
status 0 = pending/incomplete
status 2 = ready/active
status 3 = resource
status 4+ = inactive/down family
status 5 = gather-specific symbolic state
```

with the caveat that status 5 is numerically inside the `>=4` inactive range described by the generic object-data comment. Its actual meaning is therefore **context-dependent at the call site** and must not be flattened into a universal lifecycle ordering.

## 2. `status-resource` is used as a resource-search state filter

The stock corpus repeatedly passes `status-resource` into resource searches. Examples occur in `buildings.per`, `gatherers.per`, and `extremebuildings2.per` before `up-find-resource` calls for gold, stone, wood, forage, ocean fish, and shore fish.

This establishes that stock distinguishes resource-search eligibility from ordinary active-building/unit eligibility.

Important consequence:

```text
RESOURCE SEARCH
  requires resource-appropriate status semantics
```

It should not be modeled as simply “find any object with hitpoints.”

## 3. `status-ready` is used as an explicit active-resource filter

`gatherers.per` contains paths where resource discovery is followed by:

```text
(up-filter-status c: status-ready c: list-active)
```

This is direct evidence that the stock allocator can narrow a resource/object search to status 2 after a broader resource search.

Thus the distinction is operational:

```text
up-find-resource
      ↓
optional status filtering
      ↓
candidate resource set
```

The status filter is not merely decorative metadata.

## 4. Pending construction is a separate observable state

`buildings.per`, `interaction.per`, `escrow.per`, and other stock modules repeatedly use:

```text
(up-filter-status c: status-pending c: list-active)
(up-find-status-local ...)
(up-find-status-remote ...)
```

Construction code therefore treats pending objects as a searchable population distinct from active/completed infrastructure.

This validates the earlier construction transaction model:

```text
request
→ pending placement/foundation
→ incomplete object
→ active object
```

A count of completed buildings cannot substitute for pending-object state.

## 5. `status-gather` is context-sensitive and must not be generalized

The corpus contains `status-gather` searches in gatherer logic, including `up-find-status-remote` paths. Because the generic object-data comment groups values `>=4` as inactive while the symbolic constant defines `status-gather = 5`, AEGIS must not infer that “gather” is globally equivalent to “inactive.”

The correct engineering interpretation is:

```text
status constants have subsystem-specific operational use
```

The call site determines the intended object population.

This is an important guard against over-normalizing the engine ABI.

## 6. `object-data-tasks-count` is not a worker-count field

Stock uses task count as a candidate-selection and load signal. Concrete examples include:

```text
wood: remove resource candidates with tasks-count >= 2
boar: require tasks-count <= 0 for one targeting path
boar support: inspect tasks-count and calculate remaining task allowance
```

These examples use different thresholds and purposes.

Therefore the strongest supported statement is:

```text
object-data-tasks-count = engine-visible object workload signal
```

It is **not proven** to mean:

```text
number of assigned workers
```

nor:

```text
remaining economic capacity
```

Those are derived interpretations that require further engine experimentation.

## 7. Source state and worker state remain separate

The stock boar path demonstrates the separation directly. It can:

1. resolve a cached source object by ID;
2. inspect its status;
3. inspect its task load;
4. inspect delivery distance;
5. inspect its action;
6. decide whether to target it;
7. separately search for eligible villagers;
8. issue `action-default`.

Therefore an AEGIS resource transaction must not collapse source validity and worker eligibility into one Boolean.

## 8. Worker recovery remains a two-stage operation

The inspected `gatherers.per` recovery block first builds a worker search and then detects invalid orders/targets. It uses `action-stop` to terminate invalid work.

The subsequent allocation logic is separate.

The evidence therefore supports:

```text
INVALID TASK
     ↓
CLEAN / STOP
     ↓
ELIGIBLE WORKER
     ↓
ALLOCATOR
     ↓
NEW TARGET
     ↓
ACTION-DEFAULT
```

The earlier rule remains mandatory:

```text
COMMAND ISSUED != TASK CONFIRMED
```

## 9. Threat remains a policy gate, not a proven global state machine

The threat search was rechecked. Stock uses `up-enemy-units-in-town`, `underattack`, and `defend` in multiple civilian/infrastructure decisions, including suppression or redirection of farming, livestock, mining, and construction behavior.

However, the corpus still does not prove one global worker evacuation controller.

AEGIS must therefore distinguish:

```text
THREAT OBSERVED
THREAT BLOCKS OPERATION
THREAT REQUIRES EVACUATION
```

These are different predicates.

## 10. Construction recovery is more explicit than worker replacement

The construction corpus contains concrete pending-object searches, builder-count conditions, target-status validation, deletion of failed pending structures, placement reset, and adaptive camp-distance changes.

This proves substantial construction recovery plumbing.

It still does not prove one universal transaction:

```text
builder dies
→ exact builder loss detected
→ same foundation preserved
→ replacement builder selected
→ construction resumes
```

Builder replacement remains an open forensic target.

## 11. Revised AEGIS object model

The minimum safe object record should separate:

```text
OBJECT ID
OBJECT TYPE / CLASS
OBJECT STATUS
OBJECT ACTION
OBJECT ORDER
OBJECT TARGET ID
OBJECT TARGET TYPE
OBJECT LOCATION
OBJECT DROPSITE
OBJECT RESOURCE
OBJECT CARRY
OBJECT TASK LOAD
OBJECT HITPOINTS
OBJECT MAX HP
OBSERVED-AT
WORLD GENERATION
```

A derived serviceability record should then be computed from these observations rather than stored as immutable truth.

## 12. Revised failure model

The evidence supports the following causal decomposition:

```text
SOURCE IDENTITY
      ↓
SOURCE STATUS
      ↓
SOURCE WORKLOAD
      ↓
SOURCE SERVICEABILITY
      ↓
WORKER ELIGIBILITY
      ↓
WORKER TASK STATE
      ↓
COMMAND
      ↓
OBSERVED ENGINE STATE
```

Failure can occur at any layer.

That gives AEGIS typed failure classes without pretending the stock engine exposes those classes directly.

## 13. QC verdict

**Confirmed:**

- status-pending = 0;
- status-ready = 2;
- status-resource = 3;
- status-down = 4;
- status-gather = 5;
- object-data-status = field 19;
- object-data-tasks-count = field 32;
- pending construction is separately searchable;
- resource searches use explicit resource status semantics;
- worker recovery and source selection are separable operations;
- task-load filtering is real stock behavior;
- threat-aware civilian gating is real stock behavior.

**Not proven:**

- status 5 as a universal lifecycle state;
- exact mathematical meaning of task count;
- universal worker evacuation;
- immediate event-driven worker-death accounting;
- universal builder replacement;
- one centralized civilian recovery manager.

## Next pass

Move from symbolic status semantics into **object lifecycle by subsystem**. Trace one complete lifecycle for each of wood, gold, stone, forage, boar/deer, livestock, fishing, and construction:

```text
DISCOVERED
→ SELECTED
→ ASSIGNED
→ ACTIVE
→ PRODUCTIVE
→ INVALIDATED
→ CLEANED
→ RESELECTED
→ PRODUCTIVE
```

For every transition, record the exact stock predicate/action responsible. The objective is to determine where a common AEGIS lifecycle service is legitimate and where the stock ABI requires specialized handlers.
