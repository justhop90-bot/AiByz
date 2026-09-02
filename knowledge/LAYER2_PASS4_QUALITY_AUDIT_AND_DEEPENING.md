# Layer 2 Pass 4 — Quality Audit and Deepening

## Purpose

This document is the second-order quality review of `LAYER2_GENERAL_AOE2_ONTOLOGY_PASS4.md`.

The question is not whether Pass 4 is comprehensive by word count. The question is whether an engineer returning six months later can reconstruct the conceptual system, resume the research, understand why each abstraction exists, identify what is proven versus inferred, and know exactly what evidence or experiment should come next.

### Six-month return test

A successful Pass 4 library must allow a returning engineer to answer:

1. What are the fundamental objects of strategic reasoning?
2. Which are directly observable and which are inferred?
3. How do observations become beliefs?
4. How do beliefs influence objectives?
5. How do objectives create capability and resource demand?
6. How do commitments consume optionality?
7. How do position and timing alter capability value?
8. How does production convert resources into future capability?
9. How does an opponent's capability create threats and transitions?
10. How does an action change the world and generate new evidence?
11. What constitutes success, warning, failure, and recovery?
12. Which claims are facts, principles, heuristics, or hypotheses?
13. What has been derived from historical source archaeology versus independent reasoning?
14. What remains untested?
15. What should be researched next?

Pass 4 now answers the majority of these questions. This audit identifies the remaining gaps and adds the conceptual structures needed to close them.

## Evidence boundary

The principal historical evidence is the recovered HD/2013 AI source and its archaeological reconstruction. Historical code is treated as evidence for attempted strategic reasoning, not as an authoritative specification of optimal play.

ADPromisory, ByzantineWarCouncil, and AiBuilder are explicitly excluded from the AEGIS strategic evidence lineage. They are failed/derived experimental material and must not be used to validate an AEGIS abstraction.

## Audit result

### Strengths confirmed

Pass 4 successfully established:

- a typed strategic vocabulary;
- capability as a central abstraction;
- separation of world state, observation, derived state, belief, objective, commitment, authorization, execution, and verification;
- explicit resource opportunity cost;
- production as a capability pipeline;
- position and timing as modifiers of effective capability;
- initiative as a control resource;
- transition as a first-class strategic object;
- conversion tax as a family of costs imposed on an opponent;
- information value;
- failure signatures and recovery;
- causal relationships between the major domains.

### Important omissions discovered

The original Pass 4 ontology was still thinner than the final AEGIS research standard in several areas:

1. **State dimensions were named but not normalized.** A capability needs a common state model: magnitude, readiness, availability, reliability, reach, persistence, sustainability, and confidence.
2. **Constraints were present conceptually but under-modeled.** Strategy is constrained by prerequisites, hard resource limits, queue capacity, population, geography, information, time, and mutually exclusive commitments.
3. **Dependencies were not sufficiently distinguished from correlations.** AEGIS must know whether A enables B, merely predicts B, or is required for B.
4. **Opportunity cost needed an explicit counterfactual definition.** The cost of an action is partly the value of the best materially plausible alternative it prevents.
5. **Commitment needed reversibility.** Some decisions are cheap to reverse; others permanently destroy optionality.
6. **Capability needed conversion efficiency.** Possessing capability is not enough; the controller must estimate how reliably it converts capability into objective progress.
7. **Initiative needed force-response structure.** Initiative is not merely attacking first. It is the ability to impose decision demand on the opponent while retaining meaningful alternatives.
8. **Threat needed exposure and deadline.** A threat without a target, mechanism, probability, and time-to-impact is incomplete.
9. **Belief needed belief aging and contradiction handling.** Old information should decay; conflicting observations should change confidence rather than simply overwrite state.
10. **Transition needed transition feasibility and transition competition.** Two favorable transitions may compete for the same resources, production capacity, or timing window.
11. **Strategic evaluation needed non-additive interactions.** Some advantages multiply rather than add: position can amplify military capability; information can amplify timing; production can amplify composition.
12. **Scale and timescale were missing.** Dark Age, Feudal, Castle, Imperial, tactical engagement, reinforcement cycle, and economic development operate on different temporal scales.
13. **Attention/decision load was underdeveloped.** A controller can have enough resources but insufficient decision bandwidth to exploit every opportunity simultaneously.
14. **Resilience was under-modeled.** A robust strategy is not merely high expected value; it can survive plausible disruptions and recover.
15. **Strategic identity was missing.** Civilization, map, matchup, and game phase change priors and capability costs without necessarily changing universal strategic laws.
16. **Negative space was missing.** What the opponent has not done, cannot have done, or would be expected to have done if a hypothesis were true can be strategically informative.
17. **Substitutability was missing.** Multiple capabilities can satisfy the same objective, and the planner should compare them by cost, timing, risk, and transition consequences.

