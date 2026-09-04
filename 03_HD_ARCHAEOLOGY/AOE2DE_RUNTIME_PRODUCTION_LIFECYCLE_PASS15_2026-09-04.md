# AoE2DE Runtime Production Lifecycle — Pass 15
Date: 2026-09-04
Status: WORKING CANON — OBSERVATIONAL CLOSURE ATTEMPT

## Mission
Test the first runtime vertical bridge:

`QUEUE COMMAND → PENDING/PRODUCTION → OBJECT CREATION → COMPLETION → AVAILABILITY → SUBSEQUENT USE`

The experiment uses the preserved reference replay rather than the failed scenario-loader workflow.

## Evidence source
Reference body:
`06_REPLAYS/08_FORENSIC_RUNS/2026-09-02_REFERENCE/body_fresh.jsonl`

Observed corpus size: 597,681 JSONL records.
ACTION records: 6,858.
Reference ACTION sequence range: 208..10,906,683.
Terminal POSTGAME world_time: 10,906,683.

Temporal rule inherited from adjudication: sequence is a probable simulation-time candidate, is monotonic in the calibration sample, is not unique, and permits simultaneous events.

## Production observations
The replay contains 1,493 `DE_QUEUE` ACTION records across both players.
Examples for player 1 include:

- sequence 19,663: amount 4, unit_id 83, producer object [1]
- sequence 822,372: amount 1, unit_id 93, producer object [2]
- sequence 1,811,911: amount 1, unit_id 448, producer objects [1,9458,9403]
- sequence 3,111,933: amount 1, unit_id 38, producer objects [2,9403,9458,9425]
- sequence 4,774,047-class neighborhood: repeated unit_id 38 production
- late game: repeated unit_id 38, 74, 93, 448, 7, 5, and other queues.

The same recording also contains 118 `RESEARCH` ACTION records, 471 `BUILD` records, and 904 `ORDER` records.

## What the replay proves
### W0 — command
`DE_QUEUE` is direct evidence that a production queue command was recorded with actor, producer object IDs, amount, unit ID, and sequence.

### W1 — temporal placement
Subsequent events can be ordered relative to the queue command using sequence. Multiple events can share a sequence, so ordering is cluster-based rather than a unique-event ordering.

### W2 — world state
The current parser output does **not** expose a sufficiently rich, object-level production snapshot around these queue commands to establish the produced object's creation/completion state directly.
Rich `SYNC` records provide aggregate values such as `total_res`, `dp_obj_count`, `dp_obj_ttl`, and `obj_count`; they do not provide a complete per-object production ledger in the observed normalized payload.

Therefore this pass does **not** promote queue admission to completed-unit evidence.

### W3 — operational capability
A later `ORDER`, `MOVE`, `DE_ATTACK_MOVE`, `FORMATION`, `STANCE`, or similar action involving a unit object can prove that some object was controllable, but without a validated identity/type lineage it cannot safely be assigned to a particular preceding `DE_QUEUE` command.

Therefore W3 linkage remains open for the reference replay.

### W4 — strategic consequence
No production command can be promoted directly to strategic capability or strategic outcome. That requires W2/W3 closure first.

## Critical negative result
The first runtime bridge is **not closed** by ACTION data alone.

This is an important result rather than a tooling failure:

`DE_QUEUE` proves command admission, not completion.

`DE_QUEUE(unit_id=X)` also does not establish that a later object was unit X unless an independent object-level observation connects them.

The existing replay parser therefore supports reliable command chronology but only partial object lifecycle reconstruction for this specimen.

## Identity problem
The queue payload contains producer object IDs and a unit type ID. Later command payloads contain object IDs for controllable objects. The available rich synchronization data does not provide a complete normalized mapping of those later object IDs to unit types and production lineage.

Consequently, a naive rule such as:

`queue X → next MOVE → unit X completed`

would be an unsupported inference.

## What can still be reconstructed
The replay is strong enough to construct a **production command timeline**:

`producer → requested unit → amount → time → neighboring commands`

It is not yet sufficient to construct a universally reliable **production object lifecycle timeline**:

`producer → queue admission → object birth → completion → availability → use`.

## Engineering consequence for AEGIS
AEGIS must never treat its own production command as the state transition `UNIT_AVAILABLE`.

Required architecture:

`DESIRE → CAN-FACT → PRODUCTION COMMAND → PENDING → OBSERVE OBJECT/QUEUE STATE → UNIT_AVAILABLE → ASSIGN/USE`

If the world-state observation is unavailable, the state must remain `PENDING/UNKNOWN`, not `AVAILABLE`.

## Runtime observation protocol v1
For future controlled runs, capture at minimum:

1. pre-command producer identity and state;
2. exact command and simulation-time candidate;
3. immediate post-command producer/queue state;
4. object creation observation;
5. production-progress/completion observation;
6. first controllable-object observation;
7. first subsequent use;
8. object identity/type continuity;
9. failure/cancellation/disappearance evidence;
10. strategic consequence only after W3 closure.

Each observation should carry source locator, timestamp/sequence, perspective, confidence, and evidence level.

## Best next experimental target
A controlled ordinary game/replay should deliberately create a small number of unmistakable units from a single production building, then capture rich synchronization/state evidence around the exact queue and completion interval. The objective is not to test AI behavior; it is to calibrate the replay representation itself.

The existing scenario-loader automation remains retired.

## Pass 15 conclusion
The runtime layer has successfully demonstrated a reproducible W0/W1 observation surface and has identified the exact missing bridge for W2/W3: object-level production lineage.

This prevents a major category error in later AEGIS validation. We now know exactly what the replay corpus can prove and exactly what it cannot prove.

## Evidence grades
- ACTION existence: DIRECT / CONFIRMED.
- Sequence temporal placement: DIRECT + prior calibration / PROBABLE.
- Queue admission as production intent: DIRECT / CONFIRMED.
- Queue admission as completion: DISPROVEN as an evidentiary rule.
- Queue → produced-object identity: UNCERTAIN.
- Produced object → operational capability: UNCERTAIN for this specimen.
- Operational capability → strategic effect: OPEN.

## Open edges carried forward
`DE_QUEUE → object creation`
`object creation → completion`
`completion → availability`
`availability → subsequent use`
`production capability → strategic effect`
