# AEGIS — External Runtime Qualification Harness Architecture

**Date:** 2026-09-05  
**Status:** APPROVED RESEARCH ARCHITECTURE — IMPLEMENTATION NEXT  
**Scope:** AoE2:DE retail-compatible machine qualification; replaces dependence on the embedded/native test-harness path.

## 1. Decision

AEGIS will **not depend on the embedded `TEST_HARNESS_*` / FTS test-harness path** discovered in `AoE2DE_s.exe`.

The native path is treated as an internal/test-profile capability whose retail activation has not been established. It is therefore not part of the production qualification contract.

Instead, AEGIS will build an **external runtime qualification harness** around the ordinary retail game plus community-supported instrumentation and replay tooling.

The harness is an external laboratory. It does not become part of the bot's decision architecture.

## 2. Design principle

The harness must separate four responsibilities:

1. **Experiment orchestration** — prepare inputs, launch the game, supervise timeouts, collect artifacts.
2. **Runtime observation** — obtain machine evidence from permitted instrumentation and game outputs.
3. **Replay/post-run analysis** — parse `.aoe2record` artifacts and derive reproducible evidence.
4. **Verdict generation** — compare observations against an explicit experiment contract.

The harness must never silently convert an unobserved behavior into a VERIFIED semantic claim.

## 3. Community resources and their role

### AoE2Control — primary live-runtime instrumentation candidate

AoE2Control is a Lua scripting engine for AoE2:DE. Its documentation states that it can read live game state and issue commands directly, without pixel scanning or mouse/keyboard simulation. It exposes an IPC layer using Windows named pipes and JSON, including module routing, and provides headless launcher operation suitable for script-driven startup.

For AEGIS, this is the most valuable external substrate because it supplies a structured **live-state adapter** rather than forcing the laboratory to infer state from screenshots.

AEGIS will treat AoE2Control as an **instrumentation backend**, not as an AEGIS architectural dependency. Its observations must carry backend/build provenance and cannot redefine the PER/XS authority boundary.

Important constraints from its documentation:
- local-machine named-pipe IPC;
- single-player integrity restrictions;
- direct process attachment/injection;
- game-version compatibility can change after updates;
- headless launcher starts after AoE2DE is already running;
- session-control APIs can configure/start/restart/load games;
- replay mode blocks in-match command APIs.

### AutoDE — reference for orchestration, not the foundation

AutoDE demonstrates automated multi-match execution using screen capture and GUI interaction, CSV-defined matchup batches, timeouts, logging, and incremental result persistence.

AEGIS will **not copy its screen-capture architecture as the primary control path**. It is a useful fallback adapter and a source of orchestration ideas, but pixel/screen automation is inherently less deterministic than structured runtime instrumentation.

### mgz-fast / aoc-mgz — replay evidence backend

`mgz-fast` is a stripped-down AoE2 recorded-game parser supporting DE `.aoe2record` files and exposes header/body operations as structured data. `aoc-mgz` provides the broader Python parser and abstractions.

AEGIS will use replay parsing for post-run evidence, match identity, actions, sync timing, and outcome analysis. Replay parsing is **not** assumed to reconstruct arbitrary hidden machine state at arbitrary times; where a fact requires live observation, the harness must obtain it live or mark it UNKNOWN.

### aoe2rec — alternative high-throughput replay backend

`aoe2rec` is a Rust library for reading/writing DE recorded games, with Python bindings. It is a candidate for a faster production post-processing path if Python replay parsing becomes a bottleneck.

### Genieutils / AoE2 tooling — data and artifact support

`genieutils` provides read/write support for Genie-engine data and asset formats, including DE-era formats. It is useful for data extraction, scenario/tooling work, and fixture generation, but it is not a substitute for runtime semantic evidence.

### AoE2 AI Scripting Encyclopedia — semantic reference

The AI Scripting Encyclopedia provides structured documentation for commands, parameters, facts, strategic numbers, objects, technologies, unit lines, and guides. It is a reference source and hypothesis generator; target-build executable behavior remains authoritative for unresolved semantics.

### Eruner / historical AI repositories — corpus and pattern mining

The historical AI repositories provide reusable `.per` modules, functional bots, documentation, and examples of rule-engine patterns. They are useful for fixture generation, negative tests, idiom discovery, and regression corpus construction. They are not authority for current target-build semantics.

## 4. AEGIS harness layers

```text
                         AEGIS EXPERIMENT CONTRACT
                                   |
                         +---------+---------+
                         |                   |
                  ORCHESTRATOR          VERDICT ENGINE
                         |                   |
              +----------+----------+       |
              |          |          |       |
           LAUNCH     SESSION     WATCH      |
              |          |          |       |
              +----------+----------+       |
                         |                  |
                 LIVE OBSERVATION           |
                  /           \
         Retail/Stock       CONTROL adapter
          evidence             (optional)
              |                   |
              +---------+---------+
                        |
                 REPLAY ARTIFACT
                        |
              mgz-fast / mgz / aoe2rec
                        |
                 EVIDENCE BUNDLE
                        |
               QUALIFICATION VERDICT
```

## 5. Core adapters

### Adapter A — Retail launcher

Responsibilities:
- identify exact `AoE2DE_s.exe` build and SHA-256;
- create isolated experiment workspace;
- launch game with documented, ordinary retail options;
- supervise process lifetime;
- capture stdout/stderr where available;
- preserve exit code and timestamps;
- never modify the stock AI installation in-place.

### Adapter B — AI package sandbox

Every experiment receives a disposable AI package directory containing:
- `.ai` identity file;
- `.per` entrypoint;
- required `.per` dependencies;
- experiment-specific instrumentation rules;
- manifest with hashes.

