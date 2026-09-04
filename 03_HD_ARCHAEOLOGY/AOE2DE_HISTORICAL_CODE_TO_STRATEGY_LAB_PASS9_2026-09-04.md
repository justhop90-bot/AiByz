# AoE2DE Historical Code-to-Strategy Implementation Lab — Pass 9

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Status:** Working implementation lab  
**Primary source:** verified `AI (HD version).per` and verified Promisory modules  
**Runtime authority:** Layer-1 machine evidence for current DE semantics  
**Predecessor:** `AOE2DE_PRACTICAL_ENGINEERING_MASTERCLASS_PASS8_2026-09-04.md`  
**Purpose:** bridge the gap between understanding the architecture and being able to open a historical `.per` file, trace a real subsystem, and design an AEGIS equivalent without inventing semantics.

---

## 0. Pass objective

Pass 8 taught the engineering method. Pass 9 applies that method to concrete historical subsystems.

The central discipline is:

> **Never jump directly from a rule to a strategic conclusion. Trace the executable relationship.**

For every lab, reconstruct:

`GAME PROBLEM → SOURCE OBSERVATION → STATE WRITE → STATE READER → GUARD → ACTION → POSTCONDITION → LIFECYCLE → STRATEGIC INTERPRETATION → AEGIS DESIGN`

Evidence labels used throughout:

- **DIRECT:** the executable source visibly establishes the relationship.
- **COMPOSED:** multiple DIRECT relationships form a larger causal chain.
- **INFERRED:** strategic meaning reconstructed from repeated behavior or context.
- **AEGIS-GENERALIZATION:** a proposed design derived from historical evidence but not claimed as historical fact.
- **UNCERTAIN:** source evidence is insufficient.

Approximate source locations are retained where exact line anchors were not recovered in this pass. **TBD is preferable to fabricated precision.**

---

# LAB 1 — Escrowed Age Research

## 1.1 Game problem

The AI wants to advance an age, but age advancement competes with units, buildings, upgrades, and economy. The real problem is therefore not merely:

> “Do I have enough food and gold?”

It is:

> “Can I authorize the transition without allowing competing spending to consume the resources reserved for it?”

That distinction is one of the clearest strategic lessons in Promisory.

## 1.2 Historical mechanism

`Promisory/escrow.per` contains explicit age-research rules. The recovered source index shows the Imperial path using:

- `can-research-with-escrow imperial-age`
- `research imperial-age`
- `set-strategic-number sn-current-age imperial`

at the opening Imperial authorization block (exact source indexing also records the same pattern in the ADPromisory reconstruction). Later escrow logic checks research status, food/gold quantities, and adds research cost before executing additional research commitments.

**Evidence:** DIRECT for the individual source relationships. COMPOSED for the interpretation of escrow as a reservation/commitment mechanism.

## 1.3 Literal control trace

Conceptually the historical chain is:

`escrow state → research feasibility → research command → strategic-age state update`

The important engineering observation is that the research command is guarded by a feasibility predicate that knows about escrow. The AI does not merely issue `research imperial-age` whenever a numerical threshold appears true.

## 1.4 State ownership questions

Before reproducing this subsystem, identify:

| Question | Historical evidence status |
|---|---|
| Who writes escrow state? | DIRECT elsewhere in `escrow.per`; exact writer map requires full-source anchor audit |
| Who reads escrow feasibility? | DIRECT: age research rules |
| Who performs research? | DIRECT: `research imperial-age` |
| Who updates strategic age? | DIRECT: `set-strategic-number sn-current-age imperial` |
| Who verifies actual completion? | UNCERTAIN from this narrow trace; must distinguish command issuance from world-state completion |
| What releases competing claims? | DIRECT/COMPOSED across escrow reset rules |

## 1.5 Strategic meaning

**INFERRED:** the programmer treats an age transition as a protected future capability, not as an isolated purchase.

The reservation exists because the value of 800 food and 200 gold is conditional on what the AI is trying to become. Food spent on a military unit can be rational in one state and strategically destructive in another if it delays the transition.

## 1.6 AEGIS redesign

Represent the transition explicitly:

`OBJECTIVE = AGE_TRANSITION`

