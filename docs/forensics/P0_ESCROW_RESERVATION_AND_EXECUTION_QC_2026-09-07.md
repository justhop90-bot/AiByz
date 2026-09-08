# P0 Escrow Reservation and Execution QC — 2026-09-07

## Scope

Forensic inspection of the untouched stock AoE2DE Promisory corpus, concentrating on `escrow.per` and its interaction with research, construction, and unit production. The purpose is to establish the real economic reservation/execution substrate before implementing an AEGIS economic commitment layer.

Authoritative source:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\Promisory`

Inspected files:
- `escrow.per`
- `units.per`
- `researches.per`
- `buildings.per`

## Executive finding

Stock escrow is an execution-reservation mechanism built around a two-phase pattern:

```text
STRATEGIC / SUBSYSTEM DEMAND
        ↓
COST ACCUMULATION
        ↓
ESCROW FLAG / REQUEST STATE
        ↓
ESCROW COST STATE
        ↓
ESCROW-AWARE AFFORDABILITY TEST
        ↓
PHYSICAL COMMAND
        ↓
ESCROW RELEASE / RESET
```

Escrow is therefore not equivalent to strategic commitment. It is also not merely an accounting variable maintained by the AI. Stock exposes engine-facing escrow operations and escrow-aware `can-*` predicates.

## 1. Reset/release is explicit

`escrow.per` begins with a release rule that performs all of the following:

```per
(up-release-escrow)
(set-escrow-percentage wood 0)
(set-escrow-percentage food 0)
(set-escrow-percentage gold 0)
(set-escrow-percentage stone 0)
(up-modify-escrow wood c:= 0)
(up-modify-escrow food c:= 0)
(up-modify-escrow gold c:= 0)
(up-modify-escrow stone c:= 0)
(up-reset-cost-data cost-food)
```

This is direct evidence that escrow has a lifecycle and that resource reservation state can be deliberately cleared before the next economic decision cycle.

## 2. Demand is represented as typed cost accumulation

Research requests repeatedly use:

```per
(up-add-research-cost c: <research> c: 1)
(up-modify-flag escrow-flag c:+ <bit>)
```

Construction requests use:

```per
(up-add-object-cost c: <object> c: 1)
(up-modify-flag escrow-flag2 c:+ <bit>)
```

Unit-production requests use the same general pattern, with later `can-train-with-escrow` checks and train commands.

Therefore stock has an intermediate **requested-cost layer** between strategic conditions and physical execution.

## 3. Flags are request selectors, not resource amounts

Examples include:

- `escrow-flag == 1` → Castle Age
- `escrow-flag == 2` → Imperial Age
- `escrow-flag == 16384` → Cavalier
- `escrow-flag == 32768` → Paladin
- `escrow-flag2 == 1048576` → Market construction
- `escrow-flag2 == 2097153` → Siege Workshop construction
- `escrow-flag2 == 524288` → Town Center construction
- `escrow-flag3 == 8` → Trebuchet production

These flags identify the requested execution target. They do not themselves constitute the economic reservation quantity.

## 4. Escrow cost state is separately materialized

Near the end of `escrow.per`, stock executes:

```per
(up-modify-escrow wood g:= cost-wood)
(up-modify-escrow food g:= cost-food)
(up-modify-escrow gold g:= cost-gold)
(up-modify-escrow stone g:= cost-stone)
```

This is a critical architectural boundary.

The stock controller first accumulates/derives costs, then materializes those costs into escrow state. Consequently:

```text
REQUESTED COST ≠ ESCROWED COST ≠ SPENT RESOURCE
```

The exact internal timing of engine deduction versus AI-visible escrow mutation is not proven by `.per` source alone and must not be guessed.

## 5. Affordability is escrow-aware

Execution rules use predicates such as:

```per
(can-research-with-escrow <research>)
(can-build-with-escrow <object>)
(can-train-with-escrow <unit>)
```

Examples include Castle Age, Imperial Age, unique technologies, Town Centers, markets, siege workshops, castles, mangonels, monks, and numerous military upgrades.

This proves that stock's physical execution gate is explicitly coupled to escrow state.

## 6. Research execution lifecycle

The recurring stock pattern is:

```text
conditions satisfied
    ↓
