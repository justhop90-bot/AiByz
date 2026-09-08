# AEGIS-BYZ — State / Service Dependency Matrix — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Primary corpus:** target-build `AI (HD version).per`, SHA-256 `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`
**Status:** STATIC DECONSTRUCTION — exact source-site evidence; runtime scheduling remains unqualified

## 1. Purpose

This matrix is the next layer after the authority-boundary reconstruction. It records concrete state/service transitions at exact stock rule sites and translates them into proposed AEGIS service boundaries.

It is intentionally stricter than a subsystem co-occurrence census. A row is included only when the cited rule block contains an identifiable observation/precondition and an identifiable state mutation or engine-facing operation.

The AEGIS column is an architectural translation, not a claim that the stock engine contains these typed objects.

## 2. Evidence convention

```text
S = source-level fact
A = AEGIS architectural translation
R = runtime qualification required
```

No S row implies same-pass execution, immediate command completion, or a particular interpreter schedule.

## 3. Core dependency matrix

| ID | Stock rule site | Producer / input | Mutation / operation | Immediate historical consumer class | AEGIS owner | Proposed contract | Status |
|---|---:|---|---|---|---|---|---|
| SD-01 | 7526–7541 | enemy context, position=`flank`, dark-age food state, control/strategy state | `strategy-goal := flush`; `unit-goal := default-flush-unit`; military-spread controls | strategy + military | Strategy OS | `StrategicIntent(Flush)` + `MilitaryDemand` | S/A; R timing |
| SD-02 | 7572–7589 | feudal state, position=`flank`, food threshold, enemy military population, existing strategy/control | `strategy-goal := flush`; `unit-goal := default-flush-unit`; `control-goal := belated-flush-defense` | military + economy | Strategy OS | `StrategicIntent` + `EconomyDemand` + `MilitaryDemand` | S/A; R timing |
| SD-03 | 6858–6868 | enemy composition via `players-unit-type-count` | `sn-archer-threat := 2` | threat / military policy | Threat OS | `ThreatAssessment(Archer)` | S/A; R persistence |
| SD-04 | 6882–6892 | enemy composition via `players-unit-type-count` | `sn-archer-threat := 3` | threat / military policy | Threat OS | `ThreatAssessment(Archer)` | S/A; R persistence |
| SD-05 | 6906–6916 | enemy composition via `players-unit-type-count` | `sn-archer-threat := 4` | threat / military policy | Threat OS | `ThreatAssessment(Archer)` | S/A; R persistence |
| SD-06 | 7018–7032 | enemy cavalry observation/context | `sn-cavalry-threat := 1` | threat / military policy | Threat OS | `ThreatAssessment(Cavalry)` | S/A; R persistence |
| SD-07 | 26189–26206 | TC/resource/service-distance conditions, `farm-goal`, pending-farm count, `can-build farm` | `build farm` | construction execution | Construction OS | `ConstructionRequest(Farm)` | S/A; R command completion |
| SD-08 | 26137–26175 | wood/stone/economic state, villager count, research/building state, `can-build` | `build stable` / `build archery-range` / `build barracks` paths | construction execution | Construction OS | `InfrastructureDemand` → `ConstructionRequest` | S/A; R timing |
| SD-09 | 25833–25889 | strategic/economic state, tech/pending state, resource/building conditions | `build-forward` for production/siege infrastructure | construction execution | Construction OS | `ForwardConstructionRequest` | S/A; R placement persistence |
| SD-10 | 16306–16318 | research status + `can-build siege-workshop` | siege-workshop town-size/build state mutation | construction / strategic posture | Construction OS | `InfrastructureDemand(SiegeWorkshop)` | S/A; R timing |
| SD-11 | 16319–16341 | `can-build siege-workshop` + strategy-dependent conditions | siege-workshop demand/posture state | construction | Construction OS | `ConstructionRequest` | S/A; R timing |
| SD-12 | 16506–16516 | `forward-threat-goal` / strategic conditions | clears `increase-town-size-goal` | construction policy | Construction OS with Strategy input | `ConstructionCancellation` | S/A; R supersession |
| SD-13 | 7759–7783 | research availability/status including loom | strategy/unit/control state becomes flush posture | strategy + production | Strategy OS | `StrategicIntent` + `MilitaryDemand` | S/A; R timing |
| SD-14 | 7925–7939 | research status (`ri-chieftains`) | `control-goal := my-unique-unit-line`; `uu-up-goal := 1` | production policy | Production OS | `ProductionRequest(UniqueUnit)` | S/A; R control semantics |
| SD-15 | 7963–7974 | long-swordsman research status | `strategy-goal := rush`; `unit-goal := militiaman-line` | strategy + production/military | Strategy OS | `StrategicIntent(Rush)` + `MilitaryDemand` | S/A; R timing |
| SD-16 | 8002–8014 | strategic/map/context conditions | rush + aggressive-rush control + archer production state | strategy + military + production | Strategy OS | `StrategicIntent(Rush)` + typed demands | S/A; R control semantics |
| SD-17 | 8015–8027 | strategic/map/context conditions | boom + reset control + archer production state | strategy + military + production | Strategy OS | `StrategicIntent(Boom)` + typed demands | S/A; R control semantics |
| SD-18 | 8899–8914 | cavalier research status | control state copied from unit goal; `unit-goal := knight` and ranged-unit state changes on alternate paths | production + military | Production/Military boundary | `CompositionDemand` + `ProductionRequest` | S/A; R branch/schedule |
| SD-19 | 5229–5239 | nomad/landnomad state | `up-assign-builders` to TC foundation | construction execution | Construction OS | `BuilderAssignmentRequest(TC)` | S/A; R pending semantics |
| SD-20 | 5731–5745 | `can-build town-center` | `build town-center` + town-size state mutation | construction / economy | Construction OS | `ConstructionRequest(TC)` | S/A; R completion |
| SD-21 | 5923–5938 | lumber-camp eligibility + resource/service conditions | gatherer SN changes + `build lumber-camp` | economy + construction | Economy → Construction contract | `ResourceInfrastructureDemand` | S/A; R reconciliation |
| SD-22 | 5939–5954 | mining-camp eligibility + resource/service conditions | gatherer/resource-control settings + `build mining-camp` | economy + construction | Economy → Construction contract | `ResourceInfrastructureDemand` | S/A; R reconciliation |
| SD-23 | 5980–5991 | `can-research ri-loom` | `research ri-loom` | research/economic state | Research OS | `ResearchRequest(Loom)` | S/A; R completion |
| SD-24 | 20409–20420 | horse-collar research completion | `farm-goal := 1` | economy / construction | Economy OS | `FarmInfrastructureDemand` | S/A; R persistence |
| SD-25 | 6067–6078 | treadmill-crane research state | `up-assign-builders` for house | construction | Construction OS | `BuilderAssignmentRequest(House)` | S/A; R pending semantics |
| SD-26 | 16085–16094 | champion/research conditions + barracks eligibility | `build barracks` | construction / military infrastructure | Construction OS | `InfrastructureDemand(Barracks)` | S/A; R timing |
| SD-27 | 16102–16112 | heavy-scorpion/research conditions + siege-workshop eligibility | `build siege-workshop` | construction / military production | Construction OS | `InfrastructureDemand(SiegeWorkshop)` | S/A; R timing |

