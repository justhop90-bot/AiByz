# AoE2DE Cross-System Control Graph — Pass 12

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Predecessor:** `AOE2DE_CONSUMER_PROVENANCE_CLOSURE_PASS11_2026-09-04.md`  
**Status:** CROSS-SYSTEM CAUSAL NETWORK / WORKING CANON  
**Primary historical source:** verified `AI (HD version).per` + verified Promisory modules  
**Runtime authority:** Layer 1 current-build machine evidence  

---

# 0. Mission

Pass 11 closed several high-value downstream edges. Pass 12 changes scale.

The task is no longer to ask whether an isolated variable eventually reaches an action. The task is to reconstruct how the historical programmer connected major game domains into a distributed controller.

The target network is:

`ECONOMY → THREAT → PRODUCTION → TECHNOLOGY → MILITARY → MAP/POSITION → ATTACK → RECOVERY → ECONOMY`

This document does **not** claim that the historical AI contained a centralized planner. The evidence instead supports a distributed rule network whose modules exchange compact state channels and repeatedly convert game observations into eligibility, control state, search, actions, and resets.

---

# 1. Evidence contract

Every edge is classified on two independent axes.

## 1.1 Evidence grade

- **DIRECT:** exact executable source establishes the relationship.
- **COMPOSED:** multiple direct relationships establish the larger relationship.
- **INFERRED:** strategic interpretation reconstructed from repeated source behavior.
- **AEGIS-GENERALIZATION:** proposed architecture derived from the historical pattern.
- **UNCERTAIN:** insufficient evidence.

## 1.2 Closure level

- **CONTROL:** source state reaches a control/action consequence.
- **WORLD:** resulting game-state change is directly observed or otherwise source-proven.
- **STRATEGIC:** the intended game-level consequence is demonstrated rather than merely assumed.

A control-closed edge is not automatically world- or strategic-closed.

---

# 2. Canonical graph

```text
                         ┌──────────────┐
                         │   ECONOMY    │
                         └──────┬───────┘
                                │
                 resources / allocation / reserves
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
     TECHNOLOGY             PRODUCTION             THREAT
          │                     │                     │
          │                 capability               │
          │                     │                 composition
          └────────────┐        ▼                     │
                       ├──► MILITARY ◄────────────────┘
                       │        │
                       │        │ force / risk / attack state
                       │        ▼
                       │     ATTACK
                       │        │
                       │        │ retreat / pressure / reset
                       │        ▼
                       │     RECOVERY
                       │        │
                       └────────┴──────────► ECONOMY
                                ▲
                                │
                         MAP / POSITION
                                ▲
                                │
                             SCOUTING
                                ▲
                                │
                           INFORMATION
```

The diagram is conceptual. The executable implementation is distributed across modules, goals, strategic numbers, timers, search state, object data, and actions.

---

# 3. Edge ledger

