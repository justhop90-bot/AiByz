# CAL_UNCAGE_ENDPOINT_002 — CA:DE 1.25 native observer-surface recovery

**Date:** 2026-09-05  
**Classification:** RUNTIME CANDIDATE / OBSERVER INFRASTRUCTURE  
**Build target:** AoE2DE `101.103.48987.0`, Steam BuildID `24094652`, update line `#180059`  
**CA:DE installed version:** `1.25.0`

## Purpose

Recover the current CA:DE observer surface from the installed retail CA:DE 1.25 package after the older `delta-play-replay` client failed to qualify `Frames` against the target-build endpoint.

This pass deliberately does **not** claim that the current Frames RPC has been qualified. It establishes what the installed CA:DE 1.25 client actually exposes and how its renderer/IPC stack is wired, so the next experiment can target the current observer path rather than the version-skewed 2024 client.

## Immutable package evidence

Installed package root:

`C:\Users\justh\AppData\Local\Programs\CaptureAge`

`CaptureAge.exe`
- FileVersion/ProductVersion: `1.25.0` / `1.25.0.0`
- SHA-256: `A63931F666E42CD110B55321C4A55AC670AE011995B890184651E182CC684C39`

`resources\app\cade.node`
- size: `15,421,728` bytes
- SHA-256: `C64832B06229D445B4E735BB1A768100B044B64A6A74A32C45710853725BCC61`

`resources\app\package.json` identifies CaptureAge version `1.25.0` and the native/API packages:
- `@captureage/cade-api-cpp`
- `@captureage/cade-api-typescript`
- `@captureage/cade-commons`

## Native export surface

Directly loading the installed `cade.node` in Node exposed these top-level native components:

- `RawServerStreamCall`
- `Renderer`
- `RenderLoop`
- `NamedPipeEndpoint`
- `NamedPipeSender`
- `System`
- `Wrapper`
- `NgfxInjection`
- `AppConfigNative`
- `AtlasDataCollector`
- `ResourceConverter`
- `SoundSystem`

Relevant prototype methods recovered from the native module:

### `RawServerStreamCall`
- `stop`
- `flush`
- `getConnectivityState`

### `Renderer`
- `getWorldTime`
- `getAdapterDesc`

### `RenderLoop`
- `getRenderer`
- `requestFrame`
- `getGameStateId`
- `getAvailableFrameOrWakeUp`
- `postPatch`
- `postLookaheadPatch`
- `postLookaheadPatchMultiple`
- `pollLookaheadGenerateResults`
- `setPatchesRequired`
- `flushEvents`
- `flushExceptions`
- `postUpdateCamera`
- `postUpdateSelectedEntities`
- `postResetState`
- `stop`

### Named-pipe IPC
`NamedPipeEndpoint` exposes:
- `poll`
- `close`

`NamedPipeSender` exposes:
- `send`
- `close`

The native binary contains symbols/strings referencing the CaptureAge source paths:

`C:\actions-runner-2\_work\cade\cade\packages\cade\src\cpp\api\RenderLoopApi.cpp`

and

`C:\actions-runner-2\_work\cade\cade\packages\cade-api-cpp\src\rpc\RawServerStreamCall.cpp`

This is strong provenance for the installed observer/native surface, but it is not a substitute for the source tree or a qualified RPC contract.

## Electron / renderer wiring

`resources\app\electronMain.js` performs:

`cade.init(require)`

and then loads the CaptureAge application.

The live CA:DE DOM application was inspected through its own Electron remote-debugging interface on port `45678`. The page URL was:

`cafile://resources/app/domApp.html`

The live page exposed:
- `ipcRendererTransport`
- `ipcNamedPipeEndpoint`
- `system.getSequenceTime()`

The application boot code creates IPC objects named:
- `main`
- `mainWorker`

and obtains a renderer IPC object through:

`mainWorkerIpc.getRendererIpc()`

The boot path also polls `ipcNamedPipeEndpoint` and forwards JSON messages into the renderer IPC transport.

This establishes that the installed CA:DE 1.25 application has a real native/IPC observer architecture rather than being only a static replay viewer.

## Version-skew finding

The checked-in `delta-play-replay` source still contains an older `cade_api.proto` whose `CadeRemote` service surface is only:

- `Info`
- `Pause`
- `SetFogOfWar`
- `SetPerspective`
- `Frames`

The checked-in generated `cade_api.js`, however, contains materially newer message types including:

- `LoadGameRequest/Response`
- `SetDesiredGameRequest/Response`
- `SetGameSpeedRequest/Response`
- `AccessFlagRequest/Response`
- `ChangeScreenRequest/Response`
- `ChangeWindowStateRequest/Response`
- `CurrentReplay`
- `SelectedGame`
- `SelectedGameInfo`
- `GameState`
- `ScreenState`
- `WindowState`
- `OracleMessage`
- `OraclePrayer`

It also contains additional `FramesRequest` fields beyond the checked-in `.proto`, including `processAttackNotificationsForAllPlayers` and an additional resolution category (`LOW_PRIORITY_2`).

Therefore the checked-in `.proto` must **not** be treated as the current target-build API specification.

## Runtime target endpoint already proven

AoE2DE target build exposed:

`127.0.0.1:4341`

and

`[::1]:4341`

TLS/HTTP2 negotiation succeeded. The endpoint certificate identified itself as `ca-game-api`, issued by the CaptureAge root.

Authenticated `Info` returned:

- `gameVersion = 180059`
- `apiVersion = 20`
- `baseDirectory = C:\Program Files (x86)\Steam\steamapps\common\AoE2DE`

Thus the endpoint and installed CA:DE 1.25 package independently agree on the target build/API identity.

## Current conclusion

### PROVEN

1. CA:DE 1.25.0 is installed and hash-recorded.
2. Its native module is directly loadable and exposes current renderer/frame-related capabilities.
3. The native module contains current CaptureAge gRPC/native infrastructure (`RawServerStreamCall`).
4. The live CA:DE frontend uses IPC/named-pipe transport to communicate with native/main-worker components.
5. The target AoE2DE retail build exposes authenticated CA:DE API endpoint `apiVersion=20`.
6. The old checked-in `cade_api.proto` is version-skewed relative to the generated API artifacts and must not be treated as current ABI authority.

### NOT PROVEN

1. Exact current API-20 service descriptor / RPC surface.
2. Exact current `Frames` request initialization contract.
3. A target-build frame stream delivered through the old Rust/tonic client.
4. That CA:DE's native frame APIs are externally callable from AEGIS without adopting CaptureAge's own application process.
5. Any individual replay-frame field as authoritative world-state semantics until frame decoding is qualified.

## Next experiment

Recover the API-20 contract from the installed CA:DE 1.25 application/native package and qualify the least-invasive frame acquisition route. Prefer, in order:

1. current CA:DE API/client contract already used by the installed application;
2. current native observer bridge if it can be invoked without game injection or memory modification;
3. only then reconsider direct gRPC reconstruction.

Once a real frame stream is obtained, use it to establish the first world-transition evidence gates:

`DE_QUEUE -> individual unit creation`

`BUILD -> building realization`

Do not promote any of these transitions from candidate to proven merely because the CA:DE client can render them.
