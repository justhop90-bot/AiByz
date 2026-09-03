# AEGIS Layer 1 — Native Test-Harness Archaeology Gate

**Date:** 2026-09-03
**Build:** 101.103.48987.0 / internal build 180059
**Executable:** AoE2DE_s.exe
**SHA-256:** 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4
**Layer 1 status:** 89%

## Question
Can the exact retail executable expose a native test/automation path capable of deterministic game entry and machine-readable observation, while preserving the AEGIS pure-.per architecture and security boundary?

## Prior evidence
- Native executable startup and main-menu UI are established.
- Native diagnostic logging is established.
- Deterministic custom-scenario loading is not established.
- Steam-mediated launches are contaminated by persistent user launch options and are excluded from clean causal controls.
- `NOMODS` is an unresolved control anomaly and is not accepted as a clean-mod guarantee.

## Method
The exact executable was examined as immutable evidence. No executable patching, injection, hooks, debugger attachment, memory modification, or process modification was used. String findings are classified as structural evidence only; they do not establish runtime semantics without an execution test that discriminates competing hypotheses.

## Finding A — Test-harness storage paths
The executable contains native storage-path strings for `testharness\\`, `testharness\\scripts\\`, `testharness\\reports\\`, `testharness\\regressionsaves\\`, and `testharness\\xs\\`.

The binary also contains the symbolic storage names `TESTHARNESS`, `TESTHARNESS_SCRIPTS`, `TESTHARNESS_REPORTS`, `TESTHARNESS_REG_SAVES`, `TESTHARNESS_XS`, and `TESTHARNESS_XS_SCRIPTS`.

**Interpretation:** the retail executable contains a distinct native test-harness subsystem with dedicated script/report/save locations. This is stronger evidence than a generic launch-option string, but it does not prove that the subsystem is enabled or usable in the present environment.

## Finding B — Native test-harness controllers and AI interfaces
The executable contains RTTI/type information naming `GameTestEventController`, `AITestEventController`, `TimerTestEventController`, `DiagnosticInformationEventController`, `UITestEventController`, `WPFGTestEventController`, and related test-harness object/controller types.

The native AI command vocabulary contains `up-testharness-report`, `up-testharness-test`, `fe-testharness-message`, and `fe-testharness-log-seed`.

**Interpretation:** the test harness has native game/UI/AI event-controller surfaces and explicit AI-facing test-harness commands. This is a credible candidate path for controlled observation, but no claim about their exact call semantics is promoted yet.

## Finding C — Native communication interface
The executable contains the launch option `TEST_HARNESS_COMM` with the description indicating test-name identity, plus `SCRIPTREPORT` and `SESSIONID`. It also contains `TEST_HARNESS_ADDRESS` with a default string of `127.0.0.1:27015` and the native message `testharness::comm::Init UDP socket initialized on address %s`.

**Interpretation:** a localhost UDP communication channel is embedded in the executable. This is materially more promising for unattended automation than GUI-only control.
## Finding D — Harness option table
The launch-option table contains `SCRIPT`, `TEST_HARNESS_COMM`, `SCRIPTREPORT`, `SESSIONID`, `RUNNING_AUTOTEST`, `GAM`, `EDITOR`, `RUN_REGRESSION_TESTS`, and other diagnostic/test controls.

The same table describes `GAM` as `Startup save game file` and `EDITOR` as `Boot directly into the scenario editor.` These descriptions are native executable evidence of option intent, not proof of successful execution on this build/environment.

## Experiment H1 — inert SCRIPT probe
The exact executable was launched directly with a deliberately nonexistent script identifier, a unique `SCRIPTREPORT` path under the isolated lab run root, and `RUNNING_AUTOTEST`. The executable hash was verified before launch and the process was created with argv-only, sanitized environment, isolated working directory, and bounded timeout.

Result: process remained alive through the 20-second timeout and was killed/reaped. No `SCRIPTREPORT` file was created in the requested isolated path.

**Disposition:** `SCRIPT`/`SCRIPTREPORT` grammar and execution path remain **NOT ESTABLISHED**. The nonexistent script was chosen specifically to avoid executing unknown test content.

## Experiment H2 — localhost UDP communication probe
A loopback-only UDP listener was bound to `127.0.0.1:27015`. The exact executable was then launched with `TEST_HARNESS_COMM=AEGIS_HARNESS_UDP_002`, `TEST_HARNESS_ADDRESS=127.0.0.1:27015`, `SESSIONID=AEGIS_SESSION_002`, and `RUNNING_AUTOTEST`.

Result: process remained alive through the bounded 20-second window and was killed/reaped. The listener received **zero datagrams**.

**Disposition:** presence of the native UDP interface is established structurally, but the activation/handshake protocol is **NOT ESTABLISHED**. Zero traffic does not prove that the interface is inactive; it may require a script, test event, game state, or other handshake before transmission.

## Security adjudication
1. Exact executable SHA-256 was verified before each native probe.
2. All process creation used argv, not a shell command line.
3. The UDP listener was restricted to loopback; no external network endpoint was contacted.
4. No executable, game-installation, AI, or data file was modified.
5. The nonexistent-script probe deliberately avoided executing untrusted script content.
6. Temporary probe artifacts remained under the isolated lab run root.
7. Timeouts were bounded and native processes were killed/reaped after timeout.
8. Native strings, RTTI names, and zero-traffic observations are not treated as causal proof.
9. XS remains excluded from the ByzBot runtime architecture and no XS content was added to the deterministic fixture.
## Result and next discriminating test
The native test-harness subsystem is now a high-value investigation target. Structural evidence identifies dedicated test-harness storage, native event controllers, AI-facing test commands, a localhost UDP channel, and script/report/session launch controls.

The first activation probes did not establish the protocol. Therefore AEGIS will not guess a packet format, execute unknown scripts, or treat the harness as a black-box automation API without a handshake hypothesis.

The next test should be a **protocol-discovery gate** using only localhost traffic and native logs: establish whether `TEST_HARNESS_COMM` creates a listener, client, or one-shot sender; determine whether `SESSIONID` changes startup behavior; and test whether an intentionally inert harness request produces a report/acknowledgement. Any protocol implementation must be derived from observed native traffic or authoritative documentation, not invented.

A second path is to inspect the retail test-harness object model and command vocabulary for a minimal AI test that can call `up-testharness-report` from a pure `.per` probe. This must remain a lab-only probe and must not introduce XS into the ByzBot runtime.

**Promotion:** structural native-interface finding only; no runtime causal promotion.
**Layer 1:** remains **89%**.
