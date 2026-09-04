# AEGIS Layer 2 — Pass 25
## DE SYNC State-Channel Audit
**Date:** 2026-09-04
**Status:** ACCEPT — NO W2 PROMOTION

## Objective
Determine whether DE SYNC telemetry in the normalized replay can serve as an authoritative lifecycle channel for pending operations.

## Source
`06_REPLAYS/08_FORENSIC_RUNS/2026-09-02_REFERENCE/body_fresh.jsonl`
SHA-256: `3a5ceff2654d86155407dfe98acbab37c3c8432121228d5d0a5959b68c78b9f3`

## What SYNC actually exposes
The parser emits `current_time` plus, for active players, total resources, displayable-object count, displayable-object TTL/resource-on-villagers, and object count. The parser source explicitly labels these fields as guesses rather than authoritative semantic definitions.

## Direct observation
SYNC state is dense and time-indexed. Early samples show player object counts changing from 14 to 15/16 while displayable counts change independently. This demonstrates that the channel carries aggregate world telemetry.

## Lifecycle correlation experiment
For each DE_QUEUE, BUILD, RESEARCH and DELETE candidate, the nearest preceding and following populated SYNC records were compared for the issuing player. Object-count deltas were highly heterogeneous. DE_QUEUE produced deltas ranging from large negative to large positive values; BUILD likewise ranged broadly; RESEARCH frequently had zero but also substantial positive and negative changes; DELETE was similarly mixed.

Therefore an object-count delta is not a one-operation lifecycle signal.

## Critical distinction
`obj_count` is an aggregate counter. `dp_obj_count` is another aggregate/display-oriented counter. Neither exposes stable object identity, type, ownership transition, queue slot, completion marker, or technology completion state in the normalized representation.

## Why this does not close W1/W2
A queue can coexist with unrelated births/deaths, a building command can coexist with other construction or destruction, research can change no object count, and deletion can occur amid unrelated aggregate changes. The same aggregate transition therefore admits multiple causal explanations.

## Provenance rule
SYNC aggregate deltas are retained as DERIVED temporal/context evidence. They cannot promote an operation to W1 or W2 by themselves.

## Next escalation
The lowest-cost remaining target is the raw DE SYNC structure beyond the fields retained by `mgz-fast`: inspect full replay decoding/state models for fields that may preserve per-object identity or lifecycle state. Full aoc-mgz/playback structures should be treated as candidate evidence channels and independently validated against the recording.

## Quantitative findings
Lifecycle candidates: DE_QUEUE 1,493; BUILD 471; RESEARCH 118; DELETE 33. Populated SYNC records expose two player states in the reference.

For preceding/following SYNC comparisons, usable candidates were 1,488 DE_QUEUE, 467 BUILD, 118 RESEARCH and 33 DELETE. The resulting object-count changes were non-deterministic across each command class.

## Negative tests
- `DE_QUEUE + obj_count increase` is not sufficient for spawned-unit identity.
- `BUILD + obj_count increase` is not sufficient for completed-building identity.
- `RESEARCH + unchanged obj_count` is not evidence against completion, nor is a changed count evidence for completion.
- `DELETE + obj_count decrease` does not prove that the deleted target caused the aggregate change.

## Decision
The normalized DE SYNC channel is useful for aggregate economic/population/object context and temporal alignment, but it is not an authoritative lifecycle ledger.

**PASS 25: ACCEPT.** W0 remains CLOSED; W1, W2 and W3 remain OPEN. Scenario-loader remains retired.

## Engineering implication
Do not increase interpreter confidence merely because aggregate counters correlate visually with commands. The missing bridge is semantic identity/state, not more correlation heuristics.
