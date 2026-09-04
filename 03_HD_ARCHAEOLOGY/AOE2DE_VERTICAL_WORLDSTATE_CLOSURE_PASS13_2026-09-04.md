# AoE2DE Vertical World-State Closure — Pass 13

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Predecessor:** `AOE2DE_CROSS_SYSTEM_CONTROL_GRAPH_PASS12_2026-09-04.md`  
**Status:** VERTICAL CLOSURE / EVIDENCE-GRADED WORKING CANON  
**Primary historical source:** verified `AI (HD version).per` + verified Promisory modules  
**Runtime authority:** Layer 1 current-build machine evidence  

---

# 0. Mission

Pass 12 established the cross-system graph but correctly left most chains open at the world-state boundary. Pass 13 therefore changes the unit of investigation again.

The question is no longer merely:

`Does state A reach command B?`

It is:

`What exactly must change in the game for command B to have realized the capability the programmer was trying to obtain?`

The pass traces four vertical pathways:

1. **resource reservation → research conversion**;
2. **enemy threat aggregate → camel production capability**;
3. **attack threat → retreat → renewed attack control**;
4. **land-nomad geometry → villager relocation objective**.

The critical distinction remains:

`CONTROL ≠ WORLD ≠ STRATEGIC`.

Where the historical source cannot prove the world transition, the gap is preserved rather than filled by game knowledge.

---

# 1. Closure contract

A vertical chain is recorded as:

`OBSERVATION → STATE WRITE → READER → GUARD → CONTROL EFFECT → COMMAND → REQUIRED WORLD POSTCONDITION → STRATEGIC POSTCONDITION → RESET / REASSESSMENT`.

Three closure levels are mandatory.

- **CONTROL CLOSED:** executable source reaches the relevant action or control mutation.
- **WORLD CLOSED:** the source itself proves the resulting game-state transition, or an independent runtime observation records it.
- **STRATEGIC CLOSED:** evidence demonstrates that the realized state changed the intended game relationship/capability.

A command is never treated as its own postcondition.

---

# 2. Trace V1 — resource reservation → research conversion

## 2.1 Direct source pattern

The verified AI source contains the following economic-to-technology pattern:

```text
(strategic-number sn-resource-control <= 2)
(population > sixty-percent-pop)
(unit-type-count ... >= high-min-number-upgrade)
(not (can-research-with-escrow ri-blast-furnace))
(research-available ri-blast-furnace)
=>
(set-escrow-percentage food 20)
(set-escrow-percentage gold 20)
(set-goal escrow-purpose-goal blacksmith)
```

A later rule consumes the protected state:

```text
(can-research-with-escrow ri-blast-furnace)
=>
(release-escrow food)
(release-escrow gold)
(set-escrow-percentage food 0)
(set-escrow-percentage gold 0)
(research ri-blast-furnace)
(set-goal escrow-purpose-goal 0)
```

The same structural pattern is present for other technologies, including Chemistry and Iron Casting.

**Evidence:** DIRECT for the control sequence in the recovered source package. The exact source package/version must remain attached to the repository provenance ledger when this artifact is promoted to canonical status.

## 2.2 Vertical interpretation

The first rule does not merely say “research Blast Furnace.” It changes the resource-control regime before the research action is authorized.

The direct chain is:

`research available`
→ `context qualifies`
→ `food/gold allocation protected`
→ `research becomes escrow-feasible`
→ `escrow released`
→ `research command issued`
→ `escrow-purpose state cleared`.

This is a **transaction-shaped control sequence**.

It is not yet proof that the technology finishes.

## 2.3 World postcondition

Required world postcondition:

`Blast Furnace research is actually completed and the player's technology state reflects completion.`

The source excerpt proves neither completion timing nor successful completion.

Therefore:

`CONTROL = YES`

`WORLD = OPEN`

`STRATEGIC = OPEN`

## 2.4 Strategic postcondition

