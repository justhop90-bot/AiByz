# AEGIS Layer 2 — Pass 44
# Byzantine Strategic Profile — Archaeological Baseline

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory archaeology + current game-data corroboration  
**Predecessor:** Pass 43 Historical Strategic Control-State Atlas  
**Primary code source:** verified `AI (HD version).per` + verified Promisory modules  
**Current data source:** installed AoE2DE `BYZANTINES.json` / game data  
**Status:** PASS — Byzantine strategic capability surface substantially mapped  
**Implementation status:** **ZERO**. No `.per` implementation is created or authorized by this pass.

---

## 0. Boundary

This pass is research only.

The objective is to understand what makes the Byzantines strategically distinct before Layer 3 architecture is constructed. This document does **not** prescribe a controller implementation, production script, build order, or `.per` design.

The governing research question is:

```text
BYZANTINE BONUS
      ↓
AVAILABLE CAPABILITY
      ↓
RESOURCE / PRODUCTION CONSEQUENCE
      ↓
COUNTER RELATIONSHIP
      ↓
TACTICAL ROLE
      ↓
STRATEGIC OPTION
      ↓
TRANSITION CONDITION
      ↓
MAP / POSITION CONSEQUENCE
```

The key requirement is to distinguish three things:

1. **Civilization fact** — directly present in game data or authoritative patch documentation.
2. **Strategic consequence** — composed from those facts and unit relationships.
3. **AEGIS interpretation** — a future design hypothesis, not historical Byzantine intent.

---

# 1. Executive finding

The Byzantines should not be modeled as simply a “defensive civilization.” That label is too coarse for engineering purposes.

The current evidence supports a more precise characterization:

> **A broad-access civilization whose strategic value comes from unusually cheap counter-capabilities, durable infrastructure, strong defensive information, and a wide late-game option surface, with major power concentrated in the ability to change the composition of the army without abandoning the existing economic/military base.**

This is an archaeological characterization, not a claim about developer intent.

The most important strategic property for AEGIS is therefore **optionality under pressure**.

The civilization has several mechanisms that reduce the cost of responding to an opponent:

- cheaper Camel Rider line,
- cheaper Skirmisher line,
- cheaper Spearman line,
- durable buildings,
- free Town Watch / Town Patrol,
- broad technology access,
- access to both standard cavalry and regional Camel Rider lines,
- Cataphracts,
- broad siege access,
- strong monk technology access,
- specialized naval firepower.

Official current/near-current patch history confirms the continuing Byzantine naval bonus: in February 2026 the Fire Ship and Dromon attack-speed bonus was increased to **25%**. citeturn0search2

The installed current civilization data independently confirms the breadth of the roster and technology surface, including Camel Rider, Heavy Camel Rider, Knight, Cavalier, Paladin, Cataphract, Elite Cataphract, Dromon, and extensive monastery/siege technologies.

---

# 2. Civilization capability ledger

| Capability | Current evidence | Strategic meaning | Confidence |
|---|---|---|---|
| Building HP scales by age | Historical/current Byzantine design; game-data corroboration required for exact modifier | Defensive infrastructure has higher persistence | HIGH for existence; exact current modifier requires direct modifier extraction |
| Camel Rider / Skirmisher / Spearman lines cost 25% less food | Established Byzantine civilization rule; corroborated by terminology discussion and historical balance record | Counter-unit production has unusually low food opportunity cost | HIGH |
| Town Watch free | Historical/current civilization rule | Earlier information acquisition without normal research expenditure | HIGH |
| Town Patrol free/instant | Official patch 51737 | Additional map/base information at no resource cost | HIGH citeturn2search14 |
| Fire Ships / Dromons attack 25% faster | Official February 2026 patch | High naval tempo and anti-ship pressure | HIGH citeturn0search2 |
| Broad technology tree | Installed `BYZANTINES.json`; official AoE2 learning page describes an almost full technology tree | High response-option breadth | HIGH citeturn2search3 |
| Cataphract / Elite Cataphract | Installed `BYZANTINES.json` | Dedicated heavy cavalry / anti-infantry option | HIGH |
| Camel Rider / Heavy Camel Rider | Installed `BYZANTINES.json` | Knight/cavalry counter branch with regional access | HIGH |
| Halberdier | Installed `BYZANTINES.json` | Cheap anti-mounted defensive mass | HIGH |
| Arbalester | Installed `BYZANTINES.json` | High-end ranged option | HIGH |
| Bombard Cannon | Installed `BYZANTINES.json`, prerequisite Chemistry | High-end siege / anti-siege / building pressure | HIGH |
| Onager | Installed `BYZANTINES.json` | Area-control siege option | HIGH |
| Trebuchet | Installed `BYZANTINES.json` | Long-range structure pressure | HIGH |
| Strong monastery access | Installed `BYZANTINES.json` | Healing, conversion, relic and support options | HIGH |
| Dromon | Installed `BYZANTINES.json`; official patch history | Specialized late-game naval siege | HIGH |

