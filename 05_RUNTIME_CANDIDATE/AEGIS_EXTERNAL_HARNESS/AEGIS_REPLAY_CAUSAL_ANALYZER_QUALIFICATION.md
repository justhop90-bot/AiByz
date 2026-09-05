# AEGIS Replay Causal Analyzer Qualification

Status: **IMPLEMENTED / STATICALLY CALIBRATED / RUNTIME-QUALIFICATION OPEN**

## Important parser correction

The first replay-index implementation treated `SYNC.payload[2]` as if it were
a world-state snapshot containing `current_time`. That interpretation was
incorrect for the current mgz-fast output.

The current mgz-fast reference defines a SYNC payload as `(increment,
checksum, data)` and explicitly uses the first field as an elapsed-time
increment. Game duration is obtained by accumulating those increments.

The AEGIS calibration replay confirms the shape directly: its SYNC records are
`[104, null, {}]`, not object-state snapshots.

Therefore AEGIS now treats:

- `ACTION` -> command-issued evidence;
- `SYNC.payload[0]` -> replay-clock increment;
- `SYNC.payload[2]` -> parser metadata only unless independently qualified;
- world-object creation/availability/effectiveness -> **UNKNOWN** from this
  replay stream alone.

## Calibration evidence

Target replay:
`MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`

SHA-256:
`41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

Observed parsed body:

- 221,174 SYNC records;
- 2,213 ACTION records;
- 29 CHAT records;
- 1 POSTGAME record;
- 25,428,749 bytes JSONL;
- SYNC samples consistently use `[104, null, {}]`.

This is strong negative evidence: the current replay-body representation does
not expose the world-object state required to prove `COMMAND -> CREATED`.

## Consequence for the evidence ladder

The replay backend can currently provide:

`COMMAND_ISSUED -> replay-time position`

It cannot provide by itself:

`ACCEPTED -> QUEUED/PENDING -> CREATED -> AVAILABLE -> EFFECTIVE`

The causal analyzer therefore performs temporal correlation only. Temporal
adjacency is explicitly not treated as causal completion.

## Next machine experiment

The next experiment is no longer “find a cleverer replay heuristic.” It is to
obtain an independent world-state observation source and correlate it against
the replay clock:

1. controlled single-production action;
2. exact target build fingerprint;
3. replay capture;
4. independent observation of the resulting object/unit;
5. align observation time to cumulative SYNC time;
6. verify identity continuity;
7. determine the smallest evidence needed to distinguish queued, created,
available, and effective.

The embedded retail `TEST_HARNESS_*` interface remains excluded. AoE2Control
may be used only under its separately qualified invasive-adapter security
profile; it is not an AEGIS core dependency.

## External parser evidence

The upstream mgz-fast documentation describes the body parser as an
operations stream containing player actions, chat, and sync ticks, and defines
game duration by accumulating the first SYNC payload field. AEGIS follows that
contract rather than inferring a richer state model from empty metadata.
