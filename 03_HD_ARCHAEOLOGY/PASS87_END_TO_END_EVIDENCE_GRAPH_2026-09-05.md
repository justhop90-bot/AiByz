# PASS 87 — END-TO-END EVIDENCE GRAPH / HISTORICAL-TO-AEGIS BOUNDARY

**Layer:** 2 — HD archaeology / evidence synthesis  
**Status:** Research only; no `.per` implementation, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Predecessor:** Pass 86  
**Scope:** End-to-end integration of the accumulated Layer-2 evidence through Pass 86, with hostile separation of historical fact, operational inference, AEGIS generalization, and open hypothesis.

---

## Executive result

Pass 87 attacks the highest-value remaining Layer-2 question:

> **Can the accumulated archaeology be converted into one traceable evidence graph from historical source, through observable mechanism and semantic interpretation, to an AEGIS architectural requirement—without silently promoting an AEGIS design choice into a historical fact?**

The answer is **yes, with explicit boundaries**.

The resulting evidence graph is:

```text
HISTORICAL / ENGINE EVIDENCE
        ↓
OBSERVED MECHANISM
        ↓
SEMANTIC CLAIM
        ↓
EVIDENCE GRADE
        ↓
AEGIS ABSTRACTION
        ↓
ARCHITECTURAL REQUIREMENT
        ↓
IMPLEMENTATION CONSEQUENCE
        ↓
VALIDATION REQUIREMENT
```

The critical result is that the first three layers cannot be collapsed into the last four.

A historical `.per` rule may prove a state mutation. It does not, by itself, prove that the historical authors conceived a formal commitment object. An official patch may prove that a command's semantics changed. It does not prove that a Byzantine strategy should optimize that command in a particular way. A replay may prove that a production command was recorded. It does not prove why the AI issued it.

The resulting permanent epistemic boundary is:

```text
HISTORICAL FACT
    ≠
AEGIS INTERPRETATION
    ≠
AEGIS DESIGN DECISION
    ≠
RUNTIME VALIDATION RESULT
```

This pass therefore closes the **evidence-to-architecture mapping problem** at the methodology level while preserving all genuinely unresolved claims.

---

# 1. The canonical evidence graph

Every future major AEGIS subsystem should be traceable through the following chain:

```text
[E0 SOURCE]
    ↓
[OBSERVED MECHANISM]
    ↓
[SEMANTIC INTERPRETATION]
    ↓
[EVIDENCE GRADE]
    ↓
[AEGIS GENERALIZATION]
    ↓
[REQUIREMENT]
    ↓
[DESIGN]
    ↓
[IMPLEMENTATION]
    ↓
[TEST]
```

Layer 2 may populate the first six nodes.

Layer 3 owns the design and implementation nodes.

Validation belongs to the runtime/test layer and must not be retroactively used to rewrite historical evidence.

A result from a Layer-3 experiment can establish that an AEGIS design works. It cannot prove that historical HD implemented that design.

---

# 2. Permanent evidence-grade vocabulary

The project now uses four principal grades.

## E0 — Direct evidence

The proposition is directly represented by an authoritative source, executable source artifact, official patch documentation, or reproducible observation.

Examples include:

```text
historical source contains set-strategic-number
historical source contains release-escrow
official patch note changes unit-type-count-total
official patch note changes queue behavior
replay contains a recorded Make/production command
CADE schema contains Command.Make.uniqueId
uncage model declares MakeObjectAction.obj_id
```

E0 does not mean the interpretation is universal. It means the underlying observation is directly evidenced.

## E1 — Strong operational inference

The proposition follows closely from several E0 observations with limited architectural assumptions.

Examples:

```text
shared state mutation
+
later state-dependent rule guards
+
known rule-order effects
→
state mutation is operationally consequential to later controller evaluation
```

E1 is not direct engine documentation and must not be cited as such.

## E2 — AEGIS generalization

The project creates a cleaner systems concept from several lower-level observations.

Examples:

```text
commitment
candidate set
procedural arbitration
objective validity
execution feasibility
capability latency
failure taxonomy
postcondition
belief state
information value
option value
```

E2 concepts are legitimate architecture inputs but are not historical feature claims.

## E3 — Hypothesis / unresolved proposition

The proposition remains open, weakly supported, or dependent on a missing bridge.

