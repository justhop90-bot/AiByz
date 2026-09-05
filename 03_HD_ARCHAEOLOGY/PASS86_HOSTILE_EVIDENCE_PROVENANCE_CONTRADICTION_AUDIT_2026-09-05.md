# PASS 86 — HOSTILE EVIDENCE / PROVENANCE / CONTRADICTION AUDIT

**Layer:** 2 — HD archaeology / methodology audit  
**Status:** Research only; no `.per` implementation, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Scope:** accumulated Layer-2 conclusions through Pass 85

## Executive result

Pass 86 performs the hostile audit that became more valuable than another narrow primitive hunt after Pass 85.

The audit asks four questions:

1. **What is actually directly demonstrated by historical source?**
2. **Where have analytical abstractions risked being mistaken for historical mechanisms?**
3. **Where can apparently contradictory observations coexist because they operate at different semantic layers or under different state gates?**
4. **Which negative conclusions are genuinely justified, and which merely reflect incomplete search coverage?**

The principal result is positive but corrective:

> The accumulated methodology is internally coherent if—and only if—historical facts, operational interpretations, AEGIS generalizations, and unproven hypotheses remain explicitly separated.

Several recurring claims require narrower wording. None currently invalidates the central architecture boundary established through Passes 80–85.

---

# 1. The four-level evidence ladder

The project must permanently distinguish four claim classes.

## E0 — Direct evidence

The proposition is directly represented by an authoritative artifact, executable historical source, official patch documentation, or reproducible measurement.

Examples:

```text
historical author comment says rule order affects resource spending
historical source contains a specific state mutation
official patch note defines pending-object behavior
replay contains a recorded queue action
```

E0 is the strongest class.

## E1 — Strong operational inference

The proposition is not literally stated, but follows closely from multiple direct observations with little architectural assumption.

Example:

```text
shared goal is written
+
later rule guards depend on that goal
+
rule ordering is known to matter
↓
state mutation is operationally consequential to later controller evaluation
```

E1 is useful but must not be rewritten as E0.

## E2 — AEGIS generalization

The project converts several historical mechanisms into a cleaner conceptual abstraction.

Examples:

```text
commitment
candidate set
objective validity
execution feasibility
capability latency
failure taxonomy
procedural arbitration
```

These are analytical models unless an historical source explicitly uses equivalent semantics.

## E3 — Hypothesis / open question

The proposition remains plausible but requires stronger evidence.

Examples:

```text
uniqueId == spawned Entity.id
formal historical ownership transfer
universal fairness
historical argmax optimization
exact same-pass transactional handoff
```

E3 must never enter the implementation specification as a historical fact.

---

# 2. Core audit finding: the central model survives

The integrated control model remains defensible:

```text
OBSERVE
↓
ASSESS / SELECT
↓
COMMIT / POLICY STATE
↓
AUTHORIZE
↓
ACTION
↓
OBSERVE POSTCONDITION
↓
SUCCESS / PARTIAL / FAILURE
↓
RECOVER / RETAIN / ADJUST / RELEASE
↓
RE-ARBITRATE
```

But this is **not** a claim that historical HD implements one centralized state machine.

The historical evidence instead supports a distributed implementation substrate:

```text
FACTS
+
GOALS / SNs / FLAGS / TIMERS
+
LOCAL RULES
+
RULE ORDER
+
SIDE EFFECTS
+
PENDING / WORLD OBSERVATION
+
LOCAL RECOVERY
```

The centralized model belongs to AEGIS methodology.

---

# 3. Claim-promotion audit

## 3.1 “Rule order matters”

**Status:** E0.

The historical author commentary explicitly states that the first rule executed can consume resources such that later rules cannot spend them, with siege training intentionally placed above building.

Safe formulation:

> In the relevant historical execution context, rule ordering can affect which resource-consuming path obtains the opportunity first.

Unsafe formulation:

> The AI is globally first-rule-wins.

The second statement is rejected.

## 3.2 “First effective path”

**Status:** E1 / AEGIS normalization.

