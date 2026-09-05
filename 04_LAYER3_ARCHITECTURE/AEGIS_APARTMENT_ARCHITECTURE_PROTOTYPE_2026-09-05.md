# AEGIS Apartment Architecture Prototype

**Date:** 2026-09-05  
**Layer:** 3A — Architecture / Pre-furniture design  
**Status:** PROTOTYPE / ARCHITECTURAL DESIGN  
**Implementation:** NONE  
**Runtime:** NONE  
**Authority:** Architecture prototype; does not allocate runtime channels or authorize implementation.

## 0. Purpose

This document defines the first architectural prototype for the AEGIS bot after closure of Layer 2.

The central design metaphor is an apartment: Layer 2 established the building envelope, utilities, stock occupants, available mailbox space, and physical constraints. Layer 3A designs the apartment completely before a single piece of furniture is moved in.

The objective is not to reproduce the stock AI's file structure. It is to preserve every practically valuable capability demonstrated by the stock AI, remove complexity that exists primarily because the historical implementation was forced through primitive state channels, and add modern strategic capabilities that increase practical game-playing strength without creating abstraction for its own sake.

This is functional modernization, not rewrite-for-rewrite's-sake.

## 1. Design doctrine

### 1.1 Practical superiority is the objective

Every architectural component must answer a practical game-playing question:

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

### 1.2 Preserve proven practical behavior

The stock AI is a decades-refined reference implementation. Its constraints forced its authors to discover high-value techniques for resource allocation, escrow, production feasibility, threat compression, technology timing, scouting and spatial search, attack-group management, retreat and restart, construction control, trade, water control, timers, and compact state-channel communication.

AEGIS must preserve those capabilities.

### 1.3 Decompress, do not inflate

Stock often compresses several conceptual jobs into one primitive state channel because goals, strategic numbers, timers, searches, and rule interactions are limited and multiplexed.

AEGIS should expose concepts explicitly at the architectural level and only compress them when the actual machine representation requires it.

Target:

`MORE PRACTICAL FUNCTION / UNIT OF COMPLEXITY`

not:

`MORE CODE / UNIT OF COMPLEXITY`.

### 1.4 Separation of responsibility

- Sensors observe.
- Beliefs represent knowledge.
- Threats classify danger.
- Opportunities identify exploitable conditions.
- Strategy establishes posture and objectives.
- Requirements describe what must be achieved.
- Capabilities describe what the machine/game can provide.
- Candidates propose alternatives.
- Arbitration selects among alternatives.
- Commitment records a decision.
- Execution performs authorized actions.
- Verification determines what actually happened.
- Recovery handles deviation and failure.
- Memory records useful history.

### 1.5 No omniscient planner

AEGIS should not become one enormous planner that tries to solve the whole game every cycle. The preferred model is:

`shared strategic spine + specialized operational rooms + explicit mailbox contracts`.

## 2. Stock apartment: functional inventory

The stock package should be understood by function, not merely by filenames. The source tree contains specialized systems for at least:

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

The recovered cross-system topology is:

`ECONOMY → THREAT → PRODUCTION → TECHNOLOGY → MILITARY → MAP/POSITION → ATTACK → RECOVERY → ECONOMY`

with information/scouting feeding threat, map, and positioning systems.

## 3. Stock room review

### 3.1 Configuration & Bootstrap

**Stock job:** constants, initialization, civilization-specific configuration, strategic-number defaults, goals, opening conditions, and reset behavior.

**Keep:** yes.

**Modernize:** separate immutable configuration from current state and strategic policy.

### 3.2 Economy / Resource Control

**Stock job:** gatherer distribution, resource priorities, escrow, affordability conditions.

**Keep:** all practical behaviors.

**Modernize:** create an explicit Resource Portfolio distinguishing current stock, income, committed resources, reserved resources, discretionary resources, projected income, projected deficit, and time-to-affordability.

The strategic question becomes not merely `Do I have 450 food?` but `How much of that food is already committed and what capability should the remaining discretionary pool purchase?`

### 3.3 Escrow / Funding

Preserve escrow as a mechanism, but subordinate it to the Strategic Ledger / Resource Portfolio.

A reservation conceptually contains claimant, objective, amount, expected use time, priority, cancellation conditions, and release conditions.

### 3.4 Production / Capability Factory

**Stock job:** determine where/when units can be produced, check feasibility, and issue training commands.

Preserve the feasibility pipeline. Reframe production as acquisition of capability rather than a list of unit commands.

Example:

`train 3 camels` → `purchase additional anti-cavalry capability`.

The production layer then determines the legal physical implementation.

### 3.5 Infrastructure Planner

Preserve building construction, production infrastructure, defensive structures, town expansion, and placement/search behavior.

Classify infrastructure as:

- economic;
- military;
- defensive;
- technological;
- logistical;
- forward;
- transitional.

Every construction request should have a strategic reason.

### 3.6 Technology & Timing Planner

Preserve age advancement, research, escrow interaction, and feasibility.

Evaluate technology candidates against:

`benefit + timing + resource cost + opportunity cost + prerequisite effects + strategic need`.

