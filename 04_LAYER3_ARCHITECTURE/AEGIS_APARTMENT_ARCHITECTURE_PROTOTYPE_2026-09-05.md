# AEGIS Apartment Architecture Prototype

**Date:** 2026-09-05  
**Layer:** 3A — Architecture / Pre-furniture design  
**Status:** PROTOTYPE / ARCHITECTURAL DESIGN  
**Implementation:** NONE  
**Runtime:** NONE  
**Authority:** Architecture prototype; does not allocate runtime channels or authorize implementation.

---

## 0. Purpose

This document defines the first architectural prototype for the AEGIS bot after closure of Layer 2.

The central design metaphor is an apartment:

> **Layer 2 established the building envelope, utilities, stock occupants, available mailbox space, and physical constraints. Layer 3A designs the apartment completely before a single piece of furniture is moved in.**

The objective is not to reproduce the stock AI's file structure. The objective is to preserve every practically valuable capability demonstrated by the stock AI, remove complexity that exists primarily because the historical implementation was forced through primitive state channels, and add modern strategic capabilities that increase practical game-playing strength without creating abstraction for its own sake.

This is therefore a **functional modernization**, not a rewrite-for-rewrite's-sake.

---

# 1. Design doctrine

## 1.1 Practical superiority is the objective

AEGIS is not being designed to be academically elegant. It is being designed to play Age of Empires II better.

Every architectural component must answer a practical question such as:

- What is happening?
- What matters?
- What does the opponent appear to be doing?
- What is likely to happen next?
- What do we need?
- What can we afford?
- What are our alternatives?
- Which alternative is best now?
- What have we committed ourselves to?
- Did the action actually happen?
- Did it produce the intended strategic effect?
- If not, what should change?

A component that cannot improve one of those decisions should be presumed unnecessary.

## 1.2 Preserve proven practical behavior

The stock AI is a decades-refined reference implementation. Its constraints forced its authors to discover high-value techniques for:

- resource allocation;
- escrow/protected spending;
- production feasibility;
- threat compression;
- technology timing;
- scouting and spatial search;
- attack-group management;
- retreat and restart;
- construction control;
- trade;
- water control;
- timers and temporal eligibility;
- compact state-channel communication.

AEGIS must not discard those capabilities merely because the underlying implementation is old.

## 1.3 Decompress, do not inflate

The stock AI often compresses several conceptual jobs into one primitive state channel because goals, strategic numbers, timers, searches, and rule interactions are limited and multiplexed.

AEGIS should instead expose the concepts explicitly at the architectural level and only compress them when the actual machine representation requires it.

The target is:

`MORE PRACTICAL FUNCTION / UNIT OF COMPLEXITY`

not:

`MORE CODE / UNIT OF COMPLEXITY`.

## 1.4 Separation of responsibility

No room should silently perform another room's job.

- Sensors observe.
- Beliefs represent knowledge.
- Threats classify danger.
- Opportunities identify exploitable conditions.
- Strategy establishes posture and objectives.
- Requirements describe what must be achieved.
- Capabilities describe what the machine/game can provide.
- Candidates propose alternatives.
- Arbitration selects among competing alternatives.
- Commitment records a decision.
- Execution performs authorized actions.
- Verification determines what actually happened.
- Recovery handles deviation and failure.
- Memory records useful history.

## 1.5 No omniscient planner

AEGIS should not become one enormous planner that tries to solve the whole game every cycle.

The architecture should be centralized enough to maintain coherent strategic priorities, but distributed enough to remain practical in the rule-engine environment.

The preferred model is:

`shared strategic spine + specialized operational rooms + explicit mailbox contracts`.

---

# 2. What the stock apartment actually contains

The stock package should be understood by function, not merely by filenames.

The historical source tree contains specialized systems for at least the following domains:

| Stock domain / module family | Practical job | AEGIS disposition |
|---|---|---|
| `init` / constants | initialize and configure AI state | KEEP, SEPARATE |
| `gatherers` | allocate villagers/resources | KEEP, MODERNIZE |
| `escrow` | protect resources for intended uses | KEEP, GENERALIZE |
| `buildings` / `extremebuildings2` | construction and infrastructure | KEEP, REFRAME |
| `units` | unit production and unit-state control | KEEP, SPLIT |
| `researches` | technology and age progression | KEEP, MODERNIZE |
| `threats` | compress enemy composition into response signals | KEEP, EXPAND |
| `scoutcontrol` | scouting, searches, movement and danger handling | KEEP, EXPAND |
| `interaction` | inter-system/game interaction | KEEP, REFRAME |
| `attack` / `tsa` | attack groups, attack state, tactical operations | KEEP, SPLIT |
| `trade` | market/trade capability | KEEP, INTEGRATE |
| `watercontrol` | naval control | KEEP, SPECIALIZE |
| `resign` | end-state assessment | KEEP, UPGRADE |
| event/merge/support systems | sequencing, composition, communication | KEEP AS MECHANISMS, NOT AS ARCHITECTURE |
| temporary/state-channel mechanisms | inter-module communication | KEEP CONCEPT, REDESIGN CONTRACTS |

The stock architecture is therefore not a collection of isolated scripts. It behaves as a distributed controller whose modules communicate through compact state channels, searches, timers, facts, and commands.

The recovered cross-system topology is:

`ECONOMY → THREAT → PRODUCTION → TECHNOLOGY → MILITARY → MAP/POSITION → ATTACK → RECOVERY → ECONOMY`

with information/scouting feeding threat, map, and positioning systems.

---

# 3. Stock room review: keep / improve / replace

## 3.1 Initialization Room

### Stock function

Establishes constants, initial state, civilization-specific configuration, strategic-number defaults, goals, opening conditions, and other baseline behavior.

### Keep

Yes. Initialization is unavoidable.

### Correct

Do not allow configuration, current state, and strategic policy to become indistinguishable.

### AEGIS room

**Configuration & Bootstrap**

Responsibilities:

- build-specific configuration;
- civilization configuration;
- difficulty/profile configuration;
- initial policy;
- state initialization;
- reset policy.

Configuration is immutable after initialization wherever practical. Runtime state belongs elsewhere.

---

## 3.2 Economy Room

### Stock function

Controls gatherer distribution, resource priorities, escrow, and affordability conditions.

### Keep

Almost all practical behaviors.

### Replace

Replace implicit resource competition with an explicit **Resource Portfolio** concept.

The portfolio distinguishes:

- current stock;
- current income;
- committed resources;
- reserved resources;
- discretionary resources;
- projected income;
- projected deficit;
- time-to-affordability.

### Practical upgrade

The AI should not merely ask:

`Do I have 450 food?`

It should ask:

`How much of the 450 is already economically committed, how much is available for a competing objective, and what capability does spending it buy?`

This preserves stock's resource discipline while making opportunity cost explicit.

---

## 3.3 Escrow / Commitment Funding Room

### Stock function

Protect resources for intended research, age advancement, production, and other purposes.

### Keep

Yes. This is a highly valuable stock concept.

### Modernize

Escrow becomes one mechanism inside the larger **Strategic Ledger / Resource Portfolio** rather than a parallel economic universe.

A resource reservation should identify:

- claimant;
- objective;
- amount;
- expected use time;
- priority;
- cancellation conditions;
- release conditions.

---

## 3.4 Production Room

### Stock function

Determines where and when units can be produced, checks feasibility, and issues training commands.

### Keep

The practical production pipeline.

### Replace

Do not make production a list of unit commands.

AEGIS production should be a **Capability Factory**.

Example:

`train 3 camels`

is represented strategically as:

`purchase additional anti-cavalry capability`.

The production layer then determines the legal physical implementation.

This preserves all stock production functionality while allowing strategic substitution.

---

## 3.5 Infrastructure Room

### Stock function

Buildings, production infrastructure, defensive structures, town expansion, and building placement/search behavior.

### Keep

Yes.

