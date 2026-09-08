# Replay Machinery QC — 2026-09-05

## Scope

Adversarial QC of the Layer-3B replay machinery after recovery of the project handoff. The objective is to ensure that replay ingestion, temporal labeling, lifecycle indexing, and runtime supervision do not silently claim more than the evidence supports.

## Findings

### 1. ACTION semantics remain command-issued only

The calibration replay contains 2,213 ACTION records, including 448 `DE_QUEUE`, 264 `BUILD`, 59 `RESEARCH`, and 9 `DELETE`. The indexer must not promote these records to accepted, queued, pending, created, available, or effective state without an independent state observation source.

### 2. Temporal naming defect corrected

The previous indexer exposed `replay_time` using a SYNC `current_time` value even though that value was not the ACTION's timestamp. The v2 indexer now preserves:

- `event_sequence`: raw ACTION sequence field;
- `source_line`: exact JSONL source line;
- `record_ordinal`: parsed-record ordinal;
- `nearest_prior_sync_time`: last parser-observed SYNC time before the ACTION;
- `replay_time_candidate`: compatibility alias for the raw sequence, explicitly marked unit-unqualified.

No millisecond claim is made.

### 3. Calibration result

The v2 indexer was executed against `CAL_REPLAY_001`.

- input SHA-256: `04d21b03a23a1aefd790e3f7f909e061e79b73534ad8296db1f917593ff90055`
- records: 444,591
- ACTION: 2,213
- SYNC: 221,174
- SYNC records with parsed `current_time`: 442
- observed parser-time range: 8,866 to 4,693,659
- lifecycle commands indexed: 780
- ACTION sequence regressions: 0
- equal adjacent ACTION sequence pairs: 73

The equal-sequence result is preserved as evidence that ACTION ordering and temporal grouping cannot be reduced to a unique scalar timestamp without further qualification.

### 4. Replay collection race corrected

The collector previously copied the newest candidate immediately. It now verifies that the candidate's size and modification time remain unchanged for a configurable stability interval before copying. Filename build-version matching is optional rather than mandatory because the savegame corpus contains `rec.aoe2record` without the build string in its filename.

A corpus inventory check found 156 `.aoe2record` files in the savegame directory, of which 155 contain `101.103.48987.0` in the filename and one (`rec.aoe2record`) does not. The collector must not silently equate filename syntax with replay build identity.

### 5. Harness timeout classification corrected

The supervisor previously killed a timed-out process before determining whether it was still alive at the observation boundary. v1.1 records `alive_at_timeout` before termination and treats an expected long-running process as an observation success with limitations when it is demonstrably alive at the timeout boundary.

## Independent state-observer candidate

The local `delta-play-replay` / UnCage source was inspected. Its AoE2DE state model contains a `World` object with `time` and an entity map, and `Entity` contains `id`, `master_id`, `owner_id`, world coordinates, state, type, HP, and containment fields. `BuildingEntity` additionally contains `built` and `production_queue`. The gRPC frame model exposes a per-frame `time`, state `patch`, reverse patch, and commands/events.

This is materially different from raw `mgz-fast` replay parsing: it is a candidate independent world-state observation path capable, in principle, of establishing individual entity creation and building realization. It is not yet runtime-qualified on the target calibration experiment.

## Current gate

**PASS:** replay ingestion and provenance preservation.

**PASS:** command-issued classification boundary.

**PASS:** harness lifecycle timeout observation semantics.

**OPEN:** time-aligned world-state observation.

**OPEN:** `DE_QUEUE -> CREATED` qualification.

**OPEN:** `BUILD -> REALIZED` qualification.

**BLOCKED:** any claim that replay ACTION alone proves world-state completion.
