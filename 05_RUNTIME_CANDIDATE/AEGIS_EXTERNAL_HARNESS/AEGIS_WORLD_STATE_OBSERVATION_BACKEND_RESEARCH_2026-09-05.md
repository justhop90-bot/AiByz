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
deltas. Its model definition includes a real `World` object containing:

- `time`;
- `entities` keyed by entity ID;
- `players`;
- `technologies`;
- game state/end state;
- map dimensions and tiles;
- visibility-related data.

The same model includes explicit production/state types such as
`ProductionQueueRecord`, `Entity`, `BuildingEntity`, `ActionEntity`,
`CombatEntity`, and `ResearchState`.

This is materially closer to the AEGIS requirement than parsing the `.body`
file because it exposes reconstructed engine state rather than merely the
command stream.

### Security disposition

**UNQUALIFIED.** The repository establishes the existence and semantics of the
replay gRPC surface, but this record does not yet prove the endpoint's exact
activation method, transport address, permissions, or whether using it on the
installed retail build requires any invasive mechanism.

No runtime ALLOW is granted.

## Candidate B — CaptureAge

Community reverse-engineering documentation identifies CaptureAge as an
engine-replay client capable of producing true resource/unit/army state by
replaying a growing recording through the game engine. CaptureAge's own current
documentation confirms it is an external AoE2DE spectating client with advanced
real-time statistics.

CaptureAge is therefore a useful **gold-standard comparison source**, but not
currently an AEGIS automation dependency. Its internal observation transport
is not an openly specified machine ABI in the material reviewed here.

## Required qualification sequence

1. Acquire the exact `delta-play-replay` source snapshot and inspect the gRPC
   client/transport implementation.
2. Identify the endpoint activation mechanism and security boundary.
3. Determine whether the installed retail build exposes the endpoint during a
   local single-player replay.
4. Connect only in a disposable replay session.
5. Capture a minimal state delta containing `World.time` and one known entity.
6. Correlate that entity identity with an independently known replay action.
7. Test `DE_QUEUE -> ProductionQueueRecord -> Entity` as the first lifecycle
   experiment.
8. Test `BUILD -> building Entity` as the second lifecycle experiment.
9. Record exact build hash, adapter source hash, endpoint details, timestamps,
   and teardown evidence.
10. Only then consider this backend for AEGIS machine-semantic qualification.

## Why this is the correct next experiment

The project has reached the point where further replay parsing cannot close the
missing causal gates. We now have a concrete, externally documented route to
actual reconstructed engine state. The engineering objective is therefore to
qualify that observation channel—not to invent increasingly elaborate
heuristics over an inherently incomplete replay file.
