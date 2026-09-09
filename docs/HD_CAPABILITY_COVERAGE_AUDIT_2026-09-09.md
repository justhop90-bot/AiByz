# AEGIS / ByzBot — HD Capability Coverage Audit

**Date:** 2026-09-09  
**Status:** Open / authoritative closure ledger  
**Historical corpus:** verified stock `AI (HD version).per` + `Promisory/defaultConstants.per` + `Promisory/finalingConstants.per` + `Promisory/finaling.per`  
**Target runtime:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Purpose

This ledger answers one question rigorously:

> **Have we identified every meaningful capability the verified HD/Promisory AI teaches us that the final AEGIS bot needs to account for?**

The answer is **not declared closed yet**.

The ledger must be populated from direct source archaeology. A strategy label, unit list, or memory of AoE2 is not sufficient evidence.

## Method

For every historical subsystem, trace:

`GAME PROBLEM → OBSERVATION → STATE WRITE → STATE READER → GUARD → ACTION → POSTCONDITION → LIFECYCLE → RECOVERY → STRATEGIC INTERPRETATION`

Then map the capability to exactly one primary AEGIS vertical slice. Cross-cutting behavior may be referenced by additional slices, but ownership must remain singular.

## Evidence classes

- DIRECT
- COMPOSED
- INFERRED
- AEGIS-GENERALIZATION
- UNCERTAIN

Historical evidence never overrides current target-build machine authority.

## Coverage target

The current blueprint has 20 primary slices:

1. Foundation / Game-State Control Loop
2. Opening Economy / Age Advancement
3. Civilian Lifecycle
4. Resource Economy
5. Economic Logistics
6. Market / Resource Conversion / Trade
7. Construction & Infrastructure
8. Production Director
9. Cavalry Threat Containment
10. Infantry / Ranged Warfare
11. Siege Warfare
12. Monastic / Monk Operations
13. Scouting / Exploration / Map Knowledge
14. Information / Belief / Fog-of-War
15. Battlefield Force Composition
16. Battlefield Command
17. Garrison / Defense / Emergency Response
18. Naval / Water Operations
19. Technology / Research / Strategic Transitions
20. Strategic Director / Full Byzantine Integration

## Initial source-backed coverage matrix

| Historical capability/problem | Historical mechanism to inventory | Primary slice | Closure |
|---|---|---|---|
| Age advancement | escrow, research feasibility, age state, gatherer transition | 2 / 19 | OPEN |
| Villager continuity | villager production, housing, food allocation | 2 / 3 / 8 | OPEN |
| Housing continuity | housing goals, population/pending checks | 2 / 8 | OPEN |
| Contextual worker allocation | gatherer percentages and strategic conditions | 4 / 5 | OPEN |
| Resource commitment | escrow / reserved future spending | 4 / 19 | OPEN |
| Food-source transitions | hunting, farming, fishing, source availability | 2 / 5 | OPEN |
| Dropsite/logistics | camps, source access, placement | 5 / 7 | OPEN |
| Production authorization | train flags, feasibility, strategic activation | 8 | OPEN |
| Threat classification | enemy categories, military population, focus/target state | 9 / 10 / 11 / 14 | OPEN |
| Candidate search | scratch goals, counters, jumps, persistent search state | 7 / 13 / 16 | OPEN |
| Scout path analysis | safety, quartersteps, candidate points, waypoints | 13 | OPEN |
| Attack lifecycle | attack/status/retreat/restart state and timers | 16 | OPEN |
| Fortification response | enemy-fortifications state and attack suppression/defer | 11 / 16 | OPEN |
| Building recovery | alternate placement/rebuild fallback | 7 | OPEN |
| Pending/duplicate prevention | feasibility and pending checks | 8 / 19 | OPEN |
| Temporal hysteresis | timers, reset, re-entry | 1 / all | OPEN |
| Ally support | ally/enemy fact sums, assistance/tribute state | 20 | OPEN |
| Resource transfer | tribute/cooperation state | 6 / 20 | OPEN |
| Trade | trade subsystem and late-game transition | 6 / 20 | OPEN |
| Water theater | watercontrol, naval/fishing/transport behavior | 18 | OPEN |
| Terminal/resignation policy | terminal state and resignation subsystem | 20 | OPEN |
| Difficulty/execution scaling | execution-capability parameters | 20 | OPEN |

**Important:** this table is a starting index, not the completed audit. Each row requires direct source anchors before closure.

## Mandatory capability families still requiring explicit source audit

The following families must be searched directly through the verified HD/Promisory corpus rather than assumed from game knowledge:

- monks: production, healing, relic handling, conversion, positioning, survival, monastery technologies;
- unique-unit production and civilization-specific production paths;
- siege production and siege-specific tactical control;
- transport and amphibious logistics;
- fishing and water economy transitions;
- defensive garrison behavior;
- repairs and maintenance;
- wall/defensive construction behavior;
- economic infrastructure and dropsite replacement;
- target selection and target invalidation;
- retreat/re-engagement conditions;
- technology research beyond age transitions;
- market/trade behavior;
- ally cooperation and tribute;
- late-game/resignation behavior;
- taunt/operator-control interfaces;
- difficulty-dependent execution behavior;
- any civilization-specific Byzantine behavior in the historical source.

A family is not “covered” merely because a corresponding AEGIS slice exists. It is covered only after its source mechanisms have been traced.

## Closure criteria

A capability row is CLOSED only when:

1. exact historical source is identified;
2. executable mechanism is traced;
3. strategic interpretation is separated from source fact;
4. primary AEGIS owner is assigned;
5. current-build machine requirements are identified;
6. unresolved semantics are recorded;
7. no important behavior is lost during abstraction.

## Gap rule

If a capability cannot be mapped cleanly to the 20-slice blueprint, do not force it into a convenient category. Record:

`MISSING SLICE → CAPABILITY → SOURCE EVIDENCE → REASON CURRENT ARCHITECTURE FAILS`

The blueprint must then be revised before implementation proceeds.

## Relationship to implementation

This audit does not authorize `.per` code.

The machine gate remains:

`STOCK SNAPSHOT → IMPORT CLOSURE → ABI INVENTORY → COLLISION AUDIT → ABI FREEZE → IMPLEMENTATION`

The historical gate remains:

`SOURCE INVENTORY → CAPABILITY TRACE → SLICE MAPPING → GAP CLOSURE`

Both gates must be satisfied.