Examples:

```text
uniqueId == Entity.id
Command.Make.objId == MakeObjectAction.obj_id
formal historical ownership transfer
universal historical fairness
historical argmax optimizer
atomic same-pass handoff
hidden historical Byzantine utility function
```

E3 content must not be promoted into historical requirements.

---

# 3. The end-to-end graph in operational detail

The complete AEGIS research-to-engineering trace is:

```text
GAME / ENGINE
   ↓
FACT / EVENT / SOURCE OBSERVATION
   ↓
NORMALIZED STATE
   ↓
INTERPRETED SEMANTIC
   ↓
EVIDENCE GRADE
   ↓
CONTROL IMPLICATION
   ↓
AEGIS REQUIREMENT
   ↓
DESIGN OBJECT
   ↓
RUNTIME OPERATION
   ↓
POSTCONDITION
   ↓
MEASUREMENT
   ↓
VALIDATION
```

The graph is deliberately directional.

For example:

```text
official queue patch
→ queue semantics changed
```

is valid.

But:

```text
queue semantics changed
→ Byzantine AI should always maintain maximum queue depth
```

does not follow without an independent strategic argument.

Likewise:

```text
camel production observed after enemy knight production
→ temporal correlation exists
```

is valid.

But:

```text
temporal correlation
→ historical AI selected camel because it detected knights
```

is not established without causal evidence.

---

# 4. Evidence chain A — procedural arbitration

## Source

Historical HD AI contains explicit author commentary stating that rule ordering matters because the first rule executed can consume resources such that later rules cannot spend them, with siege training intentionally placed above building.

## Observed mechanism

```text
RULE ORDER
↓
FIRST EFFECTIVE SIDE EFFECT
↓
RESOURCE CHANGE
↓
LATER RULE'S OPPORTUNITY CHANGES
```

## Grade

**E0** for the specific historical statement and local behavior.

## Semantic claim

Rule order can function as procedural economic arbitration in relevant historical contexts.

## AEGIS generalization

```text
procedural arbitration
=
ordered conditional candidates
+
state gates
+
resource state
+
side effects
```

## Requirement

AEGIS must account for the fact that the execution substrate is stateful and procedural; strategic intent cannot be compiled into an unordered collection of independent commands.

## Design consequence

Layer 3 needs an explicit arbitration boundary between strategic valuation and executable actions.

## Validation consequence

A candidate scheduler must be tested not only for selected intent but also for downstream resource-state effects and suppressed competitors.

## Boundary

This does **not** prove a historical numeric utility optimizer.

---

# 5. Evidence chain B — shared controller state

## Source

Historical AI repeatedly writes and later reads goals and strategic numbers, including strategy, unit, control, and resource-policy state.

## Observed mechanism

```text
RULE A
↓
STATE WRITE
↓
RULE B GUARD
↓
STATE-DEPENDENT PATH
```

## Grade

E0 for state writes and reads.

E1 for the operational conclusion that the mutation affects later controller behavior.

## AEGIS generalization

Shared mutable controller state acts as a coordination substrate.

## Requirement

AEGIS state channels must have explicit ownership, lifecycle, validity, and provenance semantics rather than relying on accidental integer reuse.

## Design consequence

Layer 3 should distinguish:

```text
state value
state meaning
state owner
state generation
state freshness
state source
```

## Boundary

Historical mutable state does not prove a formal ownership model.

---

# 6. Evidence chain C — same-pass visibility

## Source

Passes 82 and 85 establish repeated shared-state mutation and later state-dependent rules, combined with explicit historical importance of rule order.

## Grade

E1 / high-confidence operational model for direct script-visible state mutation.

## AEGIS generalization

A controller may use same-pass state changes to influence later controller evaluation.

## Requirement

AEGIS cannot assume that all state writes are deferred until a later global planning cycle.

## Design consequence

The implementation must define exactly which state transitions are:

```text
immediate
queued
next-cycle
world-observable
```

## Boundary

Same-pass state visibility is not same-pass world realization.

Same-pass visibility is also not atomic ownership transfer.

---

# 7. Evidence chain D — two clocks

The accumulated evidence supports a mandatory separation between controller time and world time.

## Controller clock

```text
RULE
↓
GOAL / SN / FLAG / TIMER MUTATION
↓
LATER CONTROLLER EVALUATION
```

