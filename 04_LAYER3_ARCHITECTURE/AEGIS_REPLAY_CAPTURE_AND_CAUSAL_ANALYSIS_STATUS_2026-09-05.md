# AEGIS — Replay Capture and Causal Analysis Status

**Date:** 2026-09-05
**Status:** ACTIVE — EVIDENCE ACQUISITION
**Target build:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Purpose

This document records the current state of the actual replay-capture and replay-analysis subsystem so a future project lead can resume without reconstructing the investigation from conversation history.

The subsystem exists to establish causal relationships between controller commands and observable game-world transitions. It is explicitly not permitted to infer hidden engine state merely because a replay record is adjacent in time to a command.

## Actual calibration replay

**File:** `MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`

**SHA-256:** `41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

**Size:** `6,055,839 bytes`

### Extraction

- Header: `3,922,250 bytes`
- Body: `5,575,340 bytes`

### Parsed record census

- Total records: `444,591`
- ACTION: `2,213`
- SYNC: `221,174`
- CHAT: `29`
- POSTGAME: `1`

### ACTION census

- MOVE: `832`
- DE_QUEUE: `448`
- ORDER: `383`
- BUILD: `264`
- GATHER_POINT: `124`
- RESEARCH: `59`
- UNGARRISON: `38`
- DELETE: `9`
- plus specialized action types

### Time observations

The parser exposed `442` non-null `current_time` observations.

- First observed value: `8,866`
- Last observed value: `4,693,659`

These values are deliberately **not yet declared to be milliseconds**. The unit/clock semantics require an independent calibration experiment against known game-time anchors.

## Implemented replay tooling

The AEGIS external-harness branch contains executable Python tooling, not placeholder prose:

- `harness.py` — build fingerprinting, launch supervision, lifecycle capture, safety enforcement.
- `replay_collector.py` — replay artifact acquisition/monitoring.
- `replay_index.py` — conservative replay record normalization and lifecycle candidate indexing.
- `test_harness.py` — automated harness tests.
- `test_replay_index.py` — automated replay-index tests.
- `schema.json` — experiment/evidence schema.

The replay indexer generated approximately `780` lifecycle-command candidate events from the calibration replay.

## Evidence interpretation contract

The current analyzer uses the following hard rule:

`ACTION` = evidence that an action/command record exists.

`SYNC` = evidence of an aggregate game-state/snapshot record.

`ACTION + later SYNC correlation` = candidate causal evidence only.

The analyzer must not automatically upgrade that relationship to:

- accepted;
- queued;
- pending;
- created;
- available;
- deployed;
- effective;
- successful.

Those states require additional evidence.

## Required causal ladder

The machine qualification target is:

`COMMAND_ISSUED`
`    ↓`
`ACCEPTED / REJECTED`
`    ↓`
`PENDING / QUEUED`
`    ↓`
`CREATED`
`    ↓`
`AVAILABLE`
`    ↓`
`EFFECTIVE`
`    ↓`
`VERIFIED`

The replay subsystem currently proves only portions of the first and last observation layers. It does not yet establish every intermediate transition.

## Highest-value next analyzer work

### 1. DE_QUEUE → object creation

Identify an experiment with a uniquely attributable training event.

Correlate the queue action with subsequent snapshots containing the resulting unit/object identity.

Record:

- action time;
- candidate queue identity;
- first object observation;
- object identity continuity;
- elapsed controller/game time;
- competing explanations;
- evidence grade.

### 2. BUILD → building realization

Perform the same analysis for a building whose placement and object identity are unambiguous.

This is useful because it separates command issuance from physical world realization without requiring combat semantics.

### 3. RESEARCH → technology state

Establish whether a research action can be correlated with a later state that proves technology completion rather than merely command issuance.

### 4. TRAIN → availability

Separate:

`training command`
→ `queue/pending`
→ `unit object created`
→ `unit available for use`

Do not collapse these events.

## Negative experiments required

The causal analyzer must eventually be tested against intentionally non-successful cases:

- insufficient resources;
- missing production building;
- impossible build location;
- cancelled queue;
- superseded intent;
- intentionally hidden object;
- zero-result query;
- unsupported query.

These negative cases are necessary to distinguish:

`FALSE`
`ZERO`
`ABSENT`
`UNKNOWN`
`REJECTED`
`NOT OBSERVABLE`

They are not interchangeable.

## Temporal qualification

The replay `current_time` field must be independently calibrated before it becomes an AEGIS timing primitive.

Required experiment:

1. create a disposable match with known deterministic event timing;
2. record at least two events with externally known relative timing;
3. compare replay `current_time` deltas against the known timeline;
4. repeat across multiple event types;
5. document resolution, units, monotonicity, and reset behavior;
6. bind the result to the exact target build.

## Replay/live correlation

If a live observer is used later, it must be treated as a separate evidence stream.

The desired structure is:

`live observation + replay observation + build identity + experiment identity + temporal correlation`

A live observation must not silently become authoritative merely because it is more immediate. Replay evidence must not silently become authoritative merely because it is easier to archive.

The two streams should corroborate one another where possible.

## Parser limitations

Replay parsing is post-run evidence.

It does not automatically reconstruct arbitrary hidden runtime state, resource state at every instant, or the exact causal mechanism behind every action. Where the record format cannot discriminate between competing explanations, the analyzer must emit `UNKNOWN` or a qualified candidate state rather than guessing.

## Relationship to AEGIS architecture

This replay subsystem supports the Execution, Verification, Recovery, World Model, and shared Machine Truth / Qualification Layer.

It does not replace those subsystems.

Its job is to provide evidence strong enough to qualify machine primitives that those subsystems may consume.

## Promotion rule

A replay-derived conclusion cannot become a verified machine primitive solely because:

- the parser returned a field;
- an action precedes a state change;
- the timestamps look plausible;
- the result occurred in a successful human game;
- the same pattern was observed once.

Promotion requires repeatable, build-scoped evidence and explicit documentation of alternative explanations.

## Current disposition

**Replay capture:** operational.

**Replay parsing:** operational.

**Lifecycle indexing:** operational.

**Causal state inference:** partially implemented; intentionally conservative.

**Time-unit qualification:** open.

**Command acceptance qualification:** open.

**Pending/created qualification:** open.

**Created/available qualification:** open.

**Effectiveness qualification:** open.

**Negative-case discrimination:** open.

**Cross-run repeatability:** open.

**Live/replay corroboration:** open.

## Next action

Do not expand the Byzantine strategy implementation yet.

Build the smallest disposable experiment that makes one world transition unambiguous, capture it repeatedly, and use the resulting replay to extend the causal analyzer.

The immediate objective is not a better replay parser.

**The immediate objective is a defensible mapping from one issued command to one observable world transition.**
