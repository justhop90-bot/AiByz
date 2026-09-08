# P0 Production Queue Arbitration QC — 2026-09-07

## Scope
Direct forensic inspection of untouched stock `Promisory/units.per`, `escrow.per`, `researches.per`, and `buildings.per` to determine how strategic production requests become physical queue actions and how competing requests are arbitrated.

Authoritative local corpus:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

## Executive conclusion
Stock does not expose a single universal production scheduler with one explicit priority queue. Instead, it implements **distributed arbitration** using persistent goal flags, rule ordering/jump chains, suppression rules, escrow gates, queue/building searches, and final engine commands.

The effective pipeline is:

```text
STRATEGIC DEMAND
      ↓
PRODUCTION GOAL FLAG
      ↓
CONFLICT / SUPPRESSION RULES
      ↓
RESOURCE / ESCROW STATE
      ↓
QUEUE-CAPABLE OBJECT SEARCH
      ↓
CAN-* AUTHORIZATION
      ↓
PHYSICAL TRAIN / RESEARCH / BUILD COMMAND
      ↓
ENGINE STATE
      ↓
NEXT CONTROL PASS
```

## 1. Production intent is represented as persistent goal state
`units.per` initializes many independent production goals to `no`, including:
- `trainvillager`
- `trainarcher`
- `trainskirm`
- `trainpike`
- `trainknight`
- `traincamel`
- `trainhussar`
- `trainunique`
- siege and naval production goals.

Hundreds of later rules selectively set these goals to `yes` based on strategic conditions. Therefore a production request is not itself a queue command.

## 2. Goal arbitration is explicitly distributed
Stock contains numerous rules that turn competing goals off when another demand becomes dominant. Examples include:

- `trainknight` can be disabled in favor of camel production under specific economic/strategic conditions.
- `trainpike` can be disabled in favor of camel production.
- `trainarcher` can be disabled in favor of cavalry-archer or hand-cannoneer production.
- `trainmangonel` and `trainscorpion` explicitly suppress one another in several paths.
- `trainram` can be suppressed when trebuchet becomes the selected siege requirement.
- late-game population/military-cap rules can suppress broad categories of production simultaneously.

This is not a FIFO scheduler. It is a rule-mediated arbitration graph.

## 3. A special global gate exists: `siegereq`
Many final production rules require:

```per
(goal siegereq yes)
```

before issuing the actual `train` command. The same gate appears in multiple unit categories, including unique units, monks, trade units, and siege-related production paths.

This demonstrates that some production is intentionally delayed behind a broader execution authorization state.

`units.per` also contains rules that set or clear `siegereq`, so it is not merely a passive status bit.

## 4. Villager production has a distinct engine-aware path
Stock's final villager execution path is materially different from simple `train villager`:

```per
(goal trainvillager yes)
(up-can-train escrow-state c: villager)
```

followed by:

```per
(up-train escrow-state c: villager)
```

There are additional rules that inspect pending villagers, Town Center state, and Town Center progress before issuing another production action.

This establishes:

```text
TRAINVILLAGER INTENT
 → ESCROW-AWARE AFFORDABILITY/AUTHORIZATION
 → TC STATE CHECK
 → PHYSICAL QUEUE COMMAND
```

## 5. Other unit production uses queue-object discovery
For many units the pattern is:

```per
(goal trainX yes)
(goal temporary-goal 1579175)
(up-can-train 0 c: X)
```

then:

```per
(up-full-reset-search)
(up-find-local c: production-building c: 240)
(up-remove-objects search-local object-data-progress-value >= 1)
(up-remove-objects search-local object-data-under-attack >= 1)
(up-clean-search search-local object-data-distance search-order-asc)
(up-remove-objects search-local object-data-index >= 1)
(up-get-search-state local-total)
(up-target-point 0 action-train c: X)
```

A subsequent rule observes that a suitable production object was found and then performs:

```per
(can-train X)
(train X)
```

Therefore the production building itself is a selectable operational resource.

## 6. Queue availability is not equivalent to building count
The search explicitly excludes production objects based on:
- `object-data-progress-value`
- `object-data-under-attack`
- object index/order
- distance.

Thus:

```text
building-type-count == N
```

is not sufficient evidence that N buildings are currently usable production endpoints.

The engine-facing operational test is closer to:

```text
EXISTS production object
AND object usable
AND object not excluded by current state
AND can-train(unit)
```

## 7. Production command has a two-stage structure
The recurring pattern is:

```text
Stage A: discover / prepare queue target
Stage B: execute `train`
```

For many production types, `up-target-point ... action-train` is used to prepare or validate the selected production endpoint, with a temporary goal acting as a cross-rule state marker.

This is another instance of:

> COMMAND ISSUED != TASK CONFIRMED

The following rule can re-evaluate engine state rather than assuming that the previous search succeeded permanently.

## 8. Research follows the same architectural pattern but with a different endpoint
`escrow.per` contains a large research dispatch table:

```per
(up-compare-flag escrow-flag == N)
(can-research-with-escrow technology)
=>
(research technology)
```

The preceding decision layer creates research costs with:

```per
(up-add-research-cost c: technology c: 1)
(up-modify-flag escrow-flag...)
```

Therefore research follows:

```text
RESEARCH DEMAND
 → RESEARCH COST REGISTRATION
 → ESCROW FLAG
 → CAN-RESEARCH-WITH-ESCROW
 → RESEARCH COMMAND
```

## 9. Construction participates in the same expenditure architecture
`buildings.per` independently performs construction arbitration and placement. It tests resource conditions, building availability, spatial constraints, and construction state before requesting a build.

The escrow subsystem can register object costs for structures and later use `can-build-with-escrow` as an execution gate.

Thus construction is not outside the economic scheduler. It is another consumer of the reservation/expenditure substrate.

## 10. Escrow is reset and rematerialized as a transaction cycle
The stock escrow controller begins a cycle by releasing previous escrow and clearing percentages/values:

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
```

It later materializes current requested costs:

```per
(up-modify-escrow wood g:= cost-wood)
(up-modify-escrow food g:= cost-food)
(up-modify-escrow gold g:= cost-gold)
(up-modify-escrow stone g:= cost-stone)
```

This strongly supports a transactional economic model rather than a permanently reserved ledger.

## 11. Priority is partly encoded by rule graph topology
The strongest evidence against a centralized priority queue is the prevalence of:

```text
set goal
jump rule
suppress another goal
modify cost
set escrow flag
execute
```

The `up-jump-rule` graph determines which families of rules are reached or bypassed under strategic conditions.

Consequently effective priority is emergent from:
- rule ordering
- jump routing
- goal state
- suppression rules
- strategic-number conditions
- resource/escrow state
- military population constraints
- threat state
- pending queue state.

## 12. Military population acts as a global production constraint
Late `units.per` logic computes an allowed military population from ally/enemy military populations and game difficulty/context, then suppresses large groups of military production goals when the actual military population reaches the calculated limit.

The important architectural implication is:

```text
UNIT DEMAND
     ↓
MILITARY CAPACITY POLICY
     ↓