The phrase correctly captures why textual order alone is insufficient:

```text
RULE POSITION
×
FACTS
×
STATE
×
RESOURCES
×
CONTROL FLOW
```

However, “first effective path” is our analytical term, not a recovered engine primitive.

## 3.3 `sn-resource-control` as admission control

**Status:** E0 for target-bearing gating patterns; E2 for the generalized admission-control interpretation.

Historical source demonstrates mutable `sn-resource-control` values that affect downstream rule eligibility.

It does not establish that the engine defines this SN as a formal mutex, lock, reservation object, or utility score.

Safe:

> Historical scripts use `sn-resource-control` as a mutable resource-policy state that can gate competing spending behavior.

Unsafe:

> `sn-resource-control` is the HD commitment lock.

## 3.4 Commitment

**Status:** E2.

The historical system clearly contains persistent target-bearing state, resource protection, reset, replacement, and retry-like behavior. Calling the combined abstraction a “commitment” is analytically powerful.

It remains an AEGIS abstraction unless a historical source explicitly defines the equivalent semantic object.

## 3.5 Action authorization

**Status:** E2 with E0 constituents.

Historical facts such as `can-train`, resource checks, queue conditions, and target state are direct.

Calling the combined gate “authorization” is an AEGIS systems abstraction.

This distinction matters:

```text
CAN-TRAIN
≠
formal authorization object
```

## 3.6 Command success

**Status:** E2 / forensic methodology.

Pass 80 correctly rejected:

```text
train command
=
completed unit
```

and established an evidence ladder from command observation through pending state, object birth, deployment, engagement, and battlefield effect.

This is methodology, not a historical API contract.

## 3.7 Failure taxonomy F1–F8

**Status:** E2.

The classes are useful engineering/forensic categories:

```text
opportunity
resource
action producer
queue
temporal
target invalidation
partial progress
evidence ambiguity
```

They are not AoE2 engine error codes.

---

# 4. Same-pass state visibility audit

Pass 85 deliberately narrowed this claim.

The safe hierarchy is:

```text
H1 state is mutated                    → E0
H2 later logic depends on shared state → E0/E1
H3 same-pass visibility                → high-confidence operational model
H4 same-pass successor eligibility    → conditional E1
H5 atomic ownership transfer          → E3
```

This is the correct stopping point.

The temptation to promote H3 into a formal engine scheduling specification must be resisted.

A future runtime experiment could strengthen H3/H4, but it is not required to preserve the architectural boundary.

---

# 5. Two clocks survive hostile audit

The controller/world distinction is one of the most important findings and survives review.

## Controller clock

```text
RULE
↓
GOAL/SN/FLAG/TIMER STATE
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
WORLD EFFECT
↓
OBSERVATION
```

Therefore:

```text
controller state change
≠
world completion
```

This distinction prevents several false conclusions, especially around production and research.

---

# 6. Production semantics audit

The strongest production model remains:

```text
CAPABILITY DEMAND
↓
RESOURCE / COMMITMENT GATE
↓
AFFORDABILITY / CAN-TRAIN
↓
PRODUCER ELIGIBILITY
↓
TRAIN REQUEST
↓
QUEUE / PENDING
↓
COMPLETION
↓
DEPLOYMENT
↓
BATTLEFIELD EFFECT
```

Each edge requires different evidence.

The following implications are rejected:

```text
can-train → train accepted
train → queued object
queued object → completed object
completed object → deployed object
deployed object → combat effect
```

The correct evidence hierarchy remains:

```text
exact object ID
>
producer/actor + operation
>
type + time + spatial correlation
>
aggregate temporal correlation
>
heuristic inference
```

This is forensic methodology, not a claim that the engine exposes all levels equally.

---

# 7. Exact-ID branch audit

The exact-ID archaeology conducted in Passes 75–79 remains correctly downgraded.

The accumulated evidence distinguishes:

