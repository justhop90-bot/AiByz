# PASS 89 — TYPED AEGIS STATE / `.PER` REALIZATION ARCHITECTURE

**Layer:** 3 — AI architecture / runtime implementation boundary  
**Status:** Architecture specification; no production `.per` splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Predecessor:** Pass 88  
**Primary objective:** Define how the conceptual AEGIS state model is represented by the finite, integer-oriented `.per` runtime without XS, while preserving type boundaries, provenance, lifecycle, generation, ownership, uncertainty, timing, and verification semantics.  
**Evidence posture:** This document deliberately distinguishes engine-supported facts, historical archaeology, AEGIS architecture, and implementation hypotheses.

---

## Executive decision

Pass 88 established the central Layer-3 problem as a translation problem:

```text
ABSTRACT STRATEGIC NEED
        ↓
CAPABILITY
        ↓
FEASIBLE PLAN
        ↓
VERIFIED AOE2DE RUNTIME PRIMITIVES
        ↓
EXECUTION
        ↓
POSTCONDITION
        ↓
REASSESSMENT
```

Pass 89 answers the next engineering question:

> **If AEGIS has typed objects such as Observation, Belief, Objective, Capability, Candidate, Commitment, and Execution State, how can those concepts actually exist inside `.per` without pretending that `.per` has native objects, structs, dictionaries, or an XS-like memory model?**

The answer is a **typed-state convention implemented over primitive state channels**.

AEGIS will not attempt to manufacture native objects that the scripting language does not possess. Instead, it will define a deterministic schema in which goals, strategic numbers, flags, timers, searches, and engine-managed state are treated as storage classes with explicit ownership and type contracts.

The resulting design is:

```text
                    AEGIS CONCEPTUAL STATE
                              │
                 typed schema / lifecycle contract
                              │
                              ▼
                    RUNTIME STATE ABI
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       GOALS                FLAGS                SNs
 persistent integers     booleans/control    bounded numeric controls
          │                   │                   │
          └──────────────┬────┴───────────────────┘
                         ▼
                     TIMERS / SEARCHES
                  temporal / selection state
                         │
                         ▼
                  ENGINE-MANAGED STATE
             queues, objects, research, age, etc.
                         │
                         ▼
                 COMMAND / OBSERVATION
                         │
                         ▼
                    STATE TRANSITION
```

This is an **AEGIS architecture**, not a claim that the historical HD AI contained this exact type system.

The central implementation rule is:

> **A conceptual field is not implemented until its storage class, encoding, writer, reader, reset policy, validity domain, and verification path are specified.**

---

# 1. Design principles

## 1.1 `.per` is the execution substrate, not the ontology

The architecture must never confuse the storage mechanism with the semantic object.

For example:

```text
goal 4200
```

is an integer channel.

It is not intrinsically an `Objective`.

It becomes an objective field only because the AEGIS schema assigns that channel a meaning, range, writer policy, reader policy, and lifecycle.

Likewise:

```text
flag X
```

is a Boolean engine state channel.

It is not intrinsically `COMMITMENT_AUTHORIZED`.

A flag may be assigned that semantic role by AEGIS, provided the allocation is explicit and the state transition is validated.

This gives the architecture a clean separation:

```text
ENGINE PRIMITIVE
    ↓
STORAGE CHANNEL
    ↓
AEGIS FIELD
    ↓
AEGIS OBJECT
```

The reverse direction is equally important:

```text
AEGIS OBJECT
    ↓
FIELDS
    ↓
RUNTIME CHANNELS
    ↓
`.per` EXPRESSIONS
```

## 1.2 No hidden fields

Every persistent AEGIS field must have a registry entry.

Minimum registry metadata:

```text
field_id
conceptual_type
storage_class
runtime_identifier
encoding
valid_range
sentinel_values
writer_rules
reader_rules
reset_policy
generation_policy
owner
conflict_policy
verification_source
evidence_grade
validation_status
```

A field that exists only because a programmer happens to remember that `goal 4017` means something is unacceptable.

## 1.3 No overloaded channels without a generation contract

Reusing a goal or SN for different meanings is dangerous because stale state can survive the conceptual lifetime of the previous owner.

If channel reuse is ever necessary, it requires:

```text
old value invalidated
→ generation incremented
→ field rewritten
→ validity asserted
→ readers require matching generation
```

This is the runtime analogue of stale-pointer protection.

## 1.4 No false type safety

`.per` does not give AEGIS a native type checker for our conceptual schema.

Therefore type safety must be enforced through architecture:

```text
FIELD ID
+ STORAGE CLASS
+ ENCODING
+ RANGE
+ WRITER CONTRACT
+ READER CONTRACT
```

A validator or static-analysis tool should eventually enforce these contracts.

## 1.5 Conservative compatibility first

Official AoE2DE scripting history establishes that strategic numbers were extended to a maximum of 511 in Update 42848. Official Update Preview 125283 later increased available goals from 512 to 16000. citeturn0search4turn0search0

The architecture must not make the entire AI dependent on the larger goal namespace merely because a newer build supports it.

Therefore AEGIS defines two profiles:

```text
L3-COMPAT
    conservative common denominator

L3-DE-CURRENT
    expanded current-build capability, only after local validation
```

The current repository architecture is written against **L3-COMPAT semantics unless a primitive is explicitly marked build-validated**.

This is especially important because the project has already encountered validator/runtime tension around high-numbered scratch goals and unit-line identifiers.

---

# 2. The runtime state ABI

AEGIS needs an internal equivalent of an application binary interface: a stable agreement about where and how state lives.

Call this the **Runtime State ABI**.

It is not an operating-system ABI. It is an AEGIS convention governing `.per` channels.

The ABI has six layers:

```text
S0 — ENGINE STATE
S1 — OBSERVATION STATE
S2 — COGNITIVE STATE
S3 — COMMITMENT / EXECUTION STATE
S4 — CONTROL / ARBITRATION STATE
S5 — TEMPORAL / GENERATION STATE
```

## S0 — Engine state

Read-only from the AEGIS cognitive perspective unless a command changes the world.

Examples:

```text
unit counts
queue state
research state
age
resources
producer existence
object search results
pending objects
position / target facts
```

This state belongs to the engine. AEGIS does not duplicate it unless a derived value is required.

## S1 — Observation state

Normalized snapshots extracted from S0.

Examples:

```text
enemy mounted pressure estimate
own camel capability
available producer count
current food reserve
research pending state
```

The observation layer is where raw engine facts become stable AEGIS evidence.

## S2 — Cognitive state

Strategic interpretation:

```text
belief
assessment
objective validity
required capability
candidate eligibility
confidence
urgency
```

## S3 — Commitment / execution state

Tracks what the AI has actually decided and what stage of realization has been reached:

```text
selected candidate
commitment generation
resource obligation
execution stage
attempt count
last action
postcondition status
```

## S4 — Control / arbitration state

Global coordination:

```text
controller ownership
resource reservation
fairness / starvation protection
priority bands
re-arbitration request
exception state
```

These are AEGIS constructs. Historical archaeology established procedural arbitration and shared state, but not a universal historical commitment ledger or formal scheduler.

## S5 — Temporal / generation state

Controls freshness and identity:

```text
controller epoch
objective generation
commitment generation
observation age
retry cooldown
review timer
```

---

# 3. Storage-class policy

The architecture assigns each conceptual state family a preferred runtime storage class.

| Conceptual data | Preferred storage | Reason |
|---|---|---|
| Persistent bounded scalar | Goal | Larger integer state channel; suitable for state IDs, generations, counters |
| Boolean mode / latch | Flag | Natural Boolean semantics |
| Bounded control scalar | SN | Engine already treats SNs as control parameters; useful where engine commands consume them |
| Deadline / cooldown | Timer | Native temporal primitive |
| Selected object / point | Search state / target state | Engine-native selection semantics |
| Current engine facts | Fact/query | Avoid unnecessary duplication |
| Queue / pending state | Engine observation | Engine owns actual pending lifecycle |
| Capability count | Derived goal or direct fact | Cache only when repeated evaluation justifies it |
| Confidence / bucket | Goal | Avoid floating point; use enumerated levels |
| Type tag | Goal | Integer tag gives conceptual type identity |
| Generation | Goal | Persistent identity/version channel |
| Last action code | Goal | Explicit execution trace state |
| Attempt count | Goal | Bounded retry state |
| Review/cooldown | Timer + optional generation goal | Timer for time, goal for association |

