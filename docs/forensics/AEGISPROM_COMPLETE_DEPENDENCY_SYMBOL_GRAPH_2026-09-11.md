# AEGISProm Complete Dependency / Symbol Graph Audit

**Date:** 2026-09-11  
**Scope:** `main/AegisProm` only  
**Excluded:** `runtime/AegisProm`, machine-local runtime, ADProm, byzwarcouncil  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652 where stated by source files

## 1. Executive determination

`AegisProm` is not one executable architecture. It is a source laboratory containing:

1. a strategic/control-plane skeleton;
2. a civilian economic vertical slice;
3. a military/threat and tactical-micro vertical slice;
4. qualification/probe modules; and
5. stock/development constants with provenance contamination.

The most important result is that several files that appear to form a complete strategic loop are only state-propagation layers. The real game-facing behavior is concentrated in bounded vertical slices such as worker tasking, housing construction, villager production, cavalry response, and the micro physical adapter.

**No source file was modified by this audit.** This document records the graph and defects so future implementation work can be evidence-gated.

---

## 2. 49-file inventory and graph role

| # | File | Role | Graph status |
|---:|---|---|---|
| 1 | `AEGIS-Carpenter-final.per` | WM publication monitor | monitor / terminal output |
| 2 | `AEGIS-cavalry-response-v0.per` | cavalry threat response | physical production slice |
| 3 | `AEGIS-civilian-census-v0.per` | civilian observation | live candidate observer |
| 4 | `AEGIS-civilian-demand-v0.per` | civilian demand | demand producer |
| 5 | `AEGIS-civilian-lifecycle-reconciler-v0.per` | production reconciliation | observer/reconciler |
| 6 | `AEGIS-civilization-state-v0.per` | civilization snapshot | state producer |
| 7 | `AEGIS-dynamic-worker-loop-probe-v0.per` | qualification probe | experimental / non-production |
| 8 | `AEGIS-economic-demand-arbitration-v0.per` | demand arbitration | active decision component |
| 9 | `AEGIS-economic-demand-v0.per` | resource worker demand | active demand component |
| 10 | `AEGIS-foundation.per` | world model | root state producer |
| 11 | `AEGIS-housing-construction-v0.per` | housing construction | physical construction slice |
| 12 | `AEGIS-integration-candidate-v0.per` | candidate loader | explicit non-production loader |
| 13 | `AEGIS-micro-control-v0.per` | tactical intent | micro controller |
| 14 | `AEGIS-micro-execution-bridge-v0.per` | tactical execution authority | bridge |
| 15 | `AEGIS-micro-geometry-v0.per` | tactical geometry | micro support |
| 16 | `AEGIS-micro-governor-v0.per` | tactical command governor | micro support |
| 17 | `AEGIS-micro-groups-v0.per` | tactical group state | micro support |
| 18 | `AEGIS-micro-physical-adapter-v0.per` | physical tactical dispatch | physical execution |
| 19 | `AEGIS-micro-state-v0.per` | tactical state | micro observation |
| 20 | `AEGIS-micro-targeting-v0.per` | target selection | micro support |
| 21 | `AEGIS-micro-verification-v0.per` | tactical verification | verification candidate |
| 22 | `AEGIS-military-final.per` | force readiness | terminal service |
| 23 | `AEGIS-military-production-v0.per` | military production lifecycle | production candidate |
| 24 | `AEGIS-operations-final.per` | service heartbeat | terminal service |
| 25 | `AEGIS-research-age-v0.per` | age transition | transition observer |
| 26 | `AEGIS-scouting-threat-v0.per` | enemy composition threat | threat observer |
| 27 | `AEGIS-source-dropsite-serviceability-v0.per` | source qualification | task prerequisite |
| 28 | `AEGIS-stock-defaultConstants.per` | stock ABI/constants | external dependency substrate |
| 29 | `AEGIS-stock-finalingConstants.per` | stock/development constants | provenance hazard |
| 30 | `AEGIS-threat-recovery-v0.per` | tactical retreat/recovery | recovery controller |
| 31 | `AEGIS-villager-production-v0.per` | villager production | physical production slice |
| 32 | `AEGIS-worker-loop-qualification-v0.per` | worker qualification | experimental / non-production |
| 33 | `AEGIS-worker-productivity-observer-v0.per` | productivity observation | observation candidate |
| 34 | `AEGIS-worker-recovery-v0.per` | worker failure recovery | recovery candidate |
| 35 | `AEGIS-worker-role-census-v0.per` | worker role observation | observation producer |
| 36 | `AEGIS-worker-role-vector-v0.per` | role deficits | demand producer |
| 37 | `AEGIS-worker-target-selection-v0.per` | worker candidate selection | selection component |
| 38 | `AEGIS-worker-task-command-v0.per` | worker task dispatch | physical execution |
| 39 | `AEGIS-worker-task-verification-v0.per` | worker task verification | verification component |
| 40 | `Aegis-belief-final.per` | belief | control plane |
| 41 | `Aegis-commitment-final.per` | commitment | control plane |
| 42 | `Aegis-decision-final.per` | decision | control plane |
| 43 | `Aegis-economy-final.per` | economy pressure | terminal skeleton |
| 44 | `Aegis-execution-final.per` | execution state | control-plane skeleton |
| 45 | `Aegis-military-final.per` | military state | terminal skeleton |
| 46 | `Aegis-objectives-final.per` | objectives | control plane |
| 47 | `Aegis-planning-final.per` | planning | control plane |
| 48 | `Aegis-recovery-final.per` | recovery | control-plane skeleton |
| 49 | `Aegis-situation-final.per` | situation | control plane |