Important: exact numerical bonuses should be treated as data-version-specific. Where this pass does not have a direct modifier field from the installed data, it does not silently manufacture one.

---

# 3. The Byzantine economic signature

The defining economic feature is not a conventional income bonus.

The important mechanism is **reduced food expenditure on several counter-capability families**.

The three major lines are:

```text
CAMEL RIDER LINE
SKIRMISHER LINE
SPEARMAN LINE
```

All three belong to a common strategic pattern:

```text
ENEMY CAPABILITY
      ↓
COUNTER REQUIREMENT
      ↓
LOWER FOOD COST
      ↓
LOWER RESPONSE PRICE
      ↓
MORE DEFENSIVE OPTIONALITY
```

This is fundamentally different from a civilization whose bonus simply increases resource income.

A Byzantine economy can convert a given food stock into more counter-capability than an otherwise identical generic economy for these families.

The resulting strategic consequence is **resource substitution**:

```text
FOOD
 ↓
COUNTER UNITS
 ↓
LESS FOOD PRESSURE PER RESPONSE
 ↓
MORE ROOM FOR OTHER RESOURCES / TECHNOLOGY
```

This does **not** imply that Byzantines have unlimited food or that every counter is automatically optimal.

The correct interpretation is conditional:

> When one of the discounted lines is the correct capability for the current threat, the civilization's response cost is structurally reduced.

---

# 4. Defensive infrastructure as strategic capital

The building HP bonus should not be modeled merely as “buildings are tankier.”

The strategically relevant object is:

```text
BUILDING SURVIVABILITY
        ↓
TIME-TO-KILL
        ↓
TIME AVAILABLE FOR RESPONSE
        ↓
MILITARY / ECONOMIC REACTION WINDOW
```

A stronger building can therefore buy time rather than merely absorb damage.

That matters because Byzantine strategic systems contain evidence of:

- `underattack` state,
- defensive priorities,
- building recovery,
- retreat behavior,
- resource reallocation,
- military-state transitions.

Therefore the building bonus has a plausible composed interaction with the existing control network:

```text
LONGER INFRASTRUCTURE SURVIVAL
        ↓
MORE TIME BEFORE WORLD-STATE COLLAPSE
        ↓
MORE TIME FOR COUNTER-PRODUCTION
        ↓
MORE VALUE FROM DISCOUNTED COUNTER LINES
```

**Evidence grade:** COMPOSED.

**Strategic success:** not directly proven by the code alone.

Historical discussion also consistently identifies Byzantine building durability as an important defensive property, but community discussion is supporting evidence rather than authoritative game-data proof. citeturn1search11

---

# 5. Information as a Byzantine resource

Free Town Watch and Town Patrol are strategically more important than their resource cost suggests because they alter the information timeline.

The effect can be represented as:

```text
NORMAL CIVILIZATION
information
   ↓
research decision
   ↓
resource/time expenditure
   ↓
expanded vision

BYZANTINES
information
   ↓
expanded vision
```

