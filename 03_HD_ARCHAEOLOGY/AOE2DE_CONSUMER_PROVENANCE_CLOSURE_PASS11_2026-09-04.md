# AoE2DE Consumer / Provenance Closure — Pass 11

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Predecessor:** `AOE2DE_EXACT_ANCHOR_HISTORICAL_TRACE_PACK_PASS10_2026-09-04.md`  
**Purpose:** close the downstream edges identified by Pass 10: state writer → readers → first strategic consumer → action/postcondition.  
**Status:** FORENSIC CLOSURE / ACCEPT WITH CORRECTIONS  

> **Source boundary:** this pass uses the pristine `Promisory.zip` available in the project workspace for Promisory-module closure and the verified `AI (HD version).per` archive for the HD attack/retreat slice. The earlier ADPromisory reconstruction is used only where explicitly identified. No reconstruction is silently promoted to pristine historical source.

---

# 0. Executive result

Pass 11 materially changes the archaeology.

The most important closure is the one Pass 10 left open:

`cavarchers`
→ downstream research / production conditions
→ `traincamel`
→ actual camel production

This establishes a real historical chain from enemy composition measurement to a concrete counter-production response. The earlier Pass-10 caution was correct at the time, but the pristine Promisory source now closes the missing edge.

A second major closure resolves the apparent ambiguity around goals **504/505**. The search does not merely preserve an abstract “best” candidate. It preserves the indices of the **farthest villager pair**, then uses those indices to compute a midpoint, moves that midpoint nine tiles toward the map center, and finally issues `action-move`. The code therefore demonstrates a very specific spatial objective: selecting a distant villager pair to derive a central movement point for the land-nomad routine.

A third closure strengthens the scout lab: the path-analysis state is consumed by a reinforcing-group decision and later by movement toward either a scout-group point or a calculated pivot point. The geometry is therefore not isolated mathematics; it participates in actual movement control.

The attack/retreat chain is also materially strengthened because the pristine HD source is now available: retreat state is eventually consumed by an actual `up-retreat-now` action under timer/condition gates, after which retreat state is cleared and attack state is set appropriately.

Finally, the Promisory source contains an explicit escrow release rule that clears escrow flags and `escrowing`, while age-research and production actions remain separate consumers of those flags.

**Overall disposition:** Pass 11 is a substantial closure pass and should be retained as the new downstream-provenance baseline. It does not close every lifecycle, but it closes the highest-value missing causal edges.

---

# 1. Method

For each state channel:

`WRITER → ALL LOCATABLE READERS → FIRST CONCRETE CONSUMER → ACTION → POSTCONDITION`

Classify every edge as:

- **DIRECT:** executable source establishes the edge;
- **COMPOSED:** multiple direct edges establish the larger chain;
- **INFERRED:** strategic interpretation;
- **AEGIS-GENERALIZATION:** new architecture;
- **UNCERTAIN:** unresolved.

Also record whether a state is:

`OBSERVATION | CLASSIFICATION | BELIEF | REQUIREMENT | COMMITMENT | CONTROL/PERMISSION | ACTION-STATE | SCRATCH | UNKNOWN`.

---

# 2. Closure A — `cavarchers` → counter response

## 2.1 Writer

**Module:** `threats.per`  
**Anchor:** approximately lines 618–655 in pristine Promisory source.

The threat subsystem measures enemy unit families with `up-get-focus-fact unit-type-count` and accumulates them into `cavarchers` using `up-modify-sn cavarchers g:+ temporary-goal`.

The measurement families include cavalry-archer-line, war-wagon-line, mangudai-line, elephant archer variants, and camel archer.

**Evidence:** DIRECT.

## 2.2 Initialization

**Module:** `init.per`  

The source explicitly initializes:

`set-strategic-number cavarchers 0`

alongside other military threat aggregates.

**Evidence:** DIRECT.

This establishes that `cavarchers` is not merely a transient local expression. It is an explicit strategic-number state channel with lifecycle initialization.

## 2.3 Downstream readers

The pristine source contains multiple concrete readers.

### Research response

**Module:** `researches.per`

A heavy-camel research rule fires when, among other conditions:

`strategic-number cavarchers >= 10`

with appropriate camel-set/traincamel conditions and live research feasibility.

The same threshold appears in the Imperial-camel research branch.

**Evidence:** DIRECT.

### Production response