`REQUIREMENT = research_available + required_resources + required_prerequisites`

`COMMITMENT = reserve resources for age transition`

`AUTHORITY = age-transition owner may consume reserved resources`

`VERIFY = research pending/completed + current-age world state`

`FAILURE = commitment invalidated / resource theft / prerequisite failure / execution failure / transition not completed`

Do **not** claim that historical Promisory already implemented this clean semantic object. That is an AEGIS architecture built from the historical pattern.

---

# LAB 2 — Contextual Gatherer Allocation

## 2.1 Game problem

A fixed gather ratio is insufficient because the value of food, wood, gold, and stone changes with age, buildings, military plans, research, and current resource stock.

The historical question is:

> “Given the capability the AI is trying to purchase next, which resource bottleneck should villagers solve now?”

## 2.2 Historical mechanism

`Promisory/gatherers.per` contains contextual resource-allocation rules. Recovered source analysis identified:

- age-dependent food/wood/gold/stone allocation;
- conditions involving units, buildings, research, and resource state;
- a sentinel-style strategic regime using `temporary-goal10 985795`;
- percentage calculations and later Castle-oriented allocation changes.

The source therefore demonstrates contextual allocation, but it does **not** by itself prove a modern demand-forecast optimizer.

**Evidence:** DIRECT for contextual allocation; INFERRED for the higher-level “future demand forecast” interpretation.

## 2.3 Control trace

`current game state → strategic/resource condition → gatherer percentage write → villagers distributed → resource inflow changes → next feasibility condition changes`

This is a feedback controller even though it is implemented as distributed rules rather than a single mathematical optimizer.

## 2.4 Strategic interpretation

**INFERRED:** resource assignment is subordinate to capability acquisition.

A villager on gold is not inherently “a gold villager.” The villager is temporarily assigned to solve a strategic resource constraint.

That yields an important AEGIS concept:

`villager allocation = resource-control action`

rather than:

`villager allocation = static economy template`.

## 2.5 AEGIS redesign

For each resource define:

`RAW_STOCK`

`INCOME_RATE`

`COMMITTED_STOCK`

`EXPECTED_NEAR_TERM_DEMAND`

`OPPORTUNITY_COST`

`RESERVE_REQUIREMENT`

Then derive:

`ALLOCABLE_RESOURCE = RAW_STOCK - ACTIVE_COMMITMENTS - RESERVE`

This formula is an **AEGIS-GENERALIZATION**, not a claim about the historical implementation.

---

# LAB 3 — Production Authorization

## 3.1 Game problem

A unit is useful only if the AI can produce it at the right time, from the right building, with the right resources, without destroying a higher-value capability transition.

The historical production system therefore has to solve two different questions:

1. What military capability is desired?
2. Which production actions are currently authorized?

## 3.2 Historical mechanism

`Promisory/units.per` begins with numerous production flags disabled and later enables specific production goals under strategic conditions. The recovered source audit identified initial `train` flags for classes including villagers, monks, unique units, siege, rams, trebuchets, and other production categories, followed by conditional activation.

**Evidence:** DIRECT for the production-state mechanism. **Interpretation:** COMPOSED/INFERRED that these flags function as production authorization state.

## 3.3 Why this matters

A naïve bot asks:

> “Should I build a knight?”

The production controller must ask:

> “Is knight production currently authorized, feasible, economically supportable, strategically compatible, and still valid?”

That creates a pipeline:

`desired capability → unit requirement → production authorization → feasibility → queue action → world-state verification`.

## 3.4 Production capacity is part of the decision

If three stables exist but only one can continuously afford the required unit stream, the theoretical unit count is misleading.

AEGIS should therefore model:

`UNIT_REQUIREMENT`

`PRODUCTION_CAPACITY`

`QUEUE_PRESSURE`

`RESOURCE_FEED_RATE`

`TECH_PREREQUISITES`

`SWITCH_COST`

`COMMITMENT_LOCK`

This extends the historical production-flag idea into a capability pipeline.

## 3.5 Failure classes

- desired unit not enabled;
- production building absent;
- prerequisite absent;
- resources insufficient;
- queue saturated;
- composition obsolete;
- production commitment conflicts with transition;
- command succeeds but strategic objective still fails.

