# CAL_REPLAY_001 — Replay Pipeline Calibration

Status: **PARSE SUCCESS / SEMANTIC QUALIFICATION OPEN**

Target retail build: `101.103.48987.0`

## Source

Replay:
`MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`

Replay size: `6,055,839` bytes
Replay SHA-256: `41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

## Parser

Tool: `mgz-fast`
Installed version: `1.0.0`
Local source snapshot: `C:\Users\justh\OneDrive\Desktop\mgz-fast-master`

The parser successfully produced:

- decompressed header: `3,922,250` bytes
- body: `5,575,340` bytes
- parsed header JSON: `91,249` lines
- parsed body JSONL: `25,428,749` bytes

Artifact hashes:

| Artifact | SHA-256 |
|---|---|
| header.bin | `70daad999ccf4addb303f11ca14d96adac0408e83880344ea3e4d92dc100504b` |
| body.bin | `2a5185018f2d668dae81782b6fb9d859bdcf5dce9dcd917daa1f08f44c1c29f8` |
| header.json | `2e69a57392f95f7037b8d01090ee734a8884d7f78302bff25c1e9478563f7352` |
| body.jsonl | `04d21b03a23a1aefd790e3f7f909e061e79b73534ad8296db1f917593ff90055` |

## Parsed operation census

Total body records: `444,591`

| Operation | Count |
|---|---:|
| SYNC | 221,174 |
| VIEWLOCK | 221,174 |
| ACTION | 2,213 |
| CHAT | 29 |
| POSTGAME | 1 |

ACTION command census:

| Command | Count |
|---|---:|
| MOVE | 832 |
| DE_QUEUE | 448 |
| ORDER | 383 |
| BUILD | 264 |
| GATHER_POINT | 124 |
| RESEARCH | 59 |
| UNGARRISON | 38 |
| SPECIAL | 16 |
| DE_ATTACK_MOVE | 13 |
| DELETE | 9 |
| DE_MULTI_GATHERPOINT | 6 |
| GAME | 4 |
| WALL | 4 |
| BACK_TO_WORK | 4 |
| PATROL | 4 |
| TOWN_BELL | 2 |
| DE_AUTOSCOUT | 1 |
| DE_107_B | 1 |
| FORMATION | 1 |

## Header observations

The replay is a DE recording with `game_version = VER 9.4`, `save_version = 68.0`, and `log_version = 5`.

The parsed map reports `all_visible = false` and dimension `120`. Scenario instructions identify a standard Arabia two-player Tiny map with normal map visibility, no cheats, starting age Dark Age, and population limit 200.

The header contains three player records, including player IDs `1` and `2`; all three records report civilization ID `96` in this parser output. Player names are encoded hexadecimal strings and are preserved as parser output rather than decoded as identity claims.

## Clock evidence

The body contains `221,174` SYNC records, but only `442` contain a parsed integer `current_time` field.

First observed `current_time`: `8,866`

Last observed `current_time`: `4,693,659`

The parser therefore exposes a replay-clock field spanning at least `4,684,793` units between first and last non-null observations. **The unit is not promoted to milliseconds by this artifact alone.** The value is retained exactly as emitted by the parser.

## Lifecycle boundary

The replay contains substantial direct command evidence:

- `DE_QUEUE`: 448
- `BUILD`: 264
- `RESEARCH`: 59
- `DELETE`: 9

These are **issued replay actions**. They are not, by themselves, proof that the requested transition was accepted, queued, created, became available, or became effective.

The current replay stream also contains aggregate SYNC telemetry with `total_res`, `dp_obj_count`, `dp_obj_ttl`, and `obj_count` for players in some snapshots. These are aggregate observations and cannot be promoted to individual object lineage without additional evidence.

## Qualification result

`CAL_REPLAY_001 = PASS_PIPELINE_PARSE / NOT_YET_SEMANTICALLY_QUALIFIED`

What is established:

1. A real target-build `.aoe2record` exists locally.
2. Its bytes are hashable and reproducible.
3. `mgz-fast 1.0.0` successfully parses the recording.
4. Header and body extraction succeeds.
5. The body parser produces a stable JSONL event stream.
6. The stream contains direct action records and periodic aggregate synchronization records.

What remains unproven:

1. exact replay-time unit semantics;
2. command acceptance semantics;
3. pending/queued versus created state;
4. created versus available state;
5. effective world-state transition;
6. individual object identity continuity through lifecycle transitions;
7. live-runtime versus replay-time clock alignment.

The harness must preserve these distinctions. No semantic PASS is awarded from this calibration alone.
