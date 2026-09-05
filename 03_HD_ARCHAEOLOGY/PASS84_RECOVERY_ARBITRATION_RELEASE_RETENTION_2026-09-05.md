# PASS 84 — RECOVERY ARBITRATION: RELEASE VS RETENTION

**Layer:** 2 — HD archaeology / evidence only  
**Status:** Research only; no `.per`, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`

## Executive result

Pass 84 investigates the integration boundary identified by Pass 83:

> **When an action fails, does historical AI release the commitment immediately, retain it while changing execution conditions, or hand control to another objective?**

The evidence supports a nuanced answer:

> **Historical recovery is conditional. A failed or interrupted execution path can retain policy state while changing execution conditions, release resource reservations when an alternative path becomes executable, or reset state when the original objective is no longer valid. There is no evidence of a universal recovery policy.**

This is important because recovery and arbitration are not separate systems. A recovery action can itself mutate the shared state that determines which competing objective gets the next execution opportunity.

## 1. Direct evidence: resource control can survive an execution transition

Historical AI uses `sn-resource-control` as a mutable policy state and does not reset it after every individual rule action.

A representative historical pattern is:

```text
RESOURCE CONTROL = TARGET
        ↓
TARGET-SPECIFIC FEASIBILITY / EXECUTION RULE
        ↓
ACTION
        ↓
RESOURCE CONTROL MAY REMAIN TARGET-SPECIFIC
```

This matters because it rejects the simplistic model:

```text
attempt → immediately release
```

The controller can continue protecting a target across multiple control decisions.

**Evidence grade:** DIRECT for persistent shared-state patterns; interpretation as commitment retention is AEGIS-generalized.

## 2. Direct evidence: successful execution can trigger release and reopen arbitration

Historical production/research paths explicitly combine execution with resource-release and restoration operations.

For example, historical patterns include:

```text
TARGET-SPECIFIC CONTROL
+
CAN-RESEARCH-WITH-ESCROW / CAN-TRAIN-WITH-ESCROW
        ↓
RELEASE ESCROW
        ↓
EXECUTE RESEARCH / TRAIN
        ↓
RESET RESOURCE CONTROL
```

A particularly strong historical example uses a battering-ram reservation: resource control is set to the ram target, the unit becomes trainable with escrow, escrow is released, the ram is trained, and `sn-resource-control` is then reset to normal spending. citeturn1search0turn1search1

This demonstrates a concrete transition where **execution completion of the immediate command is coupled to release of the reservation policy**.

It does not prove that every historical target follows the same lifecycle.

**Evidence grade:** DIRECT for the constituent state/action sequence.

## 3. Direct evidence: reservations can be abandoned before completion

Historical AI also contains explicit conditions that release escrow without proving that the originally intended upgrade subsequently completed.

Examples include conditions involving:

```text
low resource income
population pressure
under-attack state
missing prerequisite
changed research availability
```

These paths can zero escrow percentages, release escrow, and clear the purpose state.

The critical distinction is:

```text
reservation released
≠
objective succeeded
```

This directly supports the Pass 81 conclusion that release is semantically ambiguous without its surrounding guards.

**Evidence grade:** DIRECT for release behavior; causal classification is context-dependent.

## 4. Recovery can change the next arbitration result

Pass 82 established:

```text
RULE ORDER
+
SIDE EFFECT
+
RESOURCE STATE
=
EFFECTIVE PROCEDURAL ARBITRATION
```

Pass 84 now adds:

```text
RECOVERY ACTION
        ↓
RESOURCE / GOAL / SN MUTATION
        ↓
COMPETING CANDIDATES CHANGE
        ↓
NEXT EXECUTION OPPORTUNITY CHANGES
```

This means recovery is not merely an exception-handling appendix. It is part of the scheduler's state transition surface.

For example:

```text
A reserves gold
↓
A cannot currently execute
↓
recovery releases gold reservation
↓
B becomes affordable
↓
B executes according to procedural order
```

or:

```text
A cannot execute because producer is temporarily unavailable
↓
A retains commitment / alters execution condition
↓
B remains suppressed
↓
A later becomes executable
```

These are AEGIS analytical models grounded in the historical combination of mutable resource policy and procedural arbitration. The exact universal choice between them is not proven.

## 5. Historical AI uses both release and retention mechanisms

The evidence now supports three distinct recovery dispositions:

### R1 — RETAIN
Keep the target-specific state active while waiting for a changed condition.

### R2 — ADJUST
Keep the objective but alter execution parameters, resource policy, or prerequisites.

### R3 — RELEASE / RE-ARBITRATE
Clear the reservation and allow other objectives to compete.

These should not be collapsed into a generic "retry" state.

## 6. Recovery decision boundary

A useful normalized model is:

```text
FAILURE / INTERRUPTION
        ↓
