# AEGIS Layer 2 — Pass 43
# Historical Strategic Control-State Atlas

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory archaeology  
**Predecessors:** Pass 12 cross-system control graph; Passes 35–42 evidence/control audits  
**Primary source:** verified `AI (HD version).per` + verified Promisory modules  
**Runtime authority:** Layer-1 current-build machine evidence  
**Status:** PASS — strategic control map substantially reconstructed; unresolved semantics explicitly retained  
**Implementation status:** **ZERO**. No `.per` implementation is created or authorized by this pass.

---

## 0. Boundary condition

This pass is deliberately research-only.

Layer 2 is being used to understand the existing AI's code, strategy, state model, and Byzantine-relevant behavior. Architecture construction and executable `.per` work remain Layer 3 activities.

The purpose of Pass 43 is therefore not to design the replacement controller. It is to reconstruct the control topology that a future Layer-3 design must understand before it touches the runtime.

The central question is:

```text
STATE
 ↓
WHO WRITES IT?
 ↓
HOW IS IT TRANSFORMED?
 ↓
WHO READS IT?
 ↓
WHAT DOES IT CONTROL?
 ↓
WHAT RESETS IT?
 ↓
WHAT TIMER / TRANSITION RE-ENABLES IT?
 ↓
WHAT OTHER CONTROLLERS DEPEND ON IT?
```

A state channel is not considered understood merely because its definition is known. A useful archaeological closure requires its lineage, consumers, side effects, resets, and dependencies to be traced.

---

# 1. Executive finding

The historical AI is best understood as a **distributed state machine composed of interacting control channels**, not as a single planner and not as a collection of independent scripts.

The strongest control topology reconstructed in this pass is:

```text
                 ┌──────────────┐
                 │  OBSERVATION │
                 └──────┬───────┘
                        ↓
              ┌──────────────────┐
              │ CLASSIFICATION / │
              │ COMPRESSION      │
              └────────┬─────────┘
                       ↓
             ┌────────────────────┐
             │ STRATEGIC STATE    │
             │ goals / SN / flags │
             └─────────┬──────────┘
                       ↓
          ┌────────────┼─────────────┐
          ↓            ↓             ↓
       ECONOMY     PRODUCTION      MILITARY
          │            │             │
          └────────────┼─────────────┘
                       ↓
                  ACTION / SEARCH
                       ↓
                 WORLD INTERACTION
                       ↓
                RESET / REASSESS
                       └──────→ STATE
```

The important archaeological discovery is the **density of cross-domain state reuse**. A state written in one module is frequently consumed elsewhere as a gate, eligibility condition, priority input, search selector, or reset trigger.

This makes apparently local rules strategically non-local.

---

# 2. State classes

The source exposes several distinct state mechanisms. They should not be collapsed into one generic variable class.

| State class | Historical role | Examples | Main risk if misunderstood |
|---|---|---|---|
| Goal | persistent/control state | `strategy`, `milunits`, `enemyState`, `retreatnow`, `traincamel` | confusing intent with execution |
| Strategic number | mutable numeric measurement/control | `cavalry`, `sn-focus-player-number`, percentages, group sizes | confusing derived state with immutable fact |
| Flag-like state | compact binary/multi-state control | `strategylocked`, attack/group flags | missing latch/reset behavior |
| Timer | temporal eligibility | attack/scout/recovery timers | treating time as irrelevant metadata |
| Search state | computational workspace | temporary goals, target objects, points | mistaking scratch workspace for strategy |
| Object/target state | spatial/world reference | `position-self-id`, target points, group targets | assuming state is portable across contexts |
| Research state | capability lifecycle | `research-pending`, availability/completion | treating research intent as completion |
| Production intent | authorization state | `traincamel`, `trainknight`, etc. | treating authorization as successful production |

The most important rule is:

> **A control variable is not the same thing as the world state it is intended to influence.**

For example, `traincamel=yes` is an authorization signal. It is not proof that a camel entered a production queue, much less proof that the camel survived and improved the strategic position.

---

# 3. High-value state atlas

## 3.1 `strategy` — global strategic mode

**Definition:** `const.per` defines `strategy` as a goal channel used for named strategic modes.  
**Primary writer:** `init.per`.  
**Primary reader set:** `init.per`, `buildings.per`, `researches.per`, `units.per`, `escrow.per`, `gatherers.per`, `tsa.per`, `general.per`, `interaction.per`, `threats.per`, `boarhunting.per`, and other modules.

