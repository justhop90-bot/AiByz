# P0 Civilian Lifecycle Forensics

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Evidence source:** untouched local `resources\_common\ai\Promisory` corpus  
**Status:** Forensic extraction — implementation intentionally deferred

## Executive finding

The first civilian investigation confirms that the stock economy is not a four-percentage allocator and not a simple villager-production loop. It is a layered control system in which strategic conditions authorize production, economic policy mutates gatherer percentages, `dawn.per` converts those percentages into integer worker-role counts, and additional rules feed back from infrastructure, food sources, military posture, technology, escrow and map state.

This materially validates the decision to make the complete civilian lifecycle P0.

## 1. Villager production — `units.per`

The target file contains a large civilian-production decision tree. It begins with explicit initialization of `trainvillager` to `no`, then many conditional rules set `trainvillager` to `yes`.

Important observed gates include:

- pending villager objects;
- current villager count;
- civilian population;
- population and population headroom;
- current age;
- food stockpile and multiple derived food thresholds;
- Feudal/Castle/Imperial research state;
- strategy and strategy type;
- military state;
- barracks/blacksmith/range/stable/market state;
- stone-gathering state;
- fast-Imperial logic;
- fishing and water strategy;
- wood/food/gold excess thresholds;
- dropsite distance;
- civilization-specific branches;
- minimum/target civilian population;
- escrow-aware Castle Age conditions.

### Critical conclusion

`trainvillager` is a **production authorization state**, not itself the production action.

AEGIS should preserve this conceptual separation:

```text
civilian demand
 -> affordability/reservation
 -> production authorization
 -> TC production service
 -> pending state
 -> completed-villager evidence
```

The exact consumer of `trainvillager` still requires complete extraction beyond the first source region.

## 2. Economic policy — `gatherers.per`

The target file contains numerous strategy/age/state-specific mutations of:

- `sn-wood-gatherer-percentage`
- `sn-food-gatherer-percentage`
- `sn-gold-gatherer-percentage`
- `sn-stone-gatherer-percentage`

Examples observed include transitions based on:

- age;
- villager count;
- Feudal readiness;
- stable/range/blacksmith/market presence;
- gold stockpile relative to Castle Age requirements;
- escrow flags;
- farm count;
- civilian population;
- excess wood;
- strategy variants such as flush, ranged, scout and fast-Imperial branches.

### Critical conclusion

The stock percentages are **policy outputs**, not final worker assignments.

They are also not static. The same civilization can move through materially different percentage regimes as state changes.

Therefore AEGIS must not permanently encode `35/55/10/0` or any other fixed distribution as economic authority.

## 3. Integer worker accounting — `dawn.per`

The target `dawn.per` is 457 lines and provides a much clearer representation of the next stage of the pipeline.

It maintains explicit goals:

- `sum-villagers`
- `wood-villagers`
- `food-villagers`
- `gold-villagers`
- `stone-villagers`
- `villager-addition`

A representative terminal phase is:

```text
worker-role goals
 -> sum roles
 -> compare against villagercount
 -> add one worker at a time
 -> normalize
 -> write percentages back to strategic numbers
```

The file explicitly computes worker counts from strategic-number percentages using multiplication by `villagercount`, integer division by 100, and then reconciles the sum through iterative `villager-addition` rules.

It also contains special allocation behavior for:

- housing shortages;
- low wood;
- food minimums;
- Feudal transition;
- dark-war;
- fishing;
- drush/gold requirements;
- Fast Imperial;
- Castle War;
- gold requirements for Castle Age/Loom;
- farm state;
- hunt/forage/sheep/fisherman presence;
- mining-camp state;
- strategy-specific allocation.

### Critical architectural conclusion

The correct abstraction is:

```text
strategic/economic policy
        ↓
percentage targets
        ↓
integer worker-role targets
        ↓
role reconciliation
        ↓
resource/source tasking
```

This is substantially richer than a percentage allocator.

## 4. Housing is integrated into worker allocation

`dawn.per` does not treat housing as an unrelated construction problem. Early rules explicitly move a food worker to wood when housing headroom is low, provided there is no pending house and other affordability conditions are met.

This establishes a feedback path:

```text
population pressure
 -> housing deficit
 -> worker reallocation
 -> wood availability
 -> house construction
 -> restored capacity
```

AEGIS therefore needs construction demand to be visible to economic scheduling rather than having Construction and Economy operate as disconnected systems.

## 5. Food is a portfolio

`dawn.per` checks for shepherds, hunters, fishermen, foragers, forage count, sheep and farms. This is direct evidence that food workers are not conceptually one homogeneous source.

`boarhunting.per` is separately dedicated to hunting behavior.

Therefore the AEGIS food controller must distinguish at least:

```text
herdables
forage
boar
hunt/deer
farms
fishing
civ/map-specific sources
```

