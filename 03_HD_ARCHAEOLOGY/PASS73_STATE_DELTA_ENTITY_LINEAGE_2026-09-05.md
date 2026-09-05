# Pass 73 — State-Delta Entity Lineage Archaeology

**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Status:** PASS WITH MAJOR LEAD — an engine-backed state-delta path exposes entity/world-state concepts, but individual train-command → created-object lineage remains uncertified.

## Mission

Attack the Pass-72 boundary by determining whether an engine-backed replay/state-delta representation can provide the missing object identity required to connect production commands to actual world objects.

## Executive finding

Independent public archaeology identifies an AoE2DE project, `librematch/delta-play-replay`, explicitly built to communicate with the gRPC API exposed by AoE2DE during replays and to construct a delta-based replay representation. Its stated background distinguishes the CaptureAge `.cars/.carz` replay representation from the recorded-game command stream.

The project therefore provides direct evidence that an AoE2DE replay-time interface can expose richer state than the raw `.aoe2record` command stream.

The strongest defensible model is now:

```text
.aoe2record
    ↓
recorded commands
    ↓
AoE2DE replay simulation
    ↓
state deltas
    ↓
world/entity state
    ↓
object lifecycle
```

This is a substantially stronger route to L8 object birth than raw `mgz-fast` parsing alone.

It does **not** yet close L8, because we have not demonstrated an exact production-command → queue-entry → entity-ID mapping on the project's target replay.

## 1. Independent replay-source evidence

`librematch/delta-play-replay` describes itself as tooling for communicating with the gRPC API exposed by AoE2DE during replays. It also states that CaptureAge uses an internal `.cars/.carz` representation for replaying recorded games without running the original simulation.

This establishes three distinct layers:

```text
RAW RECORDED GAME
        ↓
COMMAND / INPUT REPRESENTATION

ENGINE REPLAY
        ↓
SIMULATED WORLD STATE

CAPTUREAGE / DELTA REPRESENTATION
        ↓
STATE DELTAS FOR CONSUMERS
```

The distinction is important: a command parser and an engine-backed state consumer answer different forensic questions.

## 2. Object identity is a separate evidence dimension

Historical AoE2 format archaeology establishes that unit IDs identify a **unit type**, while object IDs identify a **specific object during a game**. New objects receive incrementing IDs in the documented legacy format model.

Therefore the desired evidence is not merely:

```text
unit type = camel
```

but:

```text
object ID = X
unit type = camel
owner = Byzantine player
creation = T
```

That is the resolution required for individual object lineage.

## 3. State-delta representation

The publicly indexed delta-play-replay material describes a delta representation in which world/entity state is reconstructed from state changes. Its source model includes an entity collection and explicit object/entity lifecycle concepts.

The relevant conceptual operations are:

```text
CREATE
UPDATE
LEAVE / DELETE
```

The important forensic property is that creation is represented as a state transition rather than inferred solely from a later aggregate count.

## 4. Production action representation

Independent modern AoE2DE replay parsing exposes production-related action families including:

```text
AI_TRAIN
TRAIN
QUEUE
DE_QUEUE
MULTIQUEUE
```

and production actions can contain player identity, building identity, unit/type identity, and related parameters depending on the action family.

This means the command side can potentially provide:

```text
player
building
unit type
command time
```

while the state-delta side can potentially provide:

```text
object ID
owner
unit type
creation time
state
position
```

The missing operation is therefore a correlation problem rather than an absence-of-data problem.

## 5. Required correlation test

The minimum acceptable object-birth proof should look like:

```text
TRAIN COMMAND
player = P
building = B
unit type = U
sequence/time = T0
        ↓
QUEUE / PENDING
building = B
unit type = U
        ↓
CREATION DELTA
object ID = O
owner = P
unit type = U
creation time = T1
        ↓
OBJECT STATE
object ID = O
position = (x,y)
```

Only after this chain is independently reproduced should L8 be promoted.

## 6. Temporal matching is necessary but not sufficient

A simple rule such as:

```text
first camel creation after train camel
```

is still insufficient where multiple camels are simultaneously queued or training.

Likewise:

```text
camel population +1
```

cannot establish object identity.

Temporal proximity becomes useful only when combined with stronger discriminators such as producer identity, queue state, unit type, and exact object creation events.

## 7. Stronger matching hierarchy