### Modernize

Create an **Infrastructure Planner** that classifies structures by purpose:

- economic;
- military;
- defensive;
- technological;
- logistical;
- forward;
- transitional.

The planner should know why infrastructure is being requested rather than treating construction as an isolated task.

---

## 3.6 Technology Room

### Stock function

Age advancement, research selection, escrow interaction, and technology feasibility.

### Keep

Yes.

### Modernize

Create a **Technology & Timing Planner**.

Every technology candidate is evaluated against:

`benefit + timing + resource cost + opportunity cost + prerequisite effects + strategic need`.

The critical modernization is timing. A technology can be good and still be wrong now.

---

## 3.7 Threat Room

### Stock function

Detects enemy composition and compresses it into strategic threat signals that influence production and technology.

### Keep

This is one of the strongest stock architectural patterns.

### Expand

Create the **Threat Intelligence Center** with explicit dimensions:

- threat type;
- severity;
- urgency;
- confidence;
- trajectory;
- counter-requirement;
- time-to-impact;
- geographic relevance.

Stock frequently answers:

`What does the enemy have?`

AEGIS should additionally answer:

`What is the enemy becoming?`

---

## 3.8 Scouting / Information Room

### Stock function

Scouting, object searches, danger checks, spatial relationships, movement, and route/pivot behavior.

### Keep

Strongly keep.

### Add

**Information Value / Attention.**

The scout controller should be capable of prioritizing unresolved information by strategic value.

Examples:

- enemy production transition: high value;
- exposed gold: high value;
- exact farm count: low value;
- remote low-value resource detail: low value.

The practical principle is:

> Scout to answer the question that most changes the decision.

This is a major modernization without requiring exotic machinery.

---

## 3.9 Opponent Model Room — NEW

The stock AI has enemy-state detection and strategic response, but the architecture should add an explicit **Opponent Model**.

Track, where evidence permits:

- civilization;
- demonstrated strategy;
- aggression tendency;
- defensive tendency;
- production preferences;
- transition tendencies;
- resource priorities;
- response patterns;
- likely next transition;
- confidence in each belief.

This is not personality simulation. It is practical predictive context.

---

## 3.10 Strategic Situation Room — NEW / CENTRAL

This is the primary room missing from the stock decomposition.

It synthesizes:

- current state;
- threats;
- opportunities;
- objectives;
- constraints;
- resources;
- map control;
- opponent model;
- timing.

Output:

**Strategic Posture.**

Examples:

- defensive stabilization;
- economic expansion;
- timing attack;
- pressure;
- counterattack;
- recovery;
- all-in;
- consolidation;
- transition.

The posture is not a permanent strategy. It is the current strategic interpretation of the game.

---

## 3.11 Opportunity Room — NEW

The stock architecture is strong at responding to threats. AEGIS should explicitly search for profitable situations.

Examples:

- exposed economy;
- displaced enemy army;
- incomplete wall;
- isolated army;
- overextended production;
- temporary technology gap;
- exposed strategic resource;
- timing window.

Output:

`opportunity + payoff + urgency + feasibility + risk`.

The objective is to make AEGIS proactive rather than merely reactive.

---

## 3.12 Forecast Room — NEW

Convert snapshots into short-horizon trajectories.

Examples:

`stable count 1 → 2 → 3`

becomes:

`increasing cavalry production capacity`.

Or:

`food income rising + stable production active`

becomes:

`increasing probability of sustained cavalry production`.

Forecasts must remain confidence-weighted and short-horizon. This is not an attempt to predict the entire game.

---

## 3.13 Attention Manager — NEW

The bot needs to decide what deserves control effort.

Attention should prioritize:

1. imminent lethal threats;
2. decisive opportunities;
3. high-value unresolved uncertainty;
4. urgent commitments;
5. ordinary maintenance.

This prevents control bandwidth from being wasted on low-impact work while strategically important events develop.

---

## 3.14 Objective Room

### Stock equivalent

Distributed across strategic goals, threat responses, technology, economy, attack, and production.