This table is a design preference, not a claim that every field must use the preferred class.

---

# 4. Goals are the primary AEGIS memory plane

Goals are the preferred state plane for AEGIS because they provide persistent integer storage suitable for explicit state machines.

The official scripting expansion to 16000 goals gives substantial namespace headroom on supported builds, while older scripting limits make compatibility an explicit engineering concern. citeturn0search0

The project therefore uses **logical namespaces**, not an assumption that every build supports the same absolute range.

## 4.1 Logical goal namespaces

Recommended namespace map:

```text
G0–G63       bootstrap / ABI / health
G64–G127     observation summaries
G128–G191    belief / confidence
G192–G255    assessment
G256–G319    objectives
G320–G383    capability requirements
G384–G447    candidate state
G448–G511    commitment / execution core
```

This is the **L3-COMPAT core**.

The exact numeric assignment is not yet a production allocation and must be reconciled against the project's existing goal definitions before implementation.

It is deliberately conservative because historical/legacy environments have materially smaller goal namespaces.

## 4.2 Expanded state plane

On a validated current build, additional goals may be allocated above 511:

```text
G512+       extended AEGIS state
```

However, high goal IDs must not be assumed to be legal in every predicate or validator context merely because the engine supports a larger goal namespace globally.

The project's prior `temporary-goal 3500` issue demonstrates why **global availability and contextual operand validity must be tested separately**.

## 4.3 Goal naming convention

Logical names should be descriptive and stable:

```text
AEGIS-G-OBJ-ID
AEGIS-G-OBJ-GEN
AEGIS-G-OBJ-VALID
AEGIS-G-OBJ-URGENCY
AEGIS-G-CAP-REQ
AEGIS-G-CAP-HAVE
AEGIS-G-CAP-DEFICIT
AEGIS-G-CAND-ID
AEGIS-G-COMMIT-ID
AEGIS-G-COMMIT-GEN
AEGIS-G-COMMIT-STAGE
AEGIS-G-COMMIT-OWNER
AEGIS-G-COMMIT-ATTEMPTS
AEGIS-G-COMMIT-LAST-ACTION
AEGIS-G-COMMIT-LAST-EVIDENCE
```

The actual `.per` names should use the project's established naming style once the runtime allocation file is constructed.

---

# 5. Flags are control-plane state, not general memory

Flags should remain Boolean whenever possible.

Good uses:

```text
AEGIS-F-OBJECTIVE-ACTIVE
AEGIS-F-OBJECTIVE-URGENT
AEGIS-F-COMMIT-AUTHORIZED
AEGIS-F-COMMIT-INTERRUPTIBLE
AEGIS-F-RECOVERY-REQUESTED
AEGIS-F-REVIEW-DUE
AEGIS-F-ARBITRATION-DIRTY
```

Bad uses:

```text
flag means candidate 4
flag means confidence 3
flag means generation 17
```

Those values belong in goals.

The rule is:

> **If a value has more than two semantic states, it is not a flag.**

A flag may mirror a goal-derived condition for efficient guards, but the authoritative source must be identified.

Example:

```text
authoritative:
    AEGIS-G-COMMIT-STAGE = AUTHORIZED

derived guard:
    AEGIS-F-COMMIT-AUTHORIZED = true
```

If both exist, the architecture must specify which one wins after reset or partial update.

---

# 6. Strategic numbers are control parameters, not arbitrary storage

Strategic numbers have a fundamentally different role from goals.

Official Update 42848 extended the maximum strategic-number range from 303 to 511. citeturn0search4

AEGIS should therefore avoid treating SNs as a second unrestricted database.

Preferred SN roles:

```text
engine-facing control values
production thresholds
behavioral parameters
bounded tactical controls
```

Examples of acceptable conceptual roles:

```text
AEGIS-SN-CAMEL-THRESHOLD
AEGIS-SN-EMERGENCY-DEFENSE
AEGIS-SN-SCOUTING-INTENSITY
AEGIS-SN-PRODUCTION-PRESSURE
```

Examples of poor roles:

```text
SN stores arbitrary object generation
SN stores a multi-field commitment record
SN stores provenance IDs
```

The reason is architectural, not merely stylistic: SNs are also consumed by engine behavior. Accidentally using a control channel as general memory can create hidden side effects.

Therefore:

> **Goals are the memory plane. SNs are the control plane.**

This distinction should become a static lint rule.

---

# 7. Typed state without native structs

The central technique is **field grouping by schema**.

A conceptual `Commitment` becomes a fixed set of channels:

```text
COMMITMENT
├── type tag
├── ID
├── generation
├── owner
├── objective ID
├── capability ID
├── candidate ID
├── lifecycle stage
├── resource obligation
├── deadline class
├── interruptibility
├── attempt count
├── last action
├── last evidence
└── review state
```

The runtime does not contain a `Commitment` object.

Instead:

```text
G-COMMIT-ID
G-COMMIT-GEN
G-COMMIT-OWNER
G-COMMIT-OBJ
G-COMMIT-CAP
G-COMMIT-CAND
G-COMMIT-STAGE
G-COMMIT-OBLIGATION
G-COMMIT-DEADLINE
G-COMMIT-INTERRUPT
G-COMMIT-ATTEMPTS
G-COMMIT-LAST-ACTION
G-COMMIT-LAST-EVIDENCE
```

Together, under the schema contract, they constitute one logical record.

This is analogous to a relational tuple or packed record implemented manually over scalar channels.

## 7.1 Atomicity warning

These fields are **not automatically atomic**.

Writing:

```text
G-COMMIT-ID
G-COMMIT-GEN
G-COMMIT-STAGE
```

in separate actions does not prove that every rule sees the conceptual record as one indivisible transaction.

Therefore AEGIS needs an explicit record-validity protocol.

---

# 8. Record-validity protocol

Every multi-field logical object should use a small state protocol.

Recommended lifecycle:

```text
INVALID
   ↓
ALLOCATING
   ↓
POPULATING
   ↓
VALID
   ↓
UPDATING
   ↓
VALID
   ↓
RELEASING
   ↓
INVALID
```

A simpler implementation may use generation and a validity flag:

```text
VALID = 0
→ write fields
→ increment/set generation
→ VALID = 1
```

Readers must first check validity.

If a field group has no valid record marker, consumers must treat it as absent rather than partially meaningful.

This is an AEGIS implementation requirement, not historical engine behavior.

---

# 9. Generation numbers are mandatory for reusable logical records

Generation is the most important protection against stale state.

Suppose commitment slot 1 previously represented:

```text
OBJ_PROTECT_GOLD
CAND_CAMEL
GEN 12
```

The commitment is released.

Later the same slot represents:

```text
OBJ_PROTECT_WOOD
CAND_SPEAR
GEN 13
```

A delayed rule that still thinks it owns generation 12 must not mutate generation 13.

Conceptually:

```text
writer_generation = 13

consumer expects = 12

12 != 13
→ stale writer rejected
```

`.per` cannot necessarily perform arbitrary transactional compare-and-swap semantics, so the implementation must approximate this through guarded rules and generation checks.

The architecture should prefer **single-writer discipline** wherever possible.

---

# 10. Single-writer discipline

Each authoritative field should have one designated subsystem responsible for mutation.

Example:

```text
G-COMMIT-STAGE
    owner: Commitment Controller

G-CAP-HAVE-CAMEL
    owner: Capability Observer

G-OBJ-VALID
    owner: Objective Controller

G-ARBITRATION-DIRTY
    owner: Global Arbiter
```

Other modules may read the fields.

They should not write them casually.

This is especially important because historical archaeology established shared mutable state and distributed controllers, but did not prove formal ownership transfer. AEGIS therefore introduces ownership explicitly as a design discipline rather than attributing it to HD.

---

# 11. Ownership semantics

Every logical record has:

```text
owner_id
owner_generation
```

Ownership means:

> **The subsystem currently authorized by the AEGIS architecture to mutate the authoritative record.**

It does not mean:

```text
engine object ownership
player ownership
unit ownership
historical AI lock
```

These are separate concepts.

A commitment may therefore have:

```text
owner = PRODUCTION_CONTROLLER
```

while the produced unit belongs to the player's normal game-side ownership.

Ownership transfer must be explicit:

```text
old owner releases
→ generation changes
→ new owner claims
→ new owner validates generation
```

No implicit transfer is permitted.

---

# 12. Objective representation

An `Objective` is represented by a compact record.

Conceptual schema:

```text
OBJ.ID
OBJ.GEN
OBJ.TYPE
OBJ.VALID
OBJ.URGENCY
OBJ.DEADLINE_CLASS
OBJ.SUCCESS_CLASS
OBJ.FAILURE_CLASS
OBJ.CONFIDENCE
OBJ.REVIEW_STATE
```

## 12.1 Objective type

Use an enumerated integer, not text:

```text
0 = NONE
1 = SURVIVE
2 = PROTECT
3 = GAIN_CAPABILITY
4 = DENY
5 = ATTACK
6 = TRANSITION
7 = INFORMATION
8 = RECOVER
```

The exact taxonomy is subject to later implementation refinement.

## 12.2 Objective validity

Validity is separate from urgency.

```text
VALID = 1
URGENT = 1
```

means an urgent valid objective.

If the underlying strategic condition disappears:

```text
VALID = 0
```

The commitment controller must not infer that execution is automatically invalid. That requires a separate feasibility evaluation.

This preserves the Pass 84 distinction:

```text
OBJECTIVE VALIDITY ≠ EXECUTION FEASIBILITY
```

---

# 13. Capability representation

A capability is a normalized strategic quantity derived from observable state.

Conceptual schema:

```text
CAP.ID
CAP.GEN
CAP.TYPE
CAP.REQUIRED
CAP.CURRENT
CAP.DEFICIT
CAP.CONFIDENCE
CAP.FRESHNESS
```

The central equation remains:

```text
DEFICIT = REQUIRED − CURRENT
```

but implementation must define the measurement function.

For cavalry containment, for example:

```text
required anti-mounted capability
current anti-mounted capability
```

should not be assumed to equal raw camel count. A future capability model may weight units by tactical suitability, technology state, readiness, or deployment.

The first vertical slice should remain simpler than the eventual model.

---

# 14. Candidate representation

Candidate records should be compact because many candidates may be evaluated repeatedly.

```text
CAND.ID
CAND.GEN
CAND.TYPE
CAND.ELIGIBLE
CAND.FEASIBLE
CAND.REJECT_CODE
CAND.EVAL_CLASS
CAND.LOCKIN_CLASS
CAND.INTERRUPT_CLASS
```

The crucial rule is ordering:

```text
candidate generated
→ hard constraints
→ feasibility
→ soft evaluation
→ selection
```

A candidate that fails hard feasibility never reaches strategic selection.

## 14.1 Candidate rejection code

Use enumerated codes:

```text
0 = NONE
1 = TECH_UNAVAILABLE
2 = PRODUCER_UNAVAILABLE
3 = RESOURCE_UNAVAILABLE
4 = POPULATION_BLOCKED
5 = QUEUE_BLOCKED
6 = INFRASTRUCTURE_MISSING
7 = DEADLINE_MISSED
8 = RUNTIME_UNSUPPORTED
9 = OBJECTIVE_INVALID
10 = EVIDENCE_TOO_STALE
```

These are AEGIS codes, not historical engine error codes.

---

# 15. Belief and uncertainty representation

A rich probabilistic belief model is not appropriate for the first `.per` implementation because the runtime does not provide convenient floating-point data structures.

Use bounded confidence classes:

```text
0 = UNKNOWN
1 = LOW
2 = MEDIUM
3 = HIGH
4 = CONFIRMED
```

Unknown must never be encoded as false.

Example:

```text
enemy cavalry = UNKNOWN
```

is semantically distinct from:

```text
enemy cavalry = 0
```

## 15.1 Range representation

When exact enemy count is uncertain, represent:

```text
LOW_ESTIMATE
HIGH_ESTIMATE
CONFIDENCE
```

Example:

```text
4 ≤ enemy cavalry ≤ 12
confidence = LOW
```

This avoids fake precision.

## 15.2 Evidence age

Every cached observation needs a freshness mechanism.

Conceptually:

```text
OBS-GEN
OBS-AGE
OBS-CONF
OBS-VALID
```

The exact implementation may use timers to represent elapsed freshness windows and goals to store the associated generation/class.

---

# 16. Freshness architecture

A cached observation is not permanently true.

Use three states:

```text
FRESH
AGING
STALE
```

A timer can drive transitions:

```text
observation accepted
→ enable freshness timer
→ timer fires
→ mark aging/stale
```

However, timer expiration is not itself proof that the world changed. It only means the observation has exceeded its freshness policy.

This distinction matters:

```text
time elapsed
≠
fact became false
```

It means:

```text
confidence should be discounted
```

or

```text
re-observation should be requested
```

---

# 17. Controller clock vs world clock

Pass 88 established two clocks. Pass 89 makes them concrete state domains.

## Controller clock

Tracks internal AI state:

```text
rule evaluation
→ goal/SN/flag mutation
→ later controller evaluation
```

State fields may change without world realization.

## World clock

Tracks external realization:

```text
command
→ engine accepts / rejects
→ queue / pending
→ object completion
→ deployment
→ interaction
```

A command is not successful because the controller clock advanced.

Therefore an execution record needs both:

```text
controller_stage
world_stage
```

Example:

```text
controller_stage = ISSUED
world_stage = UNKNOWN
```

This is a legitimate state.

It is much safer than silently setting:

```text
world_stage = COMPLETED
```

---

# 18. Execution-state encoding

The conceptual verification ladder is:

```text
V0 INTENTION
V1 AUTHORIZED
V2 ISSUED
V3 PENDING
V4 CREATED
V5 AVAILABLE
V6 DEPLOYED
V7 INTERACTION
V8 OBJECTIVE_EFFECT
```

Represent this as an integer stage:

```text
EXEC-STAGE = 0..8
```

and separately record evidence quality:

```text
EXEC-EVIDENCE = NONE / DIRECT / CORRELATED / INFERRED
```

This prevents a common semantic error:

```text
train command observed
→ unit definitely exists
```

Instead:

```text
ISSUED
```

until queue/pending/completion evidence advances the state.

Official scripting history confirms that `unit-type-count-total` and `up-pending-objects` were expanded to account for additional queued objects, and later updates changed queue behavior further. citeturn0search1turn0search2

The architecture therefore treats queue/pending state as an intermediate lifecycle stage rather than an implementation detail.

---

# 19. Command realization contract

Every command-capable primitive must expose a five-part contract:

```text
PRECONDITION
ISSUE
PENDING OBSERVATION
COMPLETION OBSERVATION
FAILURE / TIMEOUT POLICY
```

Example:

```text
CREATE_CAMEL_CAPABILITY

PRECONDITION:
    objective valid
    capability deficit > 0
    candidate feasible
    producer eligible
    can-train true

ISSUE:
    train camel-line

PENDING:
    queue/pending evidence

COMPLETION:
    aggregate capability count or stronger object evidence

FAILURE:
    no pending/completion within observation window
```

Official Update 47820 confirms `can-train`, `up-can-train`, `train`, and `up-train` behavior changes, while Update 56005 confirms that AI can queue units while research is in progress when the relevant research-queue control is enabled. citeturn0search2turn0search3

These official notes support treating queue state and research interaction as first-class feasibility concerns.

---

# 20. Timers are temporal primitives, not generic counters

Timers should represent:

```text
review delay
retry cooldown
observation freshness
emergency window
commitment expiry
```

They should not be used merely because a counter is convenient.

Conceptual timer mapping:

```text
T-OBS-THREAT-FRESHNESS
T-COMMIT-REVIEW
T-COMMIT-RETRY
T-EMERGENCY
T-TRANSITION-WATCH
```

