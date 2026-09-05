# AEGIS Layer 2 — Pass 49B
# Byzantine Player Mechanics / Strategy ↔ Historical HD AI Cross-Reference

**Date:** 2026-09-04  
**Layer:** 2 — research / archaeology only  
**Status:** **PASS — Byzantine strategic model substantially expanded and cross-referenced against current game data, official documentation, current empirical reference data, and historical HD AI evidence**  
**Implementation:** **ZERO** — no `.per`, controller, production policy, or runtime deployment created

---

## 0. Mission

Before Pass 50, this deep dive establishes the Byzantine civilization as a **player-facing strategic system**, then cross-references that system against the historical HD AI substrate already excavated in AEGIS.

The objective is not to produce a build order.

The objective is to answer:

> **What does it actually mean to play Byzantines well, what mechanical properties create those strategic possibilities, how does an expert player reason over them, and which portions of that reasoning are visibly represented in the historical HD AI?**

The research boundary is deliberately strict:

```text
PLAYER MECHANICS
↓
PLAYER STRATEGY
↓
STRATEGIC CAPABILITY MODEL
↓
HD AI REPRESENTATION
↓
EVIDENCE LIMIT
```

No Layer-3 implementation is authorized by this pass.

---

# 1. Source hierarchy

This pass uses a deliberately mixed evidence hierarchy.

### Tier A — Official current game documentation

- World's Edge / Age of Empires official civilization and gameplay documentation.
- Official AoE2:DE release notes, especially current naval and Byzantine balance changes.

These establish game rules and patch changes.

### Tier B — Current structured game-data reference

- AoE2 Insights current Byzantine civilization statistics and technology information.

Useful for current roster, bonuses, technology descriptions, production statistics, and empirical match summaries. It is not treated as equivalent to installed `.dat` authority.

### Tier C — Installed/local AEGIS evidence

Previously verified project evidence includes:

- current `CivTechTrees/BYZANTINES.json`;
- installed unit data where explicitly extracted;
- historical `Promisory` AI source archaeology;
- replay evidence;
- AEGIS control-chain analyses.

### Tier D — Historical/community AI source

Public repositories and archived HD AI material are used to corroborate scripting semantics and historical behavior patterns. They are not treated as proof of current game balance unless independently current.

### Evidence labels

```text
DIRECT
COMPOSED
INFERRED
AEGIS-GENERALIZATION
UNCERTAIN
DISPROVEN
```

Strategic statements additionally receive a provenance distinction:

```text
MECHANICAL
PLAYER-STRATEGIC
HISTORICAL-AI
AEGIS-ANALYTICAL
```

---

# 2. Executive finding

The Byzantine civilization is not best understood as “a defensive civ with cheap trash.”

That description is mechanically incomplete and strategically misleading.

A more accurate player model is:

```text
DEFENSIVE INFRASTRUCTURE
+
RESOURCE-EFFICIENT COUNTER FAMILIES
+
VERY BROAD TECHNOLOGY ACCESS
+
LOWER IMPERIAL TRANSITION COST
+
STRONG INFORMATION / VISION BASELINE
+
HEAVY ANTI-INFANTRY UNIQUE CAVALRY
+
SPECIALIZED NAVAL TEMPO
+
MONK SUPPORT
+
BROAD COMPOSITIONAL OPTION SPACE
```

The official learning material explicitly characterizes Byzantines as having an almost full technology tree and strong civilization bonuses, emphasizing their ability to experiment with different units and combinations. citeturn2search1

Current structured reference data lists the principal civilization bonuses as:

```text
Buildings +10/20/30/40% HP by Age
Camel Riders / Skirmishers / Spearman-line -25% cost
Town Watch / Town Patrol free
Imperial Age -33% cost
Fire Ships / Dromons +25% attack speed
```

and the team bonus as faster Monk healing. citeturn1search3

The strategic consequence is not simply “more defense.” It is **an unusually wide response surface whose economic leverage is concentrated in specific unit families and whose late-game transition into Imperial Age is unusually favorable.**

---

# 3. Byzantine strategic identity from the player perspective

A competent Byzantine player is usually solving five linked problems.

## 3.1 Survive efficiently

The civilization's building HP bonus makes static infrastructure harder to remove and therefore changes the value of defensive structures.

Official and current structured references establish the increasing building HP bonus by Age. citeturn1search3

The strategic interpretation is:

```text
STRONGER STRUCTURES
→ MORE TIME BOUGHT
→ MORE PREPARATION WINDOW
→ GREATER VALUE OF POSITIONAL DEFENSE
```

The final two arrows are strategic composition, not direct civilization text.

## 3.2 Spend the right resource at the right time

The three discounted families are not all-resource-cheap.

The discount specifically changes their food burden.

Thus:

```text
BYZANTINE ECONOMIC LEVERAGE
≠
25% MORE RESOURCES
```

It is better represented as:

```text
SAME RESOURCE INCOME
→ LOWER FOOD COST FOR SELECTED CAPABILITIES
→ DIFFERENT FEASIBILITY FRONTIER
```

This is a central player-level mechanic.

## 3.3 Preserve strategic optionality

The nearly complete technology tree means the Byzantine player often has more plausible branches available than a specialist civilization.

The official learning material specifically highlights the almost full technology tree as a reason Byzantines allow varied unit combinations. citeturn2search1

But optionality is not free.

Every branch can require:

```text
BUILDING
TECHNOLOGY
RESOURCE MIX
PRODUCTION TIME
POPULATION
ATTENTION
```

Therefore:

```text
BROAD TECH TREE
≠
AUTOMATIC STRATEGIC SUPERIORITY
```

## 3.4 Convert information into a response

Free Town Watch and Town Patrol improve baseline information availability without requiring the same direct technology investment as other civilizations. Town Patrol being made free and instantly researched was explicitly established by Update 51737. citeturn2search12

The player-level advantage is not “free vision = free win.” It is:

```text
BETTER BASELINE VISION
→ EARLIER DETECTION OPPORTUNITY
→ MORE RESPONSE TIME
→ MORE VALUE FROM A BROAD TECH TREE
```

This creates a particularly interesting synergy between **information** and **optionality**.

## 3.5 Convert survival into a late-game advantage

The -33% Imperial Age cost is a major timing/economic lever. Current structured data confirms it. citeturn1search3

A Byzantine player can therefore treat Imperial transition as more than an age-up milestone:

```text
IMPERIAL ACCESS
→ NEW TECHNOLOGIES / UNITS
→ STRONGER EXISTING CAPABILITIES
→ GREATER RESPONSE SURFACE
```

The actual value depends on whether the player can survive and exploit the transition.

---

# 4. Economic mechanics — the Byzantine resource model

AoE2 has four core resources: food, wood, gold, and stone. Official guidance stresses that economy must be balanced around the intended strategy and rebalanced as needs change. It also warns that floating resources carry opportunity cost. citeturn3search1

For Byzantines, this generic economic principle becomes unusually important because their bonuses are **asymmetric**.

## 4.1 Food discount

The civilization discount applies to:

```text
Camel Rider line
Skirmisher line
Spearman line
```

Current structured data lists this as -25% cost. citeturn1search3

The player should therefore think in terms of **food leverage**, not generic discount power.

Example concept:

```text
RESOURCE INCOME
        ↓
       FOOD
        ↓
 ┌──────┼────────┐
 ↓      ↓        ↓
SPEAR  SKIRM    CAMEL
```

The same food income can support more units from these families than it would without the bonus, while wood/gold requirements remain.

## 4.2 The discount changes bottlenecks

Suppose a composition is food-heavy.

A food discount can move the bottleneck from:

```text
FOOD
```

toward:

```text
WOOD / GOLD / PRODUCTION / POPULATION
```

This is more useful strategically than saying “the units are cheaper.”

The player question becomes:

> **What resource becomes the limiting factor after the Byzantine discount is applied?**

That is the beginning of genuine economic strategy.

## 4.3 Gold discipline

Camel Riders remain gold-intensive despite their food discount. Pass 45/46 local archaeology established Camel Rider and Heavy Camel Rider as 55 food + 60 gold base-cost units with 22-second train time in the installed data.

Therefore:

```text
CAMEL DISCOUNT
→ FOOD RELIEF
BUT
→ GOLD REMAINS A HARD ECONOMIC INPUT
```

This explains why camels should not be modeled as “trash cavalry.”

## 4.4 Resource conversion and market

The official economy guidance emphasizes market use as a balancing mechanism, while warning that complete reliance on the market reduces gathering efficiency. citeturn3search1

For Byzantines, market usage should therefore be interpreted as an **emergency or transition balancing mechanism**, not a replacement for economic planning.

---

# 5. Infrastructure mechanics

Byzantine building HP is a strategic system property, not merely a defensive stat.

Current civilization data gives:

```text
Dark Age    +10% building HP
Feudal      +20%
Castle      +30%
Imperial    +40%
```

citeturn1search3

## Player implications

Stronger structures can:

- buy time;
- protect resource access;
- delay raids;
- preserve production infrastructure;
- make forward defensive positions harder to remove;
- increase the cost/time required for siege or direct assault.

But the building bonus does **not** itself create map control.

The correct chain is:

```text
BUILDING DURABILITY
→ LONGER STRUCTURAL SURVIVAL
→ POSSIBLE DELAY
→ POSSIBLE TIME FOR RESPONSE
→ STRATEGIC VALUE
```

Each downstream step depends on context.

---

# 6. Information mechanics

Byzantines receive free Town Watch and Town Patrol. Update 51737 explicitly made Town Patrol free and instantly researched. citeturn2search12

This should be treated as a strategic information bonus.

## 6.1 Player information loop

```text
VISION
→ DETECTION
→ CLASSIFICATION
→ RESPONSE WINDOW
```

The key word is **window**.

Information is valuable because it changes the amount of time available to respond.

## 6.2 Synergy with defense

The civilization combines:

```text
BETTER BASELINE VISION
+
STRONGER BUILDINGS
+
BROAD TECH TREE
```

A player can therefore potentially:

```text
DETECT EARLIER
→ DEFEND LONGER
→ CHOOSE A MORE APPROPRIATE RESPONSE
```

This is a composed strategic advantage, not one explicit civilization bonus.

## 6.3 Synergy with counter production

Historical HD archaeology becomes particularly interesting here:

```text
ENEMY OBSERVATION
→ THREAT AGGREGATE
→ COUNTER CAPABILITY
→ PRODUCTION
```

The Byzantine player model therefore aligns unusually well with an HD AI architecture that can transform observed threats into production state.

---

# 7. Feudal Age Byzantine strategy

The Feudal phase is not simply “reach Castle quickly.”

The player must answer:

```text
DO I PRESSURE?
DO I DEFEND?
DO I FAST CASTLE?
DO I CONTROL MAP RESOURCES?
DO I BUILD A COUNTER MASS?
```

Official guidance explicitly frames Feudal pressure and Castle Age as situation-dependent rather than one universal sequence. citeturn3search1

## 7.1 Byzantine Feudal leverage

The major relevant families are:

```text
Spearman
Skirmisher
Camel Rider
```

plus the generic early military and economic infrastructure available through the technology tree.

Because the discounted families occupy different battlefield roles, Byzantines can shift their food economy toward the observed threat.

## 7.2 Player decision pattern

```text
SCOUT
↓
IDENTIFY ENEMY COMMITMENT
↓
CHECK OWN ECONOMIC STATE
↓
CHOOSE PRESSURE / DEFENSE / AGE-UP
↓
REALLOCATE VILLAGERS
↓
EXECUTE
↓
REASSESS
```

This is precisely the kind of chain Pass 49 identified as the bridge between player strategy and HD control semantics.

## 7.3 Feudal weakness

The broad roster does not mean all options are equally strong or equally immediate.

A candidate can be mechanically available while remaining economically or temporally infeasible.

Therefore:

```text
TECH TREE ACCESS
≠
CURRENT FEASIBILITY
```

This is a foundational Byzantine decision rule.

---

# 8. Castle Age — where the Byzantine decision space expands

Castle Age is the major strategic expansion point because Byzantines gain access to:

```text
Knights / Cavalier path
Camel Rider / Heavy Camel path
Cataphract
Monks
Siege
additional technologies
Town Centers / broader infrastructure
```

The installed Byzantine topology previously verified by AEGIS establishes these production relationships.

## 8.1 Camel branch

The camel branch is strategically important because it provides a mounted response capability with a different target profile from Cataphracts.

Historical HD archaeology has especially strong evidence here:

```text
enemy cavalry aggregate
→ camel production conditions
→ traincamel
```

This is one of the strongest examples of a Byzantine-relevant player concept having a corresponding historical control chain.

## 8.2 Cataphract branch

Cataphract is a unique heavy cavalry capability produced from the Castle.

Pass 47 established the critical invariant:

```text
MECHANICAL FAMILY = CAVALRY
STRATEGIC ROLE = ANTI-INFANTRY / HEAVY COMBAT
```

Current reference data gives Cataphract as 70 food / 75 gold, with 110 HP, 9 attack, +9 vs Infantry, 2 melee armor, 1 pierce armor, 1.8 reload, 1.35 speed, and 20-second training; Elite has 150 HP, 12 attack, +12 vs Infantry, 1.7 reload, and 15-second training in the cited reference set. These external values remain reference data unless joined to the installed `.dat`. 

The key strategic property is not merely “strong cavalry.”

It is:

```text
HEAVY CAVALRY
+
ANTI-INFANTRY SPECIALIZATION
+
MOBILITY
+
SURVIVABILITY
```

The exact battlefield value remains matchup dependent.

## 8.3 Logistica

Current structured reference lists Logistica as:

```text
Cataphracts gain trample damage
+6 attack vs Infantry
```

at 800 food / 600 gold / 50 seconds. citeturn1search3

The historical balance change reducing Logistica to 800 food is officially documented in Update 39284. citeturn2search3

This creates a classic transition question:

```text
BASE CATAPHRACT VALUE
vs
LOGISTICA INVESTMENT
```

The technology is not simply “better Cataphracts.”

It changes the intended role toward anti-infantry mass combat and area pressure.

---

# 9. Imperial Age — Byzantine acceleration

The -33% Imperial Age cost is one of the civilization's most important macro-strategic bonuses. citeturn1search3

The player-level effect is a lower entry cost into the final technology tier.

This can create a strategic pattern:

```text
SURVIVE / STABILIZE
→ REACH CASTLE
→ PRESERVE ECONOMIC TEMPO
→ ENTER IMPERIAL AT LOWER COST
→ UNLOCK LATE-GAME RESPONSE SURFACE
```

But an important correction is necessary:

```text
CHEAPER IMPERIAL
≠
AUTOMATIC FASTER IMPERIAL
```

Timing still depends on:

- food/gold income;
- villager allocation;
- military expenditure;
- buildings;
- upgrades;
- raids;
- market conditions;
- idle time;
- map resources.

The bonus reduces one cost; it does not remove the rest of the age-up pipeline.

---

# 10. Spearman-line — Byzantine economic weapon

Official AoE2 guidance identifies the Spearman-line as the standard broad counter to most cavalry. citeturn3search1

For Byzantines, the line is also discounted.

The resulting player model is:

```text
CAVALRY THREAT
→ SPEAR CANDIDATE
→ LOW FOOD BURDEN
→ BARRACKS PRODUCTION
```

The important distinction from Camels is:

```text
SPEAR
= LOW-COST ANTI-MOUNTED CAPABILITY

CAMEL
= MOBILE GOLD-REQUIRING ANTI-MOUNTED CAPABILITY
```

These are not interchangeable.

### Player choice variables

```text
MOBILITY REQUIRED?
GOLD AVAILABLE?
WOOD AVAILABLE?
ENEMY RANGED SUPPORT?
MAP OPENNESS?
CURRENT INFRASTRUCTURE?
```

A spear-heavy response can be mechanically correct but strategically inadequate if the opponent can exploit mobility or ranged support.

This is exactly why Pass 45 distinguished **nominal counter** from **effective counter**.

---

# 11. Skirmisher-line — anti-ranged economic leverage

Official guidance identifies the Archer-line as effective against infantry and describes Skirmishers as one of the non-gold/low-cost bulk military families. citeturn3search1

Byzantines receive the -25% cost bonus on the Skirmisher line. citeturn1search3

The player-level strategic chain is:

```text
RANGED PRESSURE
→ NEED RANGED-DAMAGE RESPONSE
→ SKIRMISHER CANDIDATE
→ FOOD LEVERAGE
→ MASS / SUPPORT POSSIBILITY
```

But “mass” remains contextual.

The real bottlenecks can become:

```text
WOOD
FOOD
RANGE COUNT
UPGRADES
POPULATION
SURVIVAL
```

Thus the discount is best understood as **changing the economic feasibility frontier**, not guaranteeing a particular army composition.

---

# 12. Camel Rider — the most important Byzantine counter-transition case

Camel Rider and Heavy Camel Rider are central to this project because the historical HD archaeology already exposed a Byzantine-relevant threat response.

Installed AEGIS data:

```text
Camel Rider       329
Heavy Camel Rider 330
camel-line        [1755, 329, 330, 207]
base cost         55 food + 60 gold
train time        22 seconds
production        Stable 101
```

The Byzantine discount reduces the food burden while leaving gold as a major cost.

## 12.1 Player decision

```text
ENEMY MOUNTED THREAT
        ↓
WHAT IS THE SCALE?
        ↓
SPEAR OR CAMEL?
        ↓
CAN I AFFORD GOLD?
        ↓
DO I NEED MOBILITY?
        ↓
WHAT SUPPORT DOES THE ENEMY HAVE?
```

This is far richer than:

```text
cavalry → camel
```

## 12.2 Historical HD mapping

The historical chain is unusually concrete:

```text
THREAT AGGREGATE
→ contextual production rules
→ camel-set / production-state checks
→ can-train / resource / age / research gates
→ traincamel
```

This is **STRONG historical evidence** for a selected threat→capability response.

## 12.3 What remains unproven

It is not proven that historical HD explicitly compared:

```text
camel
vs
spear
vs
monk
vs
static defense
vs
own cavalry
```

under a common scoring function.

That distinction remains critical.

---

# 13. Knight / Cavalier / Paladin branch

The Byzantine roster retains the generic Knight line through Paladin in the current installed technology topology.

This gives Byzantines a second mounted family distinct from Camel Riders and Cataphracts.

Strategically:

```text
KNIGHT LINE
= GENERAL HEAVY CAVALRY CAPABILITY

CAMEL LINE
= MOUNTED COUNTER SPECIALIZATION

CATAPHRACT
= ANTI-INFANTRY HEAVY CAVALRY SPECIALIZATION
```

These distinctions are more useful than grouping everything under “cavalry.”

The player can choose among different **capability functions**, not just unit families.

---

# 14. Cataphract — deep strategic interpretation

The Cataphract is frequently misunderstood when described only through its unit class.

Mechanical facts:

```text
cavalry
Castle production
high HP
anti-infantry bonus
anti-cavalry resilience
Logistica interaction
```

Strategic role:

```text
ANTI-INFANTRY
HEAVY COMBAT
FLANK / PENETRATION
```

The anti-cavalry-resistance property should be treated as **defensive resilience**, not as proof that Cataphracts are the civilization's primary cavalry counter.

This invariant remains binding.

## 14.1 Player use case

A strong conceptual use is:

```text
ENEMY INFANTRY CORE
→ CATAPHRACT CANDIDATE
→ FORCE CONCENTRATION
→ FLANK / CONTACT
→ ANTI-INFANTRY DAMAGE
→ SURVIVE COUNTER-CAVALRY RESPONSE
```

The final tactical chain is context dependent.

## 14.2 Why Cataphract is a Byzantine strategic asset

Community discussion repeatedly evaluates Cataphracts in the context of the entire Byzantine roster rather than in isolation. Historical player commentary specifically emphasizes their interaction with the civilization's broader cheap-unit economy and anti-infantry role. citeturn1search4

This supports a key player-strategy principle:

> **A unit's strategic value is partly a property of the civilization-wide composition ecosystem in which it operates.**

That statement is strategic inference, not a direct game rule.

---

# 15. Monks — control, sustain, and conversion

Monks should not be reduced to “healers.”

The Byzantine team bonus gives Monks +100% faster healing in the current reference data. citeturn1search3turn2search9

The player-facing capability classes are:

```text
HEALING
CONVERSION
RELIC ECONOMY
TECHNOLOGY SUPPORT
```

These have different strategic functions.

## 15.1 Healing

Healing can increase effective army persistence.

Conceptually:

```text
DAMAGE TAKEN
→ HEALING
→ SURVIVING HIT POINTS
→ LESS REPLACEMENT PRESSURE
```

It does not mean the monk itself wins the engagement.

## 15.2 Conversion

Conversion is a control capability with high target and survival dependency.

Therefore:

```text
MONK
≠
DIRECT COMBAT COUNTER
```

## 15.3 Relics

Relics are long-term economic assets, particularly relevant when gold becomes constrained. Official economy guidance identifies relics as a long-term source of gold. citeturn3search1

This introduces a macro transition:

```text
MAP CONTROL
→ RELIC ACCESS
→ LONG-HORIZON GOLD
→ SUSTAINED GOLD COMPOSITIONS
```

Again, this is not free value: obtaining and protecting relics has opportunity cost and positional risk.

---

# 16. Siege — broad but bounded

Current installed topology establishes:

```text
Onager
Bombard Cannon
Trebuchet
```

while Siege Onager is unavailable in the Byzantine technology tree.

The strategic consequence is:

```text
BROAD SIEGE ACCESS
≠
MAXIMUM SIEGE ACCESS
```

This is an important counter-ontology point.

## 16.1 Onager

Primary strategic uses:

```text
ANTI-RANGED
AREA DAMAGE
FORMATION PUNISHMENT
```

Official guidance describes Mangonel-class siege as effective against ranged units and capable of pressuring structures from range. citeturn3search1

## 16.2 Bombard Cannon

Bombard Cannon adds a different long-range and anti-siege/building capability profile.

Its presence is contingent on its research prerequisite, so it should not be treated as an immediately available Imperial default.

## 16.3 Trebuchet

Trebuchets are the principal long-range building pressure tool in Imperial Age and are produced from Castles. Official guidance emphasizes their role against Castles and Town Centers. citeturn3search1

---

# 17. Naval Byzantines — major current-version correction

This pass must explicitly use the post-2026 naval model.

Update 169123 introduced the major naval overhaul and new Hulk-line counter relationships. It also changed warship technology progression and ship combat mechanics. citeturn3search0

For Byzantines, the official update increased the Fire Ship and Dromon attack-speed civilization bonus from +20% to **+25%**. citeturn3search0

Earlier Update 83607 established that Byzantines gained Dromons and that the Fire Ship 25% attack-speed bonus also applied to Dromons; the current 2026 update further formalized the bonus at 25% in the current balance baseline. citeturn2search10turn3search0

## 17.1 Current naval strategic model

The player should now think in terms of:

```text
FIRE-SHIP / DROMON TEMPO
vs
HULK-LINE COUNTER
vs
LONGER-RANGE SHIPS
vs
SHORELINE SIEGE
```

The new Hulk-line specifically counters Fire Ships while being vulnerable to longer-ranged ships such as Galleys. citeturn3search0

Therefore:

```text
BYZANTINE NAVAL BONUS
≠
AUTOMATIC NAVAL DOMINANCE
```

It creates a **rate advantage** inside a changing counter topology.

## 17.2 Greek Fire

Current structured reference lists Greek Fire as:

```text
Fire Ships +1 range
Dromons + increased blast radius
Bombard Towers + increased blast radius
```

citeturn1search3

Official Update 87863 confirms the modern effect wording. citeturn2search0

This makes Greek Fire a multi-domain technology:

```text
NAVAL RANGE
+
NAVAL AREA EFFECT
+
STATIC DEFENSE AREA EFFECT
```

Its strategic value is therefore state dependent.

---

# 18. Defense as a tempo mechanism

A key Byzantine strategic insight is that defense should not be treated as passivity.

A defensive structure has value when it changes the timing of an interaction.

Conceptually:

```text
ATTACK ARRIVES
→ STRUCTURE SURVIVES LONGER
→ ENEMY SPENDS MORE TIME / DAMAGE
→ DEFENDER GAINS RESPONSE WINDOW
```

The player can then convert that window into:

```text
COUNTER PRODUCTION
AGE-UP
REINFORCEMENT
REPOSITIONING
SIEGE
MONKS
```

This is a **tempo-defense** interpretation.

It is not a direct civilization description.

---

# 19. Byzantine map strategy

Map value should be decomposed into:

```text
RESOURCE ACCESS
MOVEMENT ACCESS
INFORMATION ACCESS
PRODUCTION POSITION
DEFENSIVE POSITION
ATTACK ROUTES
RETREAT ROUTES
```

Byzantines benefit particularly from turning defensive infrastructure into persistent control of important areas.

However, building durability alone does not make a location valuable.

A strong position must connect:

```text
STRUCTURE
+
RESOURCE / ROUTE
+
VISION
+
MILITARY SUPPORT
```

This follows the Pass-48 optionality model.

---

# 20. Open-map versus closed-map implications

The exact optimal strategy varies by map, but the mechanical tendencies can be characterized.

## Open maps

Key problems:

```text
RAIDING
MOBILITY
RESOURCE EXPOSURE
SCOUTING
REACTION TIME
```

