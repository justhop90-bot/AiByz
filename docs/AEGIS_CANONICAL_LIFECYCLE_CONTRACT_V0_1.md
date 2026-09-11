# AEGIS Canonical Lifecycle Contract v0.1

**Status:** NORMATIVE
**Reference:** Worker Economic Tasking / Civilian Production
**Scope:** All consequential AEGIS vertical capabilities implemented in pure `.per`.

This document is the canonical lifecycle contract. The vertical-slice registry remains authoritative for each slice's concrete stages, owners, evidence requirements, and allowed transitions. This document defines the cross-slice semantics those contracts MUST preserve.

## 1. Canonical lifecycle

```text
OBSERVE
  -> CLASSIFY / RECONCILE
  -> DEMAND / INTENT
  -> FEASIBILITY
  -> AUTHORIZATION
  -> PHYSICAL_REQUEST
  -> ENGINE_ACCEPTED_PENDING
  -> WORLD_STATE_VERIFIED
  -> REASSESS

Failure / expiry / conflict may enter:
  -> RECOVER
  -> REASSESS
```

These distinctions need not be literal `.per` variables, but implementations MUST NOT collapse them semantically.

## 2. Preconditions

Every consequential transition MUST have explicit preconditions. At minimum:

```text
expected source state
AND current generation
AND authoritative owner
AND required evidence
AND valid authorization when required
AND request is not already satisfied
AND no duplicate physical request is pending
```

Capability-specific preconditions are additive.

A failed or unknown precondition MUST NOT silently advance the lifecycle.

## 3. Ownership

Every authoritative state has exactly one semantic owner.

```text
OBSERVATION       -> observer
CLASSIFICATION    -> classification/state owner
DEMAND/INTENT     -> demand/objective owner
FEASIBILITY       -> capability/feasibility owner
AUTHORIZATION     -> authorizing owner
PHYSICAL_REQUEST  -> physical-action owner
PENDING           -> lifecycle owner
VERIFICATION      -> world-state verifier
COMMITMENT        -> commitment owner
RECOVERY          -> recovery owner
REASSESSMENT      -> reassessment owner
```

Other modules may read or consume authoritative state, but MUST NOT become an unregistered second writer.

## 4. Authorization

Authorization is distinct from feasibility and command issuance.

An authorization MUST identify:

- request identity;
- capability/action;
- generation;
- authorization owner;
- creation sequence/time where available;
- expiry condition.

A physical action requiring authorization MUST NOT execute without a current authorization.

The subsystem deciding *why* an action is required does not thereby own the physical command. The subsystem that owns the consequential endpoint issues that command.

## 5. Physical action

Physical action is the first attempt to alter the game world.

A physical request SHOULD carry request identity, generation, authorization identity, action type, and relevant target/resource/unit identity.

The following equivalence is forbidden:

```text
COMMAND_ISSUED != ACTION_COMPLETED
```

Command issuance proves an attempted dispatch, not successful world-state transition.

## 6. Pending / engine acceptance

Where the engine exposes an intermediate state, AEGIS MUST preserve it.

Examples:

```text
train command -> queue/pending -> unit observed
build command -> foundation/pending -> completed building observed
research command -> research pending -> age/technology observed
```

The pending state MUST preserve the originating request identity.

The following shortcuts are forbidden unless independently proven by engine evidence:

```text
DE_QUEUE != spawned unit
BUILD command != completed building
RESEARCH command != completed research
```

## 7. Evidence

World-state evidence is independent of AEGIS intention.

Evidence strength MUST be preserved. AEGIS uses the project evidence taxonomy:

```text
DIRECT
COMPOSED
INFERRED
AEGIS-GENERALIZATION
UNCERTAIN
```

Runtime/engine evidence may establish actual behavior, but static source alone does not establish runtime behavior.

Unknown evidence remains unknown.

## 8. Verification and causal attribution

AEGIS MUST distinguish:

```text
WORLD_STATE_OBSERVED
```

from:

```text
OUR_REQUEST_CAUSED_WORLD_STATE_TRANSITION
```

A verified outcome requires the required world-state evidence. A causal claim additionally requires evidence connecting the observed transition to the corresponding authorized request.

A later matching observation MUST NOT automatically receive credit for an earlier request when concurrent or independent causes remain possible.

## 9. Postconditions

A successful transition MUST establish its declared destination state and required state mutations.

For a consequential capability, promotion-level success requires at minimum:

```text
valid lifecycle contract
AND current generation
AND required runtime/engine evidence
AND WORLD_STATE_VERIFIED
AND no active qualification blocker
```

`ISSUED`, `ACCEPTED`, `PENDING`, `VERIFIED`, `AVAILABLE`, and `EFFECTIVE` are distinct semantic states. Implementations MUST NOT use one as an implicit synonym for another.

## 10. Failure

