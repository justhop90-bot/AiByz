# P0 Civilian Lifecycle Forensics v2 — Production, Tasking, and Escrow

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Evidence:** untouched local `resources\\_common\\ai\\Promisory` corpus on Weebo  
**Status:** Forensic extraction — implementation deferred

## 1. Purpose

This pass follows the initial P0 discovery and attacks the most important unresolved question: what actually connects strategic civilian policy to physical villager behavior?

The answer is not a single subsystem. The stock implementation is a chain of authorization, reservation, allocation, search, tasking, and execution mechanisms.

The critical newly verified boundary is:

```text
strategic production decision
        ↓
trainvillager = yes
        ↓
ESCROW-AWARE TRAINING GATE
        ↓
up-train escrow-state villager
        ↓
TC production
        ↓
pending villager
        ↓
worker accounting
        ↓
resource/source tasking
```

This changes the AEGIS implementation target materially.

---

## 2. P0-A finding — `trainvillager` is authorization, and `up-train` is a separate service

### Evidence

`Promisory\\units.per` initializes `trainvillager` to `no` near the beginning of the civilian-unit section. Numerous later rules set it to `yes` when food, population, age, strategy, military and infrastructure conditions are satisfied.

The actual training service occurs much later in the same file.

The target-build source contains the following chain:

```per
(defrule
    (goal trainvillager yes)
    (up-can-train escrow-state c: villager)
=>
    (enable-timer FDrop ffdrop)
    (up-train escrow-state c: villager)
    (up-jump-rule 1))
```

A second training rule also exists for the case where there is no pending villager or a TC-specific progress condition is satisfied:

```per
(defrule
    (goal trainvillager yes)
    ...
    (up-can-train escrow-state c: villager)
=>
    (up-train escrow-state c: villager)
    ...)
```

### Conclusion

There are at least three distinct states:

1. **production desire/authorization** — `trainvillager yes`;
2. **resource/production feasibility** — `up-can-train escrow-state villager`;
3. **physical production command** — `up-train escrow-state villager`.

AEGIS must not collapse these into one rule.

### Architectural consequence

The permanent AEGIS contract should be:

```text
Civilian Demand
    ↓
Production Authorization
    ↓
Economic/Resource Authorization
    ↓
Production Service
    ↓
Pending Production Evidence
    ↓
Completion Evidence
```

---

## 3. P0-B finding — escrow is a real execution primitive, not merely an accounting concept

### Exact stock constants

`Promisory\\const.per` defines:

```per
(defconst with-escrow 0)
(defconst without-escrow 1)
```

and defines:

```per
(defconst escrow-state 241)
```

The same escrow-state constant is duplicated in `customConstants.per`, confirming that the stock architecture treats it as a named persistent goal.

### Release path

At the beginning of `escrow.per`, stock explicitly performs:

```per
(up-release-escrow)
(set-escrow-percentage wood 0)
(set-escrow-percentage food 0)
(set-escrow-percentage gold 0)
(set-escrow-percentage stone 0)
(up-modify-escrow wood c:= 0)
(up-modify-escrow food c:= 0)
(up-modify-escrow gold c:= 0)
(up-modify-escrow stone c:= 0)
(up-reset-cost-data cost-food)
```

This is direct evidence that escrow has actual engine state and release semantics.

### Execution use

Stock uses escrow-aware feasibility predicates for multiple action families:

```text
can-research-with-escrow
can-build-with-escrow
can-train-with-escrow
```

The stock corpus applies these to age advancement, economic technologies, military technologies, buildings, units and other strategic purchases.

### Critical conclusion

Our previous conceptual separation was correct but understated the importance:

```text
Strategic Commitment
        ≠
Economic Commitment
        ≠
Resource Escrow
        ≠
Execution Authorization
```

Moreover, **resource escrow is directly coupled to the engine's execution feasibility checks**.

That means AEGIS cannot implement escrow solely as an internal bookkeeping layer and expect the engine to honor it. We need an explicit AEGIS escrow policy that is translated into legal engine-side execution state where required.

---

## 4. P0-C finding — escrow is a priority/selection mechanism, not one reservation

