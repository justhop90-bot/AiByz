# AEGIS Competency 5 — Production Authority Matrix

**Date:** 2026-09-12  
**Scope:** installed `AIByzBuild` corpus  
**Targets:** spearmen, skirmishers, archers, camelriders, monks, bombardcannons, fireships, uniqueunits  
**Purpose:** identify every current writer, its condition, structural precedence, executor, verification path, and the current authoritative-owner defect.

## Executive finding

The production executor is not the missing subsystem. `militaryUnits.per` already consumes the eight `desired-number-*` goals and invokes native `can-train` → `train` execution. The actual defect is **multiple policy writers share authority over the same desired goal**.

`phaseUpdate.per` writes all eight targets on phase transitions for five phases × three difficulty branches. `byzpolicy.per` then writes several of the same goals from age baselines, count deficits, local-defense observations, and AEGIS threat state. The root load order places `phaseUpdate` before `byzpolicy`, but this document does **not** promote that structural load order into a proven same-cycle rule-evaluation precedence. Therefore there is currently **no single formally authoritative writer** for most targets.

The required Competency-5 correction is an explicit authority hierarchy, not another training executor.

## Authority model

| Rank | Authority class | Current module | Meaning |
|---|---|---|---|
| P0 | Native executor | `militaryUnits.per` | Physical training only; never owns composition policy |
| P1 | Emergency / immediate defense | `byzpolicy.per` | Local attack / town-defense response |
| P2 | Fresh classified threat | `byzpolicy.per` | Threat-conditioned composition floor |
| P3 | Byzantine strategic baseline | `byzpolicy.per` | Age/counter portfolio |
| P4 | Phase baseline | `phaseUpdate.per` | Generic AiBuilder phase/difficulty target |

**Important:** P1–P4 are the intended authority hierarchy for the matrix, not an existing engine-enforced priority mechanism. Today the `.per` code contains multiple writers; precedence must be implemented or otherwise proven before calling this hierarchy runtime-authoritative.

## Common executor contract

For the seven directly mapped targets:

```text
policy writer
  ↓
set-goal desired-number-X
  ↓
militaryUnits.per
  ↓
unit-type-count-total X < desired-number-X
  ↓
can-train X
  ↓
train X
```

The `can-train` gate remains the native feasibility boundary: building availability, resources and other engine prerequisites are not duplicated in AEGIS. This matches the documented AoE2 scripting model. citeturn0search7turn0search11

---

# 1. Spearmen

### Writers

**Phase writer — `phaseUpdate.per`**

15 transition writers:

- Phase 1: easy / moderate / hard → `phase1-spearman-cap-*`
- Phase 2: easy / moderate / hard → `phase2-spearman-cap-*`
- Phase 3: easy / moderate / hard → `phase3-spearman-cap-*`
- Phase 4: easy / moderate / hard → `phase4-spearman-cap-*`
- Phase 5: easy / moderate / hard → `phase5-spearman-cap-*`

Every phase writer has:

```text
up-compare-goal current-phase g:!= previous-phase
AND
goal current-phase N
```

**Byzantine policy writers — `byzpolicy.per`**

| Condition | Write | Line |
|---|---:|---:|
| Feudal + spearman-line < 6 | 6 | 162 |
| Castle + spearman-line < 8 | 8 | 207 |
| Imperial + spearman-line < 20 | 20 | 264 |
| Feudal+ + ≥2 enemy units in town | 12 | 372 |
| Feudal+ + ≥1 enemy building in town | 12 | 380 |
| Feudal+ + ≥2 enemy knights in town | 18 | 392 |
| Feudal+ + AEGIS cavalry threat | 18 | 427 |
| Feudal+ + AEGIS under attack | 12 | 461 |

### Precedence

Intended: **under-attack > classified threat > local counter > age baseline > phase baseline**.

