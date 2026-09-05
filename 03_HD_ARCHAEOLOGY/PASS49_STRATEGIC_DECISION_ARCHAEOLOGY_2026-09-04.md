# AEGIS Layer 2 — Pass 49
# Strategic Decision Archaeology

**Date:** 2026-09-04  
**Layer:** 2 — research / archaeology only  
**Predecessors:** Pass 48 — player-strategy ↔ HD-AI semantic bridge; Pass 47 — Cataphract role archaeology  
**Status:** PASS — decision decomposition established; historical implementation coverage mapped; strategic gaps remain explicit  
**Implementation:** **ZERO** — no `.per`, no controller, no production policy, no runtime deployment

---

## 0. Mission

Pass 49 changes the central archaeological question.

Earlier passes primarily asked:

> **What does this rule, variable, or subsystem do?**

This pass asks:

> **What decision problem is the rule network solving, what information does it require, what state does it maintain, what authority does it exercise, and what remains outside the historical implementation?**

The objective is to bridge expert AoE2 player reasoning to historical HD AI semantics without falsely equating human concepts with engine variables.

The canonical decision chain is:

```text
GAME WORLD
↓
OBSERVABLE STATE
↓
OBSERVATION
↓
KNOWN FACTS + UNCERTAINTY
↓
BELIEF STATE
↓
STRATEGIC ASSESSMENT
↓
OBJECTIVE
↓
REQUIRED CAPABILITY
↓
CANDIDATE SET
↓
HARD CONSTRAINTS
↓
SOFT EVALUATION
↓
COST + RISK + OPTION VALUE
↓
COMMITMENT
↓
AUTHORITY
↓
ACTION
↓
WORLD EFFECT
↓
VERIFICATION
↓
SUCCESS / FAILURE
↓
BELIEF UPDATE
↓
REASSESSMENT
```

This is an **AEGIS analytical model**, not a claim that historical HD AI internally implemented this formal pipeline.

---

# 1. Evidence discipline

This pass uses the following evidence grades:

- **DIRECT** — directly established by source code, installed data, replay evidence, or authoritative engine documentation.
- **COMPOSED** — relationship established by joining multiple DIRECT facts.
- **INFERRED** — strategic interpretation that is plausible but not explicitly encoded.
- **AEGIS-GENERALIZATION** — analytical abstraction proposed for future architecture; not historical fact.
- **UNCERTAIN** — evidence insufficient to close the claim.
- **DISPROVEN** — tempting interpretation contradicted by available evidence.

Historical intent must not be inferred merely because a rule's effect appears strategically sensible.

A second distinction is mandatory:

```text
MECHANICAL FACT
≠
PLAYER KNOWLEDGE
≠
PLAYER INFERENCE
≠
AI OBSERVATION
≠
AI STATE
≠
AI POLICY
≠
ENGINE ACTION
≠
WORLD OUTCOME
```

The public AI Scripting Encyclopedia confirms that AI scripting is organized around rules containing facts and actions, with goals and strategic numbers available as state/value channels and typed operators controlling how values are interpreted. citeturn0search0turn0search6turn0search9

---

# 2. The decision problem

Expert player strategy can be represented as repeated selection among feasible actions under changing constraints.

At any decision point:

```text
CURRENT STATE
+
UNCERTAINTY
+
OBJECTIVE PRIORITIES
+
AVAILABLE CAPABILITIES
+
RESOURCE / TIME / MAP CONSTRAINTS
+
OPPONENT MODEL
        ↓
CANDIDATE ACTIONS
        ↓
EVALUATION
        ↓
COMMITMENT
```

AoE2 makes this unusually difficult because resources, technology, production, position, information, and military composition are coupled. A decision that is locally efficient can be strategically poor if it consumes the resources or time required for the next critical response.

The research consequence is:

> A strategic decision should not be represented by its final command alone. The archaeological unit is the **decision chain** that makes the command intelligible.

---

# 3. Decision Atlas — Scout Enemy

## 3.1 Player problem

The player does not scout merely to move a scout. The strategic problem is:

```text
UNKNOWN ENEMY STATE
→ acquire useful information
→ reduce uncertainty
→ improve downstream decisions
```

Typical questions include:

- What age is the opponent entering?
- What military production exists?
- Which resources are exposed?
- Is a forward structure appearing?
- Is the opponent committing to cavalry, ranged units, infantry, siege, or economy?

The official AoE2 guidance explicitly frames scouting as discovering the map, resources, and opponent, and notes that enemy buildings/resources can reveal strategy. This supports the strategic importance of information acquisition. 

**Evidence grade:** DIRECT for scouting purpose as documented game guidance; COMPOSED for its role in downstream decision quality.

