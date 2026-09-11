# ACAP v0.1 — Normative Capability Contract

**Status:** NORMATIVE / implementation contract
**Scope:** Anti-Cavalry Capability vertical slice
**Project constraint:** pure `.per`; no XS, hooks, injection, memory modification, undocumented harness, debugger circumvention, or runtime patching
**Authority basis:** AI(HD) + Promisory behavioral evidence, reconciled against the existing AegisProm source tree

## 1. Purpose

ACAP answers one question:

> Given the current enemy cavalry threat and current civilization state, what verified anti-cavalry capability is required, what deficit exists, whether that deficit is feasible to address, whether action is authorized, whether production actually occurred, and whether the resulting capability changes the next decision.

ACAP is a semantic contract. It does not require one `.per` file per state or one goal per field. The implementation must preserve the ownership and evidence boundaries defined here.

## 2. Normative transition schema

Every transition is defined as:

```text
TRANSITION {
    id
    from_state
    to_state

    PRECONDITIONS {
        state_valid
        ownership_valid
        domain_conditions
        evidence_conditions
        temporal_conditions
    }

    REQUIRED_EVIDENCE {
        evidence_class
        evidence_source
        minimum_confidence
        provenance
    }

    STATE_MUTATIONS {
        set
        increment
        decrement
        invalidate
        preserve
    }

    POSTCONDITIONS {
        resulting_state
        invariants
        derived_state_requirements
    }

    FORBIDDEN_SHORTCUTS {
        prohibited_inferences
        prohibited_state_jumps
        prohibited_duplicate_actions
    }
}
```

A transition MUST NOT occur unless its mandatory preconditions and evidence predicates are satisfied. It MUST NOT claim more certainty than its evidence supports.

## 3. Global invariants

1. Exactly one authoritative owner exists for each mutable ACAP state.
2. No transition occurs without its preconditions.
3. Repeated evaluation of the same state and evidence is idempotent.
4. Evidence may strengthen but cannot fabricate a missing transition.
5. Every consequential state retains provenance.
6. Command issuance is distinct from queue acceptance, completion, and capability verification.
7. Feasibility is distinct from authorization.
8. Authorization expires and can be invalidated by material state change.
9. Effective deficit is never negative.
10. Only verified capability reduces the deficit.
11. Deficit is recalculated from current state rather than treated as a permanent instruction.
12. Verified capability changes trigger reassessment.
13. Material threat changes invalidate stale demand.
14. Failure and uncertainty remain distinct.
15. Recovery from failure requires new evidence.
16. Capability cannot be credited twice.
17. Pending capability cannot be counted as verified capability.
18. Repeated rule firing cannot create duplicate authorizations or production requests.
19. Closed demand cannot reactivate without a newly established requirement.
20. Reassessment produces a new decision rather than blindly replaying the previous decision.

## 4. Evidence invariants

The evidence chain is:

```text
observation
  != classification
  != demand
  != authorization
  != command
  != queue acceptance
  != completion
  != capability verification
  != strategic effect
```

Evidence classes:

- `DIRECT` — directly observed or directly established by an engine fact/action.
- `COMPOSED` — deterministic combination of established observations/rules.
- `INFERRED` — interpretation not directly established by world-state evidence.
- `AEGIS-GENERALIZATION` — deliberate generalization from established historical behavior.
- `UNCERTAIN` — insufficient evidence for a stronger classification.

A command such as `up-train spearman-line` proves an execution attempt. It does not prove queue acceptance, completion, or strategic effect.

## 5. State ownership

```text
THREAT_*        -> Threat / Intelligence
DEMAND_*        -> Capability / Reasoning
DEFICIT_*       -> Capability / Reasoning
FEASIBILITY_*   -> Production / Resource
AUTHORIZATION_* -> Strategic Authority
PRODUCTION_*    -> Execution / Production State
CAPABILITY_*    -> Verification
REASSESSMENT    -> Capability / Reasoning
```

Readers may consume state. They do not become a second authoritative writer merely by reading it.

## 6. Transition contracts