The intended strategic capability would be:

`relevant military units receive the technology's capability before the timing window closes`.

This is an AEGIS-level postcondition unless independently observed in runtime/game state.

## 2.5 Important discovery

The programmer separates at least three states that are easy to collapse conceptually:

1. technology is **available**;
2. technology is **feasible through the protected resource regime**;
3. technology is **requested**.

Completion is a fourth state that the `.per` control trace does not automatically establish.

This distinction is highly valuable for AEGIS.

---

# 3. Trace V2 — threat aggregate → camel capability

## 3.1 Threat signal

Promisory `threats.per` measures enemy unit families and writes strategic state including `cavarchers`.

The aggregate is not always a raw count. The source contains branches where particular ranged cavalry/elephant-archer contributions are transformed before being added to the aggregate.

Therefore the correct abstraction is:

`enemy composition → weighted threat aggregate`.

**Evidence:** DIRECT for the arithmetic and state write; COMPOSED for the strategic interpretation.

## 3.2 Response activation

Promisory `units.per` contains multiple `traincamel yes` writers. These combine conditions such as:

- own cavalry state;
- enemy Genitour state;
- `cavarchers` threshold;
- food buffer;
- camel-set ceiling;
- contextual production state.

This is important because the threat signal is not an unconditional “make camels” command.

The signal enters a larger eligibility predicate.

## 3.3 Production realization path

The exact representative execution path is:

```text
(goal traincamel yes)
(goal temporary-goal 1579175)
(can-train camel-line OR imperial-camel)
        ↓
(up-full-reset-search)
(up-find-local stable ...)
(up-remove-objects ... progress)
(up-remove-objects ... under-attack)
(up-clean-search ... distance)
(up-remove-objects ... index)
(up-get-search-state local-total)
(up-target-point 0 action-train camel-line)
(up-target-point 0 action-train imperial-camel)
(set-goal temporary-goal3 1579200)
```

A subsequent rule checks the production state and executes:

```text
(goal traincamel yes)
...
(goal siegereq yes)
(can-train camel-line OR imperial-camel)
=>
(train camel-line)
(train imperial-camel)
```

The exact source establishes a distributed chain:

`threat signal`
→ `traincamel goal`
→ `production-building search`
→ `feasibility`
→ `train action`.

## 3.4 World postcondition

Required world postcondition:

`camel-line production has actually created the intended unit stock / production queue state.`

The source shown proves the command path, not the completed unit appearance.

Therefore:

`CONTROL = YES`

`WORLD = OPEN`

`STRATEGIC = OPEN`.

## 3.5 Capability postcondition

The strategic capability is not “camel command issued.” It is:

`available camel force sufficient to alter the relevant enemy capability relationship`.

That requires at minimum:

`production → completion → surviving stock → ability to engage the threat`.

Only the first stage is presently source-closed.

## 3.6 Programmer insight

The programmer's practical unit of reasoning appears closer to **capability availability** than to raw commands:

`detect pressure → activate response → find an executable production site → verify feasibility → issue production`.

But the source does not prove that the programmer explicitly used the word “capability” or a modern capability model.

**Evidence grade:** COMPOSED / INFERRED.

---

# 4. Trace V3 — attack threat → retreat → recovery

## 4.1 Threat recognition

The HD source contains multiple conditions involving enemy castles, towers, town centers, monks, siege/military sufficiency, and attack state.

Those conditions write:

- `retreat-now-goal = 1`;
- `attack-status-goal = retreat`;
- `attack-goal = 0`;
- attack timer state;
- reset state.

This is direct evidence that threat assessment can change the attack controller state.

## 4.2 Physical command

The retreat controller later consumes the retreat state and invokes:

`up-retreat-now`.

The controller then clears or changes retreat state and adjusts attack-group state/timing.

This closes the **control** path:

`threat condition → retreat state → retreat command → controller reset`.

## 4.3 World postcondition

