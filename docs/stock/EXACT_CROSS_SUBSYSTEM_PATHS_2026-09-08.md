# Exact Cross-Subsystem Rule Paths — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`  
**Primary source:** target `AI (HD version).per`, SHA-256 `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`  
**Status:** STATIC DECONSTRUCTION — runtime semantics remain unqualified

## Scope

This pass uses exact rule blocks from the target-build AI source to establish concrete cross-subsystem paths. It deliberately does not infer interpreter ordering from textual adjacency.

## Strategy → Economy / Military

### Rule 7526–7541

Inputs:

- `enemy-goal == flush`
- `control-goal != aggressive-rush`
- `control-goal != shot`
- `strategy-goal != sling`
- `position-goal == flank`
- current age is dark
- `food-amount >= 430`

Mutations:

- `strategy-goal := flush`
- `unit-goal := default-flush-unit`
- `sn-task-ungrouped-soldiers := 1`
- `spread-military-goal := 1`
- enable `spread-military-timer` for 240

Static interpretation:

```text
enemy context + spatial posture + economy
            ↓
      strategic transition
            ↓
       military demand
```

This is a concrete example of enemy/economic observation changing strategic state and military composition simultaneously.

### Rule 7572–7589

Inputs include:

- feudal age
- `strategy-goal != flush`
- `control-goal != shot`
- `position-goal == flank`
- `food-amount < 500` OR `unit-goal == skirmisher`
- enemy military population > 2

Mutations:

- `strategy-goal := flush`
- `unit-goal := default-flush-unit`
- `control-goal := belated-flush-defense`

The source comment explicitly states that the control mutation changes gatherer percentages to collect more wood.

Static path:

```text
enemy military pressure
        +
food/resource state
        ↓
strategy
        ↓
unit demand
        ↓
control/economic response
```

## Scouting / Enemy → Military

### Rules 6858–6868, 6882–6892, 6906–6916

The controller observes enemy composition using `players-unit-type-count focus-player ...` for cavalry-archer, elephant-archer, hand-cannoneer, skirmisher, conquistador, and janissary lines.

It then mutates:

```text
sn-archer-threat := 2 / 3 / 4
```

Static path:

```text
enemy unit observation
        ↓
   archer-threat SN
        ↓
 military policy consumers
```

These rules are direct evidence of an observation → threat-signal transformation. They do not prove when downstream consumers execute.

### Rules 7526–7626

Enemy state is also used directly in counter-flush decisions. In several rules, `enemy-goal == flush` combines with `position-goal == flank`, `control-goal`, age, resource, and building conditions to produce a flush transition and military-unit selection.

This establishes that `enemy-goal` is not isolated scouting metadata; it participates in active strategic/military control.

## Economy → Construction

### Rule 26189–26206

Inputs:

- town center exists
- wood availability / resource-control conditions
- wood service distance condition
- `game-time > 180`
- `farm-goal == 1` with fewer than 2 pending farms OR `farm-goal == 2`
- fewer than 8 pending farms
- `can-build farm`

Action:

```text
build farm
```

Static path:

```text
resource/logistics state
        +
     farm-goal
        ↓
 construction eligibility
        ↓
    build farm
```

This is a concrete economic/infrastructure edge, not merely co-presence.

### Rules 26137–26175

The controller combines wood/stone/economic conditions, villager counts, research state, building counts, and `can-build` predicates to issue `build stable`, `build archery-range`, and `build barracks`.

Static pattern:

```text
resources + population + research + existing infrastructure
                         ↓
                  build eligibility
                         ↓
                  engine build action
```

This demonstrates that production infrastructure is jointly constrained by economic and technology state.

## Strategy → Construction

### Rule 25833–25889

The controller uses strategic/economic conditions such as maximum town size, research-pending state, wood/gold availability, existing building counts, and `can-build` before issuing `build-forward` for production/siege infrastructure.

The exact examples include:

- archery range
- stable
- barracks
- siege workshop

Static path:

```text
strategic / technology / resource state
                ↓
       infrastructure demand
                ↓
          build-forward
```

## Important negative result

Textual co-occurrence is not sufficient to claim causality. For example, a rule that reads `strategy-goal` and writes `unit-goal` establishes a static dependency but not that the engine immediately executes the new unit goal before another rule pass.

Likewise, `build farm` establishes an engine-facing command in the source, but exact pending-object confirmation timing remains a runtime qualification item.

## Architecture consequence

These exact paths validate the AEGIS separation:

```text
Observation
    ↓
Context / Situation
    ↓
Strategic Intent
    ↓
Demand
    ↓
Reservation / Arbitration
    ↓
Service Request
    ↓
Engine Command
    ↓
Observation
    ↓
Verification / Recovery
```

The stock controller often compresses several of these stages into one rule block. AEGIS should not reproduce that compression merely for source fidelity.

## Stock-to-AEGIS translation rule

Preserve the behavioral relationship, not the accidental representation.

Example:

```text
stock:
food-amount + farm-goal → build farm

AEGIS:
FoodState + FarmDemand
       ↓
ConstructionRequest
       ↓
ConstructionService
       ↓
FarmExecutionState
```

## Next static target

The three major subsystem edges are now grounded by concrete source rules. The next pass should extract **authority boundaries**: identify which states are truly owned by strategy, economy, construction, military, scouting, and research, and which historical channels are merely shared intermediaries.

No runtime qualification is implied by this document.