### T01 — NO_DEMAND -> THREAT_ESTABLISHED

**Preconditions**
- Current state is `NO_DEMAND`.
- Threat/Intelligence owns the transition.
- A valid enemy observation exists.
- The observation satisfies the established cavalry-detection criterion.

**Required evidence**
- `DIRECT` observation.
- Minimum confidence: `CONFIRMED`.
- Source and observation time preserved.

**Mutations**
- Establish `threat_level`.
- Establish `threat_source`.
- Record `threat_timestamp` and evidence provenance.
- Do not create demand or authorization.

**Postconditions**
- State is `THREAT_ESTABLISHED`.
- Threat evidence is preserved.
- No production action is authorized solely by detection.

**Forbidden shortcuts**
- Enemy cavalry exists -> anti-cavalry demand.
- Enemy cavalry exists -> production authorization.
- Observation -> strategic conclusion without classification.

### T02 — THREAT_ESTABLISHED -> DEMAND_ESTABLISHED

**Preconditions**
- Threat remains valid.
- Threat classification can be evaluated.
- Required contextual modifiers are available.

**Required evidence**
- `COMPOSED` from threat observations, classification logic, and context.
- Minimum confidence: `PROBABLE` or higher.

**Mutations**
- Establish `required_capability`.
- Establish `required_strength`.
- Optionally establish `desired_strength`.
- Establish urgency/deadline.
- Create a unique `demand_identity`.

**Postconditions**
- State is `DEMAND_ESTABLISHED`.
- A capability requirement exists.
- No production command has occurred solely from classification.

**Forbidden shortcuts**
- Threat -> train unit.
- Threat level -> fixed unit count without the demand rule.
- Enemy knight count -> automatic spearman quantity.

### T03 — DEMAND_ESTABLISHED -> DEFICIT_ESTABLISHED

**Preconditions**
- Required capability is defined.
- Current capability state can be evaluated.

**Required evidence**
- `COMPOSED`: demand + verified capability + committed/unavailable capability state.

**Mutations**
```text
raw_deficit = required_strength - available_strength
deficit = max(0, raw_deficit)
```

Record verified current strength, committed strength, and available strength.

**Postconditions**
- State is `DEFICIT_ESTABLISHED`.
- `deficit >= 0`.
- Unverified and duplicate capability is excluded.

**Forbidden shortcuts**
- Requested units -> verified units.
- Queued units -> verified available units.
- Future production -> current capability.
- Required - commanded -> capability deficit.

### T04 — DEFICIT_ESTABLISHED -> DEMAND_CLOSED

**Preconditions**
- `deficit <= 0`.
- Threat remains within the satisfied boundary.

**Required evidence**
- `COMPOSED` current threat + verified capability + requirement.

**Mutations**
- Mark demand closed.
- Record closure time.
- Invalidate active authorization for this demand.

**Postconditions**
- State is `DEMAND_CLOSED`.
- No production authorization is generated for this demand.

**Forbidden shortcuts**
- Negative deficit -> additional production.
- Old authorization -> continued execution.

### T05 — DEFICIT_ESTABLISHED -> FEASIBILITY

**Preconditions**
- `deficit > 0`.
- At least one response candidate exists.

**Required evidence**
- `COMPOSED` deficit + candidate validity + resources + technology + infrastructure + timing + production capacity.

**Mutations**
- Establish candidate set and constraints.
- Snapshot relevant resource, technology, infrastructure, and timing facts.

**Postconditions**
- State is `FEASIBILITY`.
- Candidate evaluation begins.
- No candidate is authorized merely by being feasible.

**Forbidden shortcuts**
- Deficit -> authorization.
- Candidate exists -> production.
- `can-train` -> authorization.

### T06 — FEASIBILITY -> AUTHORIZATION

**Preconditions**
- Selected candidate is valid and currently feasible.
- Resource, technology, infrastructure, timing, and opportunity constraints permit execution.
- Strategic authority approves.

**Required evidence**
- `COMPOSED`, minimum `PROBABLE`.
- Feasibility evidence + objective + candidate + quantity + resource commitment.