## 4. High-confidence service transitions

### 4.1 Strategy → Economy

The strongest exact site is rule **7572–7589**. The same stock rule that detects enemy military pressure and food conditions changes strategy to `flush`, selects the flush unit goal, and writes `belated-flush-defense`; the source comment explicitly associates the control mutation with changing gatherer percentages toward wood.

Therefore the static reconstruction is:

```text
Situation / enemy pressure
        +
Economic state
        ↓
Strategic transition
        ↓
Economic control demand
```

**AEGIS boundary:** Strategy owns the decision; Economy owns the resulting allocation policy. Economy must not become the owner of `StrategicIntent` merely because the historical rule mutates both.

### 4.2 Scouting → Threat → Military

Rules **6858–6868**, **6882–6892**, and **6906–6916** use enemy unit composition observations and transform them into `sn-archer-threat` levels. This is the cleanest observed source-level example of an observation-to-threat transformation.

```text
Enemy observation
      ↓
Threat assessment
      ↓
Military policy
```

**AEGIS boundary:** Scouting owns observation; Threat owns interpretation; Military consumes threat as policy input.

### 4.3 Economy → Construction

Rule **26189–26206** is the cleanest exact edge: resource/service conditions and `farm-goal` state participate in farm build eligibility, followed by the engine-facing `build farm` action.

