# AEGIS / AiBuilder Native Identifier Matrix v0.1

**Status:** source-qualified baseline; runtime qualification tracked separately
**Scope:** identifiers and selector forms directly relevant to AiBuilder and the first AEGIS vertical slices.

## Evidence legend

- **SOURCE-CONFIRMED** — directly present in Encyclopedia/AiBuilder source.
- **ENGINE-DOCUMENTED** — documented by the AI scripting reference but not necessarily emitted by the Builder GUI.
- **BUILDER-GENERATED** — emitted by the original AiBuilder generator.
- **LIBRARY-USED** — used by an AiBuilder bundled library.
- **RUNTIME-QUALIFY** — syntax/object is source-grounded, but current AoE2DE behavior still requires runtime qualification.
- **DO-NOT-INFER** — do not infer semantics from a name alone.

---

# 1. Player selector matrix

| Selector | Category | Source status | Primary use | AEGIS rule |
|---|---|---|---|---|
| numeric player (`1`, `2`, etc.) | literal PlayerId | ENGINE-DOCUMENTED | explicit player query | Never assume this means enemy |
| `my-player-number` | self PlayerId | ENGINE-DOCUMENTED | own-player facts | Preferred for explicit self queries when required |
| `target-player` | dynamic PlayerId | ENGINE-DOCUMENTED | selected target | Requires established target semantics |
| `focus-player` | dynamic PlayerId | ENGINE-DOCUMENTED | current focus | Requires established focus semantics |
| `any-enemy` | wildcard PlayerId | ENGINE-DOCUMENTED; LIBRARY-USED | generic enemy observation | Preferred generic enemy selector |
| `any-ally` | wildcard PlayerId | ENGINE-DOCUMENTED | generic ally observation | Use only with commands supporting wildcard aggregation |
| `any-neutral` | wildcard PlayerId | ENGINE-DOCUMENTED | generic neutral observation | Use only with supported commands |
| `every-enemy` | wildcard family | ENGINE-DOCUMENTED | aggregate/all-enemy contexts | Command-specific semantics must be established |
| `every-ally` | wildcard family | ENGINE-DOCUMENTED | aggregate/all-ally contexts | Command-specific semantics must be established |
| `every-neutral` | wildcard family | ENGINE-DOCUMENTED | aggregate/all-neutral contexts | Command-specific semantics must be established |

### Player-selector qualification principle

`2` is not equivalent to `any-enemy`.

A successful rule using:

```lisp
(players-unit-type-count 2 villager >= 0)
```

establishes only that player 2 can be supplied to the command. It does not establish that player 2 is an opponent.

---

# 2. Unit object matrix

| Strategic label | Concrete object identifier | Unit-line identifier | Builder GUI mapping | Source status | AEGIS observation preference |
|---|---|---|---|---|---|
| Villager | `villager` | — | economy/civilian | ENGINE-DOCUMENTED | `villager` for direct count |
| Militia/Swordsmen | `militiaman` | `militiaman-line` | Swordsmen | BUILDER-GENERATED | line for capability tracking |
| Spearman/Pikeman/Halberdier | `spearman` | `spearman-line` | Spearmen | BUILDER-GENERATED | line preferred |
| Scout Cavalry | `scout-cavalry` | `scout-cavalry-line` | Scout Cavalry | BUILDER-GENERATED | line preferred |
| Knight/Cavalier/Paladin | `knight` | `knight-line` | Knights | BUILDER-GENERATED | line preferred |
| Camel Rider | `camel` | `camel-line` | Camels | BUILDER-GENERATED | line preferred |
| Archer/Crossbow/Arbalest | `archer` | `archer-line` | Archers | ENGINE-DOCUMENTED + BUILDER-GENERATED | line preferred for ranged capability |
| Skirmisher | `skirmisher` | `skirmisher-line` | Skirmishers | BUILDER-GENERATED | line preferred |
| Cavalry Archer | `cavalry-archer` | `cavalry-archer-line` | Cavalry Archers | BUILDER-GENERATED | line preferred |
| Hand Cannoneer | `hand-cannoneer` | — | Hand Cannoneers | BUILDER-GENERATED | concrete object |
| Civilization unique unit | civ-specific object | `my-unique-unit-line` in Builder | Unique Units | BUILDER-GENERATED | civ-specific qualification required |
| Monk | `monk` | — | Monks | ENGINE-DOCUMENTED + LIBRARY-USED | concrete object |
| Mangonel/Onager/Siege Onager | `mangonel` | `mangonel-line` | Onagers | BUILDER-GENERATED | line preferred |
| Battering Ram/Capped/Armored | `battering-ram` | `battering-ram-line` | Rams | BUILDER-GENERATED | line where supported |
| Scorpion/Heavy Scorpion | `scorpion` | `scorpion-line` | Scorpions | BUILDER-GENERATED | line where supported |
| Trebuchet | `trebuchet` | — | Trebuchet | BUILDER-GENERATED | concrete object |
| Bombard Cannon | `bombard-cannon` | — | Cannons | BUILDER-GENERATED | concrete object |
| Galley/War Galley/Galleon | `galley` | `galley-line` | Galleys | BUILDER-GENERATED | line preferred |
| Fire Ship/Fast Fire Ship | `fire-ship` | `fire-ship-line` | Fire Ships | BUILDER-GENERATED | line preferred |
| Cannon Galleon | `cannon-galleon` | `cannon-galleon-line` | Cannon Galleons | BUILDER-GENERATED | line preferred |
| Demolition Ship | `demolition-ship` | `demolition-ship-line` | Demolition Ships | BUILDER-GENERATED | line preferred |
| Transport Ship | `transport-ship` | — | Transport Ships | BUILDER-GENERATED | concrete object |