## 3.2 Historical HD representation

Historical `scoutcontrol.per` contains scout groups, geometry, path analysis, dangerous local units/buildings, archers/spears/TCs, candidate pivots, movement-point evaluation, and movement commands.

This establishes a substantial control chain:

```text
SCOUT CONTROL STATE
→ ROUTE / POINT CANDIDATES
→ GEOMETRIC / SAFETY CONDITIONS
→ MOVEMENT COMMAND
```

**Evidence:** DIRECT for control mechanisms; COMPOSED for interpretation as information acquisition under movement constraints.

## 3.3 Missing semantic layer

Historical evidence does not establish a general explicit value-of-information calculation.

The stronger AEGIS abstraction is:

```text
TARGET INFORMATION
→ INFORMATION VALUE
→ ROUTE CANDIDATES
→ SAFETY CONSTRAINTS
→ EXPECTED INFORMATION GAIN
→ COST / RISK
→ ROUTE COMMITMENT
→ OBSERVE
→ UPDATE BELIEF
```

This is **AEGIS-GENERALIZATION**, not historical implementation evidence.

## 3.4 Decision verdict

**Historical implementation coverage: PARTIAL-STRONG.**

The HD system clearly contains sophisticated scouting control. It does not prove an explicit generalized uncertainty model or value-of-information optimizer.

---

# 4. Decision Atlas — Detect Cavalry

## 4.1 Player problem

The player needs to transform observations into a threat assessment:

```text
OBSERVED ENEMY UNITS
→ CLASSIFY
→ AGGREGATE
→ DETERMINE WHETHER MOUNTED PRESSURE IS MATERIAL
```

The critical distinction is:

```text
UNIT OBSERVATION
≠
THREAT ASSESSMENT
```

A single knight and a massed cavalry army may trigger radically different decisions.

## 4.2 Historical HD representation

Historical `threats.per` aggregates enemy mounted categories into strategic-number channels, including cavalry and cavalry-archer categories. The archaeology also identified context-sensitive use of these aggregates in production logic.

Historical state can therefore be summarized as:

```text
ENEMY OBSERVATION
→ CLASSIFICATION
→ AGGREGATION
→ THREAT STATE
```

**Evidence:** DIRECT for aggregate threat channels; COMPOSED for the observation→classification interpretation.

The public AI reference documents strategic numbers as engine state/control values, not human-semantic beliefs. citeturn0search9turn0search8

## 4.3 Important correction: aggregate ≠ belief

A threat strategic number is not automatically a probabilistic belief.

The historical system can represent:

```text
cavalry = observed / derived aggregate
```

without representing:

```text
P(cavalry strategy | observations)
```

Therefore:

**Historical belief model:** NOT ESTABLISHED.

**Historical threat-state model:** DIRECT.

## 4.4 AEGIS bridge

```text
OBSERVATION
→ HYPOTHESES
→ CONFIDENCE
→ EXPECTED CONSEQUENCES
→ INFORMATION VALUE
```

This is a future analytical model, not a historical claim.

---

# 5. Decision Atlas — Counter Cavalry

## 5.1 Player problem

The real player question is not:

> “What counters cavalry?”

It is:

> “Given the enemy mounted threat, what feasible response best protects or advances my current objective?”

Candidate response classes may include:

```text
SPEAR-LINE
CAMEL-LINE
STATIC DEFENSE
MONK / CONTROL
OWN CAVALRY
RANGED SUPPORT
SIEGE SUPPORT
POSITIONAL RESPONSE
MIXED COMPOSITION
```

The exact best choice depends on the state.

## 5.2 Historical HD representation

Historical archaeology established a strong threat→capability chain:

```text
ENEMY THREAT
→ THREAT AGGREGATE
→ CONTEXTUAL PRODUCTION RULE
→ FEASIBILITY CONDITIONS
→ PRODUCTION
```

`units.per` contains `traincamel` logic conditioned by threat state and production/resource feasibility. Historical `threats.per` establishes cavalry/cavalry-archer aggregates and `camel-set` establishes own camel capability state.

This proves that historical HD AI can map detected mounted pressure into a counter-capability production response.

**Evidence:** DIRECT/COMPOSED.

## 5.3 What is not proven

The evidence does **not** establish a universal optimizer comparing all counter classes by a common objective function.

It does not prove that the AI evaluates:

```text
CAMEL vs SPEAR vs MONK vs DEFENSE
```

as a single candidate set with explicit multi-dimensional scoring.

It also does not prove that a production response is always strategically successful.

## 5.4 Decision verdict

**Historical implementation coverage: STRONG for selected threat→counter chains; PARTIAL for general counter selection.**