---

# LAB 4 — Threat Classification → Response

## 4.1 Game problem

The opponent does not announce “I am now executing a cavalry strategy.” The AI must infer a threat from observations.

The historical architecture explicitly separates focus-player/target logic, military-population measurements, and branches for threat categories.

## 4.2 Historical mechanism

`Promisory/threats.per` contains branches for cavalry-archer, gunpowder, infantry and other threat classes. It also uses focus-player and target relationships and military population measurements.

This establishes a distributed threat-classification system.

**Evidence:** DIRECT for observations and threat branches. **UNCERTAIN/INFERRED** for the existence of a single unified threat score.

## 4.3 Correct trace

Do not write:

`enemy has knights → build spears`.

The historically faithful abstraction is:

`enemy observation → threat classification → strategic threat state → downstream response rules`.

The AEGIS abstraction can extend it:

`OBSERVATION → BELIEF → THREAT VECTOR → REQUIREMENT → CANDIDATE RESPONSE`.

## 4.4 Threat is capability, not merely unit identity

A cavalry threat can imply:

- mobility;
- raid pressure;
- ability to punish exposed economy;
- ability to disengage from slow units;
- pressure on vulnerable resource lines.

Therefore the counter-candidate set must not be limited to “anti-cavalry unit.”

AEGIS candidate classes may include:

`COUNTER_UNIT | FORTIFICATION | MOBILITY | POSITIONAL_DENIAL | ECONOMIC_RELOCATION | RETREAT | COUNTER_ATTACK | SIEGE | TECHNOLOGY | DELAY`

This broader candidate space is an **AEGIS-GENERALIZATION**.

## 4.5 Uncertainty

Historical detection does not prove certainty. AEGIS should maintain:

`belief strength + evidence age + alternative hypotheses + invalidation conditions`.

Observed response and predicted response must remain separate:

`OBSERVED_RESPONSE ≠ PREDICTED_RESPONSE`.

---

# LAB 5 — Candidate Search / Optimization

## 5.1 Game problem

`.per` does not provide a conventional general-purpose optimizer in the sense of a modern programming language. Yet Promisory performs repeated candidate-search operations.

The engineer must learn to recognize the pattern.

## 5.2 Historical mechanism

`general.per` contains iterative search machinery using temporary goals and persistent search state. Recovered analysis identified patterns including:

`reset search → find candidate/local villagers → obtain search state → store candidate measurements → set target objects → obtain points → calculate distance → preserve best candidate → decrement/advance search state → jump → terminate`

This is a distributed search loop implemented through rule eligibility, state, jumps, and engine primitives.

**Evidence:** DIRECT at the mechanism level; avoid describing it as a conventional sequential loop.

## 5.3 The algorithmic skeleton

```text
RESET
  ↓
INITIALIZE SEARCH STATE
  ↓
OBTAIN CANDIDATE
  ↓
MEASURE FEATURES
  ↓
CHECK CONSTRAINTS
  ↓
CALCULATE SCORE
  ↓
COMPARE WITH BEST
  ↓
PRESERVE BEST
  ↓
ADVANCE SEARCH STATE
  ↓
REPEAT / EARLY EXIT
  ↓
RETURN BEST CANDIDATE
```

## 5.4 Performance is part of correctness

For every search record:

`SEARCH_SCOPE`

`CANDIDATE_COUNT`

`FEATURE_COST`

`RULES_PER_ITERATION`

`ITERATION_COUNT`

`RESET_COST`

`EARLY_EXIT`

`PERSISTENT_STATE_COST`

`WORST_CASE_COST`

A search that finds the mathematically best location but consumes the rule budget needed for military control is not strategically optimal.

## 5.5 AEGIS candidate contract

`CANDIDATE → FEATURES → HARD CONSTRAINTS → SCORE → UNCERTAINTY → COST → TIMING → OPTIONALITY → DECISION`

The distinction between hard constraints and soft scoring is critical. A candidate that violates a mandatory prerequisite should not win because it has a high score elsewhere.

---

# LAB 6 — Scout Path / Waypoint Selection

