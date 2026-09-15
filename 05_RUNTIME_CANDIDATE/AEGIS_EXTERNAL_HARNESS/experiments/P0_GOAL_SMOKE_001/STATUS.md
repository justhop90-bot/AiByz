# P0 Goal Smoke 001 — Status

**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652
**Status:** PACKAGE BUILT — RUNTIME UNKNOWN

## Objective

Test the exact scalar goal operations required for the first AEGIS allocation band using goals 10000 and 10001.

The test performs:

1. `set-goal aegis-p0-goal 12345`
2. `up-modify-goal aegis-p0-result c:= 0`
3. readback through `up-chat-data-to-self`
4. `up-compare-goal aegis-p0-goal = 12345`
5. PASS chat emission if comparison succeeds

## Static result

The disposable package has a five-file import closure: the four target-build source files plus the test module.

The corrected ABI audit resolves seven high goal operands, all attributable to the two test goals.
No stock high goal operand was found in the four-file target closure.

## Runtime result

**UNKNOWN.** The package has not yet been executed in a controlled match.

A static pass cannot establish engine legality or runtime state persistence.

## Required evidence

A controlled run must capture:

- exact build fingerprint;
- AI package hash/manifest;
- AI initialization success;
- emitted `AEGIS_P0_WRITE_READ` chat;
- emitted `AEGIS_P0_COMPARE PASS` chat;
- replay hash and parsed CHAT records;
- repeat-run consistency.

A missing chat message is not automatically a failed goal operation; it is an unresolved runtime observation until the lifecycle is adjudicated.

## 2026-09-05 runtime-path update

A direct retail launch was attempted with `SCRIPT`, `SCRIPTREPORT`, and `RUNNING_AUTOTEST` pointing at the discovered FTS calibration script. The game remained alive, but no requested report was produced and no qualified FTS listener appeared. See `../evidence/CAL_FTS_SCRIPT_LAUNCH_001_2026-09-05.md`.

This does not fail the P0 ABI hypothesis. It fails only the attempted external invocation path. P0 remains **RUNTIME UNKNOWN** pending a controlled way to execute the disposable AI package and capture its output.
