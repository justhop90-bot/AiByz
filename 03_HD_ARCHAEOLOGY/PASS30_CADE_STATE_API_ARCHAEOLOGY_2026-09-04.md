# AEGIS Layer 2 — Pass 30
## CADE State API / Native Bridge Archaeology
**Date:** 2026-09-04  
**Disposition:** ACCEPT — W2 path materially strengthened; end-to-end replay event capture remains unproven.

## Mission
Trace the installed CaptureAge 1.25.0 boundary beyond the event-name census: renderer/preload -> native CADE bridge -> render/state API -> lifecycle/state representation.

## Installation Evidence
Installed root: `C:\Users\justh\AppData\Local\Programs\CaptureAge\resources\app`

`electronMain.js` directly requires `./cade.node`, verifies `cadeNodeVersion === 1.25.0`, then calls `cade.init(require)`. `electronMain.camod` is present but zero bytes.

Native module: `cade.node`  
Size: 15,421,728 bytes  
SHA-256: `C64832B06229D445B4E735BB1A768100B044B64A6A74A32C45710853725BCC61`

Direct Node loading succeeded and reported version `1.25.0`.

## Native API Census
Top-level exports include `NamedPipeEndpoint`, `NamedPipeSender`, `RawServerStreamCall`, `Renderer`, `RenderLoop`, `System`, and other native APIs.

`RenderLoop.prototype` exposes `flushEvents`, `postPatch`, `postResetState`, `postLookaheadPatch`, `pollLookaheadGenerateResults`, `setPatchesRequired`, `getGameStateId`, and `getAvailableFrameOrWakeUp`.

`Renderer.prototype` exposes `getWorldTime` and `getAdapterDesc`.

## Event Boundary
The installed `rendererPreload.js` contains an `AkEvents` enum/map with explicit lifecycle identifiers including `PLAY_AGE_UP`, `PLAY_VILLAGER_CREATED`, `PLAY_COMBAT_UNIT_CREATED`, `PLAY_BOAT_CREATED`, `PLAY_TECHNOLOGY_RESEARCHED`, `PLAY_MONK_CONVERT_COMPLETE`, `PLAY_UNDER_ATTACK`, `PLAY_TOWN_UNDER_ATTACK`, `PLAY_WONDER_STARTED`, `PLAY_WONDER_COMPLETED`, `PLAY_VICTORY`, and `PLAY_DEFEAT`.

The lifecycle names occur in the generated enum/map; the searched preload bundle contains no additional literal occurrences exposing their handler implementation.

The preload exposes `ipcNamedPipeEndpoint` and `ipcRendererTransport` through Electron context bridging. This proves an IPC/native transport boundary, not external AkEvent payload access.

## Stronger Native-State Evidence
Binary inspection of `cade.node` exposes C++ types under `state@cade_api`, including `Root`, `World`, `Player`, `Entity`, `CombatEntity`, `BuildingEntity`, `ProductionQueueRecord`, `Task`, `Action`, `MakeObjectAction`, `MakeTechAction`, `Technology`, `TechnologyPrerequisite`, `AttributeValue`, and `ResearchState`.

The same binary contains `state::GameState`, renderer-side `RendererLookahead` / `SimulationState`, and `RenderLoopApi`.

This is qualitatively richer than the mgz-fast model: CADE has explicit representations for entities, production queues, technologies, research state, and actions.

## Evidence Classification
**DIRECT:** installed CADE native layer contains a richer state model than aggregate replay SYNC telemetry.

**DIRECT:** application contains named lifecycle event concepts for creation, research, age-up, combat, attack, victory, etc.

**DIRECT:** native bridge exposes render-loop/state APIs and IPC/named-pipe transport.

**NOT PROVEN:** reference `.aoe2record` has been loaded into this CADE state engine.

**NOT PROVEN:** lifecycle events can be intercepted externally with payloads.

**NOT PROVEN:** CADE state is engine-authoritative rather than deterministic replay reconstruction.

## AEGIS Consequence
The credible candidate chain is:
`REPLAY / PATCH INPUT -> CADE STATE -> ENTITY / QUEUE / RESEARCH STATE -> RENDER/EVENT PROJECTION`.

Required W2 proof remains:
`RAW COMMAND -> CADE OBSERVATION -> IDENTIFIED WORLD OBJECT/STATE -> TEMPORAL POSTCONDITION`.

The next experiment must drive the reference replay through CADE and capture one DE_QUEUE, one BUILD, one RESEARCH, and one DELETE lifecycle transition, comparing identity, owner, type, world-time, queue/state transition, and event payload.

## Closure
W0: CLOSED.  
W1: OPEN.  
W2: OPEN — concrete candidate state substrate identified, but not validated against the reference replay.  
W3: OPEN.

Scenario-loader automation/testing remains permanently retired.

## Pass Verdict
**PASS 30: ACCEPT.**
The investigation has crossed from "event vocabulary exists" to "a concrete native game-state object model and render/event pipeline exist." The remaining question is operational: can the reference recording drive this state machine and expose lifecycle state without UI heuristics?
