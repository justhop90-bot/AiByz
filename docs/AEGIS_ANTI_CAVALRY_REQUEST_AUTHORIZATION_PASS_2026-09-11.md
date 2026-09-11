# AEGIS Anti-Cavalry Request / Authorization Pass — 2026-09-11

**Status:** IMPLEMENTED / NOT QUALIFIED
**Scope:** `AegisProm/AEGIS-scouting-threat-v0.per` + `AegisProm/AEGIS-cavalry-response-v0.per`

## Preserved vertical slice

```text
enemy observation
  -> threat classification
  -> capability demand
  -> feasibility
  -> authorization
  -> spearman production request
  -> pending production
  -> spearman world-state observation
  -> causal verification gate
```

The threat observer remains responsible for classifying cavalry pressure. The response module consumes that classification and owns the production lifecycle. The observer currently classifies cavalry threat when cavalry, cavalry-archer, or knight counts cross its existing thresholds. fileciteturn129file0L2-L2

## Request identity

A fresh threat generation creates one anti-cavalry capability request. `aegis-cr-request-id` is copied from `aegis-st-generation`; downstream rules do not generate a new identity.

The authorization identity and authorization generation are tied to that same request record.

## Authorization boundary

Threat classification is **not** authorization.

Authorization is granted only after the anti-cavalry response reaches its idle/qualified state and native `can-train spearman-line` feasibility is present. Physical production additionally requires valid authorization and an unused attempt.

Authorization is consumed at the `up-train escrow-state c: spearman-line` boundary.

This preserves the existing physical production command rather than substituting a different unit token.

## Expiry

Authorization generation must remain aligned with the request generation. A generation mismatch fails closed.

No native time-based authorization clock is claimed. Generation supersession is the source-level expiry mechanism until an engine-proven temporal mechanism exists.

## Pending production

`up-pending-objects c: spearman-line >= 1` remains an explicit pending state.

Pending production is **not** treated as a spawned spearman.

This follows the project's existing forensic rule that queue/dequeue or pending lifecycle evidence must not be promoted into completion without the corresponding world-state transition.

## Completion evidence

The response module captures a baseline spearman count before production and separately observes the current spearman count while pending.

A count increase establishes `WORLD_STATE_EVIDENCE`; it does not by itself manufacture request-level causal evidence.

`aegis-cr-causal-evidence` is therefore an explicit closed gate. Confirmation requires:

- world-state evidence;
- causal evidence;
- request/authorization identity match.

No source rule sets the causal bit merely because the train command was issued or because a count increased.

## Failure behavior

The slice now distinguishes:

- `NOT_FEASIBLE` before dispatch;
- `STALE_AUTHORIZATION`;
- `PENDING_LOST`;
- `CAUSALITY_UNPROVEN`.

A failed request is not automatically retried. Retry belongs to reassessment and must establish a new request/authorization identity.

## Idempotency

The physical production boundary remains one attempt per request. Authorization is single-use and consumed at dispatch.

This prevents repeated rule firing from producing multiple spearmen for one semantic request.

## Architecture decision

No change was made to `AEGIS-scouting-threat-v0.per` because its existing observation/classification role is the correct upstream owner. The response module now explicitly marks the transition from threat classification to capability demand and from capability demand to authorized physical execution.

The military-production candidate remains architecturally separate. This Anti-Cavalry slice does not promote `AEGIS-military-production-v0.per`, does not use runtime-only initialization as source evidence, and does not collapse the two verticals.

## Qualification status

**NOT QUALIFIED.**

The request/authorization boundary and pending-production evidence model are implemented. Promotion still requires target-build runtime/engine evidence, request-specific causal attribution, and the complete reassessment/qualification chain.