## World clock

```text
COMMAND
↓
ENGINE PROCESSING
↓
QUEUE / PENDING
↓
WORLD CHANGE
↓
OBSERVATION
```

## Grade

E1/E2 methodological synthesis grounded in direct state and queue evidence.

## Requirement

AEGIS actions must never equate controller acknowledgment with world completion unless a postcondition establishes the latter.

## Design consequence

Every side-effecting operation needs two independently represented states where relevant:

```text
controller_state
world_state
```

This is one of the most important architecture protections recovered in Layer 2.

---

# 8. Evidence chain E — production execution

## Source

Official AoE2DE patch history establishes that `unit-type-count-total` and `up-pending-objects` include additional queued objects. Official updates also establish that training queue configuration affects the semantics of AI training commands. Historical scripting patterns distinguish `can-train` from `train`.

## Observed mechanism

```text
DEMAND
↓
CAN-TRAIN / FEASIBILITY
↓
TRAIN REQUEST
↓
PENDING / QUEUE
↓
AGGREGATE CAPABILITY
↓
EXISTING OBJECT
↓
DEPLOYMENT
↓
EFFECT
```

## Grade

E0 for the individual command/fact semantics supported by the cited sources.

E2 for the complete ladder as a forensic/AEGIS abstraction.

## Requirement

Production verification must be multi-level.

## Design consequence

AEGIS should represent at least:

```text
requested
eligible
authorized
issued
pending
completed
available
deployed
verified-effective
```

A system must not silently convert one state into another.

## Boundary

`can-train` is not a receipt.

`train` is not automatically a completed unit.

Pending is not completion.

Aggregate increase is not exact object identity.

Object existence is not battlefield effectiveness.

---

# 9. Evidence chain F — exact identity namespaces

Passes 75–79 established that multiple identity domains exist in the replay/CADE ecosystem.

```text
I1 = replay document model-object ID
I2 = World.entities key
I3 = Ref target
I4 = Entity.id
I5 = MakeObjectAction.obj_id
I6a = Command.Make.objId
I6b = Command.Make.uniqueId
```

## Direct findings

The replay document allocator assigns internal model-object IDs and can recycle them. The playback path resolves those IDs to an Entity model and separately reads `Entity.id`. The CADE `Command.Make` schema contains both `objId` and `uniqueId`. The same `uniqueId` field occurs across multiple command families.

## Grade

E0 for the existence of the separate domains.

E3 for unresolved joins.

## Rejected joins

```text
I6b == I4
I6a == I5
I5 == I4
I5 == I1
I6a == I4
I6b == I4
```

unless independently proven.

## Requirement

AEGIS forensic tooling must use semantic joins, not numerical coincidence.

## Design consequence

Identity adapters should carry explicit namespace/type information.

## Boundary

Exact IDs remain optional for aggregate production observability. They are valuable for high-confidence forensic closure, but not required for every controller decision.

---

# 10. Evidence chain G — commitment lifecycle

Historical source demonstrates mutable resource-control state, escrow, goals, research-pending state, timers, release/reset, replacement, and retry-like behavior.

## Observed normalized lifecycle

```text
FREE
↓
TARGET SELECTED
↓
POLICY / RESOURCE PROTECTION
↓
EXECUTION
↓
PROGRESS
↓
RELEASE / RESET / REPLACE
↓
FREE OR NEW TARGET
```

## Grade

E0 for the constituent historical operations.

E2 for the unified commitment abstraction.

## Requirement

AEGIS commitments require explicit lifecycle semantics.

## Design consequence

A future commitment record should distinguish at least:

```text
target
objective
validity
resource policy
owner
generation
attempt count
last evidence
last action
next review
release condition
replacement candidate
```

## Boundary

Historical HD does not prove a first-class commitment object.

AEGIS may deliberately introduce one because it solves a demonstrated systems problem.

That introduction is a design decision, not historical reconstruction.

---

# 11. Evidence chain H — failure and recovery

Historical HD contains subsystem-specific recovery behaviors.

Examples include age-transition rollback, failed-hunt parameter adjustment, state reset, resource release, and altered subsequent execution conditions.

## Observed pattern

```text
ATTEMPT
↓
EXPECTED TRANSITION
↓
OBSERVATION
↓
FAILURE / INTERRUPTION
↓
ROLLBACK / ADJUST / RETAIN / RELEASE
```

