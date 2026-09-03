# AEGIS Layer 1 — Native Dispatch / Regression Registration Gate — 2026-09-03

## Question
Can executable evidence identify how regression tests are named/registered and whether the command-line regression path is a direct bridge to scenario-server execution?

## Build / controls
- Exact AoE2DE_s.exe build 101.103.48987.0.
- SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
- Read-only binary archaeology only.
- No arbitrary regression invocation, binary modification, injection, hooks, debugger attachment, memory modification, or UDP packets.
- Pure `.per` architecture unchanged; XS not used.

## Findings
The exact executable contains a distinct command-line/tooling surface for regression execution. `RUN_REGRESSION_TESTS` is described as running regression tests on game data from previous versions; `RUN_REGRESSION_TEST` is described as running a specific regression test and taking the regression directory of a specific test.

The native regression string neighborhood contains `..\\RegressionTests\\SaveFiles\\*`, `..\\RegressionTests\\SaveFiles\\%s\\%s`, and `..\\RegressionTests\\temp\\%s`. It also contains `Running regression tests %s`, `No regression tests found`, `Creating scenario server...`, and `Started game ok...`.

The same neighborhood identifies native source provenance `Engine\\Tools\\Regression\\RegressionTest.cpp`, strengthening the attribution of this string cluster to a regression-test subsystem.

The command-line option cluster is separate from the AI test-harness command cluster: `SCRIPT`, `TEST_HARNESS_COMM`, `SCRIPTREPORT`, and `SESSIONID` appear in the general game option table, while the regression options appear with the post-init tool surface. This supports treating regression execution and FTS test-harness execution as distinct entry mechanisms until a call relationship is proven.

No literal test-name registry was identified in the inspected ASCII string neighborhoods. No shipped RegressionTests corpus was found in the inspected user roots. Therefore the evidence does not establish a concrete regression test identity or the exact accepted directory argument contract beyond the native description/path strings.

## Revised model
Regression path: `RUN_REGRESSION_TEST -> specific regression directory -> regression test machinery -> SaveFiles -> scenario server -> game`.

This is a working structural model, not a proven end-to-end causal chain. The string `Creating scenario server...` and `Started game ok...` establish that the regression subsystem contains scenario-server startup behavior; they do not prove that every regression test reaches that path.

FTS path remains separately modeled as `SCRIPT / TEST_HARNESS_COMM -> script resolution -> FTS parser -> test controllers`. No dispatch merge is promoted.

## Competing hypotheses
- H1: `RUN_REGRESSION_TEST` receives a named directory and directly invokes the regression test runner.
- H2: `RUN_REGRESSION_TEST` is a post-init tool selector whose actual test corpus and runner are external to the retail executable.
- H3: scenario-server creation is one regression-test component, not the universal execution path.
- H4: the retail executable contains tooling but requires developer-side RegressionTests assets not shipped in the inspected installation/profile.

## Next discriminating pass
1. Trace the post-init tool option handler around `RUN_REGRESSION_TEST` and `EXIT_AFTER_POST_INIT_TOOLS` using targeted disassembly.
2. Recover argument parsing/parameter boundaries from nearby strings and code references.
3. Search for `RegressionTest` registration/factory symbols and test-name tables.
4. Separately trace `SCRIPT`/`SCRIPTREPORT` option handling to determine the FTS storage-point root.
5. Only after dispatch contracts are closed, perform one harmless valid invocation.

## Disposition
- Regression option surface: CONFIRMED.
- Specific-test directory concept: CONFIRMED.
- Native regression subsystem attribution: STRONGLY CONFIRMED structurally.
- Scenario-server creation inside regression subsystem: CONFIRMED structurally.
- Concrete test-name registry: NOT FOUND.
- Exact accepted argument grammar: NOT ESTABLISHED.
- End-to-end regression invocation: NOT ESTABLISHED.
- AI causal observation: NOT ESTABLISHED.
- Layer 1 promotion: NONE.
- Layer 1 remains 89%.
