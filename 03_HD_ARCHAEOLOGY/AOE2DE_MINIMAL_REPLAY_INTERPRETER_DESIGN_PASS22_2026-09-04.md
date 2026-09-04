# AEGIS Layer 2 — Pass 22
## Minimal Deterministic Replay Interpreter Design
**Date:** 2026-09-04
**Status:** WORKING CANON — DESIGN / PROTOTYPE BOUNDARY

## Mission

Following Pass 21 raw replay archaeology and Pass 22 playback/state-reconstruction archaeology, define the smallest deterministic interpreter capable of advancing replay evidence from command/event telemetry toward W1/W2/W3 without pretending to be an AoE2 simulator.

## Evidence boundary

The established pipeline is:

`RAW RECORDING → PARSER DECODING → NORMALIZED EVIDENCE → STATEFUL RECONSTRUCTION`

The interpreter is the fourth layer. It MUST preserve provenance for every state field:

`DIRECT_REPLAY | PARSED_SNAPSHOT | DERIVED | HEURISTIC | UNKNOWN`

No derived state may silently become authoritative state.

## What existing playback teaches us

Existing replay-viewer approaches demonstrate that useful time-indexed state can be reconstructed without implementing the complete game. They also demonstrate the principal failure mode: heuristic reconstruction can look authoritative while lacking an engine-backed completion signal.

Therefore AEGIS should not copy a viewer's simulation wholesale. It should build an evidence-preserving state machine targeted at the questions needed by strategic archaeology and later bot validation.

## Minimal state model

### Player
- player_id
- civilization
- age
- population estimate
- aggregate resource values when directly exposed
- known commands
- confidence/provenance per field

### Object
- stable replay-visible identifier when available
- owner
- type_id
- position
- alive/removed state
- last-seen timestamp
- provenance

### Pending operation
- command sequence
- command type
- actor/producer/builder IDs when exposed
- target type/object
- coordinates
- issue time
- expected postcondition
- completion evidence
- failure evidence
- confidence

### Capability
- available
- pending
- realized
- operational
- strategically inferred

These are deliberately distinct states.

## Event transition contract

For every replay event:

`OBSERVE → CLASSIFY → APPLY ONLY SUPPORTED TRANSITION → RECORD PROVENANCE → EMIT POSTCONDITION CANDIDATE`

Examples:

### DE_QUEUE
Observed:
`producer IDs + unit ID + amount`

Allowed transition:
`producer issued production request; pending production candidate exists`

Not allowed:
`unit exists`

### BUILD
Observed:
`building ID + coordinates + builder IDs`

Allowed:
`construction command issued; construction candidate pending`

Not allowed:
`building completed`

### RESEARCH
Observed:
`technology ID + research object ID`

Allowed:
`research request issued`

Not allowed:
`technology completed`

### DELETE
Observed:
`object ID/player`

Allowed:
`delete command observed; object-removal candidate`

Not automatically allowed:
`complete lifecycle reconstruction`

## Object identity strategy

Identity is strongest when an object ID is directly exposed and can be observed again. A new object should be created in the interpreter only when evidence supports creation/realization. Aggregate population or object-count deltas MUST NOT manufacture individual identities.

When identity cannot be proven:

`UNKNOWN_OBJECT` is preferable to fabricated lineage.

## W1 closure criteria

W1 becomes CLOSED for a transition only if the replay provides an authoritative accepted/pending representation or an independently validated state channel. A command alone is W0.

## W2 closure criteria

W2 for an individual object requires sufficient evidence for:
1. identity,
2. existence/realization,
3. ownership,
4. type,
5. temporal placement.

Position/type from an initial snapshot does not by itself prove later realization.

## W3 closure criteria

W3 requires evidence that the realized object/capability is operationally usable, not merely that a command was issued or an object existed.

## Temporal model

Preserve the replay action sequence as the primary ordering key where observed. It is monotonic in the calibrated reference but is not unique, so simultaneous commands are legal.

Never use ACTION count as elapsed game time.

Where a timestamp/current-time field exists, retain it separately. Do not collapse sequence and game time until their relationship is independently established.

## Minimal interpreter phases

### Phase A — Event normalization
Convert parser outputs into canonical event records without changing semantics.

### Phase B — Snapshot initialization
Load only directly supported initial objects/player/map data.

### Phase C — Pending ledger
Create pending-operation records for commands that imply a future postcondition.

### Phase D — Evidence matching
Search later observations for evidence compatible with the pending operation.

### Phase E — State transition
Promote a pending candidate only when its evidence threshold is met.

### Phase F — Confidence/provenance emission
Every promoted field carries source class and confidence.

### Phase G — Strategic projection
Only after the lower-level state is established may the interpreter emit capability or strategic implications.

## Matching rules

Use conservative matching priority:

1. exact object ID
2. exact producer/builder/actor ID + operation type
3. exact type + temporal window + spatial proximity
4. aggregate correlation
5. heuristic inference

Levels 4–5 cannot close W2.

## Required negative tests

The interpreter must prove it does NOT:
- convert DE_QUEUE into a spawned-unit event automatically;
- convert BUILD into completed-building state automatically;
- convert RESEARCH into completed-tech state automatically;
- infer individual births from population deltas;
- infer individual deaths from aggregate count deltas;
- confuse parser capability with replay occurrence;
- confuse viewer heuristic state with authoritative state;
- claim full simulation fidelity.

## Initial implementation target

The first implementation should support only:

`PLAYER | OBJECT | PENDING_OPERATION | RESOURCE_AGGREGATE | TIME/SEQUENCE | PROVENANCE`

and only the operations already strongly represented in the reference corpus:

`MOVE | ORDER | BUILD | DE_QUEUE | RESEARCH | DELETE | DE_ATTACK_MOVE | REPAIR | UNGARRISON | GATHER_POINT`

Everything else remains an opaque event until specifically qualified.

## Validation corpus

Minimum validation set:
- 2026-09-02 reference replay;
- 2026-08-29 replay used in Pass 16;
- one additional replay with contrasting production/tech activity;
- known historical `.per` observation patterns as a separate semantic comparison set.

The interpreter must be deterministic: identical normalized evidence must produce identical state output.

## Architectural consequence

AEGIS does not need a full AoE2 simulator to reason about replay-derived strategic state. It needs a conservative evidence interpreter whose central invariant is:

> **When the evidence cannot prove the transition, preserve the uncertainty instead of inventing the transition.**

This is the bridge from archaeology to engineering.

## Open questions

1. Can an existing full replay implementation expose stable object lineage for DE without heuristic invention?
2. Which DE sync structures can be decoded into authoritative state rather than aggregate telemetry?
3. Can action sequence + object IDs provide deterministic pending-operation matching across the reference corpus?
4. Which lifecycle transitions can be closed using independent evidence from replay playback?
5. What is the smallest state required to reproduce historical `.per` observation semantics?

## Disposition

**PASS 22: ACCEPT — MINIMAL INTERPRETER BOUNDARY ESTABLISHED.**

This pass does not claim W2 closure. It establishes the engineering specification for attempting W2 closure without reopening the retired scenario-loader or constructing a full simulator.