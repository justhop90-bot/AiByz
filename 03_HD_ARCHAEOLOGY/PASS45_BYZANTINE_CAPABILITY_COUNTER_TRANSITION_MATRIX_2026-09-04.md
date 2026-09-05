# AEGIS Layer 2 — Pass 45
# Byzantine Capability / Counter / Transition Matrix — Archaeological Research

**Date:** 2026-09-04  
**Layer:** 2 — research / archaeology only  
**Predecessor:** Pass 44 Byzantine Strategic Profile + Pass 44 deep QC  
**Status:** PASS — quantitative topology substantially advanced; matchup and transition economics remain bounded research gaps  
**Implementation:** **ZERO** — no `.per`, controller, production policy, or runtime deployment

---

## 0. Mission

Pass 45 converts the qualitative Byzantine profile into a capability-oriented evidence matrix:

```text
UNIT / TECH
    ↓
COST
    ↓
TRAIN TIME
    ↓
PRODUCTION BUILDING
    ↓
AGE / PREREQUISITES
    ↓
COMBAT ROLE
    ↓
COUNTER RELATIONSHIP
    ↓
RESOURCE BURDEN
    ↓
TRANSITION COST
    ↓
MAP ROLE
    ↓
STRATEGIC OPTION VALUE
```

The matrix is deliberately **not** a build order or controller specification.

Evidence classes:

- **DIRECT** — current installed data or authoritative patch documentation directly establishes the fact.
- **COMPOSED** — multiple DIRECT facts establish the relationship.
- **INFERRED** — strategic interpretation not directly encoded by the source.
- **AEGIS-GENERALIZATION** — a future design hypothesis derived from the research.
- **UNCERTAIN** — insufficient evidence; do not promote.

---

# 1. Critical correction carried forward from Pass 44 QC

Pass 44's qualitative thesis survives, but several statements were too strong. Pass 45 therefore adopts these rules:

1. A unit being present in the technology tree does **not** mean it is immediately trainable.
2. A nominal counter relationship does **not** establish effective battlefield superiority.
3. A civilization discount changes resource cost; it does **not** prove a production priority.
4. A transition path does **not** prove a cheap transition.
5. A broad technology tree proves breadth, not lower decision risk.
6. Map roles are hypotheses unless directly demonstrated by game data or replay evidence.
7. Cataphracts are not classified as a direct anti-mounted counter without matchup evidence.
8. Monks are classified as conversion/healing/control capability, not a conventional counter line.

---

# 2. Current Byzantine technology-topology audit

The installed current `CivTechTrees/BYZANTINES.json` contains **145 unit/technology nodes** and **28 building nodes**.

Directly inspected strategically relevant nodes include:

| Capability | Node type | Age | Building | Current status | Direct prerequisite data |
|---|---|---:|---:|---|---|
| Skirmisher | Unit | 2 | 87 | ResearchedCompleted | none listed |
| Elite Skirmisher | UnitUpgrade | 3 | 87 | ResearchedCompleted | none listed |
| Spearman | Unit | 2 | 12 | ResearchedCompleted | none listed |
| Halberdier | UnitUpgrade | 4 | 12 | ResearchedCompleted | none listed |
| Knight | Unit | 3 | 101 | ResearchedCompleted | none listed |
| Cavalier | UnitUpgrade | 4 | 101 | ResearchedCompleted | none listed |
| Paladin | UnitUpgrade | 4 | 101 | ResearchedCompleted | none listed |
| Camel Rider | RegionalUnit | 3 | 101 | ResearchedCompleted | none listed |
| Heavy Camel Rider | RegionalUnit | 4 | 101 | ResearchedCompleted | none listed |
| Onager | UnitUpgrade | 4 | 49 | ResearchedCompleted | none listed |
| Siege Onager | UnitUpgrade | 4 | 49 | **NotAvailable** | unavailable |
| Bombard Cannon | Unit | 4 | 49 | **ResearchRequired** | Tech ID 47 |
| Dromon | RegionalUnit | 4 | 45 | ResearchedCompleted | none listed |
| Cataphract | UniqueUnit | 3 | 82 | ResearchedCompleted | none listed |
| Elite Cataphract | UniqueUnit | 4 | 82 | ResearchedCompleted | none listed |
| Trebuchet (Packed) | Unit | 4 | 82 | ResearchedCompleted | none listed |
| Monk | Unit | 3 | 104 | ResearchedCompleted | none listed |