Town Patrol was made free and instantly researched in Update 51737. citeturn2search14

This interacts naturally with the historical scouting architecture already reconstructed in Pass 43:

```text
INFORMATION
 → OBJECT OBSERVATION
 → THREAT CLASSIFICATION
 → RESPONSE
```

The Byzantine advantage is therefore not merely “more vision.”

It is:

> **less economic friction between an information requirement and obtaining the information.**

That is a strategically meaningful distinction.

---

# 6. Counter-capability portfolio

The Byzantine roster contains multiple response families that overlap in battlefield purpose.

## 6.1 Mounted threat

Relevant responses include:

- Camel Rider / Heavy Camel Rider
- Spearman / Pikeman / Halberdier
- Cataphract in some positional/compositional roles
- Monks where conversion is strategically viable
- ranged support depending on exact mounted target

The important point is not “build camels against cavalry.”

The actual decision space is:

```text
MOUNTED THREAT
     ↓
WHAT KIND OF MOUNTED THREAT?
     ├─ knight-line
     ├─ camel-line
     ├─ scout/light cavalry
     ├─ cavalry archer
     ├─ elephant
     └─ unique mounted unit
     ↓
WHAT RESPONSE CAPABILITY IS REQUIRED?
     ↓
WHICH RESPONSE HAS THE LOWEST TOTAL STRATEGIC COST?
```

This connects directly to the historical threat/capability research but is intentionally broader than the historical camel rule.

---

## 6.2 Archer threat

Relevant responses include:

- Skirmisher line
- Knights / cavalry
- Cataphracts in appropriate circumstances
- Siege in massed formations
- defensive positioning

The discounted Skirmisher line is especially important because the response can be generated without paying the normal food burden.

Therefore:

```text
ARCHER PRESSURE
 → SKIRMISHER DEFICIT
 → DISCOUNTED FOOD COST
 → SUSTAINED COUNTER-MASS
```

This is a civilization-specific strategic leverage point.

---

## 6.3 Infantry threat

The Byzantine response surface is unusually broad:

- Archers / Crossbowmen / Arbalesters
- Cavalry
- Cataphracts
- Siege
- appropriate trash/support combinations

Cataphracts deserve special treatment because they are not simply another cavalry unit. The installed technology tree identifies them as a unique unit with Elite Cataphract upgrade and associated technologies including Logistica.

Thus the decision is not merely unit-vs-unit. It is a composition problem:

```text
INFANTRY MASS
   ↓
RANGED DAMAGE?
   ↓
HEAVY CAVALRY?
   ↓
SIEGE?
   ↓
MIXED RESPONSE?
```

---

# 7. Byzantine mounted architecture

The installed current tech tree exposes a significant distinction that must not be collapsed:

```text
KNIGHT → CAVALIER → PALADIN

CAMEL RIDER → HEAVY CAMEL RIDER

CATAPHRACT → ELITE CATAPHRACT
```

These are three strategically different mounted branches.

### Knight-line
General heavy cavalry access.

### Camel-line
Counter-mounted capability with Byzantine food-cost leverage.

### Cataphract-line
Civilization-specific heavy cavalry with distinct battlefield specialization and Castle-based production requirements.

This means “cavalry” is not a sufficient strategic state variable for Byzantine planning.

The relevant distinction is:

```text
MOUNTED CAPABILITY FAMILY
```

and then:

```text
ROLE
COST
TECH REQUIREMENT
PRODUCTION LOCATION
TIMING
COUNTER PROFILE
SURVIVABILITY
MAP FUNCTION
```

This finding is strongly compatible with the historical discovery that `cavalry` in Promisory can itself be a mutable aggregate strategic channel. The aggregate is useful for threat detection, but it is not sufficient to describe the Byzantine response space.

---

# 8. Technology architecture

The installed Byzantine technology tree demonstrates unusually broad access.

Important current-data examples include:

- Arbalester
- Elite Skirmisher
- Cavalry Archer
- Heavy Cavalry Archer
- Halberdier
- Champion
- Hussar
- Cavalier
- Paladin
- Heavy Camel Rider
- Bombard Cannon
- Onager
- Trebuchet
- Dromon
- broad monastery technologies
- Chemistry
- Ballistics
- Treadmill Crane
- extensive economic upgrades

The official AoE2 learning material describes Byzantines as having an “almost full Technology Tree,” which independently supports the breadth finding. citeturn2search3

Strategically this means:

```text
HIGH OPTION COUNT
      ↓
LOWER RISK OF DEAD-END COMPOSITION
      ↓
MORE TRANSITION PATHS
      ↓
GREATER VALUE OF INFORMATION
```

But it also creates a decision problem:

```text
MORE OPTIONS
      ↓
MORE COMPETING RESOURCE SINKS
      ↓
MORE OPPORTUNITY COST
      ↓
GREATER NEED FOR CORRECT TRANSITION SELECTION
```

That tension is likely more important for AEGIS than the raw size of the tech tree.

---

# 9. Naval specialization

The Byzantine naval profile is now materially different from the older pre-Dromon picture.

Official Update 83607 added Dromon to Byzantines and extended the existing 25% Fire Ship attack-speed bonus to Dromons. citeturn2search13

The February 2026 Update 169123 increased the Fire Ship and Dromon attack-speed bonus from 20% to 25%. citeturn0search2

The installed data confirms Dromon as an Imperial Age regional unit and also shows Fire Ship, Fast Fire Ship, Galley, War Galley, Galleon, Demolition Ship, and Heavy Demolition Ship paths.

Therefore water strategy must not be treated as a generic copy of land strategy.

The Byzantine naval chain is better characterized as:

```text
WATER INFORMATION
      ↓
FIRE-SHIP / GALLEY RESPONSE
      ↓
FAST ATTACK-TEMPO ADVANTAGE
      ↓
NAVAL CONTROL
      ↓
DROMON / SIEGE TRANSITION
```

The exact transition thresholds remain a Layer-2 research question.

---

# 10. Siege architecture

The Byzantine current tree provides a broad siege surface:

```text
RAM
MANGONEL → ONAGER
SCORPION
BOMBARD CANNON
TREBUCHET
DROMON
```

The absence/presence pattern matters more than any single unit.

A Byzantine army can therefore solve some battlefield problems through **force substitution**:

```text
DIRECT COMBAT
       ↕
RANGED COMBAT
       ↕
SIEGE
       ↕
DEFENSIVE POSITION
```

This reinforces the strategic-optionality characterization.

The installed data specifically shows Bombard Cannon gated through Chemistry and Onager available through the Mangonel line, while Siege Onager is unavailable. That means the Byzantine late-game siege identity is not “maximum siege access”; it is **broad but bounded siege access**.

That distinction matters for future candidate evaluation.

---

# 11. Monastery architecture

The current data shows a deep monastery tree:

- Monk
- Redemption
- Atonement
- Sanctity
- Fervor
- Devotion
- Faith
- Heresy
- Illumination
- Block Printing
- Theocracy
- and other support technologies.

This creates another Byzantine strategic response dimension:

```text
RAW MILITARY FORCE
        ↓
SUPPORT / CONTROL FORCE
        ↓
CONVERSION / HEALING / RELIC ECONOMICS
```

The team bonus further increases monk healing speed; official patch history records the increase from +50% to +100%. citeturn2search12

This should not be interpreted as “always make monks.”

It means monk capability can have unusually high strategic value when the game state makes healing, conversion, or relic control relevant.

---

# 12. The central Byzantine strategic tension

The most important finding of this pass is not a bonus.

It is a tension between:

```text
BREADTH
vs.
COMMITMENT
```

Byzantines have many plausible answers.

That does not mean all answers are simultaneously affordable.

Therefore:

```text
MORE OPTIONS
      ↓
MORE CANDIDATES
      ↓
MORE OPPORTUNITY COST
      ↓
MORE VALUE FROM TIMING / INFORMATION
```

