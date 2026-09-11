# AiBuilder Execution Contract — v0.1

**Status:** STUDY BASELINE — not yet a production interface

This document defines the initial contract that can be supported by static analysis of the current AiBuilder corpus. Anything marked runtime-unknown or unconfirmed is deliberately left open.

## 1. Contract model

For each AiBuilder subsystem, distinguish:

1. **Inputs** — state/facts the rules read.
2. **Policy outputs** — Goals/SNs written for downstream modules.
3. **Feasibility** — conditions that determine whether an action may be requested.
4. **Physical request** — engine-facing command such as build/train/research/buy.
5. **Pending state** — evidence that the engine has accepted or is processing the request, where the corpus exposes it.
6. **World transition** — evidence that the requested object/tech actually exists or changed state.
7. **Failure** — explicit or inferable failure state.
8. **Reassessment** — return to policy evaluation after the action lifecycle.

AiBuilder frequently establishes steps 1–4. The study must determine, rather than assume, how far each action path establishes steps 5–8.

---

## 2. `phaseUpdate.per`

### Role

Phase transition and policy projection.

### Inputs

- `current-phase`
- `previous-phase`
- phase configuration constants
- phase signals/events used by the phase rules

### Writes

The module writes the major `desired-*` and `upgrade-*` policy goals, including civilian, building, military, technology, and age-progression targets.

### State model

Current static evidence shows:

```text
current-phase: transitioned by phase-entry rules
previous-phase: read but not currently written
```

### Established behavior

Phase-entry rules use `disable-self`, while phase configuration rules are conditioned by the relationship between `current-phase` and `previous-phase`.

### Defect

**DIRECT STATIC FINDING:** `previous-phase` has no writer in the current corpus examined.

### Consequence

The phase configuration rules can remain eligible repeatedly rather than behaving as a clean one-transition projection layer.

### Repair status

A repair that records the current phase into `previous-phase` after configuration is **STATICALLY SOUND**, but whether same-pass versus next-pass evaluation produces the intended runtime behavior is **RUNTIME-UNKNOWN**.

No runtime success is credited yet.

### Additional static finding

The corpus contains a rule writing `phase1-outpost-cap` into `desired-number-docks`; this is a likely destination-symbol defect and requires exact rule-level confirmation before correction.

### Contract

```text
phase state
  → phase transition detection
  → phase policy projection
  → downstream desired/upgrade goals
```

Byzantine policy must not assume these goals are stable until the phase projection lifecycle is understood.

---

## 3. `general.per`

### Role

Explorer policy, search preparation, object filtering, group/search control, and difficulty parameter initialization.

### Inputs

- desired explorer goals
- `villager-count`
- search/object data
- root working Goals including `local-total` and `temporary-goal`

### Outputs

- explorer-related Strategic Numbers
- search/group state
- difficulty parameters

### Important execution pattern

The root provides `local-total`, `local-last`, `remote-total`, and `remote-last` as contiguous working Goals. `general.per` consumes `local-total` through `up-get-search-state` and iterates using `temporary-goal`.

### Scratch-state contract

Static tracing shows `temporary-goal` is reused for separate local operations. Under the current module load order, each identified producer/consumer sequence remains internally ordered.

**Current classification:** SAFE REUSE under preserved load order, not globally collision-free.

### Restriction

New Byzantine code must not use `temporary-goal` as shared scratch state.

### Contract

```text
phase desired explorer policy
  → SN projection
  → search construction/filtering
  → group/object action
```

---

## 4. `market.per`

### Role

Reactive market/resource exchange.

### Inputs

- age/resource state
- market feasibility conditions
- existing resource thresholds

### Outputs

- market buy/sell requests

### Contract

```text
resource state
  → market feasibility
  → buy/sell request
```

The study must distinguish the market request from the actual resulting resource balance.

### Status

**STATICALLY UNDERSTOOD; COMPLETION SEMANTICS OPEN.**

---

## 5. `economy.per`

### Role

Civilian allocation and civilian production/resource behavior.

### Inputs

- `desired-*` economy goals
- `villager-count`
- drop-site distance goals
- resource availability
- feasibility conditions
- cheat configuration where enabled

### Outputs

- gatherer allocation Strategic Numbers
- drop-site Strategic Numbers
- villager/fishing/trade production requests
- cheat-resource actions where enabled

### Timing

Several projection rules use `(true)`, so their writes are unconditional when their rule remains active.

### Important consequence

A Byzantine layer cannot safely override a policy Goal that a later or repeatedly firing phase rule will overwrite without first establishing ownership and timing.

### Contract

```text
phase desired economy policy
  → gatherer allocation
  → civilian production/resource actions
  → reassessment
```

### Status

**STATICALLY MAPPED; ACTION COMPLETION OPEN.**

---

## 6. `technologies.per`

### Role

Research policy and escrow/resource authority.

### Inputs

- `upgrade-*` goals
- age state
- villager counts
- `desired-age`
- `desired-ageup-villagers`
- `can-research-with-escrow`
- escrow state
- specific unit counts