```text
I1 model allocator slot
I2 world/entity map key
I3 model Ref target
I4 Entity.id
I5 MakeObjectAction.obj_id
I6a Command.Make.objId
I6b Command.Make.uniqueId
```

The audit rejects the following unproven joins:

```text
uniqueId == Entity.id
objId == Entity.id
uniqueId == objId
model allocator ID == world object ID
```

This branch remains optional forensic enhancement rather than a prerequisite for meaningful aggregate production observability.

That conclusion is strengthened, not weakened, by the later production-observability work.

---

# 8. Failure/recovery audit

Passes 83–84 established subsystem-specific recovery patterns.

Safe statement:

> Historical AI contains local feedback and recovery behaviors in multiple subsystems.

Unsafe statement:

> Historical AI has a universal exception-management framework.

The latter remains E3 / rejected.

The recovery dispositions can be normalized as:

```text
RETAIN
ADJUST
RELEASE / RE-ARBITRATE
```

but those labels are AEGIS terminology for a family of historical patterns.

---

# 9. Objective validity vs execution feasibility

This distinction survives and should become a permanent architecture invariant.

```text
OBJECTIVE VALIDITY
=
Does the strategic reason still exist?

EXECUTION FEASIBILITY
=
Can the chosen action execute now?
```

Therefore:

```text
VALID + INFEASIBLE → wait / adjust / alternate path
VALID + FEASIBLE   → execute
INVALID            → release / replace / re-arbitrate
```

This is an AEGIS conceptual distinction, but it is strongly grounded in the observed separation between strategic state and local execution gates.

It prevents a serious control error:

> treating temporary inability to execute as evidence that the strategic objective has become invalid.

---

# 10. Starvation claim audit

The project has previously distinguished three propositions.

### S1 — procedural suppression exists

**Supported.**

Resource consumption and resource-control gating can suppress later actions.

### S2 — persistent ineffective commitment can continue suppressing alternatives

**Structurally supported as an AEGIS model; historical occurrence not universally demonstrated.**

### S3 — historical AI systematically starves objectives

**Not proven.**

The distinction must remain explicit.

A structural mechanism is not an observed frequency distribution.

---

# 11. Fairness claim audit

No universal historical mechanism has been recovered for:

```text
waiting-time aging
round robin
minimum resource share
maximum commitment age
forced release after N failures
```

Safe statement:

> No universal fairness mechanism has been recovered from the inspected historical corpus.

Unsafe statement:

> Historical HD has no fairness anywhere.

The latter is an unjustified universal negative.

This is an important correction to the wording of prior negative research.

---

# 12. Negative research claims require bounded scope

A negative finding has three dimensions:

```text
SEARCH SCOPE
SEARCH METHOD
VERSION / SOURCE SCOPE
```

Therefore every negative claim should be expressed as:

> “Not recovered from the inspected corpus under the stated source/version/method scope.”

rather than:

> “Does not exist.”

This rule applies especially to:

- fairness;
- global optimizer;
- ownership transfer;
- universal failure manager;
- exact ID joins;
- hidden naval policy;
- generalized transition optimizer.

---

# 13. Contradiction audit: apparent contradictions that are not contradictions

Several project findings look contradictory until their semantic layer is separated.

## C1 — Rule order matters / rules are conditional

Not contradictory.

```text
rule order matters
+
not every earlier rule is effective
=
first effective path
```

## C2 — Resource control behaves like a reservation / it is not a formal lock

Not contradictory.

Operational behavior can resemble reservation without establishing a formal lock primitive.

## C3 — State is visible / world action is asynchronous

Not contradictory.

Controller state and world state operate on different clocks.

## C4 — Release enables competition / release is not ownership transfer

Not contradictory.

Reopening a policy gate is weaker than transferring ownership.

## C5 — Failure causes retry / failure does not always cause retry

Not contradictory.

Historical recovery is conditional and subsystem-specific.

## C6 — Exact IDs are useful / exact IDs are not required

Not contradictory.

Exact IDs improve forensic confidence but aggregate observability can answer many production questions without them.

## C7 — Historical AI has priority / no universal numeric priority exists

