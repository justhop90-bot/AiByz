# Pass 70 — Concrete Multi-Counter Competition Archaeology

**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Status:** PASS — procedural competition model strengthened; universal counter optimizer not proven  
**Predecessors:** Passes 56–69

## Mission

Test the Pass 69 arbitration model against the strongest available concrete evidence for situations in which multiple response capabilities can plausibly compete for the same strategic objective.

## Executive finding

The evidence supports **competition through overlapping controllers, gates, commitments, resource consumption, and procedural order**, but still does not establish a historical centralized counter-selection optimizer.

The correct model is:

```text
THREAT / OBJECTIVE
↓
MULTIPLE POTENTIAL RESPONSE PATHS
↓
EACH PATH HAS ITS OWN ELIGIBILITY CONDITIONS
↓
RESOURCE / COMMITMENT GATES
↓
PROCEDURAL EXECUTION ORDER
↓
FIRST EFFECTIVE SIDE EFFECT
↓
OTHER PATHS MAY CHANGE STATE
↓
NEXT-PASS REASSESSMENT
```

## 1. Why “multiple counters” is difficult to prove historically

A replay showing Camel production after enemy Knights does not establish that the historical AI simultaneously considered Spearmen, defensive structures, monks, siege, and other responses.

Likewise, a historical Cataphract production action does not prove that ranged units or siege were scored and rejected.

To prove true multi-counter competition, we need evidence of at least two independently eligible response paths sharing a decision context and an execution bottleneck.

That standard is deliberately higher than merely observing two different unit types in the same game.

## 2. Strongest concrete competitive surface: shared economy / production

The historical source archaeology directly establishes that multiple production and research demands can interact through shared resources and state.

Representative demands include:

```text
SIEGE
CAMEL
OTHER MILITARY UNITS
NAVY
TECHNOLOGIES
AGE TRANSITION
INFRASTRUCTURE
```

A demand can therefore be strategically desirable yet fail to obtain execution opportunity because another demand has already consumed or protected the relevant resources.

This is genuine competition for a shared execution surface even when the controllers do not explicitly compare their goals.

## 3. Procedural competition is directly evidenced

Historical AI commentary establishes that rule ordering matters because an earlier applicable production rule can consume resources before a later production rule executes.

Therefore:

```text
A eligible
B eligible
↓
A executes first
↓
resource state changes
↓
B may no longer execute
```

This is sufficient to create deterministic procedural arbitration without a utility function.

The distinction is fundamental:

```text
FIRST EFFECTIVE ACTION
≠
GLOBAL OPTIMUM
```

## 4. Counter competition is mediated by capability gates

For Byzantine mounted pressure, the Camel path is unusually well established:

```text
MOUNTED / CAVARCHER SIGNAL
↓
THREAT AGGREGATE
↓
THRESHOLD
↓
CONTEXT GATES
↓
TRAINCAMEL
↓
PRODUCER SEARCH
↓
CAN-TRAIN
↓
TRAIN CAMEL-LINE
```

But the presence of this path does not prove that another mounted-counter path was concurrently eligible.

Therefore the correct conclusion is:

**Camel is a historically evidenced response path, not a historically proven winner of a global counter contest.**

## 5. Concrete Byzantine candidate competition

Current strategic mechanics create several legitimate response families to mounted pressure:

```text
CAMEL
SPEARMAN
DEFENSIVE POSITION / FORTIFICATION
MONK SUPPORT
SIEGE SUPPORT
DIRECT MILITARY PRESSURE
```

These are current strategic alternatives. They should not be described as one historical candidate list.

The historical evidence shows individual policy ladders operating over selected signals rather than a universal candidate enumeration mechanism.

## 6. Resource commitment changes competition after candidate activation

Passes 55–60 established a stronger mechanism:

```text
CANDIDATE A
↓
RESOURCE COMMITMENT
↓
SHARED RESOURCE STATE CHANGES
↓
CANDIDATE B'S FEASIBILITY / AUTHORIZATION MAY CHANGE
```

This creates **implicit competition** even without a common decision procedure.

Conversely:

```text
A invalidated
↓
resources released
↓
B becomes feasible again
```

Therefore the candidate surface is dynamic.

