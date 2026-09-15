# Stock `farm-goal` Exact Producer/Consumer Graph — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`  
**Corpus:** restored target-build `AI (HD version).per` + Promisory source corpus  
**Status:** STATIC DECONSTRUCTION — NOT runtime qualified

## Executive result

`farm-goal` is not simply a Boolean "build farms" switch. The static source shows it functioning as an infrastructure-demand/control channel sitting between economic pressure, farm/building policy, placement, and downstream worker/economic capacity.

The source census identifies **99 behavioral rule sites** across **4 behaviorally relevant source files**.

| Source | Behavioral sites |
|---|---:|
| `AI (HD version).per` | 63 |
| `buildings.per` | 28 |
| `init.per` | 6 |
| `researches.per` | 2 |

The channel has a strongly mutation-oriented surface: approximately **92 writer operations** versus **23 read operations** in the prior behavioral census. The counts are operation-site counts, not unique semantic transitions.

## Static control topology

```text
                    ECONOMIC STATE
                         │
              food / villager pressure
                         │
                         ▼
                    farm-goal
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
       building policy         strategic policy
             │                       │
             └───────────┬───────────┘
                         ▼
                  build eligibility
                         │
                         ▼
                     placement
                         │
                         ▼
                 builder assignment
                         │
                         ▼
                  pending foundation
                         │
                         ▼
                  completed farm
                         │
                         ▼
                 economic capacity
                         │
                         └──────────────► next demand state
```

This is a static reconstruction of source relationships. It is not a claim that every edge executes synchronously or within one interpreter pass.

## Producer surface

The dominant producer surface is the flattened controller. This is significant because it means farm demand is largely established by the main strategic/economic controller rather than being owned exclusively by `buildings.per`.

`buildings.per` then acts as the physical infrastructure service consuming the demand and translating it into construction state.

`init.per` supplies initialization/spatial-economic parameters that influence the surrounding farm system.

`researches.per` contributes a small number of policy interactions, demonstrating that farm demand can be affected by technology state without making research the owner of the channel.

## Consumer surface

The major consumer is `buildings.per`, where farm demand participates in construction/building decisions. The flattened controller also consumes the channel, creating feedback between strategic/economic policy and infrastructure state.

The important architectural pattern is therefore:

```text
policy producer
    ↓
farm-goal
    ↓
construction service
    ↓
physical farm state
    ↓
economic feedback
```

## Ownership conclusion

The historical source does **not** justify assigning `farm-goal` to the construction subsystem alone.

The safer AEGIS interpretation is an interface between:

- economic demand generation;
- infrastructure demand arbitration;
- construction execution;
- economic state reconciliation.

Therefore the final AEGIS representation should separate:

```text
FoodDemand
FarmInfrastructureDemand
ConstructionRequest
FarmExecutionState
```

rather than using one integer channel for all four concepts.

## Lifecycle reconstruction target

The source strongly motivates the following AEGIS lifecycle, subject to later qualification:

```text
DEMAND_GENERATED
    ↓
DEMAND_ADMITTED
    ↓
CONSTRUCTION_REQUESTED
    ↓
PLACEMENT_SELECTED
    ↓
BUILD_AUTHORIZED
    ↓
BUILD_COMMAND_ISSUED
    ↓
PENDING_OBSERVED
    ↓
FARM_CONFIRMED
    ↓
CAPACITY_RECONCILED
```

Failure branches must eventually be represented explicitly:

```text
PLACEMENT_FAILED
BUILDER_UNAVAILABLE
FOUNDATION_INVALID
THREAT_BLOCKED
STALE_DEMAND
COMMAND_NOT_OBSERVED
```

These are architecture targets, not claims about named stock states.

## Critical boundary

Static source demonstrates the coupling. It does not establish:

- exact farm-goal mutation timing;
- whether a write is visible to a later rule in the same pass;
- placement persistence across passes;
- exact relationship between farm-goal and strategic-number farm percentages;
- exact confirmation latency;
- whether all historical branches remain active in the target runtime.

Those questions remain **TARGET-BUILD UNKNOWN / FUTURE RUNTIME QUALIFICATION**.

## Architectural significance

This is the first clean economic-to-construction feedback loop in the reconstructed graph:

```text
Economic pressure
      ↓
 farm infrastructure demand
      ↓
 Construction OS
      ↓
 physical infrastructure
      ↓
 Economic capacity
      ↓
 revised demand
```

That loop should become an explicit AEGIS service contract rather than a shared scratch goal.

## Next static join

The next high-value extraction is `control-goal`. Unlike `farm-goal`, it is a coordination channel crossing initialization, interaction, and the flattened controller. Its analysis should determine whether it represents a genuine control-plane state machine or multiple historical mechanisms sharing one namespace.

No runtime qualification is implied by this document.
