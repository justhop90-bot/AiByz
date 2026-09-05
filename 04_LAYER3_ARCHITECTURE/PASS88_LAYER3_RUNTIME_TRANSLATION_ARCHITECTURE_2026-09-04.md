# PASS 88 — LAYER 3 RUNTIME TRANSLATION ARCHITECTURE

**Layer:** 3 — AI architecture / runtime implementation boundary  
**Status:** Architecture specification; no production `.per` splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Predecessor:** Pass 87  
**Purpose:** Convert the Layer-2 evidence graph into a practical Layer-3 engineering contract for building an adaptive Byzantine AI without XS.

---

## Executive decision

Layer 3 is an **AI problem constrained by the verified AoE2DE runtime**.

XS is explicitly out of scope. The project will not depend on XS for state, computation, persistence, or decision making.

The central Layer-3 problem is:

> **Convert an abstract strategic need into a feasible, executable, and verifiable sequence of AoE2DE runtime primitives.**

The architecture therefore has two deliberately separated vocabularies:

```text
AEGIS COGNITIVE DOMAIN
    need
    objective
    assessment
    capability
    candidate
    plan
    commitment
    expected outcome
    verification
    recovery

                ↓ TRANSLATION BOUNDARY ↓

AOE2DE RUNTIME DOMAIN
    fact
    goal
    strategic number
    flag
    timer
    search
    feasibility predicate
    command
    queue / pending state
    world observation
```

The first domain answers **what the AI wants to accomplish**.
The second answers **what the engine can actually observe and do**.

Neither domain is permitted to silently impersonate the other.

---

# 1. Architecture objective

The target is not a larger rule collection.

The target is a closed-loop player model:

```text
OBSERVE
  ↓
ASSESS
  ↓
IDENTIFY STRATEGIC NEED
  ↓
DEFINE OBJECTIVE
  ↓
DEFINE REQUIRED CAPABILITY
  ↓
GENERATE CANDIDATES
  ↓
APPLY HARD RUNTIME CONSTRAINTS
  ↓
EVALUATE FEASIBLE CANDIDATES
  ↓
COMMIT
  ↓
TRANSLATE TO RUNTIME PRIMITIVES
  ↓
EXECUTE
  ↓
OBSERVE RESULT
  ↓
VERIFY POSTCONDITION
  ↓
UPDATE STATE / BELIEF
  ↓
RECOVER OR RE-ARBITRATE
  ↺
```

The loop is the product.
Individual rules are implementation details.

---

# 2. Non-negotiable Layer-3 constraints

## 2.1 No XS dependency

Layer 3 must remain viable without XS.

Any computation required by the AI must be implementable using the project's accepted `.per` runtime mechanisms and the architecture's state decomposition.

XS research may exist historically as background knowledge, but no AEGIS subsystem may require it.

## 2.2 No unverified engine semantics

An AEGIS design concept does not become an engine capability merely because a command or fact has a plausible name.

Every runtime primitive requires evidence and validation status.

## 2.3 No abstraction without a realization path

Every major AEGIS capability must answer:

```text
What does it mean?
How is it represented?
How is it translated?
What runtime primitive executes it?
How is success observed?
How is failure observed?
```

If those questions cannot be answered, the capability remains architectural/open rather than implemented.

## 2.4 No command-success inflation

```text
issued ≠ accepted ≠ pending ≠ completed ≠ available ≠ deployed ≠ effective
```

## 2.5 No strategic-state inflation

```text
observed ≠ known
unknown ≠ false
correlation ≠ causation
historical mechanism ≠ AEGIS design
```

## 2.6 Controller and world clocks remain separate

Controller state changes may affect later script evaluation without proving that the game world has already realized the corresponding effect.

---

# 3. The AEGIS cognitive object model

Layer 3 will use the following conceptual objects.

## 3.1 Observation

A normalized observation from an engine fact, search, event, or other accepted source.

Minimum metadata:

```text
value
source
observation_time
freshness
provenance
confidence
```

An observation describes evidence, not strategic meaning.

## 3.2 Belief

A reasoned interpretation of observations.

