# AEGIS — Native AoE2DE Test Harness Static Reverse Engineering

**Date:** 2026-09-05  
**Target build:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`  
**Executable SHA-256:** `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`  
**Status:** STATIC HARNESS SEMANTICS PARTIALLY ESTABLISHED; RETAIL INVOCATION REMAINS UNQUALIFIED

## 1. Major finding

The retail executable contains a substantial native Test Harness subsystem. This is not inferred from the existence of the `testharness` directory; it is directly evidenced by strings and RTTI-like symbols embedded in the target executable.

Observed native controls include:

- `TEST_HARNESS_COMM`
- `TEST_HARNESS_ADDRESS`
- `SCRIPT`
- `SCRIPTREPORT`
- `SESSIONID`
- `RUNNING_AUTOTEST`
- `up-testharness-test`
- `up-testharness-report`
- `fe-testharness-message`
- `fe-testharness-log-seed`
- `// Received FTS`
- `testharness::comm::Init UDP socket initialized on address %s`
- `testharness::comm::SockFree`

The executable also contains native event-controller types including:

- `GameTestEventController@testharness`
- `AITestEventController@testharness`
- `TimerTestEventController@testharness`
- `UITestEventController@testharness`
- `FPSEventController@testharness`
- `DiagnosticInformationEventController@testharness`
- `WPFGTestEventController@testharness`
- `uiWidgetTestEventController@testharness`

## 2. Native filesystem contract

The executable contains storage-point names for:

- `TESTHARNESS`
- `TESTHARNESS_SCRIPTS`
- `TESTHARNESS_REPORTS`
- `TESTHARNESS_REG_SAVES`
- `TESTHARNESS_XS`
- `TESTHARNESS_XS_SCRIPTS`

On the authorized workstation the active user-side harness tree is:

`C:\Users\justh\Games\Age of Empires 2\testharness\`

with:

- `scripts\AEGIS_FTS_CAL_001.fts`
- `reports\` directory

The current FTS probe is:

`WAIT 1`  
`REPORT AEGIS_FTS_CAL_001`

No report file was produced by the retail-build invocation attempts performed during this phase.

## 3. FTS parser evidence

The executable contains parser/error strings proving additional FTS grammar elements beyond the two-line probe:

- `CALL`
- `REPORT`
- `RANDOM`
- `LABEL`
- `WAIT TIME`
- `WAIT EVENTTASK`
- `WAIT EVENTTASK TIMEOUTFAIL`
- `WAIT EVENTTASK TIMEOUTCONTINUE`
- call-script file resolution
- goto/label handling
- tokenized parsing (`TKN_REPORT`, `TKN_GOTOIF`, etc.)

This is sufficient to establish that FTS is a real internal test-script language rather than an arbitrary text format.

It is **not** sufficient to claim a complete grammar or external invocation protocol.

## 4. Retail invocation experiment

Controlled launches were performed against the actual target executable using the discovered command-line surface, including combinations of:

- `TEST_HARNESS_COMM=AEGIS_FTS_CAL_001`
- `TEST_HARNESS_ADDRESS=127.0.0.1:27015`
- `RUNNING_AUTOTEST`
- `SKIPINTRO`
- `SCRIPT=<probe>`
- `SCRIPTREPORT=<report>`

The executable accepted the command line and remained alive normally, but process inspection showed only the ordinary game UDP socket (`0.0.0.0:9999`) rather than a listener on the requested test-harness address.

A raw UDP probe sent to `127.0.0.1:27015` did not trigger FTS execution and no report was generated.

Therefore:

**Retail-build harness invocation is NOT YET QUALIFIED.**

## 5. Critical interpretation

The presence of native harness code in the retail executable does not imply that the retail executable exposes the harness through the documented launch surface.

Independent launch-option documentation lists `SCRIPT`, `SCRIPTREPORT`, `SESSIONID`, and `RUNNING_AUTOTEST`, but marks the test-harness-specific controls as not established for ordinary non-debug use. This is consistent with the workstation result: the code exists, but the retail build does not presently expose the expected socket endpoint under the attempted invocation.

This distinction is now an explicit AEGIS rule:

> **Embedded capability ≠ enabled capability ≠ externally invocable capability.**

## 6. Highest-value next target

The remaining unknown is no longer “does AoE2DE have a test harness?” It does.

The remaining questions are:

1. What build/profile enables the socket controller?
2. What exact value format does `TEST_HARNESS_COMM` require?
3. What is the `SESSIONID` handshake?
4. Does the client send an FTS path, FTS contents, or a structured message?
5. What packet format is expected by `testharness::comm`?
6. When does `// Received FTS` fire relative to socket initialization?
7. How are reports serialized and written to `TESTHARNESS_REPORTS`?
8. Which event controllers are available in the retail build versus test/debug builds?

## 7. Qualification disposition

| Question | Status |
|---|---|
| Native harness code exists | **PROVEN** |
| Native FTS parser exists | **PROVEN** |
| Native report primitive exists | **PROVEN** |
| Native harness storage contract exists | **PROVEN** |
| FTS has structured grammar | **PROVEN** |
| Retail socket listener enabled by attempted invocation | **NOT PROVEN** |
| Retail FTS execution | **UNKNOWN** |
| SESSIONID handshake | **UNKNOWN** |
| Report transport/serialization | **UNKNOWN** |
| Debug/test-build harness availability | **UNKNOWN** |

## 8. Engineering consequence

This finding strengthens the AEGIS qualification strategy but does not authorize runtime implementation.

The native harness is now a **high-value target for further reverse engineering** because, if its invocation contract can be established on an authorized test build, it could provide the controlled engine experiment loop required by Q-02 through Q-12.

Until that contract is proven, AEGIS must continue to treat runtime gates as UNKNOWN rather than substituting a homemade harness and calling the resulting behavior engine truth.