| ID | From | To | State / signal | Writer | Reader / consumer | Guard / selection | Side effect | Timing / reset | Resource consequence | Capability consequence | Evidence | Closure |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G01 | Economy | Technology | age/research readiness | `escrow.per`, gatherer control | research rules | `can-research-with-escrow`, escrow flags | `research` | state later reset | resources reserved/consumed | new age/tech capability | COMPOSED | CONTROL |
| G02 | Economy | Economy | resource allocation regime | `gatherers.per` | gatherer rules | age, resource, military/building context | allocation changes | repeatedly reevaluated | changes income mix | changes future affordability | DIRECT/COMPOSED | CONTROL |
| G03 | Economy | Production | affordable production state | gatherer/escrow/resource logic | unit production | resource and `can-train` guards | train authorization | repeated | production spend | military stock | COMPOSED | CONTROL |
| G04 | Threat | Production | `cavarchers` weighted aggregate | `threats.per` | `units.per` | threshold + own state + food/camel limits | `traincamel yes` | lifecycle partly unresolved | commits food/gold capacity | camel capability | DIRECT | CONTROL |
| G05 | Threat | Technology | `cavarchers` threshold | `threats.per` | `researches.per` | camel-set/traincamel + research feasibility | camel research | repeated | research cost | upgraded camel capability | DIRECT | CONTROL |
| G06 | Production | Military | trained unit stock | unit production | military/attack systems | unit availability and group conditions | train actions | recurring | resource conversion | force capability | COMPOSED | CONTROL |
| G07 | Technology | Production | age/tech capability | `escrow.per` / research control | production rules | age/tech feasibility | enables unit/tech paths | lifecycle partly unresolved | research opportunity cost | unlocks production | COMPOSED | CONTROL |
| G08 | Threat | Military | enemy capability signal | `threats.per` / HD threat state | military response | thresholds / contextual conditions | response-state changes | repeated | redirects expenditure | counter-capability pressure | COMPOSED | CONTROL |
| G09 | Military | Attack | force / attack-group state | HD attack controller | attack/tactical rules | group size, target evaluation, timers | attack-group control | timer-driven | consumes military stock | pressure / denial | COMPOSED | CONTROL |
| G10 | Threat | Attack | fortification / defensive threat | HD threat conditions | retreat controller | castle/TC/tower/monk and military conditions | retreat state | timer/reset coupled | preserves remaining force | avoids bad engagement | COMPOSED | CONTROL |
| G11 | Attack | Recovery | retreat / failed attack state | HD attack controller | retreat/restart state | danger / building / attack conditions | `up-retreat-now`, reset state | explicit state reset | avoids further loss | preserves/rebuilds force | COMPOSED | CONTROL |
| G12 | Recovery | Attack | `restart-attack-goal` | HD controller | attack-group reset/restart | ally proximity, group count, town-size state | `up-reset-unit`, attack-group reset | explicit reset | changes production/attack posture | permits renewed attack control | DIRECT | CONTROL |
| G13 | Map | Scouting | spatial relationship | scout controller | scout search | local/remote object filters | group/path state | recurring | low direct resource cost | information access | DIRECT | CONTROL |
| G14 | Scouting | Information | enemy-object observations | `scoutcontrol.per` | danger/path analysis | interpolation + object searches | danger indicators | scan lifecycle partial | scout exposure | information state | DIRECT | CONTROL |
| G15 | Information | Map/Position | danger / pivot state | scout path analysis | candidate geometry comparison | pivot point | movement cycle | preserves scout utility | route/survival capability | COMPOSED | CONTROL |
| G16 | Map/Position | Attack | target / movement geometry | search and attack systems | attack movement | target evaluation / point actions | movement/attack positioning | repeated | travel-time opportunity cost | engagement position | INFERRED/COMPOSED | CONTROL |
| G17 | Building | Attack | town-size / building transition | TSA/building controller | restart attack | building completion/state + timers | attack timer reenabled | explicit transition | construction cost | restores attack posture | DIRECT | CONTROL |
| G18 | Economy | Map/Position | land-nomad villager distribution | `general.per` search | 504/505 consumer | farthest-pair selection | midpoint + centerward move | event/routine dependent | villager relocation cost | centralized working position | DIRECT + INFERRED | CONTROL |
| G19 | Attack | Economy | pressure / damage opportunity | attack systems | economic state | strategic interpretation | resource denial / map pressure | world-dependent | opponent economic loss | relative economic position | INFERRED | STRATEGIC OPEN |
| G20 | Recovery | Economy | preserved surviving infrastructure/army | distributed recovery rules | gather/production systems | post-failure state | resume normal control | reset/reassessment | limits replacement burden | restores economic conversion | COMPOSED | CONTROL |
| G21 | Economy | Threat | resource/military readiness available for detection response | economy + military state | threat response | thresholds and current state | response activation | recurring | opportunity cost | affects response capacity | COMPOSED | CONTROL |
| G22 | Technology | Military | upgraded combat capability | research control | unit/attack rules | research completion/availability | enables upgraded force | lifecycle unresolved | technology spend | combat capability | COMPOSED | CONTROL |
| G23 | Information | Threat | discovered enemy composition | scouting/threat readers | threat classification | object/unit-family measurement | threat aggregate/state | recurring | scout risk/time | improves response specificity | INFERRED/COMPOSED | CONTROL |
| G24 | Threat | Economy | threat-driven resource priority | threat state | gatherer/production logic | contextual thresholds | shifts resource use | recurring | opportunity cost | funds counter-capability | INFERRED | STRATEGIC OPEN |

---

# 4. Network interpretation

## 4.1 Economy is not a sink; it is a capability allocator

The historical system repeatedly changes gatherer allocation, protects research resources, constrains production by food and population state, and uses escrow. The stronger interpretation is:

`current resources → competing future capabilities → controlled conversion`.

The programmer's implicit problem is not “get resources.” It is “make the current resource portfolio produce the next useful capability without creating an unrecoverable deficit.”

**Evidence:** COMPOSED.

**AEGIS consequence:** economy must expose both stock and strategic allocation state. Raw stock is insufficient.

---

## 4.2 Threat is a bridge between information and expenditure

`threats.per` does not terminate at measurement. Enemy unit families are compressed into strategic channels such as `cavarchers`, which then participate in production and research decisions.

This is one of the strongest demonstrations that the programmer was solving a game problem rather than merely implementing unit commands:

`enemy composition → compact threat representation → response threshold → constrained capability investment`.

**Evidence:** COMPOSED with DIRECT component edges.

**Important boundary:** this proves a historical response mechanism, not a globally optimal counter-composition planner.

---

## 4.3 Production is the conversion boundary

Production is where strategic intent becomes military stock. The `traincamel` chain demonstrates a characteristic historical sequence:

`threat signal → response goal → production-building search → feasibility → train action`.

The programmer repeatedly uses search and `can-*` predicates before side effects. This suggests a practical doctrine of **do not issue an expensive side effect until the relevant capability is locally executable**.

**Evidence:** DIRECT/COMPOSED.

**AEGIS consequence:** production should be modeled as a constrained capability pipeline, not as a list of unit commands.

---

## 4.4 Technology is a capability multiplier and timing decision

Escrowed age research demonstrates protected resource conversion. The same architecture interacts with gatherer allocation, production, and military posture.

The source proves controlled research authorization. It does not provide one universal utility equation for research timing.

**Evidence:** DIRECT for authorization; COMPOSED/INFERRED for strategic interpretation.

**AEGIS consequence:** research candidates need opportunity-cost and timing evaluation.

---

## 4.5 Military is downstream of several systems

Military state is not generated solely by military rules. It depends on:

`economy → production → technology → threat response → force availability`.

Attack state then consumes that capability and feeds recovery decisions.

This explains why a strong bot cannot be architected as independent “economy,” “military,” and “scouting” scripts. Their state channels are causally coupled.

**Evidence:** COMPOSED.

---

# 5. Attack / recovery loop

The most strategically important cycle is:

```text
FORCE AVAILABLE
      ↓
ATTACK COMMITMENT
      ↓
TARGET / POSITION
      ↓
ENEMY RESPONSE
      ↓
RISK / FORTIFICATION / FORCE STATE
      ├───────────────┐
      │ safe          │ unsafe
      ▼               ▼
continue          retreat
                      ↓
                 reset / recover
                      ↓
                 rebuild / regroup
                      ↓
                 restart attack
```

The exact HD source demonstrates controller-state transitions, retreat invocation, and restart preparation. It does **not** by itself prove the full physical and strategic success of every renewed attack.

Therefore:

- `retreat command` = CONTROL evidence;
- `units physically retreat` = WORLD evidence requiring runtime observation;
- `successful renewed pressure` = STRATEGIC evidence requiring game-state observation.

This distinction is now part of the canonical Layer-2 standard.

---

# 6. Information / scouting loop

The scout system exposes another strategic cycle:

```text
MAP UNKNOWN
   ↓
SCOUT GROUP
   ↓
SPATIAL SEARCH
   ↓
ENEMY / DANGER OBJECTS
   ↓
LOCAL GEOMETRY
   ↓
PIVOT / ROUTE DECISION
   ↓
MOVE
   ↓
NEW OBSERVATION
```

The historical code clearly implements the middle of this loop. The strongest defensible strategic interpretation is that the programmer was coupling scouting with route safety and continued movement.

What remains unproven is whether the system explicitly maximizes information value, scouting coverage, or survival probability.

Those are AEGIS opportunities, not recovered historical doctrines.

---

# 7. Land-nomad geometry loop

The 504/505 chain is best represented as:

```text
VILLAGER SET
   ↓
PAIR ENUMERATION
   ↓
PAIR DISTANCE
   ↓
ARGMAX DISTANCE
   ↓
STORE 504 / 505
   ↓
RETRIEVE POINTS
   ↓
MIDPOINT
   ↓
9-TILE CENTERWARD SHIFT
   ↓
MOVE
```

The exact objective function is now known at the local algorithmic level: maximize pair distance.

The higher-level reason for that objective remains **INFERRED**. The source supports the geometric operation; the strategic interpretation that it creates a robust central relocation point remains a hypothesis until the complete land-nomad routine is traced.

---

# 8. The hidden architecture: state channels are the inter-module API

The most important architectural discovery of Pass 12 is that the historical programmer's modules appear to communicate primarily through compact state channels:

- strategic numbers;
- goals;
- flags;
- timers;
- search state;
- target points;
- attack-group state;
- object-data-derived measurements.

These channels function as a primitive inter-module API.

A module generally does not call another module in a modern software sense. Instead:

`module A writes state → module B becomes eligible → module B consumes state → module B writes new state`.

This explains how a very large `.per` program can behave as a distributed controller despite having no centralized planner object.

**Evidence:** COMPOSED.

**AEGIS consequence:** state ownership and transition contracts are more important than reproducing historical file boundaries.