`escrow.per` initializes `escrow-flag`, `escrow-flag2`, and `escrow-flag3` to zero and then constructs bitmask-like flags by adding powers of two.

Examples include:

- `escrow-flag += 1` for Castle Age;
- `escrow-flag += 2` for Imperial Age;
- `escrow-flag += 4` for unique-unit upgrade;
- `escrow-flag += 8` for unique research;
- `escrow-flag += 16` for Wheelbarrow;
- `escrow-flag += 32` for Hand Cart;
- additional bits for military technologies and units.

The action layer later dispatches on those flags.

### Architectural interpretation

The stock design is effectively a **multi-request arbitration mechanism**:

```text
many possible purchases
       ↓
conditions / affordability / strategy
       ↓
bitmask authorization set
       ↓
priority/jump ordering
       ↓
escrow-aware execution
```

Therefore AEGIS should not model escrow as one scalar “reserved amount.”

A better abstraction is:

```text
ReservationSet = {
    food: claims[],
    wood: claims[],
    gold: claims[],
    stone: claims[],
    priority,
    owner,
    generation,
    expiration,
    execution condition
}
```

---

## 5. P0-D finding — villager production and age-up compete inside the same economic control plane

Stock `escrow.per` contains rules that authorize Castle Age and Imperial Age through the same escrow machinery used by unit and technology purchases.

Castle Age authorization evaluates combinations of:

- food stockpile;
- gold stockpile;
- food-villager count;
- gold-villager count;
- enemy age/state;
- military superiority;
- civilian population;
- strategy.

Imperial Age authorization similarly evaluates:

- food;
- gold;
- food-villager count;
- gold-villager count;
- population;
- military state;
- strategy;
- enemy state.

### Consequence

The civilian scheduler cannot independently maximize villager production.

It must understand competing economic commitments:

```text
              FOOD / GOLD STOCKPILE
                     |
        +------------+-------------+
        |            |             |
        v            v             v
   Villagers       Age-up       Military
        |            |             |
        +------------+-------------+
                     ↓
               ESCROW ARBITER
```

This is one of the strongest reasons to make Escrow a first-class AEGIS service.

---

## 6. P0-E finding — worker-role counts are consumed as actual operating targets

`dawn.per` computes integer `wood-villagers`, `food-villagers`, `gold-villagers`, and `stone-villagers` from strategic-number percentages and `villagercount`.

The terminal normalization path writes the resulting integer allocation back to the strategic-number percentages.

The `gatherers.per` subsystem then consumes those values while issuing actual task commands.

Representative stock tasking patterns include:

```per
(up-find-remote c: lumber-camp c: 3)
...
(up-find-resource c: wood c: 8)
...
(up-target-objects 0 action-default -1 -1)
```

and analogous patterns for mining camps, mills, food sources, and other resources.

### Critical conclusion

The missing layer between `dawn` and the actual game is not a hypothetical abstraction. It is present in `gatherers.per` as a large task-selection and search system.

The correct chain is now:

```text
percent policy
   ↓
integer role targets (`dawn`)
   ↓
current worker-role count
   ↓
source/infrastructure search (`gatherers`)
   ↓
candidate filtering
   ↓
nearest/appropriate source
   ↓
action-default / gather task
```

---

## 7. P0-F finding — source selection is stateful and spatial

The stock wood-tasking subsystem does not simply select “a tree.”

It can:

- identify nearby lumber camps;
- calculate distance from candidate workers;
- filter workers by existing action/order;
- filter workers by carried resources;
- search active resource objects;
- exclude overloaded targets;
- clean and sort candidate searches by distance;
- select the closest acceptable resource;
- then issue `action-default` to the selected worker set.

The same architecture appears for mining and forage/mill paths.

### Consequence

`ResourceOpportunity` is not just an AEGIS design preference. It is a useful abstraction for preserving the operational information already represented by stock behavior.

---

## 8. P0-G finding — generic gathering uses `action-default`, not a universal explicit `action-gather`

A targeted search found many `action-default` task commands in `gatherers.per`, while `action-gather` appears only in specific specialized cases and debugging/special-purpose routines.

