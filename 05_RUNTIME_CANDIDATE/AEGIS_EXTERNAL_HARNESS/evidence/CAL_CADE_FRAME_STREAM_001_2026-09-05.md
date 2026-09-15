# CAL_CADE_FRAME_STREAM_001 — target-build CA:DE 1.25 frame stream

**Date:** 2026-09-05  
**Target AoE2DE:** `101.103.48987.0` / Steam BuildID `24094652` / update `#180059`  
**CA:DE:** `1.25.0`  
**Replay:** `MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`  
**Replay SHA-256:** `41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

## Result

**PROVEN: a real target-build CA:DE frame stream is being published by the installed CA:DE 1.25 application while the retail AoE2DE build is replaying the canonical calibration replay.**

This closes the earlier `Frames via old client` uncertainty at the level of the installed CA:DE observer pipeline. It does **not** yet qualify every frame field as authoritative game-state semantics.

## Runtime chain observed

The CA:DE 1.25 application was driven through its own normal replay-selection path. Its own log recorded:

- `19:36:26.243` — `gameIntegration/loadReplay/fromCadeExpanded`
- `19:36:27.255` — worker launched the target `AoE2DE_s.exe`
- `19:36:27.316` — worker invoked PID `15940`
- `19:37:07.183` — game install directory identified
- `19:37:07.194` — selected game `EMPIRES2`
- `19:37:17.199` — worker told the game to load the canonical replay
- `19:37:46.180` — `ensureSelectedGame: EMPIRES2`
- `19:37:47.316` — `gameStart`, selected game `phoenix`
- `19:37:47.662` — remote-state signaller ready
- `19:38:09.797` — `apiMetrics` reported `worldTime=4212`

The AoE2 process then exposed the local CA:DE API endpoint on TCP `4341`, owned by the target AoE2 process.

## Live CA:DE IPC observation

The running CA:DE DOM application was inspected through its own Electron debugging interface. `ipcNamedPipeEndpoint.poll()` yielded two important application streams:

### Stream 3 — loop/state publication

Observed message value contains:

- `loopStateId = b38f588c-5453-4d1f-87b7-d4e2a5529b92`
- `selectedGame = 1`
- `loopCount` increasing
- `worldTime`
- `lookaheadWorldTime`
- `applyPatchId`
- `lookaheadApplyPatchId`
- `publisherTime`
- `loopSpeed`
- `sourceProperties.sourceType = grpc`
- `sourceProperties.sourceDetails = localhost`

### Stream 4 — frame publication

Observed message value contains:

- `frame` — numeric frame handle
- `targetId = 0`
- `sharedTextureHandle = 40001342`
- `width = 1920`
- `height = 1080`
- `gameStateId`
- camera projection/view matrices
- timing metadata

A 9.829-second capture contained:

- **142** published messages
- **48** loop/state messages
- **94** frame messages
- loop count `16016 → 16823`
- frame handle `8447 → 9031`
- frame `gameStateId = 3415`
- loop `applyPatchId = 3415`

The repeated equality between frame `gameStateId` and loop `applyPatchId` is a strong candidate for state/frame coherence, but it is **not yet promoted to a formal semantic invariant**.

## Important qualification

During this capture the replay's published `worldTime` remained at `172107` and `applyPatchId` remained `3415`, while the render frame handle and loop count continued increasing. Therefore:

- frame publication is proven;
- render-loop activity is proven;
- repeated frame publication does **not** imply world-state advancement;
- `worldTime` and patch IDs remain distinct from render-frame cadence;
- the frame handle is not itself a world-state object identifier.

A separate progression capture is required to qualify world-state transitions.

## What this closes

1. The old Rust/tonic client's `Frames` failure is no longer evidence against the target observer capability.
2. The installed CA:DE 1.25 application demonstrably receives/publishes frame data from the target-build runtime.
3. The observer path is version-matched to the installed CA:DE package and target game build.
4. AEGIS now has a concrete candidate acquisition surface for the first runtime world-transition experiments.

## What remains open

- Exact API-20 protobuf/service authority.
- Semantic decoding of the native frame handle / shared texture.
- Formal meaning of `gameStateId` and `applyPatchId`.
- World-time progression and patch-generation semantics.
- Individual entity identity/lifecycle from the observer surface.
- `DE_QUEUE → CREATED`.
- `BUILD → REALIZED`.

## Disposition

**PROMOTE:** target-build CA:DE frame-stream existence as runtime evidence.  
**DO NOT PROMOTE:** CA:DE frame fields as authoritative world-state semantics.  
**DO NOT PROMOTE:** CA:DE itself as an AEGIS production dependency.

The external-harness branch remains the correct quarantine boundary for this observer infrastructure.