PRODUCTION GOAL SUPPRESSION
```

This is policy arbitration before queue execution.

## 13. Population pressure also feeds production arbitration
The same file contains late-game rules that suppress or permit villagers, trade units, naval units, and military units based on:
- population cap
- civilian population
- housing headroom
- excess resources
- military population
- strategic state.

Therefore the scheduler is cross-domain: civilian, military, naval, trade, and research decisions can compete indirectly for the same finite economic/queue capacity.

## 14. Negative finding: no universal explicit FIFO/priority queue proved
Direct inspection did **not** establish a single structure equivalent to:

```text
priority_queue<Action>
```

nor an explicit universal integer priority assigned to every production request.

We should therefore not implement AEGIS as a simple centralized FIFO scheduler merely because it is convenient.

## 15. AEGIS design consequence
AEGIS should expose a centralized **logical arbitration service** while preserving distributed physical endpoints:

```text
                 DEMANDS
                    ↓
             ARBITRATION SERVICE
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
   RESERVATION   SUPPRESSION   AUTHORIZATION
       ↓            ↓            ↓
       └────────────┼────────────┘
                    ↓
             QUEUE ENDPOINT
                    ↓
             PHYSICAL COMMAND
                    ↓
               OBSERVATION
                    ↓
               VERIFICATION
                    ↓
                RECOVERY
```

The logical service should be centralized because AEGIS needs coherent decisions. Physical queue selection must remain endpoint-aware because stock demonstrates that production buildings, Town Centers, castles, monasteries, docks, and siege workshops have distinct operational state.

## 16. Recommended AEGIS contracts

### Production request
```text
PRODUCTION_REQUEST
  generation
  category
  unit/technology/building
  quantity
  priority
  urgency
  strategic-reason
  resource-cost
  reservation-id
  endpoint constraints
```

### Queue endpoint
```text
QUEUE_ENDPOINT
  object-id
  endpoint-type
  operational-status
  under-attack
  progress
  queue-load
  distance
  can-execute
  observed-at
  generation
```

### Arbitration result
```text
ARBITRATION_RESULT
  request-id
  generation
  disposition
  reservation-id
  selected-endpoint
  suppression-reason
  authorization-state
  observed-at
```

### Execution lifecycle
```text
REQUESTED
 → ADMITTED
 → RESERVED
 → ENDPOINT_SELECTED
 → AUTHORIZED
 → COMMAND_ISSUED
 → ENGINE_OBSERVED
 → CONFIRMED
```

Failure paths:

```text
REQUESTED → REJECTED
RESERVED → RESERVATION_RELEASED
ENDPOINT_SELECTED → ENDPOINT_INVALID
AUTHORIZED → COMMAND_FAILED
COMMAND_ISSUED → ENGINE_STATE_NOT_OBSERVED
CONFIRMED → TASK_INTERRUPTED
```

## 17. Critical architecture rule for AEGIS
Do not collapse these states:

```text
Strategic commitment
Economic demand
Resource reservation
Execution authorization
Queue endpoint selection
Command issuance
Execution confirmation
```

They are observably distinct in the stock architecture.

## 18. Confidence

| Finding | Confidence |
|---|---|
| Production intent is represented by goals | HIGH |
| Production goals are independently suppressed/arbitrated | HIGH |
| Queue endpoints are explicitly searched/filtered | HIGH |
| `can-train` gates physical train commands | HIGH |
| Villager production uses escrow-aware train authorization | HIGH |
| Research uses escrow-aware authorization | HIGH |
| Construction participates in escrow/cost architecture | HIGH |
| Military population constrains production | HIGH |
| No single universal FIFO scheduler | HIGH from inspected corpus |
| Exact global rule-evaluation ordering semantics | NOT FULLY ESTABLISHED |
| Exact intra-tick competition when multiple rules can fire | NOT FULLY ESTABLISHED |
| Exact engine queue-depth semantics for all endpoints | NOT FULLY ESTABLISHED |

## 19. No live changes
No AEGIS runtime files were modified during this forensic pass. The untouched stock corpus remains the authoritative source.

## 20. Status
This pass closes a major forensic question: **the stock AI's economic scheduler is a distributed arbitration graph coupled to native escrow and endpoint-aware execution, not a single centralized queue.**

The next engineering target should be the remaining uncertainty: characterize the exact rule evaluation / jump semantics and determine how multiple simultaneously valid production commands are resolved within one AI update cycle. This requires engine-ABI evidence rather than further inference from strategic conditions alone.