### Observed lineage

```text
strategy selection conditions
        ↓
strategy = named mode
        ↓
milunits often receives corresponding mode
        ↓
strategy-affinity / attack-priority state changes
        ↓
other modules reinterpret economy / buildings / production / attack
```

Observed strategic values include modes such as:

- `usual`
- `drush`
- `r-flush`
- `s-flush`
- `a-rush`
- `krush`
- `castledrop`
- `stonewall`
- `fast-imp`
- `grush`
- `ca-rush`
- civilization/context-specific variants elsewhere in the source

### Critical finding

`strategy` is not merely a label. It is a **cross-controller policy selector**.

The same state is read by construction, technology, economy, military, scouting/interaction, and attack logic. A strategy change therefore changes the interpretation of many downstream rules without requiring those rules to know why the strategy changed.

### Strong reset behavior

The source contains repeated strategy resets in response to conditions such as:

- unsuitable dock/port distance;
- enemy walling;
- enemy nearly defeated;
- water-control transitions;
- inappropriate or malformed strategy combinations;
- attack/strategy mismatch;
- resource failure for fast-castle/fast-imperial style plans;
- state combinations that the programmer explicitly labels as strategy-selection errors.

Representative source locations include `init.per` around lines 6584–6743, 6886–7608, 8302–8411, 8693–8829, and 8882 onward.

**Evidence:** DIRECT for state writes and consumers; COMPOSED for cross-system strategic interpretation.

**Closure:** CONTROL — strong. WORLD — not established by the source alone. STRATEGIC — inferred except where specific external outcomes are independently proven.

---

## 3.2 `milunits` — military posture coupled to strategy

`milunits` is initialized and repeatedly assigned alongside `strategy`.

The strongest observed pattern is:

```text
strategy = X
      ↓
milunits = X / yes / no
      ↓
production and building rules use milunits as a military-posture gate
```

Examples:

```text
strategy = drush       → milunits = drush
strategy = r-flush     → milunits = r-flush
strategy = s-flush     → milunits = s-flush
strategy = a-rush      → milunits = a-rush
strategy = krush       → milunits = krush
strategy = castledrop  → milunits = castledrop
strategy = stonewall   → milunits = no
strategy = fast-imp    → milunits = no
```

The source also contains defensive/debugging normalization where malformed combinations are reset to a conventional state and, in one late block, `milunits` is compared against `strategy` and can be assigned from it.

### Interpretation

`milunits` is not simply “has military units.” It is a **military production/posture policy channel** whose values can encode strategic mode.

This distinction is high-value because a future archaeology pass that treats `milunits` as a Boolean military-presence fact will misread a large portion of the production network.

**Evidence:** DIRECT.

---

## 3.3 `strategylocked` — strategic hysteresis / commitment latch

Definition: `const.per:1584` gives `strategylocked 139`.

Initialization and writers occur primarily in `init.per`, with many lock assertions in `interaction.per`.

Observed lifecycle:

```text
strategy unlocked
      ↓
strategy selected
      ↓
strategylocked = yes
      ↓
many later strategy-selection rules become ineligible
      ↓
explicit failure / transition condition
      ↓
strategy reset
      ↓
strategylocked = no
      ↓
selection can resume
```

This is one of the clearest historical anti-oscillation mechanisms.

It is not proof of a modern hysteresis controller, but it is direct evidence that the programmer recognized the need to **prevent continuous strategy re-selection**.

The source also contains explicit unlock behavior around `init.per:8801–8810`.

**Evidence:** DIRECT.

**Strategic interpretation:** INFERRED but strongly supported.

---

## 3.4 `strategy-affinity` — candidate-selection pressure

`strategy-affinity` is repeatedly modified in the strategy-selection region, frequently with:

```text
up-modify-goal strategy-affinity c:max 2
```

and compared against named strategy affinities such as rush/flush/castledrop/stonewall affinities.

The pattern is:

```text
candidate conditions
      ↓
compare candidate affinity to current affinity
      ↓
select stronger candidate
      ↓
raise / retain current affinity
```

The exact numeric semantics of every affinity scale are not yet fully normalized. However, the source clearly uses affinity as a **selection discriminator**, not as a passive statistic.