## Grade

E0 for specific historical examples.

E2 for the unified failure taxonomy.

## Requirement

AEGIS must not use a universal `failure → retry` rule.

## Design consequence

Recovery policy must be tied to postcondition and failure class.

At minimum:

```text
opportunity
resource
producer
queue
temporal
target invalidation
partial progress
evidence ambiguity
```

## Boundary

These are AEGIS analytical classes, not engine error codes.

---

# 12. Evidence chain I — release versus retention

Historical recovery demonstrates both persistence and release.

## Retention

```text
TARGET-SPECIFIC STATE
↓
EXECUTION CONDITION CHANGES
↓
TARGET STATE REMAINS
↓
LATER EXECUTION
```

## Release

```text
TARGET-SPECIFIC STATE
↓
ESCROW / POLICY RELEASE
↓
NORMAL OR NEW ARBITRATION
```

## Grade

E0 for constituent state transitions.

E2 for retention/release as generalized recovery dispositions.

## Requirement

AEGIS must evaluate whether waiting remains strategically justified instead of releasing or retrying blindly.

## Design consequence

A commitment should have bounded retention.

A useful AEGIS analytical quantity is:

```text
NET RETENTION VALUE
=
EXPECTED VALUE OF WAITING
−
OPPORTUNITY COST OF BLOCKING ALTERNATIVES
−
RETENTION RISK
```

This formula is explicitly an AEGIS design construct, not a recovered HD scalar.

---

# 13. Evidence chain J — procedural arbitration and recovery are coupled

Passes 82–84 establish the combined mechanism:

```text
RECOVERY
↓
STATE / RESOURCE MUTATION
↓
CANDIDATE SET CHANGES
↓
PROCEDURAL ARBITRATION
↓
NEXT EFFECTIVE PATH
```

## Grade

E1/E2.

The constituent state changes are direct. The candidate-set formulation is AEGIS normalization.

## Requirement

Recovery must be part of scheduling, not a detached exception subsystem.

## Design consequence

The scheduler should consume recovery outcomes as state transitions that can alter subsequent candidate eligibility.

This prevents a common architecture error:

```text
planner chooses A
executor fails A
executor retries A forever
```

instead of:

```text
planner chooses A
executor attempts A
postcondition fails
recovery changes state
planner re-arbitrates
```

---

# 14. Evidence chain K — objective validity versus execution feasibility

This distinction survives all hostile review.

```text
OBJECTIVE VALIDITY
=
Does the strategic reason still exist?

EXECUTION FEASIBILITY
=
Can the selected mechanism execute now?
```

Therefore:

```text
VALID + FEASIBLE
→ execute

VALID + INFEASIBLE
→ wait / adjust / alternate

INVALID
→ release / replace / re-arbitrate
```

## Grade

E2 AEGIS generalization grounded in the historical separation between strategic state and local execution gates.

## Requirement

Temporary execution failure must not automatically destroy strategic intent.

## Design consequence

Every action failure path should report at least two independent outcomes:

```text
objective_validity
execution_feasibility
```

This is a foundational AEGIS invariant.

---

# 15. Evidence chain L — replay causality

Replay evidence has a strict evidentiary ceiling.

## Strongly supported

```text
recorded command occurred
recorded event occurred
recorded temporal ordering exists
```

## Not automatically supported

```text
hidden SN state
hidden goal state
historical rule cause
counter-selection reason
causal intent
```

## Byzantine C1-B implication

The two replay examples establish temporal corroboration that Byzantine camel production followed prior enemy knight production in the observed command stream.

They do not establish:

```text
knight observation
→
cavalry threat state
→
traincamel rule fired
→
camel command
```

without the missing state/causal evidence.

## Grade

E0 for recorded events.

E2 for temporal-correlation methodology.

Causal policy attribution remains E3.

---

# 16. Evidence chain M — parser/interpreter uncertainty

The replay interpreter currently contains parser-known-but-not-yet-supported actions.

Therefore:

```text
unsupported decoder
≠
gameplay failure
```

Likewise:

```text
no promoted W1/W2/W3 evidence
≠
transition never occurred
```

## Requirement

The forensic stack must represent three distinct conditions:

```text
OBSERVED NEGATIVE
NOT OBSERVED
UNDECODABLE / UNKNOWN
```

They are not interchangeable.

## Design consequence

Evidence objects should carry an explicit observation status rather than a Boolean success/failure flag.

---

# 17. Evidence chain N — Byzantine response archaeology

The historical Byzantine chain is strongest around mounted response:

```text
ENEMY MOUNTED PRESSURE
↓
CAVALRY THREAT AGGREGATION
↓
CAMEL RESPONSE CONDITIONS
↓
RESOURCE / FEASIBILITY GATES
↓
TRAIN CAMEL
```

## Directly grounded components

Historical source demonstrates cavalry threat aggregation, camel-related goals/conditions, resource and production gates, and camel training patterns.

## AEGIS strategic interpretation

```text
mounted threat
→
anti-mounted capability demand
```

is a sound strategic abstraction.

But a complete utility optimizer is not historically proven.

## Cataphract boundary

Cataphract is mechanically cavalry but strategically specialized toward infantry.

The statement:

```text
Cataphract = anti-infantry capability
```

is a useful AEGIS strategic model.

It does not prove that historical HD contained an explicit infantry-density utility function for Cataphract production.

## Requirement

AEGIS must model unit families by capability, not merely by mechanical class.

---

# 18. Evidence chain O — information and belief

The accumulated research repeatedly reveals partial observability:

```text
WORLD
↓
OBSERVABLE FACTS
↓
INCOMPLETE KNOWLEDGE
```

Historical threat aggregation compresses information into state, but that is not itself a probabilistic belief model.

## AEGIS requirement

The strategic layer may therefore maintain:

```text
HYPOTHESIS
CONFIDENCE
EVIDENCE AGE
EXPECTED CONSEQUENCE
INFORMATION VALUE
```

A useful analytical form is:

```text
VALUE OF INFORMATION
=
EXPECTED DECISION IMPROVEMENT
−
INFORMATION ACQUISITION COST
```

Again, this is AEGIS design, not historical HD functionality.

## Staleness

```text
OBSERVATION
+
AGE
+
LAST CONFIRMATION
=
INFORMATION QUALITY
```

This provides a clean way to prevent old threat observations from becoming permanent strategic facts.

---

# 19. Evidence chain P — version drift

Current and historical semantics must be separated.

Official AoE2DE patch history demonstrates that AI scripting semantics changed over time, including queue behavior, pending-object counting, strategic-number capacity, and other scripting behavior.

Therefore:

```text
HISTORICAL SOURCE
→ historical claim

CURRENT OFFICIAL SOURCE
→ current-build claim

CONTROLLED RUNTIME
→ current empirical claim

CROSS-VERSION EQUIVALENCE
→ separate proposition requiring evidence
```

## Requirement

Every engine-semantic claim entering Layer 3 must carry a version/build provenance tag.

## Design consequence

The architecture should not bury engine-version assumptions inside strategic logic.

A compatibility layer is preferable.

---

# 20. Evidence chain Q — current engine versus historical HD

This distinction is especially important because the project is not attempting to reproduce the historical AI verbatim.

The objective is:

```text
UNDERSTAND HISTORICAL SUBSTRATE
↓
RETAIN VALID ENGINE CONSTRAINTS
↓
BUILD SUPERIOR AEGIS STRATEGIC LAYER
```

Not:

```text
COPY HISTORICAL AI
```

Historical archaeology tells us what the execution substrate can express and what failure modes matter.

It does not dictate that AEGIS should reproduce historical policy.

---

# 21. Complete historical-to-AEGIS trace matrix

