# AEGIS Layer 2 — Pass 46
# Direct Combat / Economic Matrix — Byzantine Strategic Capability Archaeology

**Date:** 2026-09-04  
**Layer:** 2 — research / archaeology only  
**Predecessor:** Pass 45 Byzantine Capability / Counter / Transition Matrix  
**Status:** PASS WITH BOUNDED GAPS  
**Implementation:** **ZERO** — no `.per`, no controller, no production policy, no runtime deployment

---

## 0. Mission

Pass 46 tightens the Byzantine capability model by separating three things that were previously too easy to conflate:

```text
MECHANICAL / ENGINE DATA
        ≠
TACTICAL MATCHUP
        ≠
STRATEGIC ROLE
```

The project must preserve all three layers independently.

The specific correction carried into this pass is authoritative for AEGIS research:

> **Cataphract is an anti-infantry capability in strategic terms. Its strategic role must not be inferred from a mechanical/game-ID category such as cavalry.**

This means the matrix may record Cataphract as a cavalry unit mechanically while simultaneously classifying its strategic purpose as anti-infantry / infantry suppression.

That is not a contradiction. It is the required separation of ontology from role.

---

# 1. Evidence model

Every row in the eventual combat matrix must distinguish:

```text
ENGINE FACT
→ what the game data says

MATCHUP FACT
→ what the mechanics imply against a specified target

STRATEGIC ROLE
→ what function the capability serves in Byzantine play
```

Evidence classes remain:

- **DIRECT** — current installed game data or authoritative current documentation.
- **COMPOSED** — relationship derived from multiple direct facts.
- **INFERRED** — strategic interpretation supported by mechanics but not explicitly encoded.
- **AEGIS-GENERALIZATION** — future design hypothesis.
- **UNCERTAIN** — insufficient evidence.

No strategic label is permitted to overwrite the underlying engine identifier.

---

# 2. Cataphract correction — binding research rule

## 2.1 Mechanical identity

The Cataphract is mechanically a cavalry / mounted unit and is produced from the Castle.

Relevant current topology:

```text
Castle
  ↓
Cataphract
  ↓
Elite Cataphract
```

**Evidence:** DIRECT.

## 2.2 Strategic identity

For Byzantine strategy archaeology, Cataphract belongs in the **anti-infantry capability family**.

This is supported by the long-standing game role and by community discussion consistently identifying Cataphracts as an anti-infantry specialist. The important point for AEGIS is not the community wording itself; it is that strategic classification must be allowed to differ from mechanical class. citeturn0search3turn0search4

Therefore:

```text
GAME / ENGINE CLASS
→ mounted cavalry

STRATEGIC CAPABILITY
→ anti-infantry

PRIMARY STRATEGIC USE
→ suppress / destroy infantry concentrations
```

**Evidence:** mechanical identity = DIRECT; anti-infantry strategic role = INFERRED/COMPOSED from the unit's actual combat properties and established role evidence.

## 2.3 What must NOT happen

Do not implement or document the following shortcut:

```text
unit-type = cavalry
→ therefore counter = cavalry
```

Nor:

```text
cavalry armour class
→ therefore strategic role = anti-cavalry
```

Nor:

```text
mounted unit
→ candidate for mounted-threat response
```

These are category errors.

The correct chain is:

```text
MECHANICAL IDENTITY
→ COMBAT PROPERTIES
→ TARGET-SPECIFIC EFFECT
→ STRATEGIC ROLE
```

---

# 3. Strategic-role ontology

The Byzantine matrix now uses separate fields:

| Field | Meaning |
|---|---|
| `mechanical_family` | engine/game-data classification |
| `armor_classes` | mechanics used by damage calculations |
| `bonus_target_classes` | explicit bonus-damage relationships |
| `combat_profile` | attack, HP, armor, range, speed, interval |
| `target_effect` | measured effect against a specified target |
| `strategic_role` | role in Byzantine force design |
| `counter_class` | direct / composed / inferred relationship |
| `economic_profile` | resource + time burden |
| `transition_profile` | infrastructure + technology + opportunity burden |

This separation is now mandatory for later Layer-3 work.

---

# 4. Byzantine capability families — corrected

The current research surface is better represented as follows:

```text
ANTI-INFANTRY
  ├─ Cataphract / Elite Cataphract
  ├─ ranged damage candidates
  └─ siege candidates against massed infantry

ANTI-MOUNTED
  ├─ Spearman line
  ├─ Camel Rider / Heavy Camel Rider
  └─ target-specific alternatives

ANTI-RANGED
  ├─ Skirmisher line
  ├─ cavalry pressure
  └─ siege / positional responses

SIEGE / ANTI-SIEGE
  ├─ Onager
  ├─ Bombard Cannon
  └─ Trebuchet

CONTROL / SUSTAIN
  └─ Monks

NAVAL
  └─ Fire Ship / Dromon capability surface
```

These are strategic capability families, not engine type IDs.

---

# 5. Direct combat matrix contract

The final quantitative matrix must resolve, where the installed data exposes the field:

```text
UNIT NAME
UNIT ID
LINE ID
MECHANICAL FAMILY
STRATEGIC ROLE
COST FOOD
COST WOOD
COST GOLD
TRAIN TIME
PRODUCTION BUILDING
AGE
REQUIRED TECHNOLOGY
HP
MELEE ATTACK
PIERCE ATTACK
MELEE ARMOR
PIERCE ARMOR
RELEVANT ARMOR CLASSES
RANGE
SPEED
ATTACK INTERVAL
BONUS DAMAGE
BONUS TARGET CLASS
SPECIAL EFFECTS
```

Then, separately:

```text
TARGET UNIT
TARGET ARMOR CLASS
DAMAGE PER HIT
HITS TO KILL
TIME TO KILL
RESOURCE COST
POPULATION COST
PRODUCTION TIME
TECHNOLOGY BURDEN
INFRASTRUCTURE BURDEN
```

Only after these are resolved should AEGIS assign an effective-counter relationship.

---

# 6. Effective-counter definition

A unit is not an effective counter merely because it has bonus damage against the target.

For research purposes:

```text
NOMINAL COUNTER
= mechanical advantage exists

EFFECTIVE COUNTER
= mechanical advantage survives
  cost
  production
  timing
  mobility
  range
  survivability
  technology
  infrastructure
  and target response
```

Therefore the project must never use a binary:

```text
counter = true / false
```

as the sole representation.

Use a relationship such as:

```text
DIRECT
COMPOSED
INFERRED
NOT ESTABLISHED
```

and preserve the underlying measurements.

---

# 7. Cataphract-specific research model

The Cataphract should be represented as:

```text
mechanical_family = cavalry
strategic_role = anti-infantry
production = Castle
progression = Cataphract → Elite Cataphract
```

Its anti-infantry role is especially important because it is a strategic capability that does not fit a simplistic "anti-cavalry / anti-archer / anti-siege" mechanical taxonomy.

Historical/community evidence also describes Cataphracts as a unit intended to perform particularly well against infantry. citeturn0search3turn0search4

The project should therefore test Cataphracts against **infantry target classes**, not merely compare the Cataphract's cavalry label with enemy cavalry labels.

The next empirical questions are:

```text
How much infantry bonus damage?
How does armor modify it?
How many hits to kill representative infantry?
How does trample alter mass-infantry performance?
What is the resource/time cost of reaching effective Cataphract strength?
How does that compare with cheaper Byzantine anti-infantry alternatives?
```

These remain quantitative research questions, not controller rules.

---

# 8. Byzantine food-discount economics

The established Byzantine food discounts apply to the Spearman, Skirmisher, and Camel Rider families.

The economic model must therefore distinguish:

```text
RAW UNIT COST
→ CIVILIZATION MODIFIER
→ EFFECTIVE UNIT COST
```

The discount should be evaluated in both absolute and relative terms:

```text
food saved / unit
food saved / minute
food saved / army package
food saved over a production horizon
```

But food savings must not be converted directly into a claim of equivalent total economic strength.

For a mixed force:

```text
TOTAL RESOURCE BURDEN
=
food
+
wood
+
gold
+
population
+
production time
+
technology
+
infrastructure
```

This remains a research model, not an optimizer implementation.

---

# 9. Transition economics — corrected scope

Transition cost must remain distinct from unit cost.

For each candidate transition, record:

```text
UNIT COST
TECH COST
UPGRADE COST
BUILDING COST
BUILDING AVAILABILITY
PRODUCTION DISPLACEMENT
RESOURCE MIX CHANGE
TIMING LOSS
POPULATION EFFECT
REVERSIBILITY
```

Example:

```text
Spearman → Camel
```

is not simply:

```text
camel price
```

It potentially includes a stable requirement, gold reallocation, production capacity, and opportunity cost.

Likewise:

```text
Camel → Heavy Camel
```

is structurally different because the same production building and unit family are retained.

This supports the three-level transition taxonomy:

```text
VERTICAL
SAME-BUILDING LATERAL
NEW-INFRASTRUCTURE
```

---

# 10. Current Byzantine production/capability baseline

The current topology remains:

```text
Barracks
→ Spearman / Halberdier

Archery Range
→ Skirmisher / Elite Skirmisher

Stable
→ Knight / Cavalier / Paladin
→ Camel Rider / Heavy Camel Rider

Castle
→ Cataphract / Elite Cataphract
→ Trebuchet

Siege Workshop
→ Onager
→ Bombard Cannon after required technology

Monastery
→ Monk

Dock
→ current naval capability topology
```

This is capability topology, not production policy.

---

# 11. Current naval data boundary

The current naval model must use the 2026 naval rework rather than reproducing obsolete War Galley/Galleon assumptions.

The Byzantine naval capability research must preserve the distinction between:

```text
mechanical naval progression

and

Byzantine Fire Ship / Dromon strategic role
```

The February 2026 update's Byzantine Fire Ship/Dromon attack-speed bonus remains relevant as a direct civilization modifier, while strategic naval control remains an empirical question.

No naval "best counter" is assigned in Pass 46.

---