**Evidence:** DIRECT for comparison/update behavior; INFERRED for exact utility semantics.

---

## 3.5 `attackprioritychange` — reconfiguration trigger

`attackprioritychange` is written heavily in `init.per` and consumed by attack-priority setup.

A representative sequence is:

```text
strategy / situation transition
      ↓
attackprioritychange = yes
      ↓
attack-priority configuration runs
      ↓
fortification / TC / military / camp / dock / port / shipyard priorities are recalculated
      ↓
attackprioritychange = no
```

At `init.per` around 6453–6463 the source writes temporary priority values for categories such as heavy fortifications, simple fortifications, town centers, military buildings, camps, mills, docks, ports, and shipyards. The following rule consumes `attackprioritychange` to apply the resulting priorities.

### Finding

This is a **transaction-like recomputation trigger**:

```text
STATE CHANGED
   ↓
REQUEST RECOMPUTATION
   ↓
DERIVED PRIORITIES APPLIED
   ↓
TRIGGER CLEARED
```

This is more precise than calling it merely “a flag.”

**Evidence:** DIRECT.

---

## 3.6 `enemyState` — opponent age/state abstraction

Definition: `enemyState 254`.

Initialization: `dark`.

`init.per` later assigns values including:

- `imperial`
- `castlea`
- `feudal`
- `dark`
- `dfeudal`
- `fcastlea`
- `cimperial`

Consumers include `buildings.per` and `escrow.per`, with comparisons against military/technology conditions.

### Control chain

```text
focus-player / age observation
       ↓
enemyState classification
       ↓
construction / technology / military / escrow gates
```

The key insight is that downstream rules do not need to repeatedly reconstruct the opponent's state. They consume a compact classified state channel.

**Evidence:** DIRECT.

**Caution:** the exact distinction among all `enemyState` values is not yet fully documented. Do not collapse them to a simple enemy-age integer without tracing every assignment and comparison.

---

## 3.7 `retreatnow` — emergency tactical authority

Definition: `retreatnow 36`.

Writers are concentrated in `orb.per` and `tsa.per`, with initialization in `init.per`.

Observed pattern:

```text
threat / engagement failure condition
        ↓
retreatnow = yes
        ↓
retreat machinery invoked
        ↓
attack state can be reset / movement authority changes
        ↓
retreatnow = no
```

The source checks conditions involving castles, towers, Town Centers, monks, military insufficiency, and other dangerous engagement contexts.

### Important authority boundary

`retreatnow` is a **control authorization/state**, not a physical movement result.

The historical source can prove that retreat logic was enabled. It cannot, by itself, prove the exact resulting unit path or survival outcome.

**Evidence:** DIRECT for control transition; COMPOSED for attack/recovery interpretation.

---

## 3.8 `attackStart` / `attackInProgress` — explicit attack lifecycle

Definitions:

```text
attackStart       242
attackInProgress  243
```

Initialization occurs in `init.per`.

`tsa.per` contains the principal lifecycle writes:

```text
attackStart = yes
        ↓
attackInProgress = yes
        ↓
attack activity
        ↓
attackInProgress = no
```

This separates **attack initiation** from **attack currently in progress**.

That distinction is architecturally significant even though Layer 2 is not implementing anything: a binary “attacking” state would lose the temporal transition represented by these two channels.

**Evidence:** DIRECT.

---

## 3.9 `traincamel` / `trainknight` / `trainpike` / `trainarcher` / `trainunique` — production authorization channels

The production goals are initialized in `units.per` and written repeatedly from strategic/feasibility rules.

For example, `traincamel` is set in `units.per` around lines 6949–7258 and elsewhere, while production machinery later consumes the goal.

The camel chain reconstructed in Passes 37–42 is:

```text
enemy mounted observation
        ↓
cavalry / cavarchers aggregation
        ↓
context + resource + military feasibility
        ↓
camel-set ceiling
        ↓
traincamel = yes
        ↓
production machinery
        ↓
camel queue/action
```

### Critical separation

```text
traincamel = yes
        ≠
camel queued
        ≠
camel completed
        ≠
camel survived
```

Replay evidence from Pass 38 confirms actual Byzantine camel queue actions in two calibration games, but does not expose the internal historical `traincamel` state at the causal moment.

**Evidence:** DIRECT for historical authorization chain; replay corroboration for actual queue activity; causal bridge remains unobservable.

