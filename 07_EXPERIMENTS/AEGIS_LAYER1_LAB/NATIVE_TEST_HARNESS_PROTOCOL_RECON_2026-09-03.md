# AEGIS Native Test-Harness Protocol Reconstruction — 2026-09-03

## Gate status
Layer 1: 89%. No causal promotion.
Pure `.per` architecture unchanged; XS remains excluded.

## Objective
Determine what the retail executable itself reveals about the relationship among SCRIPT,
TEST_HARNESS_COMM, SCRIPTREPORT, SESSIONID, RUNNING_AUTOTEST, and the test-harness asset namespace.

## Exact build
AoE2DE_s.exe 101.103.48987.0 (#180059).
SHA-256 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.

## Native string evidence
The executable's launch-option table describes TEST_HARNESS_COMM as:
"Enable Test Harness socket communication - Test name as ID".
SCRIPT is described as "Script to run".
SCRIPTREPORT is described as "Script report outputfile".
SESSIONID is described as "Session ID with which client script should join!".
The same launch-option region contains RUNNING_AUTOTEST, AIDEBUGGING, AISCRIPTDEBUGGING,
LOGAI, LOGUAI, LOGACTION, LOGMOVE, LOGEXPLORE, LOGWAYPOINT, SHOWUNITIDS and related diagnostics.
The executable also contains testharness script/report/regression-save path strings and
up-testharness-test, up-testharness-report, fe-testharness-message and fe-testharness-log-seed.

## Important interpretation
The phrase "Test name as ID" is materially stronger than our earlier generic assumption that
TEST_HARNESS_COMM merely enables a socket. It indicates that the option carries a test identity.
The phrase "Session ID with which client script should join" independently suggests a client/session
relationship rather than a one-way logging socket. This is still string-level native evidence,
not proof of the exact parser, handshake, or state machine.

## Activation attempt
A bounded direct-executable probe supplied TEST_HARNESS_COMM=AEGIS_HARNESS_003,
TEST_HARNESS_ADDRESS=127.0.0.1:27015, SESSIONID=AEGIS_SESSION_003 and RUNNING_AUTOTEST.
A loopback UDP listener was present before launch. No datagrams were received and no report artifact
was produced. MainLog confirmed the supplied options and reached native game initialization.

## New negative result
A test-harness activation attempt with an invented test identity does not demonstrate absence of the
service. The executable may require a real shipped test name/script, a script file, an external client,
a session handshake, or a specific startup state. We therefore reject the hypothesis that simply
setting TEST_HARNESS_COMM is sufficient to prove activation.

## Security disposition
Exact build identity verified before launch. Direct executable route used.
Loopback listener only. No arbitrary packets were sent to the game.
No injection, hooks, debugger, memory modification, executable modification, or Steam configuration changes.
Execution was bounded and the native process was cleaned up. Game-installation files were not modified.

## Next discriminating experiment
Do not guess the undocumented socket protocol. First search the installed/profile corpus and
repository/public evidence for actual test-harness script names, test reports, regression saves,
client scripts, or documented examples. If a genuine asset is found, run the smallest one-variable
activation test and capture both report and communication artifacts. Only then investigate protocol
messages. If no asset is found, use one-variable launches to discriminate SCRIPT versus
TEST_HARNESS_COMM versus RUNNING_AUTOTEST while preserving the same exact-build/security controls.

## Promotion decision
Infrastructure hypothesis strengthened: native test-harness infrastructure and named test/session
concepts are confirmed at executable-string level. Harness activation remains unresolved.
No Layer 1 percentage change.