**Module:** `units.per`

The production rules repeatedly test `cavarchers` alongside direct enemy-unit counts.

Representative Castle/early response:

`cavarchers >= 4` → `set-goal traincamel yes`

and later thresholds:

`5, 7, 10, 15, 25, 40`.

These thresholds are combined with own military state, enemy-specific counts, food buffer, and `camel-set` limits.

**Evidence:** DIRECT.

## 2.4 Concrete production consumer

The `traincamel` state is initialized to `no` and later written `yes` by response rules.

A concrete production path appears around the late `units.per` production machinery:

```text
(defrule
    (goal traincamel yes)
    (goal temporary-goal 1579175)
(or  (up-can-train 0 c: camel-line)
     (up-can-train 0 c: imperial-camel))
=>
    (up-full-reset-search)
    (up-find-local c: stable c: 240)
    (up-remove-objects search-local object-data-progress-value >= 1)
    (up-remove-objects search-local object-data-under-attack >= 1)
    (up-clean-search search-local object-data-distance search-order-asc)
    (up-remove-objects search-local object-data-index >= 1)
    (up-get-search-state local-total)
    (up-target-point 0 action-train c: camel-line)
    (up-target-point 0 action-train c: imperial-camel)
    (set-goal temporary-goal3 1579200))
```

followed by a production action guarded by pending search state, siege requirement, and `can-train`:

```text
(defrule
    (goal traincamel yes)
(nand (goal temporary-goal3 1579200)
      (up-compare-goal local-total >= 1))
    (goal siegereq yes)
(or  (can-train camel-line)
     (can-train imperial-camel))
=>
    (train camel-line)
    (train imperial-camel))
```

**Evidence:** DIRECT for production state → production search → train action.

## 2.5 Closed causal chain

`enemy unit-family measurement`
→ `cavarchers aggregate`
→ `threshold comparison`
→ `traincamel yes`
→ `stable search / production candidate`
→ `can-train`
→ `train camel-line / imperial-camel`.

This is the first Pass-11 closure that converts the threat lab from “measurement only” into a demonstrated **measurement → response authorization/state → production action** chain.

## 2.6 Strategic interpretation

**COMPOSED:** the programmer uses observed enemy composition to increase the probability/eligibility of camel production and camel-related research.

This is not a universal one-to-one counter table. The response is thresholded, contextual, and interleaved with own military state, food buffers, unit-set limits, civ conditions, and technology state.

That complexity is strategically significant.

The historical design is closer to:

`enemy capability signal → response pressure → constrained counter-capability investment`

than:

`enemy unit → hard-coded counter`.

---

# 3. Closure B — Search goals 504/505 → actual land-nomad action

## 3.1 Exact search writer

**Module:** `general.per`  
**Anchor:** approximately lines 17–90 in pristine Promisory source.

The search initializes:

`temporary-goal2 = -1`

then measures pairwise distance between candidate villagers.

When:

`temporary-goal > temporary-goal2`

it writes:

`504 = temporary-goal4`

`505 = temporary-goal5 - 1`.

Therefore the literal comparator is **maximum distance**, not minimum distance.

**Evidence:** DIRECT.

## 3.2 Consumer closure

The next rule resets search, finds local villagers, retrieves object points using goals 504 and 505, and calculates:

`lerp 50%` between the two points.

It then moves that point:

`up-lerp-tiles ... c: -9`

and finally:

`up-set-target-point point-x`

`up-target-point 0 action-move -1 -1`.

**Evidence:** DIRECT.

## 3.3 Correct interpretation

The earlier phrase “best candidate” was underspecified.

The exact historical algorithm is:

`enumerate villager pairs`
→ `measure pair distance`
→ `retain farthest pair`
→ `retrieve their positions`
→ `take midpoint`
→ `shift midpoint 9 tiles toward center`
→ `move to resulting point`.

This is not merely “best location optimization.”

It is a specific geometric heuristic for the land-nomad problem.

## 3.4 Strategic meaning

**DIRECT:** the selected pair determines a movement target.

**INFERRED:** the programmer is trying to derive a robust central relocation point from dispersed villagers.

**AEGIS-GENERALIZATION:** candidate evaluation should retain the actual objective function rather than labeling every comparison “best.”

This is a major methodological correction.

---

# 4. Closure C — Scout path analysis → movement control

## 4.1 Group formation

