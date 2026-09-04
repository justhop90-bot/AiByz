# C1 — Threat → Capability Strategic Transition Specification
## Cavalry / Cavalry-Archer Threat → Camel Capability

**Date:** 2026-09-04  
**Mission:** Layer 2 historical HD/Promisory archaeology  
**Status:** C1-SPEC v1 — evidence-backed, implementation not yet authorized  
**Evidence posture:** Historical mechanisms are separated from AEGIS generalization.  
**Primary authority:** Local AoE2DE Promisory source and local game data inspected on Weebo.

---

## 1. Executive finding

The local game files support a real historical control chain in which enemy military composition is measured, compressed into strategic state, and consumed by production logic that can authorize camel production when the contextual conditions are satisfied.

The defensible chain is:

```text
ENEMY OBSERVATION
    ↓
CAVALRY / CAVALRY-ARCHER THREAT STATE
    ↓
CONTEXTUAL RESPONSE LOGIC
    ↓
CAMEL PRODUCTION CANDIDATE
    ↓
PRODUCTION FEASIBILITY
    ↓
TRAIN CAMEL
```

This is **DIRECT / CONFIRMED** at the mechanism level where the individual source files establish the links. It does **not** establish that the historical AI was solving a general counter-composition optimization problem, nor that every camel production event was strategically successful in a particular game.

The historical system is therefore best described as a **threat-triggered capability response**, not a universal optimizer.

---

## 2. Exact transition contract

### OBSERVATION

The threat subsystem measures opponent military composition, including cavalry and cavalry-archer-related categories. The relevant evidence is in:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\Promisory\threats.per`

The subsystem also establishes a focus-opponent mechanism before threat measurements are consumed. This means the response is not simply a global unit-count lookup; it is mediated by opponent/context state.

**Grade:** DIRECT / CONFIRMED / HISTORICAL.

### BELIEF

The historical program does not appear to maintain a modern probabilistic belief object. Instead, measured facts are compressed into goals/strategic numbers/flags that subsequent rules consume.

AEGIS interpretation:

```text
measurement → compressed belief/state
```

**Grade:** DIRECT for state compression; AEGIS-GENERALIZATION for the word “belief.”

### THREAT VECTOR

Relevant vector:

```text
enemy cavalry
enemy cavalry-archer pressure
        ↓
mobile mounted threat
        ↓
need for an appropriate mounted counter-capability
```

The source supports cavalry/cavalry-archer threat categories and a camel response path. It does not prove that the programmer explicitly named the abstract threat “mobile mounted threat.” That aggregation is AEGIS terminology.

**Grade:** COMPOSED / CONFIRMED for the concrete categories; AEGIS-GENERALIZATION for the aggregate vector.

### STRATEGIC OBJECTIVE

Concrete historical objective:

```text
increase access to camel counter-capability when the contextual threat logic calls for it.
```

Do not rewrite this as “maximize anti-cavalry efficiency.” That would exceed the evidence.

**Grade:** COMPOSED / PROBABLE.

### REQUIRED CAPABILITY

The required capability is the camel line, represented in the current game data by the camel-line family.

Local `unitlines.json` identifies the camel line as a family containing unit IDs including 329 and 330.

Local parsed game data further identifies:

- **329:** camel-line unit; internal name `CVLRY`
- **330:** camel-line unit; internal name `HCLRY`

The Byzantine civ data is present in the current AoE2DE data set and exposes these units to the Byzantine civilization record.

**Grade:** DIRECT / CONFIRMED / ENGINE-SPECIFIC.

### CANDIDATE SET

Historical implementation is narrower than a modern candidate generator. The relevant production response is specifically camel production rather than a general enumeration of every possible anti-cavalry response.

AEGIS candidate set for the transition should nevertheless be explicit:

```text
C = {
    Camel Rider,
    Heavy Camel Rider,
    alternative counter-capabilities only if separately qualified
}
```

The second line is a design extension; historical evidence directly establishes the camel path, not this complete candidate set.

**Historical candidate:** DIRECT.  
**AEGIS candidate expansion:** AEGIS-GENERALIZATION.

### HARD CONSTRAINTS

A camel action cannot be committed merely because a threat is observed. The historical production path contains feasibility/authorization conditions before the side effect.

The relevant implementation is in:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\Promisory\units.per`

The production side effect is guarded by contextual state and production feasibility machinery.

At minimum, the AEGIS transition contract must treat these as hard constraints:

1. target civilization must have the camel capability;
2. required production infrastructure must exist/be usable;
3. unit must be currently trainable;
4. resource/escrow conditions must permit the action;
5. the strategic state must still authorize the response when the production rule fires.

The first three are engine/game constraints. The fifth is an AEGIS architectural requirement. Escrow/resource reservation is historically demonstrated as a general mechanism but should not be falsely attributed to every individual camel rule unless the exact path proves it.