---

## 3. Strategic/control-plane dependency graph

```text
AEGIS-foundation
      |
      v
Aegis-belief-final
      |
      v
Aegis-situation-final
      |
      v
Aegis-objectives-final
      |
      v
Aegis-planning-final
      |
      v
Aegis-decision-final
      |
      v
Aegis-commitment-final
      |
      v
Aegis-execution-final
      |
      v
Aegis-verification-final
      |
      v
Aegis-recovery-final
```

Generation chain:

```text
WM 302 -> Belief 340 -> Situation 350 -> Objective 360 -> Plan 370
    -> Decision 380 -> Commitment 390 -> Execution 395
    -> Verification 398 -> Recovery 580
```

The generation numbers are publication generations, not a compiler/topological load order.

### Critical semantic result

`Aegis-execution-final.per` does not issue a physical command. It copies commitment kind into execution state. `Aegis-verification-final.per` initializes `aegis-verification-observed` to zero and marks verification valid. `Aegis-recovery-final.per` increments recovery attempts when a new verification generation appears. Therefore the apparent strategic `Execute -> Verify -> Recover` chain is a **control-state skeleton**, not a proven action lifecycle.

---

## 4. Civilian economic vertical slice

```text
AEGIS-worker-role-census
          |
          v
AEGIS-worker-role-vector
          |
          v
AEGIS-economic-demand
          |
          v
AEGIS-economic-demand-arbitration
          |
          +------------------+
          |                  |
          v                  v
AEGIS-worker-target   AEGIS-source-dropsite
-selection            -serviceability
          |                  |
          +--------+---------+
                   |
                   v
          AEGIS-worker-task-command
                   |
             +-----+------+
             |            |
             v            v
       task-verification productivity-observer
             |
             v
       worker-recovery
             |
             v
       worker-loop-qualification
```

### Physical execution point

`AEGIS-worker-task-command-v0.per` contains real `up-target-objects` dispatch for wood, gold and stone after worker/source qualification. This is a genuine engine-facing execution adapter, unlike the abstract final execution module.

### Major blocker

`AEGIS-worker-role-vector-v0.per` defines all V0 desired targets as zero:

```text
aegis-wrv-target-food 0
aegis-wrv-target-wood 0
aegis-wrv-target-gold 0
aegis-wrv-target-stone 0
aegis-wrv-target-builder 0
```