The required world postcondition is:

`the affected military units physically reposition away from the threatened engagement according to the retreat command semantics`.

The `.per` source alone does not prove the physical movement completed.

Therefore:

`CONTROL = YES`

`WORLD = OPEN`

`STRATEGIC = OPEN`.

## 4.4 Recovery / restart

The HD source also contains:

```text
(goal increase-town-size-goal 2)
(strategic-number sn-maximum-town-size >= 40)
=>
(disable-timer increase-town-size-timer)
(set-strategic-number sn-maximum-town-size 18)
(set-goal increase-town-size-goal 0)
(enable-timer attack-timer 1)
(set-goal restart-attack-goal 1)
```

The restart state is later consumed by rules that can reset attack groups:

```text
(goal restart-attack-goal 1)
(strategic-number sn-target-evaluation-ally-proximity < 1)
(strategic-number sn-number-attack-groups > 0)
(strategic-number sn-minimum-attack-group-size > 1)
(strategic-number sn-maximum-town-size < 40)
=>
(up-reset-unit c: -1)
(set-strategic-number sn-number-attack-groups 0)
(set-strategic-number sn-minimum-attack-group-size 1)
(set-goal restart-attack-goal 0)
```

This proves **restart-controller preparation**.

It does not prove that a renewed attack group later forms, reaches a target, and creates strategic pressure.

## 4.5 Vertical closure status

`retreat trigger` → `retreat state` = CONTROL CLOSED.

`retreat state` → `up-retreat-now` = CONTROL CLOSED.

`up-retreat-now` → physical reposition = WORLD OPEN.

`restart state` → attack-group reset = CONTROL CLOSED.

`reset` → renewed attack = WORLD OPEN.

`renewed attack` → successful pressure = STRATEGIC OPEN.

This is the strongest current example of why closure must be multidimensional.

---

# 5. Trace V4 — land-nomad geometry → relocation

## 5.1 Search algorithm

The `general.per` routine initializes a candidate-distance sentinel at `-1`, enumerates candidate pairs, calculates pair distance, and replaces the stored candidate when:

`new distance > stored distance`.

Therefore the local objective is:

`argmax pair distance`.

The selected pair is stored through goals `504` and `505`.

## 5.2 Consumer

The consumer retrieves the selected objects, obtains their points, computes a midpoint through interpolation, shifts the midpoint centerward by 9 tiles, and issues a movement action.

The local geometric chain is therefore:

`candidate pairs`
→ `maximum separation`
→ `504/505`
→ `two points`
→ `midpoint`
→ `9-tile centerward shift`
→ `move`.

**Evidence:** DIRECT for the algorithm and action chain.

## 5.3 World postcondition

Required world postcondition:

`the selected villager set actually relocates toward the constructed target point.`

The source establishes the action request, not physical movement completion.

Therefore:

`CONTROL = YES`

`WORLD = OPEN`.

## 5.4 Strategic postcondition

Possible interpretations include:

- centralizing villagers;
- improving working-position robustness;
- correcting an overly dispersed land-nomad settlement;
- establishing a better economic center.

The exact strategic purpose is **not yet proven**.

Do not promote any of these to historical doctrine until the consumer is traced upward into the complete land-nomad routine and its surrounding state transitions.

## 5.5 Indexing issue

The `505 = temporary-goal5 - 1` relationship remains an unresolved semantic detail unless the complete increment / object-index sequence is traced.

Do not state that it is definitively one-based-to-zero-based conversion yet.

---

# 6. Resource propagation model

Pass 13 produces a more precise historical resource model.

The source supports the following chain:

```text
RESOURCE STOCK
     ↓
RESOURCE CONTROL REGIME
     ↓
RESERVATION / ESCROW
     ↓
FEASIBILITY
     ↓
SIDE-EFFECT COMMAND
     ↓
RESOURCE RELEASE / STATE RESET
```

