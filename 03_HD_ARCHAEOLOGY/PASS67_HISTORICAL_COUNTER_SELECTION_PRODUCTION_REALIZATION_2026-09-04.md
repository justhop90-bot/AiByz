# Pass 67 — Historical Counter Selection → Production Realization

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Status:** PASS — MAJOR CAUSAL CHAIN CLOSED WITH BOUNDED LIMITS  
**Predecessors:** Passes 11, 45, 55–66

## Mission

Determine how far the historical HD/Promisory corpus can be traced from an observed enemy capability through a concrete Byzantine counter response and into an actual production command.

Target chain:

```text
ENEMY COMPOSITION OBSERVATION
↓
THREAT AGGREGATION
↓
RESPONSE THRESHOLD
↓
COUNTER-PRODUCTION STATE
↓
PRODUCTION-CANDIDATE SEARCH
↓
FEASIBILITY
↓
TRAIN COMMAND
↓
REPLAY CORROBORATION
↓
EFFECTIVE CAPABILITY
```

The final edge is deliberately treated differently from the earlier edges. A `train` command proves an attempted production action, not by itself a completed battlefield unit.

---

# 1. Executive finding

This pass closes the most important historical Byzantine counter chain currently available:

```text
ENEMY CAVALRY-ARCHER / MOUNTED COMPOSITION
↓
`cavarchers`
↓
thresholded response logic
↓
`traincamel = yes`
↓
stable search / producer selection
↓
`can-train`
↓
`train camel-line` / `train imperial-camel`
```

The strongest underlying historical source is the pristine Promisory corpus. Pass 11 already established that `cavarchers` is initialized in `init.per`, populated by threat measurement in `threats.per`, read by research and production logic, and ultimately consumed by concrete camel-training rules. The current public technical reference independently confirms that `camel-line` covers Camel Rider, Heavy Camel Rider, and Imperial Camel Rider and that `can-train` is a feasibility fact while `train` is the production action. citeturn0search1turn0search9

This is materially stronger than the earlier replay-only conclusion.

However, the historical causal chain still stops short of proving that every camel command became a completed, surviving, combat-effective camel. That requires world-state lifecycle evidence.

Therefore the correct closure is:

```text
THREAT → HISTORICAL RESPONSE AUTHORIZATION → PRODUCTION ACTION
```

not:

```text
THREAT → COUNTER SELECTED → COUNTER WON THE FIGHT
```

---

# 2. Source hierarchy

Evidence is ranked:

1. **Pristine historical Promisory source**
2. **Verified `AI (HD version).per` source**
3. **Current installed game data / runtime evidence**
4. **Calibrated replay evidence**
5. **Public technical reference**
6. **Strategic inference**

The public AoE2 AI Scripting Encyclopedia describes itself as a technical reference covering DE and related versions, while its object table identifies Camel Rider 329, Heavy Camel Rider 330, Imperial Camel Rider 207, all on `camel-line` in the Stable. citeturn0search0turn0search1

Version boundaries remain mandatory: public engine documentation can establish command vocabulary and data relationships, but it cannot by itself prove that a historical HD controller used a particular command sequence.

---

# 3. Closure A — threat observation → `cavarchers`

## 3.1 Observation

The historical `threats.per` subsystem measures enemy unit families using engine facts and aggregates the results into the `cavarchers` strategic-number channel.

The measured families include cavalry-archer and related mounted ranged families.

`cavarchers` is explicitly initialized by the historical initialization layer.

**Evidence:** DIRECT historical source.

## 3.2 State classification

`cavarchers` is not itself a raw observation.

The correct ontology is:

```text
ENEMY UNIT OBSERVATION
        ↓
CLASSIFICATION / AGGREGATION
        ↓
`cavarchers`
```

This distinction matters because the value is a transformed strategic signal rather than an untouched engine count.

**Evidence:** DIRECT / COMPOSED.

## 3.3 Reset semantics

The broader threat subsystem resets and repopulates threat aggregates rather than treating them as immutable historical facts.

Therefore a downstream consumer should interpret `cavarchers` as a **current threat signal produced by the controller's measurement cycle**, not as an eternally accumulated enemy total.

Exact update timing remains predicate/cycle dependent and must not be generalized from one observation primitive to all engine facts.

---

# 4. Closure B — threat signal → response authorization