---

## 3.10 `camel-set` — own capability inventory

Definition: `camel-set 280`.

Initialization: `init.per:556`.

Population: `init.per` around line 887 uses `up-modify-goal camel-set g:+ temporary-goal` after counting own camel-line capability.

This establishes that `camel-set` is an **own-state capability inventory**, not an enemy-threat channel.

The strategic comparison is therefore:

```text
enemy mounted pressure
        vs.
own camel capability
```

This is the strongest historical precedent for a capability-deficit interpretation, but the source does not contain a universal deficit equation.

**Evidence:** DIRECT.

---

## 3.11 `cavalry` / `cavarchers` — compressed enemy threat channels

`threats.per` aggregates focus-player mounted categories into compact strategic-number channels.

The source includes multiple mounted lines, including camel, knight, scout-cavalry, cataphract, war-elephant, and civilization-specific mounted categories.

A critical Pass-37 finding is that `cavalry` is mutable. `units.per` contains a phase where:

```text
strategic-number camels >= 1
    ↓
up-modify-sn cavalry s:- camels
```

and a later compensating addition.

Therefore:

> `cavalry` must be treated as a mutable derived channel whose semantic meaning can be transformed within a control phase.

The exact reason for the subtraction remains **UNCERTAIN**. It must not be promoted to a definitive claim about camel-threat exclusion until all consumers are traced.

**Evidence:** DIRECT for mutation; INFERRED for semantic purpose.

---

## 3.12 `escrowing` / `escrow-state` — resource reservation / search state

`escrowing` is a goal state used by `escrow.per` and related systems. `escrow-state` is also used in construction/location feasibility searches.

Historical escrow behavior demonstrates:

```text
future capability desired
        ↓
resources protected / reserved
        ↓
feasibility check
        ↓
research or production action
        ↓
escrow state released/reset
```

This is direct evidence for **resource reservation as strategic control**, not merely resource counting.

`escrow-state` also participates in `up-can-build-line` location checks, demonstrating that “escrow” state can be consumed by world-placement logic.

**Evidence:** DIRECT/COMPOSED.

---

## 3.13 `migration-state` / `transport-state` — multi-step strategic transitions

`migration-state` is initialized to 0 and later assigned 1 and 2 by `general.per` / `init.per`.

`transport-state` follows a similarly explicit 0 → 1 → 2 progression in `general.per`.

These are not Boolean facts. They are **phase-state machines**.

Representative migration chain:

```text
migration-state = 0
      ↓
transition condition
      ↓
migration-state = 1
      ↓
intermediate construction / movement behavior
      ↓
migration-state = 2
```

Transport follows the same general pattern.

**Evidence:** DIRECT.

**Implication:** historical strategic transitions frequently use small integer state machines instead of one descriptive variable.

---

## 3.14 `position-self-id` — world-object reference crossing module boundaries

`position-self-id` is read by `boarhunting.per`, `buildings.per`, `general.per`, `researches.per`, `tsa.per`, and `units.per`.

It is used with target/object APIs such as:

```text
up-set-target-by-id
up-get-object-data
```

This is a concrete example of world-object identity becoming a cross-module control input.

The important distinction is:

```text
position classification
        ≠
position object identity
```

Both coexist in the historical system.

**Evidence:** DIRECT.

---

## 3.15 `block-attacking` — explicit attack suppression gate

Definition: `block-attacking 279`.

`tsa.per` sets it to yes/no under explicit guards. Other attack logic reads it.

This produces a clean authority chain:

```text
strategic / tactical condition
        ↓
block-attacking = yes
        ↓
attack controller suppressed
        ↓
condition clears
        ↓
block-attacking = no
```

This is stronger evidence than a simple attack/no-attack flag because it demonstrates **negative authority**: a controller can be prevented from acting by another subsystem.

**Evidence:** DIRECT.

---

# 4. Cross-controller dependency map

The following is the most useful high-level dependency reconstruction from the source.

