# AEGIS Native Lifecycle Observation Gate — 2026-09-03

## Layer 1 status
**89% — unchanged. No causal proposition promoted.**

## Question
Can AEGIS obtain a trustworthy native lifecycle observation from the exact
controlled AoE2DE build while preserving the security boundary?

## Prior evidence
The earlier startup calibration proved process creation, containment,
timeout, kill, and reap, but did not prove game initialization or scenario load.
The controlled executable is `AoE2DE_s.exe`, build `101.103.48987.0`, SHA-256
`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`.

## External revision check
Official AoE2DE documentation confirms `AISCRIPTDEBUGGING` and `AIDEBUGGING` as
AI diagnostic launch parameters, and states that `AISCRIPTDEBUGGING` can be
paired with `LogSystems=AIScript` for AI debug logging. Update 58259 also records
that `up-log-data` produces an AI log file. These are candidate observation
channels, not yet accepted as native causal evidence for this build.

## Controlled tests
### Test A — debug launch
Launch arguments:
`SKIPINTRO AISCRIPTDEBUGGING LOGSYSTEMS=AIScript CONSTANTLOGGING WINDOW`

The exact executable remained alive beyond the initial observation interval.
The process was later terminated by the controlled harness. No causal claim was
made from process lifetime alone.

### Test B — editor launch probe
Launch arguments:
`SKIPINTRO EDITOR WINDOW`

The process command line was independently inspected and confirmed to contain
those exact arguments. A visible game UI was observed during the session, but
an editor-specific UI state was not established. Therefore `EDITOR` is recorded
as an observed accepted command-line argument, not as proof of editor behavior.

## Native UI observation
A screen capture during the controlled session showed the AoE2DE main menu,
including the `SINGLE PLAYER` and `EDITORS` controls. This is stronger evidence
than the earlier stdout-only test: the executable demonstrably reached a visible
native UI state during the session.

This still does not establish that the calibration scenario was loaded, that a
specific `.per` AI was attached to P1, or that an AI fact was evaluated.

## Important negative result
The expected AI log directory contained no `.txt` artifacts during the tested
session. This means the current logging invocation has not yet produced a usable
observation channel in this environment. It does not prove that AI logging is
broken; possible causes include launch context, log routing, current build
behavior, or the absence of an active AI script session.

## Competing hypotheses
- H1: direct executable launch reaches the game UI but logging requires an active
  game/AI session.
- H2: logging is redirected elsewhere or requires additional launch configuration.
- H3: the current release build differs from historical logging behavior.
- H4: the diagnostic switches are accepted but do not emit until AI execution.

No hypothesis is promoted from this test.

## Security disposition
PASS. No DLL injection, hook, debugger attachment, memory patching, or process
modification was used. Game installation remained an input/capability source;
experiment output remained under the isolated AEGIS run root.
