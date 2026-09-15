# AEGIS Channel-Aware ABI Audit v2

Closure files: **5**
Declaration rows: **5262**
Unique symbols: **1482**
Resolved goal operands: **5504**
Resolved high goal operands (512–16000): **7**

## Critical rule

Numeric defconst values are not automatically goal-channel occupancy. A value such as `heavy-wood=10000` is a constant value and becomes a goal identifier only when used in a goal-typed parameter position.

## Resolved high goal operands
- `10000` via `aegis-p0-goal` at `AEGIS_P0_GOAL_SMOKE.per:8`
- `10001` via `aegis-p0-result` at `AEGIS_P0_GOAL_SMOKE.per:9`
- `10001` via `aegis-p0-result` at `AEGIS_P0_GOAL_SMOKE.per:13`
- `10001` via `aegis-p0-result` at `AEGIS_P0_GOAL_SMOKE.per:16`
- `10001` via `aegis-p0-result` at `AEGIS_P0_GOAL_SMOKE.per:19`
- `10000` via `aegis-p0-goal` at `AEGIS_P0_GOAL_SMOKE.per:20`
- `10001` via `aegis-p0-result` at `AEGIS_P0_GOAL_SMOKE.per:23`

Numeric ABI remains unresolved until validator, build-specific legality, ownership, generation, and publication gates pass.
