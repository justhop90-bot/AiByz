# Persistent State Rule-Site Summary — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Corpus:** restored `AI (HD version).per` + all 36 Promisory `.per` modules
**Method:** lexical extraction from every `defrule` block; only the 18 high-value persistent state channels were retained.
**Result:** 1,808 rule-site records across 37 source files.

| Channel | Rule sites | Read sites | Write sites | Source files | Dominant source(s) |
|---|---:|---:|---:|---:|---|
| `unit-goal` | 928 | 624 | 431 | 1 | AI (HD version).per: 928 |
| `strategy-goal` | 710 | 499 | 327 | 1 | AI (HD version).per: 710 |
| `control-goal` | 480 | 259 | 336 | 3 | AI (HD version).per:469; init.per:8; interaction.per:3 |
| `position-goal` | 370 | 365 | 8 | 11 | AI:191; init:86; units:33; buildings:24; escrow:11 |
| `ranged-unit-type-goal` | 272 | 63 | 225 | 1 | AI (HD version).per: 272 |
| `enemy-goal` | 232 | 182 | 36 | 8 | AI:115; units:40; init:37; buildings:15; escrow:10; researches:10 |
| `increase-town-size-goal` | 194 | 167 | 170 | 1 | AI (HD version).per: 194 |
| `attack-goal` | 137 | 54 | 81 | 2 | AI:135; init:2 |
| `farm-goal` | 99 | 23 | 92 | 4 | buildings:58; AI:39; init:1; researches:1 |
| `anti-cavalry-threat-goal` | 53 | 51 | 2 | 1 | AI (HD version).per: 53 |
| `under-attack-goal` | 44 | 41 | 7 | 1 | AI (HD version).per: 44 |
| `escrow-purpose-goal` | 35 | 18 | 24 | 1 | AI (HD version).per: 35 |
| `monk-threat-goal` | 37 | 23 | 2 | 1 | AI (HD version).per: 37 |
| `enemy-fortifications-goal` | 17 | 16 | 2 | 1 | AI (HD version).per: 17 |
| `housing-goal` | 17 | 8 | 13 | 1 | AI (HD version).per: 17 |
| `retreat-now-goal` | 16 | 7 | 14 | 1 | AI (HD version).per: 16 |
| `forward-threat-goal` | 15 | 15 | 2 | 1 | AI (HD version).per: 15 |
| `restart-attack-goal` | 3 | 2 | 3 | 1 | AI (HD version).per: 3 |

## Architectural findings

### Controller-dominant channels

`unit-goal`, `strategy-goal`, `ranged-unit-type-goal`, and `increase-town-size-goal` are completely concentrated in the flattened controller. They should therefore be reconstructed by tracing the controller's internal state machine and its downstream engine effects, not by inventing a Promisory module boundary that does not exist in the source representation.

### Distributed channels

`control-goal`, `position-goal`, `enemy-goal`, and `farm-goal` cross multiple source modules. These are genuine cross-subsystem coupling channels and require ownership contracts rather than one-file translation.

### Read-heavy observation channels

`position-goal` (365 reads / 8 writes), `enemy-goal` (182 / 36), and `anti-cavalry-threat-goal` (51 / 2) are primarily observation/coordination channels in this lexical census. That does not prove semantic ownership, but it identifies where producer analysis should look for the relatively small mutation surface.

### Write-heavy command channels

`ranged-unit-type-goal` (225 writes / 63 reads), `farm-goal` (92 / 23), `attack-goal` (81 / 54), and `retreat-now-goal` (14 / 7) have substantial mutation surfaces. These are strong candidates for tracing policy-to-execution transitions.

## Rule-site extraction boundary

The machine-readable local extraction is:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\rule_site_extract_2026-09-08.csv`

The local CSV contains exact source-file names, rule ordinal, source line interval, goal set, read/write classification, selected strategic-number tokens, and selected engine-action tokens.

The extraction is deliberately lexical. It does **not** establish interpreter scheduling, same-pass visibility, effective activation for every game configuration, or command completion semantics.

## Next static operation

For each high-value channel, reconstruct the exact graph:

`activation predicate → rule site → state mutation → engine action → consumer → reset/supersession`

This is the final static join before AEGIS ownership contracts are frozen. Runtime qualification remains a later phase.