```text
Economic / infrastructure demand
        ↓
Construction eligibility
        ↓
Engine build command
```

**AEGIS boundary:** Economy emits demand; Construction owns admission, placement, builder selection, and execution.

### 4.4 Strategy → Construction

Rules **25833–25889** combine strategic, technology, resource, and existing-building state with `can-build` and then issue `build-forward` for production/siege infrastructure.

```text
Strategic + technology + economic state
        ↓
Infrastructure demand
        ↓
Construction service
```

**AEGIS boundary:** Strategy can request strategic infrastructure; Construction owns physical execution and placement.

### 4.5 Research → Production / Military

Rules **7925–7939**, **7963–7974**, and **8899–8914** demonstrate that research state is not an isolated technology subsystem. Research availability/pending state changes production composition and strategic posture.

```text
Research state
      ↓
Composition / strategic policy
      ↓
Production + Military
```

**AEGIS boundary:** Research owns technology state; Strategy/Military/Production consume typed capability information.

## 5. Verification boundary

The source repeatedly combines an engine-facing operation with predicates that concern capability or pending state. This is evidence for a distinction between:

```text
CAN EXECUTE
    ≠
COMMAND ISSUED
    ≠
FOUNDATION OBSERVED
    ≠
COMPLETED
    ≠
RECONCILED
```

Examples include `can-build` followed by `build`, and `up-assign-builders` against foundation object classes.

The source alone does **not** establish exact latency between these states.

Therefore AEGIS requires a verification boundary:

```text
Service Request
      ↓
Engine Command
      ↓
Observed Result
      ↓
Verification
      ↓
Completion / Failure / Recovery
```

## 6. Supersession requirements

The exact source sites reveal state replacement and cancellation patterns, especially for:

- `strategy-goal`;
- `control-goal`;
- `unit-goal`;
- `increase-town-size-goal`;
- `farm-goal`.

AEGIS must therefore attach generation/validity to cross-service requests where stale decisions could survive a strategic transition.

Conceptual request envelope:

```text
request_id
generation
owner
intent
priority
preconditions
created_from_evidence
expiry / validity
```

A later request must supersede an older request explicitly rather than relying on numeric overwrite semantics.

## 7. Negative findings

The static corpus cannot establish from these rule blocks alone:

- whether a mutation is visible to a later rule in the same interpreter pass;
- exact rule scheduling order;
- whether a command completes in the same pass;
- exact pending-object lifetime;
- exact placement persistence;
- whether a downstream consumer observes the value before or after another writer supersedes it;
- whether every historical branch is active under every target runtime condition.

These remain runtime qualification targets.

## 8. Architectural decision

The dependency matrix is sufficient to freeze the **direction** of the primary AEGIS service boundaries, but not sufficient to freeze the numeric state ABI.

Freeze now:

```text
Observation → Context
Context → Strategy / Threat
Strategy → Demand
Demand → Arbitration
Arbitration → Service Request
Service → Engine Command
Engine → Observed Result
Observed Result → Verification / Recovery
```

Do not freeze yet:

```text
goal numbers
strategic-number allocations
timer allocations
same-pass scheduling assumptions
completion latency assumptions
```

## 9. Next extraction

The remaining high-value static gap is not another broad subsystem census. It is **lifecycle closure**.

For the highest-value contracts, trace every state from first producer through all consumers and all reset/supersession sites:

1. `StrategicIntent → MilitaryDemand → ProductionRequest → UnitState`
2. `EnemyObservation → ThreatAssessment → MilitaryResponse`
3. `FoodDemand → FarmInfrastructureDemand → ConstructionRequest → FarmExecutionState → EconomicReconciliation`
4. `ResearchState → CapabilityChange → Strategy/Production/Military`

Each lifecycle must end in one of:

```text
CONFIRMED
FAILED + CLASSIFIED
SUPERSEDED
EXPIRED
INVALIDATED
```

Only after lifecycle closure should the AEGIS `/state` ABI be populated with persistent channels.

## Evidence discipline

**STATIC-QUALIFIED:** exact rule-site locations and source operations cited above, plus the architectural separation directly supported by those operations.

**RUNTIME-UNQUALIFIED:** temporal ordering, same-pass visibility, persistence duration, command completion timing, and engine-side side effects not explicit in source.