**Evidence:** DIRECT — installed current Byzantine technology-tree data.

Important state semantics:

```text
ResearchedCompleted
    ≠ generic universal availability at every game time

ResearchRequired
    = capability exists but requires its technology/prerequisite state

NotAvailable
    = civilization does not have that node available
```

The Onager/Siege Onager distinction is therefore a firm baseline fact.

---

# 3. Production topology

Current installed topology establishes these production locations:

```text
Barracks (12)
 ├─ Spearman
 └─ Halberdier line

Archery Range (87)
 ├─ Skirmisher
 └─ Elite Skirmisher line

Stable (101)
 ├─ Knight → Cavalier → Paladin
 └─ Camel Rider → Heavy Camel Rider

Siege Workshop (49)
 ├─ Onager
 └─ Bombard Cannon

Castle (82)
 ├─ Cataphract → Elite Cataphract
 └─ Trebuchet

Monastery (104)
 └─ Monk

Dock (45)
 └─ Dromon
```

**Evidence:** DIRECT for node/building identity and age/status; COMPOSED for strategic topology.

This topology is strategically important because transitions can require either:

- **same-building substitution**, or
- **new production infrastructure**.

That distinction is a major component of transition cost.

---

# 4. Resource-cost evidence

The installed game-data archaeology previously resolved Byzantine Camel Rider / Heavy Camel Rider unit records as:

```text
Camel Rider       = 55 food + 60 gold
Heavy Camel Rider = 55 food + 60 gold
Train time        = 22 seconds
Production        = Stable / building 101
```

Unit IDs:

```text
329 = Camel Rider
330 = Heavy Camel Rider
```

The current Byzantine civilization bonus applies a food discount to the Camel Rider, Skirmisher, and Spearman families. The exact discounted integer representation should be taken from direct engine data before being used as an executable economic constant.

**Important:** Pass 45 intentionally does not invent fractional-to-integer rounding rules where the current data extraction has not exposed them directly.

Therefore:

```text
BASE COST
    ≠
BYZANTINE EFFECTIVE COST
```

until the civilization modifier is explicitly joined to the unit cost record.

This distinction is mandatory for future optimizer work.

---

# 5. Byzantine discount matrix

The established civilization-specific discounted families are:

| Family | Food-cost leverage | Other-resource cost | Research status |
|---|---:|---:|---|
| Spearman line | -25% food | unchanged wood/gold as applicable | DIRECT civilization property |
| Skirmisher line | -25% food | unchanged wood/gold as applicable | DIRECT civilization property |
| Camel Rider line | -25% food | gold burden remains | DIRECT civilization property |

Strategic consequence:

```text
DISCOUNT
  ↓
LOWER FOOD REQUIREMENT PER UNIT
  ↓
LOWER FOOD PRESSURE
  ↓
POTENTIALLY MORE FEASIBLE COMPETING EXPENDITURES
```

The final arrow is **COMPOSED**, not DIRECT.

Do not write:

```text
25% food discount = 25% stronger economy
```

That is false as a general statement because production, resource income, gold/wood requirements, population, timing, and survival remain constraints.

---

# 6. Capability matrix — anti-mounted

## 6.1 Spearman / Pikeman / Halberdier

```text
TARGET FAMILY
→ mounted units

CAPABILITY
→ Spearman-line

PRODUCTION
→ Barracks

BYZANTINE LEVERAGE
→ discounted food cost

MAIN BURDEN
→ wood + food + production time

PRIMARY LIMITATION
→ low mobility and vulnerability to ranged/siege support
```

**Counter classification:** DIRECT/COMPOSED depending on exact target class and bonus-damage data.

The generic statement “spears counter cavalry” is insufficient for the final matrix. The eventual matchup table must join:

```text
bonus damage
armor class
base attack
attack interval
range
movement speed
cost
train time
```

before an effective-counter score is assigned.

## 6.2 Camel Rider / Heavy Camel Rider

Camel Rider is the most important current Byzantine regional counter-capability family identified by the historical archaeology and current roster.

```text
Camel Rider
→ Heavy Camel Rider
→ Stable
→ Castle / Imperial capability
```

The Byzantine food discount lowers the food component while the **60-gold cost remains material**.

The correct economic characterization is therefore:

> **food-cheaper mounted counter-capability, not cheap-all-resource cavalry.**