Example:

```text
Observed:
    6 mounted units

Belief:
    enemy mounted pressure is increasing

Confidence:
    medium

Freshness:
    recent
```

Beliefs may be wrong. They therefore retain confidence and provenance.

## 3.3 Assessment

A strategic interpretation of the current situation.

Example:

```text
Economic exposure: HIGH
Mounted threat: MEDIUM/HIGH
Response deadline: SHORT
Current anti-mounted capability: INSUFFICIENT
```

## 3.4 Objective

A desired change in the strategic state.

Example:

```text
PROTECT_GOLD
```

An objective must specify:

```text
validity condition
urgency
deadline when relevant
success condition
failure consequence
```

## 3.5 Capability requirement

The capability needed to satisfy an objective.

Example:

```text
ANTI_MOUNTED_CAPABILITY = 8
```

This is deliberately not a unit name.

## 3.6 Candidate

A possible implementation of a required capability.

Example:

```text
CAMEL
SPEAR
STATIC_DEFENSE
REPOSITION
COUNTER_ATTACK
MIXED_COMPOSITION
```

Candidates are evaluated only after hard constraints are applied.

## 3.7 Commitment

A selected candidate becomes a commitment only when the AI accepts its resource, timing, dependency, and reversal consequences.

Minimum conceptual fields:

```text
objective
capability
selected_candidate
owner
creation_generation
resource_obligation
dependencies
deadline
interruptibility
attempt_count
last_action
last_evidence
next_review
success_condition
release_condition
replacement_policy
```

## 3.8 Execution state

Tracks the runtime realization of the commitment.

```text
eligible
authorized
issued
pending
completed
available
deployed
verified_effective
```

These are states, not synonyms.

---

# 4. Capability-first design

The strategic layer should ask for capabilities, not units.

Bad:

```text
Enemy cavalry → Camel
```

Correct:

```text
Enemy mounted pressure
→
required anti-mounted capability
→
candidate set
→
choose executable implementation
```

This distinction matters because the same strategic problem can have several valid solutions.

It also allows civilization-specific implementation without contaminating the strategic ontology.

For Byzantines, a mounted-pressure problem might eventually map to some combination of:

```text
camel
spearman
static defense
army repositioning
supporting composition
counter-attack
resource denial
```

The architecture does not assume that all candidates are simultaneously valid. Feasibility and evaluation determine that.

---

# 5. Capability deficit model

The first practical bridge between strategic reasoning and production is a deficit model.

```text
REQUIRED CAPABILITY
−
CURRENT CAPABILITY
=
CAPABILITY DEFICIT
```

If the result is positive:

```text
deficit > 0 → investment may be required
```

If zero:

```text
deficit = 0 → capability is currently sufficient
```

If negative:

```text
deficit < 0 → surplus exists; resources may be redirected
```

The quantity is an AEGIS planning construct. It is not a claim about historical HD's internal arithmetic.

The implementation must define how each capability is measured from actual runtime-observable quantities.

---

# 6. Runtime translation contract

Every AEGIS action must pass through a translation contract.

```text
ABSTRACT OPERATION
      ↓
RUNTIME PLAN
      ↓
PRIMITIVE SEQUENCE
      ↓
ENGINE EXECUTION
      ↓
OBSERVABLE POSTCONDITION
```

For example:

```text
ABSTRACT:
    CREATE_ANTI_MOUNTED_CAPABILITY

RUNTIME PLAN:
    produce Byzantine camel capability

PRIMITIVES:
    identify eligible producer
    establish resource feasibility
    verify can-train
    issue train
    observe queue/pending
    observe completed capability

POSTCONDITIONS:
    production request realized
    resulting capability exists
```

The abstract operation is not considered runtime-complete until the postcondition is defined.

---

# 7. Runtime Primitive Registry

Layer 3 requires a permanent registry for every primitive that becomes an architectural dependency.

Minimum schema:

```text
primitive_id
name
purpose
inputs
preconditions
runtime_mapping
expected_controller_transition
expected_world_transition
success_observation
failure_observation
recovery_policy
build_scope
evidence_grade
validation_status
known_limits
```