### Unit identifier rule

Do not substitute an object identifier for a unit-line identifier merely because the names appear related. The distinction matters for upgrade chains and for sighted enemy information.

Historical AI documentation records bugs in sighted-unit conversion and explicitly recommends line counting in affected cases. Therefore:

```lisp
(players-unit-type-count any-enemy archer-line > 0)
```

answers a different strategic question from:

```lisp
(players-unit-type-count any-enemy archer > 0)
```

The first is capability-family oriented; the second is concrete-object oriented.

---

# 3. Building object matrix

| Strategic category | Identifier | Builder GUI | Source status | AEGIS relevance |
|---|---|---|---|---|
| Town Center | `town-center` | Town Centers | BUILDER-GENERATED | economy / base / production authority |
| Farm | `farm` | Farms | BUILDER-GENERATED | economy |
| Lumber Camp | `lumber-camp` | Lumber Camps | BUILDER-GENERATED | economy |
| Mill | `mill` | Mills | BUILDER-GENERATED | economy |
| Mining Camp | `mining-camp` | Gold/Stone mining camps | BUILDER-GENERATED | economy |
| Barracks | `barracks` | Barracks | BUILDER-GENERATED | infantry capability |
| Archery Range | `archery-range` | Archery Ranges | BUILDER-GENERATED | **ranged-production capability** |
| Stable | `stable` | Stables | BUILDER-GENERATED | cavalry capability |
| Siege Workshop | `siege-workshop` | Siege Workshops | BUILDER-GENERATED | siege capability |
| Blacksmith | `blacksmith` | Blacksmiths | BUILDER-GENERATED | technology capability |
| Market | `market` | Markets | BUILDER-GENERATED | resource conversion |
| University | `university` | Universities | BUILDER-GENERATED | technology capability |
| Monastery | `monastery` | Monasteries | BUILDER-GENERATED | monk/relic/tech capability |
| Dock | `dock` | Docks | BUILDER-GENERATED | naval capability |
| Castle | `castle` | Castles | BUILDER-GENERATED | unique-unit/siege/fortification capability |
| Tower | tower identifier | Towers | BUILDER GUI category; exact object spelling requires source/runtime qualification | defensive capability |
| Bombard Tower | `bombard-tower` | Bombard Towers | BUILDER GUI category; exact current-DE object spelling requires qualification | defensive ranged capability |

**Important:** `archery-range` is directly present in the original Builder generator source. It should not be treated as an invented AEGIS identifier.

---

# 4. Counting-command matrix

| Command | Player selector | Object parameter | Typical use | Status |
|---|---|---|---|---|
| `players-unit-type-count` | PlayerId | unit object / unit line | sighted player unit composition | ENGINE-DOCUMENTED; RUNTIME-QUALIFY |
| `players-building-type-count` | PlayerId | building object | sighted player production/infrastructure capability | ENGINE-DOCUMENTED; RUNTIME-QUALIFY |
| `players-building-count` | PlayerId | none | player building aggregate | ENGINE-DOCUMENTED; RUNTIME-QUALIFY |
| `players-unit-count` | PlayerId | none | player unit aggregate | ENGINE-DOCUMENTED; RUNTIME-QUALIFY |
| `unit-type-count-total` | self/current player context | unit object / line | own existing + pending object totals | BUILDER/LIBRARY-USED |
| `building-type-count-total` | self/current player context | building object | own existing + pending building totals | BUILDER-GENERATED |
| `unit-type-count` | self/current player context | unit object / line | own current object count | ENGINE-DOCUMENTED |
| `building-type-count` | self/current player context | building object | own current building count | ENGINE-DOCUMENTED |

Do not equate `players-*` commands with the self-state `*-type-count-total` commands. They answer different questions and use different player/object semantics.

---

# 5. Class identifiers relevant to strategic classification