Actual: **not formally enforced**. Phase writers are transition-triggered; Byzantine writers can fire continuously. The file is loaded after `phaseUpdate`, but load order alone is not treated as proof of same-pass final-write semantics.

### Final owner

**UNRESOLVED / shared.** `byzpolicy.per` is documented as the intended Byzantine policy owner, but `phaseUpdate.per` remains an active writer.

### Executor

`militaryUnits.per`:

```text
unit-type-count-total spearman-line g:< desired-number-spearmen
can-train spearman-line
→ train spearman-line
```

### Verification

- Goal state: `desired-number-spearmen` equals the winning policy target.
- Production demand: `unit-type-count-total spearman-line` reaches/exceeds target.
- Physical execution: `train spearman-line` accepted only when `can-train` is true.
- Upgrade continuity: existing technology path promotes the line through Pike/Halberdier.

---

# 2. Skirmishers

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-skirmisher-cap-*`.

**ByzPolicy:**

| Condition | Write | Line |
|---|---:|---:|
| Feudal + skirmisher-line < 8 | 8 | 156 |
| Castle + skirmisher-line < 10 | 10 | 201 |
| Imperial + skirmisher-line < 20 | 20 | 270 |
| Feudal+ + ≥2 enemy units in town | 12 | 373 |
| Feudal+ + ≥1 enemy building in town | 12 | 381 |
| Feudal+ + ≥3 enemy archers in town | 18 | 399 |
| Feudal+ + AEGIS archer threat | 18 | 437 |
| Feudal+ + AEGIS under attack | 12 | 462 |

### Precedence

Intended: **under-attack > archer threat > local archer counter > local defense > age baseline > phase baseline**. Not currently engine-enforced.

### Final owner

**UNRESOLVED / shared; intended owner `byzpolicy.per`.**

### Executor

`militaryUnits.per`:

```text
unit-type-count-total skirmisher-line g:< desired-number-skirmishers
can-train skirmisher-line
→ train skirmisher-line
```

### Verification

Count-total reaches target; native `can-train` gates execution. Existing technology path can promote to Elite Skirmisher.

---

# 3. Archers

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-archer-cap-*`.

**ByzPolicy:**

| Condition | Write | Line |
|---|---:|---:|
| Feudal + archer-line < 10 | 10 | 146 |
| Castle + archer-line < 12 | 12 | 176 |
| Imperial + archer-line < 16 | 16 | 228 |
| Feudal+ + ≥3 enemy skirmishers in town | 18 | 405 |
| Feudal+ + AEGIS infantry threat | 18 | 445 |

### Precedence

Intended: **threat-conditioned ranged requirement > local counter > age baseline > phase baseline**. Not formally enforced.

### Final owner

**UNRESOLVED / shared; intended owner `byzpolicy.per`.**

### Executor

`militaryUnits.per`:

```text
unit-type-count-total archer-line g:< desired-number-archers
can-train archer-line
→ train archer-line
```

### Verification

Count-total reaches target; native `can-train` gates production. Existing research path supports Crossbow/Arbalest progression.

---

# 4. Camel Riders

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-camelrider-cap-*`.

**ByzPolicy:**

| Condition | Write | Line |
|---|---:|---:|
| Castle + camel-line < 10 | 10 | 213 |
| Imperial + camel-line < 4 | 4 | 276 |
| Feudal+ + ≥2 enemy knights in town | 8 | 393 |
| Feudal+ + AEGIS cavalry threat | 8 | 428 |

### Precedence

Intended: **cavalry threat/local counter > age baseline > phase baseline**. Not formally enforced.

### Final owner

**UNRESOLVED / shared; intended owner `byzpolicy.per`.**

### Executor

`militaryUnits.per`:

```text
unit-type-count-total camel-line g:< desired-number-camelriders
can-train camel-line
→ train camel-line
```

### Verification

Count-total reaches target; `can-train camel-line` gates actual training. Existing technology path can research Heavy Camel where applicable.

---

# 5. Monks

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-monk-cap-*`.

