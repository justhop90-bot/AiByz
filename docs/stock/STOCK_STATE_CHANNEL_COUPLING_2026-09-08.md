# Stock State-Channel Coupling Map — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Purpose:** turn the stock reconstruction from module inventory into a state-flow model.

## Model

A state channel is considered coupled when multiple rules or subsystems can read, mutate, compare, reset, or indirectly consume it. Numeric identity alone does not establish ownership.

```text
producer → channel → consumer
             ↑
          resetter
```

For the stock system, the channel must additionally be annotated with its activation predicates and engine-facing side effects.

## High-value coupling classes

| Channel family | Typical producers | Typical consumers | Reset/reconciliation | Risk |
|---|---|---|---|---|
| Strategy goals | strategy/civ policy | production, economy, military | age/strategy transitions | HIGH |
| Unit goals | composition/strategy | `units`, military control | composition changes | HIGH |
| Building/construction goals | economy/threat/strategy | buildings/placement | pending/failure/replacement | HIGH |
| Gatherer allocation state | economy policy | worker tasking | reconciliation loops | HIGH |
| Housing state | economy/building policy | worker production/building | housing completion/failure | HIGH |
| Age transition state | economy/research | production/research | age completion | HIGH |
| Position/placement state | construction/scouting | build/target systems | placement reset | HIGH |
| Threat state | threat/scouting/military | economy/construction/retreat | threat expiry/observation | HIGH |
| Escrow state | economic arbitration | build/train/research | release/adjustment | HIGH |
| Town-size state | economy/building | construction/population | infrastructure progression | MEDIUM-HIGH |
| Naval state | water/scout/military | navy production/control | water-state reconciliation | MEDIUM-HIGH |
| Trade state | economy/trade | market/trade production | resource-state changes | MEDIUM |

## State-flow rule

For each important channel, reconstruction must answer five static questions before implementation:

1. **Who writes it?**
2. **Who reads it?**
3. **Who resets or supersedes it?**
4. **Under which activation predicates do those operations exist?**
5. **What physical engine operation ultimately depends on the channel?**

A sixth question is deferred to runtime qualification:

6. **When does a mutation become visible to another rule?**

## Construction example

Historical construction demonstrates a multi-stage dependency chain:

```text
threat / strategic demand
        ↓
construction demand goal
        ↓
can-build / placement search
        ↓
placement state
        ↓
build-line or build command
        ↓
builder assignment
        ↓
pending object
        ↓
completion / failure
        ↓
reset / retry / alternative
```

This is why a construction goal cannot be treated as a simple Boolean request.

## Economy example

Worker control similarly forms a state machine:

```text
resource demand
   ↓
allocation target
   ↓
candidate worker search
   ↓
eligibility filtering
   ↓
target selection
   ↓
order/task assignment
   ↓
productive state
   ↓
interruption/failure
   ↓
reselection
```

The historical `gatherers` substrate therefore represents an operating system, not merely a gather-percentage table.

## Byzantine extraction consequence

Byzantine-specific policy must be attached to this coupling graph. A civilization-conditioned rule that changes a goal or SN is not merely “a Byzantine rule”; it is a mutation in a larger state machine whose downstream effects may occur far from the original source line.

The next extraction pass should therefore produce records at the **rule-site level**, not only at the module level:

```text
RULE_ID
SOURCE_FILE
SOURCE_LINE
ACTIVATION_PREDICATE
READ_GOALS
WRITE_GOALS
RESET_GOALS
READ_SN
WRITE_SN
RESET_SN
TIMERS
FACTS
OBJECT_DATA
ENGINE_ACTION
DOWNSTREAM_CONSUMERS
FAILURE/RECOVERY_PATH
EVIDENCE_STATUS
```

## Boundary

This document is static reconstruction. Scheduler timing, mutation visibility, command completion, and other interpreter-temporal questions remain explicitly unqualified until the later runtime qualification phase.