## 6.1 Game problem

Scouting is an information-acquisition problem under movement and safety constraints.

The scout is not merely ordered to “explore.” It must select a route that obtains useful information without unnecessarily losing the information-gathering asset.

## 6.2 Historical mechanism

`Promisory/scoutcontrol.per` contains explicit operational comments and geometry machinery including:

- creating groups;
- analyzing paths for safety;
- breaking paths into quartersteps;
- checking for TC/spear concentrations;
- obtaining pivot points;
- generating candidate points around obstacles;
- interpolation toward target regions;
- selecting the closer candidate;
- calculating waypoints;
- selecting waypoints;
- deciding movement/action.

The source explicitly notes performance concerns around path analysis.

**Evidence:** DIRECT for the operational mechanics and performance concern.

## 6.3 Strategic interpretation

**INFERRED:** the programmer understood that scouting has information value and that path geometry can alter the quality and safety of that information.

The important question is not:

> “Did the scout move?”

It is:

> “What uncertainty did the scout reduce, at what cost and risk?”

## 6.4 AEGIS information contract

`TARGET_INFORMATION → VALUE_OF_INFORMATION → ROUTE_CANDIDATES → SAFETY_CONSTRAINTS → INFORMATION_GAIN → COST/RISK → ROUTE_COMMITMENT → OBSERVE → UPDATE_BELIEF`.

This is a major opportunity for AEGIS to generalize the historical tactical machinery into an explicit information model.

---

# LAB 7 — Attack → Retreat → Restart

## 7.1 Game problem

An attack is not a Boolean command. It is a lifecycle.

The historical AI has to manage:

`prepare → attack → pressure → retreat → regroup/reset → restart or transition`.

## 7.2 Historical mechanism

HD source analysis identified explicit state around:

- `attack-goal`;
- `attack-status-goal`;
- `retreat-now-goal`;
- attack timers;
- attack-goal clearing;
- reset state;
- `restart-attack-goal`;
- `enemy-fortifications-goal` and attack suppression/defer logic.

**Evidence:** DIRECT for these state/control relationships. **INFERRED** for the broader interpretation that the controller is preserving military capital.

## 7.3 State-machine reconstruction

```text
PREPARE
  ↓
AUTHORIZE
  ↓
MOVE
  ↓
ENGAGE
  ↓
ASSESS
  ├── CONTINUE
  ├── CHANGE OBJECTIVE
  ├── REGROUP
  └── RETREAT
          ↓
       COOLDOWN / RESET
          ↓
       REASSESS
          ↓
       RESTART / TRANSITION
```

## 7.4 Fortification branch

A detected fortification can change the value of continuing the same attack. The source establishes an `enemy-fortifications-goal` and attack-control behavior associated with fortifications.

Historical evidence supports the **state and suppression/defer mechanism**. It does not, by this evidence alone, prove a single unified “fortification causes siege optimizer.” That larger causal chain is COMPOSED at best.

## 7.5 Verification rule

Never use:

`attack command issued = attack succeeded`.

At minimum distinguish:

`COMMAND_POSTCONDITION`

`WORLD_STATE_POSTCONDITION`

`TACTICAL_POSTCONDITION`

`OPERATIONAL_POSTCONDITION`

`STRATEGIC_POSTCONDITION`.

An attack can satisfy the first and fail every higher level.

---

# LAB 8 — Building Placement → Fallback / Recovery

## 8.1 Game problem

A building request can fail for reasons unrelated to strategic intent: blocked location, invalid geometry, unavailable builders, changed battlefield conditions, or engine-specific placement restrictions.

The programmer therefore needs a recovery path.

## 8.2 Historical mechanism

`Promisory/buildings.per` contains the documented fallback:

> “Secondary backup for rebuilds - regular system occasionally fails...”

The module contains search/object handling for building placement and rebuild behavior. `extremebuildings2.per` contains additional historical placement/fallback logic and comments concerning attempts when normal placement is impossible and performance/rule-budget pressure.

**Evidence:** DIRECT for explicit fallback intent and placement/search behavior.

## 8.3 Strategic interpretation

The most important lesson is not the exact placement algorithm. It is the existence of **implementation-aware recovery**.

