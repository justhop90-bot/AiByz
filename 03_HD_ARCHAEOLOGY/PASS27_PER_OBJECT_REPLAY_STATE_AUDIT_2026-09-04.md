# AEGIS Layer 2 — Pass 27
## Per-Object Replay-State / Raw-Body Audit
**Date:** 2026-09-04
**Status:** ACCEPT — NO W1/W2 PROMOTION

## Objective
Escalate from Pass 26 by testing the raw DE body for hidden operation channels and auditing parser/model structures for genuine per-object lifecycle state.

## Reference corpus
`06_REPLAYS/08_FORENSIC_RUNS/2026-09-02_REFERENCE/body.bin`
SHA-256: `4269461f0cd488ae034f0371e7ef4a083d7f28bd60ae1054f1510e7daa519f3d`
Normalized body remains SHA-256 `3a5ceff2654d86155407dfe98acbab37c3c8432121228d5d0a5959b68c78b9f3`.

## Raw operation-channel census — DIRECT REPLAY / PARSER
The raw body was walked through the local `mgz-fast` operation decoder after its START preamble. Exactly 597,681 operations were decoded with no parser exception:
- ACTION: 6,858
- SYNC: 295,407
- VIEWLOCK: 295,407
- CHAT: 8
- POSTGAME: 1

No unknown/fallback operation ID occurred. Therefore this corpus does not contain an additional unrecognized body-operation channel hidden behind the normalized operation census.

## Parser boundary
The local parser's `operation()` reads a 32-bit operation ID and dispatches only ACTION, SYNC, VIEWLOCK, CHAT and POSTGAME; an unrecognized operation is routed to the SAVE handler. The reference walk observed no such fallback. ACTION parsing then exposes the action payloads, while CREATE is a valid action enum but did not occur in the reference corpus.

## Per-object channel test
The local DE SYNC decoder consumes 88 bytes of per-player values (11 uint32 values × 8 players) plus current time. It retains only total resources, displayable-object count, displayable-object TTL/resource-on-villagers and object count. The source itself marks the semantic interpretations as guesses. No stable per-object ID, object type, owner transition, queue slot, completion flag, or technology-completion field is emitted by this parser path.

## Rich-model source audit — SOURCE-DIRECT
Current upstream `aoc-mgz` model code constructs `Object` records from parsed initial player/Gaia object lists, carrying name/class/object/instance/index/position. Its `TimeseriesRow` contains timestamp, total resources and total objects. Body SYNC processing appends those aggregate rows; it does not construct a per-object delta stream.

`enrich_action()` adds semantic dataset lookups for technology, building, unit, command and related IDs. This enriches command meaning but does not assert execution or completion.

`Inputs.add_action()` maintains an object-ID cache to reuse IDs when an input lacks an explicit selection. This is input normalization/context carry-forward, not a world-state realization mechanism.

## Version/provenance boundary
The local `mgz-fast` directory is not a Git checkout, so no local repository commit can be used as its provenance identifier. The audited local parser source is archived by SHA-256:
`mgz/fast/__init__.py` = `DB0850F144648D7408723A422ED99E7141C7AF957490B64960A623C47AAB47E2`.
Upstream model findings are tied to the current `master` source snapshot used in this audit and must not be treated as version-invariant implementation requirements.

## External playback evidence
The open-source AOE2 game viewer advertises synced build/economy/age-up events and opening-strategy detection from replay data. These are analytics/derived events, not proof of an authoritative object-state ledger. A separate replay dataset project stores sampled game states with unit/building summaries, but explicitly reports missing tech detail and object-width/height errors; it is therefore evidence of derived state reconstruction, not independent engine-authoritative lifecycle proof.

## Engine-backed path
Current CaptureAge documentation establishes a materially different evidence tier: CA:DE can replay standard recordings through the game and exposes rich statistics; CA:DE Recordings can then store game information for playback without AoE2 open. This is the strongest identified candidate for engine-derived state, but it is external to the `.aoe2record` raw-body evidence and has not yet been validated against this reference replay.

## Strategic interpretation
Pass 27 closes an important negative branch: the reference body's operation framing does not hide a second lifecycle stream that the existing normalization simply forgot to label. The remaining gap is not more command correlation; it is execution-state reconstruction or engine observation.

## Evidence ladder
W0: CLOSED — commands/operations directly observed.
W1: OPEN — no authoritative accepted/pending lifecycle channel demonstrated.
W2: OPEN — no authoritative realized object / completed tech channel demonstrated.
W3: OPEN — operational capability remains downstream of W2.

## Decision
**PASS 27: ACCEPT.** No evidentiary promotion. Scenario-loader remains retired.

## Next lowest-cost target
Validate an engine-backed replay path against the reference recording, preferably by extracting a small set of known lifecycle checkpoints: one DE_QUEUE, one BUILD, one RESEARCH and one DELETE, and comparing engine-observed object identity/state and completion timing against the raw command sequence. If engine access is impractical, build a bounded deterministic lifecycle reconstructor and label every promoted field DERIVED rather than authoritative.
