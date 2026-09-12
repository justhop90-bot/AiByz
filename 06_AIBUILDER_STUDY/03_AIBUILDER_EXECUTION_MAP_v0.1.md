# AiBuilder Execution Map v0.1

**Status:** STUDY BASELINE — canonical working map for AiByzBuilder
**Scope:** Original `AiBuilder.per` + `AiBuilder/` corpus, interpreted against the AoE2 AI Scripting Encyclopedia.

## Purpose

This document maps AiBuilder from source composition through generated `.per`, rule evaluation, Goals/Strategic Numbers/timers, engine-facing requests, world-state change, and reassessment.

It is intentionally an AiBuilder document. It does not import AEGIS architecture or policy assumptions.

## 1. Canonical pipeline

```text
AiBuilder configuration/source
        ↓
AiBuilder.per composition root
        ↓
constants / Goals / timers / initial state / load order
        ↓
loaded Builder modules
        ↓
rule evaluation against native facts/state
        ↓
policy/state mutation
   (Goals / Strategic Numbers / timers / rule control)
        ↓
feasibility gates
        ↓
engine-facing request
   (train / build / research / buy / control)
        ↓
engine acceptance / pending state
        ↓
world-state transition
        ↓
new native facts / counts / state
        ↓
subsequent rule evaluation
        ↓
reassessment
```

The first four stages are strongly represented by the current source corpus. The distinction between request, pending state, and world transition is a study requirement; a command being issued is not completion evidence.

## 2. Source composition

`AiBuilder.per` is the composition root. Current source-map evidence identifies these responsibilities:

- phase configuration
- `constantsUP` loading
- Goal allocation
- working-state allocation
- timer allocation
- Strategic Number initialization
- map/position/time/villager observations
- building-system initialization
- module load order
- post-load customization

Current load order:

```text
AiBuilder/constantsUP
AiBuilder/phaseUpdate
AiBuilder/general
AiBuilder/market
AiBuilder/economy
AiBuilder/technologies
AiBuilder/construction
AiBuilder/militaryUnits
AiBuilder/militaryBehavior
```

Preserve this ordering unless a dependency audit proves a change safe.

## 3. Role of each module

| Module | Functional role | Main state relationship |
|---|---|---|
| `constantsUP.per` | symbolic engine/object/research definitions | foundational vocabulary |
| `phaseUpdate.per` | phase transition + policy projection | major Goal writer |
| `general.per` | exploration/search/group behavior | consumes explorer/search state |
| `market.per` | reactive market exchange | reads native resource/market state |
| `economy.per` | civilian allocation/production/resource behavior | consumes economy Goals/SNs |
| `technologies.per` | age/research/escrow behavior | consumes upgrade/age policy |
| `construction.per` | building/farm/drop-site execution | consumes building targets + search state |
| `militaryUnits.per` | military production | consumes desired unit Goals |
| `militaryBehavior.per` | grouping/targeting/attack behavior | consumes military policy/state |

## 4. Policy projection

The Builder's principal policy producer is `phaseUpdate.per`.

Representative flow:

```text
phase state/configuration
        ↓
phaseUpdate rules
        ↓
desired-* / upgrade-* Goals
        ↓
consumer module
```

Examples:

```text
desired-number-skirmishers → militaryUnits.per
desired-number-ranges      → construction.per
desired-number-villagers   → economy.per
desired-age                → technologies.per
land-attack-*              → militaryBehavior.per
```

The current ABI inventory records Goals 1–121 as explicitly allocated policy/state channels, including Goal 57 `desired-number-skirmishers`.

## 5. Rule evaluation model

A Builder rule should be traced as:

```text
facts/state read
      ↓
condition evaluation
      ↓
eligible?
  ├── no  → no consequent
  └── yes → consequent(s)
              ↓
       state mutation and/or
       engine-facing request
```

Do not infer runtime semantics from a symbol name alone. The Encyclopedia establishes command syntax and parameter typing; the Builder source establishes how those primitives are actually composed.

## 6. Goals as Builder control channels

The current root establishes two major Goal regions.

### Policy/state Goals 1–121

These carry phase-projected desired counts, upgrade policy, attack policy, economy controls, and related state.

### Working Goals 480–510

The root establishes search/geometry/time/scratch state including:

```text
point-x / point-y
point2-x / point2-y
point3-x / point3-y
position-self-x / position-self-y
gl-game-time
spread-units
villager-count
local-total / local-last
remote-total / remote-last
temporary-goal...
```

These working Goals are part of the existing Builder ABI. New code must not assume an apparently unused slot is safe without an allocation audit.

## 7. Strategic Numbers

Strategic Numbers are a separate native control channel from Goals.

The Builder uses them for behavioral parameters such as gatherer percentages, explorer behavior, distances, military spread, and related execution controls.

For each SN, the required study record is:

```text
SN name
→ writer rule/module
→ reader rule/module
→ condition
→ timing
→ downstream effect
→ runtime qualification status
```

The repository does not assign local numeric IDs to these symbolic SN names unless the engine/source explicitly establishes them.

## 8. Timers

The root explicitly allocates:

```text
town-size-timer       1
unit-spread-timer      2
cheat-timer            3
land-attack-timer      4
naval-attack-timer     5
```

A timer allocation in the root is direct source evidence. It is not permission to invent additional timer IDs.

## 9. Representative production path

The cleanest Builder execution slice currently identified is military unit production.

```text
phaseUpdate.per
      ↓
Goal 57: desired-number-skirmishers
      ↓
militaryUnits.per
      ↓
current unit-count evaluation
      ↓
production feasibility (`can-train` and related conditions)
      ↓
`train skirmisher-line`
      ↓
engine queue/processing
      ↓
unit exists in world state
      ↓
unit count changes
      ↓
production rule reevaluates
```

The final three stages must be distinguished during qualification. `train` proves an engine-facing request was issued, not by itself that a unit spawned or that the strategic objective was achieved.

## 10. Construction path

```text
desired building Goal
      ↓
construction.per
      ↓
search / candidate location
      ↓
placement and feasibility
      ↓
`build <building>`
      ↓
pending/building state
      ↓
completed building
      ↓
new building count/state
      ↓
reassessment
```

Search-state and rule-order dependencies are part of this path and must be preserved unless explicitly qualified.

## 11. Technology path

```text
upgrade-* / desired-age
      ↓
technologies.per
      ↓
prerequisites + villager/resource conditions
      ↓
escrow / research feasibility
      ↓
research request
      ↓
technology transition
      ↓
new technology/unit eligibility
      ↓
reassessment
```

The current study specifically rejects a blanket replacement of specific `unit-type-count` logic with total-count logic. Upgrade prerequisites must be traced rule by rule.

## 12. Economy path

```text
desired economy Goals
      ↓
economy.per
      ↓
Strategic Number projection
      ↓
gatherer / civilian production behavior
      ↓
resource and production requests
      ↓
world/resource state
      ↓
reassessment
```

Market behavior is a related but distinct path:

```text
resource/market state
      ↓
market feasibility
      ↓
buy/sell request
      ↓
resource state
      ↓
reassessment
```

## 13. Military behavior path

```text
military policy/state
      ↓
militaryBehavior.per
      ↓
target/group/search preparation
      ↓
attack timing/authorization
      ↓
engine military-control request
      ↓
combat/world transition
      ↓
updated military state
      ↓
reassessment
```

Attack authorization must never be treated as proof of tactical success.

## 14. The feedback loop

AiBuilder is not accurately represented as a one-way compiler followed by one-time execution. Its generated rules participate in a continuing rule-evaluation loop:

```text
WORLD
  ↓
native facts/state
  ↓
RULE EVALUATION
  ↓
GOAL / SN / TIMER STATE
  ↓
FEASIBILITY
  ↓
ENGINE REQUEST
  ↓
WORLD CHANGE
  ↓
NATIVE FACTS/STATE CHANGE
  └────────────────────────→ RULE EVALUATION
```

This loop is the core object of AiByzBuilder study.

## 15. Evidence boundary

The Encyclopedia is authoritative for documented command language and parameter concepts, but it does not replace analysis of the Builder corpus.

The following distinctions remain mandatory:

- source presence ≠ complete runtime semantics;
- valid syntax ≠ positive world observation;
- rule firing ≠ successful strategic result;
- engine request ≠ completion;
- completion ≠ strategic success;
- Goal allocation ≠ safe ownership for arbitrary new code;
- symbolic name ≠ proof of engine behavior in every context.

## 16. AiByzBuilder design consequence

AiByzBuilder should initially be treated as an extension of the **functional Builder pipeline**, not as an unrelated AI architecture:

```text
AiBuilder native substrate
        ↓
understood policy/control channels
        ↓
Byzantine-specific policy generation
        ↓
existing Builder execution modules
        ↓
engine
```

The first implementation objective is therefore to preserve the proven Builder execution machinery while expanding the quality of the policy decisions that feed it.

No new architecture should be promoted merely because it is cleaner in abstract terms. It must demonstrate compatibility with the Builder's existing Goals, SNs, timers, rule evaluation, load order, and engine-facing action contracts.

## 17. Next required research

Build the rule-level execution graph for one complete representative path, preferably:

```text
Goal 57
→ militaryUnits.per
→ skirmisher feasibility
→ train request
→ queue/pending evidence
→ spawned unit
→ count change
→ rule reassessment
```

Then replicate the same tracing method for construction, research, economy, and military behavior.

This document is the canonical map; detailed findings belong in the supporting study documents rather than being silently inferred here.
