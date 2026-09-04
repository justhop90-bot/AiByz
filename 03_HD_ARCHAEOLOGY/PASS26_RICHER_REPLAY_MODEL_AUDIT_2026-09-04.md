# AEGIS Layer 2 — Pass 26
## Richer Replay Model / Object-State Archaeology
**Date:** 2026-09-04
**Status:** ACCEPT — NO W2 PROMOTION

## Objective
Test whether the richer `aoc-mgz` model layer exposes lifecycle state that the local `mgz-fast` normalization discards.

## Direct source findings
The richer model constructs `Object` records from the parsed initial player/Gaia object lists. Each object has `class_id`, `object_id`, `instance_id`, `index`, and `position`. This is real object identity for objects present in the parsed initial state.

The model's `TimeseriesRow` contains only timestamp, total_resources, and total_objects. During body parsing, SYNC records populate those aggregate timeseries rows; the model does not convert SYNC into a per-object lifecycle stream.

Actions remain timestamped command records. `enrich_action` resolves building/unit/technology IDs through datasets, but does not assert command completion. `Inputs` further normalizes actions; its cache can reuse object IDs between related inputs, but this is input normalization, not world-state realization.

## Important distinction
Richer model != replay simulator. It supplies richer static/header object identity and semantic lookup, while preserving the same command/SYNC boundary for the body. The model therefore improves metadata and object references but does not supply a proved spawned-object, construction-completion, queue-completion, or technology-completion ledger.

## W2 implications
Initial object identity is useful for matching commands whose actors already exist in the initial snapshot. It cannot establish identity for a later-created unit/building unless the recording exposes a later authoritative object instance. Aggregate timeseries still cannot establish that bridge.

A `DE_QUEUE` action can therefore be enriched with a unit definition and producer identity, but remains a production request. A `BUILD` action can be enriched with building definition and builder IDs, but remains a construction request. `RESEARCH` can be enriched with technology metadata, but remains a research request.

## Independent external corroboration
Current `aoc-mgz` documentation/source continues to model replay actions and aggregate SYNC telemetry rather than providing a continuously simulated authoritative world state. Existing replay-viewer projects likewise demonstrate reconstructed timelines but must be treated as derived playback state unless independently validated against engine state.

## Decision
The richer model layer is valuable and should be incorporated into the AEGIS archaeology toolchain for semantic enrichment, initial object identity, map/object metadata, and provenance. It is NOT sufficient to close W1/W2.

**PASS 26: ACCEPT.** W0 remains CLOSED; W1, W2 and W3 remain OPEN. Scenario-loader remains retired.

## New architectural boundary
`RICH_REPLAY_MODEL` should be treated as an enrichment layer between normalized replay evidence and the conservative state interpreter:

RAW RECORDING -> PARSER -> RICH MODEL / NORMALIZATION -> EVIDENCE INTERPRETER -> STATE

The interpreter must still require independent postcondition evidence before promoting lifecycle candidates.

## Next target
The next lowest-cost escalation is not another aggregate-correlation experiment. Investigate whether any replay format/body section, existing parser branch, or playback implementation exposes per-object snapshots/deltas or completion state, then validate any candidate channel against known object IDs and timestamps in the reference replay.