Not contradictory.

Procedural priority can emerge without an explicit utility scalar.

---

# 14. Version-drift audit

Any engine behavior involving:

```text
queue semantics
pending objects
can-train
up-can-train
up-train
training queue controls
research queue controls
timers
extended strategic numbers
goal ranges
unit-line handling
```

must be treated as **version-sensitive** unless anchored to a specific build or official documentation.

The project already has direct evidence that AoE2DE updates changed AI queue semantics and pending-object behavior.

Therefore historical source alone cannot safely establish current-build semantics.

The rule is:

```text
historical source
→ historical behavior claim

current official documentation / controlled runtime
→ current behavior claim

cross-version equivalence
→ requires evidence
```

This is a major protection against accidental transplantation of old semantics into the future AEGIS runtime.

---

# 15. Replay evidence audit

Replay evidence is strong for recorded events but weak for hidden controller state unless that state is directly recoverable.

A replay can establish:

```text
recorded command occurred
recorded object/event exists
recorded temporal ordering
```

It cannot automatically establish:

```text
hidden SN value
hidden goal value
historical rule that caused the command
causal intent
counter-selection reason
```

Therefore the C1-B Byzantine camel/knight corroboration remains:

```text
TEMPORAL CORROBORATION
```

not:

```text
CAUSAL POLICY PROOF
```

This distinction must remain permanent.

---

# 16. Parser/interpreter audit

The replay interpreter's inability to promote W1/W2/W3 evidence must not be mistaken for evidence that the game did not perform the transition.

Current forensic rule:

```text
parser uncertainty
≠
gameplay failure
```

This is particularly important because the interpreter has parser-known-but-not-yet-supported actions.

Unsupported decoding reduces evidence quality; it does not create a negative gameplay observation.

---

# 17. Byzantine archaeology audit

The Byzantine response chain remains defensible at the historical substrate level:

```text
ENEMY MOUNTED PRESSURE
↓
CAVALRY THREAT AGGREGATION
↓
CAMEL-RELATED RESPONSE CONDITIONS
↓
RESOURCE / FEASIBILITY GATES
↓
TRAIN CAMEL
```

But the following stronger propositions remain unproven:

```text
infantry density → Cataphract utility optimizer
Cataphract → Elite → Logistica as one explicit transition chain
explicit building HP strategic optimizer
free-vision policy as generalized strategic objective
probabilistic belief model
universal composition optimizer
current naval policy as historical AI policy
```

The distinction between:

```text
CATAPHRACT = cavalry mechanically
CATAPHRACT = anti-infantry strategically
```

remains useful AEGIS analysis, not proof of historical utility scoring.

---

# 18. Architecture contamination audit

This is the most important hostile-QC category.

The following are **AEGIS requirements**, not recovered HD features:

```text
explicit candidate generation
utility scoring
opportunity cost
risk scoring
tempo scoring
option value
belief confidence
information value
staleness model
explicit commitment ownership
generation/version tokens
bounded retry policy
bounded retention policy
universal postcondition contracts
explicit fairness / starvation protection
```

These may be excellent engineering decisions.

They must never be written in documentation as though historical HD implemented them.

The correct phrasing is:

> “Historical evidence motivates / constrains this AEGIS design.”

not:

> “HD implements this AEGIS mechanism.”

---

# 19. The historical substrate / AEGIS layer boundary

The audit confirms this is currently the cleanest architecture boundary.

## Historical substrate

```text
ENGINE FACTS
GOALS
STRATEGIC NUMBERS
FLAGS
TIMERS
RULES
CONTROL FLOW
RESOURCE STATE
QUEUE STATE
COMMANDS
WORLD OBSERVATIONS
LOCAL RECOVERY
```

## AEGIS strategic layer

```text
BELIEF
OBJECTIVE MODEL
CANDIDATE GENERATION
UTILITY
RISK
OPPORTUNITY COST
TEMPO
OPTION VALUE
FAIRNESS
COMMITMENT OWNERSHIP
RECOVERY POLICY
```