This is exactly where the historical Promisory architecture becomes relevant.

The historical system already contains:

- strategy state,
- strategy locking,
- strategy affinity,
- strategy type,
- attack-priority recomputation,
- threat aggregates,
- production flags,
- escrow,
- research gates,
- military state,
- position state,
- temporal reset behavior.

The Byzantine civilization then supplies a particularly rich action space for that distributed control network.

**Evidence:** COMPOSED.

**Historical intent:** not directly proven.

---

# 13. Byzantine strategic option surface

The research baseline can now be expressed as capability families rather than build orders.

| Family | Primary use | Byzantine leverage | Main constraint |
|---|---|---|---|
| Cheap spear line | Mounted denial | Food discount | Low direct offensive reach |
| Cheap skirmisher line | Archer denial | Food discount | Vulnerable to siege/melee |
| Cheap camel line | Cavalry denial | Food discount | Gold requirement / timing |
| Knight line | Mobile heavy cavalry | Broad access | Gold/food burden |
| Cataphract line | Heavy specialist cavalry | Unique access | Castle + gold/food + upgrade burden |
| Archer line | Ranged DPS | Broad upgrades | Food/gold and tech timing |
| Crossbow/Arbalester | High-quality ranged force | Strong tech access | Gold and upgrade timing |
| Halberdier | Heavy mounted denial | Cheap food response | Slow / vulnerable to ranged/siege |
| Siege | Area/structure control | Broad access | Wood/gold + mobility |
| Monks | Sustain/control | Deep tech access | Micro / gold / vulnerability |
| Defensive buildings | Delay / map control | HP bonus | Stone/wood and positional commitment |
| Naval fire ships | Water pressure | Attack-speed bonus | Water economy |
| Dromon | Naval siege | Attack-speed bonus + regional access | Imperial timing |

This table is a research abstraction. It is not a production policy.

---

# 14. Byzantine strategic transitions

The civilization's transition problem should be studied as capability replacement, not as a list of build orders.

Candidate transition classes are:

```text
RANGED → HEAVY CAVALRY
RANGED → SIEGE
RANGED → TRASH COUNTER
CAVALRY → CAMEL
CAVALRY → HALBERDIER
CAMEL → CATAPHRACT
TRASH → GOLD ARMY
DEFENSE → MAP CONTROL
LAND → WATER
WATER → LAND
```

No transition should be considered Byzantine doctrine merely because the roster permits it.

The research question is:

> Under what observable conditions does one capability become insufficient relative to another capability's cost and timing?

That is the actual bridge from civilization data to strategic reasoning.

---

# 15. Map implications

Byzantine map value should be treated as a capability multiplier.

## Open map

Likely values:

- information,
- mobile counter-capability,
- cheap spear/skirmisher/camel responses,
- defensive infrastructure where needed,
- ability to switch composition.

## Closed map

Likely values:

- durable structures,
- siege,
- monks,
- defensive position,
- technology breadth,
- late-game transition options.

## Water map

Likely values:

- early water information,
- fire-ship tempo,
- Dromon transition,
- naval siege pressure.

These are strategic hypotheses, not direct historical rules. They require empirical testing in later work.

---

# 16. What is genuinely Byzantine vs generic AoE2

This distinction is mandatory.

## Strongly Byzantine-specific

- discounted counter-unit families,
- building durability bonus,
- free vision technologies,
- Cataphract branch,
- Byzantine naval attack-speed bonus,
- Dromon access,
- unusually broad technology surface.

## Generic AoE2 mechanisms available to Byzantines

- resource allocation,
- scouting,
- threat measurement,
- production queues,
- attack/retreat control,
- siege selection,
- technology timing,
- positional control,
- economic expansion.

## Byzantine-specific strategic consequence of generic mechanisms

The important question is not whether Byzantines possess the generic mechanism.

It is whether the civilization's bonuses change its optimal use.

Example:

```text
GENERIC MECHANISM:
respond to cavalry with anti-cavalry.

BYZANTINE MODIFIER:
camel/spear response has lower food cost.

POTENTIAL STRATEGIC CONSEQUENCE:
response threshold may be lower because the opportunity cost is lower.
```

That last line is a hypothesis until formally demonstrated.

---

# 17. Integration with historical AI archaeology

The strongest existing historical mechanisms map naturally onto Byzantine capability families.

```text
HISTORICAL STATE
      ↓
THREAT AGGREGATE
      ↓
RESPONSE FLAG
      ↓
PRODUCTION FEASIBILITY
      ↓
UNIT PRODUCTION
```

The Byzantine civilization then supplies a richer candidate set:

```text
THREAT
 ↓
CAMEL / SPEAR / SKIRM / KNIGHT / CATAPHRACT / SIEGE / MONK / RANGED
```

But the historical source does **not** prove that its original programmer evaluated all of these as a unified candidate set.

That would be an AEGIS generalization.

This distinction is critical.

---

# 18. New research hypothesis: Byzantine optionality has measurable value

A useful Layer-2 hypothesis is:

> Byzantine civilization strength is partly represented by the number and quality of feasible responses remaining after the opponent's current threat and the player's current resource/technology state are applied.

Conceptually:

```text
OPTIONALITY
=
COUNT / QUALITY OF FEASIBLE CAPABILITIES
AFTER HARD CONSTRAINTS
```

This is **not** an implementation recommendation.

It is a research hypothesis for determining whether Byzantine strategy should be studied in terms of:

- response breadth,
- response cost,
- transition cost,
- timing,
- commitment reversibility,
- and information quality.

This may become one of the most useful bridges between civilization archaeology and later strategic architecture.

Evidence grade: AEGIS-GENERALIZATION.

---

# 19. Hostile review

## Claim attacked: “Byzantines are simply defensive.”

Rejected as insufficient.

The current roster and bonuses provide substantial offensive, mobile, siege, naval, and technology options.

## Claim attacked: “Cheap trash means spam trash.”

Rejected.

Discounted cost changes response economics; it does not establish optimal composition.

## Claim attacked: “Full tech tree means always flexible.”

Rejected as incomplete.

Option count increases opportunity cost and decision complexity.

## Claim attacked: “Free vision means Byzantines always know the enemy.”

Rejected.

Vision capability is not equivalent to successful scouting, interpretation, or complete information.

## Claim attacked: “Camel discount proves camel-first strategy.”

Rejected.

It proves lower response cost for the camel line, not a universal priority.

## Claim attacked: “Cataphracts are the Byzantine endgame.”

Rejected.

The roster supports many endgame branches.

## Claim attacked: “The historical AI already understood Byzantine optionality.”

Rejected.

The historical code demonstrates distributed state and response mechanisms, not a formal optionality model.

---

# 20. Six-month re-entry test

A future engineer returning to this project should be able to answer:

1. What are the Byzantine civilization-specific resource-cost advantages?
2. Which unit lines receive them?
3. What information advantages are free?
4. What building-survivability advantage exists?
5. What makes the Byzantine mounted roster unusual?
6. What are the main ranged branches?
7. What are the main anti-mounted branches?
8. What siege is available and what is not?
9. What monastery options exist?
10. What is special about Byzantine naval production?
11. What does the Dromon add to the strategic surface?
12. Why does broad technology access increase both flexibility and opportunity cost?
13. Which properties are civilization-specific?
14. Which mechanisms are generic AoE2 mechanisms?
15. Which strategic conclusions are direct facts versus composed or inferred?
16. Why does none of this yet authorize `.per` implementation?

If these questions cannot be answered from this document and its cited source chain, the archaeology is incomplete.

---

# 21. Remaining research gaps

The following remain deliberately unresolved:

### G1 — Exact current Byzantine civilization modifiers

Need direct extraction of all active numeric modifiers from current data rather than relying on historical documentation.

### G2 — Complete unit-line cost matrix

Need current food/wood/gold costs and train times for all strategically relevant Byzantine branches.

