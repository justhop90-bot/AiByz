# AEGIS World Model — Carpenter Pass 3

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** CARPENTER  
**Status:** SIMPLIFICATION / CONTRACT REVIEW — NO IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`

## Mission

Attack Architect Pass 3 and remove anything that does not earn its complexity. The target is the smallest architecture that still survives stale information reaching execution, obsolete capability, command-as-success, partial observation, missing-search-as-destruction, strategic interpretation contaminating world truth, infinite failed retries, competing writers, and scheduler starvation.

**No `.per` implementation, runtime execution, or ABI allocation is authorized.**

## 1. Verdict

**PASS — with substantial compression.**

The Architect contract is sound, but several useful concepts should remain rules rather than physical subsystems.

Final physical model:

```text
OBSERVE / QUALIFY
        ↓
WORLD STATE
        ↓
SITUATION
        ↓
CAPABILITY
        ↓
DECIDE / COMMIT
        ↓
EXECUTE
        ↓
VERIFY
        ↓
WORLD STATE
```

No dedicated physical room is required for Commitment, Revalidation, Supersession, Currentness, Provenance, Contradiction, Recovery, or Verification Profiles.

## 2. Commitment is a state transition

Keep the semantic distinction:

```text
candidate ≠ decision ≠ commitment ≠ command
```

But physically use:

```text
DECIDE → COMMIT → EXECUTE
```

A commitment is the point at which a selected decision becomes an accepted obligation with consequences. When material, it retains the objective, required capability, assumptions that could invalidate it, owner/executor, and success/failure condition. No universal commitment database is justified.

**Decision: COMMITMENT REMAINS A STATE TRANSITION INSIDE DECISION.**

## 3. Revalidation is a gate

Do not build a transaction or global freshness engine.

```text
BEFORE CONSEQUENTIAL EXECUTION
        ↓
DID A MATERIAL ASSUMPTION CHANGE?
      /       \
    NO         YES
    ↓           ↓
 EXECUTE    REVALIDATE
                ↓
           STILL VALID?
             /    \
           YES     NO
            ↓       ↓
         EXECUTE  REPLAN
```

This defends against stale execution without continuous expensive replanning.

**Decision: REVALIDATION IS A GATE.**

## 4. Supersession is publication logic

No Supersession Manager.

```text
NEW EVIDENCE → QUALIFY → REPLACE / RETAIN / UNRESOLVE
```

The eventual goal/SN representation is an ABI qualification problem. Architecture specifies the semantic rule only.

**Decision: SUPERSESSION IS A WORLD-STATE PUBLICATION RULE.**

## 5. Provenance is conditional

Provenance earns representation only when evidence source materially affects interpretation, conflict resolution, supersession, or verification. It is not mandatory metadata on every scalar.

**Decision: PROVENANCE IS ON-DEMAND SEMANTICS.**

## 6. Current / Last-Known / Unknown / Contradicted

Keep the semantic protection; remove the machinery.

```text
QUALIFIED VALUE
      ↓
current when supported
last-known when no longer current
unresolved when conflicting
absent when unknown
```

Do not create four stores. `UNKNOWN` can normally be represented by absence of a qualified value. `CONTRADICTED` exists only when materially relevant evidence cannot safely be reconciled.

These are semantic qualifications, not rooms or universal state machines.

**Decision: KEEP SEMANTICS; REMOVE MACHINERY.**

## 7. Verification depth is policy

Keep the principle that verification depth scales with consequence and failure cost:

- routine low-cost action → cheap verification;
- material production/build → normal verification;
- strategic/high-cost commitment → strong verification.

No profile registry is required at architecture stage.

**Decision: VERIFICATION DEPTH IS POLICY.**

## 8. Recovery is a cross-cutting control

Recovery does not belong inside World State.

Minimum rule:

```text
FAILED / DEVIATING COMMITMENT → CHANGE SOMETHING
```

Repair, alter assumptions, select another candidate, abandon, or escalate/reassess. A failed commitment may never re-enter execution unchanged forever.

**Decision: RECOVERY IS CONTROL LOGIC, NOT WORLD-STATE MACHINERY.**

## 9. The load-bearing boundary

The critical architecture is:

```text
WORLD FACT
      ↓
INTERPRETATION
      ↓
