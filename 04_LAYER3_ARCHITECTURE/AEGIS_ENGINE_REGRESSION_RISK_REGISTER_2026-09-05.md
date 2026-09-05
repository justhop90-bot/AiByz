# AEGIS — AoE2DE Engine Regression Risk Register

**Date:** 2026-09-05  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Why this exists

AoE2DE AI semantics are not static. Official updates have repeatedly changed or corrected AI scripting behavior, including search stacking, focus/target facts, pending-object visibility, object-data behavior, and exploration commands. Official Update 177723 is a particularly clear example of target-level AI behavior being corrected in the engine itself.

## Risk classes

### R1 — Build drift
A game update changes a primitive's semantics while the AEGIS architecture remains unchanged.

**Control:** executable fingerprint + mandatory regression suite.

### R2 — Validator drift
A validator accepts or rejects a construct differently from the installed engine.

**Control:** validator result and runtime result are separate evidence fields.

### R3 — Search semantic drift
Filter stacking, search reset, pending visibility, multiplicity, or zero-result behavior changes.

**Control:** re-run search isolation and absence tests after build changes.

### R4 — Object-data drift
Object-data fields change semantics or edge-case behavior.

**Control:** qualify exact field usage, not merely field IDs.

### R5 — Typed-identity drift
A unit, unit-line, class, action, goal, or other typed identifier changes accepted inputs or interpretation.

**Control:** typed ABI registry with build scope.

### R6 — Lifecycle drift
Command, queue, pending, creation, availability, or cancellation transitions change.

**Control:** explicit lifecycle experiments.

### R7 — Performance drift
A primitive remains semantically correct but becomes materially more expensive.

**Control:** measured runtime budgets and regression thresholds.

## Mandatory response to a build change

1. Record new executable fingerprint.
2. Re-run Q-01.
3. Re-run all P1 semantic gates touched by changed engine behavior.
4. Re-run the minimal vertical-slice smoke qualification.
5. Do not silently carry old runtime qualification forward.

## Principle

**Architecture may survive an engine update. Machine qualification does not automatically survive it.**
