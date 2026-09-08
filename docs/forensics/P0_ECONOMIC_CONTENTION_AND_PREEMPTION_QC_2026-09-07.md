# P0 Economic Contention and Preemption QC — 2026-09-07

## Scope

Forensic inspection of the untouched stock AoE2DE `Promisory` corpus, focused on how competing economic requirements alter worker allocation and whether stock contains a single global scheduler/preemption mechanism.

Authoritative local corpus:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\Promisory`

## Executive finding

Stock does **not** expose evidence of one centralized civilian scheduler that computes a universal priority queue across food, wood, gold, stone, construction, research, military production, and emergencies.

Instead, contention is implemented as a **distributed control-flow arbitration system**:

```text
multiple strategic conditions
        ↓
ordered rules / jump chains
        ↓
strategic-number mutation
        ↓
integer gatherer targets
        ↓
resource-specific deficit checks
        ↓
worker eligibility filters
        ↓
command
```

The effective priority of a demand is therefore partly encoded in **which rule branch executes first and which later branches are skipped or reached**, not in a single numeric scheduler.

## 1. Gatherer policy is repeatedly rewritten

`gatherers.per` contains many mutually contextualized rules that directly rewrite:

- `sn-wood-gatherer-percentage`
- `sn-food-gatherer-percentage`
- `sn-gold-gatherer-percentage`
- `sn-stone-gatherer-percentage`

Examples observed in the untouched file include transitions such as:

- 45/55/0/0
- 58/33/9/0
- 48/37/15/0
- 37/47/16/0
- 30/50/20/0
- 40/53/22/0 in fast-Imperial-related logic
- 70/20/10/0 in water/strategy-specific paths

These are not static defaults. They are outputs of conditional policy rules involving age, food/gold stockpiles, buildings, research state, escrow flags, population, strategy, and map/resource conditions.

## 2. Escrow participates in policy arbitration

Multiple gatherer-policy rules explicitly test `escrow-flag`, including values associated with Feudal/Castle/Imperial economic transitions.

Therefore resource allocation is not isolated from spending authorization. Economic reservation/escrow state can change the desired worker vector.

This supports the architectural separation:

```text
Strategic commitment
        ≠
Economic demand
        ≠
Resource escrow
        ≠
Worker allocation
        ≠
Execution authorization
```

But the stock implementation couples them through rule conditions rather than a single abstract service object.

## 3. Food/wood/gold/stone contention is policy-driven, not merely shortage-driven

Observed rules change worker percentages when combinations of conditions become true. Examples include:

- Feudal/Castle timing
- Castle-age resource thresholds
- blacksmith/range/market presence
- Wheelbarrow state
- number of farms
- population thresholds
- Town Center count
- escrow state
- fast-Imperial conditions
- rush/flush/grush/boom strategy branches
- resource stockpile thresholds

Consequently, `resource low → add workers` is an incomplete model.

The correct model is:

```text
civilization state
 + strategic objective
 + technology/building state
 + stockpile state
 + escrow state
 + map/serviceability state
        ↓
policy transformation
        ↓
desired worker vector
```

## 4. There is explicit retasking, but it is selective

The corpus contains `up-retask-gatherers` call sites. Some are associated with deliberately changing food-worker specialization, for example retasking foragers, farmers, or shepherds toward hunting under qualifying conditions.

This establishes a distinct mechanism for **intentional reassignment of already specialized workers**.

It should not be conflated with ordinary deficit filling.

Two operational modes are therefore supported by evidence:

```text
DEFICIT FILL
    desired role > actual role
    → search eligible candidates
    → assign

EXPLICIT RETASK
    strategic/source transition
    → deliberately interrupt/reclassify an existing gatherer
    → assign to new role
```

## 5. Worker protection creates implicit preemption costs

The wood allocation path searches for villagers but removes candidates carrying resources and workers associated with conflicting states such as attack/build/enter activity in the relevant search path.

Therefore an existing productive task has an implicit protection barrier.

A worker is not simply a free integer token that can be moved between resource buckets.

This means the effective cost of preemption depends on worker state:

```text
idle / uncommitted
    → cheap to reassign

productive gatherer
    → protected in ordinary candidate search

builder / attacker / carrying
    → often excluded from ordinary reassignment

explicit retask condition
    → protection may be intentionally overridden
```

The exact universal protection policy is subsystem-specific and is not proven to be identical across all resources.

## 6. `villager-addition` is a reconciliation mechanism, not a global priority queue

`dawn.per` establishes `sum-villagers` and computes desired worker counts from strategic percentages.

When `sum-villagers < villagercount`, `villager-addition` becomes active. A sequence of rules then increments one worker target and `sum-villagers` until the total reconciles with the available villager population.

Observed candidate targets include wood and food, with contextual conditions controlling which receives the next worker.

This is an **ordered reconciliation algorithm**.

It does not prove a universal utility function or global optimization solver.

The important architectural consequence is:

```text
percentage vector
      ↓
integer rounding
      ↓
remainder
      ↓
