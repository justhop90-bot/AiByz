# P0 Worker Accounting and Builder Continuity QC — 2026-09-07

**Project:** AEGIS-BYZ  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Authoritative corpus:** untouched stock `resources\\_common\\ai\\Promisory` on Weebo  
**Status:** forensic evidence; implementation deliberately deferred.

## Executive result

This pass resolves an important part of the civilian substrate model: stock maintains recurrent population/accounting state rather than exposing a dedicated villager-death event controller in the inspected corpus. `villagercount` is initialized through an explicit fact acquisition, while `villagercounttotal` is a persistent goal used by strategic/economic systems. This supports a census/accounting architecture and does **not** prove immediate event-driven death accounting.

Construction continuity is also more nuanced than a simple builder-count test. Stock explicitly tracks builders as a searchable worker population (`villager-builder`), excludes current builders when selecting some replacement candidates, and uses pending-building state as an independent construction population. The inspected evidence does not prove a universal builder-death replacement transaction.

## 1. Villager accounting is explicitly acquired

`Promisory/init.per:698-704` contains:

```per
(up-get-fact population 0 my-pop)
(up-get-fact civilian-population 0 my-cpop)
(up-get-fact military-population 0 my-mpop)
(up-get-fact unit-type-count villager villagercount)
villagercounttotal
(up-modify-goal villagercount c:min 240)
(up-modify-goal villagercounttotal
```

The direct implication is that stock has at least two distinct accounting concepts:

- `villagercount`: a fact-derived current villager count used by the AI;
- `villagercounttotal`: a separate goal/state value used in later policy calculations.

The latter is not interchangeable with the former merely because both concern villagers.

## 2. `villagercounttotal` participates in strategic/economic calculations

The corpus uses `villagercounttotal` in `gatherers.per`, `buildings.per`, `boarhunting.per`, `escrow.per`, and `tsa.per`. It participates in thresholds for economy, Loom timing, resource allocation, and town-size calculations.

This demonstrates that population accounting is upstream of multiple subsystems. AEGIS should therefore publish a coherent population snapshot rather than let every service independently infer population.

## 3. No dedicated villager-death event controller was proven

A broad search for death/dead/villager-count patterns produced many unrelated `DEATH` game-mode markers and accounting callsites, but no dedicated stock rule whose semantic role is:

```text
VILLAGER DIES
  -> identify dead villager
  -> decrement authoritative villager registry
  -> reassign its task
```

Therefore the current evidence supports recurrent accounting/census semantics, not an event-driven individual death ledger.

This does **not** mean stock cannot internally update counts immediately. It means the `.per` corpus does not expose sufficient evidence to claim that timing model.

## 4. AEGIS must distinguish current census from historical population

Because stock has both `villagercount` and `villagercounttotal`, AEGIS should not overload one goal as both current population and historical/derived population.

Minimum distinction:

```text
CURRENT_POPULATION
  current engine-observed villager population

ACCOUNTING_BASELINE / DERIVED_TOTAL
  persistent value used by policy calculations

PENDING_POPULATION
  villagers in production/queue state when applicable
```

Pending production is not completion, and completion is not necessarily equivalent to productive assignment.

## 5. Builder is an operational role/state

`buildings.per` uses `villager-builder` as a live condition. Examples:

```per
(unit-type-count villager <= 1)
(and (up-pending-objects c: house == 1)
     villager-builder)
```

and:

```per
villager-builder
(up-pending-objects c: house == 1)
(unit-type-count villager >= 3)
(can-build house)
```

These rules then construct a candidate worker search while excluding workers with `actionid-build`.

This proves that `villager-builder` is an operationally meaningful population and that builder assignment affects subsequent worker eligibility.

## 6. Builder replacement is partially supported but not universally proven

Stock can search for villagers while excluding those already performing `actionid-build`. This provides a mechanism for selecting non-builders when more builders are needed.

However, the corpus does not establish a single universal sequence:

