# AEGIS Layer 1 — Native Test-Harness Asset Gate — 2026-09-03

## Question
Does the installed retail build ship discoverable test-harness scripts, regression saves, or report assets that can supply a real TEST_HARNESS_COMM test identity?

## Controls
- Exact executable: AoE2DE_s.exe build 101.103.48987.0.
- Previously verified SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
- Read-only archaeology only; no game-installation files modified.
- No arbitrary harness packets sent.
- Pure .per architecture unchanged; XS not used.

## Evidence
The executable contains the storage namespace symbols TESTHARNESS, TESTHARNESS_SCRIPTS, TESTHARNESS_REPORTS, TESTHARNESS_REG_SAVES, TESTHARNESS_XS and TESTHARNESS_XS_SCRIPTS. It also contains the launch options SCRIPT, TEST_HARNESS_COMM, SCRIPTREPORT, SESSIONID and RUNNING_AUTOTEST, plus up-testharness-test/report and the native UDP initialization message.

The live retail installation was recursively inspected for testharness/regression directories and for text/script assets. No installed directory named testharness or regression assets was found. The user's AoE2 profile was likewise inspected; no test-harness script or regression-save files were discovered in the searched roots.

Tools_Builds.zip was inspected as a ZIP archive for testharness, regression, .xs, .per, and script entries. No matching entries were returned.

## Interpretation
The native binary clearly contains a test-harness subsystem and storage-path vocabulary, but the current retail installation does not expose an obvious shipped test corpus in the inspected filesystem. Therefore the earlier hypothesis that a real local test asset could simply be selected remains unproven.

This materially changes the search strategy: the next high-value target is the executable's native command/asset resolution path, not blind filesystem hunting or invented UDP traffic.

## Competing hypotheses
H1: Test assets are downloaded/generated/created only in developer environments and are absent from retail.
H2: Assets are embedded in binary/resources or loaded through another package/archive namespace.
H3: TEST_HARNESS_COMM names an internal test registered in native code rather than a filesystem script.
H4: Test-harness activation requires a client/controller outside the game process and no shipped test corpus is required.

## Next discriminating work
1. Inspect executable resource/package metadata for testharness-related embedded names.
2. Map the native command-line option table around SCRIPT/TEST_HARNESS_COMM/SCRIPTREPORT/SESSIONID.
3. Trace static references to testharness::comm strings and native controller class names using targeted disassembly, without modifying the executable.
4. Inspect stock AI command semantics for up-testharness-test/report and identify whether a pure .per probe can establish test identity or reporting.
5. Only after native evidence identifies a valid invocation, run one minimal activation test.

## Disposition
- Test-harness infrastructure: CONFIRMED.
- Retail shipped test corpus: NOT FOUND in inspected locations.
- Real test identity: NOT ESTABLISHED.
- Protocol: NOT ESTABLISHED.
- Harness activation: NOT ESTABLISHED.
- Layer 1 promotion: NONE.
- Layer 1 remains 89%.
