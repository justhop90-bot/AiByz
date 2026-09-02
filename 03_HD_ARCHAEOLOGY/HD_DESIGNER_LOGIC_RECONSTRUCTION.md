# HD Designer Logic Reconstruction

## Thesis

`AI (HD version).per` is evidence of a human-designed strategic model compressed
into a constrained rule language. The artifact should therefore be studied as
both software and intellectual history.

The practical objective is **returnability**: a future engineer should be able
to reopen the repository years later and reconstruct the code's behavior, its
control architecture, its game-theoretic assumptions, and the engineering
constraints that shaped its implementation.

## Who

The source identifies the artifact as the official HD/2013 Edition AI and
attributes its creation to Promiskuitiv and Archon. Attribution does not by
itself establish authorship of every later modification. The code contains
historical layering, comments identifying obsolete mechanisms, experimental
branches, debugging aids, and compatibility scaffolding. Therefore authorship
should be represented as an artifact lineage rather than assumed uniformity.

The relevant "who" questions are:

- who authored the original strategic concept;
- who implemented a rule family;
- who introduced later fixes or compatibility code;
- which subsystem owns a state variable;
- which subsystems override that state;
- which behavior is inherited from the engine rather than authored in AI code.

## What

The AI explicitly represents strategy as a collection of interacting state
variables rather than a single plan object. Important state includes strategy,
unit choice, control/resource mode, enemy strategy, position, attack status,
retreat state, threat information, targets, naval state, and timers.

This reveals an important conceptual decomposition:

`strategy` answers what broad mode is being pursued;
`unit` answers what capability supports it;
`control` answers what special constraint/reservation is active;
`enemy` answers what opponent state is believed to exist;
`position` answers where the strategic geometry places the player;
`attack/retreat` answers what military control state is currently legal;
`timers` answer when a state may be reconsidered or repeated.

## When

Time is represented at several levels:

- absolute game time;
- age and age-transition state;
- current-age time;
- timer-triggered events;
- pending asynchronous actions;
- periodic resets;
- delayed re-entry into strategic states.

This means the designer's model is not purely spatial or economic. It is
explicitly temporal: the same observation can imply different decisions at
different stages of a game.

## Where

Strategic logic is distributed across source sections. The major recovered
regions include navy initialization, superiority, strategy selection, boar
hunting, resource management/age-up, basics, research, siege, villagers/buildings,
units, farms/fishing, gatherer percentages, attack/retreat, human cooperation,
and later increase/strategic-number code.

A future archaeology pass must preserve both the original section location and
the semantic subsystem location. Source proximity is not equivalent to logical
ownership.

## Why — inferred model

The strongest recurring interpretation is that the designers were solving a
continuous control problem under a weak declarative rule substrate.

The game presents a changing state. The AI cannot simply issue an ideal plan
once because:

- the opponent adapts;
- resources arrive asynchronously;
- units die or complete training;
- buildings and technologies alter capability;
- map information is incomplete;
- military commitments create opportunity costs;
- attacks can fail or become temporarily unfavorable;
- rule firing can otherwise oscillate.

The designers therefore encoded state, feedback, reservations, and timers.

## Human strategic logic visible in the code

### 1. Strategy is conditional, not permanent

Strategy selection is repeatedly reconsidered in response to opponent state,
position, map, age, resource state, and military conditions. This is evidence
against a static-build-order conception of strategy.

### 2. Enemy actions are commitments

The AI observes concrete investments—units, military population, barracks,
stables, towers, castles, technology, and timing—and translates them into an
enemy-strategy classification. This is strategically meaningful because an
enemy commitment constrains what they can afford next.

### 3. Resources have opportunity cost

The resource-control mechanism shows explicit reservation behavior. The AI can
protect resources for a strategically important conversion instead of treating
resources as undifferentiated spendable inventory.

### 4. Military capability is state-dependent

Unit selection depends on enemy composition, strategic mode, technology, map,
and other state. A unit is therefore treated as a capability within a context,
not simply as an isolated counter.

### 5. Position changes economics and military logic

Flank/pocket classification is consumed by strategic rules. Position therefore
acts as an upstream variable affecting the feasible strategic set.

### 6. Retreat preserves future capability

The retreat controller does not merely represent fear. It can clear attack
state, establish retreat state, arm timers, and later restore offensive behavior.
This is consistent with preserving military capital and avoiding catastrophic
loss rather than maximizing immediate contact.

### 7. Timers are behavioral memory

A timer remembers that a decision was recently made. It prevents the controller
from repeatedly making the same decision every evaluation cycle. In control-
theoretic terms, this introduces temporal hysteresis and rate limiting.

### 8. Reset is not failure

The source contains explicit reset states that allow a temporary tactical
condition to be cleared without abandoning the broader strategic mode. This is
a key distinction between tactical interruption and strategic transition.

## Engineering logic behind the strategy

The designers repeatedly transform expensive high-dimensional observations into
small reusable state variables. This reduces repeated condition complexity and
allows later rules to reason over compact classifications.

The tradeoff is distributed authority: multiple rule families can write related
state. This is simultaneously a practical adaptation and a source of fragility.
It explains why the source can be strategically sophisticated while remaining
architecturally difficult to reason about.

## What the designers appear to optimize

The source suggests an objective broader than winning the next fight. Repeated
patterns indicate concern for:

- maintaining economic throughput;
- preserving military mass;
- timing attacks around capability windows;
- countering opponent commitments;
- protecting strategic resources;
- avoiding wasteful attacks against defensive structures;
- changing worker allocation when strategic mode changes;
- exploiting map topology;
- maintaining enough production/replacement capacity;
- coordinating with allies;
- preventing repetitive rule firing.

These should be tested against the complete writer-reader graph before being
promoted to formal strategic principles.

## Historical interpretation

The source should be read as a fossil record. Commented code, obsolete strategic
numbers, alternative branches, duplicated mechanisms, debug interfaces, and
special-case compatibility logic are not automatically noise. They can reveal
problems encountered during development and the solutions the authors considered.

Therefore archaeology must preserve:

`implemented behavior + intended behavior + abandoned behavior + workaround +
known failure + historical rationale`.

## AEGIS interpretation

The correct lesson is not to reproduce the HD architecture wholesale. Instead,
extract the underlying principles and re-express them using explicit ownership,
observation/fact separation, belief state, strategic intent, resource reservation,
production authority, command authorization, execution acknowledgement, and
verification/recovery.

The HD source is thus a strategic knowledge fossil and engineering case study.
Its greatest value is the bridge between human strategic reasoning and executable
rule-machine behavior.

## Completion criterion

This document is not complete until the repository can answer, subsystem by
subsystem, the seven questions:

1. What did the code do?
2. What state did it represent?
3. What caused the state transition?
4. What game problem did the mechanism solve?
5. What assumptions did the designer make?
6. What engine limitation shaped the implementation?
7. What should AEGIS preserve, reject, or generalize?