**ByzPolicy:**

| Condition | Write | Line |
|---|---:|---:|
| Castle + monk-set < 3 | 3 | 182 |
| Imperial + monk-set < 5 | 5 | 240 |

### Precedence

Intended: **age baseline > phase baseline**. There is currently no emergency/threat writer for monks.

### Final owner

**UNRESOLVED / shared.** `byzpolicy.per` is intended to own Byzantine monk composition; `phaseUpdate.per` remains an active writer.

### Executor

`militaryUnits.per`:

```text
unit-type-count-total monk-set g:< desired-number-monks
can-train monk
→ train monk
```

### Verification

`monk-set` reaches/exceeds desired target; `can-train monk` confirms executable production.

---

# 6. Bombard Cannons

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-bombardcannon-cap-*`.

**ByzPolicy:**

| Condition | Write | Line |
|---|---:|---:|
| Imperial + bombard-cannon < 3 | 3 | 234 |

There is also a capacity writer:

```text
Imperial + desired-number-bombardcannons >= 1
→ desired-number-workshops = 2
```

line 468.

### Precedence

Intended: **Imperial Byzantine siege baseline > phase baseline**. No threat-conditioned bombard writer exists in the current matrix.

### Final owner

**UNRESOLVED / shared; intended owner `byzpolicy.per`.**

### Executor

`militaryUnits.per`:

```text
unit-type-count-total bombard-cannon g:< desired-number-bombardcannons
can-train bombard-cannon
→ train bombard-cannon
```

### Verification

Count-total reaches target; native `can-train` is the execution feasibility gate; workshop capacity is separately requested through the construction goal.

---

# 7. Fireships

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-fireship-cap-*`.

**ByzPolicy:**

| Condition | Write | Line |
|---|---:|---:|
| Feudal+ + AEGIS threat source classified as `warship-class` | 6 | 453 |

The same rule writes `desired-number-docks = 2`.

### Precedence

Intended: **warship threat > phase baseline**. No Byzantine age baseline writer currently exists in `byzpolicy.per`.

### Final owner

**UNRESOLVED / shared; intended owner `byzpolicy.per` when naval threat exists.**

### Executor

`militaryUnits.per`:

```text
unit-type-count-total fire-ship-line g:< desired-number-fireships
can-train fire-ship-line
→ train fire-ship-line
```

### Verification

Count-total reaches target; `can-train fire-ship-line` gates execution; dock capacity must be available through the construction subsystem.

---

# 8. Byzantine Unique Units / Cataphracts

### Writers

**PhaseUpdate:** 15 phase/difficulty transition writers using `phaseN-uniqueunit-cap-*`.

**ByzPolicy age writers:**

| Condition | Write | Line |
|---|---:|---:|
| Dark Age | 0 | 295 |
| Feudal Age | 0 | 302 |
| Castle Age | 6 | 309 |
| Imperial Age | 10 | 318 |

**ByzPolicy deficit writers:**

| Condition | Write | Line |
|---|---:|---:|
| Castle + `my-unique-unit-line < 6` | 6 | 341 |
| Imperial + `my-unique-unit-line < 10` | 10 | 347 |

### Precedence

Intended: **age/unique-unit portfolio > phase baseline**. The deficit writers repeat the same targets as the age writers and therefore do not currently create a distinct higher-priority response.

### Final owner

**UNRESOLVED / shared; intended owner `byzpolicy.per`.**

### Executor

`militaryUnits.per` provides the generic path:

```text
unit-type-count-total my-unique-unit-line g:< desired-number-uniqueunits
can-train my-unique-unit-line
→ train my-unique-unit-line
```

There are explicit civilization branches for Gothic, Hun and Bulgarian unique units; the generic path is used otherwise. The Byzantine-specific Cataphract resolution is therefore **engine/alias dependent rather than proven by a Byzantine-specific train rule in this file**.