`scoutcontrol.per` creates a group of up to 12 scouts after search/filtering and resets its group/path state.

**Evidence:** DIRECT.

## 4.2 Safety analysis

The path routine interpolates from self toward enemy position in 20-tile increments, filters within 9 tiles, searches for enemy archers, spearmen, town centers, and castles, and aggregates danger indicators.

**Evidence:** DIRECT.

## 4.3 Decision consumer

When `multi-group-reinforcing` is enabled, the source computes two rotated candidate points around the detected obstacle and chooses the closer one:

`temporary-goal4 >= temporary-goal5`
→ `pivot-point-x = point-x`

otherwise:

`pivot-point-x = point2-x`.

The subsequent movement rules consume `scout-group-x` or `pivot-point-x` and issue:

`up-target-point ... action-move`.

**Evidence:** DIRECT.

## 4.4 Closed chain

`scout group`
→ `path interpolation`
→ `danger-object search`
→ `reinforcing-group state`
→ `two geometric candidates`
→ `closer pivot`
→ `action-move`.

The route-safety mechanism therefore participates in actual movement control.

## 4.5 Strategic interpretation

**DIRECT:** path safety affects route/movement state.

**INFERRED:** the programmer is attempting to preserve scout-group movement while avoiding dangerous local military geometry.

**NOT PROVEN:** information-value optimization.

---

# 5. Closure D — Attack / retreat / restart

## 5.1 Exact HD source recovered

The verified HD source is now available from `AI (HD version).per`.

Key constants:

`retreat-now-goal = 20`

`attack-status-goal = 24`

`restart-attack-goal = 27`.

The source comments explicitly state their intended roles.

## 5.2 Retreat trigger

Representative historical rule:

`enemy castle arrows present`
+ insufficient siege
+ military level threshold
+ population threshold
→

`retreat-now-goal = 1`

`attack-status-goal = retreat`

`attack-goal = 0`

`attack-timer = 60`

`reset = 1`.

**Evidence:** DIRECT.

Equivalent rules exist for towers and TC fire, with different timers and contextual conditions.

## 5.3 Physical retreat closure

Later HD rules contain:

`goal retreat-now-goal 1`
+ `timer-triggered retreat-timer`
→

`up-retreat-now`

followed by state cleanup:

`retreat-now-goal = 0`

`attack-status-goal = retreat`.

**Evidence:** DIRECT.

This closes the previously missing distinction:

`retreat controller request`
→ `timer/eligibility`
→ `actual UP retreat command`.

It still does not prove the units physically reached a safe destination; that requires world-state observation.

## 5.4 Restart closure

When TSA reduces town-size state to place a building, the source writes:

`restart-attack-goal = 1`.

A later rule consumes it and resets attack-group state under the specified conditions, then clears the restart goal.

Another rule clears the restart goal when ally-proximity evaluation does not require the restart state.

**Evidence:** DIRECT for restart state lifecycle.

## 5.5 Strategic meaning

**DIRECT:** attack execution is governed by persistent state, timers, threat conditions, and explicit restart state.

**INFERRED:** the programmer is trying to suspend/relaunch offensive pressure without treating each attack as a one-shot action.

This is strong evidence for a temporal controller.

---

# 6. Closure E — Escrow lifecycle

## 6.1 Allocation

The source builds escrow flags through contextual conditions and research-cost additions.

Examples include:

`up-add-research-cost castle-age`
→ `up-modify-flag escrow-flag c:+ 1`

and Imperial equivalents.

**Evidence:** DIRECT.

## 6.2 Consumption

`escrow-flag == 1`
→ Castle research.

`escrow-flag == 2`
→ Imperial research.

`escrow-flag2` values similarly gate production/research operations.

**Evidence:** DIRECT.

## 6.3 Release

The source contains an explicit release rule:

`true`
→

`escrow-flag = 0`

`escrow-flag2 = 0`

`escrow-flag3 = 0`

`escrowing = no`.

**Evidence:** DIRECT.

## 6.4 Critical lifecycle limitation

The release rule is unconditional in its immediate guard.

Therefore we must **not** automatically interpret it as “release after successful conversion.” It is a global release/reset event whose precise scheduler interaction and timing relative to all escrow consumers require further execution-level tracing.

This is an excellent example of why “release” and “successful completion” must remain separate concepts.

---

# 7. Closure F — Production is more distributed than Pass 10 showed