This distinction is central to the project.

---

# 6. Decision Atlas — Age Up

## 6.1 Player problem

Age advancement is a resource-and-timing decision, not merely a technology command.

The player balances:

```text
AGE-UP BENEFIT
vs
MILITARY INVESTMENT
vs
ECONOMIC INVESTMENT
vs
IMMEDIATE SURVIVAL
vs
TIMING / TEMPO
```

The official match guidance explicitly presents Feudal pressure and Castle Age progression as situation-dependent goals rather than a universally fixed timing. 

## 6.2 Historical HD representation

Historical AI scripts contain age-state constants, age transitions, resource allocation, escrow, technology research, and conditional production/building logic.

Escrow archaeology gives a particularly important control pattern:

```text
ESCROW STATE
→ CAN-RESEARCH-WITH-ESCROW
→ RESEARCH
→ CONTROLLER STATE UPDATE
```

This supports the historical idea that resources can be protected for a future capability rather than consumed indiscriminately.

The public scripting reference also documents the role of goals, strategic numbers, and facts/actions in rule execution. citeturn0search6turn0search9

## 6.3 Missing semantic layer

Historical evidence does not prove an explicit long-horizon expected-value comparison such as:

```text
VALUE OF CASTLE AGE
-
VALUE OF 3 MORE MILITARY UNITS NOW
```

It demonstrates resource reservation and conditional authorization, but not a universal formal opportunity-cost optimizer.

## 6.4 Decision verdict

**Historical implementation coverage: STRONG control evidence; PARTIAL strategic-evaluation evidence.**

---

# 7. Decision Atlas — Attack

## 7.1 Player problem

An attack decision contains at least:

```text
CAN I ATTACK?
WHERE?
WITH WHAT?
AGAINST WHAT?
WHEN?
WHAT IF THE TARGET IS FORTIFIED?
WHAT IF THE ATTACK FAILS?
```

This is a commitment decision, not merely an attack command.

## 7.2 Historical HD representation

Historical attack state includes:

- `attack-goal`
- `attack-status-goal`
- `retreat-now-goal`
- `restart-attack-goal`
- attack timers
- fortification state
- military/siege conditions
- target/search state

Historical chains can therefore be represented as:

```text
MILITARY / MAP STATE
→ ATTACK CONDITIONS
→ ATTACK STATE
→ ATTACK COMMAND / GROUP CONTROL
→ OBSERVED STATE
```

**Evidence:** DIRECT/COMPOSED.

## 7.3 Commitment interpretation

Attack-state goals are evidence of explicit persistent control state. They are not proof of a human-like internal “attack intention” in the cognitive sense.

The safer terminology is:

> **engine-level attack commitment/control state.**

## 7.4 Decision verdict

**Historical implementation coverage: STRONG for attack lifecycle control; PARTIAL for strategic target valuation.**

---

# 8. Decision Atlas — Retreat

## 8.1 Player problem

Retreat is not simply reversing movement. The player must determine:

```text
IS THE CURRENT ENGAGEMENT NEGATIVE?
IS PRESERVING THE ARMY MORE VALUABLE?
IS THE POSITION UNSAFE?
SHOULD THE ATTACK BE ABORTED OR TEMPORARILY PAUSED?
WHEN SHOULD THE ATTACK BE RECONSIDERED?
```

## 8.2 Historical HD representation

Historical archaeology found:

```text
retreat-now-goal
attack-status-goal
restart-attack-goal
enemy-fortifications-goal
attack timers
```

Triggers include fortification and military-condition checks. Retreat can alter attack state, clear attack behavior, enable timers, and later allow restart logic.

This provides a strong lifecycle:

```text
ATTACK
→ NEGATIVE / BLOCKED CONDITION
→ RETREAT STATE
→ RECOVERY / TIMER
→ REASSESS
→ POSSIBLE RESTART
```

**Evidence:** DIRECT for state/control chain; COMPOSED for lifecycle interpretation.

## 8.3 Critical limitation

Replay archaeology explicitly preserves uncertainty where action→world-state transitions cannot be proven. A retreat command therefore cannot automatically be labeled successful retreat, army preservation, or strategic success.

**Decision verdict:** STRONG controller evidence; world-outcome evidence remains bounded.

---

# 9. Decision Atlas — Transition

## 9.1 Player problem

A strategic transition occurs when the current capability set is no longer sufficient or when a new capability offers greater strategic value.

Canonical decomposition:

```text
CURRENT COMMITMENT
→ NEW THREAT / OBJECTIVE
→ REQUIRED CAPABILITY
→ CURRENT CAPABILITY
→ GAP
→ ALTERNATIVE TRANSITIONS
→ TRANSITION COST
→ TIMING
→ RISK
→ OPTIONALITY
→ DECISION
```