The additions below address these omissions.

# I. Capability must have a state vector

A capability is not a binary possession.

A useful implementation-independent representation is:

```text
CAPABILITY
├── magnitude
├── readiness
├── availability
├── reliability
├── reach
├── persistence
├── sustainability
├── reinforcement
├── replacement
├── prerequisites
├── dependencies
├── counter-vulnerabilities
├── position dependence
├── timing dependence
└── confidence
```

### Magnitude

How much capability exists?

### Readiness

How quickly can it produce its intended effect?

### Availability

How much of the nominal capability is actually usable now?

### Reliability

How likely is the capability to accomplish its intended task under the current state?

### Reach

What geographic or strategic domain can it affect?

### Persistence

How long can the capability remain relevant without major replacement or resupply?

### Sustainability

How long can the actor maintain the capability given current resource and production flows?

This distinction is critical because nominal army size can remain constant while effective capability collapses through poor position, low readiness, reinforcement delay, or unsustainable resource demand.

# II. Capability conversion efficiency

The ontology needs a distinction between **capability** and **conversion**.

```text
CAPABILITY
     ↓
AVAILABLE ACTION
     ↓
OBJECTIVE PROGRESS
```

Define conceptually:

`conversion efficiency = objective progress / total strategic cost`

The denominator is broader than resources. It may include time, military exposure, production opportunity cost, positional exposure, replacement burden, and lost optionality.

A powerful army that cannot safely convert its strength into an objective may have lower strategic value than a smaller force with a better conversion path.

This is the conceptual foundation for the AEGIS conversion-tax doctrine.

# III. Constraints are first-class objects

A strategic decision should be modeled as:

```text
DESIRED TRANSITION
        ↓
AVAILABLE OPTIONS
        ↓
HARD CONSTRAINTS
        ↓
SOFT CONSTRAINTS
        ↓
RESOURCE / TIME / CAPACITY COMPETITION
        ↓
FEASIBLE COMMITMENTS
```

### Hard constraints

Examples include:

- age requirements;
- technology prerequisites;
- building prerequisites;
- population limits;
- unavailable resources;
- unavailable production infrastructure;
- inaccessible geography;
- impossible timing.

### Soft constraints

Examples include:

- preferred reserve levels;
- acceptable exposure;
- desired army preservation;
- target economic stability;
- preferred timing margins.

The planner must distinguish “impossible” from “possible but strategically undesirable.”

# IV. Opportunity cost requires a counterfactual

A resource expenditure should not be evaluated solely against zero expenditure.

The proper conceptual question is:

> What is the best materially plausible alternative use of this scarce resource during the relevant decision horizon?

Thus:

`opportunity cost = value(best foregone feasible alternative)`

This implies that opportunity cost is state-dependent and horizon-dependent.

The same 100 food can have radically different strategic value at different moments because the available alternatives and timing windows differ.

# V. Commitment reversibility

Commitments should carry a reversibility class:

```text
REVERSIBILITY
├── reversible immediately
├── reversible with small cost
├── reversible with substantial cost
├── effectively irreversible
└── irreversible
```

Examples of relatively reversible decisions include some short-term allocation changes.

Examples of increasingly irreversible commitments include infrastructure investment, technology paths, composition massing, exposed attacks, and strategic transitions whose resources cannot be recovered.

The more irreversible the commitment, the stronger the evidence required before execution should generally be.

# VI. Dependencies versus correlations

The ontology must distinguish:

### Requirement

A must exist for B to be possible.

`stable -> cavalry production`

### Enabler

A increases B's available capability.

`technology -> military capability`

### Modifier

A changes the value or effectiveness of B.

`position -> capability value`

### Predictor

A provides evidence that B is likely.

`observed stable count -> cavalry hypothesis`

### Correlation

A and B commonly occur together without establishing a causal relationship.

This distinction prevents historical patterns from becoming false causal laws.

# VII. Belief dynamics

A belief should have a temporal lifecycle:

```text
HYPOTHESIS
   ↓
SUPPORTED
   ↓
CONFIRMED / STRENGTHENED
   ↘
    CONTRADICTED
       ↓
    DEGRADED
       ↓
    REPLACED / RECOVERED
```

Each belief should track:

- creation time;
- last supporting observation;
- last contradictory observation;
- confidence;
- source quality;
- expected next evidence;
- expected transition;
- expiration/aging policy.

### Negative evidence

Absence can be informative.

If a hypothesis predicts that a prerequisite structure should exist by a deadline and repeated scouting fails to observe it, confidence should decline.

Negative evidence is not equivalent to proof of absence, because visibility is incomplete. Its strength depends on the probability that the object would have been observed if present.

# VIII. Threat must be typed, probabilistic, and temporal

A threat should contain:

```text
THREAT
├── target
├── mechanism
├── magnitude
├── probability
├── time-to-impact
├── required enemy capability
├── evidence
├── confidence
├── mitigation cost
└── consequence
```

This changes the question from:

> “Is the enemy dangerous?”

to:

> “What objective is threatened, by what mechanism, with what probability, and before what deadline?”

# IX. Transition competition

Transitions compete.

Suppose an actor can:

- add production;
- research technology;
- expand economy;
- mass military;
- fortify;
- scout;

but cannot fully fund all of them simultaneously.

The planner must therefore reason over a **transition frontier**:

```text
CURRENT STATE
     ↓
{T1, T2, T3, T4, T5}
     ↓
resource competition
production competition
position competition
timing competition
     ↓
feasible transition set
```

This is a deeper reason why strategy cannot be reduced to a build-order lookup.

# X. Substitutability and objective satisfaction

An objective may have several capability solutions.

```text
OBJECTIVE: protect gold
       ├── walls
       ├── defensive army
       ├── forward pressure
       ├── resource denial elsewhere
       └── relocation / alternate economy
```

The planner should compare substitutes rather than assuming one canonical solution.

This provides the conceptual basis for adaptive strategy under unusual maps and matchups.

# XI. Initiative is decision-set control

Initiative should be defined more precisely than “attacking first.”

A player has initiative when their actions materially constrain the opponent's next decision while preserving meaningful alternatives for themselves.

Thus initiative depends on:

- response demand imposed;
- opponent response time;
- number of viable opponent responses;
- cost of those responses;
- actor's own remaining options;
- ability to change direction.

A player can be attacking without having initiative if the attack is predictable, low-impact, and easily answered.

# XII. Strategic advantage is relational

Advantages should be modeled relative to the opponent and objective.

Examples:

- military advantage;
- economic advantage;
- production advantage;
- technological advantage;
- positional advantage;
- information advantage;
- timing advantage;
- initiative advantage;
- resilience advantage.

A raw advantage becomes strategically meaningful only when it can be converted into objective progress or denial.

# XIII. Non-additive interactions

The simple strategic value equation in Pass 4 is a useful conceptual starting point but is incomplete because strategic dimensions interact.

Examples:

```text
POSITION × MILITARY
INFORMATION × TIMING
PRODUCTION × COMPOSITION
ECONOMY × SUSTAINABILITY
INITIATIVE × RESPONSE_COST
MAP_CONTROL × RESOURCE_ACCESS
```

Therefore the eventual evaluation system should permit interaction terms or structured causal evaluation rather than assuming all dimensions are independent additive scores.

# XIV. Timescale hierarchy

Strategic reasoning occurs across nested timescales:

```text
GAME
 └── PHASE / AGE
      └── STRATEGIC PLAN
           └── TRANSITION
                └── TIMING WINDOW
                     └── ENGAGEMENT
                          └── ACTION
                               └── OBSERVATION
```

A decision can be locally optimal and strategically wrong because it optimizes the wrong timescale.

For example, a tactically favorable engagement may consume the army needed for a critical upcoming transition.

The controller must therefore ask:

> Optimal over what horizon?

# XV. Resilience and robustness

Expected value alone is insufficient.

A strategy should also be evaluated by how it behaves under plausible disruption:

- unexpected enemy composition;
- failed attack;
- resource denial;
- lost production building;
- scouting error;
- delayed technology;
- reinforcement interruption;
- map-control loss.

A robust strategy maintains acceptable outcomes across a range of plausible states.

Conceptually:

`robustness = acceptable performance under state perturbation`

This should become a first-class strategic property rather than an accidental benefit.

# XVI. Decision/attention budget

The ontology should recognize that an actor cannot execute unlimited independent plans simultaneously.

A decision may consume:

- resource budget;
- production budget;
- military attention;
- scouting attention;
- spatial attention;
- planning complexity.

This is especially important for an AI because excessive parallelism can create conflicting commitments even when every individual commitment looks reasonable.

AEGIS should eventually distinguish:

`can afford` from `can coordinate reliably`.