This distinction matters when comparing camels with trash anti-mounted units.

## 6.3 Cataphract

Pass 45 explicitly rejects the Pass-44 implication that Cataphracts should automatically enter the mounted-threat counter set.

Current data establishes:

```text
Cataphract → Elite Cataphract
Castle production
```

It does **not**, by itself, establish:

```text
mounted threat → Cataphract is counter
```

Classification:

**DIRECT:** unique heavy cavalry capability.  
**INFERRED:** anti-infantry / heavy-combat specialization.  
**UNRESOLVED:** effectiveness against each mounted target class.

---

# 7. Capability matrix — anti-archer

## Skirmisher line

Direct topology:

```text
Skirmisher
→ Elite Skirmisher
→ Archery Range
```

Byzantine leverage:

```text
-25% food cost
```

The correct strategic chain is:

```text
ARCHER PRESSURE
→ NEED RANGED-DAMAGE MITIGATION
→ SKIRMISHER CANDIDATE
→ LOWER FOOD BURDEN FOR BYZANTINES
```

The phrase “sustained counter-mass” remains an **INFERRED** hypothesis because sustained mass depends on production capacity, wood, food income, population, survival, and opponent response.

---

# 8. Capability matrix — anti-infantry

Relevant Byzantine capability families include:

- ranged damage,
- cavalry,
- Cataphracts,
- siege,
- monks/control.

But these are not interchangeable counters.

The required target-specific chain is:

```text
TARGET INFANTRY CLASS
→ TARGET ARMOR / HP
→ DAMAGE PROFILE
→ RANGE / MOBILITY
→ REQUIRED RESPONSE CAPABILITY
→ COST / TIME
```

**Research status:** PARTIAL.

The current tree proves the candidate surface, not the final ranking.

---

# 9. Siege capability matrix

| Capability | Current status | Production | Age | Key constraint |
|---|---|---|---:|---|
| Onager | Available | Siege Workshop | 4 | wood/gold + upgrade path |
| Siege Onager | NotAvailable | Siege Workshop | 4 | civilization restriction |
| Bombard Cannon | ResearchRequired | Siege Workshop | 4 | Chemistry prerequisite |
| Trebuchet | Available | Castle | 4 | Castle + Imperial timing |

The most important finding is:

```text
BROAD SIEGE ACCESS
        ≠
MAXIMUM SIEGE ACCESS
```

The absence of Siege Onager is a hard boundary on the Byzantine late-game siege surface.

Bombard Cannon being `ResearchRequired` also prevents the capability from being represented as a free/default Imperial option.

---

# 10. Naval capability matrix — current-version correction

Pass 44 used older naval terminology too casually. The current official naval rework must be incorporated into the research baseline.

The January 2026 naval update states that the old War Galley/Galleon/Fast Fire Ship progression was replaced by **Medium Warships / Heavy Warships**, with the latter upgrading the Galley-, Fire-, and Hulk-lines together. citeturn0search3

Therefore future current-data research must not blindly reproduce the pre-rework topology:

```text
OLD TERMINOLOGY
War Galley → Galleon
Fast Fire Ship
```

as though it were the current universal production model.

For Byzantines, current research should instead preserve:

```text
Dock
 ↓
current naval technology topology
 ↓
Fire Ship / Dromon capability
```

Official Update 169123 confirms that Byzantine Fire Ships and Dromons have the **25% attack-speed bonus**. citeturn0search4

**Evidence:** DIRECT.

The strategic interpretation:

```text
25% attack speed
→ higher attack tempo
```

is COMPOSED; it is not itself a guarantee of naval control.

---

# 11. Monastery capability

Current topology:

```text
Monastery
→ Monk
→ technology surface including healing / conversion / support technologies
```

The monastery should be decomposed into separate capability classes:

| Capability | Type | Main uncertainty |
|---|---|---|
| Healing | Sustain | actual battlefield uptime |
| Conversion | Control | target availability / monk survival |
| Relics | Economy | map access / opportunity cost |
| Monk technologies | Capability enhancement | research timing / gold burden |

The Byzantine monk healing bonus is an independent civilization lever.

Do not collapse all monastery value into one “monk score” before the metrics are defined.

---

# 12. Infrastructure cost as transition cost

A transition has at least four distinct cost layers:

```text
1. UNIT COST
2. TECHNOLOGY COST
3. PRODUCTION-INFRASTRUCTURE COST
4. LOST / DISPLACED PRODUCTION CAPACITY
```

Examples:

### Spear → Camel

Requires stable capability and significant gold allocation.

### Skirmisher → Siege

Requires Siege Workshop and different wood/gold structure.

### Ranged → Cataphract

Requires Castle production plus Cataphract-specific technology investment.

### Land → Water

Requires Dock/water infrastructure and a separate naval resource-production problem.

Therefore:

```text
TRANSITION COST
≠
NEW UNIT COST
```

This is a foundational research finding.

---

# 13. Sunk technology

A capability transition can leave previous investment useful, neutral, or stranded.

Examples:

```text
Crossbow → Arbalester
```

retains much of the same production infrastructure and unit lineage.

By contrast:

```text
Ranged → Camel
```

changes production infrastructure and resource mix.

And:

```text
Camel → Heavy Camel
```

is primarily an upgrade within the same production family.

This creates three transition classes:

| Transition type | Infrastructure reuse | Typical research meaning |
|---|---|---|
| Vertical upgrade | High | low structural transition cost |
| Same-building lateral | High | moderate transition cost |
| New-building transition | Low | higher structural cost |

These are **COMPOSED** research abstractions, not historical controller rules.

---

# 14. Transition taxonomy

The Byzantine roster supports at least these candidate transition classes:

```text
SKIRMISH → SIEGE
SKIRMISH → HEAVY CAVALRY
SKIRMISH → SPEAR

SPEAR → CAMEL
SPEAR → RANGED
SPEAR → SIEGE

CAMEL → HEAVY CAMEL
CAMEL → RANGED SUPPORT
CAMEL → CATAPHRACT

KNIGHT → CAVALIER → PALADIN

CATAPHRACT → ELITE CATAPHRACT

LAND → WATER
WATER → LAND
```

The presence of a transition does not imply that it is strategically good.

The unresolved question is:

> **At what state does the marginal capability gained by the new branch exceed the resource, timing, infrastructure, and commitment cost of entering it?**

That question belongs to later empirical work and eventually Layer 3 architecture.

---

# 15. Capability efficiency is multi-dimensional

A future comparison cannot use resource cost alone.

A capability candidate has at least these dimensions:

```text
RESOURCE COST
TRAIN TIME
TECH COST
INFRASTRUCTURE COST
UPGRADE COST
POPULATION COST
MOBILITY
RANGE
SURVIVABILITY
DAMAGE OUTPUT
COUNTER VALUE
MAP VALUE
TRANSITION REUSE
COMMITMENT REVERSIBILITY
```

Therefore “best counter” is undefined until a metric is specified.

This directly addresses the Pass-44 QC requirement that the project must not call a unit “best” without an explicit objective function.

---

# 16. Byzantine response economics

The strongest civilization-specific economic pattern now looks like:

```text
THREAT
 ↓
CANDIDATE COUNTERS
 ↓
FILTER BY TECH / BUILDING / AGE
 ↓
FILTER BY RESOURCE AVAILABILITY
 ↓
APPLY BYZANTINE FOOD DISCOUNT
 ↓
COMPARE TOTAL TRANSITION BURDEN
```

The discount belongs **inside** candidate evaluation, not as a civilization-wide scalar multiplier.

Example:

```text
CAMEL
= food-cheaper + gold-required + stable-required

SPEAR
= food-cheaper + wood-required + barracks

SKIRM
= food-cheaper + wood-required + range
```

This is a **research model**, not implementation.

---

# 17. Optionality refinement

Pass 44 proposed optionality as:

```text
COUNT / QUALITY OF FEASIBLE CAPABILITIES
AFTER HARD CONSTRAINTS
```

Pass 45 sharpens this concept without implementing it.

A capability is only meaningfully available if it passes:

```text
AGE
TECHNOLOGY
BUILDING
RESOURCE
POPULATION
TIME
MAP
TARGET
```

Thus raw roster size is a poor optionality measure.

A more rigorous research concept is:

```text
FEASIBLE RESPONSE SET
=
CAPABILITIES
SURVIVING HARD CONSTRAINT FILTERS
```

Then, separately:

```text
RESPONSE QUALITY
=
EFFECTIVENESS + TIMING + COST + RISK + TRANSITION VALUE
```

This remains **AEGIS-GENERALIZATION**.