It derives deficits from desired minus observed and clamps negative values to zero. Unless another policy writer changes those targets, normal worker demand is therefore zero. The downstream execution chain is structurally present but normally starved of demand.

### Additional semantic limitation

Worker target selection searches for eligible villagers, not persistent worker identities. This is deliberate in V0 but means later verification cannot automatically prove that the exact worker selected was the worker that produced a later observation.

---

## 5. Civilian production branch

```text
AEGIS-civilization-state
          |
          v
AEGIS-civilian-demand
       /       \
      v         v
villager     housing
production   construction
      |         |
      v         v
census/lifecycle observation
```

`AEGIS-villager-production-v0.per` contains a real villager training command and explicitly separates queue admission from completion.

`AEGIS-housing-construction-v0.per` contains a real house build command followed by pending/completed-house observation.

`AEGIS-civilian-lifecycle-reconciler-v0.per` distinguishes issued/pending/confirmed states. Its confirmation is population/census-based rather than identity-linked causal proof, so it should remain classified as composed evidence until stronger runtime evidence exists.

---

## 6. Threat/military graph

```text
AEGIS-foundation
      |
      +------------------+
      |                  |
      v                  v
scouting-threat      military-final
      |                  |
      +--------+         +--> terminal readiness
               |
        +------+------+
        |             |
        v             v
cavalry-response   threat-recovery
        |             |
        v             v
  spearman train   micro-control
```

`AEGIS-scouting-threat-v0.per` observes enemy scout cavalry, cavalry archers and knights and classifies a cavalry threat using explicit thresholds.

`AEGIS-cavalry-response-v0.per` can issue `up-train escrow-state c: spearman-line` after the threat and feasibility gates pass. This is a bounded real production response.

`AEGIS-military-production-v0.per` contains an important defect: `aegis-mp-unit` is declared and compared against `aegis-mp-unit-spearman` / `aegis-mp-unit-camel`, but the file does not establish an initial value for `aegis-mp-unit`. The intended production branch is therefore statically blocked by uninitialized selector state unless an external writer supplies it.

---

## 7. Tactical micro graph

```text
Scouting/Threat --------+
                        |
World Model ------------+--> Micro Control
                        |        |
                        |        +--> Targeting
                        |        |
                        |        +--> Geometry
                        |        |
                        |        +--> Micro State -> Groups
                        |                         |
                        |                         v
                        |                      Governor
                        |                         |
                        +-------------------------v
                                      Execution Bridge
                                             |
                                             v
                                      Physical Adapter
                                             |
                                             v
                                      Micro Verification
```

Generation allocation:

```text
Micro Control       670
Micro State         680
Micro Groups        690
Micro Geometry      700
Micro Governor      710
Micro Verification  720
Execution Bridge    730
```

### Stage-contract hazard

Micro Control creates engage intent at `stage-search`. Targeting can move the control state to `stage-authorized`. Physical Adapter requires `stage-authorized` before dispatch. This is a cross-file mutable-state contract, not a single-owner state machine. Ownership and transition authority should be made explicit before promotion.

The physical adapter contains real tactical commands:

- attack-move for engage;
- stop for retreat;
- move for regroup.

It deliberately does not infer completion from dispatch.

### Verification limitation

The micro verification module contains state for observed results, but the current source does not establish a complete world-state proof chain equivalent to “command caused tactical outcome.” It remains a verification candidate.

---

## 8. Undefined symbol classes

There are no major unresolved **Aegis-local namespace declarations** where the entire referenced `aegis-*` symbol is absent from the 49-file architecture.

There are, however, three different dependency classes that must not be conflated:

### A. Aegis-local declared state

These are the `aegis-*` goals and constants owned by AegisProm.

### B. External stock/engine ABI

Examples include:

```text
game-time
population
population-cap
resource-amount
unit-type-count
unit-type-count-total
building-type-count-total
can-train
can-build
can-research
villager-class
spearman-line
camel-line
knight-line
archer-line
skirmisher-line
action-default
action-move
action-stop
action-attack-move
actionid-attack
orderid-build
orderid-repair
orderid-enter
object-data-carry
object-data-action
object-data-order
object-data-target
object-data-tasks-count
object-data-distance
position-self-x
```