| Historical evidence | Immediate semantic | Grade | AEGIS abstraction | Layer-3 requirement |
|---|---|---|---|---|
| ordered rules can consume resources before later rules | procedural resource arbitration | E0 | procedural arbitration | explicit scheduler boundary |
| shared goals/SNs are mutated/read | shared controller state | E0/E1 | state channels | typed lifecycle state |
| state changes affect later guards | downstream eligibility changes | E1 | state-driven scheduling | immediate/deferred semantics |
| queue/pending counts include queued work | aggregate production observability | E0 | production lifecycle | multi-level verification |
| can-train differs from train | feasibility vs side effect | E0/E2 | authorization boundary | precondition + action separation |
| resource control/escrow can persist/release | reservation-like behavior | E0/E2 | commitment lifecycle | bounded retention/release |
| failed hunt changes parameters | adaptive retry | E0 | recovery policy | bounded adaptive retry |
| age state can roll back after failed transition | corrective recovery | E0 | failure recovery | rollback semantics |
| exact IDs occupy multiple namespaces | identity separation | E0 | typed identity | semantic joins only |
| replay contains commands/events | recorded temporal evidence | E0 | forensic evidence | provenance-aware observations |
| parser may not support all actions | evidence incompleteness | E0 | uncertainty state | UNKNOWN distinct from FAIL |
| Byzantine camel response patterns | capability-counter substrate | E0/E1 | capability demand | capability-based strategic model |
| no universal fairness recovered | bounded negative result | E3/negative research | fairness requirement | explicit AEGIS fairness |
| no universal argmax recovered | bounded negative result | E3/negative research | strategic valuation opportunity | explicit AEGIS valuation |
| no ownership transaction recovered | bounded negative result | E3 | transactional commitment | explicit ownership in Layer 3 |

---

# 22. Architecture contamination audit

The following are now explicitly classified as **AEGIS design**, not historical reconstruction:

```text
candidate generation
utility scoring
opportunity cost
risk scoring
tempo scoring
option value
belief confidence
information value
staleness model
explicit commitment ownership
generation tokens
bounded retry policy
bounded retention policy
universal postcondition contracts
fairness / starvation protection
capability debt
transition cost model
transition benefit model
```

This is not a weakness.

It is the correct architectural response to a historical system whose substrate provides mechanisms but not a unified modern strategic abstraction.

---

# 23. Architecture requirements recovered from archaeology

The accumulated evidence now justifies the following requirements before Layer 3 implementation.

## R1 — Separate strategy from execution

Strategic intent must not be encoded directly as raw engine commands.

## R2 — Separate objective validity from execution feasibility

A temporarily infeasible action must not automatically invalidate the strategic objective.

## R3 — Separate controller state from world state

State mutation is not world completion.

## R4 — Separate command issuance from postcondition success

An issued command is an attempt unless a postcondition confirms a stronger lifecycle state.

## R5 — Preserve evidence provenance

Every important observation must identify source, version, and confidence/grade.

## R6 — Preserve uncertainty

Unknown, unobserved, undecodable, and negative evidence must remain distinct.

## R7 — Treat procedural ordering as a real execution constraint

The scheduler must account for side-effect ordering and resource mutation.

## R8 — Give commitments explicit lifecycle semantics

Every commitment needs creation, validation, execution, progress, recovery, and release/replacement paths.

## R9 — Bound recovery

Retry and retention cannot be unbounded.

## R10 — Prevent starvation explicitly

Because the historical substrate does not provide a proven universal fairness mechanism, AEGIS must own the fairness policy if fairness is required.

## R11 — Type identity namespaces

Numerically equal IDs from different systems must not be joined without a semantic bridge.

## R12 — Version engine semantics

Engine-sensitive assumptions must be isolated and tagged by build/version.

## R13 — Validate at the correct evidence level

The validation target must specify whether it needs command, pending, object, deployment, or battlefield-effect proof.

## R14 — Re-arbitrate after recovery

Recovery may change resource and candidate state and therefore must feed back into scheduling.

## R15 — Preserve historical provenance without historical policy lock-in

The purpose of archaeology is to constrain reality, not to fossilize old strategy.

---

# 24. What is now safe to enter Layer 3

The following are sufficiently mature as **engineering requirements**:

```text
1. explicit strategic/execution boundary
2. typed state channels
3. objective-validity state
4. execution-feasibility state
5. explicit commitment lifecycle
6. explicit ownership semantics
7. bounded recovery
8. postcondition verification
9. controller/world clock separation
10. procedural arbitration awareness
11. evidence provenance
12. uncertainty preservation
13. version-sensitive engine adapter
14. capability-based production abstraction
15. starvation/fairness policy
16. re-arbitration after recovery
```

They are not all historical facts.

They are architecture requirements derived from historical evidence plus deliberate AEGIS engineering judgment.

---

# 25. What must remain outside historical claims

The following must remain labeled AEGIS until independently demonstrated:

