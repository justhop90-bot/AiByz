# AEGIS / AiByz — R4 Existing Inventory Reconciliation

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** OPEN — reconciliation pass; no new broad census authorized

## Purpose

R4 does **not** restart symbol archaeology. The repository already contains deterministic inventories, typed state census data, collision maps, ABI registries, and historical state graphs. This pass reconciles those existing artifacts into the initialization proof surface and identifies only the cells that remain unresolved.

## 1. Existing machine evidence is authoritative input

The following artifacts already provide the raw substrate:

- `_local_stock_audit_2026-09-06/symbol_inventory.jsonl`
- `_local_stock_audit_2026-09-06/goal_reference_inventory.jsonl`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_TYPED_STATE_CENSUS_2026-09-05.json`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_STATE_CHANNEL_COLLISION_MAP_2026-09-05.json`
- `04_LAYER3_ARCHITECTURE/PASS90_STATE_ABI_REGISTRY_2026-09-04.md`
- `04_LAYER3_ARCHITECTURE/PASS90_RUNTIME_PRIMITIVE_REGISTRY_2026-09-04.md`
- `04_LAYER3_ARCHITECTURE/PASS92_ABI_FINALIZATION_AND_ALLOCATION_GATE_2026-09-05.md`
- `04_LAYER3_ARCHITECTURE/PASS93_AUTHORITATIVE_ABI_INVENTORY_SPEC_2026-09-05.md`
- `03_HD_ARCHAEOLOGY/HD_STATE_CHANNEL_GRAPH_PASS4_2026-09-04.md`
- P0 stock substrate and subsystem forensics
- `docs/forensics/R2_MUTABLE_STATE_OWNERSHIP_LEDGER_2026-09-09.md`
- `docs/forensics/R3_NUMERIC_CHANNEL_ABI_ALLOCATION_GATE_2026-09-09.md`

The typed census records 4,893 numeric declaration rows, 1,480 unique declared symbols, 756 unique numeric values, and 257 values shared by multiple symbols. It also records 87 referenced GOAL channels, 143 strategic-number channels, and 29 timers. These are inventory evidence, not by themselves runtime semantics.

## 2. Reconciliation contract

For each mutable channel relevant to AEGIS, derive one row with:

```text
symbol
channel_type
numeric_value
all_declarations
initializer_sites
initializer_kind
initializer_condition
first_writer
subsequent_writers
readers
guards
resetters
reinitializers
lifetime_boundary
owner_candidate
authority_effect
active_load_status
static_evidence_grade
runtime_probe_required
probe_result
disposition
```

### Initialization kinds

Use explicit categories rather than collapsing them:

- `DECLARATION_DEFAULT`
- `LOAD_TIME_ASSIGNMENT`
- `UNCONDITIONAL_RUNTIME_INIT`
- `CONDITIONAL_RUNTIME_INIT`
- `FIRST_USE_WRITE`
- `RESET_REINIT`
- `ENGINE_PROVIDED`
- `UNKNOWN`

A declaration default is not automatically an active runtime initialization. A first observed write is not automatically a global initializer. A reset/reinitialization path is part of lifecycle semantics.

## 3. Existing evidence that can already close cells

A cell may be marked statically resolved when the existing target-build source/inventory proves the complete relevant chain without requiring assumptions about hidden engine behavior.

Examples:

- exact declaration and source line;
- exact unconditional initialization write;
- exact writer/reader operations;
- exact reset/clear operation;
- exact active load provenance;
- exact operation typing;
- exact bounded scratch lifetime in a closed algorithm.

These should be recorded as `DIRECT` or `COMPOSED`, not upgraded to runtime proof merely because the source is explicit.

## 4. Cells that remain runtime-sensitive

The reconciliation must not manufacture certainty for:

1. whether a declaration-only value exists in the engine before the first rule executes;
2. whether conditional initialization executes on every relevant game mode/map/civ path;
3. whether multiple initialization writes race by rule ordering or condition transitions;
4. whether an apparent reset is actually reached in retail execution;
5. whether a command-side write becomes observable through the expected state channel;
6. whether a state value survives reload/transition boundaries;
7. whether an engine-owned observation has a semantic lifetime different from its source declaration.

Those become targeted probe requirements rather than broad re-analysis.

## 5. Canonical examples already known

### `cavarchers`

Historical archaeology already established a writer in `threats.per` and downstream readers in `researches.per` and `units.per`. This is sufficient to establish a distributed state dependency, but the final R4 row still needs initialization/reset/lifetime closure before the channel can be treated as fully qualified.

### `retreat-now-goal`, `attack-status-goal`, `restart-attack-goal`

The historical goal values and their attack/recovery roles are already established. The remaining question is not what the symbols mean by name, but whether their initialization, transitions, reset paths, and world consequences are fully closed under the target runtime.

### `temporary-goal2`

The farthest-pair algorithm explicitly initializes scratch state before candidate comparison. This is a bounded scratch channel, not an AEGIS persistent state allocation. Its lifetime must remain scoped to that algorithm.

### Escrow state

The repository already establishes escrow reservation, release, flags, and the `escrowing` state as part of a resource-control loop. R4 must reconcile every relevant initialization and release path rather than treating the presence of the declaration as the proof.

## 6. Reconciliation result policy

Each row receives one of:

- `CLOSED_STATIC` — existing source/inventory proves the required static lifecycle facts;
- `CLOSED_COMPOSED` — multiple existing artifacts compose into a complete static proof;
- `RUNTIME_REQUIRED` — static evidence stops short of the required semantic claim;
- `CONFLICT` — existing artifacts disagree and require resolution;
- `UNRESOLVED` — insufficient evidence to classify safely;
- `ENGINE_OWNED` — state is supplied by the engine and must not be duplicated as AEGIS scratch state.

## 7. Anti-duplication rule

Do not create another independent symbol inventory, numeric census, goal inventory, or ABI registry.

This document is a **reconciliation layer** over existing machine evidence. If an existing artifact already contains a fact, reference that artifact and classify the fact; do not reproduce the entire corpus in prose.

## 8. R4 gate decision

**R4 remains OPEN.**

The repository already contains most raw initialization evidence. The remaining engineering task is to mechanically join that evidence into the canonical R2/R4 lifecycle ledger and isolate genuinely runtime-dependent cells.

No ABI allocation or production implementation should depend on an R4 cell marked merely `DECLARATION_DEFAULT`, `FIRST_USE_WRITE`, or `UNKNOWN`.

## Next operation

Build the canonical R2/R4 joined ledger from the existing inventories. After that, proceed to R5 command lifecycle qualification using the existing W0–W4 boundary, testing only unresolved transitions.
