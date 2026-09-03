# AEGIS Layer 1 — Native Test-Harness Dispatch Gate — 2026-09-03

## Question
Can the exact retail executable's native test-harness command surface be narrowed from generic socket infrastructure to a concrete script/test dispatch model?

## Build / controls
- AoE2DE_s.exe build 101.103.48987.0.
- Previously verified SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
- Read-only executable archaeology; no binary modification.
- No arbitrary UDP packets sent.
- Pure .per architecture unchanged; XS not used.

## Findings
The executable contains the AI commands `up-testharness-test` and `up-testharness-report`, plus `fe-testharness-message` and `fe-testharness-log-seed`.

The executable also contains an explicit native FTS-style test-script parser surface. Error strings identify tokens including `WAIT`, `EXECUTE`, `SET`, `GET`, `GOTOIF`, `REPORT`, `FPS_CHECK`, and `MEMORY_LEAK_CHECK`. The parser has event-task timeout forms using `WAIT EVENTTASK TIMEOUTFAIL <number>` or `TIMEOUTCONTINUE <number>`.

The parser has an explicit script-file resolution path: `failed to find call script file '%s'`, `failed to setup script '%s'`, and multiple `Parsing script '%s'` diagnostics. This is stronger evidence than the previously known `SCRIPT` command-line label alone.

The executable contains `SCRIPT` with description `Script to run`, `SCRIPTREPORT` with description `Script report outputfile`, and `TEST_HARNESS_COMM` with description `Enable Test Harness socket communication - Test name as ID`. `TEST_HARNESS_ADDRESS` is also present and defaults to `127.0.0.1:27015` in the native message surface.

The executable contains native controller/object vocabulary for `AITestEventController`, `GameTestEventController`, `TimerTestEventController`, `UITestEventController`, `DiagnosticInformationEventController`, `FPSEventController`, `WorldObject`, `PlayerObject`, `UnitObject`, `UnitListObject`, `GameOptionsObject`, and `MapObject`.

The executable also contains `TESTHARNESS_SCRIPTS`, `TESTHARNESS_REPORTS`, `TESTHARNESS_REG_SAVES`, `TESTHARNESS_XS`, and `TESTHARNESS_XS_SCRIPTS`, plus `testharness\\scripts\\`, `testharness\\reports\\`, and `testharness\\regressionsaves\\` storage names.

## Stock corpus check
The installed stock AI and gamedata text corpus contains no occurrences of the four test-harness AI commands. Therefore stock `.per` usage does not currently provide a ready-made invocation example.

## Controlled parser-resolution probes
Two minimal user-profile FTS files containing an intentionally invalid token were created temporarily under the profile test-harness scripts path and removed after execution. Direct retail launches were performed with `RUNNING_AUTOTEST` and `SCRIPT=<file>`.

No machine-readable parser diagnostic or report artifact was captured by these probes. Therefore script-path resolution and parser execution are NOT promoted. The probe is retained as a negative result showing that `SCRIPT` alone is insufficient to establish the dispatch path under the current invocation.

## Revised model
The evidence now supports the following architecture as a working hypothesis, not a proven causal chain:

`SCRIPT / TEST_HARNESS_COMM -> test/script resolution -> FTS parser -> event/controller dispatch -> game/AI/UI observation -> SCRIPTREPORT / harness report`.

The native presence of both FTS parser diagnostics and specialized test controllers makes this hypothesis materially stronger than the earlier UDP-only model.

## Competing hypotheses
- H1: `SCRIPT` selects a native FTS script and the script itself controls event-controller execution.
- H2: `TEST_HARNESS_COMM` selects a registered test by name, while `SCRIPT` is a separate automation layer.
- H3: both are developer-facing entry paths and retail invocation requires a hidden prerequisite or test-server state.
- H4: the test script is resolved from a storage point not yet identified by our profile-path assumption.

## Next discriminating pass
1. Reconstruct the native FTS grammar from token/error neighborhoods without executing arbitrary commands.
2. Identify exact storage-point resolution for `TESTHARNESS_SCRIPTS` versus ordinary profile paths.
3. Search the executable for `CALL`, `WAIT`, `EVENTTASK`, `EXECUTE`, and controller-name neighborhoods to reconstruct the smallest valid script grammar.
4. Locate native references around `SCRIPTREPORT` and `TEST_HARNESS_COMM` using the existing disassembly workflow.
5. Only after a concrete grammar/path contract is evidenced, run one minimal valid FTS script that performs a harmless timer or diagnostic observation.

## Disposition
- Native test-harness subsystem: CONFIRMED.
- Native FTS-style parser surface: CONFIRMED.
- Native test-controller model: CONFIRMED.
- Concrete test dispatch contract: NOT ESTABLISHED.
- Concrete script storage path: NOT ESTABLISHED.
- Valid FTS script execution: NOT ESTABLISHED.
- AI causal observation: NOT ESTABLISHED.
- Layer 1 promotion: NONE.
- Layer 1 remains 89%.