## 9.2 Transition cost

Pass 45 established that transition cost cannot be reduced to the next unit's resource price.

At minimum:

```text
UNIT COST
+ TECH COST
+ INFRASTRUCTURE COST
+ DISPLACED PRODUCTION
+ ECONOMIC REALLOCATION
+ TIMING LOSS
+ LOST MOMENTUM
+ RISK
```

This is an AEGIS research abstraction. It is not claimed as a historical explicit scalar in HD AI.

## 9.3 Historical HD representation

Historical scripts clearly contain:

- research authorization,
- production feasibility,
- escrow/resource protection,
- production state,
- age transitions,
- attack reset/restart behavior,
- contextual threat responses.

These are ingredients of transition control.

What remains unproven is a general historical optimizer that explicitly enumerates all feasible transitions and compares their complete opportunity costs.

## 9.4 Decision verdict

**Historical implementation coverage: PARTIAL.**

Historical AI has many transition mechanisms. A universal transition evaluator is **NOT ESTABLISHED**.

---

# 10. Decision Atlas — Recommit

## 10.1 Player problem

Recommitment asks whether a previously abandoned plan should become viable again after state changes.

Examples:

```text
RETREAT
→ ARMY RECOVERS
→ THREAT CHANGES
→ SIEGE ARRIVES
→ RECOMMIT
```

or:

```text
CAVALRY PRESSURE
→ COUNTER MASS BUILT
→ ENEMY THREAT WEAKENS
→ ATTACK WINDOW REOPENS
```

## 10.2 Historical HD representation

Historical restart-attack state and timers provide strong evidence for controller re-entry:

```text
ATTACK STATE
→ RESET / RETREAT
→ TIMER / RECOVERY
→ RESTART CONDITION
→ ATTACK STATE RE-ENTRY
```

The historical `increase-town-size-goal → maximum-town-size threshold → restart-attack-goal` chain is a concrete example of state-driven re-entry logic.

**Evidence:** DIRECT/COMPOSED.

## 10.3 Missing semantic layer

Historical evidence does not establish a generalized sunk-cost or commitment-strength model.

AEGIS therefore distinguishes:

```text
ENGINE RESTART CONDITION
≠
GENERAL COMMITMENT REVALUATION MODEL
```

---

# 11. Strategic Decision Atlas — consolidated matrix

| Decision | Player problem | Historical representation | Historical coverage | Missing capability |
|---|---|---|---|---|
| Scout enemy | reduce uncertainty / acquire useful information | scout groups, geometry, danger checks, movement | STRONG control / PARTIAL strategic valuation | explicit belief + value-of-information model |
| Detect cavalry | classify and assess mounted pressure | threat aggregates, cavalry/cavarcher channels | STRONG | explicit probabilistic belief / confidence |
| Counter cavalry | select feasible response capability | threat→camel production, feasibility gates | STRONG selected chains / PARTIAL general choice | common candidate optimizer across counter classes |
| Age up | trade immediate investment for future capability | age state, escrow, research, resource control | STRONG control / PARTIAL strategic evaluation | explicit opportunity-cost comparison |
| Attack | decide whether/where/how to commit force | attack state, search, target state, timers | STRONG lifecycle / PARTIAL valuation | generalized target-value model |
| Retreat | preserve force / abandon bad engagement / reset | retreat state, attack status, timers | STRONG lifecycle | explicit loss estimation / expected outcome |
| Transition | replace insufficient capability | research, production, escrow, state resets | PARTIAL | general transition optimizer |
| Recommit | determine when an abandoned plan becomes viable | restart goals, timers, state re-entry | STRONG selected lifecycle | generalized commitment / sunk-cost model |

This matrix is the principal Pass-49 research result.

---

# 12. What a “decision” actually contains

The archaeology now supports a more precise definition.

A strategic decision is not one variable and not one rule.

It is a **control chain** containing some subset of:

```text
OBSERVATION
→ REPRESENTATION
→ ASSESSMENT
→ OBJECTIVE
→ REQUIREMENT
→ CANDIDATE GENERATION
→ CONSTRAINT FILTER
→ EVALUATION
→ COMMITMENT
→ AUTHORITY
→ ACTION
→ WORLD EFFECT
→ VERIFICATION
→ FEEDBACK
```

Historical systems often implement only a subset.

For example:

```text
enemy cavalry
→ cavalry aggregate
→ camel production condition
→ can-train / resource gates
→ train camel
```

This is a real decision chain even if it does not contain an explicit probability distribution or general optimizer.

That is the correct middle ground between two errors:

```text
ERROR A: “HD is just dumb rules.”
ERROR B: “HD contains a full human-like strategic reasoner.”
```

The evidence supports neither extreme.

---

# 13. Decision authority model

A critical archaeological distinction is:

```text
DESIRE
→ CAN-FACT
→ AUTHORIZATION
→ SIDE-EFFECT COMMAND
→ PENDING WORLD CHANGE
→ POSTCONDITION
```

The public scripting reference explicitly distinguishes facts from actions: facts establish conditions for rule execution, while actions tell the AI to do something. citeturn0search6

Therefore a future research model must not collapse:

```text
can-train
```

into:

```text
trained
```

or:

```text
train
```

into:

```text
unit successfully deployed and survived
```

The replay interpreter work reinforces the same boundary: queued production is not automatically equivalent to a completed world transition.

---

# 14. Verification is part of the decision chain

A mature strategic loop is:

```text
DECIDE
→ ACT
→ OBSERVE RESULT
→ COMPARE EXPECTED / ACTUAL
→ UPDATE STATE
→ REASSESS
```

Historical AI has many mechanisms for re-entering controllers after timers, state changes, attack resets, production changes, and threat changes.

However, replay evidence does not establish that every command's intended postcondition was verified by a generalized success evaluator.

Therefore:

**Historical feedback loop:** DIRECT in selected controller chains; **generalized verification architecture:** NOT ESTABLISHED.

This is a major Layer-2→Layer-3 boundary.

---

# 15. Failure taxonomy

The decision archaeology exposes at least five different failure classes:

### 15.1 Perceptual / observation failure
The required state was not observed or was stale.

### 15.2 Representation failure
The relevant observation existed but was compressed into inadequate state.

### 15.3 Policy failure
The state was represented correctly but the selected response was strategically poor.

### 15.4 Authority / execution failure
The intended action could not be authorized, queued, or executed.

### 15.5 Outcome failure
The action executed but failed to achieve the strategic objective.

These must never be conflated.

Example:

```text
traincamel command issued
```

could fail because:

```text
NO AUTHORITY / FEASIBILITY
OR
QUEUE FAILURE
OR
UNIT NOT COMPLETED
OR
UNIT COMPLETED BUT LOST
OR
UNIT SURVIVED BUT DID NOT SOLVE THREAT
```

Each is a different failure class.

---

# 16. State model — historical vs AEGIS analytical

## Historical HD state

Evidence supports a distributed state system involving:

```text
goals
strategic numbers
flags
 timers
search state
target objects
target points
attack groups
production flags
resource allocation
age state
threat aggregates
```

The public reference confirms the engine has explicit goals, strategic numbers, timers, facts, and actions, with defined numeric limits. citeturn0search7turn0search8

## AEGIS analytical state

For future reasoning research, the state should be conceptualized as:

```text
ECONOMY
MILITARY
TECH
MAP
THREAT
INITIATIVE
CONFIDENCE
COMMITMENT
TEMPO
OPTIONALITY
CAPABILITY GAPS
INFORMATION QUALITY
```

This is **AEGIS-GENERALIZATION**.

It must not be retroactively projected onto historical variable names.

---

# 17. Hard constraints vs soft evaluation

One of the strongest findings from the Byzantine capability research is that candidate generation should be separated from candidate scoring.

### Hard constraints

```text
AGE
TECHNOLOGY
BUILDING
RESOURCE
POPULATION
TIME
MAP
TARGET COMPATIBILITY
```

A candidate failing a hard constraint should not be scored as if it were normally available.

### Soft evaluation

For feasible candidates, research may compare:

```text
RESOURCE EFFICIENCY
TRAIN RATE
COMBAT VALUE
SURVIVABILITY
MOBILITY
RANGE
TRANSITION COST
RISK
TIMING
OPTION VALUE
COMMITMENT REVERSIBILITY
```

This distinction is **AEGIS-GENERALIZATION**, supported by the demonstrated historical existence of feasibility gates and resource/technology checks but not itself proven as one unified historical evaluator.

---

# 18. Strategic optionality

The Pass-48 research introduced a useful definition:

```text
FEASIBLE RESPONSE SET
=
CAPABILITIES SURVIVING HARD-CONSTRAINT FILTERS
```

Optionality is therefore not simply “having many units.”

A player with:

```text
stable + barracks + monastery + castle + siege workshop
```

may have more feasible response classes than a player whose infrastructure and resources support only one branch.

However, more options also create competing investments and opportunity costs.

Thus:

```text
OPTIONALITY
→ FLEXIBILITY
+
COMPETING INVESTMENTS
+
DECISION COMPLEXITY
```

This is analytical, not historical engine semantics.

---

# 19. Commitment and reversibility