**Mutations**
- Set `authorized = true`.
- Record candidate, quantity, priority, resource commitment.
- Record authorization timestamp, expiry, and unique authorization identity.

**Postconditions**
- State is `AUTHORIZATION`.
- Authorization is uniquely identifiable and currently valid.

**Forbidden shortcuts**
- Feasible -> authorized.
- `can-train` -> authorized.
- Resources available -> strategic permission.

### T07 — FEASIBILITY -> DEFERRED

**Preconditions**
- No currently acceptable candidate satisfies constraints, or immediate execution is strategically inappropriate.

**Required evidence**
- `DIRECT` or `COMPOSED`, `CONFIRMED`/`PROBABLE`.
- Deferral reason recorded.

**Mutations**
- Record reason and timestamp.
- Schedule next feasibility evaluation.

**Postconditions**
- State is `DEFERRED`.
- No production command is issued.
- Demand remains active unless separately invalidated.

**Forbidden shortcuts**
- Deferred -> production.
- Temporary infeasibility -> demand closure.

### T08 — AUTHORIZATION -> PRODUCTION_REQUESTED

**Preconditions**
- Authorization exists and is valid.
- Authorization has not expired or been invalidated.
- Execution prerequisites remain valid.

**Required evidence**
- Direct authorization state before execution.
- Direct command issuance evidence after execution.

**Mutations**
- Set production request identity, timestamp, candidate, and quantity.
- Issue the physical production command through the execution boundary.

**Postconditions**
- State is `PRODUCTION_REQUESTED`.
- A physical command was attempted.
- Command evidence is preserved.

**Forbidden shortcuts**
- Expired authorization -> command.
- Missing authorization -> command.
- Command -> completion.
- Command -> verified capability.

### T09 — PRODUCTION_REQUESTED -> PRODUCTION_PENDING

**Preconditions**
- Production request exists.
- Direct evidence establishes engine acceptance/queue entry.
- Completion has not yet been verified.

**Required evidence**
- `DIRECT` / `ENGINE-SPECIFIC` queue or production state.
- Minimum confidence `CONFIRMED`.

**Mutations**
- Set pending state.
- Record acceptance time, request identity, and accepted quantity.

**Postconditions**
- State is `PRODUCTION_PENDING`.
- Accepted production is tracked.
- Accepted capability is not counted as verified available capability.

**Forbidden shortcuts**
- Command issued -> pending without acceptance evidence.
- Pending -> completed.
- Pending -> verified capability.

### T10 — PRODUCTION_REQUESTED -> PRODUCTION_FAILED

**Preconditions**
- Direct evidence establishes rejection, blocking, or failure.

**Required evidence**
- `DIRECT`, minimum `CONFIRMED`.

**Mutations**
- Record failure type, time, and request identity.

**Postconditions**
- State is `PRODUCTION_FAILED`.
- Verified capability is unchanged.

**Forbidden shortcuts**
- Failed request -> completed capability.
- Failed request -> deficit reduction.
- Failed request -> automatic retry without reevaluation.

### T11 — PRODUCTION_PENDING -> CAPABILITY_VERIFICATION

**Preconditions**
- Expected completion condition occurred, or a world-state change capable of proving completion was observed.

**Required evidence**
- `DIRECT` world-state evidence.

**Mutations**
- Establish a completion candidate.
- Preserve observation and timestamp.

**Postconditions**
- State is `CAPABILITY_VERIFICATION`.
- Capability remains uncredited until verification succeeds.

**Forbidden shortcuts**
- Elapsed production time -> completion.
- Queue disappearance -> completed unit.
- Command history -> completion.

### T12 — PRODUCTION_PENDING -> COMPLETION_UNVERIFIED

**Preconditions**
- Expected completion cannot be established within the permitted observation window.

**Required evidence**
- Preserved pending/request history plus absence of required confirmation.
- State remains uncertain.

**Mutations**
- Record `COMPLETION_UNVERIFIED` and uncertainty timestamp.
- Preserve pending identity.

**Postconditions**
- No capability credit is granted.
- No production failure is claimed unless independently proven.