```text
formal candidate scoring
argmax optimization
probabilistic belief
explicit utility function
transactional ownership
atomic handoff
universal fairness
universal exception manager
exact object-ID bridge
causal attribution from replay timing alone
full Byzantine composition optimizer
```

This is a hard boundary.

---

# 26. Hostile contradiction audit

## Contradiction 1

```text
rule order matters
```

versus:

```text
not every earlier rule executes
```

Resolution:

```text
first effective path
```

No contradiction.

## Contradiction 2

```text
resource-control behaves like a reservation
```

versus:

```text
resource-control is not a formal lock
```

Resolution:

Operational behavior can resemble reservation without establishing transactional semantics.

## Contradiction 3

```text
state mutation can influence later logic
```

versus:

```text
world effects are asynchronous
```

Resolution:

Two clocks.

## Contradiction 4

```text
release reopens competition
```

versus:

```text
release is not ownership transfer
```

Resolution:

Policy release is weaker than ownership transfer.

## Contradiction 5

```text
failure may cause retry
```

versus:

```text
failure does not imply retry
```

Resolution:

Recovery is conditional.

## Contradiction 6

```text
exact IDs are useful
```

versus:

```text
exact IDs are unnecessary for aggregate production
```

Resolution:

Different evidentiary requirements.

## Contradiction 7

```text
historical AI has procedural priority
```

versus:

```text
no universal numeric priority score recovered
```

Resolution:

Procedural priority does not require a global utility scalar.

No unresolved contradiction remains in the core model.

---

# 27. Negative-result discipline

Every future negative claim must carry:

```text
SOURCE SCOPE
VERSION SCOPE
SEARCH METHOD
SEARCH COMPLETENESS
```

Preferred form:

> Not recovered from the inspected corpus under the stated source/version/method scope.

Rejected form:

> Does not exist.

This is now a permanent research protocol.

---

# 28. Evidence promotion rules

A claim may move upward only when new evidence closes the required edge.

```text
E3
 ↓ direct evidence
E1/E0
```

But an AEGIS generalization does not become historical fact merely because it is useful.

Likewise:

```text
E0 constituent mechanisms
≠
E0 unified architecture
```

The project must resist composition inflation.

Three individually proven mechanisms do not automatically prove the centralized architecture that connects them.

---

# 29. Composition inflation: the central remaining epistemic hazard

This is the deepest result of Pass 87.

Suppose the historical corpus directly proves:

```text
A = threat aggregation
B = resource reservation
C = production gating
D = recovery
E = procedural ordering
```

It is tempting to conclude:

```text
A → B → C → D → E
```

as one historical controller.

That conclusion is only valid if the evidence proves the edges between the mechanisms.

Therefore every architecture graph must distinguish:

```text
PROVEN NODE
PROVEN EDGE
INFERRED EDGE
AEGIS-DESIGNED EDGE
```

This prevents architecture diagrams from becoming stronger than their evidence.

---

# 30. Edge taxonomy

Every important graph edge should be one of:

### X0 — Direct edge

Source explicitly connects A to B.

### X1 — Strong operational edge

A and B are independently evidenced and the runtime/source behavior makes their connection highly constrained.

### X2 — AEGIS design edge

AEGIS deliberately connects A to B to create a superior architecture.

### X3 — Open edge

Connection is hypothesized but not demonstrated.

This edge taxonomy should eventually be represented in the project's architecture/evidence registry.

---

# 31. The minimum defensible architecture graph

The historical substrate can safely be represented as:

```text
ENGINE FACTS
   ↓
STATE CHANNELS
   ↓
CONDITIONAL RULES
   ↓
PROCEDURAL SIDE EFFECTS
   ↓
RESOURCE / STATE MUTATION
   ↓
PENDING / WORLD OBSERVATION
   ↓
LOCAL RECOVERY
```

The AEGIS layer can then deliberately add:

```text
OBSERVATION
   ↓
BELIEF / CONFIDENCE
   ↓
OBJECTIVES
   ↓
CANDIDATES
   ↓
VALUATION
   ↓
COMMITMENT
   ↓
AUTHORIZATION
   ↓
HD EXECUTION SUBSTRATE
   ↓
POSTCONDITION
   ↓
RECOVERY / REASSESSMENT
```

The bridge between these two graphs is an explicit AEGIS design edge.

That is the correct architecture boundary.

---