```text
builder dies
 -> foundation identity preserved
 -> builder loss detected
 -> replacement builder selected
 -> build resumes
```

The existence of replacement-capable searches must not be misreported as proof of death-specific replacement.

## 7. Pending construction remains authoritative for incomplete infrastructure

`buildings.per` repeatedly uses `up-pending-objects` and `up-pending-placement`. One path explicitly searches pending buildings/towers and another deletes a damaged foundation before it is destroyed.

A construction service must therefore maintain at least:

```text
REQUESTED
PLACEMENT_PENDING
FOUNDATION_ACTIVE
BUILDING_ACTIVE
COMPLETED
FAILED
DELETED
```

with builder assignment represented separately.

## 8. Construction failure can be detected before terminal destruction

`buildings.per:484-495` searches pending building/tower objects, selects an object under attack, evaluates its hitpoints, and then issues:

```per
(up-target-point 0 action-delete -1 -1)
```

with a diagnostic explaining that the foundation is being deleted before it is destroyed.

This is direct evidence that stock intentionally converts an impending foundation loss into a controlled deletion/recovery path.

## 9. Logistics and builder continuity are separate dimensions

The evidence now supports:

```text
FOUNDATION STATE
      +
BUILDER POPULATION
      +
PLACEMENT STATE
      +
RESOURCE/ESCROW STATE
      ↓
CONSTRUCTION SERVICEABILITY
```

A foundation may remain valid while its builder population changes. Conversely, builders may exist while a foundation is invalid. These must not be represented as one Boolean `construction-valid` state.

## 10. Population accounting timing remains unresolved

The strongest safe timing statement is:

```text
stock repeatedly refreshes population-derived state
```

The exact latency from unit death/completion to the values consumed by `.per` rules remains unmeasured.

This is important for AEGIS verification. A generation-based state machine should tolerate stale population snapshots rather than assume every rule pass observes the same instant.

## 11. Revised AEGIS accounting contract

Population service should expose:

```text
population-generation
observed-at
current-villagers
current-civilian-population
current-military-population
pending-villagers
population-cap
housing-headroom
confidence/freshness
```

Builder service should expose separately:

```text
builder-candidate-count
builder-active-count
pending-foundation-count
active-foundation-count
builder-target relationship
builder-task-validity
construction-generation
```

## 12. Important architectural consequence

The civilian substrate should contain an authoritative **Population/Census Service** before worker assignment.

Proposed flow:

```text
ENGINE FACTS
   ↓
POPULATION / CENSUS
   ├─ villagers
   ├─ civilian pop
   ├─ military pop
   ├─ cap/headroom
   └─ freshness
   ↓
ECONOMIC ALLOCATION
   ↓
WORKER TASKING

CONSTRUCTION SERVICE
   ├─ pending object
   ├─ foundation
   ├─ builders
   ├─ placement
   └─ completion/failure
```

Worker death should therefore initially be represented as a **population delta plus task invalidation candidate**, not as an assumed event.

## 13. Confirmed vs unproven

### Confirmed

- `villagercount` is populated through `up-get-fact unit-type-count villager`.
- `villagercounttotal` is a distinct goal/state value.
- Population-derived values feed multiple subsystems.
- `villager-builder` is a live operational worker population.
- Builder selection excludes workers already on build action in inspected paths.
- Pending construction is independently searchable.
- Construction can be intentionally deleted before destructive foundation loss.
- Builder state and foundation state are separate concerns.

### Not proven

- Exact death-to-census latency.
- Dedicated event-driven villager-death accounting.
- Universal builder replacement after death.
- Universal builder replacement after interruption.
- One centralized stock population manager.

## Verdict

The civilian substrate now has sufficient evidence for a separate Population/Census Service and a separate Construction Service. The next highest-value target is **threat-driven worker interruption and recovery timing**, followed by source/task retasking latency. Only after those timing and interruption semantics are characterized should AEGIS freeze its substrate ABI.