---

# 9. Temporal architecture

The graph is not purely spatial or logical. Timers and persistent eligibility create temporal behavior.

The recurrent pattern is:

`state becomes true → action becomes eligible → action/pending state changes → timer/reset changes eligibility → next evaluation`.

Examples include:

- attack timer re-enabled during restart;
- retreat state cleared after retreat control;
- escrow flags reset;
- repeated threat measurements;
- repeated gatherer decisions;
- recurring scout movement.

The programmer therefore appears to have used **time as a control dimension** rather than as mere scheduling.

**Evidence:** COMPOSED.

**AEGIS consequence:** every major strategic commitment should have temporal eligibility, expiry, or reassessment semantics.

---

# 10. Resource consequence network

A single resource can simultaneously support multiple branches.

For example, food can be:

`villager production + age research + military production + technology + reserves`.

Gold can be:

`age research + military units + technologies + monastery/siege-related capability`.

Wood can be:

`housing + farms + production buildings + economic infrastructure + military infrastructure`.

The historical source repeatedly protects one use by changing allocation or escrow state. This is strong evidence for an implicit opportunity-cost model, but not for a formal scalar optimizer.

**Historical principle reconstructed:** resources are competing claims on future capability.

**AEGIS generalization:** represent resource demand as a portfolio of commitments with priority, timing, reversibility, and failure cost.

---

# 11. Capability consequence network

The historical controller is better understood as converting:

`observation → capability requirement → resource/production action → capability change`.

Examples:

### Enemy ranged/cavalry pressure

`enemy composition`
→ `weighted aggregate`
→ `camel response threshold`
→ `production/research`
→ `camel capability`.

### Age transition

`economic readiness`
→ `escrow`
→ `research`
→ `new age capability`.

### Attack threat

`fortification / enemy response`
→ `retreat state`
→ `retreat command`
→ `preserve force / reposition`.

### Scout danger

`enemy objects`
→ `danger geometry`
→ `pivot`
→ `movement`.

These are capability transformations, not merely command sequences.

---

# 12. Opponent consequence network

The programmer's code contains a recurring asymmetry:

`my state` is measured alongside `enemy state`, and enemy state changes my production, military, research, scouting, or attack behavior.

The historical opponent model is not a clean probabilistic belief engine. It is closer to:

`observable enemy facts → classified pressure signals → conditional response`.

That is enough to produce adaptive behavior, but not enough evidence to claim explicit uncertainty modeling.

**AEGIS lesson:** retain deterministic source-derived response mechanics, but add explicit confidence and alternative hypotheses above them.

---

# 13. Strategic control motifs recovered

Across systems, five motifs recur.

## M1 — Measure then compress

Raw game state is converted into compact strategic channels.

`objects / counts / facts → goal/SN/flag`.

## M2 — Guard before side effect

The source frequently places `can-*`, feasibility, population, food, or building conditions around side effects.

`desire → feasibility → action`.

## M3 — Search before commitment

When spatial choice matters, the programmer searches candidate objects/points before issuing movement/build/train actions.

## M4 — Reset after transition

Goals, timers, flags, and strategic numbers are cleared or changed after a control transition.

## M5 — Re-enter the controller

The action is not the end of the process. State is changed so later rule evaluation can continue from the new game situation.

These five motifs are stronger than any individual build-order rule.

---

# 14. What is actually “the programmer's mind”

The source does not contain a manifesto. The mental model must therefore be reconstructed from repeated implementation choices.

The strongest reconstruction after Pass 12 is:

1. **The game is a changing relationship, not a static checklist.**
2. **Visible enemy state must alter my capability allocation.**
3. **Resources have competing future uses.**
4. **A capability is useful only if it can be produced and brought to bear.**
5. **Spatial decisions require search and geometry, not only fixed coordinates.**
6. **Danger changes movement and attack state.**
7. **Major actions need resets, timers, or state transitions so the controller can continue.**
8. **The engine is constrained, so complex behavior is composed from primitive state channels and rules.**

Items 1–7 are **COMPOSED / INFERRED** reconstructions, not literal comments from the programmer. Item 8 is supported by the distributed rule/state architecture but remains an architectural interpretation.

---

# 15. What the historical AI does not yet prove

The following must not be promoted to historical fact without new evidence:

- a global utility function;
- a centralized planner;
- explicit Bayesian opponent beliefs;
- globally optimal counter-composition;
- explicit information-value optimization;
- explicit economic ROI calculation;
- universal commitment invalidation;
- guaranteed world-state verification after every command;
- a universal action-success feedback loop;
- formal minimax reasoning.

