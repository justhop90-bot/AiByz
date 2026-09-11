# AEGIS downstream REASSESS consumption pass — 2026-09-11

## Purpose

Define the downstream consumption contract for the seven local REASSESS publishers without introducing a monolithic controller.

## Normative rule

A REASSESS publication is an event token, not permission to repeat the previous action. A consumer must:

1. consume only the current terminal lifecycle generation;
2. acknowledge the exact published generation once;
3. invalidate the publication token after consumption;
4. require a newer upstream observation/demand generation before creating another lifecycle request;
5. never recreate a request from a stale terminal stage;
6. never issue a second physical request for the same request identity;
7. never select the next strategy at the reassessment boundary.

## Distributed ownership

Each vertical retains a local consumer. There is no shared reassessment controller, central event bus, or cross-vertical strategy selector. No module owns all seven reassessment signals.

| Vertical | Publisher | Consumer owner | New-generation gate |
|---|---|---|---|
| worker_economy | worker task verification | worker demand/target pipeline | newer worker-role-vector generation |
| villager_production | civilian lifecycle reconciler | civilian demand | newer civilization-state generation |
| housing | housing construction | civilian demand | newer civilization-state generation |
| age_transition | age research | age requirement | newer/current observed-age evidence and request generation |
| anti_cavalry | cavalry response | threat observation/classification | newer threat generation |
| tactical_micro | micro verification | micro-control intent | newer world/threat generation |
| military_production | military production | military requirement | newer selector/requirement generation; candidate remains unqualified |

## Stale-outcome protection

The consumer must not treat `reassess-valid == 1` as a fresh demand. The publication identifies the terminal lifecycle generation. That generation may be acknowledged once, but it cannot itself create a new physical request.

A new request requires a genuinely newer upstream generation. A consumer must never manufacture a new generation merely by observing its own reassessment token.

## Duplicate-request protection

The existing request/authorization identity remains the physical-action boundary. REASSESS consumption cannot directly dispatch a command. A new request requires a new upstream generation and an inactive request slot; authorization must then be regenerated for that request.

Thus a terminal result cannot replay a physical request merely because the reassessment publisher remains observable for another rule-evaluation cycle.

## Failure handling

Confirmed and failed lifecycle outcomes both publish REASSESS. Failed outcomes receive no success credit. Recovery remains local to the owning vertical and must lead to a newer generation before another consequential request.

## Audit requirements

Tests must prove:

- identical reassessment generation is consumed at most once;
- stale terminal publication cannot create a new request;
- a newer upstream generation can create exactly one new request;
- request identity cannot be reused for a second physical request;
- authorization is regenerated for the new request;
- failed outcomes reassess without success credit;
- no consumer mutates another vertical's generation;
- no global reassessment controller exists;
- military production remains `CANDIDATE_BLOCKED`.

## Evidence boundary

This document defines the architecture and audit contract. It does not claim target-build runtime qualification, causal verification, or successful execution of the repository test suite.