---

# 18. Map-role matrix

Map roles are intentionally hypotheses.

| Capability | Open map hypothesis | Closed map hypothesis | Water map hypothesis |
|---|---|---|---|
| Spear | defensive anti-mounted | choke/position defense | low relevance |
| Skirmisher | mobile ranged defense | protected ranged support | low relevance |
| Camel | mobile mounted response | mixed response | none |
| Knight/Cavalier | mobility / pressure | positional heavy force | none |
| Cataphract | heavy mobile force | concentrated heavy force | none |
| Siege | area denial / pressure | strong positional value | naval analogues separate |
| Monk | sustain/control | high-value support | situational |
| Dromon | none | none | specialized naval siege |

Evidence grade: **INFERRED / AEGIS-GENERALIZATION**.

No row should be treated as historical doctrine.

---

# 19. Historical-AI linkage

The historical Promisory archaeology now has a cleaner interface with the Byzantine capability matrix:

```text
HISTORICAL THREAT AGGREGATE
        ↓
CAPABILITY REQUIREMENT
        ↓
CURRENT BYZANTINE CANDIDATE SET
        ↓
RESOURCE / TECH / BUILDING FILTER
        ↓
PRODUCTION POSSIBILITY
```

Historical evidence proves threat aggregates, production authorization, research gates, escrow, state flags, timers, and reset/re-entry behavior.

It does **not** prove that the historical programmer constructed the complete current candidate matrix above.

That boundary remains mandatory.

---

# 20. Current evidence ledger

| Finding | Grade | Status |
|---|---|---|
| Byzantine current tree has 145 unit nodes | DIRECT | CONFIRMED |
| 28 building nodes in current tree | DIRECT | CONFIRMED |
| Camel Rider / Heavy Camel Rider are Stable 101 | DIRECT | CONFIRMED |
| Camel Rider / Heavy Camel Rider are Castle/Imperial regional capabilities | DIRECT | CONFIRMED |
| Onager available | DIRECT | CONFIRMED |
| Siege Onager unavailable | DIRECT | CONFIRMED |
| Bombard Cannon requires research state | DIRECT | CONFIRMED |
| Cataphract is Castle unique unit | DIRECT | CONFIRMED |
| Dromon is Imperial regional unit | DIRECT | CONFIRMED |
| Spear/Skirm/Camel food discount | DIRECT civilization property | CONFIRMED |
| Discount means lower food pressure | COMPOSED | PROBABLE |
| Discount means guaranteed stronger economy | — | REJECTED |
| Cataphract directly counters cavalry | — | UNPROVEN |
| Monks are a conventional counter line | — | REJECTED |
| Broad tree lowers dead-end risk | — | UNPROVEN |
| More transition paths exist | COMPOSED | PROBABLE |
| 25% Fire Ship/Dromon attack-speed bonus | DIRECT | CONFIRMED |
| Current naval topology equals pre-2026 topology | — | REJECTED |
| Optionality is feasible response-set quality | AEGIS-GENERALIZATION | HYPOTHESIS |

---

# 21. Hostile QC — Pass 45

## Attack: “Current tree presence equals trainability.”

**Rejected.**

`ResearchRequired` and `NotAvailable` prove why status must be retained.

## Attack: “A counter is whatever players conventionally call a counter.”

**Rejected.**

Final matrix must use armor classes, bonus damage, range, speed, cost, train time, and target class.

## Attack: “25% cheaper food means 25% cheaper unit.”

**Rejected.**

Only the food component changes.

## Attack: “Camel is cheap.”

**Rejected.**

Camel Rider retains substantial gold burden and production/time constraints.

## Attack: “Cataphract belongs in anti-cavalry set.”

**Rejected pending matchup data.**

## Attack: “Siege is one counter category.”

**Rejected.**

Different siege units have different target relationships and production costs.

## Attack: “Transition cost is the new unit price.”

**Rejected.**

Infrastructure, technology, displaced production, and resource reallocation matter.

## Attack: “Water strategy can use the old Galley/Galleon terminology unchanged.”

**Rejected.**

The 2026 naval rework changed the current technology topology. citeturn0search3

## Attack: “Map-role hypotheses are facts.”

**Rejected.**

All map-role rows remain inference/generalization.

---

# 22. Remaining high-value gaps

### G1 — Full direct unit-cost extraction