The bridge should eventually be explicit:

```text
AEGIS INTENT
↓
HD-COMPATIBLE AUTHORIZATION / STATE
↓
COMMAND
↓
OBSERVABLE WORLD EFFECT
↓
AEGIS VERIFICATION
```

---

# 20. Evidence provenance minimum standard

Every future archaeological claim should carry, at minimum:

```text
CLAIM ID
SOURCE ARTIFACT
SOURCE TYPE
VERSION / BUILD
LOCATION / ANCHOR
OBSERVED TEXT / BEHAVIOR
EVIDENCE GRADE
INTERPRETATION
ALTERNATIVE EXPLANATIONS
OPEN EDGE
```

Recommended evidence grades:

```text
E0 DIRECT
E1 STRONG OPERATIONAL INFERENCE
E2 AEGIS GENERALIZATION
E3 HYPOTHESIS / OPEN
```

The existing project documents use multiple naming conventions such as DIRECT, STRONG OPERATIONAL MODEL, AEGIS-GENERALIZATION, and NOT PROVEN. Future audit work should normalize these labels.

---

# 21. Claim conversion rule

A historical observation may be promoted only through explicit reasoning.

```text
OBSERVATION
↓
LOCAL INTERPRETATION
↓
CROSS-SOURCE CORROBORATION
↓
ALTERNATIVE-EXPLANATION CHECK
↓
EVIDENCE GRADE
↓
ARCHITECTURAL CONSEQUENCE
```

Never:

```text
interesting behavior
↓
architectural feature
```

without the intermediate evidence steps.

---

# 22. Three kinds of “proof” must remain separate

## Behavioral proof

The system demonstrably did something.

Example:

```text
camel queue action recorded
```

## Causal proof

The evidence establishes why it did it.

Example:

```text
camel production was triggered specifically by cavalry-pressure state
```

## Architectural proof

The evidence establishes the general mechanism that produced the behavior.

Example:

```text
universal threat-response optimizer exists
```

These are progressively stronger claims.

Most replay corroboration currently reaches behavioral proof but not causal proof.

Most historical code archaeology reaches local architectural proof but not proof of a universal architecture.

---

# 23. Temporal ordering is not causal ordering

This principle deserves permanent status.

Given:

```text
A occurs before B
```

we may establish:

```text
A < B in time
```

We may not automatically establish:

```text
A caused B
```

For the Byzantine replay evidence:

```text
enemy knight production
↓
Byzantine camel production
```

is temporal corroboration.

It does not prove:

```text
knight production
→
hidden cavalry threat sensor
→
traincamel
```

unless the hidden state or causal chain is separately recovered.

---

# 24. Source hierarchy

For future claims, the preferred hierarchy is:

```text
1. Official engine documentation / patch notes
2. Controlled current-build runtime measurement
3. Exact historical source artifact with version provenance
4. Replay-derived direct observation
5. Public historical/community code corroboration
6. Analytical inference
7. Heuristic hypothesis
```

Lower-level sources can be highly useful, but should not silently outrank direct authoritative evidence.

Community examples are corroboration, not authoritative proof of proprietary engine internals.

---

# 25. What is actually closed after Pass 86

The following Layer-2 questions can now be treated as **methodologically closed**:

### A — Procedural economic arbitration

```text
RULE ORDER
+
ELIGIBILITY
+
STATE
+
RESOURCE CONSUMPTION
→
FIRST EFFECTIVE PATH
```

### B — Commitment lifecycle

```text
SELECT
→
PROTECT
→
EXECUTE
→
PROGRESS
→
RELEASE / RESET / REPLACE
```

### C — Failure feedback

```text
ATTEMPT
→
POSTCONDITION
→
SUCCESS / PARTIAL / FAILURE
→
LOCAL RECOVERY
```

### D — Recovery arbitration

```text
FAILURE
→
VALIDITY / FEASIBILITY
→
RETAIN / ADJUST / RELEASE
→
RE-ARBITRATE
```