Strategic commitment should be separated from current military count.

Conceptually:

```text
COMMITMENT STRENGTH
≈
INVESTMENT
+
DEPENDENCIES
+
SUNK COST
+
CURRENT CAPABILITY
+
REVERSAL COST
```

This explains why:

```text
one completed building
```

may represent more strategic commitment than:

```text
one queued unit
```

and why a vertical upgrade can be less disruptive than a new-building transition.

Historical HD evidence contains reset/restart mechanisms and technology/production state, but does not establish this generalized commitment scalar.

**Status:** AEGIS-GENERALIZATION.

---

# 20. Temporal reasoning

Decision archaeology must distinguish:

```text
AVAILABILITY TIME
PRODUCTION TIME
RESEARCH TIME
CONSTRUCTION TIME
TRAVEL TIME
REINFORCEMENT TIME
REACTION TIME
OPPORTUNITY WINDOW
THREAT ARRIVAL TIME
STRATEGIC HORIZON
```

Historical timers provide direct evidence of temporal gating. The scripting reference documents timers as a finite engine resource, with 50 timer slots available. citeturn0search7

The strategic concept **tempo** is broader:

> the rate at which decisions, resources, production, and position become strategically relevant capability before opponent response.

That definition is **AEGIS-GENERALIZATION**.

---

# 21. Pressure vs initiative

These concepts must remain separate.

```text
PRESSURE
= forces or threatens a response

INITIATIVE
= ability to determine where/how the next meaningful interaction occurs
```

A unit can create pressure without controlling initiative.

Historical attack and threat state can represent pressure-related control conditions, but this pass does not claim that HD contains an explicit initiative scalar.

**Historical initiative model:** NOT ESTABLISHED.

---

# 22. Semantic closure

Pass 48 introduced **semantic closure** as the requirement that an intended strategic concept be traceable through the full control chain:

```text
OBSERVATION
→ REPRESENTATION
→ DECISION
→ AUTHORITY
→ ACTION
→ WORLD EFFECT
→ VERIFICATION
```

A chain is:

- **FULLY CLOSED** when each transition is evidenced;
- **PARTIALLY CLOSED** when one or more links remain inferred;
- **EXECUTION-AMBIGUOUS** when the command/world transition cannot be proven.

This is particularly important for replay archaeology.

A command record can prove:

```text
ACTION ISSUED
```

without proving:

```text
WORLD EFFECT
```

and a world effect can occur without proving:

```text
STRATEGIC INTENT
```

These distinctions are now mandatory.

---

# 23. Historical competence — corrected conclusion

The archaeology does **not** support the simplistic characterization that HD AI is merely a pile of isolated rules.

The source demonstrates a functioning controller with:

```text
threat detection
state aggregation
resource allocation
production feasibility
research authorization
attack lifecycle
retreat lifecycle
restart lifecycle
spatial scouting
search
persistent state
temporal gating
fallback behavior
```

That is evidence of real strategic competence.

At the same time, the evidence does not establish:

```text
universal candidate enumeration
probabilistic belief reasoning
explicit generalized opportunity-cost optimization
expert-level strategic generality
universal outcome verification
```

Therefore the disciplined conclusion is:

> **Historical HD AI provides substantial evidence of a functioning, competent strategic controller, but the available evidence does not establish expert-level generality, player-equivalent reasoning, or universal strategic success.**

This wording supersedes weaker or overly pessimistic interpretations.

---

# 24. Hostile QC — first investigation

### QC-1: Did we mistake goals for human concepts?
**Result:** PASS. Goals are treated as engine state channels; semantic interpretation remains separate.

### QC-2: Did we mistake facts for physical sensors?
**Result:** PASS. “Sensor” is retained only as an AEGIS abstraction; facts are engine-exposed queries/predicates.

### QC-3: Did we mistake threat aggregates for beliefs?
**Result:** PASS. Threat state is separated from probabilistic belief.

### QC-4: Did we mistake commands for outcomes?
**Result:** PASS. Action and world effect remain separate.

### QC-5: Did we infer strategic intent from sensible behavior?
**Result:** PASS. Historical intent is marked only where evidence warrants it.

### QC-6: Did we treat a counter relationship as an optimizer?
**Result:** PASS. Historical threat→camel production is strong evidence for selected response chains, not universal optimization.

### QC-7: Did we turn Cataphract's mechanical cavalry identity into strategic anti-cavalry classification?
**Result:** PASS. Pass 47 invariant preserved: mechanical family = cavalry; strategic role = anti-infantry. fileciteturn351file0

### QC-8: Did we collapse age-up, attack, retreat, and transition into one generic state?
**Result:** PASS. Each decision class has a separate problem definition and evidence profile.

