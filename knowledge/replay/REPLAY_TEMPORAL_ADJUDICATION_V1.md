# Replay Temporal Semantics Adjudication v1

Date: 2026-09-02
Status: calibration evidence / promotion candidate

## Objective
Determine whether ACTION sequence, SYNC current_time, and POSTGAME world_time are independent clocks or related simulation-time domains.

## Calibration evidence
Eight controlled recordings in AEGIS_CALIBRATION_DATA were inspected. ACTION payloads were decoded using payload[0] as command and payload[1] as payload dictionary. Sequence was extracted only from ACTION payloads; rich SYNC time was extracted only when payload[2].current_time was numeric; terminal world_time was extracted from POSTGAME.

## Observed result
All eight recordings with ACTION records show non-decreasing ACTION sequence values. Sequence uniqueness is lower than ACTION count, proving multiple commands may share one sequence value. Therefore sequence behaves as a temporal/correlation coordinate, not as a unique event identifier.

The reference recording has ACTION sequence range 208..10,906,683. Its terminal POSTGAME world_time is 10,906,683 exactly. Its final rich SYNC current_time is 10,886,319, 20,364 units earlier.

Other full calibration recordings show the same qualitative relationship: terminal ACTION sequence and rich-SYNC current_time are close, with rich synchronization generally preceding terminal world time. The offset varies, so no fixed snapshot cadence may be assumed.

## Adjudication
The earlier rule that sequence should be treated only as ordering evidence is now too conservative. Calibration provides strong evidence that sequence is a simulation-time-related coordinate. The exact unit and producer remain unestablished and require parser/native confirmation.

Promotion status:
- SEQUENCE_AS_SIMULATION_TIME_CANDIDATE = PROBABLE
- SEQUENCE_UNIT = UNKNOWN
- SEQUENCE_UNIQUENESS = FALSE
- SEQUENCE_MONOTONICITY = OBSERVED_TRUE in calibration
- POSTGAME_WORLD_TIME_CORRELATION = STRONG on calibration

## Consequences
1. Preserve sequence unchanged in every normalized event.
2. Use sequence as the primary temporal ordering coordinate unless contradicted.
3. Permit multiple events at one sequence value.
4. Never use ACTION count as elapsed time.
5. Do not treat every SYNC as a complete state snapshot.
6. Track rich-SYNC freshness/staleness relative to event sequence.
7. Retain POSTGAME world_time as an independent terminal cross-check.
8. Until units are proven, name the field replay_time_candidate rather than milliseconds.

## Required validation before universal promotion
- inspect parser implementation that creates sequence;
- determine whether sequence and world_time share the same source clock;
- quantify sequence gaps and simultaneous-event clusters;
- test reset/wrap behavior;
- compare start/end sequence with known game boundaries;
- repeat on held-out recordings.

## Architectural consequence
Temporal semantics should be a first-class replay subsystem. A strategic event should carry event_sequence, simulation_time_if_established, temporal_confidence, observation_freshness, and source locator. This prevents later state reconstruction from silently mixing clock domains.

## Next pass
Use the adjudicated temporal coordinate to build the object lifecycle ledger. Lifecycle termination must distinguish DESTROYED, TRANSFORMED, GARRISONED, DELETED, HIDDEN/UNOBSERVED, and UNKNOWN_TERMINATION rather than equating disappearance with death.