| Class | Identifier | Strategic use | Status |
|---|---|---|---|
| Infantry | `infantry-class` | infantry capability aggregation | ENGINE-DOCUMENTED |
| Archery | `archery-class` | ranged capability aggregation | ENGINE-DOCUMENTED |
| Cavalry | `cavalry-class` | cavalry capability aggregation | ENGINE-DOCUMENTED |
| Cavalry Archer | `cavalry-archer-class` | mounted ranged capability | ENGINE-DOCUMENTED |
| Archery Cannon | `archery-cannon-class` | gunpowder/ranged grouping | ENGINE-DOCUMENTED |
| Cavalry Cannon | `cavalry-cannon-class` | mounted gunpowder grouping | ENGINE-DOCUMENTED |
| Monastery | `monastery-class` | monastery/monk grouping | ENGINE-DOCUMENTED |
| Siege Weapon | `siege-weapon-class` | siege capability | ENGINE-DOCUMENTED |
| Scorpion | `scorpion-class` | scorpion-specific classification | ENGINE-DOCUMENTED |
| Packed Trebuchet | `packed-trebuchet-class` | trebuchet state | ENGINE-DOCUMENTED |
| Unpacked Trebuchet | `unpacked-trebuchet-class` | trebuchet state | ENGINE-DOCUMENTED |
| Petard | `petard-class` | demolition capability | ENGINE-DOCUMENTED |
| Warship | `warship-class` | naval combat capability | ENGINE-DOCUMENTED |
| All units | `all-units-class` | broad aggregation | ENGINE-DOCUMENTED |

Classes are not unit identifiers. Do not substitute a class for an object or line unless the command explicitly accepts a class parameter.

---

# 6. Canonical AEGIS observation forms

## Enemy ranged-unit observation

```lisp
(players-unit-type-count any-enemy archer > 0)
```

**Question:** Has the AI's sighted enemy-player information recorded one or more concrete archers?

## Enemy ranged-capability observation

```lisp
(players-unit-type-count any-enemy archer-line > 0)
```

**Question:** Has the AI's sighted enemy-player information recorded one or more members of the archer upgrade line?

## Enemy ranged-production capability

```lisp
(players-building-type-count any-enemy archery-range > 0)
```

**Question:** Has the AI's sighted enemy-player information recorded one or more Archery Ranges?

## Enemy cavalry-production capability

```lisp
(players-building-type-count any-enemy stable > 0)
```

## Enemy infantry-production capability

```lisp
(players-building-type-count any-enemy barracks > 0)
```

These are **observation predicates**, not strategic conclusions. AEGIS must classify the observation before committing to a response.

---

# 7. Source-vs-runtime boundary

### Source-confirmed

- `any-enemy` is a valid engine PlayerId wildcard.
- `players-unit-type-count` exists and accepts a PlayerId plus unit object/line.
- `players-building-type-count` exists and accepts a PlayerId plus building object.
- `archer`, `archer-line`, and the other Builder military identifiers are established engine vocabulary.
- `archery-range` is emitted by the original AiBuilder.
- Builder libraries use advanced enemy observation, including `any-enemy`.

### Runtime qualification still required

- Current AoE2DE timing of sighted-player updates.
- Exact current-DE behavior of each wildcard/object combination.
- Whether a particular enemy object has entered the AI's sighted cache.
- End-to-end observation → AEGIS goal → AiBuilder production behavior.

### Forbidden inference

Do not infer any of the following merely from source syntax:

- that an enemy object exists on the map;
- that an unseen object is counted;
- that `any-enemy` identifies a particular player for a later action;
- that an Archery Range proves an enemy has produced archers;
- that an observed archer proves continued production;
- that a successful rule parse proves the strategic response succeeded.

---

# 8. First AEGIS qualification target

The first canonical vertical slice should use the smallest native capability chain:

```text
Enemy Archery Range observed
        ↓
Ranged-production capability = PRESENT
        ↓
Byzantine response requirement = ranged counter capability
        ↓
Skirmisher target goal
        ↓
Existing AiBuilder military production
        ↓
Actual Skirmisher training
        ↓
Runtime evidence
        ↓
Reassessment
```

The observation predicate is source-grounded as:

```lisp
(players-building-type-count any-enemy archery-range > 0)
```

The production side remains delegated to the existing AiBuilder machinery.

## Qualification rule

Do not modify the immutable `AiBuilder` control. All AEGIS experiments belong in `AIByzBuild` until the vertical slice has passed source, syntax, runtime, causal, and regression gates.

---

# 9. Primary references

- AoE2 AI Scripting Encyclopedia: https://airef.github.io/
- UserPatch AI scripting reference / historical engine notes: https://airef.github.io/tables/up-patch-notes.html
- Original/community AoE2DE AIBuilder: https://github.com/JackkelDragon/AoE2DE_AIBuilder
- AEGIS/AiByz: https://github.com/justhop90-bot/AiByz