### QC-9: Did we overclaim historical feedback verification?
**Result:** PASS. Re-entry and timer logic are distinguished from generalized outcome verification.

### QC-10: Did we accidentally implement Layer 2?
**Result:** PASS. No `.per`, controller, production policy, or runtime candidate is created.

---

# 25. Deepening pass — what is the real archaeological unit?

The first investigation suggests a major methodological refinement.

The correct unit of historical analysis is often not:

```text
ONE DEFRULE
```

but:

```text
CONTROL CHAIN
```

For example:

```text
THREAT DETECTION
→ THREAT AGGREGATION
→ RESOURCE / CAPABILITY STATE
→ PRODUCTION GATE
→ QUEUE ACTION
→ FUTURE STATE
```

A single rule may only represent one link.

Therefore future archaeology should trace **chain closure**, not merely count rules.

This is a significant methodological upgrade for AEGIS.

---

# 26. Deepening pass — candidate-set archaeology

A player decision generally implies a candidate set.

Historical HD frequently exposes candidate generation indirectly through alternative rule branches, unit families, production conditions, search candidates, or contextual paths.

But the existence of alternatives in code does not prove they were jointly enumerated and scored.

The correct evidence ladder is:

```text
ALTERNATIVE RULES EXIST
        ↓
MULTIPLE CAPABILITIES ARE REPRESENTED
        ↓
CONTEXT SELECTS AMONG THEM
        ↓
JOINT CANDIDATE ENUMERATION
        ↓
COMMON SCORING FUNCTION
        ↓
OPTIMALITY CLAIM
```

Only the first three are commonly supportable from historical rule archaeology.

The final two require direct evidence.

This prevents “many if-statements” from being mislabeled an optimizer.

---

# 27. Deepening pass — requirement extraction

The bridge from player reasoning to HD semantics is now best expressed as:

```text
PLAYER OBJECTIVE
↓
REQUIRED CAPABILITY
↓
CANDIDATE CAPABILITY SET
↓
HARD CONSTRAINTS
↓
HISTORICAL REPRESENTATION
```

Example:

```text
OBJECTIVE: survive cavalry pressure
        ↓
REQUIRED CAPABILITY: mounted-threat mitigation
        ↓
CANDIDATES: spear / camel / defense / control / mixed
        ↓
HARD CONSTRAINTS: age / resource / building / tech / time
        ↓
HISTORICAL REPRESENTATION: selected threat→production chains
```

This bridge is more faithful than trying to map:

```text
“counter cavalry” → one strategic number
```

because the player concept is broader than the engine representation.

---

# 28. Deepening pass — capability graph

The research now supports a reusable conceptual graph:

```text
THREAT
  ↓
REQUIRED CAPABILITY
  ↓
AVAILABLE PATHS
  ↓
FEASIBLE PATHS
  ↓
COST
  ↓
TIMING
  ↓
RISK
  ↓
CHOOSE
```

This graph is particularly important for Byzantine archaeology because the civilization has multiple overlapping capability families:

```text
anti-mounted
anti-infantry
anti-ranged
siege
control
naval
static defense
```

A future architecture should therefore select **capabilities**, not merely hard-code target→unit pairs.

**Status:** AEGIS-GENERALIZATION.

---

# 29. Deepening pass — information quality

Information should not be treated as permanently valid.

Conceptually:

```text
OBSERVATION
+
AGE SINCE CONFIRMATION
+
LAST CONFIRMATION
+
OPPONENT OPPORTUNITY TO CHANGE STATE
=
INFORMATION QUALITY
```

Historical scouting and timers provide mechanisms consistent with repeated observation, but a generalized information-decay model is not established historically.

**Status:** AEGIS-GENERALIZATION.

---

# 30. Deepening pass — decision horizon

Different decisions operate on different horizons:

```text
TACTICAL       = seconds
OPERATIONAL    = tens of seconds / minutes
STRATEGIC      = minutes
MACRO-STRATEGIC= age / game horizon
```

The same state can therefore produce different correct actions depending on horizon.

Example:

```text
SHORT HORIZON:
train immediate spear

LONG HORIZON:
protect gold and reach a stronger age/capability
```

Historical timers and age states provide temporal mechanisms, but a universal multi-horizon planner is not established.

---

# 31. Deepening pass — objective conflict

A strategic controller must often choose between competing objectives:

```text
SURVIVAL
vs
GROWTH

IMMEDIATE DEFENSE
vs
AGE-UP

MILITARY MASS
vs
ECONOMIC INFRASTRUCTURE

PRESSURE
vs
MAP SAFETY

COUNTER MASS
vs
TECHNOLOGY
```