Recommended validation states:

```text
DOCUMENTED
ARCHAEOLOGICALLY_SUPPORTED
IMPLEMENTED
RUNTIME_VALIDATED
REPLAY_CORROBORATED
BATTLEFIELD_VALIDATED
```

A primitive should never be labeled stronger than its evidence.

---

# 8. Primitive categories

The registry should eventually cover at least these families.

## Observation primitives

```text
READ_UNIT_COUNT
READ_QUEUE_STATE
READ_RESOURCE_STATE
READ_RESEARCH_STATE
READ_AGE_STATE
READ_TARGET_STATE
READ_THREAT_STATE
SEARCH_OBJECTS
SEARCH_PRODUCERS
```

The exact list remains subject to runtime validation.

## State primitives

```text
SET_GOAL
MODIFY_GOAL
SET_SN
SET_FLAG
ENABLE_TIMER
DISABLE_TIMER
RESET_STATE
```

## Feasibility primitives

```text
CAN_TRAIN
CAN_BUILD
CAN_RESEARCH
RESOURCE_AVAILABLE
PRODUCER_AVAILABLE
QUEUE_AVAILABLE
```

## Side-effect primitives

```text
TRAIN
BUILD
RESEARCH
MOVE / CONTROL
ATTACK / TASK
```

Exact syntax and semantics are build-sensitive and must come from the verified runtime registry.

## Verification primitives

These are not necessarily engine commands. They are normalized observation procedures:

```text
QUEUE_TRANSITION_OBSERVED
PENDING_TRANSITION_OBSERVED
CAPABILITY_COUNT_CHANGED
OBJECT_AVAILABLE
POSITIONAL_STATE_CHANGED
TARGET_STATE_CHANGED
OBJECTIVE_STATE_CHANGED
```

---

# 9. Hard feasibility comes before soft evaluation

A candidate that cannot execute should not win a strategic scoring contest.

The pipeline is:

```text
CANDIDATES
   ↓
HARD CONSTRAINT FILTER
   ↓
FEASIBLE CANDIDATES
   ↓
SOFT EVALUATION
   ↓
SELECTION
```

Hard constraints may include:

```text
technology availability
producer availability
resource availability
population capacity
queue capacity
required infrastructure
runtime support
execution deadline
```

This avoids the common failure where the AI selects a theoretically excellent but practically impossible response.

---

# 10. Timing is part of feasibility

AoE2 decisions are time-constrained.

A response is not useful merely because it is eventually executable.

For a candidate:

```text
DECISION LATENCY
+
AUTHORIZATION LATENCY
+
QUEUE LATENCY
+
TRAINING / BUILD LATENCY
+
DEPLOYMENT LATENCY
=
CAPABILITY LATENCY
```

Compare that against the strategic deadline.

```text
capability_effect_time <= objective_deadline
```

is a candidate feasibility criterion when a deadline exists.

If the preferred counter cannot become effective in time, the planner must consider an emergency bridge rather than blindly selecting the preferred long-term solution.

---

# 11. Minimum sufficient capability

AEGIS should not automatically maximize every response.

It should estimate:

```text
required capability
current capability
capability deficit
```

and attempt to close the deficit with the smallest strategically adequate commitment, subject to risk and uncertainty.

This creates a practical production principle:

```text
DEFICIT → INVEST
SUFFICIENT → MAINTAIN
SURPLUS → REDIRECT
```

The quantity required is not necessarily exact. It may be represented as a bounded estimate when the engine cannot provide perfect information.

---

# 12. Uncertainty-aware planning

Belief uncertainty must affect commitment behavior.

Example:

```text
Enemy cavalry estimate: 4–12
Confidence: LOW
```

A rational response may be:

```text
small hedge
+
information acquisition
+
preserved optionality
```

rather than:

```text
maximum camel commitment
```

Behavioral rule:

```text
HIGH CONFIDENCE
→ stronger commitment permitted

MEDIUM CONFIDENCE
→ hedge / bounded commitment

LOW CONFIDENCE
→ preserve optionality / gather information
```