### E — Same-pass boundary

```text
SHARED STATE VISIBILITY
→
SUPPORTED OPERATIONAL MODEL

ATOMIC OWNERSHIP HANDOFF
→
NOT PROVEN
```

### F — Production observability

```text
COMMAND
≠
QUEUE
≠
COMPLETION
≠
DEPLOYMENT
≠
EFFECT
```

### G — Exact identity

```text
USEFUL
but
NOT FOUNDATIONAL
```

---

# 26. What remains open

The audit identifies only a small number of high-value open questions.

## O1 — Current-build runtime confirmation

Some semantics remain version-sensitive and should eventually be measured on the actual target build.

## O2 — Complete provenance normalization

Existing archaeology should eventually be assigned consistent E0–E3 grades and exact source anchors.

## O3 — Contradiction matrix

A formal machine-readable matrix linking claims, sources, versions, and contradictory observations would improve auditability.

## O4 — Layer-3 translation

The next major engineering step is converting the historical substrate constraints into an explicit AEGIS architecture without importing historical assumptions as facts.

None of O1–O3 currently invalidates the Layer-2 conceptual closure.

---

# 27. Hostile QC verdict

### Survives

- procedural arbitration;
- stateful resource gating;
- distributed commitment patterns;
- local failure recovery;
- conditional release/retention;
- separation of controller and world clocks;
- production evidence ladder;
- exact-ID downgrade;
- historical/AEGIS architectural separation.

### Requires narrower wording

- same-pass visibility;
- fairness negatives;
- starvation conclusions;
- “authorization” terminology;
- “commitment” terminology;
- universal failure semantics;
- negative claims about hidden systems.

### Rejected as historical facts

- universal argmax optimizer;
- universal fairness scheduler;
- universal exception manager;
- formal commitment ownership;
- atomic historical handoff;
- `uniqueId == Entity.id` without further proof;
- replay temporal order as causal proof;
- parser failure as gameplay failure.

---

# 28. Final audit doctrine

The project should adopt the following permanent rule:

> **Do not ask only “is this plausible?” Ask “what is the strongest claim the evidence actually permits?”**

And then:

```text
STRONGEST SUPPORTED CLAIM
↓
NO STRONGER
```

This prevents both failure modes that threaten a reverse-engineering project:

```text
UNDERCLAIMING
= missing useful architecture

OVERCLAIMING
= building on invented engine semantics
```

The objective is not maximum certainty language.

The objective is **maximum defensible information**.

---

# 29. Disposition

Pass 86 completes the first hostile cross-pass audit of the execution/commitment/recovery research chain.

The audit finds no foundational contradiction among Passes 80–85.

The main corrective action is epistemic rather than architectural:

```text
HISTORICAL FACT
≠
OPERATIONAL INFERENCE
≠
AEGIS GENERALIZATION
≠
HYPOTHESIS
```

These categories must remain visible in all future artifacts.

The project is now in a strong position to move from **“discover the substrate”** toward **“formalize the architecture.”**

Before Layer 3 implementation, however, one particularly valuable audit remains: convert the accumulated findings into a **single end-to-end evidence graph** and test whether every major AEGIS architectural requirement has a traceable historical motivation, a current-engine constraint, or an explicitly labeled design decision.

That is the next high-value pass.

---

# 30. Layer status

**Layer 1:** 89%; scenario automation remains retired.  
**Layer 2:** ~99%+; foundational execution/commitment/recovery semantics audited; remaining work is provenance normalization and final evidence-graph closure.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

## Pass 86 conclusion

The archaeology survives hostile review because the strongest findings do not depend on pretending that AEGIS concepts were historical HD features.

The historical system can defensibly be characterized as a distributed procedural controller using facts, mutable state, ordered conditional rules, resource effects, world observations, and local recovery.

AEGIS can improve this substrate by making strategic valuation, commitment ownership, postconditions, bounded recovery, fairness, and evidence handling explicit—but those are **AEGIS engineering decisions**.

That boundary is now a formal project invariant.