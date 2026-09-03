# AEGIS Native Startup Calibration â€” 2026-09-03

## Status
INFRASTRUCTURE TEST â€” TIMEOUT / NO CAUSAL PROMOTION

## Question
Can the exact verified AoE2DE executable be launched through the hardened AEGIS runtime boundary without modifying the game installation?

## Controlled build
- Executable: `AoE2DE_s.exe`
- Build: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

## Procedure
1. Verified executable SHA-256 immediately before launch.
2. Used the hardened runtime controller with `shell=False` and explicit argv.
3. Used isolated lab run root: `07_EXPERIMENTS/AEGIS_LAYER1_LAB/runs/NATIVE_STARTUP_CAL_001`.
4. Passed only `SKIPINTRO`; no injection, hooks, debugger, memory modification, or XS facility was used.
5. Enforced a 20-second positive timeout.
6. Captured stdout/stderr as raw artifacts.
7. After timeout, the child was killed and reaped.
8. Verified PID 3876 no longer existed.

## Raw observation
- Runtime result: `status=timeout`
- PID: `3876`
- Return code after enforced termination: `1`
- Duration: `20.177275099791586 s`
- stdout: empty
- stderr: empty
- post-reap process check: no matching PID

## Interpretation
The hardened runtime successfully exercised its launch, containment, timeout, kill, and reap path against the exact verified executable. The process did not terminate naturally within 20 seconds. Because stdout/stderr were empty and no native UI/state observation was captured, this result does **not** establish successful game initialization, scenario loading, AI loading, or any game-state fact. Return code `1` is attributed only to the enforced termination path unless independent evidence establishes otherwise.

## Competing hypotheses
- H1: executable reached a running/UI state but emitted no console output.
- H2: executable stalled during initialization.
- H3: executable awaited GUI/Steam/display interaction not represented in stdout/stderr.
- H4: executable failed internally before producing console output.
The current observation does not discriminate these hypotheses.

## Security disposition
PASS for the tested runtime boundary; no violation observed. The timeout path correctly terminated and reaped the child. No game-installation write destination was used.

## Scientific disposition
No native-load claim. No P0-A claim. No Layer 1 promotion. Layer 1 remains 89%.

## Next discriminating test
Establish a controlled GUI/native lifecycle observation path for the fixture, while preserving the same executable digest, isolated output root, no-injection rule, timeout/reap rule, and explicit provenance. The scenario fixture must remain external to the installed AI tree and must contain zero XS script-call elements.
