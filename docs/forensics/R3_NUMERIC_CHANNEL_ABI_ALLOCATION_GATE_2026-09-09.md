# AEGIS / AiByz — R3 Numeric Channel ABI Allocation Gate

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** OPEN — allocation gate

## Purpose

Execute unresolved-proof obligation **R3** from `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`.

The question is not "which numbers look unused?" The question is:

> **Which numeric channels are semantically available for AEGIS, for which operation types, after accounting for stock typing, declarations, references, aliases, engine-specialized meanings, and runtime qualification?**

## 1. Non-negotiable rule

A numeric value is never allocated merely because a scan shows no reference of the desired type.

The following are distinct:

- GOAL
- STRATEGIC NUMBER
- FLAG/state encoding
- TIMER
- GROUP
- scratch/index storage
- engine-defined IDs
- data-field IDs
- unit/building/research/class IDs

Therefore:

`same integer ≠ same ABI channel`

and:

`apparent vacancy ≠ permission to allocate`

## 2. Evidence already available

The repository's stock audit contains a typed symbol inventory and goal-reference inventory. The current census recorded approximately:

- 4,893 numeric declaration rows;
- 1,480 unique declared symbols;
- 756 unique numeric values;
- 257 numeric values shared by multiple symbols;
- 87 referenced goal channels;
- 3,193 goal operations;
- 143 strategic-number channels;
- 1,836 strategic-number operations;
- 29 timers;
- 83 timer operations.

These counts are evidence of namespace density, not an allocation map.

The stock audit also demonstrated the critical collision case: values in the 10,000+ range occur in declarations that are not necessarily GOAL channels. The previously proposed AEGIS cavalry scalar candidate range `10000–10015` therefore remains **UNCLEARED**.

## 3. Allocation model

Every candidate AEGIS channel must pass these gates:

### Gate A — Declaration typing

Identify the exact declaration kind and source symbol using the target-build stock inventory.

### Gate B — Operation typing

Enumerate every operation family in which the candidate would be used. A value acceptable to one operation family is not automatically acceptable to another.

### Gate C — Collision closure

Search declarations, aliases, references, constants, generated inventories and known engine-facing IDs for the candidate value and its semantic neighborhood.

### Gate D — Load closure

Determine whether the symbol/value exists in the effective target program after preprocessing and active loads. Inactive source is not runtime collision; active conditional code is.

### Gate E — Ownership closure

R2 must establish that the proposed channel is not accidentally sharing an existing stock semantic lifetime or authority path.

### Gate F — Validator/compiler qualification

Where the engine/compiler imposes a range or operation constraint, establish it experimentally or from exact target-build evidence. Validator acceptance is not treated as proof of runtime semantics.

### Gate G — Runtime qualification

For channels whose meaning cannot be established statically, a minimal retail-safe probe must distinguish initialization, write, read, reset, and downstream effect.

## 4. Current disposition

| Candidate | Current status | Reason |
|---|---|---|
| AEGIS cavalry scalar block `10000–10015` | **BLOCKED** | numeric collision/typing and runtime safety not closed |
| Any unused GOAL-looking value | **BLOCKED** | vacancy does not establish GOAL allocation permission |
| Any unused SN-looking value | **BLOCKED** | engine-specialized SN semantics and ownership not closed |
| Temporary/scratch goals | **DO NOT ALLOCATE** | must remain explicitly scoped to bounded algorithms |
| Existing stock FactIds | **ENGINE-OWNED** | observations are not AEGIS-owned storage |
| Existing ObjectData IDs | **ENGINE-OWNED** | ABI fields, not controller scratch storage |

## 5. Required machine output

Before ABI freeze, produce one canonical allocation ledger with at least:

```text
candidate_value
channel_type
proposed_symbol
stock_declarations
stock_references
active_load_status
operation_families
engine_specialization
collision_class
R2_owner_status
validator_status
runtime_probe_id
runtime_result
disposition
reason
source_evidence
```

Allowed dispositions:

- `ALLOCATED`
- `RESERVED_PENDING_RUNTIME`
- `REJECTED_COLLISION`
- `REJECTED_ENGINE_SPECIALIZATION`
- `REJECTED_OWNERSHIP`
- `REJECTED_RANGE`
- `REJECTED_UNPROVEN`

No candidate should receive `ALLOCATED` without satisfying all applicable gates.

## 6. Important distinction: stock compatibility vs AEGIS ownership

AEGIS does not need to reproduce every stock numeric channel internally.

The target architecture is:

```text
ENGINE OBSERVATION ABI
        ↓
AEGIS reconciliation
        ↓
AEGIS-owned semantic state
        ↓
AEGIS decision / commitment
        ↓
ENGINE COMMAND ABI
```

Where an engine-provided FactId or ObjectData field already supplies authoritative information, AEGIS should observe it rather than duplicate it merely for architectural symmetry.

## 7. What R3 will NOT do

This pass will not:

- choose numbers by visual emptiness;
- assume 10,000–15,999 is universally unused;
- replace a typed symbol with a raw integer merely to satisfy a validator;
- infer native behavior from a constant name;
- treat compiler acceptance as runtime proof;
- allocate channels before R2 ownership closure;
- introduce a second competing ABI ledger.

## 8. Gate decision

**R3 remains OPEN.**

The correct result at this stage is restraint: no AEGIS numeric ABI is frozen until semantic typing, ownership, collision, and required runtime qualification are closed.

## Evidence basis

- `_local_stock_audit_2026-09-06/symbol_inventory.jsonl`
- `_local_stock_audit_2026-09-06/goal_reference_inventory.jsonl`
- `docs/forensics/R2_MUTABLE_STATE_OWNERSHIP_LEDGER_2026-09-09.md`
- `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`
- `docs/architecture/AEGIS_STOCK_SUBSYSTEM_RECONSTRUCTION_MAP_2026-09-08.md`
