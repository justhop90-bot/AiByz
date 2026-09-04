# AoE2DE Runtime Controlled Observability — Pass 16

**Date:** 2026-09-04  
**Layer:** 2 — HD/Promisory archaeology and practical strategy reconstruction  
**Mission:** Attack the missing W2 bridge in production lifecycle evidence without reopening the failed scenario-loader automation.

## 1. Executive result

Pass 16 performed a direct runtime/replay observability audit on the reference recording and the installed replay parser/toolchain.

**Verdict: production replay lineage remains CLOSED AT W1, NOT W2.**

The investigation did, however, recover an important structural fact that was previously only implicit: the replay parser's `DE_QUEUE` record contains the **producer object identity**, requested unit type, quantity, player, and simulation sequence. It does **not** contain an identity for the unit object subsequently created by that queue operation.

The reference replay therefore supports:

`QUEUE COMMAND -> PRODUCER OBJECT + UNIT TYPE + AMOUNT -> PENDING/COMMAND EVIDENCE`

but not, by itself:

`QUEUE COMMAND -> CREATED UNIT OBJECT ID -> OBSERVED AVAILABLE UNIT`.

No scenario-loader automation was reopened. No claim of W2 completion was manufactured from later movement/order activity.

## 2. Evidence inspected

### 2.1 Reference replay

Reference body:
`C:\Users\justh\Desktop\AEGIS-AI-LAB\06_REPLAYS\08_FORENSIC_RUNS\2026-09-02_REFERENCE\body_fresh.jsonl`

Observed operation inventory:

- SYNC: 9,876 in the first 20,000-record sample; full reference remains the established 597,681-event corpus.
- ACTION: 6,858 in the established full corpus.
- DE_QUEUE: 1,493.
- MOVE: 2,640.
- ORDER: 904.
- BUILD: 471.
- RESEARCH: 118.
- DE_ATTACK_MOVE: 72.
- DELETE: 33.
- Other action categories include gather-point, patrol, formation, stance, repair, trade, scouting, and control actions.

The full-corpus action counts match the prior Pass 14/15 inventory.

### 2.2 Rich SYNC records

Rich SYNC records were inspected directly. Their third payload element can contain:

- `current_time`
- per-player aggregate `total_res`
- per-player `dp_obj_count`
- per-player `dp_obj_ttl`
- per-player `obj_count`

Example observed shape:

`[25, 515842, {"current_time": 16170, "1": {"total_res": 650, "dp_obj_count": 24, "dp_obj_ttl": 300, "obj_count": 14}, "2": {"total_res": 450, "dp_obj_count": 24, "dp_obj_ttl": 300, "obj_count": 14}}]`

This is aggregate object-state information, not a normalized object ledger with per-object identity/type/lifecycle fields.

### 2.3 Installed parser implementation

The installed `mgz.fast` implementation was inspected directly rather than treating the JSONL projection as an opaque black box.

`mgz.fast.operation()` dispatches body operations to `action()`, `sync()`, `viewlock()`, `chat()`, and `postgame()` handlers.

`mgz.fast.action()` reads the action type, action bytes, and sequence, then dispatches to `parse_action()`.

The current `parse_action()` implementation explicitly handles `Action.DE_QUEUE` as:

```text
player_id, unit_id, amount, *object_ids = struct.unpack_from(
    '<b4xhbx' + str(data[3]) + 'I', data)
)
return dict(
    player_id=player_id,
    object_ids=object_ids,
    amount=amount,
    unit_id=unit_id
)
```

The crucial interpretation is structural: `object_ids` in this DE_QUEUE parser are the objects participating in the queue command. They are **producer-side object IDs**. The payload does not expose a newly-created unit object ID.

A direct replay example was observed:

```json
{"op":"ACTION","payload":["DE_QUEUE",{"player_id":2,"object_ids":[1],"amount":1,"unit_id":83,"sequence":3579}]}
```

Thus `object_ids:[1]` identifies the queueing object in this record; `unit_id:83` identifies the requested unit type; `amount:1` identifies quantity.

## 3. Critical negative result

The tempting inference is:

`DE_QUEUE(unit X) -> later MOVE(object Y) -> Y is the completed X`.

Pass 16 rejects this inference.

The recording contains MOVE/ORDER/ATTACK actions with object IDs, but the available event model does not establish a creation edge that binds a newly controllable object ID to a particular earlier DE_QUEUE command.

Without a validated identity/type lineage, later control of object Y cannot be attributed to queue command X merely because the timing appears plausible.

This is not a parser defect finding. It is an **evidence-model limitation** of the currently available replay surface.

## 4. Runtime observability architecture recovered

Pass 16 sharpens the production evidence ladder:

`REQUESTED`

The AI decides that a unit is desirable.

`AUTHORIZED`

Production-side eligibility/capability conditions permit the action.

`QUEUED`

A DE_QUEUE action is recorded, including producer object identity, unit type, quantity, player, and sequence.

`PENDING`

The requested production is now an outstanding expected world transition, but completion is not yet directly observed.

`OBSERVED_AVAILABLE`

Requires a world-state observation identifying the produced object as available/controllable, or an equivalently strong postcondition.

`COMMITTED_USE`

The observed object is assigned to a concrete strategic/tactical use.

`VERIFIED_EFFECT`

The use produces an observable operational or strategic consequence.

The current replay evidence closes the first four stages only through W1-level certainty. W2 remains open.