### AEGIS replacement

Make objectives explicit.

Example:

`Survive enemy cavalry pressure.`

is an objective.

`Train camels.`

is a candidate response.

The distinction is mandatory.

---

## 3.15 Requirement Room

NEW explicit room between objective and capability.

Example:

Objective:
`contain cavalry`

Requirement:
`obtain sufficient anti-cavalry combat power near the threatened area before projected contact`.

This allows several different capabilities to satisfy the same strategic need.

---

## 3.16 Constraint Room — NEW

The constraint solver sits between requirements and candidates.

It asks:

- what prerequisites exist?
- what resources are committed?
- what can be delayed?
- what must happen first?
- what production capacity exists?
- what timing window exists?
- what conflicts with other commitments?

This is the bridge from strategic desire to executable possibility.

---

## 3.17 Capability Room

A capability is the strategic thing the AI wants to acquire or preserve.

Examples:

- anti-cavalry power;
- ranged firepower;
- siege capability;
- map vision;
- defensive fortification;
- economic throughput;
- mobility;
- naval control.

A capability has:

- prerequisites;
- cost;
- source;
- availability;
- production throughput;
- time-to-effect;
- strategic utility;
- scalability;
- confidence.

This allows strategic substitution.

---

## 3.18 Candidate Room

Generate several feasible ways to satisfy a requirement.

Example:

`cavalry threat`

may yield:

- spearmen;
- camels;
- walls;
- castle defense;
- counterraid;
- mixed army;
- positional defense;
- economic counterpressure.

The candidate system must not assume that the textbook counter is automatically the best answer.

---

## 3.19 Arbitration Room

This is the strategic traffic controller.

It resolves simultaneous demands:

`cavalry threat + age-up + exposed gold + army opportunity + food shortage`.

Evaluation dimensions should include:

- urgency;
- strategic value;
- survival impact;
- payoff;
- resource cost;
- opportunity cost;
- time-to-effect;
- reversibility;
- confidence;
- conflict with existing commitments.

Arbitration selects what receives priority now.

---

## 3.20 Strategic Ledger — NEW

The Strategic Ledger records promises the AI has made to itself.

Each project/commitment conceptually contains:

- objective;
- response;
- owner;
- generation;
- resource reservation;
- dependencies;
- expected payoff;
- expected completion;
- progress;
- cancellation conditions;
- replacement value.

This is the architecture's answer to strategic drift.

---

## 3.21 Commitment Room

Once arbitration selects a candidate, AEGIS creates a formal commitment.

The minimum conceptual envelope remains:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Commitments are not commands.

They are decisions authorizing later execution.

---

## 3.22 Execution Room

Execution translates an authorized commitment into legal engine actions.

The executor should be strategically ignorant.

It should answer:

`Can this authorized action be issued now?`

not:

`Should we pursue this strategy?`

---

## 3.23 Verification Room

This is a major AEGIS differentiator.

The architecture preserves the evidence ladder:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

A command does not prove a world transition.

A created unit does not prove strategic success.

Verification therefore exists at multiple levels:

- command/control verification;
- world-state verification;
- strategic-effect verification.

---

## 3.24 Recovery Room

The stock AI contains valuable retreat/reset/restart behavior. AEGIS should make recovery a formal room.

Possible outcomes:

- success;
- partial success;
- delayed;
- blocked;
- failed;
- invalidated;
- superseded.

Possible recovery responses:

- wait;
- retry;
- adapt;
- redirect;
- retreat;
- replace;
- escalate;
- deescalate;
- abandon;
- replan.

---

## 3.25 Military Command Room

Separate strategic military intent from tactical control.

Strategic layer:

`Attack exposed eastern army.`

Tactical layer:

- route;
- formation;
- target selection;
- focus fire;
- engagement distance;
- retreat.

This preserves the practical value of stock tactical machinery while preventing tactical code from becoming the strategic brain.

---

## 3.26 Operations Room

Attack should be represented as a mission, not merely a command.