Therefore we must not assume that a universal AEGIS gatherer command should be:

```per
(up-target-objects ... action-gather ...)
```

The stock architecture frequently uses:

```per
(up-target-objects 0 action-default -1 -1)
```

after establishing a target object and/or target point.

### ABI implication

`action-default` appears to allow the engine to apply the object's normal interaction/task semantics once a valid target has been established.

This must be treated as **OBSERVED behavior**, while the exact engine-level action dispatch semantics remain an ABI qualification item.

---

## 9. P0-H finding — specialized food systems are embedded in the general allocation loop

`gatherers.per` contains explicit source selection and retasking behavior for:

- sheep/livestock;
- forage;
- farms;
- deer/hunting;
- fishing;
- wood;
- gold;
- stone.

Examples include:

```text
current-livestock
mysheep
villager-forager
villager-farmer
villager-fisherman
villager-hunter
```

The system evaluates distance, source count, worker count, target tasks, source status and time before retasking.

This means a food controller cannot be completely independent from the generic allocator.

### Revised architecture

```text
Food Demand
    ↓
Food Worker Target
    ↓
Food Source Portfolio
    ├─ Herdables
    ├─ Forage
    ├─ Boar
    ├─ Hunt
    ├─ Farms
    └─ Fishing
    ↓
Source-specific operating controller
    ↓
Generic worker task execution
```

---

## 10. P0-I finding — construction and resource tasking are coupled

`gatherers.per` explicitly checks infrastructure such as lumber camps, mining camps, mills and town centers while choosing tasks.

When a mining camp is absent, the task-selection logic searches for the relevant foundation/pending structure and changes how it selects and retasks workers.

This establishes a dependency:

```text
resource demand
    ↓
worker target
    ↓
required infrastructure
    ↓
construction state
    ↓
resource task
```

Construction therefore cannot be a disconnected downstream utility.

---

## 11. P0-J finding — builder allocation is itself a specialized worker state

The stock corpus contains extensive `up-assign-builders` use in `buildings.per` and `init.per`.

Builder counts vary by structure and situation. Examples include one, two, three, five, ten, twenty and larger specialized assignments.

This means worker accounting must eventually distinguish at least:

```text
resource worker
builder
military worker/service
specialized food worker
idle/unassigned
```

A single four-bucket gatherer count is therefore insufficient as the complete civilization worker state.

---

## 12. P0-K finding — the stock civilian system has an explicit feedback loop

The evidence now supports a closed-loop interpretation:

```text
           STRATEGY / AGE / THREAT
                    ↓
             RESOURCE DEMAND
                    ↓
               ESCROW CLAIMS
                    ↓
              GATHERER POLICY
                    ↓
            INTEGER ROLE TARGETS
                    ↓
           SOURCE / SITE SEARCH
                    ↓
             TASK ASSIGNMENT
                    ↓
             PHYSICAL INCOME
                    ↓
           STOCKPILE / STATE DATA
                    ↓
             POLICY RE-EVALUATION
```

This is a control loop, not a static allocation table.

---

## 13. New AEGIS requirements generated by P0

### Required services

1. **Civilian Production Service**
2. **Housing Service**
3. **Worker Accounting Service**
4. **Economic Escrow Service**
5. **Resource Opportunity Service**
6. **Food Portfolio Controller**
7. **Worker Tasking Service**
8. **Construction Dependency Service**
9. **Idle/Interruption Recovery Service**
10. **Civilian Reconciliation Service**

### Required state domains

```text
civilian-demand
production-authorization
production-pending
population-cap
housing-headroom
worker-role-targets
worker-role-observed
worker-task-state
resource-opportunities
infrastructure-state
escrow-claims
escrow-flags / execution authorization
income estimates
failure/recovery state
generation/freshness
```

---

## 14. Stock-to-AEGIS forensic ledger — current revision

