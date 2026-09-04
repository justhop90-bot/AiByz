# PASS 38 — C1-B Replay Transition Proof

Date: 2026-09-04
Layer: 2 — HD/Promisory archaeology
Mission: C1 Threat → Capability
Status: PARTIAL PASS — temporal corroboration established; causal authorization remains unobservable.

## 1. Question

Can the replay corpus demonstrate a real transition from enemy mounted pressure toward Byzantine camel production without inventing an internal AI authorization event?

Required chain:

`enemy mounted capability → observable pressure → counter-state → production authorization → camel queue → post-transition capability`

## 2. Replay corpus selection

The existing AEGIS calibration corpus contains eight parsed multiplayer replay sets. Their headers identify player 1 as civilization ID 96 (Byzantine) in the inspected calibration set.

No local artifact was created for this pass. The replay data already stored on the Weebo calibration corpus was inspected directly.

## 3. Replay A — 2026-08-29 173854

Source body:
`AEGIS_CALIBRATION_DATA/MP Replay v101.103.48987.0 @2026.08.29 173854 (2).body.jsonl`

Player 1 queues camel-line unit ID 1755 three times:

- sequence 2,945,313
- sequence 2,945,509
- sequence 2,945,733

Before the first camel queue, player 2 has 35 recorded knight-line queue actions (unit ID 38), with the latest preceding knight queue at sequence 2,536,974.

The first camel queue therefore follows a substantial, already-observed enemy knight production history in the same replay.

Evidence grade: DIRECT for replay actions; COMPOSED for temporal relationship.

## 4. Replay B — 2026-08-31 094639

Source body:
`AEGIS_CALIBRATION_DATA/MP Replay v101.103.48987.0 @2026.08.31 094639 (1).body.jsonl`

Player 1 queues camel-line unit ID 1755 repeatedly. The first camel queue occurs at sequence 2,918,785; 21 camel queue actions are recorded in the replay.

Before that first camel queue, player 2 has 10 recorded knight-line queue actions. The latest preceding enemy knight queue occurs at sequence 1,855,078.

Again, camel production begins after a substantial enemy knight-production history.

Evidence grade: DIRECT for replay actions; COMPOSED for temporal relationship.

## 5. What this proves

DIRECT / CONFIRMED:

- The calibration corpus contains actual Byzantine-player camel production.
- The same corpus contains actual enemy knight production.
- In both inspected games, enemy knight production precedes the Byzantine player's first recorded camel queue.
- The replay contains real production events, not merely static civilization capability data.
- `DE_QUEUE` records the requested unit type and production-side player, giving an authoritative action-side observation for queue initiation.

## 6. What this does NOT prove

The replay does not expose the historical AI's internal strategic-number values, goals, rule firing, or `traincamel` authorization state.

Therefore we cannot directly observe:

`enemy knights → cavalry/cavarchers state → traincamel yes`.

Nor can we prove that the Byzantine player queued camels specifically because of those enemy knights.

Alternative explanations remain possible: preplanned composition, map strategy, technology timing, generic military production, or an unrelated strategic transition.

The correct disposition is therefore **temporal corroboration, not causal closure**.

## 7. Strongest current C1 chain

Static historical source gives the causal controller:

`enemy mounted measurement → cavalry/cavarchers → thresholded response → traincamel → production machinery → camel train`.

Replay evidence independently demonstrates that the corresponding world-side events can occur in the expected direction:

`enemy knight production history → Byzantine camel production`.

The two evidence streams meet at the action boundary but do not yet join at the hidden decision-state boundary.

## 8. Important engineering consequence

The replay interpreter must not manufacture the missing authorization edge.

Correct representation:

`OBSERVED enemy production`
→ `UNCERTAIN threat-state realization`
→ `OBSERVED Byzantine camel queue`

not:

`OBSERVED enemy production`
→ `ASSUMED traincamel goal`
→ `OBSERVED camel queue`.

This preserves the project's core replay invariant: when evidence cannot prove a transition, preserve uncertainty instead of inventing it.

## 9. C1-B disposition

**PARTIAL PASS.**

World-side temporal corroboration is established across two Byzantine-player calibration games. Internal strategic authorization remains unobservable from the current replay representation.

This is still valuable: it confirms that the historical controller's threat/counter mechanism corresponds to a behaviorally plausible game-state transition, while maintaining the distinction between controller evidence and world evidence.

## 10. Next target

C1-C should close the remaining bridge using a different route: reconstruct the historical controller's effective decision envelope around the replay transition.

Priority evidence:

1. identify the exact enemy mounted composition present immediately before each camel transition;
2. determine whether cavalry/cavarchers thresholds would have been crossed under the historical measurement rules;
3. identify research/technology state at the transition;
4. identify own camel-set and military-state constraints where replay-visible proxies exist;
5. test whether the observed transition is compatible with the historical ladder without claiming that compatibility is proof of causation.

The goal is not to force a replay into the historical explanation. The goal is to determine whether the historical controller is a viable explanation of the observed transition and where the evidence remains underdetermined.