These are candidate AEGIS improvements, not recovered historical internals.

---

# 16. AEGIS architecture derived from the graph

The historical graph suggests the following superior architecture:

```text
WORLD
  ↓
OBSERVE
  ↓
CLASSIFY
  ↓
BELIEF / CONFIDENCE
  ↓
TRANSITION DETECTION
  ↓
OBJECTIVE
  ↓
REQUIREMENTS
  ↓
RESOURCE / CAPABILITY PROPAGATION
  ↓
CANDIDATE GENERATION
  ↓
COST + TIMING + RISK + OPTIONALITY EVALUATION
  ↓
COMMITMENT
  ↓
AUTHORITY
  ↓
ACTION
  ↓
TACTICAL POSTCONDITION
  ↓
OPERATIONAL POSTCONDITION
  ↓
STRATEGIC POSTCONDITION
  ↓
FAILURE / SUCCESS CLASSIFICATION
  ↓
BELIEF UPDATE
  ↓
RELEASE / MODIFY / REINFORCE COMMITMENT
  ↓
REASSESS
```

This is **AEGIS-GENERALIZATION**. It is deliberately more explicit than the historical system.

---

# 17. Control-event standard for future archaeology

For every important historical edge, record:

`OBSERVATION`
→ `CLASSIFICATION`
→ `STATE WRITE`
→ `AUTHORITY / ELIGIBILITY EFFECT`
→ `RESOURCE CONSEQUENCE`
→ `PRODUCTION / TECHNOLOGY CONSEQUENCE`
→ `ACTION`
→ `TACTICAL POSTCONDITION`
→ `WORLD POSTCONDITION`
→ `STRATEGIC POSTCONDITION`
→ `RESET / INVALIDATION`
→ `REASSESSMENT`.

Missing stages must be marked **OPEN**, not silently inferred.

---

# 18. Closure matrix

| System | Control | World | Strategic | Primary remaining gap |
|---|---:|---:|---:|---|
| Economy → Technology | YES | PARTIAL | PARTIAL | completion/usefulness of conversion |
| Threat → Camel production | YES | PARTIAL | PARTIAL | actual camel stock + capability effect |
| Threat → Research | YES | PARTIAL | PARTIAL | research completion + battlefield effect |
| Production → Military | YES | PARTIAL | PARTIAL | post-train stock verification |
| Scout danger → movement | YES | PARTIAL | PARTIAL | physical movement + information/survival outcome |
| 504/505 → movement | YES | PARTIAL | PARTIAL | full land-nomad objective |
| Attack → retreat | YES | PARTIAL | PARTIAL | physical retreat + preserved-force outcome |
| Recovery → renewed attack | YES | OPEN | OPEN | renewed attack execution trace |
| Building → attack restart | YES | PARTIAL | OPEN | actual renewed attack |
| Attack → Economy | PARTIAL | OPEN | OPEN | economic damage/benefit trace |

The graph is therefore **control-rich but world/strategic-incomplete**.

That is the correct current state of knowledge.

---

# 19. Pass-12 conclusions

Pass 12 establishes a new architectural baseline.

The historical AI is best understood as a **distributed strategic control network** whose nodes are game domains and whose edges are state channels.

The programmer repeatedly solved strategy problems through the following transformation:

`game relationship → measurement → compact state → threshold/context → capability response → search/selection → action → reset/reassessment`.

The most important discovery is not a particular threshold or unit choice. It is the **network structure** connecting those choices.

The code behaves as though the programmer understood that:

> an action in one game domain changes the feasible actions in several others.

That is the central strategic insight AEGIS should inherit.

The historical implementation is primitive and distributed. AEGIS should preserve the game knowledge while making the hidden relationships explicit, typed, measurable, verifiable, and revisable.

---

# 20. Required next work

Pass 13 should deepen the graph vertically rather than merely adding more edges.

Priority order:

1. **World-state closure:** prove selected control actions produce the expected game-state changes.
2. **Resource propagation:** trace a single resource commitment from allocation through conversion and release.
3. **Capability realization:** trace threat signal → production/research → actual capability availability.
4. **Attack loop:** close retreat → regroup → renewed attack at world/control levels.
5. **Land-nomad objective:** trace the 504/505 consumer upward until the full strategic purpose is established or falsified.
6. **Scout objective:** trace danger/pivot behavior through subsequent observation to determine whether route safety or information acquisition is the actual optimization target.
7. **State ownership:** assign confidence-rated owners and lifecycle semantics to the graph's shared channels.

Do not promote any strategic interpretation merely because the network is coherent. Coherence is a hypothesis generator; exact source and world-state evidence remain the promotion gate.