up-add-research-cost
    ↓
set escrow request bit
    ↓
materialize escrow cost
    ↓
can-research-with-escrow
    ↓
research
```

For example, Castle Age is requested only after food/gold/population and strategic conditions are satisfied. The later execution rule tests the corresponding escrow flag and calls `can-research-with-escrow castle-age` before `research castle-age`.

The important distinction is that **the strategic rule requests the research; the escrow execution rule authorizes the physical action.**

## 7. Construction follows the same pattern

Town Center construction provides strong evidence.

Stock can accumulate an object cost:

```per
(up-add-object-cost c: town-center-foundation c: 1)
(up-modify-flag escrow-flag2 c:+ 524288)
```

The execution side then tests:

```per
(can-build-with-escrow town-center)
```

and eventually invokes placement/build machinery.

Construction therefore has at least these separable states:

```text
CONSTRUCTION DEMAND
→ COST REQUEST
→ ESCROW AUTHORIZATION
→ PLACEMENT
→ FOUNDATION
→ COMPLETION / FAILURE
```

This aligns with earlier construction forensics showing that pending foundations are independently searchable and recoverable.

## 8. Production has the same separation

`units.per` establishes production intent through persistent goals such as:

```per
(set-goal trainvillager yes)
(set-goal trainknight yes)
(set-goal trainram yes)
```

But production intent is not the physical command.

Earlier verified stock execution uses:

```per
(up-can-train escrow-state c: villager)
```

followed by:

```per
(up-train escrow-state c: villager)
```

Therefore:

```text
TRAIN GOAL
≠
ECONOMIC AUTHORIZATION
≠
QUEUE COMMAND
```

This is one of the strongest reasons AEGIS must preserve separate policy, reservation, authorization, and execution layers.

## 9. Stock uses explicit rejection/short-circuit logic

`escrow.per` contains many `up-jump-rule` gates before adding costs. Typical reasons for rejecting an expenditure include:

- insufficient food
- insufficient gold
- insufficient wood
- insufficient stone
- too few villagers
- insufficient military population
- under attack
- missing infrastructure
- unavailable research
- missing resource sources
- unsuitable strategic state
- pending construction
- competing strategic requirements

Thus the economic scheduler is not a simple FIFO queue. Candidate expenditures are conditionally admitted into the escrow request system.

## 10. Rule order is part of arbitration

The stock file uses numbered `up-jump-rule` control extensively. A condition can route execution past later request branches.

Therefore priority is partly encoded structurally in rule flow.

This means an exact universal numeric priority ordering such as:

```text
food > military > age-up > construction > research
```

is **not supported** by the corpus.

The correct conclusion is:

> Stock performs distributed, context-sensitive arbitration whose effective priority emerges from conditional gates, jump routing, request flags, and later escrow-aware execution.

## 11. Resource commitment is not equivalent to worker allocation

Earlier forensic passes established that gatherer allocation independently derives desired worker counts and source assignments.

This pass demonstrates that expenditure authorization is another independent plane.

The resulting architecture is:

```text
STRATEGIC DEMAND
      ↓
ECONOMIC DEMAND
      ↓
WORKER TARGET VECTOR ─────→ RESOURCE ACQUISITION
      │
      ↓
EXPENDITURE REQUEST
      ↓
COST MODEL
      ↓
ESCROW
      ↓
AFFORDABILITY
      ↓
EXECUTION AUTHORIZATION
      ↓
PHYSICAL ACTION
```

Workers produce resources; escrow protects/authorizes resources for expenditures. These mechanisms interact but must not be collapsed.

## 12. Important distinction: escrow versus reservation

The evidence supports treating escrow as an engine-facing **resource reservation/authorization mechanism**.

However, source alone does not prove every semantic detail of the underlying engine implementation—for example, the precise moment an escrowed amount becomes unavailable to another transaction or the exact ordering of engine-side deductions.

AEGIS should therefore expose an abstract reservation contract while retaining an explicit implementation adapter for the native escrow ABI.

## 13. Recommended AEGIS economic commitment model

```text
ECON_DEMAND
    generation
    resource vector
    priority
    urgency
    reason
    expiration
        ↓
