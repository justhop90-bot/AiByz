# P0 Worker Productivity Observer — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate implemented and archived; NOT runtime-qualified; NOT loaded by production root.

## Objective

Separate physical command issuance from observed worker state. The observer begins only after the worker-task command adapter reports COMMAND_ISSUED and performs a later local-worker observation. V0 does not claim that command execution equals productivity or resource income.

## Contract

COMMAND_ISSUED → OBSERVING → PRODUCTIVE_CANDIDATE or INTERRUPTED.

The candidate preserves generation fencing and records resource, observation timestamp, cycle, observed worker count, and failure disposition.

## Evidence basis

Stock gatherer logic demonstrates explicit worker searches and filtering by carry, action, order, target, and other object state. The existing AEGIS worker-task command uses the stock local-worker plus remote-resource targeting pattern and `up-target-objects 0 action-default -1 -1`. This observer intentionally does not reuse command issuance as proof of success.

## Critical qualification boundary

V0's PRODUCTIVE state is only a candidate physical-state observation: an eligible villager remains visible after command issuance. It is NOT proof that the villager is gathering, that the selected source is being serviced, that cargo is increasing, or that net resource income is positive.

Those stronger claims require additional observation of target/order/action/cargo and, ultimately, resource-state change over time.

## Failure boundary

If no eligible worker remains visible during the observation pass, V0 records `INTERRUPTED`. This is deliberately coarse. It does not yet distinguish target loss, source exhaustion, threat, command rejection, worker death, stale search state, or strategic cancellation.

## Qualification states

OBSERVED: stock worker object-state search/filter mechanisms.
CORRELATED: persistent eligible worker visibility is useful evidence that a command did not immediately destroy worker eligibility.
IMPLEMENTED: generation-fenced post-command observer.
STATIC-QUALIFIED: candidate is structurally isolated and not loaded by production root.
UNQUALIFIED: exact target-build timing, action/order mutation visibility, target attribution, source attribution, cargo progression, resource-income confirmation, and same-pass interpreter semantics.

## Architectural consequence

AEGIS must not close an economic task lifecycle at COMMAND_ISSUED. The minimum lifecycle remains:

REQUESTED → ADMITTED → RESERVED → AUTHORIZED → COMMAND_ISSUED → ENGINE_STATE_OBSERVED → PRODUCTIVE → VERIFIED.

The next pass should strengthen the observer into a worker-task verification adapter using target/order/action/cargo evidence, then add bounded recovery for interrupted or invalid tasks.