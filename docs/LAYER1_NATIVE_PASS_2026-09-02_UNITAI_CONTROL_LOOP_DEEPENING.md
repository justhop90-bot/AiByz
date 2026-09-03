# Layer 1 Native Pass — UnitAI Control-Loop Deepening

**Date:** 2026-09-02  
**Layer:** 1 — Machine Understanding  
**Scope:** Native UnitAI control-loop model, representation-aware reference recovery, and predictive consequences  
**Status:** Active archaeology; no framework implementation authority granted

---

## 1. Purpose

This pass deliberately goes one level deeper than the previous UnitAI vocabulary reconstruction. The target is not another catalogue of strings. The target is to determine what can be established about the native control loop, what failed to connect, and what the failure itself tells us about the executable's representation.

The working native model under examination is:

```text
persistent unit state
    ├── order state
    ├── action state
    ├── target state
    ├── notification state
    └── timers / queues / derived search state
             │
             ▼
        update / processing
             │
       ┌─────┴─────────┐
       │               │
   notification     order/action
   processing       processing
       │               │
       └──────┬────────┘
              ▼
        search / repair
              ▼
        target selection
              ▼
        action execution
              ▼
        simulation response
              ▼
        notification / next evaluation
```

The diagram remains a model, not a claim that the exact sequence has been recovered in native code.

---

## 2. New discriminating experiment

### 2.1 Full `.text` RIP-relative scan

A Capstone x86-64 instruction scan was run across the known native `.text` range:

- Image base: `0x140000000`
- `.text` virtual start: `0x140001000`
- `.text` size: `0x3133a000` bytes
- Target representation: little-endian RIP-relative memory operands

The scan tested the exact virtual addresses of eleven engine-facing API signature/name strings:

- `xsGetUnitObjectId`
- `xsGetUnitCopyId`
- `xsGetObjectCopyId`
- `xsGetUnitClass`
- `xsGetObjectClass`
- `xsGetUnitType`
- `xsGetObjectType`
- `xsIsObjectValid`
- `xsIsObjectAvailable`
- `xsGetGarrisonedInUnitId`
- `xsGetGarrisonedUnitIds`

**Result:** `0` direct RIP-relative instruction references to the exact target addresses.

A second scan widened the target from individual strings to the surrounding native signature region (`0x1432af000` through `0x1432b1fff`).

**Result:** `0` direct RIP-relative instruction references into that region.

A third scan tested selected native UnitAI diagnostic strings:

- `CurrentAction`
- `currentTargetID=%d`
- `processNotify`
- `processIdle`
- `ai::search`
- `BESTUNITTOATTACK`

**Result:** `0` direct RIP-relative instruction references to those exact string addresses.

### 2.2 What this does establish

Within the tested executable `.text` representation and the tested RIP-relative addressing mode, the native strings are not being reached by ordinary direct code references that resolve to those exact addresses.

This is meaningful negative evidence because the scan covered the complete known `.text` interval rather than a small hand-selected neighborhood.

### 2.3 What this does not establish

The result does **not** prove that the strings are unused. It does not exclude:

- indirect pointer tables;
- pointer-to-pointer access;
- hash-based lookup;
- ordinal/index lookup;
- generated registration structures;
- address materialization through non-RIP mechanisms;
- runtime relocation or initialization code outside the tested pattern;
- code that reaches the strings through another data structure;
- representation artifacts caused by incomplete disassembly or non-code regions;
- use by another module/process.

The result therefore changes the representation hypothesis; it does not close the semantic question.

---

## 3. Stronger interpretation of the API signature region

The raw executable region around `0x1432af648` is not merely a sequence of isolated names. It contains repeated pairs of the form:

```text
API NAME\0 ... API SIGNATURE\0
```

Examples include:

```text
xsGetUnitObjectId
int xsGetUnitObjectId(int32_t unitId)

xsGetUnitCopyId
int xsGetUnitCopyId(int32_t unitId)

xsGetObjectCopyId
int xsGetObjectCopyId(int32_t playerId, int32_t objectId)

xsGetUnitClass
int xsGetUnitClass(int32_t unitId)

xsGetObjectClass
int xsGetObjectClass(int32_t playerId, int32_t objectId)
```

The spacing is variable rather than an immediately obvious fixed-size record stride.

### Interpretation

The strongest current hypothesis is that this region belongs to an API-description/registration representation rather than being a conventional collection of debug strings.

However, the exact structure is not yet known. In particular, there is currently no implementation evidence proving a tuple such as:

```text
{name pointer, signature pointer, native function pointer}
```

or any equivalent layout.

The correct next question is therefore **how the runtime consumes this metadata**, not whether more names can be found.

---

## 4. Consequence for native archaeology strategy

The previous strategy was:

```text
string -> instruction reference -> function -> implementation
```

The new evidence says that this path is not currently observable through direct RIP-relative references to the tested strings.

The investigation should therefore pivot to:

```text
metadata region
    ↓
possible registration/index structure
    ↓
initialization/loader consumer
    ↓
lookup/dispatch mechanism
    ↓
actual native implementation
```

The highest-value artifacts are now likely to be:

1. tables containing pointers or compact offsets associated with the metadata region;
2. initialization routines that enumerate or transform the region;
3. hash/index construction;
4. function-pointer arrays or registration records;
5. code that converts script/API identifiers into callable native handlers;
6. failure paths for unknown API identifiers.

Broad string scanning is now low-value and should not be repeated unless a new hypothesis requires it.

---

## 5. UnitAI control-loop model — deeper reconstruction

The previous pass identified four persistent state families plus derived search state. This pass sharpens their likely causal roles.

### 5.1 Order state

Native vocabulary distinguishes `currentOrder`, `currentOrderPriority`, and `OrderQueue` from `CurrentAction`.

The safest current interpretation is:

- **order:** persistent requested work / task context;
- **order priority:** relative precedence among requested work;
- **order queue:** pending work contexts;
- **action:** the current mechanical execution state needed to realize an order.

This separation is highly consequential. It means an AI framework should not equate "what the unit has been told to do" with "what the unit is currently doing."

### 5.2 Action state

Native vocabulary includes `CurrentAction` and an explicit diagnostic for actions that have failed, been invalidated, or require a search.

That vocabulary supports a control interpretation in which an action is not assumed to be permanently valid after selection. An action can become invalid and force recovery.

### 5.3 Target state

The native diagnostic vocabulary distinguishes at least:

- `currentTargetID`
- `currentTargetType`
- `currentTargetValue`
- `CurrentTarget`
- `CurrentTargetPosition`
- `DefendTarget`
- `DesiredTargetDistance`

This supports a model in which target state is richer than a single object identifier. Target identity, target classification, target value/priority, spatial target state, and role-specific target restrictions can all participate in execution.

### 5.4 Notification state

`NotifyQueueSize` and `processNotify` provide native vocabulary for an event/notification channel distinct from the order queue.

A useful abstraction is therefore:

```text
OrderQueue: "perform this work"
NotifyQueue: "something changed / happened"
```

This is an architectural interpretation, not yet a native contract. Exact enqueue/dequeue ordering remains open.

### 5.5 Search state

Native search diagnostics expose more than nearest-object selection. They include:

- line-of-sight state;
- search radius;
- object-interest filters;
- defend-target restrictions;
- candidate classification by GAIA / SELF / FRIEND / NEUTRAL / ENEMY;
- candidate validation;
- a final best-attacker style result (`BESTUNITTOATTACK`).

The most defensible conceptual decomposition is:

```text
search request
    ↓
candidate generation
    ↓
visibility / radius filtering
    ↓
object-interest filtering
    ↓
ownership / relationship classification
    ↓
validity checks
    ↓
policy/scoring selection
    ↓
target state update
```

The exact order of those stages is not yet proven.

---

