# P0 Worker Target-to-Assignment QC — 2026-09-07

Target: AoE2DE 101.103.48987.0 / BuildID 24094652
Corpus: untouched stock `resources/_common/ai/Promisory` on Weebo.
Status: forensic evidence; implementation deferred.

## Executive finding

The stock economy has now been traced across the critical boundary between **desired worker counts** and **physical worker reassignment**.

The architecture is not a centralized assignment table. It is a distributed feedback controller:

```text
Strategic conditions
      ↓
Gatherer percentages
      ↓
Integer worker targets
      ↓
Actual role counts
      ↓
Deficit / exceptional condition
      ↓
Candidate worker search
      ↓
Eligibility filtering
      ↓
Spatial/source filtering
      ↓
Resource selection
      ↓
Physical command
      ↓
Engine-derived role/task state
```

The most important new result is that **stock reassignment is condition-driven and candidate-search-driven**. It does not appear to maintain a persistent per-villager assignment registry in `.per` code.

## 1. Target counts are explicit persistent goals

`dawn.per` converts strategic percentages into integer goals. The exact sequence is:

```per
(up-modify-goal wood-villagers s:= sn-wood-gatherer-percentage)
(up-modify-goal food-villagers s:= sn-food-gatherer-percentage)
(up-modify-goal gold-villagers s:= sn-gold-gatherer-percentage)
(up-modify-goal stone-villagers s:= sn-stone-gatherer-percentage)
(up-modify-goal wood-villagers g:* villagercount)
(up-modify-goal food-villagers g:* villagercount)
(up-modify-goal gold-villagers g:* villagercount)
(up-modify-goal stone-villagers g:* villagercount)
(up-modify-goal wood-villagers c:/ 100)
(up-modify-goal food-villagers c:/ 100)
(up-modify-goal gold-villagers c:/ 100)
(up-modify-goal stone-villagers c:/ 100)
```

Thus `wood-villagers`, etc. are integer desired-role populations derived from current civilian population and current strategic policy.

They are not evidence of named worker identities.

## 2. `sum-villagers` is an allocation reconciliation accumulator

`dawn.per` checks:

```per
(up-compare-goal sum-villagers g:< villagercount)
```

and sets:

```per
(set-goal villager-addition 1)
```

Subsequent rules add one worker at a time to a selected target role and increment `sum-villagers`.

Examples include:

```per
(up-modify-goal wood-villagers c:+ 1)
(up-modify-goal sum-villagers c:+ 1)
(set-goal villager-addition 0)
```

and equivalent food/gold branches.

This is a discrete reconciliation loop, not a one-shot vector assignment.

## 3. Allocation has explicit priority/exception ordering

The first reconciliation branches are not neutral.

For example, when housing is tight, wood can receive an additional worker:

```per
(housing-headroom < 3)
(population-headroom > 0)
(up-compare-goal excessWood < house-cost)
(up-pending-objects c: house <= 0)
(up-compare-goal wood-villagers < 2)
(game-time >= 60)
```

then:

```per
(up-modify-goal wood-villagers c:+ 1)
(up-modify-goal sum-villagers c:+ 1)
```

Other branches preferentially add food, then wood, based on minimum food, town-center count, pending villagers, strategy, and other conditions.

Therefore the target vector is itself a policy-resolution mechanism.

## 4. Target deficit is compared against actual engine role state

The wood controller provides direct evidence of the next layer:

```per
(unit-type-count villager-wood g:<= wood-villagers)
```

When the actual wood-worker population is at or below the desired target, stock enters a worker-search path.

The controller then performs:

```per
(up-find-local c: villager-class g: villagercount)
```

followed by exclusion filters.

This proves the architecture is effectively:

```text
Desired wood population
        ↓
Compare with actual villager-wood population
        ↓
If deficient, search eligible villagers
```

The engine's `unit-type-count villager-wood` is therefore part of the feedback loop.

## 5. Candidate selection is not “pick any villager”

The wood path searches all villagers but excludes several classes of workers:

```per
(up-remove-objects search-local object-data-action == actionid-enter)
(up-remove-objects search-local object-data-order == orderid-enter)
(up-remove-objects search-local object-data-target == tree-class)
(up-remove-objects search-local object-data-carry >= 1)
```

It also filters by proximity to the selected lumber camp and excludes attack/build conflicts:

```per
(up-filter-distance c: -1 c: 6)
(up-filter-exclude -1 actionid-attack orderid-build -1)
```

This is a significant architecture finding.

A worker already carrying a resource is not treated as an ordinary reassignment candidate. A worker attacking or building is also protected from this allocation path.

Therefore reassignment is **opportunistic but constrained**.

## 6. Existing productive assignments are not blindly destroyed

The candidate search explicitly excludes:

- workers entering objects
- workers already targeting trees
- workers carrying resources
- workers in attack state
- workers associated with build orders in the relevant exclusion filter

This supports a preservation principle:

```text
Do not interrupt a worker merely because another resource has demand.
```

Instead, stock first looks for an eligible candidate set.

This is not proof that stock never forcibly retasks productive workers. Other specialized controllers can deliberately stop workers, and explicit emergency/retasking rules exist. The safe conclusion is narrower: **the ordinary wood-deficit acquisition path protects several active worker states.**

## 7. Explicit retasking exists as a separate mechanism

The corpus contains `up-retask-gatherers` callsites in `init.per` and `gatherers.per`.

These occur in special transition/reallocation scenarios such as enabling a mill and commented/conditional food-source-to-hunt transitions.

This establishes two different mechanisms:

```text
NORMAL DEFICIT ACQUISITION
→ find eligible worker

EXPLICIT RETASKING
→ deliberately interrupt/reclassify a worker population
```

The distinction is architecturally important.

Normal allocation should not be implemented as universal forced retasking.

## 8. Source selection occurs after worker candidate selection

The wood path first establishes a nearby lumber-camp point and candidate worker set. It then searches for wood:

```per
(up-filter-distance c: -1 c: 4)
(up-filter-status c: status-resource c: list-active)
(up-find-resource c: wood c: 8)
(up-filter-status c: status-ready c: list-active)
(up-find-resource c: wood c: 8)
(up-remove-objects search-remote object-data-tasks-count >= 2)
```

The final resource candidates are sorted by distance and reduced to the selected object before:

```per
(up-target-objects 0 action-default -1 -1)
```

Therefore actual assignment is a **joint worker/source selection problem**, not merely worker-role assignment.

## 9. `action-default` is the physical assignment boundary

The final wood operation is:

```per
(up-target-objects 0 action-default -1 -1)
```

The `.per` layer therefore does not demonstrate a separate persistent “assignment object” being created.

Persistence comes from the engine state that results from the command: target, order, action, carry, task load, and subsequent role-count classification.

Consequently:

```text
COMMAND ISSUED
      ≠
TASK CONFIRMED
```

This is consistent with the previously established worker interruption/recovery model.

## 10. Food is demonstrably a portfolio, not one role

`villager-food` is an aggregate category while stock separately exposes:

- `villager-shepherd`
- `villager-forager`
- `villager-farmer`
- `villager-hunter`
- `villager-fisherman`

The stock code explicitly retasks between these source roles under conditions involving sheep, forage, farms, hunting distance, fish, and strategic food demand.

For example, a commented/conditional path explicitly describes retasking a forager to hunt and calls `up-retask-gatherers`.

Thus AEGIS must not model food as one undifferentiated worker bucket.

## 11. Buildings and economy contend through shared worker state

Construction uses `villager-builder` as an operational population and gatherers uses worker-state filters that exclude builders/build orders in relevant paths.

This creates an implicit shared-resource constraint:

```text
Civilian population
   ├── resource workers
   ├── builders
   ├── hunters / shepherds / foragers
   ├── fishermen
   └── other operational roles
```

The roles are therefore competing consumers of the same finite worker population.

No evidence was found for a centralized scheduler resolving every role in one place. The stock solution is distributed conditional control.

## 12. Escrow interacts with worker allocation indirectly

`escrow.per` uses actual worker-role counts alongside resource stockpiles when deciding whether strategic investments can proceed.

Examples include conditions involving:

```per
unit-type-count villager-wood
wood-amount
unit-type-count villager-stone
total-stone-amount
```

This demonstrates a feedback loop:

```text
Worker allocation
      ↓
Resource production capacity
      ↓
Resource stockpile
      ↓
Escrow / investment authorization
      ↓
Strategic demand
      ↓
Worker allocation
```

The economy is therefore a closed-loop controller rather than a static assignment system.

