# Stock Scratch-Goal Finding — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Source:** restored target-build Promisory corpus + A1 typed-state census
**Status:** STATIC-QUALIFIED

## Finding

The historical stock controller uses `temporary-goal`, `temporary-goal2` through `temporary-goal6` as **reusable scratch registers**, not as stable semantic state channels.

A static extraction of 1,790 rule sites touching these names shows broad cross-module reuse:

| Scratch channel | Rule sites touching it | Writes observed |
|---|---:|---:|
| `temporary-goal` | 902 | 455 |
| `temporary-goal2` | 614 | 278 |
| `temporary-goal3` | 579 | 316 |
| `temporary-goal4` | 338 | 161 |
| `temporary-goal5` | 243 | 122 |
| `temporary-goal6` | 149 | 83 |

The largest contributing modules include `buildings.per`, `init.per`, `tsa.per`, `general.per`, `units.per`, `orb.per`, `gatherers.per`, and `threats.per`.

## Representative proof

`buildings.per` reuses the same scratch channels for materially unrelated computations, including placement calculations, object distances, counts, town-size calculations, and construction state.

`boarhunting.per` likewise reuses `temporary-goal` through `temporary-goal4` for boar counts, hunter counts, distance calculations, lurer selection, and search bookkeeping.

A single rule can write several scratch channels simultaneously and another rule can reinterpret those channels for a different computation later in the control flow.

## Architectural consequence

These stock names **must not be promoted directly into the AEGIS semantic ABI**.

AEGIS should use typed state contracts such as:

```text
WorldModel.*
Economy.*
Construction.*
Production.*
Research.*
Military.*
Threat.*
Information.*
Verification.*
Recovery.*
```

If scratch storage is required, it must be explicitly scoped to a service/rule transaction and must not masquerade as persistent strategic state.

## Stable-state distinction

The A1 goal census separately identifies persistent semantic channels including:

- `strategy-goal`
- `unit-goal`
- `control-goal`
- `position-goal`
- `attack-goal`
- `ranged-unit-type-goal`
- `increase-town-size-goal`
- `housing-goal`
- `farm-goal`
- `under-attack-goal`
- `retreat-now-goal`
- `restart-attack-goal`
- `enemy-goal`
- `anti-cavalry-threat-goal`
- `forward-threat-goal`
- `monk-threat-goal`
- `enemy-fortifications-goal`
- `escrow-purpose-goal`

These require a different ownership analysis from scratch registers.

## Important correction to earlier extraction

A rule-site scanner that counts only a fixed list of scratch names is useful for proving aliasing, but it is **not** sufficient for complete state ownership extraction. The canonical goal census contains 87 distinct goal symbols, and the next ownership pass must operate over that complete vocabulary.

## Next step

Build the full **87-goal × 36-module** occupancy matrix and then classify each goal as:

`PERSISTENT_SEMANTIC` / `SCRATCH` / `OBJECT_ID` / `CONTROL_FLAG` / `TERMINAL_STATE` / `UNKNOWN`

with exact readers, writers, resetters, activation predicates, and cross-module consumers.