# 12. Hostile quality review

The following failure modes were explicitly tested against this pass.

### Failure A — mechanical class becomes strategic role

**Result:** REJECTED.

Cataphract is the primary correction. Cavalry classification does not make it an anti-cavalry strategic unit.

### Failure B — bonus damage becomes universal counter

**Result:** REJECTED.

Bonus damage is target-specific and must be joined with armor, attack interval, cost, and timing.

### Failure C — cheap food cost becomes cheap unit

**Result:** REJECTED.

Gold, wood, production time, infrastructure, and population remain constraints.

### Failure D — technology-tree presence becomes immediate availability

**Result:** REJECTED.

Age, prerequisites, technology state, and production building remain separate facts.

### Failure E — nominal counter becomes effective counter

**Result:** REJECTED.

Effectiveness requires a target-specific metric.

### Failure F — strategic role becomes programmer intent

**Result:** REJECTED.

A role can be a strong strategic interpretation without proving historical programmer intent.

### Failure G — Layer 2 becomes implementation

**Result:** REJECTED.

No `.per`, architecture implementation, runtime controller, or executable production policy is produced by this pass.

---

# 13. Six-month re-entry test

A future researcher returning to this pass must be able to answer:

1. Is Cataphract still mechanically cavalry?
2. Is Cataphract still classified by AEGIS as anti-infantry strategically?
3. What current patch changed its attack, armor, bonus damage, trample, cost, or train time?
4. Which facts come from game data versus strategic interpretation?
5. Which counter relationships are direct and which are inferred?
6. What technology is required before the unit becomes practically deployable?
7. What is the total transition cost from the incumbent composition?
8. What metric defines "effective" in the comparison?
9. Has the naval technology topology changed again?
10. Has any Layer-3 implementation incorrectly collapsed strategic role into mechanical type?

If any answer cannot be reproduced from durable source evidence, the corresponding claim must be downgraded.

---

# 14. Pass 46 findings

### FINDING 46.1 — Strategic role and mechanical identity must be separate fields

**Status:** CONFIRMED methodological requirement.

### FINDING 46.2 — Cataphract belongs in Byzantine anti-infantry strategic capability analysis

**Status:** CONFIRMED as strategic classification; exact matchup/economic ranking remains quantitative research.

### FINDING 46.3 — Cataphract must not be inserted into an anti-mounted response set merely because its engine family is cavalry

**Status:** CONFIRMED.

### FINDING 46.4 — Effective-counter analysis requires target-specific combat and economic measurements

**Status:** CONFIRMED.

### FINDING 46.5 — Byzantine food discounts should be modeled as resource-specific modifiers, not as global economic multipliers

**Status:** CONFIRMED.

### FINDING 46.6 — Transition cost requires infrastructure, technology, production displacement, and timing dimensions in addition to unit cost

**Status:** CONFIRMED.

### FINDING 46.7 — Exact full combat matrix remains a bounded data-extraction task

**Status:** OPEN.

The installed `.dat` remains the authoritative local source for exact unit-level mechanics. The remote machine was not available for direct extraction during this pass, so no unverified numerical values have been fabricated.

---

# 15. Next research frontier

Pass 47 should close the remaining quantitative gap by obtaining an exact, reproducible extraction of the relevant Byzantine unit records and constructing representative matchup rows.

Priority target set:

```text
Cataphract
Elite Cataphract
Spearman
Pikeman
Halberdier
Skirmisher
Elite Skirmisher
Camel Rider
Heavy Camel Rider
Knight
Cavalier
Paladin
Onager
Bombard Cannon
Trebuchet
Monk
Dromon
Fire Ship line
```

For each:

```text
ID
LINE
COST
TRAIN TIME
BUILDING
AGE
PREREQUISITES
HP
ATTACK
ARMOR
RANGE
SPEED
ATTACK INTERVAL
BONUS DAMAGE
ARMOR CLASSES
SPECIAL EFFECTS
```

Then construct representative target pairs and compute:

```text
DAMAGE / HIT
HITS TO KILL
TIME TO KILL
RESOURCE COST
RESOURCE COST / DAMAGE
PRODUCTION TIME
POPULATION COST
TRANSITION BURDEN
```

The output should answer the strategic question without collapsing it into a simplistic counter table:

> **Which Byzantine capability provides the required battlefield effect at acceptable resource, timing, infrastructure, and commitment cost under the observed state?**

That question is still research in Layer 2. The eventual decision engine belongs to Layer 3.

---

# 16. Provenance and boundary declaration

This artifact is intentionally research-only.

```text
Layer 1: frozen at 89%
Layer 2: active archaeology
Layer 3: implementation deferred
```

No `.per` implementation is part of Pass 46.

No strategic-role classification in this document is permission to hard-code that role into the bot.

No current combat number should be promoted to executable constants until the installed game-data extraction is directly reproduced and provenance-recorded.

**Pass 46 disposition: PASS WITH BOUNDED GAPS.**

The Cataphract classification correction is now incorporated into the AEGIS research model: **mechanical cavalry identity, strategic anti-infantry role.**