The architecture must keep timer identity separate from goal identity.

A timer firing should produce a state transition request, not silently mutate unrelated strategic state.

---

# 21. Searches are selection state, not permanent identity

A search answers a question such as:

```text
find eligible stable
find producer
find target
find nearby enemy
```

A search result must not automatically be treated as a durable object identity.

The identity taxonomy discovered during Layer 2 explicitly separates model/object IDs, references, entity IDs, action object IDs, and command correlation IDs.

Therefore AEGIS should store a search result only when:

```text
identity semantics are known
or
identity is explicitly classified as provisional
```

If the runtime cannot guarantee persistent identity, the architecture should use:

```text
search again
```

rather than retaining a potentially stale identity indefinitely.

---

# 22. State channels vs engine state

A major architectural rule is **minimum duplication**.

Do not cache something merely because a goal can store it.

Example:

```text
current age
```

should normally come from engine state.

By contrast:

```text
objective generation
```

does not exist as an engine fact and therefore belongs in AEGIS state.

This yields three classes:

### Authoritative engine state

```text
resources
age
queue
units
research
objects
```

### Authoritative AEGIS state

```text
objective
commitment
owner
generation
policy
candidate selection
recovery state
```

### Derived cache

```text
capability summary
threat summary
freshness bucket
```

Derived caches must be disposable and recomputable.

---

# 23. The state dependency graph

AEGIS should enforce this dependency direction:

```text
ENGINE FACTS
    ↓
OBSERVATIONS
    ↓
BELIEFS
    ↓
ASSESSMENTS
    ↓
OBJECTIVES
    ↓
CAPABILITY REQUIREMENTS
    ↓
CANDIDATES
    ↓
FEASIBILITY
    ↓
COMMITMENT
    ↓
EXECUTION
    ↓
WORLD OBSERVATION
    ↓
VERIFICATION
    ↓
REASSESSMENT
```

Reverse contamination should be minimized.

For example, a production controller should not redefine the strategic meaning of an objective merely because its queue is blocked.

Instead:

```text
queue blocked
→ execution feasibility false
→ recovery / re-arbitration
```

The objective may remain valid.

---

# 24. Capability observer design

The first practical observer should produce normalized capability summaries.

Example:

```text
CAPABILITY: ANTI_MOUNTED

CURRENT:
    own camel count
    own spear-line count
    relevant supporting capability

REQUIRED:
    bounded requirement

DEFICIT:
    required - current

FRESHNESS:
    fresh / aging / stale

CONFIDENCE:
    low / medium / high
```

Initially, the capability formula should remain intentionally simple.

For the cavalry vertical slice:

```text
CURRENT_ANTI_MOUNTED
    = validated weighted combination of accepted own-capability observations
```

The weighting model should not be implemented until its constituent measurements are individually validated.

This prevents “strategic sophistication” from outrunning measurement quality.

---

# 25. Resource obligation encoding

A commitment needs to know what it is consuming.

Do not attempt to encode a full economic ledger initially.

Use bounded obligation classes:

```text
0 = NONE
1 = LOW
2 = MEDIUM
3 = HIGH
4 = CRITICAL
```

Then separately represent resource-specific reservation state only where a controller genuinely needs it.

Example:

```text
FOOD_OBLIGATION = HIGH
GOLD_OBLIGATION = MEDIUM
WOOD_OBLIGATION = LOW
```

This avoids an early combinatorial explosion.

Later, the architecture may introduce quantitative reservations if the runtime representation proves robust.

---

# 26. Arbitration state

Global arbitration needs only a compact control plane initially.

Recommended fields:

```text
ARB-EPOCH
ARB-DIRTY
ARB-ACTIVE-COMMIT
ARB-PROPOSAL
ARB-REASON
ARB-FAIRNESS-STATE
```

`ARB-EPOCH` increments when a major state invalidation occurs.

Controllers compare their cached epoch with the current epoch.

```text
local_epoch != arb_epoch
→ recompute / re-arbitrate
```

This is a practical way to force stale local decisions back through a global control point without requiring a general event bus.

---

# 27. Fairness and starvation

Historical archaeology proved procedural resource competition but not a universal historical fairness scheduler.

AEGIS therefore introduces bounded starvation protection as a design requirement.

A candidate/commitment can track:

```text
wait class
last serviced epoch
age bucket
```

The first implementation should not calculate a complicated fairness score.

Use bounded policy:

```text
if waiting too long
→ increase arbitration attention
```

This is deliberately procedural and inspectable.

---

# 28. Recovery state

Recovery should be explicit.

Recommended:

```text
RECOVERY.NONE
RECOVERY.RETRY
RECOVERY.MODIFY
RECOVERY.REPLACE
RECOVERY.RELEASE
RECOVERY.GATHER_INFO
```

The controller must also store:

```text
failure_code
attempt_count
last_failure_generation
cooldown state
```

Failure does not imply automatic retry.

Historical archaeology found subsystem-specific rollback/recovery patterns, not a universal historical exception manager. The AEGIS recovery controller is therefore a deliberate architecture layer.

---

# 29. Failure-code taxonomy

The architecture should normalize runtime failures into a small vocabulary:

```text
F0 NONE
F1 OPPORTUNITY_LOST
F2 ECONOMIC_BLOCK
F3 PRODUCER_BLOCK
F4 QUEUE_BLOCK
F5 TEMPORAL_DEADLINE
F6 TARGET_INVALID
F7 PARTIAL_PROGRESS
F8 EVIDENCE_MISSING
F9 OBJECTIVE_INVALID
F10 RUNTIME_UNSUPPORTED
F11 STALE_GENERATION
F12 OWNERSHIP_CONFLICT
```

The distinction between `F8 EVIDENCE_MISSING` and actual world failure is mandatory.

For example:

```text
no observed completion
```

does not prove:

```text
unit failed to train
```

It proves only that completion evidence is unavailable within the observation contract.

---

# 30. Reset protocol

Every state object needs a deterministic reset sequence.

Generic release:

```text
1. disable side-effect permissions
2. invalidate record
3. clear transient fields
4. increment generation
5. release resource reservations
6. disable associated timers
7. clear derived flags
8. request re-arbitration
```

The order matters.

If the commitment is invalidated only after its side-effect flag is cleared, a later rule cannot accidentally act on a record that is conceptually dead.

Exact `.per` rule ordering must be validated during implementation.

---

# 31. Reuse protocol

State slots should be reusable.

A reusable slot must follow:

```text
FREE
→ ALLOCATE
→ GENERATE
→ POPULATE
→ VALIDATE
→ ACTIVE
→ RELEASE
→ INVALIDATE
→ REUSE
```

Never rely on zero as the universal reset value because zero may be a valid semantic value.

Instead define explicit sentinels:

```text
ID = 0        means NONE
VALID = 0     means invalid
GEN > 0       means allocated generation
```

Every field must declare whether zero is valid data or a sentinel.

---

# 32. Compact state is preferable to rich state

The first implementation must resist the temptation to encode every conceptual field.

A runtime record should contain only information needed to:

```text
make the next decision
protect the commitment
execute the next action
verify the next transition
recover if necessary
```

This is the **minimum sufficient state principle**.

A field should be rejected from the ABI if no consumer can answer:

```text
What decision does this field change?
What action does it guard?
What verification does it enable?
What recovery does it control?
```

---

# 33. Proposed minimum Commitment record

The first vertical slice can operate with approximately this conceptual record:

```text
COMMIT.ID
COMMIT.GEN
COMMIT.VALID
COMMIT.OWNER
COMMIT.OBJ
COMMIT.CAP
COMMIT.CAND
COMMIT.STAGE
COMMIT.ATTEMPTS
COMMIT.LAST-ACTION
COMMIT.LAST-EVIDENCE
COMMIT.FAILURE
COMMIT.REVIEW
```

Optional later fields:

```text
resource obligation
deadline
interruptibility
expected capability delta
confidence
```

This is intentionally smaller than the complete Pass-88 conceptual model.

---

# 34. Proposed minimum Objective record

