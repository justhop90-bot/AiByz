# AoE2DE Strategic Problem → Historical Solution Matrix

**Date:** 2026-09-04  
**Purpose:** practical companion to the HD archaeology and `.per` coding knowledge base.

This matrix starts from the **game problem** rather than the code primitive. It is intended to prevent AEGIS from solving programming-shaped problems instead of AoE2-shaped problems.

| Game problem | What the AI needs to know | HD / Promisory solution | AEGIS lesson |
|---|---|---|---|
| Reach next Age | resources, prerequisites, timing, current commitments | escrow + research feasibility + age state + gatherer allocation | age-up is a capability transition |
| Maintain villager production | TC state, housing, food, production continuity | villager training + housing goals + food allocation | civilian production is core economic throughput |
| Avoid housed production | population, housing pending/completed, future demand | housing state and building checks | forecast production capacity, don't merely react to cap |
| Fund competing projects | stockpile + future commitments | resource-control / escrow | resources have opportunity cost |
| Choose worker allocation | strategic demand by resource | contextual gatherer percentages | economy is a control output |
| Protect economic infrastructure | resource access, dropsite need, safety | camps/dropsites/building rules | logistics affects effective gather rate |
| Secure early food | food requirement, source availability, timing | boar/hunting + food-source transitions | early food is a timing capability |
| Transition off food source | depletion/availability + wood/food demand | farms/fishing/hunting state | source transitions are strategic events |
| Identify enemy strategy | age, units, buildings, timing, military population | enemy-goal classifications | model commitments and likely transitions |
| Detect immediate threat | source, mechanism, target, timing | threat-source/target/classes + defensive branches | threat must be typed |
| Select military capability | enemy capability, map, tech, timing, resources | unit-goal + strategy coupling | choose capability, not a memorized counter |
| Build production capacity | desired capability + infrastructure prerequisites | building counts + pending + can-build | production is a pipeline |
| Research military/economic tech | future benefit + resource conflict + timing | escrow flags + can-research | technology is an investment |
| Decide whether to attack | capability, target, fortification, timing, position | attack-goal + military level + timers | attack is a lifecycle, not a boolean |
| Avoid bad engagement | local strength, fortifications, siege, position | retreat-goal/status + timers + reset | tactical interruption preserves strategy |
| Restart after regroup | attack objective + elapsed cooldown + force recovery | restart-attack-goal + timers | recovery is part of the plan |
| Attack defensive structures | fortification state + siege capability | enemy-fortifications-goal + siege checks | counter the defensive mechanism |
| Pick a target | target set, distance, HP, damage, range, objective | target evaluation + DUC/search | candidate evaluation must be contextual |
| Move safely | obstacles, enemy structures, local threat | scout path analysis + tactical waypoint logic | route quality is strategic value |
| Scout efficiently | information gaps + route safety + timing | scout groups + candidate points + waypoints | maximize decision value, not raw exploration |
| Handle water map | map class + docks + ships + transport + naval threat | watercontrol + map-dependent production | water is a separate theater |
| Protect/retreat naval forces | group position, HP, enemy strength | naval group/retreat/action states | naval control needs lifecycle state |
| Transport armies | capacity, route, escort, timing | transport flags + naval/tactical control | logistics is a commitment |
| Support allies | ally/enemy population and capability | ally/enemy fact sums + assistance/tribute | team strategy requires relational state |
| Give resources | donor stock + recipient need + self opportunity cost | tribute/cooperation state | transfer is a strategic conversion |
| Choose trade | map/economy/late-game conditions | trade subsystem | economy can change generation model |
| Recover from failed building placement | placement failure + alternate capability | backup/rebuild and alternate placement paths | failure is a branch, not a null result |
| Avoid duplicate asynchronous commands | pending state | can-build/can-research/pending checks | request != completion |
| Prevent rule oscillation | recent decision history | timers/self-disable/reset states | temporal hysteresis is necessary |
| Manage search under rule constraints | candidates + scores + termination | scratch goals + counters + jumps | search must be explicitly stateful |
| Maintain operator controls | external request + authority + lifetime | taunt interface / strategic state controls | external inputs require controlled authority |
| Scale behavior by difficulty | strategic knowledge vs execution skill | execution-capability parameters | strategy and mechanics are separable |
| End hopeless game | terminality + leniency + game state | resignation subsystem | terminal policy must be explicit |
| Survive engine patch | changed constants/semantics | custom constants + patch refill guidance | runtime compatibility is a first-class dependency |

## 1. Cross-cutting strategic questions

Every row should ultimately be connected to these variables:

`CAPABILITY | COST | TIMING | POSITION | INFORMATION | OPPONENT | COMMITMENT | OPTIONALITY | FAILURE | RECOVERY`

A decision that ignores one of these may still be valid, but the omission must be intentional.

## 2. The historical coding pattern behind the matrix

The HD/Promisory solution repeatedly decomposes a game problem into:

1. **Observe** — facts, counts, objects, map, time, age, pending state.
2. **Classify** — enemy, threat, position, strategy, capability.
3. **Persist** — goal, strategic number, timer, search state, escrow purpose.
4. **Gate** — feasibility, authority, age, resource, timer, pending operation.
5. **Act** — build, research, train, move, attack, retreat, tribute, scout.
6. **Verify** — observe resulting world state rather than assuming success.
7. **Recover** — fallback, reset, restart, reallocation, alternate candidate.

This pattern is more important than any individual `.per` idiom.

## 3. AEGIS candidate standard

For any strategic candidate `X`, the minimum evaluation record should be:

- capability gained;
- objective served;
- immediate resource cost;
- reserved/future resource cost;
- production/infrastructure cost;
- timing value;
- map/position effect;
- information requirement;
- opponent transition affected;
- optionality lost;
- expected failure modes;
- recovery path;
- confidence.

A future optimizer may turn this into a numerical score, but the semantic fields must exist before the score is trusted.

## 4. Conversion-tax interpretation

A strategic action is especially valuable when it forces the opponent to spend resources, time, production capacity, map control, or optionality beyond what the action cost us.

This is an AEGIS abstraction, not a historical term used by the HD source. The historical source provides supporting ingredients: reservation, threat classification, defensive response, timing windows, production coupling, and transition-aware opponent modeling.

## 5. Implementation priority

When building AEGIS, implement the following dependency order:

`OBSERVATION -> STATE/BELIEF -> CAPABILITY MODEL -> RESOURCE COMMITMENT -> PRODUCTION -> ACTION AUTHORITY -> TACTICAL EXECUTION -> VERIFICATION -> RECOVERY -> STRATEGIC REASSESSMENT`.

Do not start with tactical commands and attempt to bolt strategic reasoning on afterward.