# 32. Byzantine-specific implementation implication

The Byzantine bot should eventually reason in capability space rather than raw unit IDs.

Example:

```text
OBSERVED ENEMY CAPABILITY
        ↓
MOUNTED PRESSURE
        ↓
COUNTER CAPABILITY DEMAND
        ├── Camel family
        ├── Spear family
        └── positional / economic alternatives
```

Separately:

```text
INFANTRY PRESSURE
        ↓
ANTI-INFANTRY DEMAND
        ├── Cataphract
        ├── ranged alternatives
        ├── siege alternatives
        └── positional alternatives
```

And separately:

```text
NAVAL PRESSURE
        ↓
NAVAL COUNTER CAPABILITY
        ↓
CURRENT BUILD / QUEUE / TECH CONSTRAINTS
```

The historical corpus informs the substrate and known counter families.

AEGIS must decide the strategic tradeoff.

---

# 33. What Pass 87 does NOT do

This pass does not:

- implement `.per` code;
- modify PORPHYRA;
- splice the live AI;
- reopen Layer-1 scenario automation;
- claim exact object-ID closure;
- claim historical utility optimization;
- claim historical probabilistic belief;
- claim universal fairness;
- claim atomic ownership transfer;
- claim current-build equivalence for every historical primitive.

Those remain outside the pass scope.

---

# 34. Layer status after Pass 87

**Layer 1:** 89%; scenario-loader automation remains retired.  
**Layer 2:** effectively closed at the methodology/evidence-boundary level; remaining work is only targeted evidence gaps that materially change architecture.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

The word “closed” here means **sufficiently characterized for architecture construction**, not that every engine question has been solved.

---

# 35. Final closure

Pass 87 establishes the end-to-end research discipline required to move from archaeology into architecture without epistemic contamination.

The complete defensible chain is:

```text
DIRECT EVIDENCE
      ↓
OBSERVED MECHANISM
      ↓
EVIDENCE-GRADED SEMANTIC
      ↓
AEGIS GENERALIZATION
      ↓
ARCHITECTURAL REQUIREMENT
      ↓
IMPLEMENTATION DESIGN
      ↓
RUNTIME VALIDATION
```

The most important new conclusion is not another engine primitive.

It is this:

> **The evidence graph must track edges as carefully as nodes.**

A historical source can directly prove five mechanisms without proving that those mechanisms formed one centralized controller. AEGIS may connect them deliberately—but that connection must be labeled as AEGIS architecture.

This gives the project a defensible path into Layer 3.

The historical substrate has now been reduced to its strongest reusable constraints:

```text
STATEFUL
PROCEDURAL
RESOURCE-CONSTRAINED
CONDITIONALLY EXECUTED
PARTIALLY OBSERVABLE
VERSION-SENSITIVE
LOCALLY RECOVERING
```

AEGIS can now deliberately add the capabilities that the historical substrate does not demonstrably provide:

```text
EXPLICIT BELIEF
EXPLICIT OBJECTIVES
EXPLICIT CANDIDATES
EXPLICIT VALUATION
EXPLICIT COMMITMENT OWNERSHIP
BOUNDED RECOVERY
POSTCONDITION VERIFICATION
FAIRNESS
STARVATION PROTECTION
VERSION-ISOLATED EXECUTION
```

That is the clean boundary between **understanding the old system** and **engineering the new one**.

---

# Pass 87 disposition

**PASS:** COMPLETE  
**PRIMARY RESULT:** End-to-end evidence graph established.  
**HISTORICAL CLAIMS:** bounded and provenance-graded.  
**AEGIS REQUIREMENTS:** explicitly separated from historical claims.  
**CONTRADICTIONS:** resolved by semantic-layer separation.  
**NEGATIVE CLAIMS:** bounded by source/version/method scope.  
**COMPOSITION INFLATION:** identified as the principal remaining epistemic hazard.  
**LAYER-3 READINESS:** sufficient for architecture construction, subject to targeted runtime/version validation of engine-sensitive primitives.

## Recommended next target

Layer 2 should not continue indefinitely for completeness theater.

The next high-value activity is **Layer 3 architecture construction**, beginning with an explicit typed state/commitment/observation contract and an engine-adapter boundary.

Only evidence gaps that can materially invalidate that architecture should interrupt the transition.