Join current `.dat` unit records to Byzantine civilization modifiers and technology-tree nodes.

### G2 — Train-time matrix

Extract exact train times for every strategically relevant line.

### G3 — Bonus-damage / armor-class matrix

This is the most important unresolved counter-mechanics layer.

### G4 — Exact technology costs

Separate upgrade cost from unit cost.

### G5 — Exact infrastructure cost

Separate existing-building reuse from new-building construction.

### G6 — Current naval topology

Fully re-extract Byzantine Dock/University naval nodes after the 2026 naval rework.

### G7 — Transition economics

Quantify:

```text
NEW RESOURCES
+
NEW BUILDINGS
+
UPGRADES
+
LOST PRODUCTION
+
TIMING DELAY
+
POPULATION DISPLACEMENT
```

### G8 — Replay transition evidence

Correlate observable enemy composition with Byzantine production transitions without falsely claiming hidden controller causality.

---

# 23. Six-month re-entry test

A future engineer should be able to answer all of these without consulting undocumented assumptions:

1. Which Byzantine unit families receive food-cost leverage?
2. Which production buildings host those families?
3. Which are Castle/Imperial transitions?
4. Which current technology-tree nodes are `ResearchedCompleted`, `ResearchRequired`, or `NotAvailable`?
5. Why is Onager not equivalent to Siege Onager?
6. Why is Bombard Cannon not an immediately free capability?
7. Why is Camel a lower-food-cost response but not a low-total-cost unit?
8. Why can Cataphract not be called an anti-cavalry counter without matchup evidence?
9. Why is a counter matrix different from a unit roster?
10. Why is transition cost different from unit cost?
11. What infrastructure can be reused during each major transition?
12. What technology investment is sunk, reusable, or stranded?
13. How did the 2026 naval rework change the terminology/topology problem?
14. Which claims are DIRECT, COMPOSED, INFERRED, or AEGIS-GENERALIZATION?
15. Why does this document authorize no `.per` implementation?

---

# 24. Final disposition

**PASS 45 — PASS WITH RESEARCH GAPS.**

Pass 45 materially improves the Byzantine profile by replacing vague “counter” language with a capability topology and by explicitly separating:

```text
UNIT AVAILABILITY
RESOURCE COST
PRODUCTION TOPOLOGY
TECHNOLOGY STATE
COUNTER RELATIONSHIP
TRANSITION COST
MAP HYPOTHESIS
```

The next highest-value research target is not another civilization essay.

It is the **direct combat/economic matrix**:

```text
UNIT
→ UNIT ID
→ LINE
→ COST
→ TRAIN TIME
→ BUILDING
→ AGE
→ TECH
→ HP
→ ATTACK
→ ARMOR
→ RANGE
→ SPEED
→ BONUS DAMAGE
→ TARGET ARMOR CLASS
→ COUNTER RELATIONSHIP
→ EFFECTIVE COST
→ TRANSITION COST
```

Only after that matrix is complete should Byzantine strategic transition research be considered quantitatively mature enough for Layer 3 handoff.

**Implementation status remains ZERO.**

---

# 25. Source record

### Installed current data

- `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\dat\CivTechTrees\BYZANTINES.json`
- `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\dat\empires2_x2_p1.dat`
- verified current game-data extraction environment

### Historical archaeology

- verified `AI (HD version).per`
- verified Promisory modules
- Pass 43 Historical Strategic Control-State Atlas
- Pass 44 Byzantine Strategic Profile
- Pass 44 Deep QC / Errata

### Current authoritative external evidence

- Age of Empires II: Definitive Edition — Update 169123 (2026-02-17): Byzantine Fire Ships and Dromons attack 25% faster. citeturn0search4
- Age of Empires II: Definitive Edition — New Naval Warfare (2026-01-28): current naval technology restructuring. citeturn0search3
- Age of Empires II: Definitive Edition — Update 51737: Town Patrol free and instantly researched. citeturn1search0
- Official AoE2 civilization learning material: Byzantines have an almost full Technology Tree. citeturn0search0

---

# 26. Provenance rule

Current claims must be tied to current installed data or authoritative current patch documentation.

Historical claims must be tied to verified HD/Promisory archaeology.

Strategic consequences must be labeled COMPOSED or INFERRED where appropriate.

AEGIS design concepts must be labeled AEGIS-GENERALIZATION.

No implementation artifact belongs in Layer 2.
