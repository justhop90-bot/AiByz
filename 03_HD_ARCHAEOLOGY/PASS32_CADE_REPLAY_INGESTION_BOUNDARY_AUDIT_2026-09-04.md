# AEGIS Layer 2 — Pass 32
## CADE Replay Ingestion Boundary Audit
**Date:** 2026-09-04
**Disposition:** ACCEPT — boundary narrowed; replay-loader remains unresolved.

## Mission
Trace how the installed CaptureAge renderer reaches the native CADE substrate and identify the process-argument contract that initializes the native bridge.

## Direct Findings
The installed preload does not directly implement replay loading. It derives three values from process.argv after the literal `cadeDomArguments` marker:
1. `namedPipePrefix`
2. `nativeModulePath`
3. `namedPipeEndpointName`

The native module is then loaded from the supplied `nativeModulePath` using a non-webpack require path.

The preload constructs `NamedPipeEndpoint(joined prefix/name, 1)` and exposes only `poll()` and `close()` as `window.ipcNamedPipeEndpoint`.

A separate renderer transport listens for Electron `ipc-transport` messages and exposes `setHandler()` and `send()`.

The native CADE API object exports `AkEvents`, `akEventMaps`, `RenderLoopEventAction`, and `RenderLoopEventType` to the renderer.

## RenderLoop Boundary
The exported event-action enum contains explicit state/render actions: Idle, Render, Patch, UpdateAppConfig, GetObjectsInViewRect, FlushMetrics, ReleaseTexture, UpdateCamera, ResetState, and PlaySound.

The lifecycle event map contains concrete IDs for `PLAY_VILLAGER_CREATED`, `PLAY_COMBAT_UNIT_CREATED`, `PLAY_TECHNOLOGY_RESEARCHED`, `PLAY_AGE_UP`, attack-state events, wonder completion, victory, and defeat.

## Important Negative
Search of the installed application JavaScript found no direct replay-loader implementation keyed to `.aoe2record`, `loadReplay`, or `loadRecording` that exposes a replay path through the preload boundary.

The inspected preload therefore functions as a native-bridge/bootstrap layer, not the replay ingestion implementation.

## Architectural Interpretation
The strongest currently supported topology is:
`Electron main/bootstrap -> cade.node -> native CADE -> named pipe / IPC -> renderer preload -> renderer application`.

`cadeDomArguments` is an important bootstrap contract. It proves the native module path and named-pipe endpoint are supplied externally to the renderer process rather than hard-coded inside the preload.

This shifts Pass 33's search target to the Electron main/bootstrap layer and its process spawning or window-creation code. That layer should reveal who constructs `cadeDomArguments` and therefore where the replay/state producer is attached.

## W2 Boundary
No lifecycle event was captured from the reference `.aoe2record` in this pass. Therefore no W2 promotion is justified.

W0: CLOSED.
W1: OPEN.
W2: OPEN.
W3: OPEN.

## AEGIS Consequence
Do not build an AEGIS dependency on CADE's event names alone. The eventual adapter must bind to an observed replay-fed state/event stream and retain provenance.

Scenario-loader automation/testing remains permanently retired.

## Pass Verdict
**PASS 32: ACCEPT.** The native bridge's bootstrap contract is now explicit. The next highest-value target is the main-process code that constructs `cadeDomArguments` and launches the renderer/native state path.
