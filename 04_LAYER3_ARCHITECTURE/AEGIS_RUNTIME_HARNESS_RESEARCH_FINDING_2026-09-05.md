# AEGIS — Runtime Harness Research Finding

**Date:** 2026-09-05  
**Status:** VERIFIED PRESENCE / SEMANTICS UNKNOWN

## Direct workstation evidence

The installed AoE2DE tree contains exactly two copies of the discovered calibration script:

- `resources\_common\ai\testharness\scripts\AEGIS_FTS_CAL_001.fts`
- `testharness\scripts\AEGIS_FTS_CAL_001.fts`

Both files contain exactly:

`WAIT 1`

`REPORT AEGIS_FTS_CAL_001`

The normal `testharness` directory contains no additional files beyond this script.

## Tooling finding

The stock AI tree contains `AoE2ScenarioParser-master\...\xs-check\xs-check.exe`, version `0.2.29`. It is an XS linter, not evidence of a PER runtime harness.

## Engineering conclusion

The calibration script's presence is verified. Its invocation mechanism, report transport, result persistence, scenario binding, and relationship to the current executable remain UNKNOWN.

Therefore no runtime claim is made from the harness artifact alone.

## Next investigation

The correct next step is to identify the engine/editor invocation surface for `.fts` scripts through controlled process/file/log inspection, rather than guessing from the script syntax.
