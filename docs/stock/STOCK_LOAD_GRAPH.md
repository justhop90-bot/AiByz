# Stock Load Graph — A1 reconstruction index

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652

The exact restored stock tree is external A1 evidence. This document records the currently verified normal-HD closure and distinguishes it from the much larger Promisory source substrate used for archaeology.

## Verified normal-HD entry closure

`AI (HD version).per`
→ `Promisory/defaultConstants.per`
→ `Promisory/finalingConstants.per`
→ `Promisory/finaling.per`

The 2026-09-05 machine capture reports no further loads from those four files.

## Full Promisory archaeology boundary

The restored stock package contains a substantially larger Promisory tree, including systems such as:

`buildings`, `boarhunting`, `const`, `customConstants`, `dawn`, `escrow`, `gatherers`, `general`, `init`, `interaction`, `orb`, `researches`, `scoutcontrol`, `threats`, `trade`, `tsa`, `units`, `watercontrol`.

These names are topology evidence. They do not by themselves establish runtime load order or subsystem semantics.

## Reconstruction rule

The final AEGIS runtime will not depend on stock Promisory merely because the stock package loads it. Each required capability must be rehosted/reimplemented under explicit AEGIS ownership after deconstruction.

## Authoritative machine records

- `docs/MACHINE_EVIDENCE/AEGIS_A1_STOCK_MANIFEST_2026-09-05.jsonl`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_LOAD_CLOSURE_2026-09-05.json`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_RUNTIME_TOPOLOGY_2026-09-05.json`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_TYPED_STATE_CENSUS_2026-09-05.json`
- `docs/MACHINE_EVIDENCE/AEGIS_A1_STATE_CHANNEL_COLLISION_MAP_2026-09-05.json`
