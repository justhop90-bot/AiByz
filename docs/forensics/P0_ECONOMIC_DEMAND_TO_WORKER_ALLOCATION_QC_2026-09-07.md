# P0 Economic Demand → Worker Allocation QC — 2026-09-07

Target: AoE2DE 101.103.48987.0 / BuildID 24094652
Corpus: untouched stock `resources/_common/ai/Promisory` on Weebo.
Status: forensic evidence; implementation deferred.

## Executive finding

Stock does not translate strategy directly into individual worker commands. It uses a two-stage economic control system:

```text
STRATEGIC / ECONOMIC CONDITIONS
        ↓
GATHERER POLICY
        ↓
STRATEGIC-NUMBER PERCENTAGES
        ↓
DAWN INTEGER TARGETS
        ↓
WORKER TASKING / RESOURCE SELECTION
```

This confirms the Economic Scheduler must sit between AEGIS cognition and civilian tasking.

## 1. Gatherer policy is dynamic

`gatherers.per` repeatedly changes the four gatherer percentages according to age, villager population, stockpiles, buildings, technology state, strategy and resource requirements.

Representative exact stock transitions include:

```text
45 wood / 55 food / 0 gold / 0 stone
→ 44 / 55 / 1 / 0
→ 40 / 57 / 3 / 0
→ 25 / 57 / 18 / 0
```

Other strategy branches use distributions such as:

```text
58 / 33 / 9 / 0
48 / 37 / 15 / 0
40 / 44 / 16 / 0
37 / 50 / 13 / 0
35 / 50 / 15 / 0
```

These are not fixed economy presets. They are conditional policy outputs.

## 2. Gold demand can directly change allocation

A stock Feudal branch requires:

- current age >= Feudal;
- economic context indicating Castle-age preparation;
- gold infrastructure or acceptable gold dropsite distance;
- total gold below the Castle requirement.

It then changes allocation to:

```text
25 wood / 57 food / 18 gold / 0 stone
```

This is direct evidence that resource demand is converted into worker distribution by policy rules rather than by individual worker commands.

## 3. Allocation policy is state-dependent, not purely resource-stock based

The same resource can receive materially different worker targets depending on:

- current age;
- building availability;
- research state;
- military strategy;
- villager count;
- stockpile targets;
- resource infrastructure;
- escrow state;
- map/source conditions.

Therefore AEGIS should not implement `if gold-low then +gold-workers` as its complete scheduler.

## 4. Dawn converts percentages into discrete worker targets

`dawn.per` first initializes target variables:

```text
wood-villagers
food-villagers
gold-villagers
stone-villagers
sum-villagers
villager-addition
```

It then uses actual `villagercount` and percentage strategic numbers to derive integer worker targets.

Exact stock operations near the end of `dawn.per`:

```text
wood-villagers  := sn-wood-gatherer-percentage
food-villagers  := sn-food-gatherer-percentage
gold-villagers  := sn-gold-gatherer-percentage
stone-villagers := sn-stone-gatherer-percentage

wood-villagers  *= villagercount
food-villagers  *= villagercount
gold-villagers  *= villagercount
stone-villagers *= villagercount

wood-villagers  /= 100
food-villagers  /= 100
gold-villagers  /= 100
stone-villagers /= 100
```

Thus percentages are explicitly converted to integer target populations.

## 5. Rounding/reconciliation is an actual control stage

`dawn.per` uses `sum-villagers` and `villager-addition` to reconcile target counts with the actual villager population.

Examples:

```text
if sum-villagers < villagercount
    villager-addition = 1
```

Then individual rules add the next worker to wood or food depending on constraints. Other rules increment food or wood when their target falls below strategic minimums.

This means worker allocation is not simply four independent integer divisions. There is a reconciliation stage that ensures the target distribution consumes the available civilian population.

## 6. Minimums override proportional allocation

Exact stock examples include:

- housing shortage causes additional wood allocation;
- insufficient food workers causes food allocation;
- Feudal transition requires minimum food/wood distributions;
- military strategy can increase wood or food requirements;
- gold allocation can be increased for Castle-age requirements;
- fishing/water strategy changes worker distribution;
- farms and available food sources modify the final food allocation.

Therefore the scheduler is better represented as:

```text
BASE POLICY
  ↓
RESOURCE DEMAND MODIFIERS
  ↓
MINIMUM CONSTRAINTS
  ↓
INFRASTRUCTURE CONSTRAINTS
  ↓
STRATEGY CONSTRAINTS
  ↓
INTEGER RECONCILIATION
  ↓
FINAL TARGETS
```

## 7. Worker targets are not worker identities