# XVII. Strategic identity and priors

Universal strategic laws do not imply universal policy values.

The following alter priors and costs:

- civilization;
- matchup;
- map type;
- starting conditions;
- game phase;
- difficulty/rule environment;
- known opponent tendencies.

These should modify the model rather than redefine the underlying ontology.

Thus:

`ontology = stable vocabulary`

while:

`priors/policies = context-dependent parameters`.

# XVIII. Objective hierarchy and utility conflicts

Objectives must be partially ordered rather than treated as one flat list.

A useful hierarchy is:

```text
SURVIVAL
   ↓
PRESERVE CORE CAPABILITY
   ↓
STABILIZE ECONOMY
   ↓
SECURE POSITION / RESOURCES
   ↓
ESTABLISH CAPABILITY ADVANTAGE
   ↓
DENY ENEMY TRANSITION
   ↓
CONVERT ADVANTAGE
   ↓
END GAME
```

This is not a universal fixed sequence. Higher-level objectives can temporarily yield to urgent lower-level constraints.

The important concept is **priority under conflict**.

# XIX. Strategic evaluation should include the alternative

A decision is better evaluated as:

```text
VALUE(action)
    compared with
VALUE(best feasible alternative)
```

This is stronger than assigning an absolute score to each action independently.

The planner is fundamentally solving a constrained choice problem.

# XX. New central model

After this quality pass, the ontology's central abstraction becomes:

```text
STATE
├── observable world
├── derived state
├── beliefs / uncertainty
├── capabilities
├── objectives
├── commitments
├── constraints
├── reserves / optionality
├── threats
├── transitions
├── timing windows
├── initiative
└── decision budget

DECISION
├── objective served
├── capability changed
├── resources consumed
├── constraints satisfied/violated
├── alternatives foregone
├── optionality consumed
├── timing window affected
├── opponent response induced
├── expected conversion
├── risk / uncertainty
└── failure signature

RESULT
├── world-state change
├── observed consequence
├── belief update
├── objective update
├── commitment update
└── next transition frontier
```

This is the stronger six-month-return representation of the strategic system.

# XXI. What Pass 4 now means

Pass 4 should be considered **ontology foundation complete, calibration incomplete**.

We now have enough conceptual structure to proceed without prematurely implementing the runtime.

The remaining work is no longer primarily “add more nouns.” It is to determine which relationships and values survive empirical testing.

## Foundation complete

- strategic entities;
- state hierarchy;
- causal vocabulary;
- capability model;
- production model;
- resource/opportunity-cost model;
- commitment/optionality;
- information/belief model;
- threat model;
- initiative;
- timing;
- transitions;
- conversion taxes;
- failure/recovery;
- context/priors;
- robustness;
- alternative comparison.

## Calibration incomplete

- exact capability metrics;
- marginal resource valuation;
- transition probabilities;
- belief update rates;
- timing-window valuation;
- initiative valuation;
- conversion efficiency estimation;
- robustness scoring;
- interaction terms;
- decision-budget costs.

# XXII. Required cross-validation matrix for Pass 5

Each major ontology relationship should receive a research record with:

| Field | Requirement |
|---|---|
| Claim | Exact proposition being tested |
| Ontology relation | Entities/relationship involved |
| Historical evidence | Relevant source archaeology |
| Independent rationale | Why the claim should hold in AoE2 |
| Observable signals | What runtime can measure |
| Hidden variables | What must be inferred |
| Context | Civ/map/age/matchup restrictions |
| Counterexample | State where the claim may fail |
| Test | Experiment/replay analysis needed |
| Metric | What constitutes support/refutation |
| Falsifier | Evidence that would reject it |
| Status | FACT/PRINCIPLE/HEURISTIC/HYPOTHESIS |
| AEGIS consequence | Required abstraction or architecture |

## Pass 5 objective

Pass 5 is therefore not “more documentation.” It is **causal stress testing**.

The research loop becomes:

`claim -> evidence -> counterexample -> experiment -> measurement -> adjudication -> ontology revision -> implementation requirement`.

That is the point at which the strategic library becomes an engineering-grade theory rather than a collection of intelligent observations.

## Final quality determination

Pass 4, after this audit, satisfies the six-month return standard at the **conceptual-foundation level**.

A returning engineer should now be able to reconstruct the architecture of the strategic reasoning model and understand what remains unknown without reopening the historical implementation.

The next major risk is no longer conceptual shallowness. It is **unvalidated assumptions**.

Therefore Pass 5 should aggressively attack the ontology rather than expand it indiscriminately.
