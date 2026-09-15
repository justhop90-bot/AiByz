# CA:DE World-State Observation Qualification — CAL_CADE_WORLD_STATE_002

**Date:** 2026-09-05  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`  
**Observer:** CaptureAge `1.25.0` normal replay path  
**Replay:** canonical calibration replay `MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`  
**Evidence class:** target-build runtime observation  
**Disposition:** **QUALIFIED OBSERVATION BACKEND; NOT A PRODUCTION DEPENDENCY**

## Objective

Perform the final focused CA:DE pass: determine whether the current CA:DE path exposes more than rendered frames and elapsed world time, specifically whether it publishes coherent patch/state progression and actual entity/world-state data.

## Method

CA:DE was launched normally with its existing replay UI path. No process injection, memory writes, patching, debugger attachment, or modification of AoE2DE was used. The CA:DE DOM remote-debugging endpoint was used only to read CA:DE's own named-pipe IPC publication queue.

The target game exposed the normal local gRPC endpoint on port 4341. CA:DE's own worker connected to it and replayed the canonical recording.

A 10.6-second IPC capture collected 24 poll intervals containing stream-3 loop/state publications and stream-4 frame publications.
## Results

### Loop/state progression

The captured loop-state stream showed:

- `loopCount`: 13175 → 14106;
- `applyPatchId`: 4375 → 4731;
- `worldTime`: 219947 → 237744;
- `lookaheadApplyPatchId`: 4425 → 4781;
- `lookaheadWorldTime`: 222443 → 240240;
- `rendererWorldTime` tracked the published world time, with brief observed lag at individual samples;
- `sourceType`: `grpc` throughout the captured state samples;
- `lastLoopNumberPatchesApplied` was observed as both 0 and 1.

The lookahead relationship was particularly stable: it was 50 patch IDs ahead and approximately 2,496–2,509 world-time units ahead in the captured samples.

### Frame/state publication

Stream 4 simultaneously published frame records with `gameStateId`, dimensions, camera state, and a shared texture handle. In the capture:

- frame: 7419 → 8039;
- gameStateId: 4371 → 4730;
- resolution remained 1920×1080.

The frame stream therefore continued advancing alongside the runtime state stream; however, frame number and gameStateId are not treated as semantically interchangeable without further qualification.
### Actual entity/world-state evidence

The same stream-3 publications contained `uiStatePatches` carrying concrete world-state records, including `memMap` entries with fields such as:

- `entityId`;
- `ownerId`;
- `masterIdentity` / `masterId`;
- `currentAction`;
- `productionQueue`;
- `constructionProgress`;
- world coordinates `x` / `y`;
- visibility and fog fields.

Observed examples included production-state records for master identity `83_15_5606`, with changing production progress and remaining time, and minimap/entity records with concrete entity IDs and coordinates.

This is materially stronger than a renderer-only observation path. CA:DE is receiving and publishing structured game-state information reconstructed from the target engine's replay execution.

## What this proves

1. CA:DE can normally drive the target retail build into replay execution.
2. The target build exposes advancing `worldTime` through the CA:DE observation path.
3. The target build exposes a continuing patch/state progression (`applyPatchId`, lookahead fields).
4. CA:DE publishes frame records and associated game-state identifiers.
5. CA:DE publishes structured entity/world-state records, not merely pixels.
6. The observation path can be consumed externally from CA:DE's own IPC without modifying the target executable.
## What this does NOT prove

This pass does **not** establish:

- formal units for `worldTime`;
- exact identity between CA:DE `worldTime` and replay SYNC raw units;
- formal semantics of `applyPatchId` or `gameStateId`;
- a stable one-to-one entity lineage across every patch;
- `DE_QUEUE → CREATED` causal completion;
- `BUILD → REALIZED` causal completion;
- that CA:DE can be required by AEGIS at runtime;
- that CA:DE's private IPC surface is a supported public API.

In particular, the presence of `productionQueue` is evidence of observed runtime state, not proof that a preceding replay `DE_QUEUE` command caused a specific later entity to be created. That requires a controlled lifecycle experiment.

## Final CA:DE disposition

**PROMOTE:** CA:DE as an optional independent runtime observation/adjudication backend for later testing.

**DO NOT PROMOTE:** CA:DE as an AEGIS architectural dependency, authoritative ABI source, or command-completion oracle.

The original question — whether the CA:DE investigation is practical and can be deferred to runtime testing — is now answered decisively: **yes.** The observation capability is sufficiently established that continued CA:DE archaeology is no longer an architecture blocker. The remaining lifecycle questions belong in the controlled runtime campaign.