## 5. Why the SYNC object counts are insufficient

`obj_count` is an aggregate count. A change in object count can indicate that the world object population changed, but it does not establish:

- which object was created;
- its unit type;
- which producer created it;
- which DE_QUEUE caused it;
- whether it was immediately controllable;
- whether it belongs to the player whose queue command is being studied.

Likewise, `dp_obj_count` and `dp_obj_ttl` are aggregate-derived fields in the available SYNC projection. They do not close the individual production lineage required by W2.

Therefore aggregate count deltas may be useful corroboration, but cannot be promoted to object-level production completion.

## 6. Controlled-experiment feasibility

The installed game was checked at runtime during this pass. The game executable was not running during the audit; Steam processes were present.

The savegame corpus contains hundreds of ordinary `.aoe2record` recordings, including the previously used reference recording and the known scenario files:

- `AEGIS_P0A_TEST.aoe2scenario`
- `AEGIS_P0A_EDITOR.aoe2scenario`

The scenario files still exist on disk, but the project decision remains to **retire automated scenario-loader testing** because loading was unreliable. Their existence is not treated as runtime proof.

A tiny controlled ordinary-game production experiment is therefore retained as a future option, but this pass does not pretend that one was completed. The useful experiment would require an ordinary game/replay with:

1. one unmistakable producer building;
2. a very small number of produced units;
3. a unit type with no ambiguity in the visible action stream;
4. capture of the richest available runtime/object-state representation;
5. correlation against MOVE/ORDER/DELETE events;
6. a reproducible identity chain from producer to created object.

If the recording format cannot expose that chain, the experiment should close the question negatively rather than infer it.

## 7. Parser-level conclusion

The parser is not merely throwing away an obvious `created_object_id` field in the current DE_QUEUE structure. The current action representation itself contains:

`producer object(s) + unit type + amount + player + sequence`.

The CREATE action parser exists in the installed parser code, but the reference replay's observed full operation inventory contains no CREATE operation category. Therefore the presence of a parser branch for CREATE cannot be used to claim that this particular DE recording emits creation events.

This distinction is important:

**parser capability != evidence emitted by this recording format/version.**

## 8. Consequence for Layer 2 archaeology

Historical `.per` production chains can now be read with a stronger implementation discipline.

For example, the Promisory camel path establishes a chain of the form:

`weighted threat aggregate -> traincamel goal -> stable search/filter -> target-point train action -> can-train gate -> train command`.

Pass 16 confirms why that chain should not be described as "camel created" merely because a `train` action exists in source or a replay DE_QUEUE exists after it.

The historical programmer's architecture is strongest at **decision and command issuance**. The runtime evidence is weaker at **world-state realization**.

That is itself strategic information: the old system was engineered around an action-oriented control surface whose observability was substantially richer for decisions than for postconditions.

## 9. AEGIS design consequence

AEGIS must never collapse these two propositions:

`the bot ordered a unit`

and

`the bot now possesses the unit`.

The production subsystem should maintain separate state for:

- desired production;
- authorization;
- queue request;
- pending production;
- observed availability;
- committed use;
- verified outcome.

A future implementation should prefer a delayed commitment when the expected unit has not yet crossed the observation boundary. This prevents a production request from consuming strategic state twice or causing downstream planners to reason from phantom capability.

## 10. Evidence status table

| Claim | Evidence level | Status |
|---|---|---|
| DE_QUEUE exists in reference corpus | W0 | CONFIRMED |
| DE_QUEUE contains producer object ID(s) | W0 | CONFIRMED |
| DE_QUEUE contains requested unit type | W0 | CONFIRMED |
| DE_QUEUE contains amount | W0 | CONFIRMED |
| DE_QUEUE contains sequence | W0 | CONFIRMED |
| Rich SYNC contains aggregate object counts | W2-aggregate | CONFIRMED |
| Rich SYNC identifies each produced object | W2-object | DISPROVEN FOR CURRENT PROJECTION |
| Later MOVE proves queue completion | W2 | REJECTED |
| Replay currently closes queue -> created object identity | W2 | OPEN / NOT CLOSED |
| Scenario loader is a viable controlled runtime method | — | RETIRED |
| Ordinary-game controlled experiment is feasible in principle | DESIGN/PROBABLE | RETAIN |

## 11. Pass 16 disposition

**Production replay lineage:** `W1 CLOSED / W2 OPEN`.

**Parser evidence:** `CLOSED` for the currently exposed DE_QUEUE schema.

**Scenario automation:** `RETIRED`; do not reopen without a materially different loader/runtime mechanism.

**Layer 2 strategic interpretation:** strengthened. The historical architecture should be understood as highly capable at translating strategic interpretation into production commands, but its replay observability does not automatically expose the resulting world-state transition.

## 12. Next priority

The production W2 question is now sufficiently characterized that further blind replay inspection has diminishing value.

Priority should shift to runtime surfaces with naturally stronger postconditions:

1. **research completion** — determine whether research has a distinct observable postcondition beyond `RESEARCH` action;
2. **building completion** — determine whether build lifecycle can be closed through object/state evidence;
3. **attack execution** — determine whether target/contact/damage consequences can be observed strongly enough to close W2/W3;
4. **production** — return only if a richer object-state or controlled ordinary replay becomes available.

This preserves the project standard: close what the evidence closes, preserve the negative boundary, and spend experimental effort where the next observation can actually increase epistemic coverage.
