# AEGIS Native Test-Harness Activation Gate — 2026-09-03

## Status
Layer 1 remains 89%. No causal proposition promoted.
Pure `.per` architecture remains unchanged. XS is excluded.

## Question
Can the retail build's native test-harness communication path be activated or observed safely enough to become the deterministic experiment entry channel?

## Prior evidence
The exact verified AoE2DE_s.exe contains TESTHARNESS paths, TEST_HARNESS_COMM, TEST_HARNESS_ADDRESS,
SCRIPTREPORT, SESSIONID, RUNNING_AUTOTEST, and up-testharness-test/report plus FE test-harness commands.
The executable identifies the default harness address as 127.0.0.1:27015.
The user profile contains testharness/regressionsaves and testharness/reports directories, but no files.

## Controlled setup
Build: 101.103.48987.0.
SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
Direct executable launch only; no Steam-mediated launch.
Run root: isolated AEGIS Layer 1 lab run directory.
Loopback UDP listener: 127.0.0.1:27015 only.
No external listener, injection, hooks, debugger, memory modification, or process modification.

## Activation probe
Launch options included TEST_HARNESS_COMM=AEGIS_HARNESS_003,
TEST_HARNESS_ADDRESS=127.0.0.1:27015, SESSIONID=AEGIS_SESSION_003,
RUNNING_AUTOTEST, AIDEBUGGING, AISCRIPTDEBUGGING, LOGSYSTEMS=AIScript,
CONSTANTLOGGING, NOMODS, WINDOW, SKIPINTRO, and bounded EXIT=25.
The game was allowed 28 seconds; the process then terminated/was forcibly stopped by the harness wrapper if necessary.

## Raw observations
MainLog recorded the exact launch options, AIScript logging, SyncAI logging, and normal native initialization.
The native build logged Steam initialization and repeated unrelated rlink SSL-context errors.
No UDP datagrams were received on 127.0.0.1:27015.
No files appeared under the user testharness directory's regressionsaves or reports directories.
No SCRIPTREPORT artifact was produced.
The wrapper observed GAME_PID=18508, EXITED=True, CODE=-1.

## Interpretation
The command-line controls are accepted as launch options and the executable reaches native initialization.
This does NOT establish that the test-harness communication service was listening, that the supplied test name
was resolved, that a client handshake was attempted, or that a test was executed.
Zero UDP traffic is therefore an activation-negative observation, not proof that the harness is absent or broken.
The absent report and absent regression artifacts likewise do not identify the missing activation condition.

The strongest new finding is structural: the retail executable has a first-class test-harness filesystem namespace,
command-line controls, native UDP initialization code/message, test-harness AI commands, and an automation-test mode.
The user's existing profile also has the expected reports/regressionsaves directories, although currently empty.

## Competing hypotheses
H1: TEST_HARNESS_COMM requires a specific internal test name/script before communication starts.
H2: TEST_HARNESS_COMM opens only after a particular game/test state is entered.
H3: The UDP endpoint is client-driven and requires an external handshake packet.
H4: RUNNING_AUTOTEST is a prerequisite but does not itself select a test.
H5: SESSIONID identifies an already-running client session rather than initiating one.
H6: The retail build contains the infrastructure but this invocation path is not exposed without additional test assets.

## Next discriminating work
Do not guess a UDP protocol or send arbitrary packets to the executable.
Prefer read-only archaeology of the shipped test-harness asset namespace and exact command/event vocabulary.
If a native test asset can be identified from installed/user files or authoritative public evidence, reproduce its
minimum invocation with the same security gates. Otherwise investigate the relationship among SCRIPT,
TEST_HARNESS_COMM, RUNNING_AUTOTEST, SESSIONID, SCRIPTREPORT, and the up-testharness commands using controlled
one-variable-at-a-time launches.

## Safety and security disposition
PASS: exact executable identity check.
PASS: direct executable route; Steam launch options excluded.
PASS: loopback-only observation endpoint.
PASS: bounded runtime and cleanup.
PASS: no game-installation modification.
PASS: no user Steam configuration modification.
PASS: no code injection, hooks, debugger, memory patching, or process modification.
PASS: parser remains outside runtime.
PASS: pure `.per` architecture preserved.
FAIL CLOSED: no causal experiment permitted from this gate.

## Promotion decision
No Layer 1 claim promoted. No percentage change.
This gate advances infrastructure knowledge only.
