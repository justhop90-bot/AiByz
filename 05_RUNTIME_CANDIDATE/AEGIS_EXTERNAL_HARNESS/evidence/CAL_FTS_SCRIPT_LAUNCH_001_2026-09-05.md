# CAL_FTS_SCRIPT_LAUNCH_001 — Retail SCRIPT/FTS Probe

## Disposition

**NOT QUALIFIED.** The retail executable accepted the supplied command line and remained alive, but no FTS report or test-harness listener was observed.

## Target

- AoE2DE executable: `AoE2DE_s.exe`
- Build: `101.103.48987.0`
- Steam BuildID: `24094652`
- Probe script: `resources\\_common\\ai\\testharness\\scripts\\AEGIS_FTS_CAL_001.fts`
- Expected report: `FTS_PROBE_REPORT_001.txt`

## Invocation

The executable was launched directly with:

`SKIPINTRO SCRIPT="...\\AEGIS_FTS_CAL_001.fts" SCRIPTREPORT="...\\FTS_PROBE_REPORT_001.txt" RUNNING_AUTOTEST`

The process remained alive for the controlled observation window.

## Runtime observations

- Game process PID: `2548`
- Ordinary game UDP socket observed: `0.0.0.0:9999`
- Additional UDP endpoint observed for the process: ephemeral local port `55300`; no listener appeared on the previously targeted test-harness port `27015`.
- Requested `SCRIPTREPORT` file was not created.
- No FTS report content was recovered.
- The process was terminated after the observation window.

## Interpretation

This probe establishes only that the launch arguments can be passed to the retail executable without immediate process failure. It does **not** establish that `SCRIPT`, `SCRIPTREPORT`, or `RUNNING_AUTOTEST` activate the internal FTS controller in this retail build.

The existing harness finding therefore remains unchanged:

> Embedded capability != enabled capability != externally invocable capability.

## Consequence for P0

The scalar-goal smoke test remains **RUNTIME UNKNOWN**. Static legality and closure are established; a valid controlled AI execution path is still required before a runtime verdict can be issued.

## Evidence class

`MACHINE_OBSERVED / RETAIL_RUNTIME / NEGATIVE_QUALIFICATION`