IS ORIGINAL OBJECTIVE STILL VALID?
   ┌───────────────┐
   │               │
  NO              YES
   │               │
   ↓               ↓
RELEASE       CAN EXECUTION BE ADJUSTED?
                  ┌───────────────┐
                  │               │
                 YES             NO
                  │               │
                  ↓               ↓
                ADJUST        WAIT / RETAIN
                  │               │
                  └──────┬────────┘
                         ↓
                   REASSESS / RETRY
```

This is an AEGIS analytical state machine, not an HD primitive.

## 7. Commitment validity and execution feasibility are separate dimensions

Pass 84 exposes a useful distinction:

```text
OBJECTIVE VALIDITY
```

asks whether the strategic reason for the commitment still exists.

```text
EXECUTION FEASIBILITY
```

asks whether the current engine-visible conditions permit execution.

Therefore:

```text
VALID + INFEASIBLE → RETAIN / ADJUST / WAIT
VALID + FEASIBLE    → EXECUTE
INVALID             → RELEASE / RE-ARBITRATE
```

This prevents an important architecture error: treating temporary execution failure as evidence that the strategic objective itself has failed.

## 8. Economic reservation can be the hidden coupling mechanism

Historical AI often expresses commitment through resource-control and escrow rather than through an explicit object representing ownership.

Consequently a failed action can have two separate effects:

```text
ACTION FAILURE
├── execution state changed? NO
└── reservation state changed? MAYBE
```

This produces four analytically distinct states:

| Execution | Reservation | Interpretation |
|---|---|---|
| failed | retained | wait / adjust |
| failed | released | abandon / re-arbitrate |
| partial | retained | continue |
| success | released | complete |

This matrix is AEGIS analysis; the historical scripts provide constituent examples rather than one centralized matrix.

## 9. Starvation risk is now structurally identifiable

Pass 82 established that procedural order can allow an early effective path to consume resources before later paths execute.

Pass 84 establishes that persistent reservations can extend that effect across multiple controller evaluations.

Therefore the combined historical mechanism can structurally produce:

```text
COMMITMENT A
↓
RESOURCE PROTECTION
↓
A REMAINS INEFFECTIVE
↓
RESOURCE REMAINS RESTRICTED
↓
B CANNOT EXECUTE
↓
REPEATED REASSESSMENT
```

This is a **starvation mechanism**, not proof that historical AI systematically suffered starvation in every such case.

No universal fairness mechanism has been found.

## 10. Bounded retention is an AEGIS requirement

Pass 83 required bounded retry.

Pass 84 adds a second requirement:

> **A commitment that retains resources while execution is infeasible must have a bounded retention/reassessment policy.**

Layer-3 design should therefore distinguish:

```text
retry_count
retention_age
last_progress_time
last_failure_class
resource_cost_of_retention
alternative_candidate_value
release_deadline
```

This creates a bridge from failure handling to opportunity-cost reasoning.

## 11. Opportunity cost of retaining a failed commitment

A commitment should not be judged solely by its own expected payoff.

While it retains resources, it imposes an opportunity cost on competing candidates.

AEGIS analytical form:

```text
NET RETENTION VALUE
=
EXPECTED VALUE OF WAITING
−
OPPORTUNITY COST OF BLOCKING ALTERNATIVES
−
RETENTION RISK
```

This is deliberately an AEGIS strategic construct. Historical HD does not prove that it calculates such a scalar.

## 12. Recovery and procedural priority are different layers

Pass 82 showed that rule order can determine which eligible path obtains resources first.

Pass 84 shows that recovery determines whether the resulting commitment continues to occupy the state space.

Thus:

```text
PROCEDURAL PRIORITY
= who gets the current opportunity

RECOVERY POLICY
= what happens after the opportunity fails or changes
```

They interact, but they are not the same mechanism.

## 13. No universal handoff protocol found

The research still does not establish a formal historical protocol of:

```text
A RELEASES
↓
B RECEIVES OWNERSHIP
↓
B ACKNOWLEDGES HANDOFF
```

Instead, shared mutable state and subsequent rule evaluation appear to provide the practical coupling mechanism.

Therefore the safe historical description remains:

> **Controllers mutate shared state; later eligible rules operate on the resulting state.**

The stronger AEGIS concept of explicit commitment ownership and atomic handoff remains architecture work for Layer 3.

## 14. Revised integrated control loop

Passes 80–84 now support this evidence-aware model:

```text
OBSERVE
  ↓
