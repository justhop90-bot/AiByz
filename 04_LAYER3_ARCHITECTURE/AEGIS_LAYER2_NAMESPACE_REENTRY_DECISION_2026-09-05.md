# AEGIS — Layer 2 Namespace Reentry Decision

**Date:** 2026-09-05  
**Status:** REVIEWED — NO REOPEN REQUIRED  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Trigger

Wave A acquisition found numeric `defconst` values of `10000` and `14000` for the conditional symbol `heavy-wood` in the stock HD entrypoint closure.

A naive numeric scan could have interpreted these as collisions with the AEGIS candidate goal namespace.

## 2. Reentry result

Layer 2 is **not reopened**.

The reason is that the corrected channel-aware audit distinguishes a numeric constant value from a goal identifier. The specialist scripting reference explicitly describes typed command parameters and the separate roles of `Defconst`, `Goal`, `Sn`, `ClassId`, `BuildingId`, and related types. citeturn3search5turn3search6

The corrected audit resolves operands specifically in goal-typed operations (`set-goal`, `goal`, `up-modify-goal`, `up-compare-goal`). It finds:

- 5,490 resolved goal operands;
- 0 resolved high goal operands in `512–16000`.

Therefore the Layer-2 conclusion remains valid in its original narrow form: the normal HD closure contains no resolved high goal identifier in the audited goal-operation positions.

## 3. What changed

The qualification methodology was strengthened:

**Before:** numeric declaration occupancy could be mistaken for channel occupancy.  
**Now:** ABI occupancy is evaluated by channel + parameter position + semantic type.

This is an improvement to the audit mechanism, not a relaxation of the namespace rule.

## 4. New invariant

> A numeric value is not an ABI collision unless the engine/validator interprets that value in the same semantic channel and parameter type relevant to the proposed allocation.

Examples:

`GOAL:10000 ≠ CONST-VALUE:10000`

unless a command context makes the latter a Goal parameter.

## 5. Layer-2 disposition

- Layer-2 architecture: **CLOSED**.
- Layer-2 namespace conclusion: **PRESERVED / NARROWED**.
- Numeric allocation: **still blocked** pending validator and target-build legality.
- Channel-aware audit: **required** for all future ABI collision decisions.

## 6. Engineering significance

This is exactly the type of adversarial result the qualification phase is supposed to produce. The process found a plausible collision, refused to promote it, traced the actual semantic type, corrected the audit, and preserved the stronger claim without weakening the safety boundary.