Historical HD contains mechanisms that coordinate these domains, but the archaeology has not established one global utility function.

Therefore the safer historical model is:

> **distributed priority/control rules interacting across subsystems.**

This is stronger and more precise than calling the entire system a single finite-state machine or a single optimizer.

---

# 32. Final strategic decision model

Pass 49 establishes the following durable analytical model:

```text
OBSERVE
↓
REPRESENT
↓
ASSESS
↓
DEFINE OBJECTIVE
↓
DERIVE REQUIRED CAPABILITY
↓
GENERATE CANDIDATES
↓
FILTER HARD CONSTRAINTS
↓
EVALUATE FEASIBLE OPTIONS
↓
COMMIT
↓
AUTHORIZE
↓
ACT
↓
OBSERVE WORLD EFFECT
↓
VERIFY
↓
CLASSIFY RESULT
↓
UPDATE STATE / BELIEF
↓
REASSESS
```

Historical HD implements **subsets and chains** of this model, with particularly strong evidence for:

```text
OBSERVATION / FACTS
STATE AGGREGATION
FEASIBILITY GATES
RESOURCE / TECHNOLOGY CONTROL
PRODUCTION
ATTACK / RETREAT LIFECYCLES
TEMPORAL REASSESSMENT
```

The largest unresolved areas are:

```text
GENERAL BELIEF MODEL
GENERAL CANDIDATE ENUMERATION
COMMON MULTI-OBJECTIVE SCORING
EXPLICIT TRANSITION OPTIMIZATION
GENERAL OUTCOME VERIFICATION
EXPERT-LEVEL STRATEGIC GENERALITY
```

---

# 33. Layer-2 boundary declaration

This pass is strictly archaeological.

It contains:

- no `.per` implementation;
- no production rules;
- no controller;
- no runtime candidate;
- no deployment;
- no modification of stock AI;
- no Layer-3 architecture implementation.

The purpose is to establish what a strategic decision **means**, how historical HD AI represents pieces of that decision, and where the historical evidence stops.

---

# 34. Six-month re-entry test

A future engineer returning to this pass should be able to answer all of the following without reconstructing the research from scratch:

1. **What is the archaeological unit?** A control/decision chain, not necessarily one `defrule`.
2. **What is the canonical player decision pipeline?** Observe → represent → assess → objective → capability → candidates → constraints → evaluate → commit → authorize → act → verify → reassess.
3. **What does HD demonstrably do well?** Threat aggregation, feasibility gating, resource/technology control, production, attack/retreat lifecycle, temporal gating, and selected spatial/search behavior.
4. **Does a strategic number equal a human strategic concept?** No.
5. **Does a fact equal a physical sensor?** No; it is an engine-exposed query/predicate. “Sensor” is an AEGIS abstraction.
6. **Does a command prove a world outcome?** No.
7. **Does threat aggregation prove probabilistic belief?** No.
8. **Does threat→camel production prove a universal counter optimizer?** No; it proves a selected historical response chain.
9. **Does historical HD have meaningful strategic competence?** Yes, substantial evidence supports a functioning, competent controller.
10. **Does the evidence prove expert-level generality or player-equivalent reasoning?** No.
11. **What is the major methodological upgrade?** Trace semantic closure across control chains rather than interpreting isolated rules.
12. **What remains for later passes?** Byzantine-specific decision matrices, measured combat graphs, transition archaeology, and failure/feedback archaeology.
13. **Was Layer 2 implemented?** No. Implementation remains zero.

Failure of any answer indicates that the pass should be reopened.

---

# 35. Verdict

**PASS — STRATEGIC DECISION DECOMPOSITION ESTABLISHED.**

The central finding is:

> **Expert AoE2 strategy is best understood as repeated decision-making over changing capability, constraint, timing, positional, economic, and informational state. Historical HD AI implements meaningful portions of that process through distributed stateful rule chains, facts, feasibility gates, production/research controls, search, timers, and lifecycle state—but the evidence does not justify treating it as either a trivial rule pile or a complete human-equivalent strategic reasoner.**

The durable AEGIS bridge is:

```text
PLAYER SEMANTICS
↓
STRATEGIC ONTOLOGY
↓
STATE / BELIEF MODEL
↓
REQUIREMENT MODEL
↓
CONSTRAINT MODEL
↓
CANDIDATE GENERATION
↓
EVALUATION
↓
COMMITMENT
↓
HD REPRESENTATION
↓
ENGINE AUTHORITY
↓
ACTION
↓
WORLD VERIFICATION
```

**Pass 49 closes the general strategic-decision archaeology milestone.**

**Next research frontier:** Pass 50 — Byzantine Strategic Decision Matrix.
