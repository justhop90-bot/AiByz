# PASS 80 — AGGREGATE PRODUCTION OBSERVABILITY AND COMMAND-SUCCESS SEMANTICS

**Layer:** 2 — HD archaeology / evidence only  
**Status:** Research only; no `.per`, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`

## Executive result

Pass 80 deliberately pivots away from the low-value exact-ID branch identified in Pass 79 and attacks a more useful question:

> **What can the HD AI actually know, and what can it prove, about production after it issues a train command?**

The strongest result is that the scripting substrate deliberately exposes **aggregate production observability**, but the semantics are not equivalent to concrete object birth.

Official patch history establishes that `unit-type-count-total` and `up-pending-objects` were changed specifically to include objects in the unit queue, not merely the unit currently training. The UserPatch reference is even more explicit: the total-count family operates on the true number of pending units, including both training and queued units. This means that an AI rule can observe a production commitment at aggregate level without having a concrete object identity.

This yields a much more practical verification model:

```text
TRAIN INTENT
    ↓
QUEUE / PENDING OBSERVATION
    ↓
AGGREGATE PRODUCTION STATE
    ↓
LATER EXISTING-OBJECT OBSERVATION
```

The critical boundary is:

```text
aggregate confirmation ≠ exact command success
aggregate confirmation ≠ exact object birth
aggregate confirmation ≠ deployment
```

The evidence also shows that training-queue configuration directly changes the semantics of the training commands. `sn-enable-training-queue` affects `can-train`, `train`, `up-can-train`, and `up-train`, and later fixes explicitly prevented technologies and units from being queued when the training queue was disabled. Therefore command success is conditional on the engine's current queue policy and eligibility state, not merely on the AI having emitted a `train` action.

## 1. Direct evidence: total counts include queued production

Official AoE2DE Update 36202 states that:

- `unit-type-count-total` now counts additional objects in the unit queue.
- `up-pending-objects` now counts additional objects in the unit queue.

The accompanying UI change in the same update refers explicitly to the queued total in the building queue.

**Evidence grade:** DIRECT official source.

Source: Age of Empires II: Definitive Edition Update 36202.

## 2. Stronger historical specification of the same behavior

The UserPatch AI patch notes provide unusually precise historical wording for the underlying feature request. They state that unit counting commands should consider queued units in addition to units currently in training, and that the `X-count-total` family, including `pending-objects`, therefore operates using the true number of pending units across both training and queue.

This is important because it establishes that these facts were intentionally designed as **aggregate production-state queries**.

It does not establish that a queued unit has a concrete world-object identity, nor does it establish that a count increment proves a specific `train` command was accepted.

**Evidence grade:** DIRECT historical scripting reference.

## 3. Revised production observability ladder

The earlier object-birth ladder remains valid, but Pass 80 adds a practical aggregate layer before exact object identity:

```text
P0  CAPABILITY DEMAND
↓
P1  RULE ELIGIBILITY
↓
P2  CAN-TRAIN / FEASIBILITY
↓
P3  TRAIN COMMAND ISSUED
↓
P4  PENDING / QUEUE OBSERVATION
↓
P5  AGGREGATE TOTAL INCREASE / PENDING STATE
↓
P6  EXISTING-OBJECT OBSERVATION
↓
P7  DEPLOYMENT / TASKING
↓
P8  BATTLEFIELD EFFECT
```

The key interpretation is:

- P0–P2 describe **authorization/eligibility**.
- P3 describes **attempted side effect**.
- P4–P5 provide **aggregate production evidence**.
- P6 provides **world-object evidence**.
- P7–P8 provide **capability/effect evidence**.

No level should be silently promoted into another.

## 4. `can-train` is a precondition, not a receipt

Public scripting examples consistently use the pattern:

```text
(can-train UNIT)
→
(train UNIT)
```

The official scripting patch history also treats `can-train` and `train` as separate affected commands.

Therefore the safe semantic model is:

```text
can-train = eligibility predicate
train     = requested side effect
```

There is no evidence in the inspected sources that `can-train` is a transactional receipt or that its truth guarantees the subsequent command will produce a completed unit.

**Evidence grade:** DIRECT for command distinction; INTERPRETIVE for the receipt terminology.

## 5. Queue policy is part of command semantics

The UserPatch reference states that `sn-enable-training-queue` controls whether an additional unit may be queued at each building and that the strategic number affects:

```text
can-train
can-train-with-escrow
train
up-can-train
up-train
```

Official AoE2DE Update 50292 subsequently fixed a case where AI players could queue technologies and units while `sn-enable-training-queue` was disabled.

This proves a major engineering point:

> **The same apparent `train` request cannot be interpreted independently of queue configuration.**

A production controller must treat queue policy as part of the observable execution environment.

## 6. Pending is not synonymous with completed

The scripting reference defines `up-pending-objects` as a comparison with pending object counts, while `unit-type-count-total` is the aggregate count family.

The historical implementation notes distinguish pending/training/queued objects from already existing objects.

Therefore:

```text
pending > 0
```

can establish that production work is represented in the pending state, but it cannot by itself establish:

```text
unit has completed
unit has spawned into the world
unit has deployed
unit has reached destination
unit has contributed to combat
```

This is a direct application of the evidence-boundary rule rather than an engine claim beyond the sources.

## 7. Why aggregate observability is more valuable than exact-ID archaeology

The exact-ID branch asks whether identifiers from CADE's command protocol can be joined to `MakeObjectAction.obj_id` and ultimately to `Entity.id`.

Pass 80 shows that AEGIS can obtain a useful production state without closing that join:

```text
TRAIN REQUEST
↓
PENDING / QUEUED STATE
↓
TOTAL COUNT
↓
EXISTING COUNT
```

This supports practical questions such as:

- Is the AI carrying pending production?
- Is a production target already represented in the queue?
- Has production state changed after a command opportunity?
- Is the controller repeatedly requesting the same unit because its own pending guard is missing?
- Has aggregate capability increased sufficiently to permit reassessment?

Those questions are directly relevant to AEGIS architecture. Exact object identity is not required for them.

## 8. New command-success taxonomy

Pass 80 replaces the overly binary notion of "command succeeded" with an evidence ladder:

```text
S0 = command rule became eligible
S1 = command action was issued
S2 = pending/queue state reflects production work
S3 = aggregate production state reflects the intended capability
S4 = concrete existing object is observed
S5 = object is deployed/tasking is observed
S6 = battlefield consequence is observed
```

These are not official engine status codes. They are an AEGIS analytical taxonomy for preventing evidence inflation.

The important rule is:

```text
S1 ≠ S2 ≠ S3 ≠ S4 ≠ S5 ≠ S6
```

A controller may use S2 or S3 as sufficient evidence for one purpose while still lacking S4-level proof.

## 9. Failure taxonomy refined

The previous failure taxonomy can now be sharpened:

### F1 — Eligibility failure
`can-train` is false.

Possible causes include missing producer, technology, resources, queue conditions, or other engine constraints. Exact cause must be separately evidenced.

### F2 — Opportunity/competition failure
The rule is theoretically eligible, but another rule or earlier side effect changes the state before the desired production action executes.

This is where the previously established procedural arbitration model applies.

### F3 — Queue-state failure
The requested unit cannot enter the available queue under current queue policy or queue occupancy.

### F4 — Pending-state absence
A command was issued, but subsequent aggregate observations do not show the expected pending state.

This is evidence of a failed or unobserved transition, not proof of the exact failure mechanism.

### F5 — Completion/effect failure
Pending state existed, but the expected existing object or later capability state does not appear.

Again, exact causal diagnosis requires more evidence.

### F6 — Evidence failure
The available observation system cannot distinguish among competing lifecycle explanations.

This is not necessarily a gameplay failure.

## 10. Multi-building production is a critical confounder

A 2025 AoE2DE bug report documents a real limitation: AI `can-train`, `train`, `can-train-with-escrow`, `up-can-train`, and `up-train` were reported to check only the first train location for units that could be trained from multiple building locations.

The report specifically describes Serjeants trainable from both Castles and Donjons, while the AI commands failed to account for the additional train location.

This is important evidence that:

```text
mechanically trainable
≠
AI-command-visible trainability
```

and therefore:

```text
engine capability state
≠
AI scripting abstraction state
```

**Evidence grade:** DIRECT for the reported bug and affected commands; not a universal statement about every current build because the report concerns a specific historical build/issue.

## 11. Production verification architecture now justified

For Layer 3, the strongest low-complexity architecture suggested by current evidence is:

```text
DEMAND
↓
TARGET CAPABILITY
↓
CAN-TRAIN / FEASIBILITY
↓
PENDING GUARD
↓
TRAIN
↓
PENDING / TOTAL OBSERVATION
↓
REASSESS
```

with an optional stronger verification path:

```text
PENDING / TOTAL OBSERVATION
↓
EXISTING OBJECT OBSERVATION
↓
DEPLOYMENT OBSERVATION
```

The exact-ID path should remain an optional forensic enhancement, not a prerequisite.

## 12. Hostile QC

Rejected:

- `can-train` is a transaction receipt.
- `train` command presence proves queue acceptance.
- pending count proves object birth.
- `unit-type-count-total` proves a specific command created a specific unit.
- aggregate count increase proves exact producer attribution.
- queue presence proves eventual completion.
- current multi-location bugs are universal current-build behavior.
- a command failure can be diagnosed from absence of pending state alone.
- aggregate observability can replace all world-state verification.

## 13. Evidence ledger

| Proposition | Grade |
|---|---|
| `unit-type-count-total` includes additional queued objects | DIRECT — official AoE2DE update |
| `up-pending-objects` includes additional queued objects | DIRECT — official AoE2DE update |
| Historical scripting reference explicitly treats queued + training units as pending totals | DIRECT — UserPatch reference |
| `sn-enable-training-queue` affects training command semantics | DIRECT — scripting reference |
| Disabled training queue can prevent unit/tech queueing | DIRECT — official AoE2DE update |
| `can-train` and `train` are distinct scripting operations | DIRECT |
| `can-train` is a transactional receipt | REJECTED / NOT PROVEN |
| `train` proves queue acceptance | NOT PROVEN |
| pending state proves object birth | REJECTED |
| aggregate count proves exact object identity | REJECTED |
| multi-location production can expose AI abstraction limitations | DIRECT historical bug report |
| aggregate production observability is sufficient for some controller decisions | AEGIS-GENERALIZATION |
| S0–S6 command-success ladder | AEGIS-GENERALIZATION |

## 14. Disposition of the exact-ID branch

The Pass 79 identity work remains valuable defensive archaeology.

It should now be classified as:

**OPTIONAL FORENSIC ENHANCEMENT — NOT AN AEGIS IMPLEMENTATION PREREQUISITE.**

Do not spend further Layer-2 passes attempting to prove every CADE identifier join unless a new source makes the expected value materially higher.

The higher-value research surface is now:

```text
aggregate state transition
→
command acceptance evidence
→
commitment release/replacement
→
multi-candidate arbitration
→
world-outcome verification
```

## 15. Layer status

**Layer 1:** 89%; scenario automation remains retired.  
**Layer 2:** materially strengthened; production observability semantics now have a practical evidence ladder.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

## Pass 80 conclusion

The central discovery is not a new command. It is an evidence boundary.

AoE2's HD AI scripting system exposes enough aggregate production state to build a robust controller without possessing exact object identity. `can-train` establishes an eligibility condition; `train` requests a side effect; pending/total counts expose aggregate production state; later object observation can establish realized world state.

That is the practical bridge AEGIS needed.

The exact-ID archaeology can therefore stop being a blocking dependency. The next high-value research target is the **commitment lifecycle**: how an AI reservation/claim is released, replaced, invalidated, or handed to another controller after a production opportunity changes.