## 6. New control-loop hypothesis

The combined evidence supports a stronger hypothesis than "UnitAI periodically evaluates rules."

### H5 — Native UnitAI is a persistent reactive controller with recovery

**Status:** strongly supported as an architectural hypothesis; implementation-level ordering remains unresolved.

**Evidence:**

- persistent action vocabulary;
- persistent order vocabulary;
- explicit target state vocabulary;
- notification queue vocabulary;
- order queue vocabulary;
- timers/state diagnostics;
- explicit action-invalid/search-required diagnostic;
- search diagnostics that include filtering, classification, and selection;
- native `processNotify`, `processIdle`, and search vocabulary.

**Predicted behavior:**

```text
intent/order
   ↓
current action
   ↓
execution
   ↓
world changes
   ↓
notification or invalidation
   ↓
state reconciliation
   ↓
search/repair when required
   ↓
new target/action
   ↓
continued execution
```

This predicts that native AI robustness is partly a **state-reconciliation problem**, not merely a decision-quality problem.

That distinction is important for ByzBot architecture: strategic planning can be excellent while execution still fails if the executor does not continuously reconcile intended work with actual machine state.

---

## 7. Predictive test derived from the model

A critical future runtime experiment should use a controlled target-loss event.

### Scenario

A unit is executing an attack against a valid target. The target becomes invalid or disappears from the unit's usable execution context.

### Required prediction trace

```text
PRECONDITION
    unit has active order
    unit has current action
    unit has target

TRIGGER
    target becomes invalid/unavailable

DISPATCH
    invalidation reaches UnitAI through the relevant native mechanism

PROCESSING
    current action/order/target state is inspected
    notification and/or action validation is processed

STATE TRANSITION
    current action is invalidated or otherwise changed

SEARCH / REPAIR
    a search may be entered if the action requires recovery

TARGET SELECTION
    candidates are generated, filtered, classified, validated, scored

ACTION
    a replacement action is selected or the order is abandoned/deferred

EXECUTION
    native execution resumes, changes state, or emits failure

POSTCONDITION
    either the original intent is restored through a new execution state,
    or the unit reaches a stable failed/idle/recovery state
```

The exact native sequence is currently unknown. This is intentionally a **prediction specification**, not a claimed trace.

The experiment becomes high-value once the native or runtime instrumentation can observe the transition.

---

## 8. Programmer-intent reconstruction

The architecture visible in the native vocabulary suggests several design pressures.

### Constraint A — world state changes independently of AI intent

Targets die, move, become inaccessible, ownership relationships change, and paths become invalid. A persistent order cannot safely be treated as equivalent to a persistent executable action.

### Constraint B — target selection is policy-driven

The presence of ownership classes, LOS, search radius, object-interest filters, validation, and a best-target result suggests that target selection is a constrained policy operation rather than a raw nearest-neighbor query.

### Constraint C — failure is expected

The explicit diagnostic for an action that has failed, been invalidated, or requires a search strongly suggests that invalid execution is part of the normal controller lifecycle rather than an exceptional impossible state.

### Supported design rationale

The resulting architecture is consistent with a game AI that separates **persistent intent** from **transient execution** and uses feedback/recovery to keep the two aligned.

This is a programmer-intent reconstruction, not a recovered design document. It remains below native-implementation certainty until the relevant state transitions and call paths are recovered.

---

## 9. Engineering consequence for ByzBot

No strategic module should directly own mechanical execution state.

The eventual bot should have at least these conceptual boundaries:

```text
STRATEGIC BRAIN
    objectives
    priorities
    plans
    resource policy
    military policy
    economic policy
          │
          ▼
TACTICAL ORDER LAYER
    unit/group intents
    target policies
    movement/formation requests
          │
          ▼
EXECUTION / RECONCILIATION LAYER
    validate capability
    observe current state
    issue commands
    detect failure
    repair/replan
          │
          ▼
MACHINE / SIMULATION
```

