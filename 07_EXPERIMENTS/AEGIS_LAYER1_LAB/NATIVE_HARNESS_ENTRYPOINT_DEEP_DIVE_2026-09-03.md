# Native Harness Entrypoint Deep Dive — 2026-09-03

## Executive finding
The strongest new result is a boundary correction: the presence of SCRIPT, SCRIPTREPORT, TEST_HARNESS_COMM, SESSIONID, RUNNING_AUTOTEST, and regression options in the retail executable does not establish that those launch options are active entry points in this retail build.

## Question
Why do deliberately malformed SCRIPT and test-harness invocations produce no parser or harness diagnostic, despite the executable containing the relevant parser and controller vocabulary?

## Evidence before
- Exact controlled executable: AoE2DE_s.exe, version 101.103.48987.0, game build #180059, Steam Build ID 24094652, SHA-256 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
- Native executable contains SCRIPT, SCRIPTREPORT, TEST_HARNESS_COMM, SESSIONID, RUNNING_AUTOTEST, FTS grammar, test controllers, and test-harness storage points.
- Native executable contains Post-Init Tools, RUN_REGRESSION_TEST, RUN_REGRESSION_TESTS, EXIT_AFTER_POST_INIT_TOOLS, and Tool Manager strings.

## New controlled observations
1. Minimal FTS probe `WAIT 1 / REPORT AEGIS_*` supplied through SCRIPT produced no report and no inspected FTS parser diagnostic.
2. Variants using plain, dash-prefixed, and split command-line forms produced no report or parser diagnostic.
3. Missing SCRIPT filename, missing TEST_HARNESS_COMM test identity, communication-only plus SESSIONID, and explicit testharness/scripts path forms produced no parser diagnostic.
4. `EXIT_AFTER_POST_INIT_TOOLS` plus nonexistent regression test/test-set names produced no tool-manager report artifact.
5. Deliberately malformed/absent inputs therefore failed to produce the expected negative diagnostic signal.

## Critical interpretation correction
A launch-option string is an interface declaration, not proof of an executable path from command-line parsing to subsystem dispatch. The option may be dormant, build-gated, consumed only in a different lifecycle, or merely configure a subsystem that requires another native trigger.

The public third-party launch-option reference lists SCRIPT, SCRIPTREPORT, SESSIONID, TEST_HARNESS_COMM and RUNNING_AUTOTEST, but does not establish that these options execute in every release build. It also warns that many options do not operate in release builds. This is corroboration only; native evidence remains primary.

## Competing hypotheses
H1: SCRIPT is an active retail entry point but requires a missing prerequisite/state transition.
H2: SCRIPT is present in the retail binary but its dispatch is build/configuration gated or dormant.
H3: SCRIPT configures an automation client/test session rather than directly launching FTS.
H4: FTS is primarily reached by the native regression/test runner, not ordinary command-line SCRIPT dispatch.
H5: The parser is shipped for internal tooling while the retail executable does not expose the full developer invocation path.

## Discriminating consequence
The next investigation must recover the option-consumption code and its gating conditions, rather than try additional filename/path variants.

Priority trace:
command-line option registry -> option parser -> SCRIPT/TEST_HARNESS_COMM storage -> gating predicate -> Tool Manager/test runner -> FTS parser.

For regression:
RUN_REGRESSION_TEST -> post-init tool dispatch -> regression directory resolution -> scenario server.

## Intuition-driven insight
The obvious thing we were missing was to ask whether we were trying to operate a *tool interface* that is actually dormant in the retail configuration. We had proven that the machine contains the workshop; we had not proven that the public build exposes the workshop door.

The absence of expected failure diagnostics from deliberately bad inputs is now positive evidence against the simple direct-entry model, though not proof of dormancy.

## Security
No executable modification, DLL injection, hooks, debugger attachment, memory modification, arbitrary UDP protocol guessing, or installed AI corpus modification was performed. Test files were disposable and isolated.

## Promotion
No Layer 1 causal promotion. Harness architecture evidence remains confirmed; exact retail entry protocol remains unestablished.

## Next gate
Recover the native launch-option registry/dispatch path and identify whether SCRIPT/TEST_HARNESS_COMM have a retail-build gate. If they are gated, pivot to the native regression/test-runner entry path and determine whether it is active in the same build.

Layer 1 remains exactly 89%.
