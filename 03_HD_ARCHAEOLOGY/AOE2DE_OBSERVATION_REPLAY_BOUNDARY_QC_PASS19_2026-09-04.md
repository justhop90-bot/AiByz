# Layer 2 Pass 19 QC — Observation / Replay Information Boundary

**Date:** 2026-09-04
**Verdict:** ACCEPT WITH CORRECTIONS — WORKING CANON

## Audit target
Determine whether Pass 19 overstates what the external `aoc-mgz` parser proves about dynamic replay state.

## Findings

### QC-01 — Fast/full distinction
PASS. The upstream project explicitly distinguishes a fast parser from a fuller parser and documents materially different support/capability.

### QC-02 — Rich object schema
PASS. The inspected object parser contains object identity, type, owner context, hitpoints, object state, position, under-attack state, movement/path information, action/target information, AI state, and building production/construction fields.

### QC-03 — Initial-object scope
PASS. The inspected model constructs object records from player/gaia objects parsed from the header. These are not demonstrated to be a complete time-indexed dynamic object ledger.

### QC-04 — Body architecture
PASS. The model processes the body as operations/actions and SYNC-derived aggregate timeseries. No complete continuously mutated object database was identified in the inspected implementation.

### QC-05 — Full parser solves W2
FAIL if stated categorically. Correct statement: full parser exposes richer information and parses more, but the inspected implementation does not establish automatic dynamic W2 reconstruction.

### QC-06 — Replay is initial state plus moves
PASS. Upstream documentation explicitly describes recorded games as an initial-state header followed by body moves that the game applies to mutate state.

### QC-07 — Replay simulation implication
PASS WITH QUALIFICATION. Applying those moves through validated game semantics is the natural route to arbitrary reconstructed state, but exact equivalence to the current DE runtime remains unvalidated.

### QC-08 — Historical AI observation comparison
PASS AS INFERENCE. `.per` executes against live engine objects and uses object-data/search primitives. Replay parser output is not the same observation interface.

### QC-09 — W2 closure
PASS. W2 remains open for production, research, building, and attack on the normalized replay surface.

### QC-10 — AEGIS architecture
PASS AS AEGIS-GENERALIZATION. Separating immutable replay evidence from a stateful reconstruction layer is recommended design, not recovered historical doctrine.

## Required language discipline
Never write “the replay contains no object state.” The more precise finding is: the tested normalized body surface does not expose sufficient dynamic object-state lineage for the requested W2 claims.

Never write “full mgz cannot reconstruct state.” State only that the inspected full parser/model does not itself provide a continuously reconstructed dynamic world-state database.

Never promote external parser implementation details to Layer-2 historical authority. They are secondary technical evidence about replay tooling.

## Final disposition
Pass 19 is accepted as a working-canon boundary study. It materially narrows the runtime problem from “find the missing JSON field” to “identify or implement a validated stateful replay executor.”

The next pass should inventory existing replay playback/state-reconstruction implementations before any custom simulator is considered.
