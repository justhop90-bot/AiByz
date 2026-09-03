# AEGIS Layer 1 — Native Entry and Observation Gate

**Date:** 2026-09-03
**Build:** 101.103.48987.0 / internal build 180059
**Executable:** AoE2DE_s.exe
**SHA-256:** 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4
**Layer 1 status:** 89%

## Question
Can the exact controlled AoE2DE build provide a deterministic, unattended route from process startup to a known game/scenario state with a trustworthy AI observation channel, without weakening the AEGIS security boundary?

## Prior evidence
- Exact executable launch, native window creation, and background/minimized operation were previously established.
- A deterministic DE 1.58 `.aoe2scenario` fixture exists, but native scenario loading is not yet established.
- Official release documentation identifies `GAM` as a startup save-game launch parameter and `NOMODS` as a mod-disabling parameter.
- Official Update 58259 states that `up-log-data` produces an AI log file.

## Method
Each native probe verified the executable SHA-256 before launch. Experiments used argv-only process creation and retained raw native logs. No DLL injection, hooks, debugger attachment, memory modification, or process modification was used.
## Experiment A — GAM filename-only probe

A known 512,028-byte `.aoe2spgame` autosave was copied to the user save directory under a unique test filename. The exact build was launched with `GAM=AEGIS_GAM_GATE_003.aoe2spgame`, without the undocumented `-autogame` flag. The native process remained alive and consumed substantial CPU/memory, but the session log reached the ordinary startup/menu path and did not provide evidence that the supplied save became the active game.

The temporary save copy was deleted after the test. No game-installation file was modified.

**Disposition:** GAM filename-only startup load remains **NOT ESTABLISHED**.

## Experiment B — launch-option archaeology

The exact executable contains the strings `Startup save game file` and `GAM` in the native launch-option string table. This independently confirms that the current executable carries a `GAM` launch-option definition; it does not prove its loading grammar or execution path.

The same native binary contains `AISCRIPTDEBUGGING`, `AIDEBUGGING`, `LOGSYSTEMS`, `LOGAI`, and related diagnostic option definitions. The binary does not contain the literal strings `-autogame` or `AUTOGAME` in ASCII/UTF-16LE search.

## Experiment C — Steam launch contamination discovered

The Steam `localconfig.vdf` for AppID 813780 contains an existing user launch-options value: `-autogame -AIdebug`. A Steam-mediated launch therefore appended those flags to the native command line even when the experiment itself did not request them.

`-autogame` is not present as a literal in the controlled executable's ASCII or UTF-16LE strings, while `AIDEBUGGING` is present. This is not sufficient to prove the behavior of either token, but it makes Steam-mediated runs unsuitable as clean causal controls until launch-option contamination is isolated.

**Disposition:** Steam launch path is an **environmental confounder** for controlled experiments. AEGIS will prefer direct verified executable launches unless a Steam path is itself the object of the experiment. Existing Steam launch options will not be silently edited.

## Experiment D — AI logging / random-game probe

The exact executable was launched directly with verified SHA-256 and the following diagnostic controls: `AISCRIPTDEBUGGING`, `AIDEBUGGING`, `LOGSYSTEMS=AIScript`, `CONSTANTLOGGING`, `LOGAI`, `LOGUAI`, `LOGACTION`, `LOGMOVE`, `LOGEXPLORE`, `LOGWAYPOINT`, `SHOWUNITIDS`, `SHOWAIGROUPS`, deterministic `RANDOMGAME` and `RANDOMMAP` seeds, `ALLCP`, and `EXIT=30`.

`MainLog.txt` recorded `AIScript is being logged`, `SyncAI is being logged`, the complete active launch-option set, build identity, `Running Game`, and subsequent native runtime logging. This establishes that the requested AI diagnostic controls are accepted and that the native logging channel is operational.

However, no deterministic custom scenario was loaded and no AI rule/fact result was isolated. Therefore this is **observation-channel/instrumentation evidence only**, not proof of `.per` rule execution or P0-A causality.
## Experiment E — NOMODS control anomaly

The same direct diagnostic run included `NOMODS`. The native `MainLog.txt` nevertheless emitted repeated `Enabling mod #0 (...)` records for the user's installed mods before `Setup post mod manager` completed.

Official documentation defines `NOMODS` as disabling the mods system. The observed logging is therefore a control anomaly. It may represent mod-manager enumeration/initialization rather than effective activation, but the current evidence does not discriminate those interpretations.

**Disposition:** `NOMODS` is **not accepted as a clean-mod control** for causal experiments until a sentinel test proves whether installed mod content can affect the resulting runtime. No user mod configuration was changed during this pass.

## Security / quality adjudication

1. Build identity remains fail-closed: exact SHA-256 checked before every native launch.
2. Steam-mediated launch is excluded from clean causal controls until its persistent launch options are isolated.
3. No user Steam launch configuration was modified.
4. The temporary GAM test save was removed after use.
5. No game-installation AI/data file was modified.
6. No injection, hooks, debugger attachment, memory patching, or process modification was used.
7. Native logs are treated as observations, not as causal claims by themselves.
8. Parser tooling remains outside the game runtime and the pure `.per` architecture remains unchanged.

## Result

The native observation gate has advanced: we now have a reproducible, machine-readable native log stream and exact-build launch provenance. Deterministic custom-game entry remains the blocking gate. The next discriminating work should isolate a clean game-start mechanism and then prove execution of a deliberately tiny pure `.per` probe before P0-A experiments begin.

**Promotion:** none.
**Layer 1:** remains **89%**.