This is an AEGIS design rule, not a historical HD feature claim.

---

# 13. Information can be a candidate action

The candidate set should not consist solely of production and military actions.

Possible candidates include:

```text
ACT
SCOUT
WAIT
DEFEND
REPOSITION
TRANSITION
DENY
```

The strategic system can compare action against information acquisition.

Conceptual value-of-information model:

```text
VOI
=
expected future decision improvement
−
information acquisition cost
```

This should initially be qualitative/bounded rather than pretending to possess precise probabilities.

---

# 14. Resource arbitration

The global planner must recognize competing commitments.

Example:

```text
CAMEL COMMITMENT
TECH COMMITMENT
TC COMMITMENT
SIEGE COMMITMENT
```

Each has:

```text
resource obligation
expected benefit
deadline
reversal cost
opportunity cost
```

The architecture must prevent local controllers from collectively committing more than the civilization can sustain.

This is an AEGIS requirement, not a claim that historical HD had a universal commitment ledger.

---

# 15. Commitment debt

AEGIS introduces the following analytical construct:

> **Commitment debt** = the future resource, infrastructure, production, and strategic obligations created by current commitments.

Examples:

```text
Castle commitment
→ stone + villager + follow-on expectations

Cataphract commitment
→ gold + stable + upgrades + research

Heavy military transition
→ sustained resource allocation + opportunity cost
```

The planner should consider:

```text
CURRENT STATE
+
ACTIVE COMMITMENTS
+
FUTURE OBLIGATIONS
```

before creating another commitment.

---

# 16. Optionality

A candidate should be evaluated partly by what future options it preserves.

Example:

```text
PLAN A
heavy single-purpose investment
→ high immediate capability
→ low future flexibility

PLAN B
mixed / reversible investment
→ lower immediate specialization
→ more future options
```

Optionality is therefore an evaluation dimension, not a decorative concept.

It should initially be represented through explicit qualitative/bounded features:

```text
reversible
partially reversible
high lock-in
multi-purpose
single-purpose
```

Do not invent a precise optionality score until there is a validated reason to do so.

---

# 17. Commitment lifecycle

AEGIS commitment state should follow:

```text
FREE
 ↓
PROPOSED
 ↓
AUTHORIZED
 ↓
EXECUTING
 ↓
PROGRESSING
 ↓
VERIFIED
 ↓
MAINTAIN / REDUCE
 ↓
RELEASE / REPLACE
 ↓
FREE / NEW COMMITMENT
```

Failure can branch at multiple stages:

```text
FAILURE
 ↓
CLASSIFY
 ↓
LOCAL RECOVERY
 ↓
REASSESS
 ↓
RETRY / MODIFY / REPLACE / RELEASE
```

A commitment must never be allowed to persist indefinitely without review.

---

# 18. Interruptibility

Every significant commitment should eventually declare:

```text
NON_INTERRUPTIBLE
CONDITIONALLY_INTERRUPTIBLE
INTERRUPTIBLE
```

This prevents strategic inertia.

Emergency defense may interrupt an economic plan.
A queued production action may be less interruptible.
A long-term transition may be conditionally interruptible.

Exact behavior is implementation policy, not historical reconstruction.

---

# 19. Verification ladder

AEGIS should use a layered success model:

```text
V0 — intention exists
V1 — action authorized
V2 — command issued
V3 — pending / queue transition observed
V4 — capability / object created
V5 — capability available
V6 — capability deployed
V7 — battlefield interaction observed
V8 — objective-level effect observed
```

Not every primitive can reach every level.

The primitive registry must declare the highest verification level actually supported.

This prevents a production command from being mistaken for strategic success.

---

# 20. Recovery architecture

Recovery is not a separate exception universe.

It feeds back into arbitration.

```text
PLAN A
 ↓
EXECUTION
 ↓
POSTCONDITION FAILURE
 ↓
FAILURE CLASSIFICATION
 ↓
STATE CHANGE
 ↓
CANDIDATE SET CHANGES
 ↓
RE-ARBITRATION
```

Possible recovery dispositions:

