# AEGIS / AiByz — R2 Mutable State Ownership Ledger

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** IN PROGRESS — ledger skeleton and high-confidence seed entries established

## Purpose

Execute unresolved-proof obligation **R2** from `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`.

The objective is to stop treating the stock AI's mutable state as a bag of numbers. Every state channel that AEGIS may depend upon must have an explicit lifecycle and owner.

Required model:

`channel → symbol → declaration → initializer → writers → readers → guards → resetters → lifetime → owner → authority effect → downstream consumers → evidence grade`

## 1. Ownership rules

1. **Engine-owned state is not AEGIS-owned state.** Facts and ObjectData are observations/capabilities supplied by the engine unless the engine contract proves otherwise.
2. **A writer is not automatically an owner.** A module can write a channel as a consequence of another service's decision.
3. **A reader is not an authority.** Consumption of a state value does not establish permission to mutate it.
4. **Resetters define lifetime boundaries.** A channel with a clear/reset path is not equivalent to persistent memory.
5. **Scratch state must be isolated.** Temporary goals and index variables cannot become durable AEGIS state merely because they carry useful values.
6. **Same numeric value does not imply same channel.** GOAL/SN/FLAG/TIMER semantics remain distinct.
7. Every eventual AEGIS-owned state channel must have one declared semantic owner and an explicit generation/lifetime policy.

## 2. High-confidence seed entries

These entries are deliberately limited to relationships already established by repository archaeology. They are not presented as the complete matrix.

| Channel | Symbol/state | Known writers | Known readers/consumers | Reset/lifetime evidence | Provisional owner | Status |
|---|---|---|---|---|---|---|
| threat aggregate | `cavarchers` | `threats.per` path | `researches.per`, `units.per` | threat recomputation/reset behavior requires full ledger | Threat Service | PARTIAL |
| escrow state | `escrowing` / related escrow state | escrow authorization/release paths | research/production/economic guards | release paths clear escrow state | Resource Arbitration | STRONG, needs symbol-level closure |
| persistent goal | `retreat-now-goal` = 20 | attack/retreat control | retreat/recovery control | lifecycle tied to attack state | Military OS | STRONG historical; runtime open |
| persistent goal | `attack-status-goal` = 24 | attack control | attack/recovery logic | attack lifecycle transitions | Military OS | STRONG historical; runtime open |
| persistent goal | `restart-attack-goal` = 27 | attack/recovery control | restart logic | restart/recovery transitions | Military OS | STRONG historical; runtime open |
| temporary goal | `temporary-goal2` in 504/505 path | geometry selection | farthest-pair comparison | initialized to `-1` within algorithm | Land-Nomad/Geometry service | DIRECT source behavior; runtime semantics open |
| timer | attack/recovery timers | attack/retreat paths | transition guards | timer expiry drives reassessment | Military OS / Recovery | PARTIAL |
| fact | stock FactIds 0–55 | engine | many service rules | engine-owned | Engine Observation ABI | ABI evidence strong |
| ObjectData | stock object-data fields | engine | worker/construction/scout/military consumers | engine-owned | Engine Observation ABI | ABI evidence strong |

## 3. Required ledger fields

The eventual machine-readable ledger must use at least these fields:

```text
channel_type
symbol
numeric_value
source_file
source_line
active_load_status
declaration_kind
initializer
initializer_condition
writer
writer_condition
reader
reader_condition
guard
resetter
reset_condition
lifetime
semantic_owner
authority_effect
downstream_consumer
evidence_level
confidence
runtime_probe_required
runtime_probe_id
superseded_by
notes
```

## 4. Channel classes that must be censused

### GOAL

- persistent strategic goals;
- temporary scratch goals;
- goal values used as indices or handles;
- goals read by cross-service policy.

### STRATEGIC NUMBER (SN)

- policy scalars;
- thresholds;
- percentages;
- difficulty/runtime tuning;
- values that appear mutable but may be engine-specialized.

### FLAG

- boolean state encoded through strategic numbers or other channels;
- attack/retreat/production/escrow flags;
- initialization and reset semantics.

### TIMER

- timer IDs;
- timer activation/deactivation;
- timer status reads;
- timer-driven transitions.

### GROUP

- military groups;
- scout/exploration groups;
- temporary selection groups;
- ownership and destruction/reuse semantics.

### ESCROW / RESOURCE STATE

- reservation state;
- escrow percentages;
- committed resources;
- release conditions;
- interaction with feasibility guards.

### SCRATCH / INDEX STATE

- temporary goals;
- selected-unit indices;
- temporary distances;
- temporary points/coordinates;
- midpoint and candidate-selection state.

### ENGINE OBSERVATION STATE

- FactIds;
- ObjectData;
- search results;
- object IDs;
- target IDs;
- terrain/search outputs.

## 5. Immediate unresolved cells

The next machine pass must determine, for every AEGIS-relevant mutable symbol:

1. whether it is actually active in the target effective program;
2. declaration and first initialization site;
3. every write site;
4. every read site;
5. every guard that gives the value authority;
6. every reset/clear site;
7. whether the value survives rule passes, age transitions, production cycles, attack cycles, or death;
8. whether multiple subsystems intentionally share it;
9. whether ownership is stock-global, subsystem-local, engine-owned, or scratch-local;
10. whether AEGIS should preserve, replace, observe, or eliminate the channel.

## 6. Required output format

The final ledger should be generated from the existing stock symbol inventory and source corpus rather than manually copied into prose. Manual seed entries are useful for orientation only.

The final artifact should support queries such as:

- “Who can write this state?”
- “Who resets it?”
- “What guard gives this state authority?”
- “What downstream behavior changes when it changes?”
- “Is this engine state or controller state?”
- “Can AEGIS safely own an equivalent channel?”
- “What runtime experiment is required to resolve the remaining ambiguity?”

## 7. Gate decision

**R2 gate: NOT CLEARED.**

The architecture is not blocked because the complete matrix is missing today; it is blocked from final ABI allocation because ownership/lifetime collisions remain possible.

Do not allocate AEGIS state channels from apparent numeric vacancies until this ledger and R3 are closed.

## Evidence basis

- `_local_stock_audit_2026-09-06/symbol_inventory.jsonl`
- `_local_stock_audit_2026-09-06/goal_reference_inventory.jsonl`
- `docs/architecture/AEGIS_STOCK_SUBSYSTEM_RECONSTRUCTION_MAP_2026-09-08.md`
- `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`
- historical Pass 9–13 archaeology and associated QC documents

## Anti-regression rule

Do not create subsystem-specific “state maps” that silently become authoritative. This ledger is the canonical ownership surface; future subsystem documents should link to it and add evidence, not fork competing ownership tables.
