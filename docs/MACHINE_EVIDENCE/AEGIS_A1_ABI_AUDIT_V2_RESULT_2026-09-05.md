# AEGIS A1 — Channel-Aware ABI Audit v2 Result

**Date:** 2026-09-05  
**Evidence class:** A1 exact installed target package/build  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## Result

The deterministic channel-aware audit was executed against the exact normal HD AI closure:

- 4 closure files;
- 5,259 declaration rows;
- 1,480 unique symbols;
- 4,892 numeric declarations;
- 5,490 resolved goal operands;
- **0 resolved high goal operands in 512–16,000**.

## Critical correction

A raw numeric scan finds `heavy-wood` values of 10,000 and 14,000 in conditional `defconst` blocks. Those values are **not automatically goal-channel occupancy**. The audit was corrected to resolve identifiers according to the parameter position in which they are used.

This is consistent with the specialist scripting reference's typed parameter model: parameter types distinguish goals, strategic numbers, classes, buildings, defconsts, and other semantic domains. citeturn3search5turn3search6

## Exact evidence artifact

The complete deterministic v2 run exists locally on the authorized workstation:

`C:\Users\justh\AEGIS_A1_ABI_AUDIT_V2_2026-09-05\`

Run-manifest SHA records:

- `audit_report.md`: `6709df7b68f0aa64f7438688189d0c62978ec9575cec371d3b79b28f10ce1abc`
- `goal_reference_inventory.jsonl`: `277587947945a80fcbb723efa5ec9ef3b70338ca0bdbb9bfba49b6f6a4ac3074`
- `import_closure.json`: `60b37c78673c852acb7a4a7e8f13555ca2aa7ce47c454f2468c53a0e4ec1ac01`
- `snapshot_manifest.json`: `66eb2a9c7a6b1fc442cdc47a289aa58fed2a3bdece5e8fea4206761eff14016e`
- `symbol_inventory.jsonl`: `5c39ff4f994bed7ebe93dc009bd39af979d5d288ee18b928d289681c4fc33b0e`

## Disposition

This result **supports** the Layer-2 candidate namespace conclusion in the narrow goal-typed sense.

It does **not** clear numeric allocation. Engine legality, validator acceptance, ownership, generation, publication, and build-profile gates remain open.

The audit correction is itself a successful qualification outcome: the process caught a false collision before it could become an ABI allocation rule.