```text
OBJ.ID
OBJ.GEN
OBJ.VALID
OBJ.TYPE
OBJ.URGENCY
OBJ.CONFIDENCE
OBJ.REVIEW
```

Deadline and success semantics can initially be encoded as classes rather than complex predicates.

Example:

```text
DEADLINE = NONE / LONG / MEDIUM / SHORT / IMMEDIATE
```

This allows strategic timing to exist without requiring a continuous time model.

---

# 35. Proposed minimum Capability record

```text
CAP.ID
CAP.REQUIRED
CAP.CURRENT
CAP.DEFICIT
CAP.CONFIDENCE
CAP.FRESHNESS
```

A capability ID selects a measurement function.

Example:

```text
CAP.ID = ANTI_MOUNTED
```

The observer knows which engine facts feed that capability.

This is the critical separation:

```text
CAPABILITY NAME
≠
UNIT TYPE
```

---

# 36. Proposed minimum Candidate record

Candidates can be represented transiently rather than as persistent objects.

For the first implementation:

```text
CANDIDATE-UNDER-EVALUATION
CANDIDATE-FEASIBLE
CANDIDATE-REJECT-CODE
CANDIDATE-SELECTED
```

This avoids allocating a large persistent candidate table.

Candidate generation can remain procedural initially:

```text
evaluate camel
→ evaluate spear
→ evaluate static defense
→ evaluate reposition
→ select feasible candidate
```

If later evidence shows that parallel candidate persistence is necessary, the ABI can expand.

---

# 37. Runtime State ABI: canonical transition protocol

The core state transition should be:

```text
OBSERVE
  ↓
WRITE OBSERVATION
  ↓
ASSESS
  ↓
VALIDATE OBJECTIVE
  ↓
CALCULATE CAPABILITY DEFICIT
  ↓
GENERATE CANDIDATE
  ↓
CHECK HARD FEASIBILITY
  ↓
SELECT
  ↓
ALLOCATE COMMITMENT GENERATION
  ↓
AUTHORIZE
  ↓
ISSUE COMMAND
  ↓
WAIT FOR WORLD EVIDENCE
  ↓
ADVANCE EXECUTION STAGE
  ↓
VERIFY POSTCONDITION
  ↓
RELEASE / MAINTAIN / RECOVER
  ↓
RE-ARBITRATE
```

The architecture must not shortcut:

```text
SELECT
→ COMPLETE
```

or:

```text
ISSUE
→ EFFECTIVE
```

---

# 38. State machine for Commitment

Canonical conceptual state machine:

```text
                    ┌──────────────┐
                    │     FREE     │
                    └──────┬───────┘
                           │ allocate
                           ▼
                    ┌──────────────┐
                    │   PROPOSED   │
                    └──────┬───────┘
                           │ authorize
                           ▼
                    ┌──────────────┐
                    │  AUTHORIZED  │
                    └──────┬───────┘
                           │ issue
                           ▼
                    ┌──────────────┐
                    │   EXECUTING  │
                    └──────┬───────┘
                           │ evidence
                           ▼
                    ┌──────────────┐
                    │  PROGRESSING │
                    └──────┬───────┘
                           │ verify
                 ┌─────────┴─────────┐
                 ▼                   ▼
          ┌─────────────┐      ┌──────────────┐
          │   VERIFIED  │      │    FAILURE   │
          └──────┬──────┘      └──────┬───────┘
                 │                    │ classify
                 ▼                    ▼
          ┌─────────────┐      ┌──────────────┐
          │ MAINTAINED  │      │   RECOVERY   │
          └──────┬──────┘      └──────┬───────┘
                 │                    │ retry/modify/
                 │                    │ replace/release
                 └─────────┬──────────┘
                           ▼
                    ┌──────────────┐
                    │    RELEASE   │
                    └──────┬───────┘
                           ▼
                         FREE
```

No state is permanent.

Every active commitment needs at least one exit path.

---

# 39. Hard feasibility representation

Feasibility should be represented as a Boolean gate plus a rejection code.

Conceptually:

```text
FEASIBLE = TECH_OK
        AND PRODUCER_OK
        AND RESOURCE_OK
        AND QUEUE_OK
        AND DEADLINE_OK
        AND RUNTIME_OK
```

Each component should be separately observable where practical.

Example:

```text
TECH_OK = 1
PRODUCER_OK = 1
RESOURCE_OK = 1
QUEUE_OK = 0
DEADLINE_OK = 1
RUNTIME_OK = 1
```

Result:

```text
FEASIBLE = 0
REJECT = QUEUE_BLOCK
```

This is superior to one opaque `cannot-do` flag because recovery depends on the failure class.

---

# 40. Soft evaluation representation

Only feasible candidates reach soft evaluation.

The first implementation should use discrete classes rather than arbitrary large scores.

Possible dimensions:

```text
COUNTER_VALUE = 0..4
TEMPO = 0..4
RISK = 0..4
LOCKIN = 0..4
OPTIONALITY = 0..4
```

Selection can initially be implemented as ordered policy bands rather than a universal mathematical optimizer.

This follows the evidence boundary: historical archaeology supports procedural arbitration but does not prove a universal numeric argmax scheduler.

A future optimizer may exist, but it must be justified by implementation need and validated independently.

---

# 41. Deadline encoding

Do not immediately encode absolute game-time timestamps if the runtime does not make that cheap or reliable.

Use deadline classes:

```text
0 = NONE
1 = LONG
2 = MEDIUM
3 = SHORT
4 = IMMEDIATE
```

Then map candidate capability latency into the class.

Conceptual test:

```text
candidate latency > deadline budget
→ infeasible
```

Later, if a validated timer/time measurement substrate supports finer precision, the schema may expand.

---

# 42. Capability latency representation

The architecture defines:

```text
CAPABILITY LATENCY
=
DECISION LATENCY
+
AUTHORIZATION LATENCY
+
QUEUE LATENCY
+
TRAINING / BUILD LATENCY
+
DEPLOYMENT LATENCY
```

The `.per` implementation should initially represent this qualitatively:

```text
LATENCY CLASS
0 = instant / already available
1 = short
2 = medium
3 = long
4 = too late
```

This keeps the first controller robust while preserving the concept needed for later quantitative optimization.

---

# 43. Research queue interaction

Research is part of execution feasibility.

Official Update 47820 introduced `sn-enable-research-queue`; Update 56005 later enabled AI unit queuing while research is in progress when the research queue is enabled. citeturn0search2turn0search3

Therefore an AEGIS feasibility predicate must distinguish:

```text
research available
research authorized
research pending
research blocking queue
research and production coexistence
```

The architecture should not hard-code the assumption that research always blocks unit production.

---

# 44. Queue state is engine-owned

AEGIS must not simulate its own queue as authoritative state.

It may cache:

```text
queue expected
```

but engine observation remains authoritative for:

```text
queue pending
queue occupancy
object completion
```

This is essential because official scripting behavior explicitly changed around queued-object counting and research/production interaction. citeturn0search1turn0search3

---

# 45. Production state encoding

Production should expose at least:

```text
DEMAND
ELIGIBLE
AUTHORIZED
ISSUED
PENDING
CREATED
AVAILABLE
DEPLOYED
EFFECTIVE
```

These correspond to different controller/world states.

For a camel response:

```text
DEMAND
→ deficit > 0

ELIGIBLE
→ candidate survives hard constraints

AUTHORIZED
→ commitment permits production

ISSUED
→ train command executed

PENDING
→ queue evidence observed

CREATED
→ aggregate/object evidence

AVAILABLE
→ capability count / unit state supports use

DEPLOYED
→ unit has entered intended operational state

EFFECTIVE
→ battlefield/objective evidence
```

The architecture should allow the state to stop at any level when evidence is insufficient.

---

# 46. Evidence-strength encoding

Use a separate evidence-strength class:

```text
E0 = NONE
E1 = DIRECT ENGINE FACT
E2 = DIRECT STATE TRANSITION
E3 = CORRELATED OBSERVATION
E4 = HEURISTIC INFERENCE
```

This is an implementation representation of the broader repository evidence discipline.

Do not conflate:

```text
execution stage
```

with:

```text
evidence strength
```