The pristine `units.per` source materially improves Lab 3.

Production control has at least these layers:

`strategic response condition`
→ `train<unit> goal`
→ `availability / feasibility`
→ `production-building search`
→ `pending/progress filtering`
→ `action-train`
→ `train`.

This means “production authorization” is an insufficient historical description by itself.

A more accurate historical model is:

`DESIRE/RESPONSE STATE → FEASIBILITY → PRODUCTION-CANDIDATE SEARCH → ACTION`

The AEGIS authority plane remains a design improvement, not a recovered historical subsystem.

---

# 8. State-channel ownership findings

## `cavarchers`

- initializer: `init.per`
- writers: `threats.per`
- readers: `researches.per`, `units.per`, other threat-composition logic
- reset: initialization / later threat-cycle behavior requires full lifecycle audit
- type: **STRATEGIC AGGREGATE**
- evidence: DIRECT

## goals 504/505

- writer: `general.per` search routine
- readers: immediately by the land-nomad placement routine
- reset: overwritten on later searches; lifecycle is routine-scoped rather than globally unique
- type: **SEARCH RESULT STATE**
- evidence: DIRECT

## `retreat-now-goal`

- writers: multiple HD tactical/strategic rules
- readers: retreat execution rules
- resetters: retreat execution / timers / reset conditions
- type: **ACTION-STATE / CONTROL STATE**
- evidence: DIRECT

## `restart-attack-goal`

- writer: TSA/building transition
- readers: attack-group reset/restart rules
- resetters: restart consumers
- type: **TRANSITION CONTROL STATE**
- evidence: DIRECT

## `temporary-goal10`

Still not globally classified as scratch because the historical Promisory package reuses the same channel in unrelated subsystems.

**Finding:** the identifier name “temporary” is not enough to establish semantic ownership or lifetime.

---

# 9. New strategic deductions

## 9.1 Threat response is thresholded capability pressure

The source does not simply classify an enemy and instantly choose a counter.

Instead:

`measured enemy composition`
→ `aggregate pressure`
→ thresholds
→ `own-state constraints`
→ response-state activation
→ feasibility
→ production/research.

That is closer to a **distributed pressure controller** than a lookup table.

**Evidence grade:** COMPOSED.

## 9.2 Candidate evaluation is objective-specific

The search routine proves an important general rule:

> **“Best” has no meaning without an explicit objective function.**

Here the objective is maximum pairwise distance, followed by geometric transformation.

A future AEGIS candidate evaluator must therefore store:

`objective | metric | direction | tie-break | constraints | consumer`.

**Evidence:** historical mechanism DIRECT; AEGIS rule AEGIS-GENERALIZATION.

## 9.3 Geometry is not cosmetic

Scout and land-nomad code both demonstrate that geometry is part of strategic/operational decision-making:

- midpoint;
- lerp;
- distance;
- rotation;
- pivot selection;
- target-point movement.

This should be treated as a first-class AEGIS service rather than embedded ad hoc in individual rules.

## 9.4 Recovery is temporal, not merely alternate code

Building fallback, attack restart, retreat timers, search resets, and escrow release all show the same deeper engineering pattern:

`state enters a constrained condition`
→ `temporary control regime`
→ `action or alternative`
→ `state cleared/replaced`
→ `normal control resumes`.

This is strong composed evidence for the historical programmer's use of **stateful recovery**.

---

# 10. Remaining unresolved edges

### U1 — `cavarchers` complete lifecycle

We have initialization, writers, and multiple readers. We have not yet exhaustively mapped every reset/recompute boundary across all threat cycles.

### U2 — `traincamel` final production postcondition

We have the train action. We still need world-state confirmation such as unit-count/pending/progress transition after issuance.

### U3 — 504/505 search performance

The exact algorithm is known, but actual engine cost per candidate iteration remains unmeasured.

### U4 — Scout danger-state lifetime

The exact path scan and movement consumer are closed, but full reset/replacement semantics for every danger accumulator remain open.

### U5 — Attack restart physical outcome

Controller restart is closed; actual renewed attack movement/engagement remains a downstream TSA/attack-group trace.

### U6 — Escrow release scheduler relationship

The reset action is exact; the exact temporal relationship between allocation, consumption, research completion, and unconditional release remains unresolved.

---

# 11. Evidence coverage after Pass 11