**Forbidden shortcuts**
- No evidence -> failure.
- No evidence -> success.
- Timeout -> completed unit.

### T13 — CAPABILITY_VERIFICATION -> CAPABILITY_VERIFIED

**Preconditions**
- World-state evidence proves the capability exists.
- Capability is attributable to the requested transition.
- Verification rule is satisfied.

**Required evidence**
- `DIRECT`, minimum `CONFIRMED`.
- Independent world-state observation.

**Mutations**
- Mark production verified.
- Add only attributable completed capability to verified capability.
- Remove corresponding pending capability.
- Preserve verification evidence and timestamp.

**Postconditions**
- State is `CAPABILITY_VERIFIED`.
- Verified capability may enter the deficit calculation.
- The same capability cannot be credited twice.

**Forbidden shortcuts**
- Command -> verified capability.
- Queue entry -> verified capability.
- Time elapsed -> verified capability.
- Unattributed unit -> automatically attributed completion.

### T14 — CAPABILITY_VERIFIED -> REASSESSMENT

**Preconditions**
- Verified capability state is committed.

**Required evidence**
- Direct verification evidence plus current threat state.

**Mutations**
- Record reassessment timestamp and cycle identity.

**Postconditions**
- State is `REASSESSMENT`.
- Current threat and verified capability are reconsidered.

**Forbidden shortcuts**
- Verified unit -> demand closed without recalculation.
- Verified unit -> no further threat evaluation.
- Previous decision -> automatic repetition.

### T15 — REASSESSMENT -> DEMAND_CLOSED

**Preconditions**
- Current threat remains valid.
- Verified available capability satisfies requirement.
- Recalculated deficit `<= 0`.

**Required evidence**
- `COMPOSED` current threat + verified capability + commitments + requirement.

**Mutations**
- Set deficit to zero.
- Close demand.
- Invalidate active authorization.

**Postconditions**
- State is `DEMAND_CLOSED`.
- No further production is required for this demand.

**Forbidden shortcuts**
- Previous production quantity -> closure.
- Command count -> closure.
- Pending units -> closure.

### T16 — REASSESSMENT -> DEFICIT_ESTABLISHED

**Preconditions**
- Threat remains materially relevant.
- Recalculated deficit `> 0`.

**Required evidence**
- Current threat + current verified capability + current requirement.

**Mutations**
- Recalculate required, verified, committed, available strength, and deficit.
- Do not automatically reuse previous authorization.

**Postconditions**
- State is `DEFICIT_ESTABLISHED`.
- Deficit is current and positive.

**Forbidden shortcuts**
- Old deficit -> current deficit.
- Old authorization -> new authorization.
- Previous quantity -> current requirement.

### T17 — REASSESSMENT -> THREAT_ESTABLISHED

**Preconditions**
- New evidence materially changes threat state.
- Existing demand is no longer authoritative.

**Required evidence**
- Updated `DIRECT` or `COMPOSED` threat evidence.

**Mutations**
- Invalidate stale demand and authorization.
- Update threat state and timestamp.

**Postconditions**
- State is `THREAT_ESTABLISHED`.
- A new demand must be derived from the new threat state.

**Forbidden shortcuts**
- New threat -> reuse old demand.
- New threat -> reuse old authorization.

### T18 — DEMAND_CLOSED -> NO_DEMAND

**Preconditions**
- Threat expired or requirement is no longer active.

**Required evidence**
- Current threat/world-state evidence.

**Mutations**
- Clear active demand and authorization.
- Preserve closure history.

**Postconditions**
- State is `NO_DEMAND`.
- Future activation requires a new threat establishment.

**Forbidden shortcuts**
- Closed demand -> active demand.
- Old threat -> new threat.
- Old authorization -> new authorization.

### T19 — AUTHORIZATION -> AUTHORIZATION_EXPIRED

**Preconditions**
- Authorization is active.
- Current time is at or beyond expiry.
- Valid execution has not already begun.

**Required evidence**
- Direct temporal evidence.

**Mutations**
- Set `authorized = false`.
- Record expiry state and timestamp.