The programmer understood that:

`desired building ≠ successful building placement`.

Therefore a robust controller needs:

`INTENT → CANDIDATE LOCATION → FEASIBILITY → PLACEMENT ATTEMPT → WORLD OBSERVATION → FALLBACK / RETRY / ABORT`.

## 8.4 AEGIS recovery classes

- `RETRY_SAME_CANDIDATE` — transient obstruction;
- `TRY_ALTERNATE_CANDIDATE` — candidate invalid;
- `CHANGE_POSITION` — local geometry changed;
- `CHANGE_OBJECTIVE` — building no longer valuable;
- `ESCALATE_TO_DIFFERENT_CAPABILITY` — substitute infrastructure;
- `ABORT_COMMITMENT` — conditions invalidate the investment.

The last three are AEGIS extensions, not direct historical claims.

---

# 9. Cross-Lab Architecture

The eight labs expose the same underlying architecture without pretending the historical source was written as one modern framework.

| Layer | Historical evidence | AEGIS interpretation |
|---|---|---|
| Observation | facts, counts, search results, map/path data | typed observation |
| Classification | threat branches, map/role logic | classification |
| Belief | persistent strategic interpretations are distributed | explicit belief object |
| Requirement | implicit through production/research/attack conditions | explicit requirement |
| Candidate | search, units, buildings, tactical alternatives | candidate set |
| Evaluation | distance, capability, feasibility, contextual rules | cost/timing/risk/optionality score |
| Commitment | escrow and persistent state | explicit commitment |
| Authority | production/research/attack state gates | separate authority plane |
| Action | train/research/build/move/attack | side-effect boundary |
| Verification | pending/state checks and subsequent rules | tactical/operational/strategic postconditions |
| Recovery | reset/retry/fallback/restart | explicit failure taxonomy |
| Reassessment | timers, state changes, repeated rules | transition controller |

The table is a **composed AEGIS reconstruction**, not a claim that these semantic categories were literally named in the historical source.

---

# 10. Read a `.per` Rule Backwards

This is the practical debugging technique to carry into implementation.

When you encounter an important action, start at the side effect:

`ACTION`

then walk backward:

`ACTION ← GUARDS ← STATE DEPENDENCIES ← WRITERS ← INITIALIZATION ← LOAD ORDER`.

Example:

`research imperial-age`

Ask:

1. What guards make this rule eligible?
2. Which facts are engine observations?
3. Which values are goals or SNs?
4. Who wrote those values?
5. What reset or competing writer can change them?
6. Was escrow established first?
7. Is research pending handled?
8. What proves the age actually changed?
9. What later rule consumes the new state?
10. What happens if the transition fails?

Then perform the forward trace:

`OBSERVATION → STATE WRITE → GUARD → ACTION → RESULT → NEXT STATE`.

The combination of backward and forward tracing exposes hidden dependencies much faster than reading `.per` files top-to-bottom.

---

# 11. What `.per` Is Not

`.per` should not be mentally modeled as ordinary sequential application code.

It is not safe to assume:

- every rule executes once;
- textual adjacency means causal adjacency;
- a rule firing proves its strategic objective succeeded;
- a command proves a world-state transition;
- one writer owns a variable for its whole lifecycle;
- a high-numbered goal is automatically scratch;
- a proximity relationship means object ownership;
- a shared trigger proves causality;
- a historical workaround is an ideal architecture;
- a strategy inferred from repeated behavior is a direct programmer statement.

The actual program emerges from eligibility, persistent state, facts, actions, jumps, timers, search state, load order, and repeated evaluation.

---

# 12. State Ownership Contract for AEGIS

Every strategic state variable should eventually have this record:

`STATE_ID`

`SEMANTIC_TYPE`

`OWNER`

`WRITERS`

`READERS`

`RESETTER`

`AUTHORITY_EFFECT`

`LIFETIME`

`INVALIDATION`

`SIDE_EFFECTS`

`EVIDENCE_GRADE`

Historical archaeology must recover as much of this as evidence permits. AEGIS implementation should refuse ambiguous ownership for high-impact state unless explicitly designated as shared state.

---

# 13. Commitment Contract

