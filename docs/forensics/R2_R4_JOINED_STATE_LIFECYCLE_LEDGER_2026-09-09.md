# AEGIS / AiByz — R2/R4 Joined State Lifecycle Ledger

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** OPEN — canonical join specification + evidence-backed seed rows; not a fabricated complete census

## 0. Why this artifact exists

R2 and R4 are not separate archaeology programs.

- **R2** asks who owns mutable state and controls its lifetime.
- **R4** asks how that state is initialized, reset, reinitialized, and invalidated.

This ledger is the single reconciliation surface for both questions.

It deliberately references existing machine inventories instead of copying them. The authoritative raw evidence remains:

- `_local_stock_audit_2026-09-06/symbol_inventory.jsonl`
- `_local_stock_audit_2026-09-06/goal_reference_inventory.jsonl`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_TYPED_STATE_CENSUS_2026-09-05.json`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_STATE_CHANNEL_COLLISION_MAP_2026-09-05.json`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_LOAD_CLOSURE_2026-09-05.json`
- `04_LAYER3_ARCHITECTURE/PASS90_STATE_ABI_REGISTRY_2026-09-04.md`
- `04_LAYER3_ARCHITECTURE/PASS90_RUNTIME_PRIMITIVE_REGISTRY_2026-09-04.md`
- `04_LAYER3_ARCHITECTURE/PASS92_ABI_FINALIZATION_AND_ALLOCATION_GATE_2026-09-05.md`
- `04_LAYER3_ARCHITECTURE/PASS93_AUTHORITATIVE_ABI_INVENTORY_SPEC_2026-09-05.md`
- `03_HD_ARCHAEOLOGY/HD_STATE_CHANNEL_GRAPH_PASS4_2026-09-04.md`
- `docs/forensics/R2_MUTABLE_STATE_OWNERSHIP_LEDGER_2026-09-09.md`
- `docs/forensics/R3_NUMERIC_CHANNEL_ABI_ALLOCATION_GATE_2026-09-09.md`
- `docs/forensics/R4_EXISTING_INVENTORY_RECONCILIATION_2026-09-09.md`

## 1. Evidence contract

A ledger row is not considered complete merely because a symbol exists in the inventory.

For each symbol/channel the join must preserve:

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

The source hash is part of the evidence identity. A row must not silently combine facts from differently hashed source snapshots.

## 2. Existing machine inventory facts

The typed census records, for the target stock snapshot:

- 4,893 numeric declaration rows;
- 1,480 unique declared symbols;
- 756 unique numeric values;
- 257 numeric values shared by multiple symbols;
- 87 referenced GOAL channels;
- 143 strategic-number channels;
- 29 timers.

The inventory also records exact source hashes. For example, `AI (HD version).per` is 1,167,238 bytes / 36,141 lines with SHA-256 `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`; the three Promisory runtime-substrate files have independently recorded hashes in the same census. These values are provenance, not semantic claims.

## 3. Seed rows that are already evidence-backed

These are **not claimed to be the complete ledger**. They demonstrate the exact join form and identify where existing evidence stops.

| Symbol | Channel | Numeric declaration | Static evidence currently established | Owner candidate | Remaining R2/R4 gap | Disposition |
|---|---|---:|---|---|---|---|
| `sn-cavalry-threat` | SN | 65 | Exact declaration in target stock snapshot: `AI (HD version).per:24`; downstream threat/research/production use is documented in existing archaeology | Stock threat/intelligence state | Full writer set, clearers, lifetime and target-runtime observability | RUNTIME_REQUIRED |
| `cavarchers` | mutable threat state | source-defined | Existing archaeology identifies writer in `threats.per` and readers in `researches.per` / `units.per` | Threat/intelligence subsystem | Exact initialization/reset/lifetime join against authoritative source snapshot | RUNTIME_REQUIRED |
| `retreat-now-goal` | GOAL | 20 | Exact declaration: `AI (HD version).per:52`; attack/retreat lifecycle is established historically | Tactical attack/retreat controller | Complete initialization, reset, transition reachability and world consequence | RUNTIME_REQUIRED |
| `attack-status-goal` | GOAL | 24 | Exact declaration: `AI (HD version).per:56`; attack lifecycle role established historically | Tactical attack controller | Complete writer/reset ownership and target-build transition realization | RUNTIME_REQUIRED |
| `restart-attack-goal` | GOAL | 27 | Exact declaration: `AI (HD version).per:59`; restart lifecycle role established historically | Tactical recovery controller | Complete reset/re-entry ownership and target-build realization | RUNTIME_REQUIRED |
| `temporary-goal2` | scratch GOAL | algorithm-local | Existing archaeology proves explicit initialization before farthest-pair candidate comparison | `general.per` search routine | Exact source/hash occurrence join and confirmation that no cross-routine lifetime escapes exist | CLOSED_COMPOSED* |

`*` The bounded-lifetime interpretation is compositionally supported by the recovered algorithm, but it does **not** grant this scratch channel permission for AEGIS allocation.

## 4. Important declaration collision already demonstrated

The inventory contains `treaty-time` with value `33` in `AI (HD version).per` and value `54` in `Promisory/defaultConstants.per`.

This is precisely why the join key cannot be:

`numeric value → meaning`.

The required identity is at minimum:

`source hash + source file + symbol + channel/operation context`.

The existing census already exposes this collision; no new interpretation is required.

## 5. Static closure rules

A cell may be `CLOSED_STATIC` only when the target snapshot proves the relevant fact directly.

A cell may be `CLOSED_COMPOSED` only when multiple existing artifacts compose without an unsupported assumption.

A cell becomes `RUNTIME_REQUIRED` when static source evidence cannot establish execution-dependent behavior such as:

- conditional initialization actually executing;
- rule-order interaction;
- reset reachability;
- state persistence across transitions;
- command-side state becoming observable;
- engine-provided observation lifetime;
- accepted/queued/pending/created/available/effective transitions.

Unknown is not converted to false, zero, absent, or success.

## 6. Owner determination rules

Owner is not synonymous with writer.

A symbol may have multiple writers while still having one semantic owner, but only if those writers are structurally governed by the same ownership contract. Otherwise the row remains unresolved/conflicted.

The following distinctions are mandatory:

- **ENGINE_AUTHORITATIVE:** engine observation is the source of truth.
- **AEGIS_AUTHORITATIVE:** AEGIS owns the semantic state.
- **DERIVED_CACHE:** recomputable state; not authoritative.
- **OBSERVATIONAL:** diagnostic/evidence state only.

A reader never becomes an owner merely by consuming the value.

## 7. Initialization classification

Use only these values:

`DECLARATION_DEFAULT`
`LOAD_TIME_ASSIGNMENT`
`UNCONDITIONAL_RUNTIME_INIT`
`CONDITIONAL_RUNTIME_INIT`
`FIRST_USE_WRITE`
`RESET_REINIT`
`ENGINE_PROVIDED`
`UNKNOWN`

Do not infer `UNCONDITIONAL_RUNTIME_INIT` from the existence of a declaration.

Do not infer `RESET_REINIT` from a later write unless the source operation and control path establish reset semantics.

## 8. The exact remaining join work

The raw inventory is already sufficient to avoid another broad symbol census. The missing operation is a source-level occurrence join.

For every relevant symbol, the reconciliation process must:

1. resolve every declaration from the existing symbol inventory;
2. preserve the declaration's source SHA-256;
3. enumerate every source occurrence in the same authoritative snapshot;
4. classify each occurrence by operation role: read, write, clear/reset, compare/guard, or declaration;
5. capture the enclosing rule and condition text without normalizing away tokens;
6. identify initialization candidates separately from ordinary writes;
7. identify reset/reinitialization candidates separately from first-use writes;
8. join readers and writers to the existing historical state graph;
9. join the symbol to active-load evidence;
10. assign the strongest defensible static evidence grade;
11. mark runtime-required cells rather than filling them by inference;
12. emit one canonical row per semantic symbol/channel, while retaining all underlying occurrences.

The underlying occurrence records must remain available as evidence. The ledger is an index, not a replacement for raw evidence.

## 9. No numeric ABI allocation follows from this ledger yet

The ledger deliberately does **not** clear any AEGIS numeric identifier.

In particular, the proposed `10000–10015` cavalry scalar range remains blocked. The existing inventory already demonstrates cross-channel numeric collisions and Pass 93 requires collision, load, ownership, validator, and runtime gates before allocation.

## 10. R2/R4 status

**R2: OPEN.**  
**R4: OPEN.**  
**Joined ledger: PARTIAL / SEED COMPLETE, EXHAUSTIVE OCCURRENCE JOIN PENDING.**

This is an intentional evidence boundary. Claiming an exhaustive join from the currently retrievable repository excerpts would fabricate closure.

## 11. Next gate

Once the exhaustive occurrence join is generated from the exact stock snapshot, the next operation is **R5 command lifecycle qualification**, restricted to transitions that remain unresolved after this ledger is complete:

`DESIRE → CAN-FACT → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

The R5 program must not retest transitions already closed by direct evidence, and it must not use command presence as proof of world-state realization.