### Outputs

- research requests
- escrow release
- escrow percentage changes

### Important correction

The current static trace does **not** support a blanket replacement of `unit-type-count` with `unit-type-count-total`.

The infantry and archer upgrade chains check the specific unit type to which the upgrade applies. For example, the Long Swordsman rule checks Men-at-Arms rather than the original Militiaman type. That preserves the intended progression after each upgrade changes the unit's type.

**Classification:** DISPROVEN — the blanket replacement claim is not supported and is contradicted by the rule-by-rule trace.

### Contract

```text
upgrade policy
  → prerequisite/escrow feasibility
  → research request
  → technology state change
  → next upgrade eligibility
```

The actual research-completion transition still requires lifecycle evidence.

---

## 7. `construction.per`

### Role

Building target reconciliation, placement, and construction requests.

### Inputs

- desired building counts
- villager/search state
- resource/drop-site conditions
- pending object/placement conditions
- build feasibility
- scratch Goals

### Outputs

- `build <building>` requests
- `up-build-line`
- placement/reset actions
- town-size/town-placement Strategic Number changes

### State

The module uses several scratch Goals and search-state variables. Its farm-placement logic depends on rule ordering and control-flow jumps.

### Hazard

Negative `up-jump-rule` control flow and search-state persistence are maintainability/ordering hazards. They are not, by themselves, proof that the algorithm is incorrect.

### Contract

```text
desired building requirement
  → candidate location/search
  → build feasibility
  → placement
  → build request
  → pending/world-state evidence
```

Completion must not be inferred merely from `build` being issued.

---

## 8. `militaryUnits.per`

### Role

Military unit production.

### Inputs

- `desired-number-*` unit goals
- civilization-specific conditions
- `can-train`
- unit-line and unit identity constants

### Outputs

- `train <unit>` requests

### Important behavior

The module consumes desired counts rather than owning the strategic decision that produced them. This makes it a natural execution boundary for a later Byzantine policy layer — provided ownership and timing of those desired goals are made explicit.

### Unique-unit issue

Only some civilization-specific unique-unit branches are explicitly present in the inspected module. Other civilizations may fall through to the generic unique-unit-line path. The exact engine semantics of that fallback require confirmation before relying on it for Byzantine Cataphracts.

### Contract

```text
desired unit requirement
  → train feasibility
  → train request
  → queue/pending state
  → spawned unit/world transition
  → reassess requirement
```

The final three stages are not automatically proven by the training command.

---

## 9. `militaryBehavior.per`

### Role

Military grouping, target selection, attack timing, and attack-control behavior.

### Inputs

- military spread/attack goals
- target player state
- enemy-building count
- player-in-game/stance state
- timers
- military state

### Outputs

- military-control Strategic Numbers
- target-player state
- wall-targeting state
- attack percentage/timing behavior
- grouping/search actions

### Scratch-state pattern

`temporary-goal` is written from the target-player Strategic Number and subsequently read back. Static ordering inside the module preserves the intended sequence.

### Contract

```text
military policy/state
  → target selection/grouping
  → attack authorization/timing
  → military control
  → reassessment
```

The study must not treat attack authorization as proof of tactical success.

---

## 10. Cross-module contract

The principal current dependency is:

```text
AiBuilder.per
   │
   ├── Goal/SN/timer state
   │
   └── load order
          │
          ▼
   phaseUpdate
          │
          ├── desired economy/building/military goals
          └── upgrade policy
                │
        ┌───────┼────────┬────────────┐
        ▼       ▼        ▼            ▼
     economy construction tech    militaryUnits
        │       │        │            │
        └───────┴────────┴────────────┘
                        │
                        ▼
                     engine
                        │
                        ▼
                 world-state change
```

This is a **policy-to-execution** architecture. It is not yet an evidence-complete lifecycle architecture.

## 11. Byzantine extension rule

Until this contract is further qualified, Byzantine work may:

- study and document existing policy inputs;
- identify candidate policy insertion points;
- propose new state with an explicit ownership/ABI plan;
- trace existing AiBuilder behavior;
- prepare static vertical-slice designs.

Byzantine work may not yet:

- invent new primitives;
- invent timer IDs;
- assume symbolic Goal names allocate safely;
- globally replace existing primitives;
- duplicate the production system;
- claim an engine action succeeded because its command was issued;
- treat unconfirmed enemy-observation syntax as established;
- promote strategy thresholds to reverse-engineering facts.

## 12. Qualification gates

### Gate A — Static substrate integrity

Required:

- complete Goal inventory
- complete SN writer/reader matrix
- complete timer inventory
- multi-Goal width/span audit
- unresolved-symbol audit
- duplicate/conflicting allocation audit
- module load-order dependency audit

### Gate B — Representative execution slice

At least one representative path must be traced from:

`policy → feasibility → request → engine acceptance/pending → world transition → attribution → reassessment`

The first candidate is **Cataphract/unique-unit production**.

No broad Byzantine policy layer should be considered promotion-ready until these gates produce a defensible contract.