### SOFT SCORE

No evidence currently proves that the historical camel rule computes a continuous utility score among camel alternatives.

Therefore:

```text
Historical soft score: NOT ESTABLISHED.
AEGIS soft score: REQUIRED for generalized candidate evaluation.
```

For AEGIS, a candidate score should eventually consider:

```text
threat coverage
resource burden
production burden
timing
current mass
survivability / tactical fit
map / mobility value
optionality
commitment cost
```

This is new AEGIS architecture, not historical reconstruction.

### RESOURCE COST

The current local AoE2DE data was parsed directly from:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\dat\empires2_x2_p1.dat`

For the Byzantine civ record:

| Unit ID | Internal name | Food | Gold | Train time |
|---:|---|---:|---:|---:|
| 329 | CVLRY | 55 | 60 | 22 s |
| 330 | HCLRY | 55 | 60 | 22 s |

Both use the same recorded resource-cost tuple in the local game data: 55 food + 60 gold, plus the engine's standard creatable/train metadata. The local parsed data associates their train location with unit/building ID 101.

These are **game-data facts**, not historical strategic interpretation.

### PRODUCTION COST

The production cost is not merely the unit's resource price. AEGIS must account for:

```text
unit resources
+ production-slot occupancy
+ infrastructure opportunity cost
+ time to field
+ future reinforcement burden
```

Only the first component and the recorded training time are directly available from the local unit data in this pass. The full opportunity-cost model is AEGIS design.

### TIMING

The historical system uses strategic state and rule eligibility rather than a single explicit “respond within N seconds” contract.

AEGIS should represent timing as:

```text
threat detection time
→ authorization time
→ first production time
→ fielding time
→ reassessment deadline
```

The 22-second train time in the local unit data is a concrete lower-level production timing parameter, not a strategic deadline.

### POSITION

The response must be evaluated against where the threat is exerting pressure. Historical position/state machinery exists elsewhere in Promisory, but this pass does not establish a direct position dependency inside the camel authorization rule itself.

**Disposition:** preserve as a downstream AEGIS constraint, not retroactively claim it as part of the historical camel trigger.

### RISK

Historical source proves conditional production logic, but does not directly expose a scalar risk calculation for the camel response.

AEGIS risk model should include:

- resource lock-up,
- delayed technology,
- insufficient existing military mass,
- threat misclassification,
- counter-composition change,
- production bottleneck,
- map/position mismatch.

**Grade:** AEGIS-GENERALIZATION.

### OPTIONALITY

No direct historical optionality metric was found in this pass.

AEGIS must explicitly model whether committing resources to camels closes important alternatives. This is especially important because the historical rule engine is capable of using escrow/resource-control mechanisms, but that does not prove a modern opportunity-cost calculation.

### COMMITMENT

Historical camel production is an action authorization, not yet proven to be a persistent strategic commitment object.

AEGIS therefore must add explicit commitment semantics:

```text
ACTIVATE
→ minimum persistence
→ monitor threat
→ invalidate if threat disappears / capability becomes obsolete
→ replace or reinforce if superior response emerges
```

This is AEGIS-GENERALIZATION.

### AUTHORITY

The important historical architectural boundary is:

```text
contextual state
→ production authorization
→ feasibility
→ side-effect
```

The production action should not be treated as equivalent to desire. AEGIS preserves this distinction:

```text
DESIRE
→ CAN-FACT
→ AUTHORITY
→ SIDE EFFECT
→ WORLD OBSERVATION
```

### ACTION

Historical action:

```text
traincamel
```

The relevant consumer is in `Promisory\units.per`.

### VERIFICATION

Historical source demonstrates command issuance, not guaranteed world-state success.

AEGIS verification must therefore wait for an observable postcondition:

```text
production queue accepted
→ unit lifecycle evidence
→ fielded camel capability
```

The replay interpreter's current invariant must remain in force: DE_QUEUE is not equivalent to spawned-unit identity without sufficient evidence.

### FAILURE SIGNATURE

Possible failures:

1. production authorization fires but no trainable infrastructure exists;
2. resource state changes before the intended production side effect;
3. queue is unavailable/full;
4. threat changes before fielding;
5. enemy transitions away from cavalry;
6. camel response is insufficient against the actual composition;
7. inferred production success cannot be proven from replay evidence.

Only some of these are directly demonstrated by historical machinery. The complete list is an AEGIS failure contract.

### RECOVERY

Historical Promisory demonstrates broader fallback/recovery patterns, including explicit building rebuild fallback and attack retreat/restart lifecycle. It does not yet prove a camel-specific recovery controller.

AEGIS response:

```text
camel commitment fails
→ classify failure
→ preserve useful resources if possible
→ remeasure threat
→ regenerate candidate set
→ choose replacement capability
```

### REASSESSMENT

The transition is not complete at the train command.

Required AEGIS closure:

```text
OBSERVE
→ CLASSIFY
→ AUTHORIZE
→ PRODUCE
→ VERIFY
→ REASSESS
```

This matches the strongest repeated historical motif identified in the Layer-2 archaeology: **measure → compress into state → guard side effect → transition/reset → re-enter controller**.

---

## 3. Historical causal-edge ledger

| Edge | Evidence | Grade | Boundary |
|---|---|---|---|
| Enemy military composition → threat state | `Promisory\threats.per` | DIRECT / CONFIRMED | Historical control |
| Cavalry/cavalry-archer categories → contextual threat response | `Promisory\threats.per` | DIRECT / CONFIRMED | Historical control |
| Contextual state → camel production logic | `Promisory\units.per` | DIRECT / CONFIRMED | Historical control |
| Camel production logic → feasibility gate | `Promisory\units.per` | DIRECT / CONFIRMED | Historical control |
| Feasibility → traincamel side effect | `Promisory\units.per` | DIRECT / CONFIRMED | Historical control |
| Escrow → protected future production/research | `Promisory\escrow.per` | DIRECT / CONFIRMED | Historical mechanism |
| Camel line → unit IDs 329/330 | `_common\dat\unitlines.json` | DIRECT / CONFIRMED | Game data |
| Byzantine civ → camel unit availability | `_common\dat\CivTechTrees\BYZANTINES.json` + parsed DAT | DIRECT / CONFIRMED | Game data |
| Camel unit → 55F/60G/22s | parsed `empires2_x2_p1.dat` | DIRECT / CONFIRMED | Game data |
| Threat → “optimal counter” | none | NOT ESTABLISHED | Do not claim |
| Camel rule → strategic success | none | NOT ESTABLISHED | Requires replay evidence |
| Camel response → persistent commitment | none | NOT ESTABLISHED | AEGIS extension |
| Camel response → scalar utility score | none | NOT ESTABLISHED | AEGIS extension |

---

## 4. What the historical programmer appears to have built

The strongest reconstruction is not:

```text
IF enemy has X knights
THEN calculate mathematically optimal camel quantity.
```

It is closer to:

```text
MEASURE enemy composition
        ↓
