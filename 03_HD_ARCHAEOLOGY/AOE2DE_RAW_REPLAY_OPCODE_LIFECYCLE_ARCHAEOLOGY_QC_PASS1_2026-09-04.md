# Layer 2 Pass 21 QC — Raw Replay Opcode / Lifecycle Archaeology

**Date:** 2026-09-04
**Target:** `AOE2DE_RAW_REPLAY_OPCODE_LIFECYCLE_ARCHAEOLOGY_PASS21_2026-09-04.md`
**Verdict:** ACCEPT — WORKING CANON

## QC-01 — Reference identity
PASS. The pass names the exact local reference body and normalized JSONL used for the experiment.

## QC-02 — Raw ACTION census
PASS. The scanner recovered 6,858 ACTION frames, matching the normalized ACTION count.

## QC-03 — Known-ID coverage
PASS. Every recovered reference ACTION ID belongs to the inspected local `mgz.fast.Action` enum.

## QC-04 — Unknown DE actions
PASS. None of the local `DE_UNKNOWN_*` action IDs occurred in the reference ACTION stream.

## QC-05 — CREATE
PASS. CREATE is recognized by the parser enum but absent from the reference recording. No object-birth claim is made.

## QC-06 — Parser capability vs recording evidence
PASS. The pass explicitly separates parser recognition from actual opcode emission in the specimen.

## QC-07 — SYNC interpretation
PASS WITH CAUTION. The pass treats SYNC `obj_count` as an aggregate parser-exposed field and preserves the source's uncertainty about several SYNC semantics.

## QC-08 — Command-to-count correlation
PASS. Aggregate changes are reported as non-causal and non-lineage evidence. No individual queue/build/delete completion is inferred from them.

## QC-09 — W1 discipline
PASS. Pending state is not promoted to authoritative W1 without a validated source.

## QC-10 — W2 boundary
PASS. Object-level realization remains open. The experiment materially narrows the search but does not overclaim impossibility.

## QC-11 — L0/L1/L2/L3 separation
PASS. Raw recording, parser decoding, normalized evidence, and stateful reconstruction remain distinct layers.

## QC-12 — Raw-format exhaustion
PASS. The pass explicitly states that absence of unknown ACTION IDs does not exhaust all raw binary lifecycle possibilities.

## QC-13 — Strategic relevance
PASS. The result directly informs the forensic architecture and prevents wasting effort on an unsupported unknown-opcode shortcut.

## QC-14 — Scenario-loader boundary
PASS. The retired scenario-loader path is not reopened.

## QC-15 — Simulator escalation
PASS. A full simulator is not assumed necessary. Existing playback/state reconstruction is the next escalation; a minimal deterministic interpreter is the fallback.

## QC-16 — Evidence grading
PASS. Direct local experiment, composed inference, and unresolved hypotheses are distinguished.

## QC-17 — Reproducibility
PASS. The raw body, normalized JSONL, local parser, census method, and principal counts are specified sufficiently to reproduce the experiment on the same machine.

## QC-18 — Negative-result integrity
PASS. The absence of CREATE/unknown ACTIONs is recorded as a negative finding rather than as proof of format impossibility.

## QC-19 — Historical authority boundary
PASS. Local parser implementation is used as technical evidence, not as historical HD/Promisory authority.

## QC-20 — Canonical disposition
PASS. **ACCEPT — WORKING CANON.** W2 remains open; the next pass should investigate existing replay playback/state-reconstruction implementations before custom reconstruction.