Byzantine vision and flexible counter families become particularly relevant.

## Closed maps

Key problems shift toward:

```text
TECHNOLOGY
SIEGE
ECONOMY
LATE-GAME COMPOSITION
```

The broad technology tree and Imperial discount become relatively more important.

These are strategic generalizations, not universal matchup rules.

---

# 21. Byzantine counter ontology

A Byzantine response should be classified across multiple counter dimensions.

| Target problem | Candidate capability | Mechanical relationship | Strategic function | Major constraint |
|---|---|---|---|---|
| Cavalry | Spear line | anti-mounted | cheap defensive mass | mobility / ranged support |
| Cavalry | Camel line | anti-mounted specialization | mobile counter | gold |
| Cavalry | Monk | conversion/control | high-value target denial | monk survival / target |
| Cavalry | Static defense | positional | delay / protection | location |
| Infantry | Cataphract | anti-infantry | heavy mobile damage | food/gold/Castle |
| Infantry | Archer/Skirmish support | ranged damage | kiting / support | protection / target profile |
| Ranged | Skirmisher | anti-ranged | low-food response | wood / range / upgrades |
| Ranged | Cavalry | mobility | close distance / raid | gold / counter-cavalry |
| Buildings | Siege | structural pressure | breach / denial | protection / siege cost |
| Massed units | Onager / area effect | area damage | formation punishment | friendly-fire / positioning |
| Naval fire ships | Hulk counter topology | current naval mechanics | deny fire-ship advantage | water composition |

This table is a research ontology, not an executable priority list.

---

# 22. Counter choice is a state problem

The player never sees only:

```text
ENEMY = CAVALRY
```

They see something closer to:

```text
ENEMY CAVALRY
+
NUMBER
+
UPGRADES
+
SUPPORT
+
POSITION
+
MAP
+
OWN ECONOMY
+
OWN INFRASTRUCTURE
+
TIMING
+
NEXT THREAT
```

Thus:

```text
COUNTER SELECTION
=
STATE-DEPENDENT CAPABILITY SELECTION
```

This is the central strategic bridge between player reasoning and AEGIS architecture.

---

# 23. Composition is a system, not a unit list

A Byzantine army should be evaluated as:

```text
CORE CAPABILITY
+
SUPPORT CAPABILITY
+
COUNTER-CAPABILITY
+
SIEGE / CONTROL
+
REINFORCEMENT RATE
+
POSITION
```

Example conceptual compositions:

```text
SPEAR + SKIRM
= anti-mounted + anti-ranged support

CAMEL + SKIRM
= mobile anti-mounted + ranged support

CATAPHRACT + MONK
= heavy anti-infantry + sustain/control

CATAPHRACT + SIEGE
= mobile heavy force + area/structure pressure
```

These are capability examples, not recommended fixed compositions.

---

# 24. Transition strategy

Byzantines have an unusually rich transition surface.

The player can move between:

```text
SPEAR
↔ CAMEL
↔ KNIGHT
↔ CATAPHRACT

SKIRMISH
↔ ARCHER SUPPORT
↔ SIEGE

LAND
↔ NAVAL

MILITARY
↔ TECHNOLOGY
↔ IMPERIAL
```

The cost of transition includes:

```text
RESOURCE
TECH
INFRASTRUCTURE
PRODUCTION DISRUPTION
TIMING
MOMENTUM
RISK
```

The Byzantine player should therefore prefer transitions that reuse infrastructure when the tactical problem allows it.

Examples:

```text
Camel → Heavy Camel
```

has high family/infrastructure continuity.

Whereas:

```text
Skirmisher → Cataphract
```

requires a different production ecosystem and resource structure.

---

# 25. Vertical versus lateral transition

A useful player distinction is:

### Vertical transition

```text
Knight → Cavalier → Paladin
Camel → Heavy Camel
Cataphract → Elite Cataphract
```

Infrastructure and strategic identity remain relatively continuous.

### Lateral transition

```text
Spear → Camel
Skirmisher → Siege
Ranged → Cataphract
```

The new branch solves a different problem and may require new infrastructure/resource allocation.

This is a major transition-cost variable.

---

# 26. Byzantine strategic tempo

Tempo should be treated as the ability to turn resources and decisions into useful capability before the opponent can invalidate them.

Byzantine-specific tempo mechanisms include:

```text
CHEAPER SELECTED FOOD COSTS
+
FREE VISION TECH
+
DURABLE BUILDINGS
+
BROAD TECHNOLOGY ACCESS
+
LOWER IMPERIAL COST
+
FAST-ATTACK NAVAL BONUS
```

None is sufficient alone.

The strategic power emerges from interaction.

This is one reason why civilization analysis must be done at the **system level** rather than unit-by-unit.

---

# 27. Byzantine strategy as a capability graph

The complete player model can now be expressed as:

```text
ENEMY / MAP / ECONOMY STATE
            ↓
       THREAT / OBJECTIVE
            ↓
    REQUIRED CAPABILITY
            ↓
  ┌─────────┼───────────┐
  ↓         ↓           ↓
SPEAR     CAMEL      CATAPHRACT
  ↓         ↓           ↓
SKIRM     SUPPORT     MONK
  └─────────┼───────────┘
            ↓
          SIEGE
            ↓
       IMPERIAL PATH
            ↓
       LATE-GAME STATE
```

The graph is deliberately capability-based rather than unit-target hardcoding.

---

# 28. Historical HD AI cross-reference — economy

Historical HD archaeology demonstrates several economic control mechanisms:

```text
escrow
resource thresholds
resource allocation
age conditions
research-pending
production feasibility
```

Escrow specifically demonstrates a pattern in which resources can be protected for future research/capability rather than consumed immediately.

Player semantic:

```text
“I need to preserve resources for the next capability.”
```

Historical representation:

```text
ESCROW STATE
→ CAN-RESEARCH-WITH-ESCROW
→ RESEARCH
→ STATE UPDATE
```

**Coverage:** STRONG control correspondence; no proof of a generalized economic utility optimizer.

---

# 29. Historical HD AI cross-reference — scouting

Historical `scoutcontrol.per` includes:

```text
scout groups
geometry
path analysis
dangerous local units/buildings
archers
spears
TCs
candidate pivots
movement-point selection
commands
```

Player semantic:

```text
“I need information, but the scout must survive and route efficiently.”
```

Historical representation:

```text
SCOUT STATE
→ GEOMETRY / DANGER CONDITIONS
→ CANDIDATE MOVEMENT
→ COMMAND
```

