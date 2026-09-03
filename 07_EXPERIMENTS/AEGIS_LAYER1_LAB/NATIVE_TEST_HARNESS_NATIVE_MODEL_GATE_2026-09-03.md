# AEGIS Layer 1 — Native Test Harness Native Model Gate

Date: 2026-09-03
Build: AoE2DE 101.103.48987.0
Executable SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4
Status: structural/native-model archaeology only; no causal promotion

## Question
What can the exact retail executable tell us about the native test-harness object model and its activation contract?

## Method
Read-only analysis of the verified executable. Extracted printable native strings and MSVC RTTI/type-name strings associated with `testharness`, controller classes, command vocabulary, launch options, and test-harness paths. No binary modification, injection, hooks, debugger attachment, memory patching, or arbitrary socket traffic was used.

## Observations
The executable contains native RTTI/type names for `AITestEventController`, `GameTestEventController`, `TimerTestEventController`, `FPSEventController`, `DiagnosticInformationEventController`, `WPFGTestEventController`, `UITestEventController`, and `uiWidgetTestEventController`.

`GameTestEventController` is associated with native objects including `WorldObject`, `PlayerObject`, `UnitObject`, `UnitListObject`, `GameOptionsObject`, `MapObject`, and `MapStyleObject`.

`UITestEventController` is associated with `UIElementObject`, `SelectTaskProcessor`, `CheckTaskProcessor`, `WaitTask`, and `WaitForElementTask`. This indicates the harness is not merely a socket listener; it contains native game/UI test abstractions.

The executable exposes the AI command vocabulary `up-testharness-test`, `up-testharness-report`, `fe-testharness-message`, and `fe-testharness-log-seed`.

The executable defines launch-option text for `SCRIPT`, `TEST_HARNESS_COMM`, `SCRIPTREPORT`, and `SESSIONID`. The `TEST_HARNESS_COMM` description explicitly says: `Enable Test Harness socket communication - Test name as ID`. `SESSIONID` is described as a session ID with which a client script should join.

Native path strings include `testharness\\`, `testharness\\scripts\\`, `testharness\\reports\\`, `testharness\\regressionsaves\\`, and `testharness\\xs\\`.

The executable contains `127.0.0.1:27015` and the native message `testharness::comm::Init UDP socket initialized on address %s`, establishing a concrete loopback UDP communication path in the binary.

`RUNNING_AUTOTEST` is present with text explaining that code which may halt the game should be ignored because an automation test may not have human handling.

## Important correction
Earlier reasoning treated the absence of shipped test files as evidence that the harness might be developer-only. This pass does not establish that conclusion. The executable contains a substantially richer native test object model than a simple communication shim, while the expected filesystem asset namespace is absent from the inspected retail installation/profile. The correct status is therefore: native framework present; retail asset availability unresolved.

## Competing hypotheses
H1: retail executable contains framework plus external test assets not present in this installation.
H2: test definitions are embedded/registered in native code or packaged elsewhere.
H3: `TEST_HARNESS_COMM` selects a registered test by name and opens communication only in the context of that test.
H4: `SESSIONID` identifies a client joining an already-established harness session.
H5: `SCRIPT` and `SCRIPTREPORT` form a separate script/report execution path that can drive the same native event controllers.

No hypothesis is promoted beyond structural indication.

## Discriminating next tests
1. Identify native registration/lookup strings surrounding test names, script loaders, and event-controller dispatch.
2. Determine whether a test-name list or script manifest exists in shipped package/resource data rather than ordinary files.
3. Search the executable's native command/option tables for parameter syntax and relationships among `SCRIPT`, `TEST_HARNESS_COMM`, `SESSIONID`, and `SCRIPTREPORT`.
4. Only after identifying a real test identity or script contract, perform one-variable activation.
5. Keep arbitrary UDP packet generation prohibited until the protocol is evidenced.

## Evidence boundary
This report establishes native framework structure, not successful activation, scenario loading, `.per` execution, fact evaluation, or causal AI behavior.

## Promotion decision
Layer 1 remains 89%. No causal proposition promoted.

## Security adjudication
PASS: exact executable hash verified; read-only archaeology; no installation modification; no Steam configuration modification; no injection/hooks/debugger/memory modification; no arbitrary network packets.