These are legitimate external dependencies only if supplied by the target stock/engine environment. They are not proof that AegisProm is self-contained.

### C. External strategic numbers

The source/dropsite serviceability module references:

```text
sn-maximum-gold-drop-distance
sn-maximum-stone-drop-distance
```

These are not defined in the AegisProm directory and must be treated as explicit stock strategic-number ABI dependencies.

---

## 9. Declared-but-uninitialized / weakly established state

This category is more important than ordinary lexical undefined symbols.

### `aegis-mp-unit`

Declared but no initial assignment is established before branch selection. **P0/P1 integration blocker.**

### `aegis-wm-age`

Foundation explicitly sets it to zero rather than acquiring a verified age fact. Age therefore must not be treated as observed world state.

### `aegis-wm-focus-player`

Foundation sets it to `1`. This is an implementation value, not proof that `1` is the engine's self-player identity. Player-index semantics require direct engine qualification.

### `aegis-verification-observed`

Declared as an observation field but initialized to `0` by the final verification skeleton. No actual world-state observation establishes success.

### `aegis-mv-observed`

Micro verification has an observation field but the source graph does not establish a complete physical outcome writer.

---

## 10. Duplicate/conflicting definitions

### Definite duplicate: `building-count`

Defined in both stock constants files with value `27`.

### Definite duplicate: `building-type-count`

Defined in both stock constants files with value `28`.

### Severe conflict: `port`

`AEGIS-stock-finalingConstants.per` defines `port` repeatedly with values:

```text
45
2141
2142
2143
2172
```

This is not a clean canonical symbol definition.

### Severe conflict: `trainocteres`

Defined twice:

```text
8007
8008
```

### Conditional duplicate families

The finaling constants also repeatedly redefine naval identifiers under civilization-specific conditional blocks, including `galley-line`, `demolition-ship-line`, `fire-ship-line`, `cannon-galleon-line`, `fishing-ship`, and `transport-ship`.

These are not all unconditional duplicates because conditional compilation matters, but they demonstrate that the file is an amalgam of stock/development provenance rather than a clean Byzantine namespace.

---

## 11. Dead / terminal modules

“Dead” is divided into intentional experimental dead-end, terminal output, and blocked output.

### Intentional non-production

- `AEGIS-integration-candidate-v0.per`
- `AEGIS-dynamic-worker-loop-probe-v0.per`
- `AEGIS-worker-loop-qualification-v0.per`

These should remain outside production unless explicitly promoted after qualification.

### Terminal service outputs

- `Aegis-economy-final.per`
- `Aegis-military-final.per`
- `AEGIS-operations-final.per`
- `AEGIS-Carpenter-final.per`

Their outputs do not have demonstrated consumers in the 49-file source graph.

They are not necessarily useless; they are currently **terminal monitors/services**, not demonstrated decision inputs.

### Dead state inside live files

Several fields are published without a demonstrated downstream consumer or without a world-state writer. These should be classified individually as `LIVE`, `TERMINAL`, `EXPERIMENTAL`, `RESERVED`, or `BLOCKED`, not blindly deleted.

---

## 12. Candidate load order

The explicit candidate loader provides the clearest source-level load order for the civilian slice:

```text
foundation
Carpenter
belief
situation
objectives
planning
decision
commitment
execution
verification
recovery
economy
operations
civilian census
civilization state
worker role census
worker role vector
civilian demand
economic demand
economic demand arbitration
worker target selection
source/dropsite serviceability
worker task command
worker task verification
worker productivity observer
worker recovery
villager production
civilian lifecycle reconciler
housing construction
qualification probes
```

The loader explicitly labels itself **candidate only** and says it is not loaded by the production root. Therefore this is a **candidate load graph**, not evidence of runtime qualification.