This is stronger than the earlier phrase “resources are an opportunity-cost model.”

The exact source proves **resource protection and release behavior**. Opportunity cost remains a strategic interpretation of why competing demands exist.

The distinction is:

- `resource protection` = DIRECT;
- `competing resource claims` = COMPOSED;
- `formal opportunity-cost optimization` = NOT PROVEN.

---

# 7. Capability realization model

A capability must be represented as a chain, not a boolean command.

For production:

`intent → eligibility → production site → feasibility → queue/command → completion → stock → usable capability`.

For technology:

`intent → reservation → feasibility → research command → completion → available technology → usable capability`.

For military movement:

`intent → target/route → movement command → physical reposition → engagement state`.

The historical source often closes only the left side of these chains.

AEGIS should make the entire chain explicit.

---

# 8. New strategic distinction — conversion vs realization

Pass 13 establishes a distinction that should become canonical:

## Conversion

A controller commits resources or issues an action intended to buy a capability.

Examples:

- research command;
- train command;
- retreat command;
- movement command.

## Realization

The game state actually changes so the purchased/attempted capability exists.

Examples:

- technology completed;
- unit exists in stock;
- army physically repositioned;
- villagers occupy the intended location.

## Strategic realization

The realized capability changes the game relationship in the intended direction.

Examples:

- upgraded army wins an engagement it otherwise could not;
- camel force changes the cavalry/ranged-cavalry relationship;
- retreat preserves sufficient army to continue pressure;
- relocation improves economic output or strategic survivability.

The historical source frequently demonstrates conversion but not realization.

That is not a weakness in the code; it is a boundary in our evidence.

---

# 9. World-state evidence hierarchy

For future passes, use this hierarchy:

### W0 — command only

Exact `.per` action exists.

### W1 — pending state

Source exposes a pending/queue/eligibility state indicating the action was accepted for execution.

### W2 — world-state observation

Runtime/replay/source-visible game state demonstrates the object, research, movement, building, or other intended state changed.

### W3 — operational capability

The changed state is sufficient to perform the intended next operation.

### W4 — strategic effect

The game relationship changed in the intended direction.

Pass 13 currently establishes many W0/W1 chains, but few W2+ chains.

This becomes the standard vocabulary for Layer 2.

---

# 10. Falsifier register

## F1 — research

Would be falsified as a successful conversion if the command is systematically rejected despite the apparent `can-research-with-escrow` guard.

## F2 — camel production

Would be falsified as realized capability if `traincamel` activates but no valid production path or unit stock follows under the same state conditions.

## F3 — retreat

Would be falsified as physical retreat if `up-retreat-now` consistently leaves the relevant attack group stationary or produces no repositioning under valid execution conditions.

## F4 — land-nomad relocation

Would be falsified as physical relocation if the action consumer does not move the selected villager/search set toward the constructed point under valid execution conditions.

## F5 — strategic interpretations

Centralization, counter-capability improvement, survival preservation, and economic improvement remain falsifiable hypotheses. None should be promoted without world-state evidence.

---

# 11. State ownership observations

Pass 13 strengthens several ownership classifications.

| Channel | Observed writer role | Observed reader role | Ownership confidence | Lifecycle |
|---|---|---|---|---|
| `escrow-purpose-goal` | research/resource controller | escrow/research rules | HIGH | event/reset |
| food/gold escrow percentages | resource controller | resource/escrow execution | HIGH | persistent until release |
| `traincamel` | threat/context rules | production rules | MEDIUM-HIGH | event/context dependent |
| `cavarchers` | threat measurement | production/research | MEDIUM | lifecycle still incomplete |
| `retreat-now-goal` | threat/attack controller | retreat controller | HIGH | transient |
| `restart-attack-goal` | building/attack transition | attack reset | HIGH | transient |
| `504/505` | land-nomad search | movement consumer | HIGH for local edge | routine-dependent |

Ownership means “observable control role,” not exclusive source-file ownership.