ordered remainder allocation
      ↓
exact worker target vector
```

This is a discrete allocator and should be modeled explicitly in AEGIS.

## 7. Control-flow order is part of stock priority

`gatherers.per` contains extensive `up-jump-rule` control flow. Conditions can jump over portions of the policy tree, meaning a rule's position and jump destination influence which later policy transformations can execute.

Thus stock priority cannot safely be reconstructed solely from the numerical percentages appearing in the file.

The more accurate representation is:

```text
policy branch selection
        ↓
branch-local mutations
        ↓
jump/skip
        ↓
subsequent eligible policy
```

A later rule may be semantically lower priority because an earlier branch prevents execution, even if its percentage change looks more aggressive.

## 8. Construction competes indirectly through policy

The stock corpus does not show evidence that construction simply takes a worker out of the economy through one global resource-scheduler transaction.

Instead, construction state changes other policy variables and worker populations. `villager-builder` is a distinct operational population, and gatherer allocation paths explicitly account for builders in some decisions.

Therefore construction contention is represented through **worker-state exclusion and strategic policy**, not proven global preemption accounting.

## 9. Production/research contention is similarly mediated by resource policy

Stock uses research availability/pending state, production requirements, stockpiles, and escrow conditions as inputs to gatherer policy.

The economic system therefore reacts to future spending requirements by changing worker targets before the actual spending event.

This is a form of **anticipatory allocation**:

```text
future expenditure requirement
        ↓
resource demand
        ↓
gatherer percentage change
        ↓
worker target change
        ↓
resource accumulation
```

That is materially different from a purely reactive shortage controller.

## 10. No single global preemption order is proven

We specifically looked for a universal ordering equivalent to:

```text
emergency > construction > military > research > food > wood > gold > stone
```

No such centralized ordering was established.

Instead, priorities are conditional and subsystem-local.

Examples:

- housing shortages can cause wood demand to rise
- age-up requirements can elevate food/gold demand
- military strategy can alter the desired economic vector
- escrow can alter resource allocation
- resource/serviceability failure can trigger source-specific reassignment
- threat state can alter economic behavior

Therefore AEGIS should **not** implement one hard-coded universal resource priority ladder.

## 11. Recommended AEGIS arbitration model

The stock evidence supports a typed demand arbitration layer:

```text
DEMANDS
  ECON_RESOURCE
  CONSTRUCTION
  PRODUCTION
  RESEARCH
  SAFETY
  RECOVERY

        ↓

DEMAND NORMALIZATION
  resource
  amount/rate
  deadline
  priority
  urgency
  reason
  generation
  protected-state constraints

        ↓

ARBITRATION
  feasibility
  strategic priority
  urgency
  deadline pressure
  escrow reservation
  infrastructure availability
  worker disruption cost
  threat/safety state

        ↓

TARGET VECTOR
  food
  wood
  gold
  stone
  builders
  scouts/specialists

        ↓

WORKER ALLOCATION
```

Crucially, arbitration should produce **targets and permissions**, while the worker service owns physical assignment.

## 12. AEGIS preemption policy

Recommended explicit states:

```text
UNCOMMITTED
PRODUCTIVE
PROTECTED
PREEMPTABLE
PREEMPT_REQUESTED
INTERRUPTED
REASSIGNING
CONFIRMED
```

A worker should normally move only through:

```text
productive
   ↓
preemption eligibility
   ↓
preemption authorization
   ↓
interrupt/cleanup
   ↓
new task selection
   ↓
command
   ↓
confirmation
```

Source failure is not equivalent to strategic preemption.

Threat blocking is not equivalent to resource failure.

Builder reassignment is not equivalent to ordinary gatherer allocation.

## 13. Confidence

### HIGH confidence
- stock repeatedly rewrites gatherer percentages from conditional policy
- `dawn.per` converts percentages into integer worker targets
- `villager-addition` performs ordered reconciliation
- escrow state participates in gatherer policy
- explicit `up-retask-gatherers` exists
- worker candidate filtering protects certain active states
- construction and gathering populations interact through worker-state accounting

### MEDIUM confidence
- effective policy priority is substantially encoded by rule/jump ordering
- stock uses anticipatory rather than purely reactive economic allocation

### NOT PROVEN
- one global stock priority queue
- one universal worker preemption cost
- exact rule-evaluation timing between policy mutations and worker reassignment
- exact duration of a worker's protected state
- universal construction-vs-gatherer arbitration order
- universal emergency preemption order

## Architectural consequence

The next-generation AEGIS economy should not copy stock as a giant rule tree.

It should preserve the discovered semantics while making the arbitration boundary explicit:

```text
DEMAND
  ↓
ARBITRATION
  ↓
RESERVATION / ESCROW
  ↓
TARGET VECTOR
  ↓
WORKER ALLOCATION
  ↓
TASKING
  ↓
VERIFICATION
  ↓
RECOVERY
```

Stock's distributed rule ordering is evidence of the required behavior, not necessarily the desired AEGIS implementation architecture.