The load order is also not a complete dependency proof: `.per` modules can share symbols and external ABI, and generation numbers do not themselves establish rule firing order.

---

## 13. Generation conflicts / semantic mismatches

The generation bands are mostly coherent within each subsystem, but there are several distinct concepts being called “generation”:

1. world-model publication generation;
2. downstream snapshot generation;
3. command generation;
4. lifecycle generation;
5. tactical epoch.

These must not be treated as the same clock.

Examples:

```text
WM generation           302
Belief                  340
Situation               350
Objective               360
Plan                    370
Decision                380
Commitment              390
Execution               395
Verification            398
Recovery                580

Worker census           433/440
Worker role census      450-range
Worker role vector      465
Economic demand         479
Arbitration             490
Source qualification    499
Worker selection        510
Task command            519
Productivity             526
Task verification       534/545
Worker recovery         546+

Threat                  610-range
Micro                    670-730
```

The numerical values are useful namespace allocations, but they are not proof of execution ordering.

The micro bridge additionally uses a tactical epoch field while other modules use generation fields. This should be normalized by contract rather than by arbitrary renumbering.

---

## 14. Highest-priority defects

### P0 — Final strategic execution is not physical execution

`Aegis-execution-final.per` is a state copier. It is not an engine command adapter.

### P0 — Final verification is not verification

`Aegis-verification-final.per` does not observe a world-state consequence.

### P0 — Stock finaling constants are symbolically unsafe

At minimum, `port` and `trainocteres` have conflicting definitions.

### P1 — Economic vertical slice is demand-starved by default

Worker-role policy targets are all zero.

### P1 — Military production selector is uninitialized

`aegis-mp-unit` lacks a demonstrated initializer.

### P1 — Micro control-stage ownership is split

Targeting changes state that the physical adapter later interprets as authorization.

### P1 — External ABI is not fully closed inside AegisProm

Strategic numbers and stock engine vocabulary remain required.

### P2 — Terminal outputs need ownership classification

Economy, military, operations, and Carpenter outputs currently terminate without demonstrated consumers.

---

## 15. What should NOT be done

1. Do not delete the final control-plane modules merely because they are incomplete.
2. Do not declare them functional because their state chain is syntactically coherent.
3. Do not promote candidate/probe modules to production by adding them to a loader.
4. Do not clean the stock constants by guessing which duplicate value is correct.
5. Do not infer native engine semantics from symbol names alone.
6. Do not replace historical AI/Promisory behavior with invented abstractions merely to fill graph gaps.
7. Do not equate command issuance, queue admission, object completion, world-state consequence, or strategic success.

---

## 16. Promotion strategy

The correct reconstruction strategy is vertical, not architectural-by-name:

```text
Historical AI(HD) + Promisory evidence
                 |
                 v
          behavioral contract
                 |
                 v
          AegisProm adapter
                 |
                 v
       actual engine-facing action
                 |
                 v
       observable world consequence
                 |
                 v
          verified outcome
                 |
                 v
       belief/state update
                 |
                 v
            reassessment
```

The strongest existing AegisProm candidates for this treatment are:

1. worker task command;
2. worker task verification;
3. housing construction;
4. villager production/lifecycle;
5. cavalry threat -> spearman response;
6. tactical micro physical adapter.

Each should be proven independently before being wired into the higher-level strategic loop.

---

## 17. Final architectural verdict

**AegisProm status: EXPERIMENTAL ENGINEERING BASE / PARTIAL VERTICAL IMPLEMENTATION.**

It is not a finished Byzantine bot, but it is not empty scaffolding either.

The source contains real engine-facing execution behavior and several well-separated observation/reconciliation contracts. The principal danger is the appearance of completeness created by the `*-final.per` control-plane naming. The graph shows that those final layers are presently mostly coordination/state propagation, while the strongest actual behavior exists in the V0 vertical slices.

The next implementation phase should therefore preserve the useful slices, repair their state/ABI contracts, and reconstruct the missing strategic behavior from the proven historical AI(HD)+Promisory functional chain.