ECON_RESERVATION
    reservation-id
    generation
    resource vector
    owner
    state
    validity
        ↓
EXECUTION_AUTHORIZATION
    reservation-id
    action-id
    target
    affordability evidence
    authorization state
        ↓
EXECUTION
    command-issued
    engine-observed
    confirmed
    failed
        ↓
RELEASE / RECOVERY
```

Recommended states:

```text
REQUESTED
RESERVING
RESERVED
AUTHORIZED
ISSUED
CONFIRMED
FAILED
RELEASED
EXPIRED
```

## 14. Do not collapse these four concepts

AEGIS must retain the following distinctions:

```text
STRATEGIC COMMITMENT
“We intend to pursue cavalry pressure.”

ECONOMIC DEMAND
“We require 350 additional gold for that plan.”

RESOURCE RESERVATION / ESCROW
“That gold is protected from competing expenditures.”

EXECUTION AUTHORIZATION
“This specific Cavalier action may now be issued.”
```

These are different state transitions and should have different identifiers and failure modes.

## 15. Failure taxonomy

A reservation/execution request can fail for materially different reasons:

```text
DEMAND_REJECTED
INSUFFICIENT_RESOURCE
RESOURCE_RESERVED_BY_OTHER_REQUEST
INFRASTRUCTURE_MISSING
INFRASTRUCTURE_PENDING
TARGET_UNAVAILABLE
AFFORDABILITY_FAILED
THREAT_BLOCK
STRATEGY_INVALIDATED
COMMAND_FAILED
POST_COMMAND_STATE_INVALID
```

`AFFORDABILITY_FAILED` must not automatically mean `DEMAND_INVALIDATED`. A request may remain strategically valid while waiting for resources.

## 16. Interaction with worker allocation

A resource request such as:

```text
MIL_REQUEST: knight × 3
```

should generate economic demand:

```text
food += required food
 gold += required gold
```

The economic allocator can then increase worker demand for food/gold. That allocation changes future resource production, which changes reservation readiness.

Thus the closed loop is:

```text
MILITARY PLAN
    ↓
ECONOMIC DEMAND
    ↓
WORKER ALLOCATION
    ↓
RESOURCE PRODUCTION
    ↓
ESCROW / RESERVATION
    ↓
AFFORDABILITY
    ↓
UNIT PRODUCTION
    ↓
VERIFICATION
    ↓
NEW MILITARY STATE
```

This is the correct substrate model for AEGIS.

## 17. Negative findings

Not proven from `.per` alone:

- exact engine-side escrow ledger implementation
- exact timing between escrow mutation and resource deduction
- universal global priority ranking among all expenditures
- a centralized stock economic scheduler object
- atomic multi-resource transaction semantics
- exact starvation-prevention guarantees
- exact rollback semantics for every failed command

These remain runtime/engine-ABI questions.

## 18. Engineering implications

AEGIS should not copy the stock `escrow-flag` bitfield architecture literally.

Instead, use typed requests with explicit ownership and lifecycle state, while adapting to native escrow for physical execution.

Recommended service boundary:

```text
Economic Commitment Service
        ↓
Reservation Manager
        ↓
Native Escrow Adapter
        ↓
Affordability Gate
        ↓
Execution Authorization
        ↓
Execution Service
        ↓
Verification / Recovery
```

The native engine remains authoritative for actual affordability and physical spending.

## 19. Qualification

Static forensic confidence: **HIGH** for the existence and structural role of escrow-aware request/cost/execution pathways.

Runtime semantic confidence: **NOT ESTABLISHED** for exact engine-side reservation timing and transaction semantics.

No live AEGIS runtime files were modified during this investigation.

## 20. Bottom line

The stock civilization substrate is now best understood as two coupled control loops:

```text
RESOURCE ACQUISITION LOOP
Demand → worker targets → source selection → tasking → production → recovery

EXPENDITURE LOOP
Demand → cost request → escrow → affordability → execution → verification → release
```

AEGIS should connect these loops through explicit economic demand, but must preserve their separate state machines.
