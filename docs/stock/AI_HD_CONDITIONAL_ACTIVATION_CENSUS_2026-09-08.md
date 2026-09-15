# `AI (HD version).per` Conditional Activation Census — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Source:** restored target-build `AI (HD version).per` on Weebo

This is a lexical census of conditional-compilation directives. It is deliberately not a claim about which branches are active in a particular game. Activation depends on the engine-defined symbol environment and load-if processing.

## Global count

A direct source scan found **1,102 `#load-if*` directives** in the 36,141-line flattened AI file.

This is a major reason the file cannot be reconstructed correctly by treating its physical regions as independent always-active modules.

## Highest-frequency activation symbols

| Symbol | Directive occurrences | Category |
|---|---:|---|
| `DIFFICULTY-EASIEST` | 38 | Difficulty |
| `DIFFICULTY-EASY` | 38 | Difficulty |
| `DEATH-MATCH` | 35 | Game mode |
| `DIFFICULTY-MODERATE` | 34 | Difficulty |
| `UP-POCKET-POSITION` | 32 | Map/position |
| `POST-IMPERIAL-AGE-START` | 31 | Starting-age configuration |
| `AZTEC-CIV` | 29 | Civilization |
| `LOW-RESOURCES-START` | 28 | Starting resources |
| `MAYAN-CIV` | 27 | Civilization |
| `SARACEN-CIV` | 27 | Civilization |
| `DIFFICULTY-HARD` | 25 | Difficulty |
| `BYZANTINE-CIV` | 23 | Civilization |
| `BRITON-CIV` | 23 | Civilization |
| `VIKING-CIV` | 23 | Civilization |
| `DIFFICULTY-EXTREME` | 23 | Difficulty |
| `TURKISH-CIV` | 22 | Civilization |
| `WONDER-RACE` | 22 | Game mode |
| `DIFFICULTY-HARDEST` | 22 | Difficulty |
| `KOREAN-CIV` | 21 | Civilization |
| `GOTHIC-CIV` | 20 | Civilization |
| `HUN-CIV` | 20 | Civilization |
| `CHINESE-CIV` | 19 | Civilization |
| `CELTIC-CIV` | 18 | Civilization |
| `INCAN-CIV` | 17 | Civilization |
| `INDIAN-CIV` | 16 | Civilization |
| `ITALIAN-CIV` | 16 | Civilization |
| `MONGOL-CIV` | 16 | Civilization |
| `SLAVIC-CIV` | 16 | Civilization |
| `FEUDAL-AGE-END` | 14 | Age boundary |
| `POPULATION-CAP-25` | 13 | Population configuration |
| `BERBERS-CIV` | 12 | Civilization |
| `FRANKISH-CIV` | 12 | Civilization |
| `TEUTONIC-CIV` | 12 | Civilization |
| `MAGYAR-CIV` | 11 | Civilization |
| `PERSIAN-CIV` | 11 | Civilization |
| `SPANISH-CIV` | 11 | Civilization |
| `DEFEND-WONDER` | 11 | Game mode/objective |
| `SUDDEN-DEATH` | 11 | Game mode |
| `DARK-AGE-END` | 11 | Age boundary |

Additional symbols include Malian, Portuguese, Ethiopian, Japanese, Khmer, Vietnamese, Burmese, Malay, Bohemian, Wei/Wu/Shu, map-specific, age-start, victory and newer-civilization symbols.

## Engineering significance

The activation surface is dominated by four dimensions:

1. **difficulty** — changes operating parameters and behavior;
2. **civilization** — selects civilization-specific strategy/policy;
3. **game mode/start condition** — changes initial assumptions and late-game behavior;
4. **map/topology** — changes naval, position, resource and terrain behavior.

These predicates cut across the behavioral regions in `AI_HD_FLATTENED_REGION_MAP_2026-09-08.md`.

Therefore the correct stock reconstruction unit is not simply:

`line range → subsystem`

but:

```text
line range
× activation predicate stack
× state channels touched
× side effects
× consumers
```

## Byzantine-specific observation

`BYZANTINE-CIV` occurs **23 times** in the flattened source. This is not enough to characterize Byzantine policy by itself. The next pass should extract each Byzantine-conditioned rule, its surrounding predicates, every state channel it reads/writes, and the downstream subsystem it influences.

That will produce a **Byzantine policy graph** rather than a loose list of Byzantine bonuses or rules.

## Important boundary

`#load-if*` is parser/load-time machinery. A conditional branch being present in the source does not prove that it is active in the current normal-HD runtime, and an inactive branch is still valuable historical source evidence.

No runtime experiment is required for this census.
