# Layer 2 — General AoE2 Strategic Ontology, Pass 4

## Purpose

This pass converts recovered historical strategic knowledge into an implementation-independent ontology of strong AoE2 reasoning.

The source is evidence, not a specification. The objective is to identify the objects, states, relationships, transitions, constraints, and measurable quantities that a strong controller must reason about regardless of whether the implementation is historical rules, a modern symbolic controller, or a future AEGIS runtime.

The central transformation is:

`historical control event -> strategic principle -> general AoE2 concept -> ontology -> measurable state -> decision policy`

This document deliberately does **not** reproduce historical source code. Small source snippets may be used as archaeological exhibits in dedicated casebooks when they materially clarify a concept.

## Evidence boundary

Primary evidence is the recovered HD/2013 AI source and the derived archaeology records under `03_HD_ARCHAEOLOGY/`.

ADPromisory, ByzantineWarCouncil, and AiBuilder are excluded from the evidence base. They are failed/derived experimental material and do not establish AEGIS strategy or architecture.

## Epistemic classes

Every ontology concept should eventually be marked as one of:

- `MECHANICAL_FACT` — directly established by game/engine evidence.
- `OBSERVABLE` — directly measurable from available game state.
- `DERIVED_STATE` — computed from observations.
- `BELIEF` — uncertain model of hidden/opponent state.
- `STRATEGIC_PRINCIPLE` — generalized causal rule about strong play.
- `HEURISTIC` — useful but tunable decision approximation.
- `HYPOTHESIS` — plausible but requiring empirical validation.
- `ENGINE_CONSTRAINT` — limitation imposed by the execution substrate.

The ontology must not silently convert a heuristic into a fact.

# I. Ontology architecture

The strategic world can be represented as interacting domains rather than isolated categories:

```text
WORLD
├── Environment
│   ├── Map
│   ├── Geography
│   ├── Resources
│   └── Visibility
├── Actors
│   ├── Self
│   ├── Opponent
│   └── Allies
├── Capability
│   ├── Economic
│   ├── Military
│   ├── Production
│   ├── Technology
│   ├── Position
│   └── Information
├── Control
│   ├── Objective
│   ├── Commitment
│   ├── Constraint
│   ├── Reservation
│   ├── Initiative
│   └── Timing Window
└── Epistemic State
    ├── Observation
    ├── Belief
    ├── Hypothesis
    ├── Confidence
    └── Expected Transition
```

The important point is that these domains are coupled. A military capability consumes resources; resources constrain production; production changes capability; capability changes map control; map control changes resource access; observations change beliefs; beliefs change objectives and commitments; commitments change future options.

# II. Core entities

## 1. Actor

An actor is a player-controlled strategic system: self, opponent, or ally.

Attributes:

- civilization;
- age;
- economy;
- technology;
- production infrastructure;
- military capability;
- map position/control;
- known objectives;
- current commitments;
- reserves;
- vulnerabilities;
- uncertainty.

Relationships:

`Actor owns Capability`

`Actor makes Commitment`

`Actor pursues Objective`

`Actor occupies Position`

`Actor generates Observation`

`Actor responds to Threat`

## 2. Resource

A resource is not merely a quantity.

State should distinguish:

- stock;
- income rate;
- expenditure rate;
- committed amount;
- reserved amount;
- immediately available amount;
- projected amount;
- acquisition difficulty;
- conversion opportunities;
- opportunity cost.

Relationships:

`Resource enables Capability`

`Resource funds Production`

`Resource funds Technology`

`Resource funds Infrastructure`

`Resource is reserved for Commitment`

`Resource value changes with Timing Window`

### General law

**The strategic value of a resource is conditional on what that resource can enable, deny, or preserve next.**

This generalizes the historical resource-control concept into a broader opportunity-cost model.

## 3. Capability

Capability is the preferred strategic object over raw unit count.

A capability answers:

> What can this actor reliably do in the current state?

Examples:

- defend against cavalry;
- raid exposed economy;
- deny a resource;
- break a wall;
- contest a location;
- produce siege;
- sustain a prolonged fight;
- reinforce quickly;
- threaten a timing attack;
- transition to Imperial technology.

A capability depends on:

`composition + technology + production capacity + resources + position + readiness + reinforcement + timing`.

Thus two armies with identical unit counts can have different strategic capability.

## 4. Production Capacity

Production capacity is the ability to convert resources and infrastructure into future capability.

Attributes:

- buildings;
- active queues;
- available queue slots;
- production rates;
- prerequisites;
- resource throughput;
- reinforcement distance/time;
- replacement capacity;
- bottlenecks.

General law:

**Current military power is partly a function of future reinforcement capacity.**

## 5. Technology

Technology is a capability investment.

Attributes:

- cost;
- research time;
- immediate benefit;
- scaling benefit;
- dependencies;
- composition dependency;
- production dependency;
- counter effect;
- transition effect;
- opportunity cost.

Technology should therefore be evaluated as an investment into a future capability state rather than as a checklist.

## 6. Position

Position represents strategic geometry.

Attributes:

- location;
- access;
- exposure;
- defensive value;
- retreat routes;
- reinforcement distance;
- resource access;
- attack routes;
- choke value;
- vision value;
- control value.

General law:

**Position modifies the effective value of every capability that depends on geography.**

## 7. Information

Information is knowledge about the world and opponent.

Attributes:

- observation;
- age of observation;
- visibility;
- confidence;
- source quality;
- contradiction;
- inferred state;
- expected value of additional information.

General law:

**Information is economically valuable when it changes the expected value of available decisions.**

## 8. Belief

A belief is an uncertain model of hidden state.

A mature opponent belief should include:

- hypothesis;
- probability/confidence;
- supporting observations;
- contradictory observations;
- expected next transition;
- required resources;
- production prerequisites;
- timing window;
- vulnerability;
- alternative hypotheses.

A belief must never be treated as an observation.

## 9. Objective

An objective is a desired world-state change.

Examples:

- survive;
- stabilize economy;
- secure a resource;
- establish map control;
- deny enemy transition;
- preserve military capital;
- force enemy defensive investment;
- break production;
- obtain a timing window;
- convert initiative into decisive advantage;
- end the game.

Objectives should be hierarchical.

## 10. Commitment

A commitment is a strategic decision that consumes resources, time, production, position, information, or optionality.

Examples:

- adding production buildings;
- investing in technology;
- massing a composition;
- attacking;
- expanding;
- contesting a resource;
- transitioning civilizations/ages/technologies;
- concentrating forces.

Every commitment has:

`cost + expected payoff + duration + prerequisites + opportunity cost + exit condition + failure signature`.

## 11. Threat

Threat is typed rather than scalar.

Possible dimensions:

- military;
- economic;
- technological;
- positional;
- production;
- timing;
- information;
- objective-level.

A threat should answer not merely “how dangerous?” but:

> Dangerous to what, through which mechanism, within what time window?

## 12. Initiative

Initiative is control over the sequence of decisions.

State includes:

- who currently forces a response;
- expected next commitment;
- response time;
- ability to change the opponent's feasible choices;
- tempo advantage;
- cost of surrendering initiative.

Initiative is therefore a strategic resource.

## 13. Timing Window

A timing window is an interval during which an action or capability has unusually favorable strategic value.

Attributes:

- opening time;
- closing condition;
- preparation time;
- enemy reaction time;
- expected capability delta;
- required commitment;
- risk of missing the window.

Examples:

`technology advantage window`

`reinforcement window`

`enemy transition vulnerability window`

`economic vulnerability window`.

## 14. Reserve / Optionality

Reserve is unused capacity that preserves future choices.

It includes:

- unspent resources;
- uncommitted production capacity;
- surviving military mass;
- undisclosed information;
- available map routes;
- alternative technologies;
- uncommitted strategic direction.

Optionality is the value of those remaining choices.

## III. Causal relationships

The ontology becomes useful when relationships are explicit.