**Coverage:** STRONG movement/control; PARTIAL strategic information valuation.

---

# 30. Historical HD AI cross-reference — cavalry detection

Historical `threats.per` aggregates enemy mounted categories into strategic-number channels.

Player semantic:

```text
“They are investing in cavalry; I need to account for that.”
```

Historical representation:

```text
ENEMY UNITS
→ CLASSIFICATION
→ CAVALRY AGGREGATE
→ DOWNSTREAM RULES
```

**Coverage:** STRONG threat-state representation.

**Missing:** explicit probabilistic belief / confidence model.

---

# 31. Historical HD AI cross-reference — Byzantine camel response

This is the most direct player/AI correspondence identified in the Byzantine archaeology.

Player semantic:

```text
Enemy mounted pressure is material.
I need mounted-threat mitigation.
Camels are feasible and appropriate.
Produce them.
```

Historical evidence:

```text
CAVALRY / CAVARCHER THREAT STATE
→ contextual camel conditions
→ own camel-set state
→ resource / age / research / availability gates
→ traincamel
```

**Coverage:** STRONG selected decision chain.

**Not proven:** generalized counter optimizer.

---

# 32. Historical HD AI cross-reference — Cataphract

The historical archaeology does not yet show an equally strong dedicated:

```text
INFANTRY THREAT
→ CATAPHRACT OPTIMIZATION
```

chain.

The unit exists in the civilization's capability surface, but the evidence currently does not prove that historical HD dynamically evaluates Cataphracts as a strategic response to infantry in the same explicit way that camel production is linked to mounted threat state.

Therefore:

```text
CATAPHRACT AVAILABILITY
= DIRECT

CATAPHRACT ANTI-INFANTRY ROLE
= DIRECT / COMPOSED

HISTORICAL HD INFANTRY→CATAPHRACT DECISION CHAIN
= NOT YET CLOSED
```

This is a major research gap for Pass 50/51.

---

# 33. Historical HD AI cross-reference — defensive buildings

Historical building archaeology found a primary-execution/fallback motif:

```text
BUILD INTENT
→ PRIMARY EXECUTION
→ FAILURE
→ FALLBACK
```

The Byzantine building HP bonus is not itself a historical AI decision variable.

But the player semantic effect is:

```text
DEFENSIVE STRUCTURE
→ MORE DURABLE POSITION
→ MORE TIME TO RESPOND
```

The historical AI has building execution and failure recovery mechanisms, but no evidence yet proves that it explicitly values Byzantine building HP as strategic tempo.

Therefore:

**Civilization mechanic:** DIRECT.  
**Player strategic interpretation:** COMPOSED.  
**Historical AI exploitation of that specific Byzantine advantage:** UNCERTAIN.

---

# 34. Historical HD AI cross-reference — Imperial transition

Historical HD contains age state, research state, resource control, escrow, and transition-dependent production/building logic.

This maps strongly to the mechanics of an age transition.

However, the specific Byzantine -33% Imperial cost is a civilization property, and historical archaeology has not yet proven that the HD controller explicitly reasons:

```text
“Byzantines should reach Imperial earlier because their age-up cost is discounted.”
```

Therefore:

```text
AGE TRANSITION CONTROL = STRONG
BYZANTINE-SPECIFIC COST VALUATION = NOT ESTABLISHED
```

This distinction matters.

---

# 35. Historical HD AI cross-reference — naval strategy

The current naval mechanics changed substantially in 2026.

Historical HD source archaeology is therefore insufficient by itself to infer current Byzantine naval policy.

The current official game now has a changed naval topology, including the Hulk-line and revised ship upgrades. citeturn3search0

Therefore:

```text
CURRENT NAVAL MECHANICS
= CURRENT OFFICIAL DATA

HISTORICAL HD NAVAL POLICY
= SEPARATE RESEARCH QUESTION
```

No historical naval rule should be assumed current without validation.

---

# 36. Historical AI semantic bridge — complete Byzantine loop

The strongest combined player/AI model is now:

```text
GAME WORLD
↓
SCOUT / OBSERVE
↓
THREAT / MAP / ECONOMIC STATE
↓
REQUIRED CAPABILITY
↓
BYZANTINE CANDIDATE SET
↓
AGE / TECH / BUILDING / RESOURCE / TIME FILTERS
↓
EVALUATION
↓
COMMITMENT
↓
HISTORICAL HD AUTHORITY
↓
PRODUCTION / RESEARCH / BUILD / ATTACK
↓
WORLD CHANGE
↓
REASSESSMENT
```

The first half is largely the player-strategy abstraction.

The middle is where historical HD shows selected implementations.

The final verification loop remains incompletely evidenced.

---

# 37. The most important Byzantine strategic distinction

A Byzantine player should not ask:

> **“What is the Byzantine counter to X?”**

The stronger question is:

> **“What capability solves the current problem at acceptable cost, timing, risk, and commitment given the capability set I already possess?”**

This creates the Byzantine decision function:

```text
THREAT
+
OBJECTIVE
+
CURRENT CAPABILITY
+
RESOURCE STATE
+
TECH STATE
+
INFRASTRUCTURE
+
MAP
+
TIMING
+
RISK
        ↓
RESPONSE SET
        ↓
CHOOSE
```

That is the correct player-perspective bridge to Pass 50.

---

# 38. What makes Byzantines unusually interesting for AEGIS

The civilization exposes nearly every major strategic concept the project needs to understand.

### Information

Free vision technologies.

### Defense

Durable structures.

### Economic asymmetry

Selective food discounts.

### Counter selection

Spear / Camel / Monk / positional alternatives.

### Heavy specialization

Cataphract anti-infantry capability.

### Technology breadth

Near-complete technology tree.

### Transition economics

Many overlapping production branches.

### Temporal strategy

Discounted Imperial transition.

### Resource scarcity

Gold-dependent elite capabilities.

### Position

Defensive infrastructure and mobility choices.

### Naval specialization

Fire Ship / Dromon attack-rate advantage.

### Control

Monk conversion/healing.

### Siege

Broad but bounded late-game access.

This makes Byzantines an unusually good civilization through which to study strategic decision architecture.

---

# 39. Byzantine capability families — final ontology

The player-level ontology emerging from this research is:

```text
SURVIVAL
├── durable buildings
├── spear
├── skirmisher
└── monks

ANTI-MOUNTED
├── spear
├── camel
├── monk / conversion
├── positional defense
└── mixed response

ANTI-RANGED
├── skirmisher
├── cavalry
├── siege
└── positional response

ANTI-INFANTRY
├── Cataphract
├── ranged support
├── siege
└── mixed response

SIEGE / STRUCTURE
├── Onager
├── Bombard Cannon
└── Trebuchet

CONTROL / SUSTAIN
├── Monk
├── healing
└── conversion

NAVAL
├── Fire Ship
├── Dromon
└── current naval counter topology

MACRO / TEMPO
├── selective food discount
├── free vision
├── building HP
└── Imperial cost reduction
```

This ontology is intended for research, not direct code generation.

---

# 40. Hard strategic invariants

The following should now be treated as project invariants.

### Invariant 1

```text
Cataphract mechanical family = cavalry
Cataphract strategic role = anti-infantry / heavy combat
```

### Invariant 2

```text
Byzantine -25% unit discount
= selective cost leverage
≠ 25% stronger economy
```

### Invariant 3

```text
Technology-tree presence
≠ current feasibility
```

### Invariant 4

```text
Nominal counter
≠ effective counter
```

### Invariant 5

```text
Command
≠ world outcome
```

### Invariant 6

```text
Threat aggregate
≠ probabilistic belief
```

### Invariant 7

```text
Historical response chain
≠ universal optimizer
```

### Invariant 8

```text
Current naval mechanics
must be validated against the post-2026 naval system
```

### Invariant 9

```text
Layer 2 research
≠ Layer 3 implementation
```

---

# 41. Hostile QC

## QC-1 — Did we confuse Byzantines with AoE4 Byzantines?
**PASS.** Current player analysis is AoE2:DE. AoE4 Byzantine material was excluded from the AoE2 mechanics model.

## QC-2 — Did we use outdated naval rules?
**PASS.** Current official February 2026 naval overhaul is explicitly incorporated. citeturn3search0

## QC-3 — Did we call Cataphracts anti-cavalry because they resist cavalry?
**PASS.** No. Defensive anti-cavalry resilience is separated from offensive strategic role.

## QC-4 — Did we call camels cheap because they receive the food discount?
**PASS.** Gold burden remains explicit.

## QC-5 — Did we treat the near-complete tech tree as automatic strategic superiority?
**PASS.** Breadth is separated from feasibility and opportunity cost.

## QC-6 — Did we treat free Town Patrol as automatic map control?
**PASS.** It is treated as improved information availability and response opportunity.

## QC-7 — Did we infer that historical HD explicitly optimized every Byzantine advantage?
**PASS.** Byzantine-specific historical exploitation is marked separately from generic HD mechanisms.

## QC-8 — Did we mistake historical camel production for universal counter selection?
**PASS.** It is explicitly classified as a strong selected response chain.

## QC-9 — Did we mistake unit availability for strategic intent?
**PASS.** Availability and strategic role are separated.

## QC-10 — Did we cross Layer 2 into implementation?
**PASS.** No `.per`, controller, production policy, or runtime artifact created.

---

# 42. Deepening pass — the Byzantine “defensive” label is insufficient

The official/current data classifies Byzantines as defensive. citeturn1search3

But a player-level model must not stop there.

Defense is a **means**, not a complete strategy.

The civilization can use defensive advantages to create:

```text
TIME
→ INFORMATION
→ RESOURCE ACCUMULATION
→ COUNTER SELECTION
→ TECHNOLOGY
→ IMPERIAL TRANSITION
→ OFFENSIVE CAPABILITY
```

Therefore a better strategic identity is:

> **defensive resilience converted into adaptive response and eventual power concentration.**

This is an AEGIS strategic synthesis, not a direct official description.

---

# 43. Deepening pass — “adaptive” must be constrained

It is tempting to call Byzantines an “adaptive civilization.”

That is directionally useful but dangerous if interpreted as:

```text
CAN BUILD EVERYTHING
→ CAN ALWAYS ADAPT
```

The correct player model is:

```text
BROAD OPTION SPACE
+
RESOURCE CONSTRAINT
+
TIME CONSTRAINT
+
INFRASTRUCTURE CONSTRAINT
+
TECH CONSTRAINT
+
MAP CONSTRAINT
+
OPPONENT PRESSURE
```

Therefore Byzantine adaptation is a **feasibility problem**.

The best response may be unavailable in time even when it exists in the technology tree.

---

# 44. Deepening pass — the Byzantine discount is an allocator, not merely a discount

A deeper economic interpretation is:

```text
SELECTIVE DISCOUNT
→ CHANGES MARGINAL COST
→ CHANGES RELATIVE ATTRACTIVENESS
→ CHANGES RESOURCE ALLOCATION
→ CHANGES COMPOSITION FEASIBILITY
```

The bonus therefore potentially influences **what the economy can support simultaneously**.

This is more strategically meaningful than unit-level price reduction.

It also explains why the Byzantine food discount should eventually be modeled at the **composition and transition level**, not merely attached as a unit metadata field.

---

# 45. Deepening pass — information + option value

Free vision technologies become more valuable because Byzantines possess a broad response surface.

Conceptually:

```text
MORE INFORMATION
→ EARLIER STATE KNOWLEDGE
→ MORE TIME TO SELECT
→ MORE VALUE FROM MULTIPLE AVAILABLE CAPABILITIES
```

A narrow civilization may detect an enemy early but have few practical responses.

Byzantines can potentially convert the same information into a broader feasible response set.

This is a major AEGIS-generalization:

> **Information value depends partly on the quality and breadth of the action set it can inform.**

Not a historical AI claim.

---

# 46. Deepening pass — defensive infrastructure + information

The strongest Byzantine system-level synergy may be:

```text
VISION
+
DURABLE STRUCTURES
+
COUNTER ECONOMICS
```

A conceptual response sequence is:

```text
DETECT
↓
DELAY
↓
ALLOCATE
↓
PRODUCE
↓
INTERCEPT
```

This is more strategically expressive than simply saying “Byzantines defend well.”

Historical HD already contains pieces of this sequence:

```text
observation
→ threat state
→ resource / production gates
→ response
```

The exact Byzantine-specific structural synergy remains a research inference.

---

# 47. Deepening pass — the real Byzantine decision tree

At a high level, a Byzantine player is repeatedly solving:

```text
WHAT IS THE OPPONENT DOING?
        ↓
WHAT DO I NEED TO SURVIVE / WIN THE NEXT INTERACTION?
        ↓
WHAT CAPABILITIES CAN SOLVE IT?
        ↓
WHICH ARE CURRENTLY FEASIBLE?
        ↓
WHICH FIT MY EXISTING INFRASTRUCTURE?
        ↓
WHICH PRESERVE MY NEXT OPTION?
        ↓
WHICH ARRIVES BEFORE THE THREAT MATTERS?
        ↓
COMMIT
        ↓
VERIFY
        ↓
REASSESS
```

This is the player-strategy core that Pass 50 should operationalize as a research matrix.

---

# 48. Deepening pass — historical HD coverage matrix

| Byzantine player concept | Mechanical basis | HD evidence | Coverage |
|---|---|---|---|
| Strong defense | building HP bonus | building execution/fallback | PARTIAL |
| Early information | free Town Watch/Patrol | scout control / facts | STRONG generic / Byzantine-specific UNCERTAIN |
| Counter cavalry with spears | discounted spear line | threat/production architecture | STRONG generic |
| Counter cavalry with camels | discounted camel line | cavalry→camel production chain | **STRONG Byzantine-relevant** |
| Anti-ranged with skirms | discounted skirm line | production/feasibility mechanisms | STRONG generic / civ-specific UNCERTAIN |
| Anti-infantry with Cataphracts | Cataphract + Logistica | Cataphract availability; no closed infantry-response chain yet | PARTIAL |
| Monk sustain/control | faster healing + conversion | monk state exists; strategic valuation incomplete | PARTIAL |
| Siege response | broad siege access | production/research controls | STRONG generic / civ-specific partial |
| Imperial acceleration | -33% Imperial cost | age/escrow/research state | STRONG generic / civ-specific UNCERTAIN |
| Naval tempo | +25% Fire Ship/Dromon attack speed | current naval mechanics; historical AI naval policy separate | CURRENT MECHANIC DIRECT / AI PARTIAL |
| Adaptive transitions | broad tree | distributed transition controls | PARTIAL |
| Strategic optionality | broad tree + multiple counters | historical alternatives exist | INFERRED / PARTIAL |
| Belief-based adaptation | scouting + threat state | threat aggregates | PARTIAL; belief NOT ESTABLISHED |

---

# 49. What the HD AI understands about Byzantines — current evidence

The strongest defensible statement is:

> **Historical HD AI can represent and act on selected Byzantine-relevant capability relationships, especially mounted-threat aggregation and camel production, while also possessing generic mechanisms for scouting, production feasibility, research, resource control, attack/retreat, and temporal reassessment.**

What is not established is that it has a unified internal representation of:

```text
“Byzantine strategic identity”
```

or:

```text
“adaptive Byzantine strategy”
```

Those are player-level and AEGIS-level abstractions.

---

# 50. What a future Byzantine research model must measure

Before Layer 3, the research should eventually quantify:

```text
UNIT COST
TRAIN TIME
UPGRADE COST
TECH COST
BUILDING COST
BUILDING TIME
RESOURCE INCOME
COUNTER DAMAGE
ARMOR INTERACTION
RANGE
SPEED
REINFORCEMENT RATE
SURVIVAL
TRANSITION COST
MAP DEPENDENCE
```

And at the strategic level:

```text
THREAT MAGNITUDE
RESPONSE WINDOW
CURRENT CAPABILITY
CAPABILITY GAP
FEASIBLE CANDIDATES
TRANSITION BURDEN
OPTION VALUE
RISK
COMMITMENT
EXPECTED OUTCOME
ACTUAL OUTCOME
```

This is the research bridge into Pass 50 and later Pass 51.

---

# 51. Six-month re-entry test

A future engineer returning to this artifact should be able to answer:

1. What are the Byzantine civilization's current major bonuses?
2. Which unit families receive the -25% discount?
3. Why is that a food-leverage mechanic rather than a generic 25% economic bonus?
4. What does the building HP bonus strategically buy?
5. What is the importance of free Town Watch/Town Patrol?
6. Why is the -33% Imperial cost strategically significant but not equivalent to guaranteed faster Imperial?
7. What are the three major mounted capability branches and how do they differ?
8. Why are Cataphracts not classified as the primary anti-cavalry branch?
9. What does Logistica change?
10. Why are Monks a control/sustain capability rather than a normal counter line?
11. What are the current major Byzantine siege boundaries?
12. What changed in the 2026 naval system?
13. What is the current Byzantine Fire Ship/Dromon attack-speed bonus?
14. What is the strongest historical HD Byzantine response chain currently proven?
15. Which Byzantine strategic behaviors remain only partially mapped to HD AI?
16. Why is the technology tree not equivalent to immediate strategic feasibility?
17. Why must counter choice be modeled as a state problem?
18. What is the difference between historical HD evidence and AEGIS strategic generalization?
19. Was any Layer-3 implementation created?
20. What must Pass 50 now do with this research?

If these cannot be answered, the artifact should be reopened.

---

# 52. Final verdict

**PASS — BYZANTINE PLAYER MECHANICS / STRATEGY MODEL SUBSTANTIALLY ESTABLISHED.**

The central conclusion is:

> **Byzantines are not strategically defined by one “best unit” or one defensive behavior. Their power is an interacting system of durable infrastructure, improved baseline information, selective food-cost leverage, unusually broad technology access, multiple distinct counter-capability families, heavy anti-infantry cavalry, control/sustain tools, broad but bounded siege, specialized naval tempo, and a discounted Imperial transition.**

From the player perspective, the civilization is fundamentally a **capability-selection problem under changing constraints**.

From the historical HD-AI perspective, meaningful pieces of that problem are demonstrably represented through:

```text
OBSERVATION
→ THREAT AGGREGATION
→ STATE
→ FEASIBILITY
→ RESOURCE / TECHNOLOGY CONTROL
→ PRODUCTION
→ TEMPORAL CONTROL
→ ATTACK / RETREAT
→ REASSESSMENT
```

The strongest Byzantine-specific historical bridge currently proven is:

```text
ENEMY MOUNTED PRESSURE
→ CAVALRY THREAT STATE
→ CAMEL PRODUCTION CONDITIONS
→ FEASIBILITY GATES
→ TRAIN CAMEL
```

The major remaining research gap is not “what units exist.” It is:

> **How the full Byzantine capability surface should be selected, compared, transitioned between, and verified under actual player-level strategic conditions.**

That is exactly the problem Pass 50 should attack.

**Layer-2 implementation remains ZERO.**

**Next:** Pass 50 — Byzantine Strategic Decision Matrix.
