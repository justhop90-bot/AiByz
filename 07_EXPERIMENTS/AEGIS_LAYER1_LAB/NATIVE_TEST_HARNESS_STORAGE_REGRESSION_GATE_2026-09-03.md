# AEGIS Layer 1 — Native Test-Harness Storage / Regression Gate — 2026-09-03

## Question
Can the exact retail executable narrow the test-harness storage model and identify a deterministic regression-test entry path?

## Build / controls
- AoE2DE_s.exe build 101.103.48987.0.
- SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
- Read-only executable archaeology.
- No binary modification, injection, hooks, debugger attachment, memory modification, or arbitrary UDP packets.
- Pure `.per` architecture unchanged; XS not used.

## Findings
The executable contains a native storage-point namespace including `TESTHARNESS`, `TESTHARNESS_SCRIPTS`, `TESTHARNESS_REPORTS`, and `TESTHARNESS_REG_SAVES`.

The same binary contains `StoragePointBase_t`, `StoragePoint_t`, `PathSpec`, `Base`, `Point`, and `Spec`, with source provenance `Engine\\FileSystem\\storagepoint.cpp`. This establishes a typed native storage abstraction rather than isolated directory strings.

The executable contains explicit relative paths `testharness\\`, `testharness\\scripts\\`, `testharness\\reports\\`, and `testharness\\regressionsaves\\`. These constrain the native harness topology, but do not alone prove the final OS-resolved root for each storage point.

The executable separately contains a native regression subsystem with `RUN_REGRESSION_TESTS` and `RUN_REGRESSION_TEST`. It contains `..\\RegressionTests\\SaveFiles\\*`, `..\\RegressionTests\\SaveFiles\\%s\\%s`, and `..\\RegressionTests\\temp\\%s`, plus messages including `Running regression tests`, `No regression tests found`, `Creating scenario server`, and `Started game ok`.

This is strong structural evidence for a native automated regression path that can create a scenario server. It is not yet proof that the retail executable accepts an arbitrary user-supplied regression test name or that the path can be safely adapted to our Layer 1 experiment corpus.

## Storage/path observation
A recursive search of the inspected user roots `C:\\Users\\justh\\Games\\Age of Empires 2`, `C:\\Users\\justh\\AppData\\Local`, and `C:\\Users\\justh\\AppData\\Roaming` found no actual test-harness script or RegressionTests corpus files.

The absence of a corpus is a negative environmental observation, not evidence that the native subsystem is absent. The executable itself contains the storage namespace and path vocabulary.

## Revised architecture hypothesis
`StoragePoint_t -> TESTHARNESS_SCRIPTS / TESTHARNESS_REPORTS / TESTHARNESS_REG_SAVES -> native filesystem resolution -> FTS / regression assets`.

Separately: `RUN_REGRESSION_TEST(S) -> RegressionTests\\SaveFiles -> scenario server -> game`.

The two paths are related candidates but have not been proven to share a dispatch entry point.

## Competing hypotheses
- H1: test-harness storage points resolve under the user profile testharness root and are consumed by FTS.
- H2: storage points resolve through another base/profile root selected by native configuration.
- H3: regression tests are an independent developer-tool path and do not use TESTHARNESS_SCRIPTS.
- H4: retail builds contain the runner but require an external regression corpus not shipped with the game.

## Discriminating next pass
1. Target the command-line option handler around `RUN_REGRESSION_TEST` and `RUN_REGRESSION_TESTS`.
2. Reconstruct the storage-point enum-to-path mapping around `StoragePoint_t` / `PathSpec` without executing unverified tests.
3. Search for registration tables or literal test names adjacent to regression dispatch.
4. Determine whether `SCRIPTREPORT`, `SCRIPT`, and `TEST_HARNESS_COMM` resolve through the same storage abstraction.
5. Only after a concrete contract is established, run one harmless native parser/regression calibration.

## Disposition
- Native test-harness storage namespace: CONFIRMED.
- Native harness relative-path topology: CONFIRMED.
- Typed storage-point abstraction: CONFIRMED.
- Native regression runner: CONFIRMED.
- Regression scenario-server path: CONFIRMED structurally.
- Actual storage-point OS resolution: NOT ESTABLISHED.
- Actual regression test identity/corpus: NOT ESTABLISHED.
- Valid regression invocation: NOT ESTABLISHED.
- AI causal observation: NOT ESTABLISHED.
- Layer 1 promotion: NONE.
- Layer 1 remains 89%.