| Stock source | Exact behavior | AEGIS owner | Evidence |
|---|---|---|---|
| `units.per` early civilian rules | decide whether `trainvillager` becomes yes | Civilian Production Policy | OBSERVED |
| `units.per` training rules | `up-can-train escrow-state villager` gates execution | Production Service + Escrow | OBSERVED |
| `units.per` training rules | `up-train escrow-state villager` issues production | Production Service | OBSERVED |
| `units.per` pending checks | pending villager objects affect production rules | Civilization State | OBSERVED |
| `dawn.per` | percentage → integer worker counts | Worker Allocation | OBSERVED |
| `gatherers.per` | candidate worker/source searches | Worker Tasking | OBSERVED |
| `gatherers.per` | distance/status/task filtering | Spatial Economy | OBSERVED |
| `gatherers.per` | `action-default` target execution | Worker Tasking / ABI | OBSERVED |
| `buildings.per` | builder assignment | Construction OS | OBSERVED |
| `escrow.per` | escrow release | Escrow Service | OBSERVED |
| `escrow.per` | resource escrow state | Escrow Service | OBSERVED |
| `escrow.per` | bitmask purchase authorization | Escrow Arbitration | OBSERVED |
| `escrow.per` | escrow-aware research/build/train | Execution Authorization | OBSERVED |
| `boarhunting.per` | dedicated hunt subsystem | Food Controller | OBSERVED |

---

## 15. Architecture decisions now frozen

### AD-P0-01
`trainvillager` is a policy/authorization state. It is not the physical training operation.

### AD-P0-02
`up-can-train escrow-state` is part of the production execution contract.

### AD-P0-03
Escrow is an execution-relevant engine state, not merely AEGIS bookkeeping.

### AD-P0-04
Worker allocation and worker tasking are distinct services.

### AD-P0-05
Food worker count and food-source selection are distinct decisions.

### AD-P0-06
Construction is an economic dependency and must publish infrastructure availability to allocation/tasking.

### AD-P0-07
Generic gathering must not assume `action-gather`; stock frequently uses `action-default` after target selection.

### AD-P0-08
Worker state must represent builders and specialized task states in addition to four resource roles.

### AD-P0-09
AEGIS economic control must operate as a feedback loop, not a one-way percentage setter.

---

## 16. Still open — architecture-changing questions

1. Exactly which rules consume `wood-villagers` etc. to choose individual workers?
2. What is the complete idle-villager recovery path in `general.per`?
3. How are `action-default` target commands translated by the interpreter into gathering behavior?
4. Which `escrow.per` rules actually modify per-resource escrow amounts, and under what cost model?
5. How are escrow claims released after successful/failed actions?
6. How does stock prevent simultaneous commands from overspending an escrowed resource?
7. What exact production completion evidence is used for pending villagers?
8. Which task-state identifiers correspond to the specialized villager unit types?
9. Which worker state is engine-native versus inferred from action/order/object data?
10. How do construction failures propagate back into gatherer allocation?

These questions remain open until extracted from the target corpus or directly qualified in the target interpreter.

---

## 17. Next forensic operation

The next pass should **not** implement a worker allocator yet.

It should reconstruct the complete individual-worker tasking state machine:

```text
worker selected
  ↓
worker eligibility filter
  ↓
source/infrastructure search
  ↓
target selection
  ↓
action/order assignment
  ↓
productive state
  ↓
completion/depletion/interruption
  ↓
idle detection
  ↓
reclassification
  ↓
reassignment
```

The primary files are:

```text
Promisory\\gatherers.per
Promisory\\general.per
Promisory\\interaction.per
Promisory\\buildings.per
Promisory\\boarhunting.per
```

The objective is to find the exact boundary where a worker changes from a **role count** into an **individual engine command**.

Only when that boundary is understood should AEGIS implement its Worker Tasking Service.

---

## 18. P0 verdict

**P0 remains open, but the civilian architecture has now crossed a major evidence threshold.**

We have established that the missing substrate is not one economic module. It is a coordinated system of:

```text
policy
+ escrow
+ integer allocation
+ spatial source selection
+ infrastructure dependency
+ individual tasking
+ physical execution
+ reconciliation
+ recovery
```

The next investigation therefore moves one layer deeper: **individual worker tasking and recovery**.