The stock `/resources/_common/ai` directory remains a frozen reference. No experiment may write directly into it.

### Adapter C — Live instrumentation

Preferred implementation:
- AoE2Control module;
- named-pipe IPC;
- JSON observation envelopes;
- optional high-throughput snapshot buffers where needed.

Observation envelope target:

```json
{
  "experiment_id": "...",
  "build_sha256": "...",
  "backend": "aoe2control",
  "game_time_ms": 0,
  "controller_time_ms": 0,
  "player_id": 0,
  "generation": 1,
  "observation_kind": "...",
  "payload": {},
  "evidence_level": "runtime_observed"
}
```

The envelope deliberately includes build, time, generation, and provenance so an observation cannot be mistaken for timeless global truth.

### Adapter D — Replay collector/parser

At experiment termination:
- locate the resulting `.aoe2record`;
- hash it before processing;
- parse with `mgz-fast` first;
- fall back to `aoc-mgz` when richer fields are required;
- optionally validate/scale with `aoe2rec` for high-volume batches;
- emit normalized action/sync/outcome records.

### Adapter E — GUI fallback

Only when structured APIs cannot expose the required state:
- use Windows/UI automation or screen capture as a last-mile adapter;
- record screenshots and interaction logs;
- never treat visual recognition as equivalent to a machine-state observation without an explicit uncertainty grade.

## 6. Experiment lifecycle

Every experiment follows:

```text
CONTRACT
  -> FREEZE BUILD
  -> FREEZE INPUTS
  -> PREPARE SANDBOX
  -> LAUNCH
  -> ATTACH OBSERVER
  -> RUN MICROTEST
  -> COLLECT LIVE EVENTS
  -> COLLECT REPLAY
  -> PARSE
  -> CROSS-CHECK
  -> CLASSIFY
  -> ARCHIVE
  -> UPDATE QUALIFICATION REGISTER
```

No experiment is considered successful merely because the game did not crash.

## 7. Evidence bundle

Each run produces a self-contained directory:

```text
runs/<experiment_id>/
  manifest.json
  build.json
  inputs/
  ai_package/
  launch/
    command.json
    stdout.log
    stderr.log
  live/
    observations.jsonl
    transport.log
  replay/
    *.aoe2record
    header.json
    body.jsonl
  derived/
    normalized_events.jsonl
    verdict.json
  artifacts.sha256
```

`manifest.json` records every input hash, tool version, backend version, start/end time, and verdict.

## 8. Verdict model

Allowed verdicts:

- `PASS_RUNTIME_CONFIRMED`
- `PASS_CROSS_CORROBORATED`
- `OBSERVED_WITH_LIMITATIONS`
- `FAIL_RUNTIME_BEHAVIOR`
- `FAIL_HARNESS`
- `UNKNOWN`
- `NOT_APPLICABLE`

`UNKNOWN` is a valid engineering result. It is not a failure and must never be silently promoted to PASS.

## 9. First experiments

The first implementation batch should not attempt to qualify the entire AEGIS architecture. It should establish the minimum machine substrate required by the Cavalry Threat Containment vertical slice:

1. build identity and backend identity;
2. player identity / perspective;
3. game clock observation;
4. unit/object identity;
5. unit type and owner;
6. fog-aware visibility semantics;
7. enemy cavalry observation;
8. command issue vs world-state change;
9. queued/pending vs created/available distinction;
10. replay/live timestamp correlation;
11. restart/repeatability;
12. negative/zero/absence cases.

Each experiment must have one semantic question.

## 10. Determinism policy

The harness must capture and reuse all deterministic inputs available to it:
- exact game build;
- map/scenario identity and hash;
- lobby/game settings;
- civilization assignments;
- player slots;
- game seed where exposed;
- AI package hashes;
- instrumentation backend version;
- harness version.

Repeated experiments with identical inputs must be grouped as a reproducibility set. A single run is evidence; repeated runs establish stability.

## 11. Security / integrity boundary

The harness is explicitly for single-player engineering and qualification. It must never be used to interfere with ranked multiplayer integrity.

External instrumentation is isolated from the bot's production authority path. In particular:
- CONTROL observations do not become AEGIS truth merely because they are available;
- external commands are test actions, not hidden production control;
- all injected/instrumented backends are build/version qualified separately;
- the stock AI tree remains immutable during experiments.

## 12. Engineering conclusion

The embedded retail test-harness discovery was valuable because it proved the executable contains a substantial internal testing architecture. It is not necessary for AEGIS.

The superior engineering path is to construct a **portable external laboratory** using:

- AoE2Control for optional structured live runtime access and IPC;
- ordinary Windows process/session control for orchestration;
- disposable AI packages and fixtures;
- AutoDE-derived ideas for batch execution, but not its screen-capture dependency;
- mgz-fast/aoc-mgz/aoe2rec for replay evidence;
- AI Scripting Encyclopedia and historical AI repositories for semantic corpus and fixture generation;
- GitHub as the evidence ledger.

This gives AEGIS a test system that is independent of the game's hidden test profile, while retaining a clean separation between **production bot authority** and **external measurement/qualification**.

## 13. Immediate implementation order

1. Build the run-manifest schema.
2. Build the sandbox/package copier with stock-tree protection.
3. Build the retail launcher/supervisor.
4. Build the replay collector and parser adapter.
5. Build the AoE2Control adapter behind an interface, not as a hard dependency.
6. Implement one ping/clock/player observation experiment.
7. Implement one cavalry observation experiment.
8. Correlate live observations against replay evidence.
9. Add repeatability and negative tests.
10. Only then begin qualification of AEGIS machine semantics.

**This document authorizes engineering of the external harness. It does not authorize unresolved machine semantics to enter production AEGIS code.**
