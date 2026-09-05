# Pass 66 — Same-Pass Release → Successor Claim Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Status:** PASS WITH VERSION/EVIDENCE BOUNDARY  

## Mission

Determine whether state mutations performed by one rule/controller are visible to later rules in the same script pass, and whether this is sufficient to prove a release→successor commitment handoff in the same pass.

## Strong engine-family evidence

The public AOE2-derived scripting reference states that strategic-number and goal updates occur immediately, while some world-derived facts such as `enemy-buildings-in-town` update on the next script pass. It also provides concrete rule-order examples in which a goal is changed and a later rule consumes the changed value. This establishes that controller state is not universally frozen for an entire pass.

The same source describes a practical failure mode where a following rule can edit a shared strategic number after an earlier rule has edited it, motivating a cooldown. This is direct evidence for same-pass susceptibility to later rule writes in the scripting family.

## Critical boundary

This does **not** by itself prove the exact AoE2 HD historical behavior of every predicate, nor does it prove the specific `sn-resource-control` release→successor sequence.

Therefore:

```text
SAME-PASS STATE VISIBILITY
        ≠
SAME-PASS COMMITMENT HANDOFF PROVEN
```

To close the latter, we need a historical HD corpus trace or controlled runtime observation showing:

```text
RULE A
→ release shared commitment
→ state becomes available
→ RULE B later in same pass
→ observes released state
→ claims successor commitment
```

## Temporal model

The strongest current model is:

```text
T0  same-rule mutation
T1  later rule in same pass
T2  next script-pass observation
T3  real-time timer interval
```

But T0/T1 visibility is predicate-dependent. A goal/SN read cannot automatically be generalized to a world-observation fact.

## Priority consequence

If the exact release→successor sequence is eventually proven, rule order becomes capable of implementing an immediate handoff:

```text
CONTROLLER A
→ RELEASE
→ CONTROLLER B
→ CLAIM
```

If it is only visible on the next pass, the handoff contains an unavoidable pass boundary:

```text
PASS N: A RELEASES
PASS N+1: B CLAIMS
```

That distinction affects reaction latency, starvation exposure, and procedural priority.

## Evidence status

| Finding | Grade |
|---|---|
| Goals/SNs can be observed after earlier state mutation in the scripting pass | DIRECT engine-family evidence |
| Later rules can overwrite/re-edit shared state | DIRECT engine-family evidence |
| Some world-derived facts update on a later script pass | DIRECT engine-family evidence |
| Same-pass release→successor is possible in principle | INFERRED / engine-family-supported |
| Same-pass `sn-resource-control` release→successor in historical HD | NOT PROVEN |
| Same-pass production commitment handoff in historical HD | NOT PROVEN |
| Temporal priority inversion occurs historically | NOT PROVEN |

## Research consequence

Pass 66 closes the broader question of whether controller state can change during a pass, but deliberately leaves the narrower handoff question open. This is preferable to converting general same-pass semantics into an unsupported historical claim.

## Byzantine consequence

A future Byzantine controller may require immediate replacement of a stale commitment by a more urgent counter. Whether that replacement can occur in the same pass is an implementation/runtime question and must not be designed as a Layer-2 historical fact until specifically proven.

## Layer boundary

No `.per` implementation, architecture implementation, runtime deployment, or canonical bot modification was performed. Research only.
