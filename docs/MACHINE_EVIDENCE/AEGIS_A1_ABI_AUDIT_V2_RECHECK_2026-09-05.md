# AEGIS A1 — ABI Audit v2 Recheck / Counting Defect Correction

**Date:** 2026-09-05  
**Evidence class:** A1 exact installed target package/build  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`  
**Status:** VERIFIED RECHECK — COUNTING IMPLEMENTATION CORRECTED

## 1. Trigger

A cross-artifact QC pass found a discrepancy between the deterministic v2 audit and the typed census:

- prior v2 audit: 5,259 declaration rows / 4,892 numeric declarations / 5,490 resolved goal operands;
- typed census: 5,260 declaration rows / 4,893 numeric declarations.

The discrepancy was investigated against the untouched stock four-file closure.

## 2. Root cause

The v2 audit used `re.search()` for `defconst` and goal-operation extraction, so it captured at most one matching form per physical source line.

The stock file contains a concrete counterexample at `Promisory/defaultConstants.per:99`:

`(defconst gate-descending-open 91);(defconst gate-descending-open 99)`

The typed census records both declarations. The audit recorded only the first.

The same single-match defect existed in the goal-operation regex. Seven stock lines contain two audited goal operations on one physical line, so seven goal operands were previously omitted.
## 3. Corrected implementation

`tools/aegis_abi_audit_v2.py` now uses `finditer()` for both declaration and goal-operation extraction.

The script was rerun directly against:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

No stock AI file was modified.

## 4. Corrected result

The exact four-file closure now reports:

- closure files: **4**;
- declaration rows: **5,260**;
- unique symbols: **1,480**;
- numeric declarations: **4,893**;
- resolved goal operands: **5,497**;
- resolved high goal operands `512–16,000`: **0**.

The corrected declaration count exactly matches the typed census.

## 5. Interpretation

The seven additional goal operands are real source operations, not new ABI channels. Their recovery improves audit completeness only.

The important conclusion remains unchanged: no resolved high numeric operand was found in the audited goal-typed command families.

This does **not** clear `10000–10015` for AEGIS allocation. Validator, target-build legality, ownership, generation, publication, and runtime gates remain mandatory.

## 6. Engineering disposition

- Previous v2 count: **superseded** for declaration/goal-operation totals.
- Corrected audit implementation: **active**.
- Stock package: **unchanged**.
- Numeric ABI allocation: **still blocked**.
- Audit lesson: source-line cardinality must not be confused with declaration/operation cardinality.