This is an architectural consequence, not permission to implement the framework before Layer 1 closes the relevant native boundaries.

The key principle is:

> **Planning expresses intent; execution continuously proves whether that intent remains mechanically realizable.**

---

## 10. Evidence ledger for this pass

| Claim | Evidence | Level | Status |
|---|---|---|---|
| `.text` contains no direct RIP-relative references to the eleven tested API string addresses | Complete Capstone `.text` scan | NATIVE-IMPLEMENTATION / negative | Established for tested addressing mode |
| `.text` contains no direct RIP-relative references into the widened API signature region | Complete Capstone `.text` scan | NATIVE-IMPLEMENTATION / negative | Established for tested addressing mode |
| Selected UnitAI diagnostic strings likewise have no direct RIP-relative references in tested `.text` | Complete Capstone `.text` scan | NATIVE-IMPLEMENTATION / negative | Established for tested addressing mode |
| API names occur with adjacent signature strings | Raw executable observation | NATIVE-VOCABULARY | Established |
| API region is a registration/metadata table | Structure and repetition | INFERENCE | Unverified |
| `currentOrder` and `CurrentAction` represent distinct state concepts | Distinct native vocabulary | INFERENCE | Strong hypothesis |
| `NotifyQueue` is a separate event channel | `NotifyQueueSize` + `processNotify` | INFERENCE | Strong hypothesis |
| search is a multi-stage constrained selection process | Native search diagnostics | INFERENCE | Strong hypothesis |
| UnitAI is a persistent reactive controller with recovery | Combined native vocabulary | INFERENCE | Strong architectural hypothesis |
| replay object references equal native object IDs | None | HYPOTHESIS | Explicitly unproven |

---

## 11. Revised unknowns

The highest-value unknowns have shifted.

1. What data structure consumes the API name/signature region?
2. Is API dispatch keyed by pointer, offset, hash, ordinal, or generated index?
3. Where is the registration structure initialized?
4. Where does an API identifier become a callable native handler?
5. Where are unknown/unavailable API identifiers rejected?
6. Which native structure owns `CurrentAction`?
7. Which native structure owns `currentTargetID/type/value/position`?
8. Who writes `OrderQueue` and `NotifyQueue`?
9. What event causes action invalidation?
10. Does search mutate target state directly or return a candidate to another layer?
11. What is the exact order of notification, order, search, and action processing?
12. What state persists across update ticks?
13. Which state is derived and recomputed?
14. What native mechanism bridges UnitAI and simulation object identity?

These questions now have higher leverage than further string collection.

---

## 12. Next discriminating investigation

The next native pass should attack the **metadata-consumer problem** and the **state-owner problem** in parallel, but with narrowly bounded experiments.

### Track A — metadata consumer

Search for structures containing multiple nearby addresses/offsets corresponding to the signature region and inspect initialization code around candidate tables. Test 32-bit relative offsets, 64-bit pointers, and compact index patterns before broad disassembly.

### Track B — UnitAI state owner

Use the strongest native diagnostic clusters to identify candidate functions through local instruction/data structure recovery, then trace writes to the fields represented by the diagnostics. The objective is not to name a function prematurely; it is to recover one real state mutation chain.

### Promotion criterion

The next major promotion should be a complete, evidence-backed chain of the form:

```text
native entry / update
    ↓
state read
    ↓
condition
    ↓
state write
    ↓
subsequent consumer
```

Once one such chain is recovered, use it as the anchor for expanding outward rather than attempting another whole-executable semantic sweep.

---

## 13. Layer 1 status after this pass

This pass increases confidence in the **architecture of the control-loop model**, but it does not close the critical native implementation gaps.

The most important advance is methodological: the API signature region and UnitAI diagnostic strings should no longer be treated as if ordinary direct string xrefs are the expected bridge to implementation. The executable is forcing a representation-aware investigation.

Layer 1 therefore remains active. No strategic implementation should be promoted on the basis of the hypotheses above alone.