### Verification

- Goal target reached through `my-unique-unit-line` count.
- `can-train my-unique-unit-line` must succeed.
- Byzantine Cataphract identity requires separate explicit qualification.
- Existing upgrade path uses `my-unique-unit-upgrade`; Elite Cataphract resolution likewise requires explicit qualification.

---

# Cross-target writer inventory

| Target | PhaseUpdate writers | Byzantine policy writers | Emergency/threat writers | Executor | Current authoritative owner |
|---|---:|---:|---:|---|---|
| Spearmen | 15 | 3 baseline + 5 response | Yes | `spearman-line` | **Shared / unresolved** |
| Skirmishers | 15 | 3 baseline + 5 response | Yes | `skirmisher-line` | **Shared / unresolved** |
| Archers | 15 | 3 baseline + 2 response | Yes | `archer-line` | **Shared / unresolved** |
| Camel Riders | 15 | 2 baseline + 2 response | Yes | `camel-line` | **Shared / unresolved** |
| Monks | 15 | 2 baseline | No | `monk` | **Shared / unresolved** |
| Bombard Cannons | 15 | 1 baseline | No | `bombard-cannon` | **Shared / unresolved** |
| Fireships | 15 | 1 response | Yes | `fire-ship-line` | **Shared / unresolved** |
| Unique Units | 15 | 4 age + 2 deficit | No | `my-unique-unit-line` | **Shared / unresolved** |

## Critical result

The earlier claim that `byzpolicy.per` already owns composition is **not true at the authority level**. It owns a large subset of composition decisions, but `phaseUpdate.per` is still a live writer for every target.

This is not necessarily a bug: phaseUpdate provides a legitimate generic baseline. The defect is that the system currently lacks an explicit arbitration contract saying which writer wins when multiple rules can write the same goal.

## Required Competency-5 authority contract

The desired end state is:

```text
PHASE BASELINE
     ↓
BYZANTINE BASELINE
     ↓
LOCAL COUNTER
     ↓
FRESH THREAT RESPONSE
     ↓
IMMEDIATE DEFENSE
     ↓
FINAL COMPOSITION TARGET
     ↓
AiBuilder executor
```

But this hierarchy must be implemented with an actual `.per` mechanism or otherwise proven through engine semantics. It must not exist only in documentation.

## Forbidden shortcut

Do **not** solve the conflict by simply moving all Byzantine rules below phaseUpdate or by relying on textual file order. That would still leave multiple writers and would make authority accidental.

The correct next design is a **single composition-authority write point** or an equivalent monotonic-floor mechanism where each policy layer contributes a requirement and one final writer emits `desired-number-*`.

## Verification contract

For every target, qualification must distinguish:

1. **Policy evidence:** which rule established the final target.
2. **Goal evidence:** the resulting `desired-number-*` value.
3. **Executor evidence:** `unit-type-count-total < desired-number-*` became true.
4. **Feasibility evidence:** `can-train X` became true.
5. **Command evidence:** `train X` was accepted.
6. **World evidence:** unit count/state actually increased.
7. **Persistence evidence:** target remains governed after subsequent policy passes.
8. **Expiry/recovery evidence:** temporary threat target disappears when its source state expires and the baseline becomes authoritative again.

The project must not treat **command accepted** as equivalent to **world transition completed**.

## Status

**Production executor:** substantially confirmed for the eight selected targets, with unique-unit Byzantine resolution conditional.  
**Production authority:** **NOT QUALIFIED**.  
**Primary defect:** multiple active writers to the same desired goals.  
**Next implementation milestone:** consolidate composition authority without replacing `militaryUnits.per`.

## Source note

The native AoE2 scripting model uses `unit-type-count-total` plus `can-train` and `train` as the standard production pattern; the AIBuilder project likewise describes its generated `.per` files as using basic build/train/attack instructions. citeturn0search0turn0search7