## 7. Competition has multiple meanings

AEGIS must distinguish:

### Strategic competition
Two responses solve the same objective or threat.

### Economic competition
Two demands require the same resources.

### Production competition
Two demands require constrained production capacity.

### Procedural competition
Two eligible rules can execute but rule order gives one the first opportunity.

### Temporal competition
Two responses compete for a shrinking reaction window.

### Information competition
A response can be delayed because the evidence needed to authorize it has not yet arrived or is stale.

These mechanisms can overlap.

## 8. Historical arbitration surface

Pass 69's abstraction is strengthened:

```text
ARBITRATION SURFACE =
CANDIDATE SET
× RESOURCE STATE
× TECHNOLOGY STATE
× PRODUCER STATE
× COMMITMENT STATE
× TEMPORAL STATE
× THREAT STATE
× PROCEDURAL ORDER
```

A candidate does not merely have a utility value. It has an execution opportunity determined by its position on this surface.

Again, this is an AEGIS analytical abstraction, not a historical engine structure.

## 9. A more rigorous counter-selection test

For future historical claims, classify evidence as follows:

```text
T0 = candidate exists mechanically
T1 = candidate is represented in AI policy
T2 = candidate becomes eligible
T3 = candidate competes with another eligible path
T4 = candidate receives execution opportunity
T5 = candidate executes
T6 = candidate realizes in world
T7 = candidate affects battlefield outcome
```

Current evidence frequently reaches T2 or T5 but does not automatically reach T3 or T7.

This prevents a common archaeological error:

```text
OBSERVED UNIT
↓
ASSUMED SELECTED COUNTER
↓
ASSUMED COMPETING ALTERNATIVES
↓
ASSUMED OPTIMIZATION
```

Each arrow requires independent evidence.

## 10. Important negative result

No universal historical structure of the form:

```text
GENERATE ALL COUNTERS
↓
SCORE ALL COUNTERS
↓
NORMALIZE COST / TIME / RISK
↓
SELECT ARGMAX
```

has been established.

This negative result is valuable. It prevents Layer 3 from accidentally encoding a fictitious historical mechanism.

## 11. Current-DE reconciliation

Current game mechanics must be evaluated independently of historical AI policy.

Official Update 169123 states that the February 2026 naval overhaul added a Hulk-line counter to Fire Ships and changed the Byzantine Fire Ship/Dromon attack-speed bonus from +20% to +25%. citeturn0search1

The official naval-overhaul announcement describes Hulks as having high armor and being resistant to Fire Ship attacks, while remaining vulnerable to longer-ranged ships. citeturn0search0

Therefore a modern Byzantine naval counter model cannot simply inherit historical naval policy from the HD corpus.

## 12. Hostile QC

**Claim:** Two unit types appear in a replay, therefore the AI compared them.

**Verdict:** REJECTED.

**Claim:** A threshold proves optimization.

**Verdict:** REJECTED. It proves policy activation at a measured boundary.

**Claim:** Resource contention proves intentional priority.

**Verdict:** Not necessarily. Competition can emerge procedurally without strategic intent being encoded.

**Claim:** A production command proves a successful counter.

**Verdict:** REJECTED. Pass 68's realization ladder remains mandatory.

**Claim:** Current mechanics prove historical AI behavior.

**Verdict:** REJECTED.

## 13. Closure

Pass 70 materially strengthens the arbitration model:

```text
CANDIDATE GENERATION
≠
CANDIDATE ELIGIBILITY
≠
CANDIDATE COMPETITION
≠
ARBITRATION
≠
EXECUTION
≠
REALIZATION
≠
EFFECT
```

The historical system is best understood as a distributed procedural control environment in which multiple controllers can compete indirectly through shared state and resources.

The central optimizer hypothesis remains unsupported.

## Research frontier after Pass 70

Highest-value unresolved questions:

1. same-pass release → successor claim;
2. exact object-birth lineage after train;
3. deployment linkage;
4. engagement/effect verification;
5. one concrete replay containing independently provable competing response paths;
6. final cross-pass hostile QC;
7. complete current-DE Byzantine policy reconciliation.

No `.per` implementation, architecture construction, runtime promotion, or deployment is authorized by this pass.