```text
RETRY
MODIFY
ALTERNATE PRODUCER
ALTERNATE CANDIDATE
WAIT
RELEASE
ABANDON
ESCALATE
```

The correct disposition depends on failure type and remaining objective validity.

---

# 21. First vertical slice — Cavalry Threat Containment

This is the first architecture proof.

## Input

Observed enemy mounted pressure.

## Required chain

```text
OBSERVE
→
CLASSIFY
→
BELIEF
→
ASSESS
→
OBJECTIVE
→
REQUIRED ANTI-MOUNTED CAPABILITY
→
CURRENT CAPABILITY
→
DEFICIT
→
CANDIDATES
→
HARD FEASIBILITY
→
EVALUATION
→
COMMITMENT
→
RUNTIME TRANSLATION
→
EXECUTION
→
QUEUE / PENDING
→
CAPABILITY CREATED
→
DEPLOYMENT
→
EFFECT OBSERVATION
→
REASSESSMENT
```

## Required branch test

The slice must also handle:

```text
enemy cavalry
→
AEGIS commits to a response
→
enemy composition changes
→
original objective/candidate assumptions change
→
AEGIS preserves useful sunk capability
→
releases or reduces obsolete commitments
→
creates new candidate set
→
re-arbitrates
```

This is the minimum demonstration that the system is adaptive rather than merely reactive.

---

# 22. Implementation order

The first Layer-3 coding sequence is now fixed:

### L3-P1 — Cognitive + Runtime Contract

Deliver:

```text
state schema
observation schema
belief schema
objective schema
capability schema
candidate schema
commitment schema
execution schema
verification schema
failure schema
```

### L3-P2 — Runtime Primitive Registry

For each primitive:

```text
exact syntax
preconditions
expected transition
verification path
failure path
build scope
```

### L3-P3 — State/Rule Encoding

Compile the first architectural objects into accepted `.per` mechanisms.

### L3-P4 — Feasibility Engine

Implement:

```text
producer
resource
queue
technology
population
latency
```

constraints.

### L3-P5 — Capability Deficit Controller

First production controller should close a measured capability deficit rather than use fixed arbitrary unit counts.

### L3-P6 — Cavalry Threat Vertical Slice

Complete the full closed loop.

### L3-P7 — Adversarial Transition Tests

Test:

```text
cavalry → archers
cavalry → infantry
cavalry → siege support
threat disappears
producer becomes unavailable
resources disappear
queue becomes constrained
```

### L3-P8 — Global Arbitration

Only after the first controller works should competing objectives be allowed to contend for resources.

---

# 23. What counts as “implemented”

A Layer-3 feature is not complete when code exists.

It is complete only when:

```text
ABSTRACTION DEFINED
        ↓
RUNTIME MAPPING DEFINED
        ↓
CODE WRITTEN
        ↓
VALIDATOR ACCEPTS
        ↓
ENGINE EXECUTION OBSERVED
        ↓
POSTCONDITION VERIFIED
        ↓
FAILURE PATH TESTED
```

Where a step is impossible to validate, the feature remains explicitly open.

---

# 24. What we are deliberately not claiming

This architecture does not claim that historical HD had:

```text
formal objective objects
formal candidate scoring
formal ownership
universal fairness
universal exception handling
probabilistic belief
value-of-information optimization
commitment debt
optionality scoring
centralized global arbitration
```

Those are AEGIS design constructs motivated by problems exposed through archaeology.

The historical record instead provides validated mechanisms and constraints from which AEGIS can deliberately design a better system.

---

# 25. Layer-3 success criterion

The ultimate proof is not code volume.

The proof is whether the bot can repeatedly demonstrate this property:

> **Given a strategically meaningful need, AEGIS identifies a useful objective, derives a required capability, selects an executable plan, translates it into verified AoE2DE primitives, observes the actual result, and changes the plan when reality invalidates its assumptions.**

That is the minimum definition of an adaptive expert-player architecture.

The long-term objective is to make that loop operate across economy, military, technology, map control, defense, offense, transitions, and Byzantine-specific composition management—without abandoning runtime verifiability.