```text
                    ┌──────────────┐
                    │  enemyState  │
                    └──────┬───────┘
                           │
                           ▼
                    TECHNOLOGY / ECO
                           │
                           ▼
                    ┌──────────────┐
                    │   strategy   │◄──────────────┐
                    └──────┬───────┘               │
                           │                       │
              ┌────────────┼────────────┐          │
              ▼            ▼            ▼          │
          milunits   attackpriority   economy      │
              │         change                     │
              ▼            │                       │
          production       ▼                       │
              │       attack/defense               │
              ▼                                    │
          military ───────────────► attack          │
              │                     │              │
              │                     ▼              │
              └──────────────► retreat/reset ───────┘

Information / threat
        │
        ▼
  cavalry/cavarchers
        │
        ▼
 production authorization
        │
        ▼
   military capability
        │
        └──────────────► attack
```

The graph is intentionally asymmetric. Some state channels have many consumers but only one or two writers. Others are heavily rewritten workspaces. Their failure modes are therefore different.

---

# 5. Writer / transformer / consumer classes

A useful classification emerged from the trace.

## Class A — Policy writers

Examples:

- `strategy`
- `milunits`
- `enemyState`
- `strategylocked`

These alter the interpretation of downstream systems.

## Class B — Authorization writers

Examples:

- `traincamel`
- `trainknight`
- `trainpike`
- `trainarcher`
- `trainunique`
- `block-attacking`

These grant or deny permission for a downstream action.

## Class C — Measurement/compression channels

Examples:

- `cavalry`
- `cavarchers`
- `camel-set`
- resource strategic numbers
- military superiority channels

These compress observations into reusable state.

## Class D — Transition state

Examples:

- `attackStart`
- `attackInProgress`
- `migration-state`
- `transport-state`
- research states

These encode phase progression.

## Class E — Recalculation triggers

Examples:

- `attackprioritychange`
- selected temporary-goal channels

These do not represent the desired world state directly. They request recomputation of derived control.

## Class F — Workspace / search state

Examples:

- `temporary-goal*`
- target IDs
- target points
- distance scratch values

These must not be promoted to strategic state without lineage tracing.

---

# 6. The historical control loop

Across the traced controllers, a recurring pattern is now sufficiently strong to state as an archaeological generalization:

```text
OBSERVE
  ↓
CLASSIFY / COMPRESS
  ↓
WRITE STATE
  ↓
USE STATE AS AUTHORITY / ELIGIBILITY
  ↓
SEARCH / EXECUTE
  ↓
RESET OR TRANSITION
  ↓
REASSESS
```

Examples:

### Strategy

```text
situation
 → candidate strategy
 → affinity comparison
 → strategy write
 → lock
 → downstream policy changes
 → reset condition
 → unlock
```

### Threat response

```text
enemy composition
 → threat aggregation
 → own capability measurement
 → threshold / feasibility
 → production authorization
 → production machinery
 → reassessment
```

### Attack

```text
attack opportunity
 → attackStart
 → attackInProgress
 → engagement
 → danger / block / retreat condition
 → retreat or reset
 → regroup / restart
```

### Strategic transition

```text
transition desire
 → escrow / resource protection
 → feasibility
 → research / construction
 → state transition
 → new policy eligibility
```

These are **historical control patterns**, not permission to implement them in Layer 2.

---

# 7. What resets what?

A major finding is that reset behavior is part of the controller's semantics, not cleanup.

| State | Typical reset / release mechanism | Meaning |
|---|---|---|
| `strategy` | explicit reset rules in `init.per` | current plan invalidated |
| `strategylocked` | unlock transition | selection permitted again |
| `attackprioritychange` | recomputation completion | derived priorities refreshed |
| `traincamel` etc. | production/selection logic | authorization withdrawn or replaced |
| `retreatnow` | retreat lifecycle | emergency authority cleared |
| `attackInProgress` | attack lifecycle | active engagement ended |
| `migration-state` | phase transition | migration progressed |
| `transport-state` | transport lifecycle | transport phase progressed |
| `escrowing` | escrow lifecycle | reserved-resource operation completed/aborted |
| temporary goals | local controller/search reset | workspace released |

This yields a strong rule for future archaeology:

> **A state without its reset path is only half-understood.**

---

# 8. Timers are state transitions, not decoration

The historical source repeatedly couples timers to future eligibility.

The correct abstraction is:

```text
CURRENT STATE
   +
TEMPORAL CONDITION
   ↓
FUTURE ELIGIBILITY
```

Observed applications include:

- attack cooldown/restart;
- scouting reassessment;
- recovery windows;
- strategic reevaluation;
- building/placement transitions;
- trade and map-control timing.

