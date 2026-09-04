# AEGIS Layer 2 — Pass 31
## CADE Replay Bridge / Event Delivery Audit
**Date:** 2026-09-04
**Disposition:** ACCEPT WITH BOUNDARY — CADE state/event substrate confirmed; end-to-end replay injection remains unproven.

## Mission
Move from Pass 30's native-state discovery to the actual runtime delivery boundary: determine how the Electron renderer obtains CADE events/state and whether the installed application exposes an external replay-to-state path.

## Runtime Evidence
CaptureAge launched successfully from the installed executable. The running application confirms the installed build is operational; no claim is made that the reference replay was loaded during this pass.

The installed preload constructs a native `NamedPipeEndpoint` from process arguments and exposes it to the DOM as `ipcNamedPipeEndpoint` with `poll()` and `close()`.

It separately exposes `ipcRendererTransport`, backed by Electron's `ipc-transport` channel. This establishes two distinct transport layers: native named-pipe polling and Electron IPC transport.

## Renderer API Evidence
The preload imports the native module and exposes CADE enums/API objects to the renderer. `RenderLoop` event-action identifiers include Queue, Start, Stop and render/patch/reset operations.

The preload's native API export includes `AkEvents`, `akEventMaps`, `RenderLoopEventAction`, and `RenderLoopEventType`.

`RenderLoop` exposes `flushEvents`, `postPatch`, `postResetState`, `postLookaheadPatch`, `pollLookaheadGenerateResults`, `setPatchesRequired`, `getGameStateId`, and `getAvailableFrameOrWakeUp`.

`Renderer` exposes `getWorldTime` and `getAdapterDesc`.

## Lifecycle Event Evidence
The installed event map assigns concrete identifiers to lifecycle concepts including:
- PLAY_VILLAGER_CREATED
- PLAY_COMBAT_UNIT_CREATED
- PLAY_BOAT_CREATED
- PLAY_TECHNOLOGY_RESEARCHED
- PLAY_AGE_UP
- PLAY_UNDER_ATTACK
- PLAY_TOWN_UNDER_ATTACK
- PLAY_MONK_CONVERT_COMPLETE
- PLAY_WONDER_STARTED
- PLAY_WONDER_COMPLETED
- PLAY_VICTORY
- PLAY_DEFEAT

The lifecycle names occur in the generated event map, but the inspected preload bundle does not expose their handler bodies as additional literal source. Therefore event-name presence is not equivalent to externally observable payload delivery.

## State Substrate
Pass 30's binary evidence remains valid: `cade.node` contains native state types for World, Player, Entity, CombatEntity, BuildingEntity, ProductionQueueRecord, Task, Action, MakeObjectAction, MakeTechAction, Technology, TechnologyPrerequisite, AttributeValue, and ResearchState, plus GameState and renderer SimulationState/lookahead types.

Pass 31 adds the transport/control evidence connecting the renderer to the native module. The credible runtime topology is:
`renderer DOM -> preload bridge -> Electron IPC / NamedPipeEndpoint -> native CADE module -> RenderLoop / GameState -> renderer state/event projection`.

## Critical Negative Finding
No inspected runtime artifact in this pass provides a documented/public function that accepts an `.aoe2record` path and returns the corresponding lifecycle-event stream to an external process.

The application clearly has replay/state/render infrastructure, but the exact replay-loader invocation and event payload boundary remain unresolved.

No attempt was made to patch or instrument the installed application. The investigation remains read-only.

## W2 Test Status
Required proof remains:
`reference .aoe2record -> CADE replay input -> CADE state transition -> identified object/state -> lifecycle event/payload -> externally captured evidence`.

Pass 31 established the middle transport/state boundary but did not complete the first or last links. Therefore W2 remains OPEN.

## AEGIS Interpretation
CADE should now be treated as a **candidate observation backend**, not as an assumed authoritative oracle.

The AEGIS evidence model should support a backend adapter abstraction:
`ReplaySource -> StateBackend -> ObservationStream -> EvidenceInterpreter`.

A CADE adapter may eventually provide stronger realization evidence than mgz-fast, but only observations actually captured from the replay run may receive DIRECT provenance.

## Closure
W0: CLOSED.
W1: OPEN.
W2: OPEN — concrete CADE transport/state path established, replay injection and external lifecycle capture unresolved.
W3: OPEN.

Scenario-loader automation/testing remains permanently retired.

## Pass Verdict
**PASS 31: ACCEPT WITH BOUNDARY.**
The investigation has established that CADE's rich native state is connected to the renderer through concrete IPC/named-pipe and render-loop interfaces. The remaining engineering problem is no longer "does a rich state model exist?" but "what exact replay-loader and event-delivery contract feeds it?"
