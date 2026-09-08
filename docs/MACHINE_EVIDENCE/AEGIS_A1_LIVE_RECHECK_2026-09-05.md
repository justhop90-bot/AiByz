# AEGIS A1 Live Stock Recheck — 2026-09-05

**Status:** PASS — restored stock tree matches captured A1 file inventory
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## 1. Purpose

Revalidate the restored stock AI tree after the earlier immutable capture.
The live tree was read only; no files were modified.

## 2. Executable identity

- Path: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- FileVersion/ProductVersion: `101.103.48987.0`
- Steam BuildID: `24094652`

## 3. Complete tree comparison

The live recursive tree contains **516 files**.
The prior A1 manifest contains **516 file records**.

Comparison used normalized relative paths and case-normalized SHA-256 values.

Result:

- missing files: **0**
- new files: **0**
- changed files: **0**

The apparent prior eight hash differences were hexadecimal case only; after normalization, all eight matched exactly.

## 4. Runtime import closure

The channel-aware ABI audit, executed directly against the live stock tree, resolves the selected entrypoint `AI (HD version).per` to **4 imported files**:

1. `AI (HD version).per`
2. `Promisory/defaultConstants.per`
3. `Promisory/finaling.per`
4. `Promisory/finalingConstants.per`

This is an **import closure**, not a statement that the other 512 files are absent. Physical presence and runtime reachability remain separate facts.

## 5. Corrected live ABI census

- declaration rows: **5,260**
- unique symbols: **1,480**
- numeric declarations: **4,893**
- resolved goal operands: **5,497**
- resolved high goal operands (512–16,000): **0**

The audit used the corrected `finditer()` extraction logic, which handles multiple declarations/goal operations on one physical line.

## 6. Engineering disposition

The authoritative A1 stock package is now independently revalidated at the file level.
The remaining ABI work is no longer package acquisition. It is semantic qualification: validator join, ownership, generation, publication, operation-specific legality, and controlled runtime behavior.

No production `.per` allocation is cleared by this report alone.
