# P0 Dropsite / Resource Logistics Forensics

**Project:** AEGIS-BYZ  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Authoritative corpus:** untouched stock `resources\_common\ai\Promisory` on the project machine  
**Status:** Forensic evidence captured; implementation deliberately deferred.

## Executive finding

The stock economy treats dropsite topology as an operational constraint on resource acquisition. Resource decisions are not based only on the existence of a resource object. Stock combines resource discovery with dropsite distance, camp-distance policy, source availability, construction state, and strategic conditions.

The architectural consequence is that a resource source is serviceable only in relation to infrastructure capable of receiving its output. AEGIS must model source and dropsite as a coupled logistics relationship rather than independent objects.

## 1. Initialization establishes explicit logistics parameters

`Promisory/init.per` initializes distinct strategic parameters for food, wood, gold, and stone drop distances, plus a maximum fish-boat drop distance. It also initializes `sn-minimum-dropsite-buffer = 13`, `sn-required-forest-tiles = 10`, `sn-camp-max-distance = 12`, and `sn-mill-max-distance = 18`, alongside civilian gatherer/build/explorer caps.

The same initialization establishes intelligent gathering and retasking controls. These values are consumed by later resource and building rules as operational gates.

## 2. Dropsite distance participates in resource policy

`gatherers.per` repeatedly uses `dropsite-min-distance` in conditions that change gatherer allocation across food, wood, gold, stone, hunting, scouting, and infrastructure-related decisions.

This establishes that distance to the relevant dropsite is part of the economic state used to decide whether a source remains attractive or another acquisition path should be considered.

The critical distinction is:

```text
resource distance != service distance
```

A resource may be physically present but economically or operationally unattractive because its delivery relationship to a dropsite is poor.

## 3. Lumber camp migration is explicitly distance-driven

`buildings.per` contains a direct wood-camp rule. When wood is found but `dropsite-min-distance wood > 5`, and the distance remains within map bounds, stock can build another lumber camp when an existing camp is present and the camp-distance policy permits it.

The rule enables adjacent dropsites, adjusts `sn-camp-max-distance`, and issues `build lumber-camp`.

This is direct evidence that infrastructure can be created as a response to a degraded resource-to-dropsite relationship.

```text
existing wood service
      ↓
wood delivery distance increases
      ↓
camp-distance policy permits migration
      ↓
request new lumber camp
      ↓
new infrastructure
      ↓
shorter logistics path
```

## 4. Camp placement has bounded adaptive behavior

The stock building rules show `sn-camp-max-distance` being increased incrementally when wood, gold, or stone is found at progressively greater dropsite distance, subject to an upper bound.

Observed rules compare `dropsite-min-distance RESOURCE` against `sn-camp-max-distance` and increment the permitted camp distance when the source is within a bounded range.

Therefore the camp-distance threshold is not one immutable constant. Stock can adapt its willingness to build additional dropsites to the spatial layout.

## 5. Gold and stone use the same logistics architecture

Gold mining-camp rules require resource discovery plus spatial constraints. Representative conditions include:

```text
resource-found gold
mining-camp requirement
 dropsite-min-distance gold > minimum
 dropsite-min-distance gold <= sn-camp-max-distance
can-build mining-camp
```

Other rules detect cases where an existing gold camp is insufficiently positioned and can request another camp. Stone uses the same conceptual mechanism with resource-specific conditions.

AEGIS should therefore implement one common **Source ↔ Dropsite Serviceability** model rather than separate conceptual logistics systems for wood, gold, and stone.

## 6. Construction state is part of logistics state

Stock distinguishes existing building counts, pending objects, `can-build`, placement state, and camp-type requests. `general.per` also contains lumber-camp placement reset behavior: when placement remains pending under specified conditions, stock calls `up-reset-placement` and adjusts camp-distance policy.

Thus logistics realization is transactional:

```text
need shorter delivery path
      ↓
select camp type
      ↓
placement
      ↓
foundation / pending state
      ↓
completion
      ↓
usable dropsite
```

A failed placement cannot be treated as equivalent to a completed camp.

## 7. Resource source and dropsite must be represented separately

AEGIS should represent:

```text
RESOURCE SOURCE
  identity
  type
  status
  task-load
  location
  remaining/availability evidence

DROPSITE
  identity
  type
  status
  location
  capacity/utility evidence

SERVICE RELATIONSHIP
  source
  dropsite
  delivery distance
  reachability
  current worker load
  policy threshold
  validity/freshness
```

The economic scheduler should reason about required capacity. The Resource Acquisition Service should determine whether a particular source/dropsite pair can actually deliver that capacity.

## 8. `dropsite-min-distance` is not proven to be exact walking distance

The stock predicate is an engine-level measurement used as a resource/dropsite spatial gate. The present evidence does not establish its exact internal distance metric or pathfinding algorithm.

AEGIS specifications should therefore call this **delivery/service distance** until independently characterized.

## 9. Strategic and operational layers remain distinct

The evidence supports this chain:

```text
Strategic policy
  ↓
Economic allocation
  ↓
Logistics / serviceability
  ↓
Infrastructure requirement
  ↓
Worker tasking
```

A high-level objective should not directly issue a camp-building command without logistics establishing the need and service relationship.

## 10. Proposed AEGIS logistics contract

```text
SOURCE DISCOVERY
      ↓
SOURCE STATUS
      ↓
DROPSITE DISCOVERY
      ↓
SOURCE ↔ DROPSITE DISTANCE
      ↓
REACHABILITY / SPATIAL VALIDITY
      ↓
TASK LOAD / WORKER CAPACITY
      ↓
SERVICEABILITY
      ↓
  ┌───┴────┐
  ▼        ▼
VALID    INVALID
  │        │
  ▼        ▼
TASK     MIGRATE / BUILD
         NEW DROPSITE
```

Minimum serviceability record:

```text
source-id
source-type
dropsite-id
delivery-distance
source-status
dropsite-status
task-load
worker-capacity
threshold
observed-at
generation
valid
failure-reason
```

## 11. Negative findings

This pass does **not** prove that `dropsite-min-distance` is exact path distance, that every resource type uses identical placement algorithms, that camp migration is immediate at every threshold, that every failed placement has identical recovery, or that stock has one centralized logistics manager.

The evidence instead shows distributed logistics logic connected through shared engine predicates and strategic numbers.

## 12. Architectural consequence

AEGIS civilian substrate should contain a distinct **Logistics / Serviceability layer** between economic demand and worker tasking:

```text
Strategy
  ↓
Economic Demand
  ↓
Resource Allocation
  ↓
Logistics / Serviceability
  ├─ source state
  ├─ dropsite state
  ├─ delivery relationship
  ├─ capacity/load
  └─ infrastructure requirement
  ↓
Infrastructure Service
  ↓
Worker Assignment Service
  ↓
Execution
  ↓
Verification
  ↓
Recovery
```

This refines the Resource Acquisition Service model: **source selection cannot be correct without a serviceability relationship to infrastructure.**

## Next forensic target

Continue with source-specific exhaustion and migration evidence for woodline, gold, stone, forage/farms, and fishing; then threat-driven evacuation, worker-death accounting, and construction interruption/builder replacement.

No AEGIS runtime implementation should begin from this document alone. Remaining evidence must establish failure taxonomy and timing semantics first.