A stage may be `PENDING` with E1 evidence.

A stage may be `CREATED` with only E3 correlation.

The architecture must decide whether E3 is sufficient for promotion before doing so.

---

# 47. State promotion rules

State transitions must be monotonic unless recovery explicitly rolls them back.

Example:

```text
AUTHORIZED → ISSUED → PENDING → CREATED
```

is monotonic.

But:

```text
PENDING → AUTHORIZED
```

is not a normal transition. It requires explicit failure/recovery classification.

This prevents silent semantic regression.

A recovery may deliberately perform:

```text
PENDING
→ FAILURE
→ PROPOSED replacement
```

rather than pretending the original commitment never happened.

---

# 48. World-state verification policy

Verification must be tied to the primitive's declared capability.

For production:

```text
train issued
```

may verify only V2.

If queue evidence is observed:

```text
V3
```

If completion is observed:

```text
V4/V5
```

If battlefield interaction is observed:

```text
V7
```

If the strategic objective improves:

```text
V8
```

The primitive registry must state the maximum supported verification level.

---

# 49. Stale-state attack model

Pass 89 treats stale state as an adversarial engineering problem.

Potential stale-state cases:

```text
old objective remains valid after threat disappears
old commitment writes after replacement
old producer identity is reused
old observation survives too long
old queue expectation survives cancellation
old timer fires after commitment release
```

Each requires a guard.

Recommended guard families:

```text
generation check
validity check
owner check
epoch check
freshness check
stage check
```

A rule with no applicable guard should be presumed dangerous until proven otherwise.

---

# 50. Timer-stale interaction

A particularly dangerous pattern is:

```text
commitment A starts timer T
commitment A releases
commitment B reuses state
T fires
→ B is accidentally modified
```

The solution is to associate timer-triggered actions with a generation.

Conceptually:

```text
T-COMMIT-REVIEW belongs to GEN 12
```

When it fires:

```text
current generation == 12 ?
    yes → process
    no  → ignore as stale
```

If direct timer-to-generation binding is awkward in `.per`, use a shared review generation goal checked by the consuming rule.

---

# 51. Search-stale interaction

Similarly:

```text
search producer
→ save result
→ producer dies / becomes invalid
→ later command uses saved result
```

The correct pattern is:

```text
search result
→ validate current eligibility
→ act
```

not:

```text
search result
→ trust indefinitely
```

This is especially important for dynamic battlefield targets and production locations.

---

# 52. Resource reservation model

AEGIS should treat resource reservations as policy state, not as engine resources.

For example:

```text
G-RESERVE-FOOD
G-RESERVE-WOOD
G-RESERVE-GOLD
G-RESERVE-STONE
```

may represent intended obligations.

Actual resources remain engine state.

Therefore:

```text
actual gold = 200
reserved gold = 150
available discretionary gold = 50
```

is an AEGIS interpretation, not an engine fact.

The architecture must never claim that the engine itself knows the reservation.

---

# 53. Reservation safety

A reservation should be created only after commitment authorization.

Sequence:

```text
candidate feasible
→ commit
→ reservation state
→ action
```

Not:

```text
candidate considered
→ reserve resources
```

Otherwise candidate evaluation itself can starve competing candidates.

Release policy:

```text
verified completion
→ release unused reservation

invalidated objective
→ release

failed execution
→ release or modify

replacement
→ release old / allocate new
```

This extends the historical commitment/release archaeology into an explicit AEGIS design.

---

# 54. Arbitration dirty-bit

Every significant world or strategic change should be able to mark arbitration dirty.

Examples:

```text
major threat increase
resource collapse
commitment failure
producer loss
objective invalidation
capability completion
```

Conceptually:

```text
ARB-DIRTY = 1
```

The global controller consumes it:

```text
if ARB-DIRTY
→ recompute active commitments
→ clear ARB-DIRTY
```

This creates a lightweight event-driven effect using ordinary state channels.

It does not require an event bus.

---

# 55. Avoiding controller thrash

Re-arbitration after every observation can create instability.

Therefore use a review gate:

```text
minor observation
→ update belief
→ no global arbitration

material state change
→ dirty arbitration

commitment failure
→ mandatory arbitration

objective invalidation
→ mandatory arbitration
```

Materiality can initially be discrete:

```text
NONE
LOW
MEDIUM
HIGH
CRITICAL
```

The controller should only escalate when the change can alter candidate feasibility or commitment validity.

---

# 56. Commitment review cadence

A commitment must not remain active forever.

Each commitment receives:

```text
review timer
```

At review:

```text
objective still valid?
capability deficit still present?
execution progressing?
resource burden acceptable?
new higher-priority threat?
```

Then:

```text
MAINTAIN
MODIFY
REPLACE
RELEASE
```

This is the runtime realization of bounded commitment persistence.

---

# 57. Objective vs commitment invalidation

The architecture must support four combinations:

| Objective | Commitment | Meaning |
|---|---|---|
| valid | valid | continue |
| valid | invalid | find replacement execution |
| invalid | valid | release or repurpose |
| invalid | invalid | release |

This matrix is important because a failed execution does not necessarily invalidate the strategic need.

Example:

```text
Objective: protect against cavalry
Camel commitment fails because stable is unavailable
```

Correct:

```text
objective remains valid
commitment fails
→ candidate set regenerated
→ spear/static-defense candidate considered
```

Not:

```text
camel failed
→ stop defending
```

---

# 58. Information candidate

The candidate set should eventually include:

```text
ACT
WAIT
SCOUT
REPOSITION
DEFEND
TRANSITION
DENY
```

A low-confidence threat may produce:

```text
SCOUT
```

rather than immediate maximal production.

The state representation needs no special information-action object. It can reuse candidate type:

```text
CAND.TYPE = INFORMATION
```

and a commitment lifecycle identical to production.

This demonstrates the value of capability-first architecture: information acquisition becomes another executable candidate class.

---

# 59. Compatibility profiles

## L3-COMPAT

The conservative profile assumes:

```text
goals: low-numbered core allocation
SNs: ≤ 511
flags: Boolean
 timers: finite explicit pool
search: engine-managed
no XS
```

No architectural dependency may require a goal above the conservative core without a build gate.

## L3-DE-CURRENT

The expanded profile may exploit the larger goal namespace documented by Update Preview 125283, but only after the installed game build and validator accept the relevant identifiers. citeturn0search0

## Profile selection

At startup, the bot should eventually establish a build/runtime profile through validated configuration rather than guessing.

Conceptually:

```text
BUILD PROFILE
→ supported goal range
→ supported SN range
→ primitive availability
→ known validator constraints
```

No unsupported feature should silently fall back to a semantically different operation.

---

# 60. Build-sensitive primitive registry

Every primitive should carry:

```text
MIN_BUILD
MAX_TESTED_BUILD
PROFILE
```

Example:

```text
PRIM-UP-PENDING-OBJECTS
profile: L3-COMPAT
status: ARCHAEOLOGICALLY_SUPPORTED
```

Another primitive may be:

```text
PRIM-EXTENDED-GOAL-STATE
profile: L3-DE-CURRENT
status: DOCUMENTED
runtime validation: OPEN
```

The registry therefore prevents accidental cross-build assumptions.

---

# 61. Static validation requirements

Before any runtime deployment, the project should add a state-schema validator capable of detecting:

```text
unknown field
wrong storage class
out-of-range goal
out-of-range SN
invalid sentinel
multiple writers
missing reset policy
missing generation guard
missing owner
missing verification path
```

For every `.per` state symbol, the validator should be able to answer:

```text
What is this?
Who writes it?
Who reads it?
What values are legal?
When is it valid?
How is it reset?
What generation protects it?
```

This becomes the Layer-3 equivalent of the project's existing evidence discipline.

---

# 62. Runtime lint rules

Proposed lint rules:

### L3-S001 — undeclared state channel

Reject any AEGIS-prefixed goal/SN/flag/timer without a registry entry.

### L3-S002 — multiple authoritative writers

Reject more than one writer unless explicitly declared as an arbitration protocol.

### L3-S003 — missing validity guard

Reject reads of multi-field logical records without a validity check.