The historical production controller repeatedly tests `cavarchers` at multiple thresholds and, under additional conditions, sets `traincamel` to `yes`.

Representative threshold structure includes:

```text
cavarchers >= 4
cavarchers >= 5
cavarchers >= 7
cavarchers >= 10
cavarchers >= 15
cavarchers >= 25
cavarchers >= 40
```

These thresholds are not standalone.

The rules also consider combinations of:

- own camel-set size;
- military state;
- food buffer;
- age;
- research status;
- unit availability;
- population;
- civ-specific conditions;
- enemy composition.

**Evidence:** DIRECT historical source.

This is crucial because it disproves an overly simple model:

```text
cavarchers >= X → always train camel
```

The actual historical controller is conditional.

---

# 5. What “counter selected” means historically

The historical source does not expose a single semantic object called `COUNTER_SELECTION`.

Instead, the decision is distributed across:

```text
THREAT SIGNAL
↓
THRESHOLD / CONTEXT CONDITIONS
↓
`traincamel = yes`
```

Therefore the most defensible historical interpretation is:

> **The controller authorizes a camel-response state when a mounted-threat signal and its surrounding production conditions satisfy the relevant rule set.**

Calling this a modern “counter-selection engine” would overstate the source.

Calling it merely “unit production” would understate it.

The correct middle description is:

**thresholded response authorization.**

---

# 6. Closure C — response authorization → producer selection

The historical camel-production path does not immediately issue a blind `train` action.

It first performs production-candidate work including:

```text
`up-can-train`
↓
reset search
↓
find local Stable objects
↓
remove unsuitable / in-progress / attacked candidates
↓
order remaining candidates by distance
↓
obtain local search state
↓
construct train target
```

The historical source therefore demonstrates that producer availability is itself part of the production path.

This is an important extension of Pass 64's production topology.

The producer is not simply:

```text
Stable exists → train
```

It is closer to:

```text
Stable candidates
↓
filter candidate state
↓
select usable producer
↓
issue production action
```

**Evidence:** DIRECT historical source.

---

# 7. Closure D — producer selection → feasibility → train

The final historical production path includes `can-train` guards before the train action.

The relevant semantic separation is:

```text
RESPONSE STATE
≠
PRODUCER ELIGIBILITY
≠
AFFORDABILITY / FEASIBILITY
≠
TRAIN ACTION
```

The public command index independently defines `can-train` as checking whether training can start and `can-train-with-escrow` as checking whether it can start including escrowed resources. citeturn0search9

This independently supports the historical distinction between a capability being desired and the engine being willing/able to begin training.

The historical chain therefore closes as:

```text
`traincamel = yes`
↓
producer search
↓
`can-train`
↓
`train camel-line`
```

or the corresponding Imperial Camel branch.

**Evidence:** DIRECT historical source; technical corroboration from current command reference.

---

# 8. Closure E — replay corroboration

The calibrated replay corpus independently showed Byzantine Camel Rider production commands and enemy knight-line production preceding them in the relevant reference games.

Replay A:

```text
Player 1 camel-line queues = 3
first camel queue sequence ≈ 2,945,313
```

Replay B:

```text
Player 1 camel-line queues = 21
first camel queue sequence ≈ 2,918,785
```

The replay evidence also showed enemy knight-line production before the Byzantine camel-production sequences in both cases.

This corroborates that the historical production path has a real runtime manifestation.

But the replay does not prove that the historical `cavarchers` rule fired immediately before those commands.

Therefore:

```text
SOURCE CAUSALITY = CLOSED
REPLAY MANIFESTATION = CORROBORATED
REPLAY CAUSAL LINK = NOT INDIVIDUALLY PROVEN
```

That is the correct evidence boundary.

---

# 9. The counter-realization ladder

Pass 67 produces a more precise ladder for future archaeology:

```text
L0 — THREAT OBSERVED

L1 — THREAT CLASSIFIED

L2 — RESPONSE BECOMES ELIGIBLE

L3 — RESPONSE STATE / COMMITMENT ACTIVATED

L4 — PRODUCER CANDIDATE SELECTED

L5 — TRAIN FEASIBILITY CONFIRMED

L6 — TRAIN COMMAND ISSUED

L7 — QUEUE / PENDING STATE ESTABLISHED

L8 — OBJECT BIRTH

L9 — UNIT DEPLOYED

L10 — UNIT ENGAGES RELEVANT THREAT

L11 — BATTLEFIELD EFFECT VERIFIED
```