## 13. Housing and production create non-resource allocation pressure

`dawn.per` does not only reconcile economic percentages. It also modifies worker targets in response to housing, pending villager production, town-center count, food affordability, and strategic conditions.

This means AEGIS cannot define economic allocation as:

```text
resource demand → resource workers
```

It must include civilization-maintenance demand:

```text
food demand
wood demand
housing demand
construction demand
production demand
military demand
technology demand
```

These demands compete for the same worker pool and resource budget.

## 14. Correct AEGIS Worker Allocation abstraction

The evidence supports the following service contract:

```text
WORKER_ALLOCATION_REQUEST
  generation
  desired-role-vector
  role-priority
  urgency
  protected-role-policy
  source constraints
  dropsite constraints
  reason

WORKER_ALLOCATION_SNAPSHOT
  generation
  observed-at
  actual-role-vector
  desired-role-vector
  deficits
  protected-worker-count
  eligible-worker-count
  builder-count
  task-invalid-count
  freshness

WORKER_ALLOCATION_RESULT
  generation
  role
  worker-set / candidate count
  source
  command-stage
  confirmation-stage
  failure-class
  failure-detail
```

The implementation should preserve the distinction between:

```text
DESIRED COUNT
ACTUAL COUNT
DEFICIT
CANDIDATE SET
ASSIGNMENT COMMAND
OBSERVED RESULT
```

## 15. Recommended reassignment algorithm for AEGIS

The stock evidence supports this architecture, while avoiding unsupported claims about hidden engine internals:

```text
1. Read current civilization census.
2. Read current desired role vector.
3. Calculate role deficits.
4. Protect workers with incompatible active state.
5. Identify eligible candidates.
6. Rank candidates by task safety and spatial suitability.
7. Validate source and dropsite serviceability.
8. Issue assignment command.
9. Re-observe engine state.
10. Confirm role/productivity transition.
11. If failed, preserve cause and re-enter allocation.
```

For explicit emergency retasking:

```text
Demand spike / source failure / threat
        ↓
Protected-state evaluation
        ↓
Select interruptible worker class
        ↓
Stop/reclassify if required
        ↓
New source selection
        ↓
Command
        ↓
Observe
```

## 16. Critical architectural correction for AEGIS

Do not create a central table such as:

```text
worker #17 = wood
worker #18 = food
worker #19 = gold
```

as the primary source of truth.

Stock's observable architecture is much closer to:

```text
ENGINE STATE
    ↓
ROLE COUNTS
    ↓
DEFICIT
    ↓
SEARCH/FILTER
    ↓
COMMAND
    ↓
ENGINE STATE
```

AEGIS may maintain metadata for request ownership, generation, freshness, and failure diagnosis, but the engine remains authoritative for physical worker state.

## 17. Negative findings

Not proven:

- a centralized stock worker-allocation manager
- persistent per-villager assignment records in `.per`
- exact priority ordering across every civilian role controller
- universal protection of productive workers from explicit retasking
- exact timing between role-count change and command issuance
- exact engine implementation of `villager-wood` role classification
- universal fairness policy among eligible workers
- exact hidden semantics of `up-retask-gatherers`
- universal builder-vs-gatherer arbitration outside inspected rules

## 18. Architectural consequence

The civilian substrate should be modeled as a **feedback allocator**, not a dispatcher:

```text
               ┌──────────────────────────┐
               │   Strategic / Economic   │
               │        Demand            │
               └────────────┬─────────────┘
                            ↓
                    Desired Role Vector
                            ↓
                    Actual Role Census
                            ↓
                         Deficit
                            ↓
                    Candidate Selection
                            ↓
               ┌────────────┴─────────────┐
               │                          │
          Preserve active             Interrupt only
             workers                  when justified
               │                          │
               └────────────┬─────────────┘
                            ↓
                    Source / Site Selection
                            ↓
                       Command Issue
                            ↓
                    Engine State Change
                            ↓
                       Re-observation
                            ↓
                         Recovery
```

This is now the strongest evidence-backed model for the AEGIS Worker Allocation Service.

## Qualification status

Static forensic confidence: HIGH for target-vector derivation, deficit-triggered candidate search, worker-state filtering, source selection, and command boundary.

Runtime confidence: NOT ESTABLISHED.

No live AEGIS runtime files were modified in this pass.
