# AEGIS World-State Observation Backend Research — 2026-09-05

Status: **CANDIDATE RESEARCH / NOT AUTHORIZED FOR RUNTIME**

## Finding

The replay-body parser is now correctly understood as a command stream plus
SYNC timing, not a tick-by-tick world-state log. This is a hard limitation for
proving `COMMAND -> CREATED -> AVAILABLE -> EFFECTIVE` from `.aoe2record`
alone.

The next observation backend should therefore be an actual engine-replay
state source rather than another replay-file heuristic.

## Candidate A — AoE2DE replay gRPC state-delta interface

The community `librematch/delta-play-replay` project documents an AoE2DE gRPC
endpoint exposed while watching replays and describes it as providing state
deltas.

Its client implementation provides unusually strong concrete evidence:

- endpoint URI used by the reference client: `https://[::1]:4341`;
- HTTP/2 transport;
- TLS with a project-supplied CA and client certificate/key;
- RPC service `CadeRemote`;
- `Frames(FramesRequest) -> stream FrameSequence`;
- each `Frame` contains engine time, state patch, events, reverse patch,
  metrics, and commands;
- RPCs also expose `Info`, `Pause`, `SetFogOfWar`, and `SetPerspective`.

The corresponding model definition contains a real `World` object with:

- `time`;
- `entities` keyed by entity ID;
- `players`;
- `technologies`;
- game state/end state;
- map dimensions and tiles;
- visibility-related data.

The model also explicitly defines production/research/combat structures,
including `ProductionQueueRecord`, `Entity`, `BuildingEntity`,
`ActionEntity`, `CombatEntity`, and `ResearchState`.

This is materially closer to the AEGIS requirement than parsing the `.body`
file because it exposes reconstructed engine state rather than merely the
command stream.

### Security disposition

**UNQUALIFIED.** The repository establishes the existence, transport, RPC
surface, and state model, but AEGIS has not yet proven that the endpoint is
active on the installed retail build, how it is activated, whether its
certificate material is accepted by the current build, or whether accessing
it requires any invasive mechanism.

No runtime ALLOW is granted.

## Candidate B — CaptureAge

Community reverse-engineering documentation identifies CaptureAge as an
engine-replay client capable of producing true resource/unit/army state by
replaying a growing recording through the game engine. CaptureAge's current
public documentation describes CA:DE as an external AoE2DE spectating client
with advanced real-time statistics.

CaptureAge is therefore a useful **gold-standard comparison source**, but not
currently an AEGIS automation dependency. Its internal observation transport
is not an openly specified machine ABI in the material reviewed here.

## Required qualification sequence

1. Acquire the exact `delta-play-replay` source snapshot and hash the source
   files used for the client/protocol definition.
2. Inspect the bundled certificate material and determine its intended scope.
3. Start the exact target AoE2DE build in a disposable single-player replay.
4. Probe only the documented localhost endpoint; do not inject, patch, or
   modify the game process.
5. Call `Info` first and record `gameVersion` / `apiVersion` if the endpoint
   accepts the connection.
6. Request a minimal `Frames` stream with no optional command/control use.
7. Decode one frame and prove `World.time` plus one known entity identity.
8. Test `DE_QUEUE -> ProductionQueueRecord -> Entity` as the first lifecycle
   experiment.
9. Test `BUILD -> BuildingEntity` as the second lifecycle experiment.
10. Correlate engine time from the gRPC frame with cumulative replay SYNC time.
11. Record exact build hash, adapter source hash, endpoint details,
    certificates, timestamps, and teardown evidence.
12. Only then consider this backend for AEGIS machine-semantic qualification.

## Why this is the correct next experiment

The project has reached the point where further replay parsing cannot close the
missing causal gates. We now have a concrete, externally documented route to
actual reconstructed engine state. The engineering objective is therefore to
qualify that observation channel—not to invent increasingly elaborate
heuristics over an inherently incomplete replay file.