| Lab | Writer | Reader | Concrete consumer | Action | World-state postcondition | Status |
|---|---|---|---|---|---|---|
| Escrow | YES | YES | YES | YES | PARTIAL | OPEN |
| Gatherers | YES | YES | YES | YES | PARTIAL | OPEN |
| Production | YES | YES | YES | YES | PARTIAL | OPEN |
| Threat | YES | YES | YES | YES | PARTIAL | **MAJOR CLOSURE** |
| Search | YES | YES | YES | YES | PARTIAL | **MAJOR CLOSURE** |
| Scout | YES | YES | YES | YES | PARTIAL | **MAJOR CLOSURE** |
| Attack/retreat | YES | YES | YES | YES | PARTIAL | **MAJOR CLOSURE** |
| Building fallback | YES | YES | YES | YES | PARTIAL | STRONG |

The remaining “PARTIAL” world-state column is intentional. A `.per` action invocation is not equivalent to observing the resulting game state.

---

# 12. Historical programmer model after Pass 11

The strongest evidence-backed reconstruction is now:

```text
GAME STATE
   ↓
OBSERVATION / MEASUREMENT
   ↓
COMPACT STATE CHANNEL
   ↓
THRESHOLD / CONTEXT / FEASIBILITY
   ↓
RESPONSE STATE
   ↓
SEARCH / SELECT / CONFIGURE
   ↓
ACTION
   ↓
TIMER / PENDING / STATE RESET
   ↓
NEXT CONTROL CYCLE
```

This is more defensible than saying the historical AI contains a clean modern planner.

It does not.

It contains a large distributed rule system that repeatedly implements **controller-like state transitions** using primitive engine operations.

That distinction should remain central to AEGIS architecture.

---

# 13. What AEGIS should inherit

### Inherit directly as engineering lessons

- intermediate state as a first-class implementation tool;
- explicit initialization;
- thresholded response;
- contextual feasibility;
- candidate search;
- objective-specific comparison;
- geometry primitives;
- temporal attack/retreat state;
- fallback/recovery;
- state reset;
- production-building selection;
- separation of strategic signals from immediate actions.

### Improve

- typed state ontology;
- explicit ownership;
- explicit belief/confidence;
- commitment lifecycle;
- authority separate from intent;
- world-state verification;
- measurable objective functions;
- failure taxonomy;
- invalidation;
- performance budgets;
- transition ownership.

### Reject

- calling every numeric comparison “optimization”;
- calling every control flag “authority”;
- calling every measurement “belief”;
- calling every action a successful outcome;
- assuming a variable named `temporary` is globally scratch;
- assuming a reset means successful completion;
- assuming a counter threshold is a complete strategic model.

---

# 14. Pass-11 conclusion

Pass 10 established literal source.

Pass 11 establishes downstream consequence.

That is a major methodological step.

We can now demonstrate several complete historical causal chains rather than merely isolated mechanisms:

### Threat → counter capability

`enemy composition → cavarchers → traincamel → stable selection → camel production`

### Search → spatial decision

`villager pair search → maximum distance → 504/505 → midpoint → central shift → move`

### Scout safety → route movement

`enemy-object search → danger state → reinforcing mode → pivot geometry → movement`

### Threatened attack → physical retreat

`fortification/TC/tower condition → retreat state → timer → up-retreat-now → retreat-state reset`

### Building transition → attack restart

`TSA building state → restart-attack-goal → attack-group reset/restart control`

These chains substantially improve our understanding of the programmer's mind.

The programmer was not merely encoding “build X” or “make Y.” They were repeatedly constructing **small state machines that transform measured game relationships into controlled actions under engine constraints**.

That is now a source-backed conclusion rather than a purely architectural hypothesis.

---

# 15. Next pass

**Pass 12 — Cross-System Control Graph / Strategic Causal Network.**

Now that the highest-value consumer edges are closing, the next step should not be another isolated lab.

Build the cross-system graph:

`ECONOMY → THREAT → PRODUCTION → TECHNOLOGY → MILITARY → MAP/POSITION → ATTACK → RECOVERY → ECONOMY`

For every edge record:

`source state | writer | reader | guard | side effect | timing | resource consequence | capability consequence | opponent consequence | reset | evidence grade`.

The goal is to recover the **distributed strategic controller as a network**, while preserving the fact that the historical implementation is not a clean centralized planner.
