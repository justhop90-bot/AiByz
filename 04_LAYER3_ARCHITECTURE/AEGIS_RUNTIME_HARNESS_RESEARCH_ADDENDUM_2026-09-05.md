# AEGIS — Runtime Harness Research Addendum

**Date:** 2026-09-05  
**Status:** PARTIALLY QUALIFIED — INVOCATION SURFACE DISCOVERED, TEST EXECUTION NOT YET QUALIFIED
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Breakthrough finding

Direct binary inspection of the installed `AoE2DE_s.exe` exposed a native test-harness launch surface that was not visible from the tiny installed `.fts` directory alone.

The executable contains the following launch parameters:

- `SCRIPT` — Script to run
- `TEST_HARNESS_COMM` — Enable Test Harness socket communication; value described as test name / ID
- `SCRIPTREPORT` — Script report output file
- `SESSIONID` — Session ID with which client script should join
- `RUNNING_AUTOTEST` — automation-test mode

The executable also contains:

`TEST_HARNESS_ADDRESS = 127.0.0.1:27015`

and the string:

`testharness::comm::Init UDP socket initialized on address %s`

This establishes that the test harness is a native engine facility with UDP communication, rather than merely a stray `.fts` file.

## 2. Native test-harness primitives exposed by the executable

The binary also contains the scripting primitive names:

- `up-testharness-report`
- `up-testharness-test`
- `fe-testharness-message`
- `fe-testharness-log-seed`

The executable contains `GameTestEventController@testharness`, `AITestEventController@testharness`, `TimerTestEventController@testharness`, `FPSEventController@testharness`, `DiagnosticInformationEventController@testharness`, and `WPFGTestEventController@testharness` symbols.

This is substantially stronger evidence than the filesystem-only discovery.

## 3. Controlled invocation attempt

A disposable calibration launch was attempted against the installed executable using the discovered launch surface and a local UDP listener on `127.0.0.1:27015`.

The game executable launched successfully and remained active, but the listener received no UDP payload during the observation window and no requested `SCRIPTREPORT` file was produced.

This result does **not** mean the harness is broken. It means the remaining invocation contract is not yet known.

Possible unresolved variables include:

- exact syntax/value expected by `TEST_HARNESS_COMM`;
- whether `SCRIPT` expects a filesystem path, registered test name, or another identifier;
- whether an external harness client must initiate the session;
- whether `SESSIONID` must correspond to a live client;
- whether the harness is enabled only under a particular game mode/build configuration;
- exact report-path resolution;
- whether `up-testharness-test` must trigger the FTS test from inside the AI/script environment;
- whether the socket sends only after a client handshake.

## 4. Important negative result

The experiment did **not** alter the stock `/ai` closure.

No production `.per` implementation was installed.

No ABI allocation was promoted from the experiment.

The game process was terminated after the controlled attempt.

## 5. Engineering consequence

The runtime qualification path is now much closer than previously believed.

The correct next investigation is no longer “find whether a harness exists.” That question is answered.

The next question is:

> **What exact client/session protocol causes the native test harness to execute an FTS test and emit a report?**

That question should be solved before attempting Q-02/Q-04/Q-06 runtime experiments because the harness may provide the safest native path for deterministic target-build qualification.

## 6. Evidence grade

- Native launch-parameter strings: **E0-static / direct target-binary evidence**
- Native harness controller symbols: **E0-static / direct target-binary evidence**
- UDP address: **E0-static / direct target-binary evidence**
- Successful game launch with test parameters: **E0-runtime process evidence**
- UDP protocol semantics: **UNKNOWN**
- FTS execution semantics: **UNKNOWN**
- Report semantics: **UNKNOWN**

## 7. Status

**Runtime harness existence:** QUALIFIED  
**Launch surface:** PARTIALLY QUALIFIED  
**Transport endpoint:** QUALIFIED (`127.0.0.1:27015`)  
**Client/session protocol:** UNKNOWN  
**FTS execution:** UNKNOWN  
**Report production:** UNKNOWN  
**Safe automated qualification:** NOT YET QUALIFIED