DECISION
      ↓
ACTION
      ↓
EVIDENCE
```

Never collapse:

```text
OBSERVATION ≠ BELIEF
BELIEF ≠ SITUATION
SITUATION ≠ CAPABILITY
CAPABILITY ≠ DECISION
DECISION ≠ COMMAND
COMMAND ≠ SUCCESS
SUCCESS CLAIM ≠ VERIFIED WORLD FACT
```

These distinctions earn their complexity because each prevents a demonstrated failure mode.

## 10. Minimum World Model

Two physical responsibilities only:

### Observation Workbench

```text
SEARCH / FILTER / SELECT / READ / MEASURE / DERIVE / QUALIFY
```

### World State

Persist only observations that earn persistence because multiple important consumers need them, identity continuity matters, recomputation is materially expensive, forgetting causes dangerous strategic amnesia, or the fact represents a meaningful transition.

Everything else may remain transient.

## 11. Minimum Situation

Situation earns a physical boundary because it answers a different question:

> What does the observed world mean strategically right now?

Example:

```text
WORLD STATE: enemy stable observed
SITUATION: cavalry-production risk elevated
```

Threat, opportunity, urgency, vulnerability, map-control implications, and tempo remain interpretations, not world facts.

## 12. Minimum Capability

Capability earns separation because it answers:

> Can we actually do this?

rather than:

> Should we do this?

Minimum inputs:

```text
WORLD STATE
TECHNOLOGY
INFRASTRUCTURE
PRODUCTION CAPACITY
RESOURCES
TIME
```

Minimum semantic outputs:

```text
FEASIBLE / AVAILABLE / EFFECTIVE
```

No universal capability database is implied.

## 13. Minimum Planning / Decision

The old Objective, Requirement, Constraint, Candidate, Arbitration, and Commitment rooms should not automatically become separate physical rooms.

Use one Planning/Decision area with logical stages:

```text
OBJECTIVE → OPTIONS → CONSTRAINTS → ARBITRATION → SELECT → COMMIT
```

Explicit reasoning remains; unnecessary walls disappear.

## 14. One authoritative publisher

Keep one rule:

> **One semantic fact has one authoritative publisher; many systems may consume it.**

Example:

```text
WORLD STATE: enemy stable observed
       │
       ├── Situation
       ├── Scouting
       ├── Attention
       ├── Opponent Model
       └── Capability
```

Consumers may derive interpretations but cannot silently become competing publishers of the underlying world fact.

## 15. Scheduler survives the cut

Scheduler remains load-bearing because observation/search operations have meaningful cost and critical changes can invalidate a plan.

Its responsibilities are:

```text
WHAT TO OBSERVE
WHEN TO OBSERVE IT
WHEN TO REASSESS
WHEN TO VERIFY
```

Separation remains:

```text
SCHEDULER → WHEN
WORLD MODEL → WHAT IS OBSERVED
SITUATION → WHAT IT MEANS
DECISION → WHAT TO DO
```

## 16. Smallest safe feedback loop

```text
WORLD STATE
    ↓
SITUATION
    ↓
CAPABILITY
    ↓
DECISION / COMMIT
    ↓
EXECUTION
    ↓
VERIFICATION
    ↓