The exact timer semantics remain controller-specific. Arbitrary numeric values must not be generalized into universal timing laws.

**Evidence:** COMPOSED/DIRECT depending on controller.

---

# 9. Byzantine-specific implications supported by this map

This pass is not the Byzantine strategy pass yet. However, several Byzantine-relevant facts are now structurally clear.

## 9.1 Byzantine military decisions are downstream of generic controller state

A Byzantine-specific response cannot be understood by reading only Byzantine unit rules. It is filtered through:

```text
strategy
milunits
enemyState
threat aggregates
research state
resource feasibility
production authorization
```

Therefore the civilization layer must eventually be studied **inside** the generic controller network, not as an isolated tech-tree list.

## 9.2 Camel response is an instance of a larger historical mechanism

The camel chain is useful because it exposes the relationship among:

```text
enemy mounted pressure
own camel capability
resource feasibility
production authority
```

But the exact historical thresholds are context-dependent. They should not be mistaken for a complete Byzantine strategy policy.

## 9.3 Byzantine strategic identity cannot yet be reduced to one unit

The control map demonstrates why this would be methodologically unsound. A civilization's effective strategy depends on the interaction of:

```text
bonuses
+ unit lines
+ tech availability
+ costs
+ train times
+ production buildings
+ counter relationships
+ map role
+ economy
+ timing
+ enemy state
+ current strategic mode
```

The next research stream therefore remains a full Byzantine strategic profile.

---

# 10. Hostile quality review

## Attack against the map

### Challenge 1 — “This is just a list of variables.”

**Rejected.** The map explicitly traces writers, transformations, consumers, authority effects, and resets. The strategic value is the cross-module dependency structure.

### Challenge 2 — “`strategylocked` proves modern hysteresis.”

**Rejected.** It proves a lock/latch against repeated selection. Calling that modern hysteresis is an AEGIS interpretation, not a historical source fact.

### Challenge 3 — “`traincamel` proves camel production was caused by cavalry pressure.”

**Rejected.** Pass 39 already established that the internal causal bridge is not observable in the replay corpus. The historical source proves a response-capable rule network; replay proves temporal compatibility, not causal closure.

### Challenge 4 — “`cavalry` is enemy cavalry count.”

**Rejected.** Pass 37 demonstrated phase-scoped mutation of the aggregate. Its semantic purpose must be traced by consumer context.

### Challenge 5 — “`milunits` is just a Boolean.”

**Rejected.** The source assigns named strategy values such as `drush`, `r-flush`, `s-flush`, `a-rush`, `krush`, and `castledrop`, as well as `yes`/`no`.

### Challenge 6 — “A reset means the strategy failed.”

**Rejected.** A reset proves invalidation/reconfiguration logic. It does not prove game-level strategic failure.

### Challenge 7 — “Control closure equals strategic success.”

**Rejected.** The project evidence model explicitly separates CONTROL, WORLD, and STRATEGIC closure.

---

# 11. Six-month re-entry test

A future engineer returning to this artifact after six months should be able to answer:

1. What does `strategy` mean?
2. Which modules write it?
3. Which modules consume it?
4. What locks it?
5. What resets it?
6. Why is `milunits` not equivalent to military population?
7. What is the distinction between `attackStart` and `attackInProgress`?
8. What grants attack suppression authority?
9. Why is `traincamel` not evidence of completed camel production?
10. Why is `camel-set` friendly capability rather than enemy threat?
11. Why is `cavalry` a mutable derived channel?
12. What is `enemyState` doing for downstream consumers?
13. Why are `migration-state` and `transport-state` phase machines?
14. Why must temporary goals be treated as workspace until proven otherwise?
15. Why are reset paths part of state semantics?
16. Which claims are DIRECT, COMPOSED, INFERRED, or UNCERTAIN?
17. Which findings are historical and which are AEGIS generalizations?
18. Why is no Layer-2 `.per` implementation present?

If these questions cannot be answered from this document plus its cited source locations, the map has not remained durable.

---

# 12. Evidence ledger

