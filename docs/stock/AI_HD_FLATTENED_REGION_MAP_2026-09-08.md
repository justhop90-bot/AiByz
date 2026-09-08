# Flattened `AI (HD version).per` Region Map — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Source:** restored target-build `AI (HD version).per` on Weebo

This map converts the flattened stock file into explicit behavioral regions. It is a source-organization map, not a claim that each region is an independently loaded module.

## Exact major boundaries

| Start | End | Region | Reconstruction significance |
|---:|---:|---|---|
| 1 | 6,267 | Initialization / bootstrap / early operating setup | Initial state, constants, load-if structure, baseline doctrine and startup configuration. |
| 6,268 | 6,584 | Navy initialisation | Initial naval configuration and map/water setup. |
| 6,585 | 7,521 | Superiority code | Strategic military superiority/state evaluation. |
| 7,522 | 15,900 | Strategy selection + civ-dependent strategy | Strategic intent selection, map/game-mode branches, civ policy and strategy transitions. |
| 15,901 | 16,001 | Boar hunting | Dedicated early food acquisition lifecycle. |
| 16,002 | 19,623 | Resource management and age up | Economy control, age transition, resource policy, trade/resource interactions. |
| 19,624 | 21,050 | Basics | General baseline operating rules. |
| 21,051 | 22,561 | Research | Research policy and prerequisite/affordability logic. |
| 22,562 | 23,777 | Siege units | Siege production and military capability selection. |
| 23,778 | 26,207 | Buildings | Construction/building demand and building-state rules. |
| 26,208 | 29,128 | Units | Unit production, composition and unit-control rules. |
| 29,129 | 29,580 | Other researches | Additional research policies and conditional technology handling. |
| 29,581 | 29,681 | Farms / fishing ships | Food infrastructure and water-food production. |
| 29,682 | 32,470 | Gatherer percentages | Economic allocation and worker-role policy. |
| 32,471 | 34,586 | Attack & retreat rules | Military action lifecycle, attack posture, retreat and restart behavior. |
| 34,587 | 34,645 | Optional cheats | Optional/nonstandard behavior; not core strategic authority. |
| 34,646 | 34,805 | Human cooperation | Cooperation, ally interaction and communication. |
| 34,806 | 35,? | Increase TS code | Town-size/infrastructure growth control. |

**File length:** 36,141 lines.

The final exact end of the `INCREASE TS CODE` region and the remaining miscellaneous tail are still to be bounded from the source rather than inferred from the rounded section heading. The earlier 36,141-line total remains authoritative.

## Important interpretation

The flattened file contains both general engine-facing operating rules and large blocks of conditional compilation. In particular, `#load-if-defined`, `#load-if-not-defined`, and civ/map/game-mode guards make simple textual section boundaries insufficient to reconstruct the effective program.

The next static pass must therefore add a second dimension:

```text
physical line region
        ×
load-if / conditional activation predicate
        ×
state channel
        ×
side effect
        ×
consumer/producer relationship
```

That is the correct route from a flattened source file to a control-topology reconstruction.

## Deconstruction priority

Highest-value regions for the next cross-system join:

1. Strategy selection / civ-dependent strategy
2. Resource management and age up
3. Buildings
4. Units
5. Gatherer percentages
6. Attack & retreat
7. Research
8. Boar hunting
9. Scouting / superiority / naval control
10. Cooperation and late-game support

The priority is based on cross-system coupling, not line count alone.
