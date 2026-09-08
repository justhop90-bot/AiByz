# P0 Production Queue Arbitration QC — 2026-09-07

## Scope
Direct forensic inspection of untouched stock `Promisory/units.per`, `escrow.per`, `researches.per`, and `buildings.per` to determine how strategic production requests become physical queue actions and how competing requests are arbitrated.

Authoritative local corpus:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

## Cross-reference update
External scripting references materially corroborate the native mechanisms identified locally:
- `up-can-train`, `up-train`, `up-can-build`, `up-build`, `up-can-research`, and `up-research` are documented engine actions/facts.
- UserPatch release notes explicitly document escrow-aware command semantics and state that `sn-enable-training-queue` affects `can-train`, `can-train-with-escrow`, `train`, `up-can-train`, and `up-train` immediately in rules.
- Historical UserPatch notes document `up-release-escrow` and `up-modify-escrow` as native escrow operations, confirming that the stock escrow observations are engine-level rather than merely Promisory bookkeeping.
- The external command index documents `up-train` and `up-train-site-ready`, supporting the distinction between selecting/validating a training endpoint and issuing the physical training action.
- Official DE Update 42848 confirms that the modern DE scripting ABI has changed over time, including strategic-number capacity and object-data semantics; therefore current-stock confirmation remains mandatory for version-specific behavior.

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
`units.per` initializes many independent production goals to `no`, including `trainvillager`, military, siege, naval, and other production goals. Later rules selectively set them to `yes` based on strategic conditions. Therefore a production request is not itself a queue command.

## 2. Goal arbitration is explicitly distributed
Stock contains numerous rules that turn competing goals off when another demand becomes dominant. Examples include knight/camel, pike/camel, archer/cavalry-archer/hand-cannoneer, mangonel/scorpion, and ram/trebuchet competition, plus population and military-cap suppression.

This is not a FIFO scheduler. It is a rule-mediated arbitration graph.

## 3. A special global gate exists: `siegereq`
Many final production rules require `(goal siegereq yes)` before issuing the actual `train` command. The same gate appears in multiple unit categories. Rules also set/clear `siegereq`, so it is an execution authorization state rather than passive metadata.

## 4. Villager production has a distinct engine-aware path
Stock uses:

```per
(goal trainvillager yes)
(up-can-train escrow-state c: villager)
```

followed by:

```per
(up-train escrow-state c: villager)
```

with pending-villager and Town Center checks around the path.

## 5. Other unit production uses queue-object discovery
Many paths use `goal trainX`, `up-can-train`, production-building searches, `object-data-progress-value`, `object-data-under-attack`, distance/index filters, `action-train`, and a later `can-train`/`train` stage.

This establishes the production building as a selectable operational resource.

## 6. Queue availability is not equivalent to building count
A production building can be excluded because of current progress, attack state, search position, or other endpoint constraints. Therefore `building-type-count == N` does not prove N usable production endpoints.

## 7. Production command has a two-stage structure
The recurring pattern is:

```text
Stage A: discover / prepare queue target
Stage B: execute train/research/build
```

This supports the architecture rule:

> COMMAND ISSUED != TASK CONFIRMED

## 8. Research follows the same architectural pattern
`escrow.per` dispatches research using escrow flags and `can-research-with-escrow`, followed by `research`. Costs are registered before authorization.

## 9. Construction participates in the same expenditure architecture
Construction has its own placement/resource/state arbitration while escrow can register object costs and authorize building through `can-build-with-escrow`.

## 10. Escrow is reset and rematerialized as a transaction cycle
Stock releases previous escrow and later writes current requested costs. Historical UserPatch notes independently document `up-release-escrow` and `up-modify-escrow`, including the distinction between escrow-included and escrow-deducted execution states.

This strongly supports a transactional economic model rather than a permanently reserved ledger.

## 11. Priority is partly encoded by rule graph topology
The combination of goal mutation, jump routing, suppression, escrow, and execution gates means effective priority is emergent from control flow and state, not from one explicit queue.

## 12. Military population acts as a global production constraint
Late `units.per` logic can suppress military production goals when military population reaches calculated limits.

## 13. Population pressure also feeds production arbitration
Civilian population, housing headroom, excess resources, military population, and strategic state can suppress or permit production categories.

## 14. Negative finding: no universal explicit FIFO/priority queue proved
Direct inspection did not establish a single universal priority queue or explicit integer priority assigned to every production request.

## 15. AEGIS design consequence
AEGIS should expose a centralized **logical arbitration service** while preserving distributed physical endpoints:

```text
DEMANDS → ARBITRATION → RESERVATION/SUPPRESSION/AUTHORIZATION
        → QUEUE ENDPOINT → PHYSICAL COMMAND → OBSERVATION → VERIFICATION → RECOVERY
```

## 16. Recommended AEGIS contracts

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

## 17. Critical architecture rule
Do not collapse:

```text
Strategic commitment
Economic demand
Resource reservation
Execution authorization
Queue endpoint selection
Command issuance
Execution confirmation
```

They are observably distinct.

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
No AEGIS runtime files were modified during this forensic pass. The untouched stock corpus remains authoritative.

## Sources and links

- Official World's Edge Update 42848 — DE scripting ABI changes: https://www.ageofempires.com/news/aoe2de-update-42848/
- Official World's Edge Update 61321 — AI script debugging and control-flow diagnostics: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/
- AoE2 AI Scripting Encyclopedia — command index: https://airef.github.io/commands/commands-index.html
- AoE2 AI Scripting Encyclopedia — UserPatch patch notes, including escrow and training-queue semantics: https://airef.github.io/tables/up-patch-notes.html
- UserPatch Scripting Guide — command/fact/action reference: https://userpatch.aiscripters.net/reference.html
- Public AI scripting corpus used as behavioral evidence: https://gist.github.com/mateuszszulc/491e6e94797ee0fcd4a6f24229d1be3f