| Finding | Evidence | Closure | Source anchor |
|---|---|---|---|
| `strategy` is a cross-module policy state | DIRECT/COMPOSED | CONTROL | `init.per`, broad consumers |
| `milunits` mirrors/encodes strategic posture | DIRECT | CONTROL | `init.per`, `buildings.per`, `units.per` |
| `strategylocked` inhibits reselection | DIRECT | CONTROL | `init.per`, `interaction.per` |
| `strategy-affinity` participates in candidate selection | DIRECT | CONTROL | `init.per` strategy-selection region |
| `attackprioritychange` triggers priority recomputation | DIRECT | CONTROL | `init.per` ~6450–6527 |
| `enemyState` is compact opponent-state abstraction | DIRECT | CONTROL | `init.per` ~4188–4233; consumers |
| `retreatnow` is emergency retreat authority | DIRECT | CONTROL | `tsa.per`, `orb.per` |
| `attackStart` and `attackInProgress` form lifecycle state | DIRECT | CONTROL | `tsa.per` ~4152–4166 |
| production goals are authorization channels | DIRECT | CONTROL | `units.per`, `buildings.per`, `researches.per` |
| `camel-set` is own camel capability | DIRECT | CONTROL | `init.per` ~556, ~887 |
| `cavalry` is mutable derived state | DIRECT | CONTROL | `units.per` normalization blocks |
| escrow protects future capability expenditure | DIRECT/COMPOSED | CONTROL | `escrow.per` |
| migration/transport are multi-step state machines | DIRECT | CONTROL | `general.per`, `init.per` |
| `position-self-id` crosses module boundaries | DIRECT | CONTROL | multiple modules |
| `block-attacking` provides negative authority | DIRECT | CONTROL | `tsa.per` |
| timer state changes future eligibility | COMPOSED | CONTROL | attack/scouting/recovery controllers |
| historical controller is a centralized planner | **NOT PROVEN** | — | architecture inference rejected |
| camel production in replay was caused by knight pressure | **NOT PROVEN** | — | Pass 38–39 replay evidence |
| every reset represents strategic failure | **NOT PROVEN** | — | source semantics |

---

# 13. Pass result

## **PASS — Strategic control-state topology substantially reconstructed.**

The historical AI can now be described with much greater precision as a distributed network of:

```text
OBSERVATIONS
→ COMPRESSED STATE
→ POLICY STATE
→ AUTHORITY / ELIGIBILITY
→ SEARCH / ACTION
→ RESET / TRANSITION
→ REASSESSMENT
```

The highest-value discoveries are:

1. `strategy` is a cross-system policy selector, not a label.
2. `milunits` is a strategy-coupled military posture channel, not a simple unit-count fact.
3. `strategylocked` provides explicit commitment/latch behavior.
4. `attackprioritychange` is a recomputation trigger.
5. `enemyState` is a compact opponent-state abstraction.
6. attack state has multiple lifecycle dimensions (`attackStart`, `attackInProgress`, `retreatnow`, `block-attacking`).
7. production goals are authority channels, not world confirmations.
8. `camel-set` and `cavalry/cavarchers` occupy opposite sides of a threat-versus-capability relationship.
9. derived strategic numbers can be transformed and restored within a phase.
10. reset/re-entry behavior is a first-class part of the historical controller topology.

### Remaining uncertainty

The map is substantially reconstructed, but not every historical state channel is closed. In particular:

- complete timer-to-controller lineage remains incomplete;
- exact semantics of several affinity scales remain partially unresolved;
- exact purpose of cavalry normalization remains uncertain;
- some high-numbered temporary goals require consumer-specific classification;
- world/strategic outcomes remain under-observable in replay evidence.

These are appropriate Layer-2 research targets, not reasons to begin implementation prematurely.

---

# 14. Next research target

The next high-value Layer-2 stream is the **Byzantine Strategic Profile**:

```text
BYZANTINE BONUSES
       ↓
UNIT ROSTER / UNIT LINES
       ↓
TECH TREE
       ↓
COSTS / TRAIN TIMES
       ↓
COUNTERS
       ↓
PRODUCTION INFRASTRUCTURE
       ↓
ECONOMIC DEMANDS
       ↓
COMPOSITION OPTIONS
       ↓
MAP / POSITION IMPLICATIONS
       ↓
STRATEGIC TRANSITIONS
       ↓
CIVILIZATION-SPECIFIC WIN CONDITIONS
```

The objective is not to produce a generic “Byzantine strategy guide.” It is to determine which strategic properties are **intrinsic to Byzantines**, which are inherited from generic AoE2 control logic, and which emerge only from their interaction.

That research must be reconciled against the control-state atlas before Layer 3 architecture begins.