The evidence hierarchy should now be expanded:

```text
LEVEL 1 — exact object ID / creation event
LEVEL 2 — exact producer + queue transition + creation event
LEVEL 3 — exact type + producer + temporal + spatial state
LEVEL 4 — exact type + temporal population transition
LEVEL 5 — aggregate correlation
LEVEL 6 — heuristic inference
```

Only Levels 1–3 should normally close an individual command → object lineage claim.

Levels 4–6 can support hypotheses but should not silently promote them to causal closure.

## 8. What the AoE2DE command format cannot prove alone

A recorded `TRAIN` action establishes that a production action was recorded. It does not itself prove that the engine successfully completed the production.

Similarly:

```text
TRAIN
≠ QUEUED
≠ COMPLETED
≠ CREATED
```

This remains a fundamental Layer-2 invariant.

## 9. Why the engine-backed path matters

The public `mgz` documentation explicitly states that arbitrary-time resources, kills, and similar world-state quantities cannot simply be recovered from the recorded file without replaying the match in-game. The file consists of an initial state followed by recorded moves that mutate state according to the game rules.

This directly supports the separation:

```text
PARSER FORENSICS
→ command chronology

ENGINE REPLAY FORENSICS
→ reconstructed world chronology
```

The object-birth problem belongs primarily to the second category.

## 10. Current status of the Byzantine camel case

The historical AI evidence already establishes the command-side chain:

```text
mounted threat
↓
camel response conditions
↓
producer search
↓
can-train
↓
train camel-line
```

Replay evidence independently corroborates concrete camel-line train actions.

Pass 73 now identifies a plausible state-side route for closing:

```text
train camel-line
↓
engine replay
↓
creation delta
↓
camel object ID
```

But this specific correlation has not yet been executed and verified.

Therefore the formal evidence grade remains:

```text
L0–L6  CLOSED / STRONG
L7     PARTIAL
L8     OPEN — HIGH-VALUE TARGET
L9     OPEN
L10    OPEN
L11    OPEN
```

## 11. CaptureAge interpretation

Earlier CADE archaeology identified entity and production-state vocabulary including combat-unit creation and production queue records.

The new state-delta archaeology strengthens the hypothesis that CADE is consuming or representing a richer engine-backed replay state rather than merely decoding the raw command stream.

However, no claim is made here that CADE itself provides a stable public extraction API for arbitrary `.aoe2record` → object lineage.

The correct status remains:

```text
ENGINE-BACKED STATE PATH = CONFIRMED AS A RESEARCH TARGET
CADE AS CERTIFIED OBJECT-LINEAGE ORACLE = NOT PROVEN
```

## 12. Critical new research target

The next empirical test should not be another generic parser search.

It should seek one concrete replay and attempt to produce this ledger:

```text
command_seq
command_time
player
producer/building
unit_type
queue_state
creation_time
object_id
owner
spawn_position
```

For a Byzantine Camel case, success would be:

```text
TRAIN CAMEL #N
        ↓
QUEUE ENTRY #N
        ↓
OBJECT ID #M CREATED
        ↓
OBJECT TYPE = CAMEL
        ↓
OWNER = BYZANTINE PLAYER
```

If the state-delta interface cannot provide enough information, the failure should be documented as an interface limitation rather than treated as parser failure.

## 13. Hostile QC

Rejected claims:

- existence of an entity model = proof of our Camel lineage
- object creation operation = proof that every recorded train is represented
- object count increase = exact object identity
- temporal proximity = causality
- CaptureAge internal state = stable public API
- gRPC replay state = automatically accessible from every `.aoe2record`
- legacy object-ID behavior = automatically identical to every current DE internal implementation

## 14. Layer-2 disposition

Pass 73 materially reduces uncertainty around the object-birth frontier.

Before this pass:

```text
DO WE EVEN HAVE A STATE-SIDE ROUTE?
```

After this pass:

```text
YES — A REPLAY-TIME STATE-DELTA ROUTE IS DOCUMENTED.
```

The remaining question is now concrete:

```text
CAN WE EXTRACT AND CORRELATE THE STATE DELTA
WITH THE EXACT TRAIN COMMAND IN OUR TARGET REPLAY?
```

That is the next empirical target.

**No `.per` implementation. No runtime deployment. No architectural promotion.**