WORLD STATE
```

Cross-cutting controls:

```text
SCHEDULER / ATTENTION / OWNERSHIP / EVIDENCE
REVALIDATION / RESOURCE LEDGER / MAP / DOCTRINE
RISK / MEMORY / STATE INTEGRITY / RECOVERY
```

No transaction engine, universal freshness engine, universal event bus, or universal object database.

## 17. Adversarial retest

| Failure | Surviving mechanism |
|---|---|
| Enemy disappears | last-known/unknown semantics; no destruction inference |
| Enemy changes before execution | material revalidation gate |
| Producer destroyed | capability invalidation + revalidation |
| Command fails | verification observes resulting state |
| Partial census | observation scope remains meaningful |
| Two systems disagree | authoritative publisher for underlying fact |
| Stale retry | recovery must change, abandon, or escalate |
| Expensive polling | Scheduler controls cadence |
| Architecture becomes bureaucracy | no universal metadata/transaction machinery |

**All previously identified failure classes remain covered.**

## 18. Explicit cuts

Not physical architecture:

- Commitment Room;
- Revalidation Manager;
- Supersession Manager;
- Freshness Manager;
- Provenance Manager;
- Contradiction Manager;
- Verification Profile Registry;
- Recovery Engine inside World State;
- universal generation subsystem;
- universal timestamp subsystem;
- universal confidence subsystem;
- world-event bus;
- object database;
- one record per unit;
- one manager per semantic qualifier.

These may return only if later evidence demonstrates a concrete failure that cannot be solved without them.

## 19. Final floor plan

```text
                         STRATEGIC CONTROL
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
       WORLD / OBSERVATION                    BELIEF / HISTORY
              │                                   │
              └────────────────┬──────────────────┘
                               ↓
                         SITUATION ANALYSIS
                               ↓
                          PLANNING / DECISION
                               ↓
                         CAPABILITY CHECK
                               ↓
                          DECIDE / COMMIT
                               ↓
                  ┌────────────┴────────────┐
                  ↓                         ↓
          ECONOMIC EXECUTION        MILITARY EXECUTION
                  │                         │
                  └────────────┬────────────┘
                               ↓
                           VERIFICATION
                               ↓
                            RECOVERY
                               ↓
                           WORLD STATE
```

This pass does not finalize the entire apartment's physical room layout; it establishes the minimum World Model contract and its interfaces.

## 20. Behavioral-return test

| Concept | Return | Decision |
|---|---|---|
| Observation Workbench | engine observation | KEEP |
| World State | prevents strategic amnesia | KEEP |
| Situation | converts facts into significance | KEEP |
| Capability | prevents impossible plans | KEEP |
| Decision | selects among competing actions | KEEP |
| Commitment semantics | prevents silent plan drift | KEEP AS STATE |
| Revalidation | prevents stale execution | KEEP AS GATE |
| Verification | prevents command=success | KEEP |
| Scheduler | controls expensive observation/reassessment | KEEP |
| Provenance | conflict/evidence support when needed | CONDITIONAL |
| Supersession | prevents stale overwrite | KEEP AS RULE |
| Universal freshness | not justified | CUT |
| Universal generation | not justified | CUT |
| Universal confidence | not justified | CUT |
| Transaction engine | unnecessary | CUT |
| Universal event bus | unnecessary | CUT |
| Object database | excessive | CUT |

## 21. Acceptance

The compressed architecture passes if it:

1. distinguishes world facts from interpretations;
2. distinguishes capability from decision;
3. distinguishes decision from commitment;
4. distinguishes command from verified result;
5. can invalidate materially stale execution;
6. does not require universal freshness machinery;
7. does not require universal generation machinery;
8. does not infer destruction from missing search;
9. does not infer totals from partial observation;
10. prevents strategic consumers from becoming world-fact publishers;
11. prevents unchanged infinite retries;
12. gives Scheduler control over computational attention;
13. keeps World State selective;
14. allows provenance when materially useful without making it universal;
15. preserves supersession semantics without a transaction system;
16. leaves representation and ABI qualification to later Scientist work;
17. adds no runtime implementation during architecture.

**CARPENTER RESULT: PASS.**

## Final conclusion

The Architect did not make a conceptual mistake. It was beginning to turn useful semantic distinctions into infrastructure.

The Carpenter removes that infrastructure while retaining the distinctions that prevent failure.

> **Keep distinctions that prevent failure. Remove machinery that merely records those distinctions.**

Minimum safe World Model contract:

```text
OBSERVE
  ↓
QUALIFY
  ↓
WORLD STATE
  ↓
INTERPRET
  ↓
ASSESS CAPABILITY
  ↓
DECIDE / COMMIT
  ↓
REVALIDATE WHEN MATERIAL
  ↓
EXECUTE
  ↓
VERIFY
  ↓
UPDATE WORLD STATE
```

**NEXT MODE: ⚔️ ADVERSARY**

The next adversarial pass should stop focusing narrowly on World Model internals and attack the apartment under full-system conditions: Dark Age opening, economic allocation, first scouting divergence, enemy cavalry transition, production bottleneck, military commitment, failed attack, recovery, Castle transition, opponent reversal, map-control conflict, and late-game resource exhaustion.

The question becomes:

> **Can the entire apartment remain coherent when multiple rooms simultaneously believe they need different things?**