Multiple writers remain possible.

---

# 12. Strategic closure scoreboard

| Chain | Control | W0/W1 | W2 | W3 | W4 | Status |
|---|---:|---:|---:|---:|---:|---|
| resource escrow → research | YES | YES | OPEN | OPEN | OPEN | control-closed |
| threat → camel response | YES | YES | OPEN | OPEN | OPEN | control-closed |
| threat → camel research | YES | YES | OPEN | OPEN | OPEN | control-closed |
| attack threat → retreat | YES | YES | OPEN | OPEN | OPEN | control-closed |
| retreat → restart controller | YES | YES | OPEN | OPEN | OPEN | control-closed |
| land-nomad search → movement | YES | YES | OPEN | OPEN | OPEN | control-closed |

The central result is deliberately conservative:

> **Layer 2 is now strong on causal control provenance, but world-state and strategic-effect closure remain the major empirical frontier.**

---

# 13. What Pass 13 changes in the programmer reconstruction

The programmer's architecture can now be described more precisely.

They repeatedly built mechanisms that answer:

1. **Is the capability worth pursuing?** — often only partially visible/inferred.
2. **Can the capability be afforded?** — strongly represented.
3. **Can the engine execute the action now?** — strongly represented.
4. **Where should execution occur?** — often explicitly searched.
5. **What state should persist while execution is pending?** — frequently represented.
6. **What state should be released/reset afterward?** — frequently represented.
7. **Did the game actually realize the capability?** — generally not directly proven by source archaeology.
8. **Did the realization improve the strategic position?** — generally requires runtime/game evidence.

This is a sharper model than “the programmer wrote a distributed controller.”

The historical controller is particularly strong at **conversion control** and comparatively opaque at **postcondition observation** when studied only as source.

That asymmetry is itself an important engineering finding.

---

# 14. AEGIS design consequence

AEGIS should make the missing vertical stages first-class:

```text
OBJECTIVE
  ↓
REQUIREMENT
  ↓
RESOURCE / CAPABILITY RESERVATION
  ↓
EXECUTABILITY CHECK
  ↓
ACTION
  ↓
PENDING
  ↓
WORLD POSTCONDITION
  ↓
OPERATIONAL POSTCONDITION
  ↓
STRATEGIC POSTCONDITION
  ↓
SUCCESS / FAILURE CLASSIFICATION
  ↓
COMMITMENT RELEASE / MODIFICATION
```

The historical source gives us excellent examples of the left half.

AEGIS must not inherit the assumption that the left half is sufficient.

---

# 15. Pass 13 conclusion

Pass 12 gave us the network.

Pass 13 gives us the vertical boundary conditions of that network.

The strongest current historical statement is:

> The programmer repeatedly transformed game observations into compact control state, protected or redirected resources, checked local executability, searched for an executable location or target, issued a side effect, and reset controller state for subsequent evaluation.

The source strongly supports **conversion control**.

The source alone does not yet prove the complete chain from command to realized world state to strategic success.

Therefore the next research target is not another conceptual architecture document.

It is **empirical closure**: obtain reproducible observations of selected historical behaviors and attach those observations to the existing causal edges.

---

# 16. Pass 14 mission

Pass 14 should build the first **Historical Runtime Observation Pack**, without relying on the shelved automated scenario-loading workflow.

Priority:

1. establish a minimal reproducible runtime observation protocol;
2. use existing verified source behaviors that can be observed in ordinary gameplay/replay;
3. capture before/after state around research, training, retreat, and movement actions;
4. distinguish command acceptance, pending state, realized world state, and strategic effect;
5. attach observations to the existing graph as W2/W3/W4 evidence;
6. if a behavior cannot be reproduced reliably, mark it OPEN rather than substituting assumptions.

The scenario automation failure is therefore not a reason to stop Layer 2. It simply means the empirical method must be redesigned around the stable runtime surfaces available to us.