**Postconditions**
- State is `AUTHORIZATION_EXPIRED`.
- Expired authorization cannot execute.

**Forbidden shortcuts**
- Expired authorization -> execute.
- Expired authorization -> silently extend.
- Expired authorization -> retry without reassessment.

### T20 — PRODUCTION_PENDING -> PRODUCTION_FAILED

**Preconditions**
- Direct evidence establishes cancellation/failure.
- Completion has not been verified.

**Required evidence**
- `DIRECT`, minimum `CONFIRMED`.

**Mutations**
- Clear pending state.
- Record failure type, time, and request identity.

**Postconditions**
- State is `PRODUCTION_FAILED`.
- No capability credit is granted.
- Recovery requires reevaluation.

**Forbidden shortcuts**
- Failed pending request -> completed capability.
- Failed pending request -> deficit reduction.
- Failed pending request -> automatic successful retry.

## 7. Idempotency rules

Repeated evaluation of the same logical observation SHALL NOT:

- create a second demand identity;
- increase the deficit without new evidence;
- create duplicate authorization;
- issue duplicate production commands;
- credit the same completed unit twice;
- reopen a closed demand.

A new action requires a new authoritative reason: changed threat, increased deficit, expired/invalidated authorization followed by reassessment, or another explicitly established state transition.

## 8. Authorization validity rules

Authorization is valid only while all are true:

```text
active authorization
AND not expired
AND not invalidated
AND demand remains authoritative
AND execution prerequisites remain valid
```

Any material invalidating event routes through reassessment. An expired or invalidated authorization cannot be resurrected by repeated rule firing.

## 9. Reassessment rules

Reassessment SHALL use current values for:

- threat;
- required capability;
- verified capability;
- committed capability;
- available capability;
- feasibility constraints.

It SHALL NOT treat the previous decision as authoritative merely because it was previously correct.

Canonical loop:

```text
CAPABILITY_VERIFIED
      -> REASSESSMENT
      -> current THREAT
      -> current DEMAND
      -> current DEFICIT
      -> FEASIBILITY / DEMAND_CLOSED / new THREAT
```

## 10. Pure `.per` implementation rule

This contract does not prescribe invented runtime mechanisms. Implementation SHALL use only demonstrated AoE2DE `.per` primitives and repository-established semantics.

Goals, flags, timers, searches, engine facts, and actions may represent portions of the contract only where their semantics are established. A missing engine primitive is a qualification gap, not permission to invent one.

In particular:

- no XS implementation;
- no runtime hooks;
- no memory modification;
- no external execution bridge masquerading as native `.per` behavior;
- no undocumented completion signal;
- no inference that a source symbol is authoritative merely because its name sounds appropriate.

## 11. Promotion criterion

The anti-cavalry vertical slice is promotable only when it demonstrates, with appropriate evidence:

```text
THREAT_ESTABLISHED
  -> DEMAND_ESTABLISHED
  -> DEFICIT_ESTABLISHED
  -> FEASIBILITY
  -> AUTHORIZATION
  -> PRODUCTION_REQUESTED
  -> PRODUCTION_PENDING
  -> CAPABILITY_VERIFIED
  -> REASSESSMENT
  -> DEMAND_CLOSED or renewed DEFICIT
```

At least one failure/uncertainty path must also preserve the distinction between failed and unverified:

```text
AUTHORIZATION -> AUTHORIZATION_EXPIRED -> REASSESSMENT
PRODUCTION_REQUESTED -> PRODUCTION_FAILED -> FEASIBILITY/REASSESSMENT
PRODUCTION_PENDING -> COMPLETION_UNVERIFIED -> REASSESSMENT
```

A script that merely detects cavalry and executes `up-train spearman-line` does not satisfy ACAP v0.1.

## 12. Non-goals

ACAP v0.1 does not establish a universal military optimizer, complete strategic architecture, or final production director. It is a bounded vertical-slice contract designed to prove that AEGIS can turn an observed tactical threat into a capability requirement and close the loop through verified world-state evidence and reassessment.
