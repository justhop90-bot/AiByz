# AEGIS Layer 1 — Native Scenario Entry Gate

**Date:** 2026-09-03  
**Build:** AoE2DE `101.103.48987.0` / `#180059`  
**Executable SHA-256:** `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`  
**Constraint:** pure `.per`; XS is excluded from the ByzBot architecture and from causal calibration fixtures.

## Question

Can the AEGIS laboratory automatically take a generated `.aoe2scenario` fixture and cause the exact controlled AoE2DE build to enter that scenario as a running game, without weakening the native security gate?

## Prior evidence

- The qualified AoE2ScenarioParser can generate and round-trip a deterministic DE 1.58 scenario.
- Parser bundled tests: 106/106 PASS.
- AEGIS adapter/scenario-provider tests: 7/7 PASS.
- The deterministic P0-A fixture contains a Byzantine AI candidate, controlled resources, an initial villager, a timed create-object trigger, and zero XS script-call conditions/effects.
- The hardened native runtime verifies the exact executable hash, launches with `shell=False`, sanitizes the child environment, confines outputs to the lab run root, captures stdout/stderr, and enforces timeout/kill/reap.
- Native launch has already reached the actual AoE2DE UI. The current build's startup log records `Running Game` and the exact launch options.

## External revision check

Official Update 107882 documents that the `EDITOR` launch parameter should boot directly into the Scenario Editor. Official Update 153015 documents `Ctrl+Space` as the Scenario Editor Test Scenario action. The current official June 2026 Update 177723 remains the latest release checked during this pass and includes current AI/pathfinding changes. These sources establish intended feature semantics, not the result of this experiment.

## Controlled tests

### Test A — `EDITOR` launch parameter

Arguments:

`SKIPINTRO EDITOR WINDOW NOMODS AISCRIPTDEBUGGING LOGSYSTEMS=AIScript CONSTANTLOGGING`

Observed on the exact controlled executable:

- `Active Launch Options` contains `EDITOR`.
- Native initialization completed.
- `Running Game` was logged.
- No `Setting up scenario editor` / `Exiting scenario editor` marker was observed in the resulting MainLog.
- A native window titled `Age of Empires II: Definitive Edition` was present.
- A direct `PrintWindow` capture of that window showed the normal AoE2DE main menu, including `SINGLE PLAYER` and `EDITORS`, rather than the Scenario Editor.

Disposition: **EDITOR flag acceptance is confirmed; EDITOR -> editor UI is not established on this direct-launch path.** This is a build/environment/path-specific negative result, not a contradiction of the official feature documentation.

### Test B — `GAM=<generated .aoe2scenario>`

Arguments included:

`GAM=C:\Users\justh\Desktop\AEGIS-AI-LAB\_adapter_qc\07_EXPERIMENTS\AEGIS_LAYER1_LAB\fixtures\P0A_CAL_001_BASE.aoe2scenario`

Observed:

- The exact argument was recorded by the game in `Active Launch Options`.
- Native initialization completed and `Running Game` was reached.
- No controlled scenario-load marker was observed.

The external launch-option reference describes `GAM` as a **startup save game file**, so passing an `.aoe2scenario` is not evidence that the option should load a scenario. The experiment therefore establishes only that the argument reaches the native command-line layer; it does **not** establish `.aoe2scenario` compatibility with `GAM`.

Disposition: **negative for the proposed scenario-via-GAM route; no causal game-state claim.**

### Test C — `RANDOMGAME` / `RANDOMMAP`

Arguments included:

`RANDOMGAME=12345 RANDOMMAP=12345 ALLCP EXIT=5`

Observed:

- Arguments were accepted and recorded.
- Native initialization completed and `Running Game` was reached.
- No deterministic custom-scenario load was established.

Disposition: **not a viable demonstrated custom-scenario entry route.**

## Observation-channel finding

The native window can be captured independently of the desktop compositor using `PrintWindow`. This is materially better than relying on global desktop screenshots, because the authorized Weebo environment can have browser/Steam windows in the foreground while the AoE2DE native window exists.

However, synthetic keyboard/mouse injection is not yet a trustworthy control channel in this environment. Attempts to activate the native window and send menu input did not establish a deterministic UI transition. The resulting behavior is treated as an input-channel/environment limitation, not as game-state evidence.

No DLL injection, hooks, debugger attachment, memory patching, or process modification were used.

## Causal chain status

```text
verified executable
        ↓
native process
        ↓
native UI                    CONFIRMED
        ↓
scenario loaded              NOT CONFIRMED
        ↓
simulation running           NOT CONFIRMED
        ↓
pure .per loaded             NOT CONFIRMED
        ↓
AI rule executes              NOT CONFIRMED
        ↓
AI observation R0            NOT CONFIRMED
```

## Interpretation

The laboratory can **construct valid deterministic scenarios and launch the exact native executable**, but this pass does not yet justify the stronger statement that it can automatically execute a generated scenario as a controlled game experiment.

The immediate bottleneck is now specifically **native scenario-entry/control**, not scenario generation or executable launch.

The best next routes are:

1. qualify a reliable native UI-control mechanism that works on the same Windows desktop/input context as AoE2DE;
2. use the documented Scenario Editor workflow: Editors → load scenario → Test Scenario;
3. alternatively identify a native command-line/save mechanism that accepts a real `.gam` startup save, then establish how to deterministically produce that save without manual play;
4. once one route is proven, add it to the hardened adapter and run a tiny calibration fixture before any P0-A causal experiment.

## Promotion

**No Layer 1 proposition is promoted from this pass.**

This pass does not change the formal Layer 1 percentage. The 89% status remains unchanged because no remaining P0 causal proposition has been closed.

## Reproduction artifacts

- Fixture: `07_EXPERIMENTS/AEGIS_LAYER1_LAB/fixtures/P0A_CAL_001_BASE.aoe2scenario`
- Run: `07_EXPERIMENTS/AEGIS_LAYER1_LAB/runs/SCENARIO_LOAD_GATE_001/`
- Run: `07_EXPERIMENTS/AEGIS_LAYER1_LAB/runs/GAM_SCENARIO_PROBE_001/`
- Run: `07_EXPERIMENTS/AEGIS_LAYER1_LAB/runs/RANDOMGAME_PROBE_001/`
- Run: `07_EXPERIMENTS/AEGIS_LAYER1_LAB/runs/GUI_CAPTURE_001/`

## Methodology record

`question → prior evidence → competing hypotheses → discriminating test → exact build/setup → raw observation → interpretation → confidence → promotion/rejection → repository artifact → next test`

This report records the current gate as an infrastructure/entry-path investigation. It intentionally does not convert launch success, UI presence, command-line acceptance, timeout behavior, or absence of log markers into AI causal evidence.