### L3-S004 — missing generation guard

Reject delayed/timer-driven writes to reusable records without generation protection.

### L3-S005 — SN memory misuse

Flag arbitrary persistence in engine-sensitive SNs.

### L3-S006 — goal range violation

Reject goal IDs outside the active build profile.

### L3-S007 — sentinel ambiguity

Reject fields where zero is simultaneously valid data and the declared `NONE` sentinel.

### L3-S008 — command promotion

Flag code that advances execution stage without declared evidence.

### L3-S009 — stale observation

Flag strategic decisions consuming observations beyond their freshness contract.

### L3-S010 — objective/feasibility collapse

Flag logic that equates objective validity with action feasibility.

---

# 63. The first implementation allocation should be smaller than this document

This document deliberately defines the complete architecture envelope.

The first implementation should use only:

```text
objective
capability
candidate
commitment
execution stage
failure code
review timer
arbitration dirty state
```

It should not begin by implementing:

```text
probabilistic belief engine
complex fairness optimizer
full resource reservation matrix
multi-object candidate database
continuous optionality score
```

Those are later increments.

The architecture must be capable of expansion without requiring them on day one.

---

# 64. First vertical slice state map: Cavalry Threat Containment

The first implementation target from Pass 88 is:

```text
ENEMY MOUNTED PRESSURE
```

Minimal state flow:

```text
OBSERVE ENEMY MOUNTED COUNT
        ↓
UPDATE THREAT OBSERVATION
        ↓
OBJECTIVE = CONTAIN MOUNTED THREAT
        ↓
REQUIRED ANTI-MOUNTED CAPABILITY
        ↓
CURRENT OWN CAPABILITY
        ↓
DEFICIT
        ↓
CANDIDATE CAMEL
        ↓
HARD FEASIBILITY
        ↓
COMMIT
        ↓
TRAIN
        ↓
QUEUE/PENDING
        ↓
CREATED/AVAILABLE
        ↓
REASSESS DEFICIT
```

The historical Byzantine camel chain provides strong precedent for the low-level runtime pattern: mounted threat state, camel-set own-capability state, feasibility gates, and camel production conditions. The AEGIS architecture adds explicit objective/capability/commitment semantics above that substrate.

---

# 65. Vertical-slice minimum state

The cavalry slice should require no more than:

```text
THREAT-OBSERVATION
THREAT-FRESHNESS
THREAT-CONFIDENCE
OBJECTIVE-VALID
CAP-REQUIRED
CAP-CURRENT
CAP-DEFICIT
CAND-FEASIBLE
COMMIT-VALID
COMMIT-GEN
COMMIT-STAGE
COMMIT-ATTEMPTS
COMMIT-FAILURE
ARB-DIRTY
REVIEW-TIMER
```

If implementation requires substantially more state before the first successful closed loop, the architecture should be reviewed for accidental complexity.

---

# 66. Example end-to-end state transition

Assume:

```text
enemy mounted pressure = HIGH
own anti-mounted capability = 4
required = 8
```

Observer writes:

```text
CAP-CURRENT = 4
CAP-REQUIRED = 8
CAP-DEFICIT = 4
```

Objective controller writes:

```text
OBJ-VALID = 1
OBJ-URGENCY = HIGH
```

Candidate evaluator tests camel:

```text
TECH_OK = 1
PRODUCER_OK = 1
RESOURCE_OK = 1
QUEUE_OK = 1
DEADLINE_OK = 1
RUNTIME_OK = 1
```

Candidate becomes feasible.

Commitment controller allocates:

```text
COMMIT-VALID = 1
COMMIT-GEN = 17
COMMIT-CAND = CAMEL
COMMIT-STAGE = AUTHORIZED
```

Production controller issues training:

```text
COMMIT-STAGE = ISSUED
```

Queue observation confirms pending:

```text
COMMIT-STAGE = PENDING
```

Completion evidence confirms additional capability:

```text
COMMIT-STAGE = CREATED/AVAILABLE
```

Capability observer recomputes:

```text
CURRENT = 8
DEFICIT = 0
```

Objective is reassessed.

The commitment can then be maintained or released according to policy.

Notice that no single action ever meant “we won.”

---

# 67. What the state model explicitly does not claim

This architecture does **not** claim that historical HD AI possessed:

```text
native Objective objects
native Capability objects
native Commitment objects
native ownership transactions
native generation counters
formal probabilistic beliefs
universal exception manager
universal fairness scheduler
universal priority score
atomic state transactions
```

Those are AEGIS engineering constructs.

Historical evidence instead supplies mechanisms from which the architecture can be built safely:

```text
persistent goals
strategic numbers
flags
timers
searches
resource gates
procedural rule ordering
state reset/release
pending/queue observations
failure-specific recovery
```

The architecture is therefore **inspired by and constrained by the substrate**, not presented as a reconstruction of historical author intent.

---

# 68. External engine evidence incorporated into this pass

Several official updates materially affect the state design.

### Strategic-number range

Update 42848 extended the maximum strategic-number range from 303 to 511. This supports the conservative SN ceiling used here. citeturn0search4

### Goal namespace

Update Preview 125283 increased available goals from 512 to 16000. This supports an expanded current-build profile but does not justify making the conservative profile depend on it. citeturn0search0

### Queued-object observability

Update 36202 states that `unit-type-count-total` and `up-pending-objects` count additional objects in the unit queue. This supports the explicit pending lifecycle used by AEGIS. citeturn0search1

### Training/research interaction

Update 47820 documents `can-train` / `train` changes and introduces `sn-enable-research-queue`. Update 56005 documents AI queuing units during research when the research queue is enabled. This supports treating queue and research interaction as runtime feasibility state. citeturn0search2turn0search3

### Current-build caution

Update 177723, the June 2026 major update, contains additional AI-engine fixes, demonstrating that AI scripting/runtime behavior remains a living surface rather than a permanently frozen historical interface. citeturn1search0

### XS exclusion

Official Update 87863 added XS support with persistent information and additional mathematical/storage functionality. AEGIS explicitly does not use that mechanism. citeturn1search6

---

# 69. Validation ladder for the state ABI

The state architecture itself needs validation.

## ABI-V0 — documented

Field schema exists in the registry.

## ABI-V1 — static validated

Names, ranges, ownership, and storage classes pass static validation.

## ABI-V2 — parser validated

`.per` syntax and identifiers are accepted by the project's validator.

## ABI-V3 — controller validated

State transitions occur as expected under deterministic test conditions.

## ABI-V4 — engine validated

State correctly mediates real engine commands and observations.

## ABI-V5 — replay corroborated

Recorded games corroborate the relevant world-state transitions.

## ABI-V6 — adversarial validated

Stale generation, invalid target, queue blockage, resource starvation, and recovery cases behave correctly.

## ABI-V7 — battlefield validated

The state model reliably supports a complete strategic vertical slice in actual play.

No field should be described as “fully implemented” merely because ABI-V0 or ABI-V2 has passed.

---

# 70. Adversarial test matrix

The minimum test matrix for the commitment state is:

| Test | Expected result |
|---|---|
| objective disappears before action | commitment released/replanned |
| producer disappears | feasibility fails; candidate replacement considered |
| resources insufficient | no command issued |
| queue blocked | commitment remains pending/recovery; no false completion |
| command issued but no evidence | stage remains bounded; uncertainty preserved |
| unit completes | stage advances only on evidence |
| old timer fires after release | stale generation ignored |
| old writer acts after replacement | generation/owner guard rejects it |
| threat decreases | deficit recomputed; overproduction avoided |
| threat increases during commitment | arbitration may escalate |
| two commitments compete | global policy prevents uncontrolled overcommit |
| observation becomes stale | confidence/freshness degrades; re-observation possible |
| validator rejects primitive | feature remains unimplemented; no semantic fallback |

This matrix should eventually become executable test documentation.

---

# 71. What must be measured before implementation

Before writing the first production `.per` state module, the following must be verified against the actual installed build:

```text
goal range accepted by validator
SN range accepted by validator
flag namespace behavior
timer count and semantics
exact goal comparison operand limits
exact up-get-focus-fact operand behavior
unit-line handling
queue/pending fact semantics
search invalidation behavior
same-pass state visibility
rule ordering behavior
```