A good technology can still be wrong now.

### 3.7 Threat Intelligence Center

Preserve the stock pattern:

`enemy composition → compact threat signal → response threshold → capability investment`.

Expand it with:

- threat type;
- severity;
- urgency;
- confidence;
- trajectory;
- counter-requirement;
- time-to-impact;
- geographic relevance.

Stock asks `What does the enemy have?` AEGIS should also ask `What is the enemy becoming?`

### 3.8 Scouting / Information

Preserve stock scouting, object searches, danger checks, spatial reasoning, movement, and route/pivot behavior.

Add **Information Value**:

> Scout to answer the question that most changes the decision.

The system should prioritize unresolved information by strategic value instead of treating all scouting targets equally.

### 3.9 Opponent Model — NEW

Maintain an evidence-weighted model of:

- civilization;
- demonstrated strategy;
- aggression tendency;
- defensive tendency;
- production preferences;
- transition tendencies;
- resource priorities;
- response patterns;
- likely next transition;
- confidence.

This is predictive context, not personality simulation.

### 3.10 Strategic Situation Model — NEW / CENTRAL

Synthesize:

- current state;
- threats;
- opportunities;
- objectives;
- constraints;
- resources;
- map control;
- opponent model;
- timing.

Output a **Strategic Posture**, such as defensive stabilization, economic expansion, timing attack, pressure, counterattack, recovery, all-in, consolidation, or transition.

Posture is a current interpretation, not a permanent strategy.

### 3.11 Opportunity Engine — NEW

Explicitly search for profitable situations:

- exposed economy;
- displaced enemy army;
- incomplete wall;
- isolated army;
- overextended production;
- temporary technology gap;
- exposed strategic resource;
- timing window.

Output opportunity, payoff, urgency, feasibility, and risk.

### 3.12 Forecast Engine — NEW

Convert snapshots into short-horizon trajectories.

Example:

`stable count 1 → 2 → 3` → `increasing cavalry production capacity`.

Forecasts remain confidence-weighted and short-horizon; this is not whole-game prediction.

### 3.13 Attention Manager — NEW

Prioritize:

1. imminent lethal threats;
2. decisive opportunities;
3. high-value unresolved uncertainty;
4. urgent commitments;
5. ordinary maintenance.

This is control-bandwidth management.

### 3.14 Objective Room

Make objectives explicit rather than allowing them to emerge only from distributed state.

Example:

`Survive enemy cavalry pressure` is an objective.

`Train camels` is a candidate response.

That distinction is mandatory.

### 3.15 Requirement Room — NEW explicit layer

Translate an objective into what must actually be achieved.

Example:

`contain cavalry` → `obtain sufficient anti-cavalry combat power near the threatened area before projected contact`.

This allows multiple capabilities to satisfy one requirement.

### 3.16 Constraint Room — NEW

Propagate prerequisites and conflicts before candidate selection:

- resources;
- prerequisites;
- production capacity;
- timing windows;
- existing commitments;
- delays and dependencies.

This is the bridge from strategic desire to executable possibility.

### 3.17 Capability Room

Represent strategic capabilities such as anti-cavalry power, ranged firepower, siege, map vision, fortification, economic throughput, mobility, and naval control.

A capability has prerequisites, cost, source, availability, throughput, time-to-effect, utility, scalability, and confidence.

### 3.18 Candidate Room

Generate several feasible ways to satisfy a requirement.

For cavalry, candidates may include spearmen, camels, walls, castle defense, counterraid, mixed army, or positional defense.

The textbook counter is not automatically the best response.

### 3.19 Arbitration Room

Resolve simultaneous demands such as cavalry threat + age-up + exposed gold + army opportunity + food shortage.

Evaluate urgency, strategic value, survival impact, payoff, resource cost, opportunity cost, time-to-effect, reversibility, confidence, and commitment conflict.

### 3.20 Strategic Ledger — NEW

Record strategic promises:

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

This prevents strategic drift.

### 3.21 Commitment Room

Once arbitration selects a candidate, create a formal commitment.

Minimum conceptual envelope remains:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Commitments are decisions authorizing execution; they are not commands.

### 3.22 Execution Room

Translate an authorized commitment into legal engine actions.

The executor is strategically ignorant: it answers whether an authorized action can be issued, not whether the strategy is good.

### 3.23 Verification Room

Preserve the evidence ladder:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

A command does not prove a world transition. A created unit does not prove strategic success.

Verification is therefore separated into control, world, and strategic-effect evidence.

### 3.24 Recovery & Resilience

Make the stock retreat/reset/restart family explicit.

Possible outcomes:

- success;
- partial success;
- delayed;
- blocked;
- failed;
- invalidated;
- superseded.

Possible responses:

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

### 3.25 Military Command

Separate strategic military intent from tactical control.

Strategic layer: `Attack exposed eastern army.`

Tactical layer: route, formation, target selection, focus fire, engagement distance, retreat.

Preserve useful stock tactical machinery without making it the strategic brain.

### 3.26 Operations Command

Represent attack as a mission:

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