Historical source currently closes through **L6** for the camel response chain.

Replay archaeology currently corroborates production activity around **L6/L7**, but does not universally close L8–L11.

This ladder replaces the vague phrase “counter produced.”

---

# 10. Why L6 is not L8

A production action is a request/command.

A completed unit is a world-state transition.

Those are separated by:

```text
QUEUE ADMISSION
↓
QUEUE WAIT
↓
TRAINING TIME
↓
COMPLETION
↓
OBJECT CREATION
↓
DEPLOYMENT
```

The current replay interpreter deliberately preserves this uncertainty. Its pending lifecycle candidates include BUILD, DELETE, DE_QUEUE, and RESEARCH states, and it does not promote ambiguous aggregate correlations into completed-object identity.

This is the correct forensic behavior.

---

# 11. Counter choice is not counter effectiveness

This pass establishes an important strategic separation:

```text
COUNTER AUTHORIZATION
        ≠
COUNTER REALIZATION
        ≠
COUNTER EFFECTIVENESS
```

A camel can be authorized but fail to materialize.

A camel can materialize but arrive late.

A camel can arrive but be outnumbered.

A camel can fight but be neutralized by ranged support, terrain, siege, or other composition effects.

Therefore a future effectiveness metric cannot simply be:

```text
counter chosen = success
```

It must eventually consider at least:

```text
REALIZATION
× ARRIVAL TIMING
× NUMERICAL SUFFICIENCY
× ENGAGEMENT CONDITIONS
× SURVIVAL
× TARGET MATCHUP
```

This is an **AEGIS-GENERALIZATION**, not a historical formula.

---

# 12. The strongest historical chain currently available

The project can now state the following without overclaiming:

```text
ENEMY MOUNTED COMPOSITION
↓
THREAT AGGREGATION (`cavarchers`)
↓
THRESHOLDED RESPONSE RULES
↓
CAMEL RESPONSE STATE (`traincamel`)
↓
STABLE SEARCH / FILTERING
↓
TRAIN FEASIBILITY
↓
CAMEL TRAIN COMMAND
```

That is a **closed historical control chain**.

The chain is not a single rule. It is a distributed cross-module controller.

This is consistent with the broader historical model already established:

```text
DISTRIBUTED CONTROLLERS
+
SHARED STATE
+
RULE ORDER
+
RESOURCE GATES
+
ENGINE SIDE EFFECTS
=
EMERGENT CONTROL SYSTEM
```

Pass 11's provenance closure and Passes 63–65's production archaeology now meet at this point.

---

# 13. What is still missing

The remaining gaps are now much narrower.

## A. Same-pass commitment handoff

Still not proven:

```text
Controller A releases resource control
↓
Controller B claims it
↓
same script pass
```

Pass 66 correctly left this open.

## B. Historical camel object-birth closure

Need direct evidence connecting a specific `train`/queue request to a specific spawned Camel object.

## C. Camel deployment closure

Need proof that the resulting camel leaves the producer and becomes an operational military asset.

## D. Battlefield-effect closure

Need combat/event evidence linking the realized camel population to suppression or defeat of the relevant threat.

## E. Alternative-counter arbitration

The historical source clearly has spears and other responses, but a complete same-state trace of:

```text
CAVALRY THREAT
→ SPEAR VS CAMEL VS OTHER CAPABILITY
→ ARBITRATION
```

is not yet closed as a universal candidate-selection mechanism.

## F. Current-version Byzantine policy

The historical HD chain should not be assumed to be the optimal policy for current DE. Current unit/technology data and current naval mechanics require a separate current-runtime policy layer.

---

# 14. Hostile QC

### Claim: “The historical AI chooses camels because it sees cavalry.”

**Verdict:** Too broad.

Correct:

> The historical Promisory threat state contributes to thresholded camel-response rules under additional conditions.

### Claim: “`traincamel = yes` means camels were produced.”

**Verdict:** False.

It is response/production state, not object-birth proof.

### Claim: “`train camel-line` means a camel entered combat.”

**Verdict:** False.

It is a production action.

### Claim: “Replay camel queues prove the threat rule caused them.”

**Verdict:** False.

They corroborate runtime production behavior, not the exact hidden causal chain.

### Claim: “Camel is the optimal Byzantine cavalry counter.”

