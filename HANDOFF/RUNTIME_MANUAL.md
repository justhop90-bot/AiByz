# AEGIS-BYZ Runtime Manual

## 1. Read this before changing anything
This repository is institutional memory. Do not begin by rewriting the bot. Establish authority, provenance, current branch state, evidence status, and known unknowns first.

## 2. Authority hierarchy
1. PORPHYRA_V2_2_2 — immutable control/baseline.
2. User-designated `02_STRATEGY/V3_CANONICAL_SOURCE` — canonical V3 strategy source.
3. Current replay calibration artifacts — empirical evidence for the specified game/version corpus.
4. HD/2013 archaeology — strategic knowledge source and historical design evidence.
5. Native engine research — machine contract evidence.
6. V4 and other experimental artifacts — evidence only.
7. ADPromisory and WarCouncil — rejected experimental substrates; do not use them.

## 3. Machine-learning rule
Never promote a parser guess into an engine fact. Use an evidence ladder: source usage, parser implementation, native signatures/callgraph, diagnostics, and behavioral validation.

## 4. Replay evidence levels
LEVEL 0: raw replay bytes / preserved source.
LEVEL 1: parser-decoded events.
LEVEL 2: reconstructed state.
LEVEL 3: decision/strategic events.
Every transition needs provenance, method, confidence, and uncertainty.

## 5. Temporal contract
Maintain event_sequence, replay_time_candidate, temporal_confidence, source_clock, observation_time, serialization_index, and freshness. ACTION sequence is probable temporal information but its exact unit remains unproven. SYNC current_time is parser-described as milliseconds from beginning. POSTGAME world_time is terminal simulation-time evidence.

Never use file order as causal order when events share a sequence coordinate.

## 6. Object contract
An object record needs identity, owner, type, first_seen, last_seen, lifecycle state, visibility, relationships, commands, production origin, transformation lineage, engagements, and confidence. Missing observation creates a termination candidate; it does not prove death.

## 7. Production contract
Represent:
intent -> queue command -> admission -> queued -> started -> completed -> object birth -> capability available -> deployed -> reinforced.

For every production event retain producer IDs, unit ID, amount, sequence/time, admission confidence, completion evidence, object lineage confidence, and unresolved alternatives.

## 8. Strategic state contract
At minimum:
Economy, Production, Military, Technology, Map, Position, Information, Timing, Infrastructure, Logistics, Reserves, Threats, Commitments, Opportunities, Confidence, Initiative, Objective.

## 9. Capability contract
Do not equate unit count with capability. Track readiness, location, technology, health when observable, production support, reinforcement, mobility, and strategic objective.

## 10. Opponent model
For each opponent maintain beliefs about composition, economy, production infrastructure, technology, position, current commitment, likely objective, required resources, transition, confidence, alternatives, and vulnerabilities.

## 11. Decision contract
At each decision event reconstruct only the information available then. Evaluate feasible actions and preserve alternatives. Record expected consequence, risk, failure signature, recovery, reversibility, commitment magnitude, and confidence.

## 12. Failure protocol
A failed action is not merely a bug. Preserve its signature. Distinguish command rejection, execution failure, non-realization, delayed realization, strategic failure, and measurement failure.

## 13. Engineering authority
Critical state should have explicit ownership. Prefer one authoritative writer. Sensors are read-only. Planners propose. Authorizers approve. Executors issue commands. Observers acknowledge outcomes. Recovery handles failure.

## 14. Testing doctrine
Every promoted feature requires:
- positive test;
- negative control;
- parser regression test;
- provenance check;
- cross-recording check;
- counterexample search;
- falsifier statement.

## 15. Six-month reconstruction procedure
If the conversation is gone, do this in order:
1. Read this directory.
2. Read `KNOWN_UNKNOWN_LEDGER.md`.
3. Read the dissertation.
4. Inspect replay/action/temporal/object documents.
5. Inspect native-engine research.
6. Inspect V3 strategy archaeology.
7. Verify local PC artifacts and hashes.
8. Re-run calibration before modifying inference.
9. Only then continue the next research pass.

## 16. Next frontier
The next empirical task after the production architecture is Production-to-Object Lineage Reconstruction. Then capability-ramp reconstruction, resource-flow coupling, opponent response, decision events, and eventually conversion-tax measurement.

## 17. Non-negotiable
Do not optimize the implementation before understanding the state model. Do not optimize the state model before understanding the evidence. Do not optimize the strategy before understanding the machine.