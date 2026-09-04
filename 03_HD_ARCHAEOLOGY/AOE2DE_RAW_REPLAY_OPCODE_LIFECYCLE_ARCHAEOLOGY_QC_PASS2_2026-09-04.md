# Layer 2 Pass 21 — Deep QC Pass 2

**Date:** 2026-09-04  
**Target:** `AOE2DE_RAW_REPLAY_OPCODE_LIFECYCLE_ARCHAEOLOGY_PASS21_2026-09-04.md`  
**Verdict:** ACCEPT WITH CORRECTIONS — corrected working canon

## QC-01 — Reference identity
PASS. The artifact identifies the reference body and normalized replay used for the experiment.

## QC-02 — Raw ACTION coverage
PASS. The scanner recovered 6,858 ACTION frames, matching the normalized ACTION count. This is strong direct evidence for frame-count parity.

## QC-03 — Known opcode coverage
PASS. Every recovered ACTION ID belongs to the local `mgz.fast.Action` enum. No unknown action IDs were observed in the reference specimen.

## QC-04 — CREATE
PASS. CREATE is recognized by the parser but absent from the reference ACTION stream. The artifact correctly refuses to promote parser recognition into lifecycle semantics.

## QC-05 — Unknown DE opcodes
PASS. The named `DE_UNKNOWN_*` enum entries are absent from the reference specimen. Their meanings remain unresolved rather than being inferred from names.

## QC-06 — Parser capability versus recording evidence
PASS. The distinction is explicit and should remain canonical:

`parser capability != recording emission != semantic interpretation != reconstructed state`.

## QC-07 — SYNC semantics
CORRECTED. SYNC `obj_count`, `dp_obj_count`, and `dp_obj_ttl` must be described as parser-exposed fields whose meanings are partly source-documented as guesses. They are useful aggregate observations but not independently authoritative object identity.

## QC-08 — Temporal correlation
PASS WITH LIMITATION. Sequence is a valid ordering candidate and was used for neighborhood correlation. It is not by itself proof of elapsed wall-clock time or causal completion.

## QC-09 — Population deltas
PASS. Aggregate object-count changes around lifecycle commands are non-causal with respect to individual command completion. Multiple game events can affect the same aggregate.

## QC-10 — Production lineage
PASS. `DE_QUEUE` exposes producer IDs, unit ID, amount, player and sequence, but does not expose a newly-created unit ID. Later control of an object cannot be attributed to a specific queue without validated lineage.

## QC-11 — Build lineage
PASS. BUILD exposes builder selection/coordinates/building ID in the tested parser surface. It does not itself prove foundation completion or completed-building identity.

## QC-12 — Research lineage
PASS. RESEARCH proves a research command against an object and technology ID. It does not itself prove research completion.

## QC-13 — Delete lineage
PASS. DELETE exposes an object ID and player. It proves a deletion command, not the complete lifecycle history that led to deletion.

## QC-14 — W1 wording
CORRECTED. W1 means **authoritative accepted/pending state**, not merely an inferred state after a command. A command may justify a pending hypothesis, but that hypothesis must not be promoted to W1 without an authoritative state observation.

## QC-15 — W2 wording
PASS. W2 remains OPEN. The experiment did not close individual object-level realization.

## QC-16 — W3 wording
PASS WITH CORRECTION. W3 may be established for an individual object only when operational capability is independently observed. Command-lineage evidence alone does not prove realized capability.

## QC-17 — W4 wording
PASS. Strategic effect remains OPEN and is deliberately separated from command execution.

## QC-18 — L0/L1/L2/L3 boundary
PASS. The four-layer model is correct as an engineering/forensic abstraction:

`L0 RAW RECORDING → L1 PARSER DECODING → L2 NORMALIZED EVIDENCE → L3 STATEFUL RECONSTRUCTION`.

The experiment tests L0 sufficiently to establish the observed ACTION census, but does not exhaustively reverse-engineer every non-ACTION byte structure.

## QC-19 — Simulator escalation
PASS. A full game simulator is not yet justified. Existing playback/state reconstruction should be investigated first; if necessary, a minimal deterministic interpreter is the preferred engineering escalation.

## QC-20 — Scenario-loader boundary
PASS. The scenario-loader remains retired and is not required for this line of investigation.

## Corrections to Pass 21

1. Treat the artifact as **parser-boundary + reference ACTION archaeology**, not complete raw-format archaeology.
2. Retain `W1 OPEN` unless a separate authoritative pending-state source is found.
3. Retain `W2 OPEN`.
4. Do not interpret SYNC aggregates as object identity.
5. Do not interpret absence of unknown opcodes as proof of absence of all lifecycle information from L0.
6. Promote existing playback/state-reconstruction archaeology to the next escalation.

## Final disposition

**PASS 21 — ACCEPT WITH CORRECTIONS / WORKING CANON.** The core negative finding survives: the reference ACTION stream contains no unknown-action or CREATE shortcut capable of closing W2. The raw replay format is not declared exhausted.