DEMAND / CANDIDATES
  ↓
COMMIT / RESOURCE POLICY
  ↓
AUTHORIZATION
  ↓
ACTION ATTEMPT
  ↓
OBSERVE POSTCONDITION
  ├───────────────┬───────────────┐
  ↓               ↓               ↓
SUCCESS         PARTIAL         FAILURE
  ↓               ↓               ↓
RELEASE        ADJUST         VALIDITY TEST
                                  ├───────┐
                                  ↓       ↓
                               INVALID  VALID
                                  ↓       ↓
                               RELEASE  FEASIBILITY TEST
                                           ├───────┐
                                           ↓       ↓
                                        FEASIBLE INFEASIBLE
                                           ↓       ↓
                                        RETRY   RETAIN/ADJUST/WAIT
                                           \       /
                                            RE-ARBITRATE
```

The model intentionally separates **objective validity** from **execution feasibility**.

## 15. Hostile QC

Rejected:

- every failure should release resources;
- every failure should retain the commitment;
- escrow release proves objective completion;
- resource-control reset proves failure;
- persistent reservation proves successful execution;
- historical AI has a formal fairness scheduler;
- historical AI calculates opportunity cost as an explicit scalar;
- recovery always precedes arbitration;
- recovery and priority are the same mechanism;
- state release constitutes an atomic handoff;
- historical shared state constitutes explicit commitment ownership.

## 16. Evidence ledger

| Proposition | Grade |
|---|---|
| Historical resource-control state can persist across controller evaluations | DIRECT historical source |
| Historical execution paths can release escrow and reset resource control | DIRECT historical source |
| Historical scripts can release escrow without proving objective completion | DIRECT historical source |
| Historical recovery can alter controller parameters | DIRECT historical source |
| Recovery can affect future procedural arbitration | AEGIS-GENERALIZATION grounded in Passes 82–84 |
| Objective validity and execution feasibility are distinct analytical dimensions | AEGIS-GENERALIZATION |
| Historical AI has a universal release-vs-retain policy | NOT PROVEN |
| Historical AI has explicit ownership/handoff transactions | NOT PROVEN |
| Persistent ineffective reservation can structurally create starvation | AEGIS-GENERALIZATION |
| Bounded retention is required for AEGIS | AEGIS ENGINEERING REQUIREMENT |
| Opportunity-cost retention score exists historically | NOT PROVEN |

## 17. Disposition

Pass 84 materially closes the **recovery arbitration boundary** at the level required for Layer-2 methodology.

The historical system can now be characterized as:

```text
DISTRIBUTED CONTROLLERS
+
MUTABLE COMMITMENT / RESOURCE STATE
+
LOCAL POSTCONDITION / FAILURE FEEDBACK
+
PROCEDURAL ARBITRATION
+
CONDITIONAL RELEASE / RETENTION / ADJUSTMENT
```

The remaining open questions are increasingly implementation-specific rather than foundational:

- exact same-pass release→successor handoff;
- complete causal mapping of every historical recovery branch;
- exact timing/latency of individual recovery loops;
- whether any hidden subsystem implements stronger fairness than the inspected sources reveal.

None is currently a prerequisite for beginning Layer 3 architecture once the broader research program is formally closed.

## 18. Layer status

**Layer 1:** 89%; scenario automation remains retired.  
**Layer 2:** ~99%+; commitment, arbitration, execution feedback, and recovery boundaries materially integrated.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

## Pass 84 conclusion

The key result is a distinction that AEGIS must preserve:

> **A failed action does not automatically invalidate the objective that caused it.**

Historical AI provides evidence for retaining state while waiting, changing execution conditions, releasing reservations, and returning to normal spending under different guards. These behaviors interact with procedural arbitration because recovery itself changes the shared state that competing controllers observe.

The resulting architecture principle is therefore:

```text
FAILURE
↓
CLASSIFY EXECUTION RESULT
↓
SEPARATE OBJECTIVE VALIDITY FROM EXECUTION FEASIBILITY
↓
RETAIN / ADJUST / RELEASE
↓
RE-ARBITRATE
```

Layer 3 should make this explicit, bounded, and observable rather than reproduce the historical ambiguity of shared mutable state.