**Verdict:** Not established.

The historical code proves a response path, not global optimality.

### Claim: “This is a centralized counter optimizer.”

**Verdict:** False.

The evidence points to distributed, thresholded, rule-mediated response control.

---

# 15. Research implications for Byzantine understanding

The Byzantine strategic model can now be sharpened substantially.

The civilization's discounted Camel Rider family is not merely an item in a counter table.

Its historical value emerges through a chain:

```text
ENEMY MOUNTED PRESSURE
↓
CAMEL RESPONSE SIGNAL
↓
FOOD-FAVORABLE COUNTER ECONOMICS
↓
STABLE PRODUCTION
↓
REINFORCEMENT POTENTIAL
```

The food discount is only one component.

The complete capability depends on:

```text
RESOURCE FLOW
+
GOLD AVAILABILITY
+
STABLE CAPACITY
+
TECHNOLOGY
+
UNIT COUNT
+
TRAIN TIME
+
MAP POSITION
+
REINFORCEMENT DISTANCE
+
SURVIVAL
```

This reinforces the earlier Byzantine conclusion:

> **Byzantine strength is not one bonus; it is the interaction of several capability levers under changing constraints.**

The historical AI captures part of that interaction procedurally.

AEGIS must understand the remainder before Layer 3 begins.

---

# 16. Updated canonical pipeline

The Layer-2 canonical pipeline is now:

```text
GAME WORLD
↓
OBSERVABLE STATE
↓
OBSERVATION
↓
CLASSIFICATION
↓
BELIEF / UNCERTAINTY
↓
STRATEGIC ASSESSMENT
↓
OBJECTIVE
↓
REQUIRED CAPABILITY
↓
CANDIDATE RESPONSE
↓
HARD CONSTRAINTS
↓
SOFT EVALUATION
↓
COMMITMENT
↓
AUTHORITY
↓
ACTION
↓
QUEUE / PENDING STATE
↓
WORLD REALIZATION
↓
VERIFICATION
↓
BELIEF UPDATE
↓
REASSESSMENT
```

Historical HD/Promisory evidence closes only selected portions of this full pipeline.

That is a feature of the research, not a deficiency in the evidence.

It tells us exactly where the historical engine's semantic substrate ends.

---

# 17. Evidence ledger

| Finding | Grade |
|---|---|
| Enemy mounted/cavalry-archer families are measured | DIRECT |
| Measurements are aggregated into `cavarchers` | DIRECT |
| `cavarchers` contributes to thresholded camel-response rules | DIRECT |
| `traincamel` is an explicit response state | DIRECT |
| Camel production searches/selects Stable candidates | DIRECT |
| Production feasibility is separately checked | DIRECT |
| Train action follows the feasibility path | DIRECT |
| Public reference defines camel-line and can-train semantics | DIRECT technical corroboration |
| Replay independently shows Byzantine camel production activity | DIRECT replay evidence |
| Replay proves `cavarchers` caused each camel queue | NOT PROVEN |
| Train command proves object birth | NOT PROVEN |
| Object birth proves deployment | NOT PROVEN |
| Deployment proves combat effectiveness | NOT PROVEN |
| Camel is globally optimal counter | NOT PROVEN |
| Historical system is a centralized counter optimizer | REJECTED |
| Same-pass release→successor handoff | OPEN |

---

# 18. Research closure

Pass 67 closes a major Layer-2 question:

> **How far does the historical Byzantine response system actually travel from enemy observation to concrete counter production?**

Answer:

```text
OBSERVATION
→ THREAT AGGREGATION
→ THRESHOLD RESPONSE
→ COUNTER-PRODUCTION STATE
→ PRODUCER SEARCH
→ FEASIBILITY
→ TRAIN ACTION
```

That chain is historically grounded.

The next missing semantic layer is no longer “does the AI know how to counter cavalry?”

We now know that, for at least the camel-response path, it does implement a concrete threat-to-production response.

The remaining question is **realization and consequence**:

```text
TRAIN
↓
OBJECT
↓
DEPLOYMENT
↓
ENGAGEMENT
↓
RESULT
↓
REASSESSMENT
```

That is where the next high-value archaeology should concentrate.

---

# 19. Layer boundary

No `.per` implementation was created or modified.

No architecture was implemented.

No runtime candidate was promoted.

No canonical bot was changed.

**Layer 2 implementation remains 0%.**
