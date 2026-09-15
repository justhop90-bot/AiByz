# CAL_UNCAGE_ENDPOINT_001 — Target-Build CADE/UnCage Endpoint Probe

Date: 2026-09-05

## Purpose

Determine whether the target retail AoE2DE build exposes the CADE/UnCage-style local game API on the machine, whether the endpoint can be authenticated and identified independently, and whether the existing `delta-play-replay` client is sufficient to obtain a frame stream.

This is a **qualification probe**, not a claim that the endpoint is an approved AEGIS production dependency.

## Target build

- Executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- Build ID: `24094652`
- Update line: `#180059`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

## Observed endpoint

During replay/runtime observation, the retail process listened on:

- `127.0.0.1:4341`
- `[::1]:4341`
- owning process: `AoE2DE_s.exe`

A direct TLS connection established:

- TLS: `TLSv1.3`
- ALPN: `h2`
- peer certificate SHA-256: `896e6aae0457b971b2a84f4421a1b2f3ee3afe0cb08d519244db48b2655caf14`
- peer certificate subject CN: `ca-game-api`
- peer certificate issuer: `CaptureAge Root Certificate`

The endpoint therefore exists in the target retail build and is not merely an offline source-code artifact.

## gRPC authentication / Info RPC

Using the CaptureAge certificate material shipped with the inspected `delta-play-replay` client, the endpoint accepted a mutually authenticated gRPC connection when the TLS authority was set to `ca-game-api`.

`Info` returned:

- `gameVersion = 180059`
- `apiVersion = 20`
- `baseDirectory = C:\\Program Files (x86)\\Steam\\steamapps\\common\\AoE2DE`

The returned game version independently matches the target build/update identity.

## Frame-stream result

The existing `delta-play-replay` / UnCage client was used against the live target endpoint.

`Info` succeeds.

`Frames` does **not** yet produce a frame sequence. Observed outcomes included:

- `DEADLINE_EXCEEDED`
- `CANCELLED`
- `UNAVAILABLE: Stream removed ... connection reset`

These results do **not** establish that the target engine lacks a frame stream. They establish only that the existing client/protocol combination has not yet been qualified to obtain one from this build/state.

## Critical protocol provenance finding

The checked-in `delta-play-replay` source is internally version-skewed.

Its checked-in `crates/uncage-client/proto/cade_api.proto` currently declares only the older service surface:

- `Info`
- `Pause`
- `SetFogOfWar`
- `SetPerspective`
- `Frames`

However, the repository's generated `cade_api.js` exports a materially newer API surface containing message types including:

- `LoadGameRequest/Response`
- `SetDesiredGameRequest/Response`
- `SetGameSpeedRequest/Response`
- `AccessFlagRequest/Response`
- `ChangeScreenRequest/Response`
- `ChangeWindowStateRequest/Response`
- `FramesRequest`
- `InfoRequest/Response`
- `PauseRequest/Response`
- `SetFogOfWarRequest/Response`
- `SetPerspectiveRequest/Response`

The generated JavaScript also defines replay-loading state (`LoadGameRequest.LoadReplay`) and current-replay metadata (`CurrentReplay`). Therefore the checked-in `.proto` file cannot currently be treated as the authoritative target-build API definition.

This version skew is a credible explanation for why the old client can successfully call `Info` yet cannot currently establish a usable `Frames` stream. It must be resolved before making any judgment about the target API's state-observation capability.

## Current CaptureAge installation evidence

Installed CA:DE:

- FileVersion: `1.25.0`
- ProductVersion: `1.25.0.0`
- CaptureAge.exe SHA-256: `A63931F666E42CD110B55321C4A55AC670AE011995B890184651E182CC684C39`
- `cade.node` exports include `Renderer.getWorldTime`, `RenderLoop.getRenderer`, `RenderLoop.requestFrame`, `RenderLoop.getAvailableFrameOrWakeUp`, `RenderLoop.getGameStateId`, `RenderLoop.postPatch`, `AtlasDataCollector.applyPatch`, and `RawServerStreamCall`.

This is important because the current CADE native module itself contains a world-state/frame abstraction. It is stronger evidence of an observer path than the stale UnCage `.proto` alone.

## Security/TLS note

The shipped `certificate-authority.pem` is an old v1 self-signed certificate and is rejected by Python/OpenSSL as a CA because of its certificate constraints. The gRPC client nevertheless successfully established the target connection using the same CaptureAge certificate material.

The old `delta-play-replay` client also contains hostname-verification workarounds that are no longer justified by the observed target certificate: the target peer certificate identifies itself as `ca-game-api`.

This is a research-infrastructure concern. It is not a reason to weaken AEGIS security controls; it is a reason to make the target-build transport configuration explicit and independently qualified.

## Qualification result

### PROVEN

- Target retail build exposes a local TLS/HTTP2 endpoint on port 4341 during runtime/replay conditions.
- Endpoint identifies the target game build as `gameVersion=180059`.
- Endpoint API version observed as `20`.
- Mutual TLS/gRPC `Info` call succeeds with the inspected CaptureAge credentials.
- Current CA:DE 1.25 native module contains direct renderer/world-time/frame APIs.

### OPEN

- Obtain a target-build frame stream through a version-matched API/client.
- Establish whether current CADE's native `Renderer`/`RenderLoop` path can be externally harnessed without invasive injection or memory modification.
- Correlate an independently observed entity birth with `DE_QUEUE`.
- Correlate building realization with `BUILD`.

### REJECTED

- Treating the checked-in `delta-play-replay` `.proto` as the current target-build API specification.
- Treating `Info` success as proof that `Frames` is qualified.
- Treating a `Frames` failure from the stale client as proof that the retail engine cannot emit state frames.
- Promoting CADE/UnCage to an AEGIS production dependency based solely on source inspection.

## Next experiment

The next engineering task is **API-version reconciliation**, not another replay-parser rewrite:

1. recover the current CADE 1.25 API/protocol surface from the installed/native client;
2. establish the exact current RPC/service contract for `Frames` and replay loading;
3. obtain a frame stream from the target build using the least-invasive available route;
4. only then implement the `DE_QUEUE -> CREATED` and `BUILD -> REALIZED` correlation experiment.
