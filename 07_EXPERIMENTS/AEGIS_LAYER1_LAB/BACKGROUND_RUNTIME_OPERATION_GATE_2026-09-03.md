# AEGIS Layer 1 — Background Runtime Operation Gate

**Date:** 2026-09-03  
**Layer 1 status:** 89%  
**Scope:** native runtime lifecycle / observation infrastructure

## Question
Can controlled AoE2DE experiments run without requiring the operator to keep the game foregrounded, allowing the operator to minimize the game and use the workstation for unrelated activity?

## Prior evidence
The hardened runtime already verifies the exact AoE2DE executable, launches with `shell=False`, confines experiment output to the lab run root, sanitizes the child environment, captures stdout/stderr, and enforces timeout/reap. Native UI startup had previously been observed, but GUI focus was known to be an environmental confounder for visual observation.

Official Update 61321 documents `AISCRIPTDEBUGGING` plus `LogSystems=AIScript` as the supported AI debugging/logging path. The current controlled build is 101.103.48987.0 and was independently verified before launch.

## Controlled test
**Run:** `BACKGROUND_RANDOMGAME_002`  
**Executable:** `AoE2DE_s.exe`  
**Build:** `101.103.48987.0 #(180059)`  
**Launch mode:** Windows process started with `WindowStyle=Minimized`  
**Arguments:** `SKIPINTRO WINDOW NOMODS AISCRIPTDEBUGGING LOGSYSTEMS=AIScript CONSTANTLOGGING RANDOMGAME=12345 RANDOMMAP=12345 ALLCP EXIT=5`

The launcher returned a live native AoE2DE process. Independent process inspection observed the exact executable, a valid main window handle, `Responding=True`, and the exact command line. The native log reached `Running Game`. The run terminated normally with launcher exit code 0.

The resulting session log contained `AIScript is being logged`, `Constant Logging is ON`, the exact launch options, and `Running Game`. No separate AI-script event stream was observed in the inspected log, so AI rule execution is not promoted from this run.

## Result
**PASS — background runtime operation is viable for non-GUI experiments.**

The game can be launched and run while minimized; the native process remains observable through process/log channels. This means the operator does not need to watch the game continuously for infrastructure-only or machine-readable observation experiments.

## Important limitation
Minimization is **not** equivalent to proving simulation continuity under every graphics/focus condition. Any experiment whose dependent variable is a visual UI state, editor state, camera state, or other foreground-sensitive observation must explicitly classify window focus as a control variable. Such tests may require restoring the game window for the observation phase.

Likewise, this test does **not** prove scenario loading, `.per` execution, fact evaluation, or causal P0-A behavior. `Running Game` establishes that the launch path entered the game runtime, not that the intended experimental scenario or AI script was loaded.

## Security disposition
No DLL injection, hooks, debugger attachment, memory patching, process modification, or game-install write was used. The experiment was launched from the controlled executable and isolated run directory. Background operation does not relax any security gate.

## Architecture impact
The native experiment harness may treat GUI visibility as optional for non-GUI runs. The observation architecture should prefer machine-readable logs/process/artifacts over screen capture whenever the scientific question permits it. GUI observation remains a separate channel with explicit focus controls.

## Promotion
**Infrastructure capability promoted:** controlled AoE2DE execution does not inherently require foreground observation.  
**Layer 1 causal proposition promoted:** none.  
**Layer 1 percentage:** remains **89%**.

## Next discriminating test
Use the now-validated background launch path to identify the exact scenario/startup mechanism and then prove, in order:

`scenario loaded → pure .per selected → known probe rule executes → observation emitted → controlled mutation → changed observation`

Only after that bridge is established should P0-A persistent-fact freshness arms execute.