### G3 — Counter matrix

Need data-backed matchup relationships, including bonus damage, armor classes, range, speed, and effective production economics.

### G4 — Byzantine production topology

Need exact mapping:

```text
CAPABILITY
→ BUILDING
→ AGE
→ TECHNOLOGY
→ TRAIN TIME
→ RESOURCE COST
→ INFRASTRUCTURE REQUIREMENT
```

### G5 — Byzantine-specific historical AI behavior

Need to isolate which Promisory rules are actually Byzantine-specialized rather than generic rules inherited by every civilization.

### G6 — Replay corroboration

Need multiple replay examples where Byzantine transitions can be correlated with observable enemy composition and subsequent production changes. Causal closure should not be claimed without internal state visibility.

### G7 — Map-conditioned Byzantine strategy

Need separate study of open, closed, hybrid, and water maps.

### G8 — Transition economics

Need to quantify the cost of abandoning one composition for another, including sunk technology and infrastructure costs.

---

# 22. Current strategic profile

The strongest research-level representation is:

```text
                    BYZANTINES
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   DEFENSIVE         COUNTER          OPTION BREADTH
   PERSISTENCE       ECONOMICS             │
        │                │                │
   BUILDINGS       CHEAPER FOOD        LARGE TECH
   + VISION        COUNTERS            / UNIT SURFACE
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                 RESPONSE OPTIONALITY
                         ↓
                TRANSITION CAPACITY
                         ↓
              INFORMATION + TIMING VALUE
                         ↓
                 STRATEGIC FLEXIBILITY
```

This is the central Layer-2 research hypothesis.

It is intentionally more precise than “defensive civ” and more cautious than “jack of all trades.”

---

# 23. Final disposition

**PASS 44 — PASS.**

The Byzantine strategic surface is now sufficiently defined to move from general civilization description into a rigorous **Byzantine capability/counter/transition matrix**.

The next research step should not be `.per` construction.

It should be the empirical/data layer beneath this profile:

```text
BYZANTINE UNIT / TECH DATA
        ↓
COST
        ↓
TRAIN TIME
        ↓
PRODUCTION LOCATION
        ↓
COUNTER RELATIONSHIPS
        ↓
RESOURCE BURDEN
        ↓
TRANSITION COST
        ↓
MAP ROLE
        ↓
STRATEGIC OPTION VALUE
```

Only after that matrix is sufficiently understood should Layer 2 be considered complete enough to hand the findings to Layer 3.

---

# 24. Source record

Primary local/current evidence:

- `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\dat\CivTechTrees\BYZANTINES.json`
- verified historical `AI (HD version).per`
- verified Promisory modules
- Pass 12 Cross-System Control Graph
- Pass 43 Historical Strategic Control-State Atlas

Authoritative external patch evidence used for current-change corroboration:

- Age of Empires II: Definitive Edition Update 169123 (February 17, 2026): Byzantine Fire Ships and Dromons attack 25% faster. citeturn0search2
- Age of Empires II: Definitive Edition Update 83607: Byzantine Dromon introduction and application of the Fire Ship attack-speed bonus to Dromons. citeturn2search13
- Age of Empires II: Definitive Edition Update 51737: Town Patrol free and instantly researched. citeturn2search14
- Age of Empires II: Definitive Edition Update 56005: Byzantine monk team bonus increased to +100% healing speed. citeturn2search12
- Official AoE2 civilization learning material: Byzantines described as having an almost full Technology Tree. citeturn2search3

Community sources are treated only as corroborative/contextual evidence, never as authoritative definitions of current game state.

---

# 25. Provenance rule

Where this document says **current**, it means corroborated against the installed current game-data source and/or a current official patch record.

Where this document says **historical**, it refers to the verified HD/Promisory code archaeology.

Where this document says **strategic consequence**, it is a composed interpretation.

Where this document says **AEGIS-GENERALIZATION**, it is not being attributed to the historical programmer.

No inference in this pass is permitted to silently cross those boundaries.
