# HD AI Forensic Quantitative Profile — 2026-09-02

Derived structural analysis of the recovered HD artifact. Proprietary stock source text is not copied into the public repository.

## Global profile
- `lines`: **36164**
- `defrules`: **2447**
- `defconst`: **4230**
- `load_calls`: **21**
- `goal_writes`: **2142**
- `sn_writes`: **1809**
- `timer_enables`: **239**
- `train_actions`: **253**
- `research_actions`: **614**
- `build_actions`: **117**
- `attack_actions`: **2**
- `max_line_length`: **145**

## Major source regions

| Region | Start | Rules | Span | Dominant behavior |
|---|---:|---:|---:|---|
| NAVY INITIALISATION | 6289 | 27 | 317 | map/water/navy bootstrap |
| SUPERIORITY CODE | 6606 | 86 | 937 | military/economic superiority state |
| STRATEGY SELECTION | 7543 | 655 | 8480 | strategic mode transitions |
| RESOURCE MANAGEMENT AND AGE UP | 16023 | 275 | 3621 | economy/age transition |
| BASICS | 19644 | 113 | 1428 | bootstrap/building/economy substrate |
| RESEARCH | 21072 | 131 | 1511 | technology policy |
| SIEGE UNITS | 22583 | 282 | 3646 | siege capability and support |
| UNITS | 26229 | 206 | 2921 | military capability production |
| OTHER RESEARCHES | 29150 | 43 | 553 | secondary technology policy |
| GATHERER PERCENTAGES | 29703 | 232 | 2789 | economic allocation control |
| ATTACK & RETREAT RULES | 32492 | 165 | 2175 | offensive/defensive feedback control |
| HUMAN COOPERATION | 34667 | 12 | 160 | human/team command interface |
| INCREASE TS CODE | 34827 | 114 | 1338 | late strategic-number/control extensions |

## Interpretation

The code's shape is itself evidence. It is a distributed controller with heavy state mutation and policy parameterization rather than a centralized planner.

### Key signals
1. Goal and strategic-number mutation is extensive relative to rule count.
2. The gatherer-allocation region contains a very large number of strategic-number writes, showing that economy is repeatedly reconfigured as strategic state changes.
3. Military logic is partitioned into superiority, siege, unit, and attack/retreat controllers that communicate through shared state.
4. Research is integrated with strategic state rather than being an isolated technology queue.
5. Timers are concentrated around behavior that can oscillate or requires delayed reconsideration.
6. Human-cooperation and command-oriented state constitute an explicit interface layer.

## Limitation

These metrics identify structure, not semantic ownership. The forthcoming writer-reader-transition graph must adjudicate authoritative versus advisory, scratch, legacy, and contested state. Regex counts are reconnaissance evidence, not semantic proof.
