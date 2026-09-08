# CAL_BUILD_001 — Retail Build Calibration

Status: **PASS_BUILD_IDENTITY / OBSERVED_RUNTIME_LIFECYCLE**

## Target

Executable:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`

Expected build:
- Version: `101.103.48987.0`
- Steam Build ID: `24094652`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

Observed executable size: `71,648,568` bytes

Observed SHA-256 exactly matched the expected fingerprint.

## Retail launch observation

Launch argument:
`-SKIPINTRO`

Observation window: `20` seconds

Expected process state: `running_at_timeout`

Observed result:
- process remained alive through the observation window;
- supervisor terminated it after the observation window;
- no embedded `TEST_HARNESS_COMM` or `TEST_HARNESS_ADDRESS` controls were used;
- no injection, hooks, memory writes, executable patching, or debugger attachment were used.

## Harness correction discovered during calibration

The first harness implementation classified any timeout as `FAIL_RUNTIME_BEHAVIOR`. That was semantically incorrect for a game process whose expected state is to remain running during the observation window.

The harness was corrected to distinguish:

- `expected_process_state = running_at_timeout`
- `expected_process_state = exited`

A timeout is now an expected lifecycle observation when the manifest explicitly declares `running_at_timeout`.

This correction is itself a useful harness-QC result: **supervisor timeout is not equivalent to runtime failure.**

## Verdict

`OBSERVED_WITH_LIMITATIONS`

The build identity is confirmed for this machine at the time of the run. The launch lifecycle is observed. No semantic game-state claim is made from this experiment.

Next qualification target: acquire and normalize replay evidence from a controlled run, then correlate replay events with independently observable lifecycle markers.