The repository already contains strong historical evidence for many of these, but architecture-level confidence is not equivalent to current-build runtime validation.

The local workstation is currently not reachable through the authorized remote connection, so this pass intentionally makes **no local runtime claim**.

---

# 72. Implementation order after Pass 89

The correct next implementation sequence is now:

```text
P90 — Runtime Primitive Registry
    ↓
P91 — State ABI static validator
    ↓
P92 — Minimal state module
    ↓
P93 — Feasibility engine
    ↓
P94 — Capability deficit controller
    ↓
P95 — Cavalry vertical slice
    ↓
P96 — Verification / recovery harness
    ↓
P97 — Adversarial transition tests
    ↓
P98 — Global arbitration
```

The exact numbering is provisional; the dependency order is the important part.

---

# 73. Hard architectural invariants

The following invariants are now mandatory for Layer 3:

### I1 — Unknown is not false

No missing observation may silently become zero/false.

### I2 — Objective validity is not feasibility

A valid strategic objective may have no currently feasible execution.

### I3 — Issued is not completed

Command issuance never advances beyond the evidence supported by the runtime.

### I4 — Controller state is not world state

Internal state transitions do not prove world realization.

### I5 — Generation protects reuse

Reusable records require generation discipline.

### I6 — Ownership is explicit

Authoritative mutation requires an assigned writer/owner.

### I7 — Recovery is explicit

Failure must enter a classified recovery path rather than implicit retry.

### I8 — Derived state is disposable

Cached observations must be recomputable from engine evidence.

### I9 — Engine state remains authoritative

AEGIS reservations or expectations never overwrite the meaning of engine resources/queues/objects.

### I10 — Feasibility precedes optimization

Impossible candidates never win strategic selection.

### I11 — Every active commitment has an exit path

No commitment may become immortal state.

### I12 — Build profile controls feature availability

No current-build feature may be assumed portable to the compatibility profile.

---

# 74. Architectural significance

Pass 88 defined the translation boundary.

Pass 89 defines the memory/state substrate across that boundary.

This is the point at which AEGIS becomes implementable without pretending that `.per` is a modern object-oriented language.

The architecture now has a concrete answer to the question:

> Where does the AI's strategic state live?

Answer:

```text
ENGINE FACTS
    → engine-owned world state

GOALS
    → authoritative AEGIS scalar state

FLAGS
    → Boolean control/latch state

SNs
    → engine-facing control parameters

TIMERS
    → temporal validity/review/retry state

SEARCHES
    → dynamic selection mechanisms

GENERATIONS
    → stale-state protection

OWNERS
    → authoritative mutation discipline

EXECUTION STAGES
    → controller/world lifecycle separation

EVIDENCE CODES
    → epistemic boundary preservation
```

The architecture does not require XS.

It does not require native structs.

It does not require a hidden external database.

It requires disciplined scalar state, explicit schemas, bounded encodings, guarded transitions, and verification.

That is the practical route from abstract AI architecture to `.per`.

---

# 75. Final engineering judgment

The critical insight of Pass 89 is that **typed architecture does not require typed language primitives**.

A sufficiently disciplined runtime ABI can provide the essential properties:

```text
identity
lifetime
ownership
validity
generation
state
provenance
uncertainty
timing
execution stage
recovery
```

using a constrained collection of integer, Boolean, temporal, search, and engine-observation primitives.

But there is an equally important warning:

> **The schema is not the implementation.**

Until the actual `.per` encoding is written, statically validated, executed in the current build, and tested against failure transitions, this remains an architecture specification.

The next engineering step is therefore not more conceptual abstraction.

It is to construct the **Runtime Primitive Registry and State ABI registry**, then make the first minimal state machine pass the validator before adding strategic complexity.

The project should now move from:

```text
WHAT SHOULD AEGIS MEAN?
```

to:

```text
WHICH EXACT RUNTIME PRIMITIVES CAN REALIZE EACH FIELD AND TRANSITION?
```

That is the Layer-3 implementation boundary.

---

# Appendix A — Compact field registry template

Every field introduced by implementation should be registered in this form:

```text
FIELD_ID:
CONCEPTUAL_TYPE:
SEMANTIC_NAME:
STORAGE_CLASS:
RUNTIME_IDENTIFIER:
ENCODING:
MIN:
MAX:
SENTINEL:
AUTHORITATIVE_OWNER:
READERS:
WRITERS:
VALIDITY_GUARD:
GENERATION_GUARD:
RESET_POLICY:
TIMER_DEPENDENCY:
ENGINE_DEPENDENCY:
SUCCESS_EVIDENCE:
FAILURE_EVIDENCE:
BUILD_PROFILE:
EVIDENCE_GRADE:
VALIDATION_STATUS:
KNOWN_LIMITS:
```

---

# Appendix B — Compact Commitment ABI

```text
COMMIT.VALID
COMMIT.GEN
COMMIT.OWNER
COMMIT.OBJ
COMMIT.CAP
COMMIT.CAND
COMMIT.STAGE
COMMIT.ATTEMPTS
COMMIT.LAST_ACTION
COMMIT.LAST_EVIDENCE
COMMIT.FAILURE
COMMIT.REVIEW
```

Required guards:

```text
VALID == 1
GEN == expected_gen
OWNER == current_writer
```

---

# Appendix C — Compact Objective ABI

```text
OBJ.VALID
OBJ.GEN
OBJ.TYPE
OBJ.URGENCY
OBJ.CONFIDENCE
OBJ.REVIEW
```

Required rule:

```text
OBJ.VALID = 0
```

must prevent new commitments for that objective unless an explicit recovery/retirement rule authorizes another transition.

---

# Appendix D — Compact Capability ABI

```text
CAP.REQUIRED
CAP.CURRENT
CAP.DEFICIT
CAP.CONFIDENCE
CAP.FRESHNESS
```

Required equation:

```text
CAP.DEFICIT = CAP.REQUIRED - CAP.CURRENT
```

with saturation/negative-value policy explicitly defined before implementation.

---

# Appendix E — Compact execution ABI

```text
EXEC.STAGE
EXEC.EVIDENCE
EXEC.FAILURE
EXEC.ATTEMPTS
```

Stage values:

```text
0 INTENTION
1 AUTHORIZED
2 ISSUED
3 PENDING
4 CREATED
5 AVAILABLE
6 DEPLOYED
7 INTERACTION
8 OBJECTIVE_EFFECT
```

Promotion requires evidence.

Rollback requires classified recovery.

---

# Appendix F — Evidence grades used by this document

```text
E0 — direct source / engine documentation
E1 — strong operational inference
E2 — AEGIS generalization / architecture
E3 — open hypothesis
```

For implementation readiness:

```text
DOCUMENTED
ARCHAEOLOGICALLY_SUPPORTED
IMPLEMENTED
RUNTIME_VALIDATED
REPLAY_CORROBORATED
BATTLEFIELD_VALIDATED
```

These dimensions must not be collapsed into one confidence score.

---

# Appendix G — Source boundary

Primary historical and project evidence is maintained in the repository's Layer-2 archaeology and Layer-3 architecture artifacts. Pass 87 establishes the evidence graph and explicitly separates historical fact, AEGIS interpretation, AEGIS design, implementation, and validation. Pass 88 establishes the runtime translation contract and primitive registry. This pass specializes that contract into a concrete state-representation architecture. fileciteturn878file0 fileciteturn881file0

Official engine references used for build-sensitive claims are the Age of Empires II: Definitive Edition release notes cited inline above.

---

**Pass 89 disposition:** COMPLETE AS ARCHITECTURE.  
**Production `.per`:** NOT YET IMPLEMENTED.  
**Local runtime validation:** BLOCKED BY CURRENT WORKSTATION CONNECTION STATE.  
**Layer 1:** UNCHANGED / CLOSED AT PRIOR STATE.  
**XS:** EXCLUDED.  
**Next highest-value action:** Build the Runtime Primitive Registry and State ABI registry, then statically validate the minimal state substrate before implementing strategic logic.