A strategic commitment should eventually be representable as:

`OWNER`

`OBJECTIVE`

`RESOURCE_COST`

`TIMING_WINDOW`

`DEADLINE`

`BREAK_CONDITION`

`REPLACEMENT_CONDITION`

`AUTHORITY`

`RELEASE_ACTION`

`VERIFICATION`

This is AEGIS architecture. Historical escrow supplies strong evidence for the general idea of resource reservation, but not for every field above.

A commitment is valuable because it prevents the controller from repeatedly reconsidering an already-authorized transition unless a meaningful invalidation occurs.

---

# 14. Historical Inheritance Matrix

## Preserve

- explicit strategic state;
- contextual resource allocation;
- resource reservation/escrow;
- feasibility gates;
- production-state control;
- threat classification;
- map-aware strategy;
- tactical candidate search;
- geometry-aware movement;
- attack/retreat/reset/restart lifecycle;
- timers and temporal guards;
- fallback/recovery;
- modular decomposition;
- performance awareness.

## Improve

- state ownership;
- typed observation vs belief;
- explicit requirements;
- explicit commitments;
- authority separated from intent;
- postcondition verification;
- failure taxonomy;
- invalidation and replacement;
- opportunity cost;
- uncertainty;
- transition ownership;
- measurable objectives;
- performance budgets;
- historical-vs-AEGIS candidate separation.

## Reject as design doctrine

- unexplained shared state;
- giant rules;
- command-equals-success reasoning;
- permanent thresholds without hysteresis;
- one threat class mapped to one mandatory response;
- raw resource stock treated as freely spendable;
- historical implementation debt treated as ideal architecture;
- inferred programmer intent presented as source fact.

---

# 15. Pass-9 Conclusions

### Finding 1 — The historical AI is more operationally sophisticated than a build-order script.

The source contains state, search, feasibility, reservations, threat classification, temporal control, geometry, tactical control, and recovery.

**Evidence:** COMPOSED from the eight labs.

### Finding 2 — The programmer repeatedly solved strategic problems by introducing intermediate state.

Goals, SNs, timers, flags, search state, escrow state, target identity, attack status, and threat state are all examples of breaking a strategic problem into rule-manageable pieces.

**Evidence:** COMPOSED/INFERRED.

### Finding 3 — The strongest common pattern is capability transition.

Age research, production, threat response, scouting, attack, and infrastructure all change what the AI can do next.

**Evidence:** INFERRED synthesis over DIRECT mechanisms.

### Finding 4 — Search and geometry are strategic infrastructure, not isolated tactical tricks.

Candidate selection determines where resources, production, scouts, attacks, and buildings can successfully convert intent into game-state change.

**Evidence:** COMPOSED + AEGIS-GENERALIZATION.

### Finding 5 — Recovery is part of the original engineering mindset.

The source explicitly documents fallback behavior and repeated state reset/restart patterns.

**Evidence:** DIRECT for fallback/reset mechanisms; broader recovery doctrine is COMPOSED.

### Finding 6 — AEGIS should not copy the historical architecture literally.

The correct inheritance is the **problem-solving knowledge**: observe context, preserve state, constrain actions, spend resources conditionally, execute through feasibility gates, observe consequences, and reassess.

The modern architecture can make these responsibilities explicit without pretending they were explicit in the original code.

**Evidence:** AEGIS-GENERALIZATION.

---

# 16. Next Archaeological Requirement

Pass 9 is sufficient to move from conceptual mastery to source-level implementation training, but it exposes the next evidence requirement:

## Pass 10 — Exact-Anchor Historical Trace Pack

For each of the eight labs, recover the smallest complete executable slice containing:

`defrule → all guards → all state writes → side effect → relevant reset/release → immediate readers`

Then record:

`Exact source text | exact line | source module | writer | reader | state ontology | temporal semantics | mechanism | postcondition | failure/recovery | evidence grade`

The goal of Pass 10 is not more theory. It is **forensic reproducibility**: another engineer should be able to open the verified source, jump to the anchor, and reproduce the entire reasoning trace without relying on this document's interpretation.

That is the point at which Layer 2 begins transitioning from archaeology into implementation specification.