The allocation problem is therefore two-dimensional:

```text
How many workers should be food workers?
                    AND
Which food source should those workers exploit?
```

## 6. Dropsite distance is an economic variable

Both `units.per` and `gatherers.per` contain conditions involving dropsite distance. `dawn.per` also adjusts allocations in response to source/infrastructure conditions.

This confirms that resource quantity alone cannot be the final World Model economic input.

AEGIS must eventually represent opportunity in terms of:

```text
resource type
quantity
location
dropsite relationship
distance/accessibility
setup cost
expected income
risk
```

## 7. Infrastructure is part of the lifecycle

Worker allocation depends on infrastructure such as:

- mining camps;
- mills;
- lumber camps;
- town centers;
- military buildings;
- markets;
- blacksmiths.

A worker cannot be modeled as independently choosing a resource. The civilization must satisfy the infrastructure dependency chain first.

## 8. Escrow is upstream of civilian decisions

`units.per` explicitly contains `can-research-with-escrow castle-age`, while `gatherers.per` references `escrow-flag` in allocation decisions.

This is strong evidence for the earlier architectural distinction:

```text
strategic commitment
 !=
economic commitment
 !=
resource escrow
 !=
execution authorization
```

The P0 investigation must therefore include `escrow.per` before the civilian architecture is frozen.

## 9. New civilian control-loop model

The evidence currently supports this model:

```text
                    STRATEGIC / TECHNOLOGY STATE
                              |
                              v
                     CIVILIAN DEMAND MODEL
                              |
                              v
                     RESOURCE RESERVATIONS
                              |
                              v
                     GATHERER POLICY
                  (strategic percentages)
                              |
                              v
                   INTEGER ROLE ACCOUNTING
                              |
                 +------------+------------+
                 |                         |
                 v                         v
          SOURCE SELECTION          INFRASTRUCTURE
                 |                         |
                 +------------+------------+
                              v
                      CIVILIAN TASKING
                              |
                              v
                     PHYSICAL EXECUTION
                              |
                              v
                       OBSERVED RESULT
                              |
                              v
                     RECONCILIATION /
                         RECOVERY
```

## 10. What remains unproven

The following must not yet be treated as established:

1. exact consumer of `trainvillager`;
2. complete transition from role counts to individual villager task assignment;
3. complete idle-villager recovery path;
4. exact escrow reservation/release semantics;
5. exact source-selection algorithm for every resource type;
6. complete construction failure lifecycle;
7. exact event/timer ownership for every transition;
8. exact relationship between `dawn.per` role counts and specialized gatherer controllers;
9. all civ-specific deviations;
10. all water/trade interactions with civilian allocation.

## 11. P0 stock-to-AEGIS mapping

| Stock evidence | Behavior extracted | Proposed AEGIS owner | Status |
|---|---|---|---|
| `units.per` | conditional villager-production authorization | Civilian OS / Production Service | OBSERVED |
| `gatherers.per` | state-dependent resource policy | Economic Scheduler | OBSERVED |
| `dawn.per` | integer worker-role reconciliation | Civilian State / Allocation Service | OBSERVED |
| `dawn.per` | housing-driven wood reallocation | Economy + Construction contract | OBSERVED |
| `dawn.per` | food-source awareness | Food Controller | OBSERVED |
| `units.per` / `gatherers.per` | dropsite-distance dependencies | Spatial Economy | OBSERVED |
| `escrow` references | reservation-aware decisions | Escrow Service | OBSERVED interaction; semantics pending |
| `boarhunting.per` | specialized food lifecycle | Food Controller | OBSERVED subsystem existence |

## 12. Immediate next forensic passes

Before implementation:

1. Trace every `trainvillager` write and identify its consumer/action path.
2. Trace every `wood-villagers`, `food-villagers`, `gold-villagers`, `stone-villagers` write and identify downstream consumers.
3. Extract the exact worker-tasking subsystem after `dawn.per`.
4. Map idle-villager detection and recovery.
5. Extract `escrow.per` reservation/release semantics.
6. Extract construction dependencies from `buildings.per`.
7. Reconcile specialized food systems with generic worker allocation.
8. Produce the first complete civilian lifecycle ledger.
9. Run the six-reviewer gate.
10. Only then design the AEGIS civilian vertical slice.

## 13. Current P0 verdict

**P0 remains open.**

However, the first forensic pass has already invalidated the simplistic model of the economy and strengthened the hierarchical substrate architecture.

The correct implementation target is not:

```text
set percentages -> villagers gather
```

It is:

```text
strategic demand
 -> reservation
 -> policy
 -> integer allocation
 -> infrastructure/source selection
 -> tasking
 -> execution
 -> measurement
 -> reconciliation
 -> recovery
```

That distinction is now a canonical AEGIS architectural requirement.