Mission classes include:

- raid;
- deny;
- defend;
- escort;
- contest;
- destroy;
- harass;
- probe;
- reposition;
- retreat.

Each operation has an objective, force requirement, target/area, timing, risk, and termination condition.

---

## 3.27 Map Control Room — NEW explicit strategic layer

Scouting tells the bot what is visible.

Map Control tells the bot what the map means.

Concepts:

- safe;
- controlled;
- contested;
- denied;
- exposed;
- strategically important;
- route-critical;
- resource-critical.

Vision, routes, chokepoints, resources, and territory are all treated as strategic assets.

---

## 3.28 Tempo Room — NEW

Tempo is the race to obtain the next meaningful capability before the opponent can respond.

Examples:

- Castle Age before enemy counter-tech;
- second production building before enemy reinforcement;
- siege before infantry mass arrives;
- raid before walls complete.

The tempo room converts time from a passive clock into a strategic resource.

---

## 3.29 Strategic Memory Room — NEW

Separate current state from historical learning.

Example:

`STATE: enemy currently has 8 knights.`

`MEMORY: opponent repeatedly transitions to cavalry after fast Castle.`

`MODEL: cavalry probability elevated.`

`FORECAST: next Castle transition likely to produce cavalry.`

Memory should store only information useful enough to affect future decisions.

---

## 3.30 Trade / Exchange Room

Preserve stock trade capability but integrate it into the resource portfolio.

Trade is a method of acquiring strategic resource flow, not merely a late-game button.

It should consider:

- resource bottleneck;
- route safety;
- infrastructure cost;
- expected throughput;
- military protection;
- alternative resource conversion.

---

## 3.31 Water Operations Room

Preserve naval control as a specialized operational domain beneath the common strategic spine.

The strategic layer should request capabilities such as:

- water control;
- transport;
- naval pressure;
- shoreline defense.

The water room handles actual naval implementation.

---

## 3.32 Game-State Assessment Room

Replace resignation as a narrow terminal check with a broader assessment of game viability.

Evaluate:

- economic viability;
- military viability;
- map control;
- technological gap;
- recovery potential;
- opponent momentum;
- resource access;
- win-condition progress.

Resignation becomes one possible consequence, not the room's entire purpose.

---

# 4. The final apartment topology

The recommended architecture is:

```text
                              WORLD
                                │
                                ▼
                         ┌─────────────┐
                         │  SENSORIUM  │
                         └──────┬──────┘
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 BELIEF      MAP DATA    HISTORY
                    │           │           │
                    └──────┬────┴──────┬────┘
                           ▼             ▼
                      THREATS       OPPORTUNITIES
                           │             │
                           └──────┬──────┘
                                  ▼
                         ┌────────────────┐
                         │ SITUATION MODEL│
                         └───────┬────────┘
                                 │
               ┌─────────────────┼─────────────────┐
               ▼                 ▼                 ▼
          OPPONENT MODEL      FORECAST         ATTENTION
               │                 │                 │
               └─────────────────┼─────────────────┘
                                 ▼
                          STRATEGIC POSTURE
                                 │
                                 ▼
                           OBJECTIVES
                                 │
                                 ▼
                           REQUIREMENTS
                                 │
                                 ▼
                            CONSTRAINTS
                                 │
                                 ▼
                            CAPABILITIES
                                 │
                                 ▼
                            CANDIDATES
                                 │
                                 ▼
                            ARBITRATION
                                 │
                                 ▼
                         STRATEGIC LEDGER
                                 │
                                 ▼
                            COMMITMENT
                                 │
                                 ▼
                            AUTHORIZATION
                                 │
                                 ▼
                            EXECUTION
                                 │
                                 ▼
                            VERIFICATION
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
                 EFFECTIVE                DEVIATION
                    │                         │
                    └────────────┬────────────┘
                                 ▼
                              RECOVERY
                                 │
                                 └──────────► REASSESS
```

Operational rooms below the strategic spine:

```text
ECONOMY / RESOURCE PORTFOLIO
PRODUCTION / CAPABILITY FACTORY
INFRASTRUCTURE
TECHNOLOGY
MILITARY COMMAND
TACTICAL CONTROL
OPERATIONS
TRADE
WATER
MAP CONTROL
```

Cross-cutting utilities:

```text
MAILBOX CONTRACTS
OWNERSHIP
GENERATIONS
EVIDENCE
CLOCKS
MEMORY
RESOURCE LEDGER
STRATEGIC LEDGER
```

---

# 5. The mailbox architecture

The mailbox concept is retained but modernized.

A mailbox is not merely a numeric location. Architecturally it is a contract.

Conceptual message:

```text
MESSAGE
├── TYPE
├── PAYLOAD
├── OWNER
├── GENERATION
├── VALID
├── CONFIDENCE
├── PRIORITY
├── CREATED_AT
└── EXPIRY / REASSESS CONDITION
```

The physical representation may eventually use primitive engine channels, but the architecture must never confuse the representation with the concept.

A room may:

`PUBLISH → another room becomes eligible → CONSUME → produce new state`.

This preserves the stock AI's proven distributed-controller pattern while removing accidental semantic ambiguity.

---

# 6. Dual-clock architecture

AEGIS uses two conceptual clocks.

## Controller clock

Controls:

- rule eligibility;
- reassessment;
- arbitration epochs;
- message freshness;
- commitment expiry;
- search scheduling.

## World clock

Represents:

- training;
- construction;
- research;
- movement;
- combat;
- object creation;
- resource accumulation.

The architecture must never infer world completion merely because controller time advanced.

---

# 7. State hierarchy

AEGIS state is conceptually layered:

```text
OBSERVATION
    ↓
CLASSIFICATION
    ↓
BELIEF
    ↓
FORECAST
    ↓
OBJECTIVE
    ↓
REQUIREMENT
    ↓
COMMITMENT
    ↓
EXECUTION STATE
    ↓
VERIFICATION
    ↓
STRATEGIC RESULT
```

This hierarchy prevents stale observations from masquerading as strategic decisions and prevents commands from masquerading as completed outcomes.

---

# 8. What we deliberately do NOT build

The architecture rejects:

- a fake neural network inside `.per`;
- a giant omniscient planner;
- one manager per unit;
- unnecessary object hierarchies;
- abstractions that only rename engine commands;
- mathematical optimization where simple thresholds are superior;
- dozens of independent state machines for trivial behaviors;
- duplicated rooms with overlapping authority;
- permanent state when a transient signal is sufficient;
- historical complexity preserved solely because stock uses it.

The test is always:

> **Does this make the AI play better, make a critical decision more reliable, or make a proven capability easier to control?**

If not, remove it.

---

# 9. Practical superiority targets

AEGIS should aim to surpass stock in the following dimensions without sacrificing stock capability:

| Capability | Stock strength | AEGIS target |
|---|---|---|
| Economy | adaptive allocation | allocation + explicit portfolio/opportunity cost |
| Threat response | strong compressed signals | threat + confidence + trajectory |
| Scouting | useful spatial control | useful spatial control + information value |
| Production | strong feasibility pipeline | capability-driven production |
| Technology | conditional research | benefit + timing + opportunity cost |
| Military | established attack/retreat machinery | mission-driven command |
| Recovery | distributed resets/restarts | explicit recovery state machine |
| Strategy | distributed implicit strategy | explicit strategic posture |
| Opponent | enemy-state reaction | opponent model + prediction |
| Opportunities | limited/implicit | explicit opportunity detection |
| Timing | timers and rule eligibility | explicit tempo reasoning |
| Map | searches/positioning | strategic map-control model |
| Memory | distributed historical state | selective strategic memory |
| Verification | implicit | explicit evidence ladder |
| State ownership | implicit/multiplexed | explicit contracts |
| Arbitration | distributed priorities | explicit strategic arbitration |

---

# 10. The first vertical slice

The architecture should be tested conceptually before implementation using:

## Cavalry Threat Containment

```text
OBSERVE
  ↓
CLASSIFY
  ↓
BELIEVE
  ↓
FORECAST
  ↓
THREAT
  ↓
OBJECTIVE
  ↓
REQUIREMENT
  ↓
CONSTRAINTS
  ↓
CAPABILITIES
  ↓
CANDIDATES
  ↓
ARBITRATION
  ↓
COMMIT
  ↓
RESOURCE RESERVATION
  ↓
EXECUTE
  ↓
VERIFY
  ↓
EFFECTIVE?
 ├── YES → MAINTAIN / REASSESS
 └── NO  → RECOVER / RE-ARBITRATE
```

This vertical slice deliberately exercises the architecture rather than merely testing camel production.

---

# 11. Architecture acceptance criteria

Layer 3A should not be considered architecturally complete until a game-domain walk-through can answer all of the following:

1. Where does every important observation enter?
2. Where is observation distinguished from belief?
3. Where is uncertainty represented?
4. Where is threat classified?
5. Where is opportunity detected?
6. Where is opponent behavior represented?
7. Where is future trajectory represented?
8. Where is strategic posture selected?
9. Where is an objective created?
10. Where are requirements derived?
11. Where are constraints propagated?
12. Where are alternative capabilities generated?
13. Where are alternatives evaluated?
14. Where is arbitration performed?
15. Where is a commitment recorded?
16. Where are resources reserved?
17. Where is execution authorized?
18. Where is the physical action issued?
19. Where is world-state completion verified?
20. Where is strategic effect verified?
21. Where does failure go?
22. Where does stale state expire?
23. Where does a new generation supersede an old decision?
24. Where does the system remember useful experience?
25. Where does the system reassess the whole situation?

If any answer is “somewhere in a giant rule file,” the architecture is not finished.

---

# 12. Relationship to Layer 2

Layer 2 froze the static ABI boundary and identified the candidate AEGIS scalar-goal namespace of `10000–15999`.

That namespace is **not allocated by this document**.

Architecture comes first.

The sequence is:

`ARCHITECTURAL CONCEPT → FIELD CONTRACT → OWNERSHIP → REPRESENTATION → EMPIRICAL ABI QUALIFICATION → IMPLEMENTATION`

Never reverse this sequence merely because a free-looking numeric channel exists.

---

# 13. Next architectural pass

The next pass should not write `.per` code.

It should perform a **full game-flow architectural walk-through**.

Recommended scenarios:

1. standard Dark Age opening;
2. fast Castle transition;
3. enemy cavalry opening;
4. enemy ranged transition;
5. early aggression;
6. defensive containment;
7. failed attack;
8. successful pressure;
9. economic recovery;
10. late-game resource exhaustion;
11. water contest;
12. trade transition;
13. opponent strategy reversal;
14. unexpected technology transition.

For each scenario, trace the information through every room and identify:

- missing room;
- duplicated authority;
- unnecessary state;
- ambiguous mailbox;
- missing transition;
- missing recovery path;
- impossible decision;
- timing hole;
- verification hole.

Only after those walkthroughs should the architecture be frozen enough to begin field-level ABI design.

---

# 14. Architectural conclusion

The stock AI should be treated as a **highly optimized historical reference implementation**, not as an architectural template to copy and not as obsolete code to discard.

Its enduring lesson is practical:

> primitive mechanisms can produce sophisticated game behavior when their interactions are carefully designed.

AEGIS should retain that lesson while removing the accidental complexity caused by primitive representation.

The intended final architecture is therefore:

**Stock capability preservation + conceptual decompression + explicit strategic reasoning + proactive opportunity detection + forecasting + formal commitment/verification + disciplined recovery.**

The apartment is not complete because it contains many rooms.

It is complete when every important game decision has a clear place to live, every room has one job, every mailbox has a contract, and the whole apartment can turn information into effective game action without hidden dependencies.

**STATUS: ARCHITECTURE PROTOTYPE — PRE-FURNITURE.**