```text
RESOURCE
  enables -> CAPABILITY
  funds -> COMMITMENT
  is_reserved_for -> OBJECTIVE
  has -> OPPORTUNITY_COST

CAPABILITY
  enables -> OBJECTIVE
  constrains -> OPPONENT_OPTIONS
  depends_on -> PRODUCTION
  depends_on -> TECHNOLOGY
  depends_on -> POSITION
  consumes -> RESOURCE

PRODUCTION
  creates -> FUTURE_CAPABILITY
  requires -> RESOURCE
  requires -> INFRASTRUCTURE
  is_limited_by -> BOTTLENECK

TECHNOLOGY
  modifies -> CAPABILITY
  enables -> TRANSITION
  consumes -> RESOURCE
  creates -> TIMING_WINDOW

POSITION
  modifies -> CAPABILITY_VALUE
  modifies -> RESOURCE_ACCESS
  modifies -> REINFORCEMENT_COST
  modifies -> ENGAGEMENT_VALUE

OBSERVATION
  updates -> BELIEF
  reduces -> UNCERTAINTY

BELIEF
  predicts -> TRANSITION
  changes -> OBJECTIVE_PRIORITY
  changes -> ACTION_SELECTION

COMMITMENT
  consumes -> RESOURCE
  consumes -> TIME
  consumes -> PRODUCTION_CAPACITY
  destroys -> OPTIONALITY
  creates -> VULNERABILITY

ACTION
  changes -> WORLD_STATE
  produces -> OBSERVATION

FAILURE
  invalidates -> BELIEF_OR_EXPECTATION
  triggers -> RECOVERY
  may_preserve -> STRATEGIC_OBJECTIVE

INITIATIVE
  changes -> OPPONENT_DECISION_SET
  creates -> RESPONSE_DEMAND
```

# IV. State hierarchy

A strong controller should distinguish at least these layers:

```text
RAW WORLD STATE
      ↓
OBSERVATIONS
      ↓
DERIVED FACTS
      ↓
BELIEFS / HYPOTHESES
      ↓
STRATEGIC STATE
      ↓
OBJECTIVES
      ↓
COMMITMENTS
      ↓
AUTHORIZED ACTIONS
      ↓
EXECUTION
      ↓
OBSERVED RESULT
      ↓
BELIEF UPDATE
```

This prevents a major conceptual error: treating an intention as though it were a fact about the world.

# V. Strategic capability model

The strategic unit should be capability rather than unit.

```text
CAPABILITY
├── required objective
├── supporting composition
├── technology prerequisites
├── production prerequisites
├── resource demand
├── map requirements
├── preparation time
├── readiness
├── reinforcement rate
├── replacement rate
├── counter-vulnerability
├── transition path
└── confidence
```

This enables reasoning such as:

> “The opponent has 12 cavalry units”

becoming:

> “The opponent has a developing mobility/raid capability whose next requirements probably include additional stable production, food/gold throughput, and a favorable mobility window.”

That is strategically richer because it predicts what the opponent must do next.

# VI. Production ontology

Production should be represented as a pipeline:

```text
OBJECTIVE
  ↓
REQUIRED CAPABILITY
  ↓
COMPOSITION
  ↓
PRODUCTION CAPACITY
  ↓
PREREQUISITES
  ↓
RESOURCE DEMAND
  ↓
RESOURCE ALLOCATION
  ↓
QUEUE
  ↓
TRAINING
  ↓
REINFORCEMENT
  ↓
READINESS
  ↓
REPLACEMENT
```

This reveals why a “train unit X” decision is usually downstream of several strategic decisions.

A production bottleneck can exist even when resources are abundant.

# VII. Counter ontology

A counter should not be modeled as:

`unit A counters unit B`.

The stronger model is:

```text
OPPONENT CAPABILITY
      ↓
VULNERABILITY
      ↓
AVAILABLE COUNTER CAPABILITIES
      ↓
COUNTER COST
      ↓
COUNTER TIMING
      ↓
COUNTER POSITION
      ↓
COUNTER TRANSITION
      ↓
OPPONENT RESPONSE
```

A counter is good when its total strategic conversion efficiency is favorable, not merely when its nominal combat interaction is favorable.

# VIII. Transition ontology

The game is a sequence of state transitions.

A transition has:

- source state;
- trigger;
- prerequisites;
- commitment;
- preparation time;
- capability delta;
- resource delta;
- positional delta;
- information change;
- opponent response;
- expected result;
- failure signature;
- recovery;
- destination state.

General principle:

**Strong play is partly the ability to enter favorable transitions before the opponent can invalidate them and to deny the opponent's favorable transitions.**

# IX. Resource-tax ontology

A strategic action can impose several taxes on the opponent:

- resource tax;
- production tax;
- timing tax;
- positional tax;
- information tax;
- attention/decision tax;
- replacement tax;
- transition tax.

This generalizes the AEGIS concept of the **conversion tax**.

The strongest counter may therefore be one that forces the opponent to spend resources on a defense that does not advance their primary objective.

# X. Information-value ontology

Information should be valued by decision impact.

A useful conceptual quantity is:

`Value of Information ≈ expected improvement in decision outcome - acquisition cost`

Acquisition cost includes:

- scout production;
- scout travel time;
- exposure;
- opportunity cost;
- attention/processing budget;
- delayed action.

This prevents the controller from treating all scouting as free.

# XI. Failure ontology

Failure should preserve information.

For every major commitment:

```text
PLAN
├── expected result
├── success signature
├── warning signature
├── failure signature
├── abort condition
├── fallback objective
└── recovery transition
```

A failed attack, for example, should not automatically erase the strategic objective. It should update beliefs about the feasibility and cost of the current transition.

# XII. Strategic evaluation ontology

A decision should eventually be evaluated across multiple dimensions:

```text
Strategic Value ≈
  military gain
+ economic gain
+ map gain
+ technology gain
+ production gain
+ information gain
+ initiative gain
+ reserve preservation
- resource cost
- production opportunity cost
- timing cost
- transition cost
- replacement cost
- exposure
- uncertainty
```

This is a conceptual evaluation function, not yet a calibrated numerical formula.

# XIII. The ontology's central causal graph

The emerging general theory can be compressed into:

```text
INFORMATION
    ↓
BELIEF
    ↓
OBJECTIVE PRIORITY
    ↓
CAPABILITY REQUIREMENT
    ↓
RESOURCE / PRODUCTION DEMAND
    ↓
COMMITMENT
    ↓
POSITION + TIMING + EXECUTION
    ↓
WORLD-STATE CHANGE
    ↓
OPPONENT RESPONSE
    ↓
NEW INFORMATION
    ↓
UPDATED BELIEF
```

This is the strategic loop.

The important consequence is that **strategy is not a selection from a list of builds. It is controlled transformation of a changing state under uncertainty and resource constraints.**

# XIV. What this pass adds to the ontology

The previous ~30% ontology had the correct top-level domains but lacked sufficient internal structure.

Pass 4 adds:

1. typed entities;
2. state layers;
3. causal relationships;
4. capability as a central abstraction;
5. commitment and optionality;
6. typed threats;
7. initiative;
8. timing windows;
9. production pipelines;
10. transition structure;
11. resource-tax structure;
12. information value;
13. failure/recovery semantics;
14. strategic evaluation dimensions.

The ontology is therefore no longer merely a taxonomy. It is becoming a **causal strategic ontology**.

# XV. What remains incomplete

This pass does not yet establish calibrated quantitative values for:

- capability strength;
- resource marginal value;
- timing-window value;
- information value;
- initiative value;
- conversion efficiency;
- transition cost;
- replacement cost;
- uncertainty penalties.

It also does not yet fully enumerate civilization-specific modifications, map-generation effects, or empirical competitive priors.

Those belong in subsequent cross-validation and specialization work.

# XVI. Next research target

The next step should be **Cross-Validation and Causal Stress Testing**.

For each major ontology relationship, ask:

1. Does the historical source exhibit it?
2. Does independent AoE2 game knowledge support it?
3. Can it be measured from runtime observations?
4. Can a counterexample invalidate it?
5. Is it universal or context-dependent?
6. Is it a law, heuristic, or hypothesis?
7. What would falsify it?
8. What runtime state would AEGIS require to represent it?

The objective is to prevent elegant ontology from becoming unfalsifiable philosophy.

## Current determination

**Pass 4 establishes the first serious implementation-independent strategic ontology for AEGIS.**

The major advance is the shift from domain labels to causal entities and relationships. This provides the conceptual substrate for the opponent model, transition engine, resource-tax model, initiative model, and eventually Byzantine doctrine.
