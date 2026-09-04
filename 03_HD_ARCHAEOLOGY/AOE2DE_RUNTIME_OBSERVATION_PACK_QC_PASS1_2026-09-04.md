# Pass 14 Runtime Observation Pack — QC Pass 1

**Date:** 2026-09-04  
**Status:** ACCEPT WITH CORRECTIONS — WORKING CANON  
**Artifact under review:** `AOE2DE_RUNTIME_OBSERVATION_PACK_PASS14_2026-09-04.md`

## QC verdict

Pass 14 is accepted as a runtime-observation baseline.

It correctly changes the evidence target from command existence to command-to-world correlation while explicitly refusing to equate command events with completed state.

## Strengths

1. Dataset counts were obtained directly from `body_fresh.jsonl`.
2. Action-family distribution is reproducible.
3. Player attribution is retained.
4. Sequence numbers are retained.
5. Research, production, building, attack, scouting, economy, and recovery surfaces are all represented.
6. The W0 command boundary is explicit.
7. The replay is not misrepresented as proof of historical HD-controller execution.
8. Scenario-loader automation remains correctly outside the critical path.
9. The next experiment is narrow and falsifiable.

## Corrections / open items

### Q01 — Sequence semantics
The `sequence` field is used as an ordering key. Its exact engine temporal semantics are not yet independently established. Treat it as replay-stream order, not automatically as simulation ticks.

### Q02 — World time
The terminal `world_time` is available from POSTGAME, but a complete mapping from sequence to simulation time has not yet been established.

### Q03 — Object lifecycle
Object IDs in action payloads must be joined to object lifecycle records before unit/building completion is claimed.

### Q04 — Command causality
An action immediately preceding a state change is temporal correlation, not proof that the action caused the state change. Causal promotion requires stronger lifecycle evidence.

### Q05 — Historical execution
The replay must remain calibration evidence unless the AI identity/configuration and execution provenance are independently established.

### Q06 — DE_QUEUE semantics
Queue amount and unit ID are command-level fields. Completion must be established from object creation/lifecycle events.

### Q07 — RESEARCH semantics
Technology ID identifies the requested research command. Completion and availability must be separately observed.

### Q08 — BUILD semantics
Building ID and coordinates establish a build command. Construction completion must be separately observed.

### Q09 — ATTACK semantics
`DE_ATTACK_MOVE` establishes an attack-move command. It does not establish contact, damage, target destruction, or strategic pressure.

### Q10 — Scout semantics
`DE_AUTOSCOUT` establishes an autoscout command. Information acquisition requires subsequent observation of newly exposed enemy/map state.

### Q11 — Recovery semantics
STOP, TOWN_BELL, REPAIR, and movement are candidate recovery markers, not proof of a retreat controller transition.

### Q12 — Economic semantics
BUY/SELL/GATHER_POINT events expose economic actions but not their opportunity cost or strategic benefit.

### Q13 — Player behavior
The event distribution is asymmetric between players. This is an observation, not an explanation of skill, strategy, or controller quality.

### Q14 — Terminal state
Player 1 resignation is terminal evidence. It must not be used alone to infer why the player resigned.

### Q15 — World-state closure metric
Future passes should report closure per chain using W0 command, W1 pending/accepted, W2 world state, W3 operational capability, W4 strategic effect.

### Q16 — Negative controls
At least one future experiment should test a command where the expected world postcondition does not occur, establishing that the join does not mechanically assume success.

### Q17 — Identity joins
Object identity must be tracked across command payloads, creation, state changes, destruction, and ownership. Raw integer overlap is insufficient without event-model validation.

### Q18 — Temporal window
Future correlation must define an explicit observation window rather than selecting an arbitrary nearest event.

### Q19 — Confounding
Multiple commands can affect the same world-state variable. Candidate causal edges require competing-command/confounder review.

### Q20 — Promotion gate
No W2/W3/W4 claim should enter the canonical historical ledger until the underlying object/state join is reproducible.

## Final assessment

**PASS 14 = ACCEPT WITH CORRECTIONS.**

The project has now crossed the boundary from static source archaeology into a reproducible runtime-observation program. The next pass should not broaden the dataset prematurely. It should close one object lifecycle completely and use that result as the template for the remaining world-state chains.
