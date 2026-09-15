# Full Stock Goal Rule Coverage Summary — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Corpus:** flattened `AI (HD version).per` + all Promisory `.per` modules
**Method:** rule-block extraction against the 87-goal target vocabulary from the A1 typed-state census.

## Result

All **87/87** census goals are represented in behavioral rule blocks somewhere in the combined source corpus.

The extraction produced **6,509 goal × rule-site records**. Constant/declaration-only occurrences were excluded from the behavioral matrix.

The raw machine-readable matrix is generated locally as:

`docs/stock/STOCK_FULL_GOAL_RULE_COVERAGE_2026-09-08.csv`

## Highest-coupling channels

| Goal | Sources | Rule sites | Read sites | Write sites |
|---|---:|---:|---:|---:|
| `unit-goal` | 1 | 925 | 623 | 429 |
| `strategy-goal` | 1 | 708 | 498 | 326 |
| `control-goal` | 3 | 478 | 259 | 335 |
| `custom-civ-pop` | 14 | 438 | 435 | 3 |
| `temporary-goal2` | 19 | 421 | 169 | 279 |
| `position-goal` | 11 | 365 | 363 | 8 |
| `increase-ts` | 7 | 292 | 188 | 239 |
| `ranged-unit-type-goal` | 1 | 272 | 63 | 225 |
| `temporary-goal7` | 13 | 209 | 60 | 165 |
| `strategy-type` | 13 | 203 | 201 | 11 |
| `increase-town-size-goal` | 1 | 193 | 166 | 169 |
| `enemy-goal` | 8 | 163 | 150 | 33 |
| `total-food-amount` | 12 | 168 | 167 | 1 |
| `farm-goal` | 4 | 97 | 23 | 91 |
| `relic-count` | 10 | 59 | 59 | 2 |
| `retargetenemy` | 9 | 71 | 32 | 50 |
| `landnomad` | 9 | 55 | 50 | 7 |
| `victory-time` | 8 | 42 | 42 | 0 |
| `assistance` | 7 | 53 | 46 | 7 |
| `reset` | 5 | 23 | 8 | 22 |

## Critical architectural finding

The previously obvious `unit-goal` and `strategy-goal` channels are **not broadly shared across the Promisory module corpus**. They are concentrated in the flattened `AI (HD version).per` representation, while channels such as `control-goal`, `position-goal`, `custom-civ-pop`, and scratch goals cross multiple Promisory services.

This means the stock source has two distinct kinds of coupling:

1. **flattened-controller coupling** — large rule populations centralized in `AI (HD version).per`;
2. **distributed Promisory coupling** — shared state reused by multiple specialized source modules.

AEGIS must account for both. A direct one-to-one module translation would miss this distinction.

## Important scratch-state confirmation

`temporary-goal2` appears across **19 sources** and `temporary-goal7` across **13 sources**. These channels therefore cannot be treated as stable semantic state merely because they have large write counts.

The same scratch register is reused for unrelated calculations in construction, scouting, economy, military, research and shared-object services.

## Critical persistent channels

The following high-impact semantic channels require dedicated ownership analysis:

- `unit-goal`
- `strategy-goal`
- `control-goal`
- `position-goal`
- `attack-goal`
- `ranged-unit-type-goal`
- `increase-town-size-goal`
- `housing-goal`
- `farm-goal`
- `enemy-goal`
- `under-attack-goal`
- `retreat-now-goal`
- `restart-attack-goal`
- `anti-cavalry-threat-goal`
- `forward-threat-goal`
- `monk-threat-goal`
- `enemy-fortifications-goal`
- `escrow-purpose-goal`

## Caveat

The extraction identifies lexical state use inside rule blocks. It does not prove interpreter ordering, same-pass mutation visibility, runtime ownership, or effective activation under every load-if environment.

Those remain separate runtime/ABI questions.

## Next static join

For each persistent channel, join exact rule sites to:

```text
activation predicate
→ read/write operation
→ state producer/consumer
→ engine action
→ reset/supersession
→ downstream module
```

That produces the actual stock control graph required before AEGIS ownership can be frozen.
