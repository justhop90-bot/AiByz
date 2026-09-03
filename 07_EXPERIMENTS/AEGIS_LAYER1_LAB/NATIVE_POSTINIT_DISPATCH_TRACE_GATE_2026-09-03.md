# AEGIS Layer 1 — Native Post-Init Dispatch Trace Gate — 2026-09-03

## Question
Can the exact retail executable's post-init regression options be traced beyond the option/string table into a concrete callable dispatch target?

## Build / controls
- AoE2DE_s.exe build 101.103.48987.0.
- SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
- Read-only executable archaeology.
- No binary modification, injection, hooks, debugger attachment, memory modification, arbitrary UDP, or unverified regression execution.
- Pure `.per` architecture unchanged; XS not used.

## Static evidence recovered
The executable contains a post-init tool table with `RUN_REGRESSION_TEST`, `EXIT_AFTER_POST_INIT_TOOLS`, and `TOOL_MANAGER_LOG_LOCATION`.

`RUN_REGRESSION_TEST` occurs in a native regression-tool string cluster containing the description that it runs a specific regression test and takes that test's regression directory. The same cluster contains `RegressionTest.cpp` source provenance, `RegressionTests\\SaveFiles\\*`, `RegressionTests\\SaveFiles\\%s\\%s`, `RegressionTests\\temp\\%s`, `Running regression tests '%s'`, `No regression tests found`, `Creating scenario server...`, and `Started game ok...`.

The general launch-option table separately contains `SCRIPT`, `TEST_HARNESS_COMM`, `SCRIPTREPORT`, and `SESSIONID`. This continues to support separate FTS/test-harness and post-init regression entry surfaces unless a code-level relationship is demonstrated.

## Trace attempt
A targeted IDA batch-analysis probe was prepared against the exact executable to locate the option strings, their data references, containing functions, and local instruction neighborhoods. The installed environment exposes `IDA Free 9.4`, but the non-interactive batch invocation did not produce the expected analysis/output artifact. No callable address or control-flow edge was therefore accepted from this attempt.

This is an instrumentation limitation, not a negative finding about the executable. The static string evidence remains valid; the desired code-level trace remains open.

## Current causal model
`post-init option parser -> RUN_REGRESSION_TEST argument -> regression runner -> specific regression directory -> SaveFiles/temp -> scenario server -> game`

The first and last portions are structurally evidenced, but the arrows between them are not all code-traced. In particular, no exact function address, argument register/stack contract, registration table, or factory dispatch has been established.

## Disposition
- Post-init regression option surface: CONFIRMED.
- Specific-test directory concept: CONFIRMED.
- Regression subsystem attribution: STRONGLY CONFIRMED structurally.
- Scenario-server component: CONFIRMED structurally.
- Code-level dispatch target: NOT ESTABLISHED.
- Argument ABI/grammar: NOT ESTABLISHED.
- Test registration/factory: NOT ESTABLISHED.
- End-to-end regression invocation: NOT ESTABLISHED.
- AI causal observation: NOT ESTABLISHED.
- Layer 1 promotion: NONE.
- Layer 1 remains 89%.

## Next discriminating test
Use an interactive IDA database or equivalent PE-aware disassembly workflow to resolve xrefs from `RUN_REGRESSION_TEST` and `EXIT_AFTER_POST_INIT_TOOLS`, then identify the post-init tool dispatch function and its regression-test argument contract. Do not execute a guessed regression test until that contract is closed.