STORE compressed strategic state
        ↓
RUN contextual response rules
        ↓
IF camel response is currently eligible
        ↓
CHECK production feasibility
        ↓
TRAIN CAMEL
```

This is an important distinction. The historical architecture is a **rule-mediated strategic controller**. It achieves strategic behavior through distributed state, gates, resource controls, timers, searches, and production consumers rather than through a single explicit planner.

---

## 5. AEGIS reconstruction

AEGIS should preserve the demonstrated control chain while making its latent strategic semantics explicit:

```text
WORLD
 ↓
OBSERVE
 ↓
CLASSIFY: mounted threat
 ↓
BELIEF: confidence / severity / trend
 ↓
REQUIREMENT: anti-mounted capability
 ↓
CANDIDATES: camel + qualified alternatives
 ↓
PROPAGATE CONSTRAINTS
 ↓
EVALUATE: cost / timing / risk / optionality
 ↓
COMMIT
 ↓
AUTHORIZE
 ↓
EXECUTE
 ↓
VERIFY
 ↓
REASSESS
```

This is **AEGIS-GENERALIZATION**, not a claim that Promisory literally implemented this object model.

---

## 6. Hard implementation rule

Do not implement the camel director yet.

Before coding, the next evidence pass must answer:

1. What exact threat-state variables feed `traincamel`?
2. Where are those variables initialized/reset?
3. Which rules can override or suppress camel production?
4. What exact feasibility predicates are used immediately before the side effect?
5. How does `camel-set` get established and consumed?
6. Does the historical controller prevent oscillation or repeated toggling?
7. Can replay evidence demonstrate a complete threat → camel transition in an actual HD bot game?

Only after those questions are closed should the AEGIS C1 implementation contract be frozen.

---

## 7. Current disposition

**C1-SPEC v1: ACCEPTED as the historical control model, with explicit evidence boundaries.**

### Confirmed
- cavalry/cavalry-archer threat measurement exists;
- threat state feeds contextual response machinery;
- camel production exists as a consumer;
- production feasibility is checked before the side effect;
- camel-line IDs and Byzantine game-data properties are locally verified;
- resource/escrow control is a real historical mechanism.

### Not confirmed
- universal counter-composition optimization;
- scalar utility scoring;
- explicit persistent camel commitment;
- strategic success in a particular replay;
- exact programmer intent beyond the demonstrated control graph.

### Next highest-value target
**C1-A — Exact variable lineage audit:** trace every state variable read by `traincamel` backward to its writer, reset, initialization, and competing writers; then trace its production-side effects forward to verification/reassessment.

The purpose is to convert the current causal chain from “strongly demonstrated” into a complete executable lineage.