Failure MUST be explicit. Canonical failure classes include:

```text
PRECONDITION_FAILED
NOT_FEASIBLE
AUTHORIZATION_DENIED
AUTHORIZATION_EXPIRED
PHYSICAL_COMMAND_REJECTED
ENGINE_ACCEPTANCE_UNKNOWN
PENDING_TIMEOUT
WORLD_TRANSITION_NOT_OBSERVED
CAUSALITY_UNPROVEN
WORLD_STATE_CONTRADICTED
DUPLICATE_REQUEST
STALE_GENERATION
OWNER_CONFLICT
```

`UNKNOWN` and `FAILED` receive no success credit.

If a later world transition occurs independently, that observation is new evidence; it does not retroactively convert the failed request into a success.

## 11. Authorization expiry

Authorization MUST be finite or explicitly governed by a current-state validity condition.

Authorization becomes unusable when it:

- expires;
- is superseded by a newer generation;
- is cancelled;
- has invalidated preconditions;
- is no longer needed because the request is satisfied; or
- is invalidated by its owner.

An expired authorization MUST NOT be reused or silently renewed. The system returns to reassessment and obtains a new authorization if the requirement remains valid.

## 12. Idempotency

Repeated evaluation of the same request MUST NOT produce duplicate physical actions.

For request identity `R` and generation `G`:

```text
R,G already issued
AND still pending
    -> NO DUPLICATE PHYSICAL REQUEST
```

A retry requires an explicit state establishing that the prior attempt failed, expired, was cancelled, became invalid, or otherwise requires retry.

Idempotency applies to both state mutation and physical command issuance.

## 13. Monotonic evidence

Evidence may strengthen knowledge only when the new evidence supports the stronger claim.

```text
UNKNOWN -> OBSERVED -> SUPPORTED -> VERIFIED -> CAUSALLY_VERIFIED
```

Absence of evidence MUST NOT be treated as evidence of failure unless engine semantics establish that interpretation.

Contradictory evidence creates a conflict requiring reassessment rather than arbitrary overwrite.

## 14. Recovery

Recovery evaluates whether a failed, expired, or contradicted request remains valid.

Recovery may retry, cancel, replace, reprioritize, reallocate resources, delay, retreat, or request new authorization.

Recovery MUST NOT bypass authorization or invent success evidence.

## 15. Reassessment

`REASSESS` is a mandatory lifecycle boundary after consequential success, failure, expiry, conflict, recovery, or material world-state change.

Reassessment means re-evaluating current:

```text
world state
beliefs
requirements
constraints
resources
threats
commitments
authorizations
pending actions
```

It is not a blind loop back to the previous command.

## 16. Universal invariants

1. Observation is not classification.
2. Classification is not demand/intent.
3. Feasibility is not authorization.
4. Authorization is not command issuance.
5. Command issuance is not engine acceptance.
6. Pending is not completion.
7. Completion is not automatically strategic success.
8. Unknown completion remains unknown.
9. Failed execution receives no success credit.
10. Repeated rule firing cannot create duplicate physical requests.
11. Stale generations cannot authorize current actions.
12. Expired authorization cannot execute.
13. Every consequential state has one semantic owner.
14. Evidence cannot be strengthened without supporting evidence.
15. Recovery requires current-state evaluation.
16. Consequential outcomes terminate in reassessment.
17. Runtime qualification is required before promotion.
18. Static plausibility cannot substitute for engine evidence.

## 17. Normative transition schema

Every transition SHALL be representable as:

```text
TRANSITION {
    transition_id
    source_state
    destination_state
    preconditions[]
    state_owner
    authorization_required
    authorization_identity
    authorization_expiry
    required_evidence[]
    physical_action
    physical_action_owner
    state_mutations[]
    postconditions[]
    failure_transitions[]
    idempotency_rule
    reassessment_rule
}
```

A transition is conformant only when all applicable fields are satisfied.

## 18. Reference-slice interpretation

The Worker Economic Tasking / Civilian Production slice is the reference because it exercises the greatest number of lifecycle concerns in one bounded capability:

```text
role/world observation
 -> demand
 -> arbitration
 -> worker selection
 -> source/serviceability qualification
 -> authorization
 -> physical task command
 -> task/productivity observation
 -> recovery
 -> reassessment
```

The contract is not a requirement to copy its file structure. It is the semantic boundary that every other vertical must satisfy.

## 19. Qualification rule

A vertical is not qualified because its `.per` rules look complete.

It is qualified only when the authoritative registry contract, ownership, authorization, physical endpoint, evidence chain, failure/expiry behavior, idempotency, and reassessment behavior are demonstrated on the target build to the required evidence threshold.

The vertical-slice registry at `schemas/AEGIS-VERTICAL-SLICE-CONTRACTS-1.0.json` remains the machine-readable authority for concrete slice contracts.