Each operation has objective, force requirement, target/area, timing, risk, and termination condition.

### 3.27 Map Control — NEW explicit strategic layer

Scouting tells the bot what is visible. Map Control tells it what the map means.

Classify areas as:

- safe;
- controlled;
- contested;
- denied;
- exposed;
- strategically important;
- route-critical;
- resource-critical.

Vision, routes, chokepoints, resources, and territory are strategic assets.

### 3.28 Tempo Manager — NEW

Treat time as a strategic resource: who obtains the next meaningful capability first.

Examples include Castle timing, production timing, siege timing, and raids before defensive completion.

### 3.29 Strategic Memory — NEW

Separate current state from historical learning.

`STATE: enemy currently has 8 knights.`

`MEMORY: opponent repeatedly transitions to cavalry after fast Castle.`

`MODEL: cavalry probability elevated.`

`FORECAST: next Castle transition likely to produce cavalry.`

Store only history useful enough to affect future decisions.

### 3.30 Trade / Exchange

Preserve trade, but integrate it into the resource portfolio. Consider bottleneck resource, route safety, infrastructure cost, expected throughput, protection, and alternatives.

### 3.31 Water Operations

Preserve naval control as a specialized operational domain beneath the common strategic spine. The strategic layer requests capabilities; the water room handles naval implementation.

### 3.32 Game-State Assessment

Expand resignation into a broader viability assessment covering economic viability, military viability, map control, technological gap, recovery potential, opponent momentum, resource access, and win-condition progress.

Resignation is one possible consequence, not the room's whole purpose.

## 4. Final apartment topology

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

`ECONOMY / RESOURCE PORTFOLIO`  
`PRODUCTION / CAPABILITY FACTORY`  
`INFRASTRUCTURE`  
`TECHNOLOGY`  
`MILITARY COMMAND`  
`TACTICAL CONTROL`  
`OPERATIONS`  
`TRADE`  
`WATER`  
`MAP CONTROL`

Cross-cutting utilities:

`MAILBOX CONTRACTS / OWNERSHIP / GENERATIONS / EVIDENCE / CLOCKS / MEMORY / RESOURCE LEDGER / STRATEGIC LEDGER`

## 5. Mailbox architecture

The mailbox concept is retained but modernized.

A mailbox is architecturally a contract rather than merely a numeric location.

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

The physical representation may eventually use primitive engine channels, but the architecture must never confuse representation with concept.

The communication pattern remains:

`PUBLISH → consumer becomes eligible → CONSUME → produce new state`.

## 6. Dual-clock architecture

### Controller clock

Controls rule eligibility, reassessment, arbitration epochs, message freshness, commitment expiry, and search scheduling.

### World clock

Represents training, construction, research, movement, combat, object creation, and resource accumulation.

The architecture must never infer world completion merely because controller time advanced.

## 7. State hierarchy

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

This prevents stale observations from masquerading as strategic decisions and prevents commands from masquerading as completed outcomes.

## 8. What we deliberately do not build

Reject:

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

Test every component:

> Does this make the AI play better, make a critical decision more reliable, or make a proven capability easier to control?

If not, remove it.

## 9. Practical superiority targets

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

## 10. First vertical slice

The first architecture walkthrough is **Cavalry Threat Containment**:

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

The slice is deliberately broad enough to exercise the architecture rather than merely testing camel production.

## 11. Architecture acceptance criteria

Layer 3A is not complete until a game-domain walkthrough can answer:

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

If any answer is merely `somewhere in a giant rule file`, the architecture is not finished.

## 12. Relationship to Layer 2

Layer 2 froze the static ABI boundary and identified the candidate AEGIS scalar-goal namespace of `10000–15999`.

That namespace is **not allocated by this document**.

The sequence remains:

`ARCHITECTURAL CONCEPT → FIELD CONTRACT → OWNERSHIP → REPRESENTATION → EMPIRICAL ABI QUALIFICATION → IMPLEMENTATION`

Architecture comes first.

## 13. Next architectural pass

The next pass should remain pre-furniture and perform a full game-flow architectural walkthrough across:

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

For every scenario, identify missing rooms, duplicated authority, unnecessary state, ambiguous mailboxes, missing transitions, missing recovery paths, impossible decisions, timing holes, and verification holes.

Only after these walkthroughs should the architecture be frozen enough for field-level ABI design.

## 14. Architectural conclusion

The stock AI is a highly optimized historical reference implementation, not an architecture to copy and not obsolete code to discard.

Its enduring lesson is practical:

> primitive mechanisms can produce sophisticated game behavior when their interactions are carefully designed.

AEGIS should retain that lesson while removing accidental complexity caused by primitive representation.

The intended architecture is:

**Stock capability preservation + conceptual decompression + explicit strategic reasoning + proactive opportunity detection + forecasting + formal commitment/verification + disciplined recovery.**

The apartment is complete when every important game decision has a clear place to live, every room has one job, every mailbox has a contract, and the whole apartment can turn information into effective game action without hidden dependencies.

**STATUS: ARCHITECTURE PROTOTYPE — PRE-FURNITURE.**