The `wood-villagers`, `food-villagers`, `gold-villagers`, and `stone-villagers` goals represent population targets, not permanent worker registries.

Separate stock tasking logic subsequently searches eligible villagers, filters their existing action/order/target/carry state, considers resource and dropsite topology, and issues commands.

Therefore:

```text
TARGET COUNT ≠ ASSIGNED UNIT
```

This supports the previously established distinction between population state and task state.

## 8. Economic policy can be modified by other subsystems

`dawn.per` contains direct `up-modify-sn` operations that synchronize strategic-number percentages with the calculated integer targets.

`gatherers.per` also contains many strategic-number assignments based on economic and military conditions.

This creates a distributed policy pipeline:

```text
strategy / research / infrastructure / economy
                ↓
       strategic-number policy
                ↓
       dawn target calculation
                ↓
       gatherer/task controllers
```

AEGIS must avoid reproducing this as uncontrolled cross-module writes. State ownership needs to be explicit.

## 9. Escrow is a separate control plane

`escrow.per` and `researches.per` contain `can-build-with-escrow`, `can-research-with-escrow`, escrow-state transitions, and explicit escrow release operations.

Example stock behavior saves the existing `escrow-state`, switches to `with-escrow`, executes a build through the escrow state, then restores the previous escrow state.

This confirms the earlier architecture:

```text
STRATEGIC COMMITMENT
        ≠
ECONOMIC DEMAND
        ≠
RESOURCE ESCROW
        ≠
EXECUTION AUTHORIZATION
```

## 10. Important correction to AEGIS economic architecture

The Economic Scheduler should NOT directly assign every villager.

Its primary output should be:

```text
TARGET DISTRIBUTION
```

plus demand/reservation information.

Civilian Operations then resolves:

```text
TARGET DISTRIBUTION
→ actual worker candidates
→ eligibility
→ source selection
→ dropsite/serviceability
→ command
→ observed productivity
```

This preserves separation of concerns.

## 11. Recommended scheduler model

```text
DEMAND VECTOR
  food +F
  wood +W
  gold +G
  stone +S
        ↓
RESERVATIONS / ESCROW
        ↓
BASE WORKER TARGETS
        ↓
CONSTRAINT SOLVER
  minimum food
  housing
  infrastructure
  military
  age-up
  research
  map/source availability
  threat
        ↓
INTEGER RECONCILIATION
        ↓
WORKER TARGET VECTOR
        ↓
CIVILIAN TASKING
```

The target vector should be generation-tagged and have a freshness/validity contract.

## 12. Allocation hysteresis is an AEGIS requirement, not yet proven stock behavior

Stock visibly changes percentages through many rules, but the inspected evidence does not prove a generalized hysteresis algorithm.

AEGIS should nonetheless deliberately add bounded hysteresis to prevent oscillation caused by rapid strategic demand changes.

This is an architectural improvement, not a claim about stock internals.

## 13. Failure and contention model

A worker target can be correct while physical execution fails:

```text
TARGET = 4 gold workers
        ↓
only 2 serviceable gold jobs
        ↓
2 assigned
2 remain candidates
        ↓
new source / camp / dropsite / alternative demand
```

Likewise a strategic reservation can be valid while immediate execution is unauthorized because prerequisites or affordability are missing.

The scheduler must therefore report both:

```text
DESIRED TARGET
ACTUAL PRODUCTIVE CAPACITY
```

and the delta between them.

## 14. Proposed Economic State contract

```text
ECON_GENERATION
observed-at

DEMAND
  food
  wood
  gold
  stone
  priority/reason

RESERVATION
  food
  wood
  gold
  stone
  reservation IDs

TARGET
  food-workers
  wood-workers
  gold-workers
  stone-workers

ACTUAL
  food-workers
  wood-workers
  gold-workers
  stone-workers

DELTA
  target - actual

CONSTRAINTS
  housing
  infrastructure
  source availability
  threat
  strategic commitment

VALIDITY
  fresh/stale
  generation
```

## 15. Negative findings

Not proven from static stock inspection:

- one centralized economic scheduler object;
- generalized demand vectors;
- generalized reservation IDs;
- explicit allocation hysteresis;
- exact timing from strategic-number change to worker command;
- a single rule responsible for all worker reassignment.

What IS proven is the functional chain from conditional economic/military state to strategic-number percentages, from percentages to integer worker targets, and from targets into separate worker-tasking controllers.

## Qualification

Static forensic confidence: HIGH for the percentage → integer target conversion and distributed policy pipeline.

Runtime confidence: NOT ESTABLISHED.

No live AEGIS runtime files modified.
