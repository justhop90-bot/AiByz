# AiBuilder Goal / Strategic-Number / Timer ABI Matrix

**Repository:** `justhop90-bot/AiByz`  
**Corpus:** current default branch `AiBuilder.per` + `AiBuilder/` load corpus  
**Status:** static-source ABI inventory; runtime semantics are not claimed unless directly established by the corpus.

## 1. Scope and evidence rule

This document inventories the execution ABI exposed by the current AiBuilder corpus. A **Goal** is treated as a named slot only where `AiBuilder.per` explicitly assigns its numeric value. A **Strategic Number (SN)** is treated as a symbolic native engine channel: the current repository uses names such as `sn-food-gatherer-percentage`, but does not assign repository-local numeric SN IDs. A **Timer** is explicitly numbered in `AiBuilder.per`.

**Evidence labels:**
- **DIRECT** — explicit definition or read/write occurrence in the current source corpus.
- **COMPOSED** — relationship assembled from multiple direct source facts.
- **INFERRED** — interpretation needed to describe an operation span or likely ABI behavior; not an engine guarantee.
- **UNKNOWN** — the repository does not establish the requested property.

A negative reader/writer entry means no occurrence was found in the current AiBuilder corpus inspected; it does **not** prove the underlying engine cannot use the symbol elsewhere.

## 2. Load order

| Order | Module | Role | Depends on |
|---:|---|---|---|
| 0 | `AiBuilder.per` | composition root; Goal/timer allocation, initialization, module loading | — |
| 1 | `AiBuilder/constantsUP.per` | engine/fact/object/research/timer/etc. symbolic constants | root load |
| 2 | `AiBuilder/phaseUpdate.per` | phase state transition and policy projection | root Goals + phase constants |
| 3 | `AiBuilder/general.per` | explorer SN projection + search cleanup | root desired-explorer Goals + search-state Goals |
| 4 | `AiBuilder/market.per` | reactive commodity buying/selling | native resource/market facts |
| 5 | `AiBuilder/economy.per` | gatherer SN projection, villager/trade production, cheat loop | root economy Goals/SNs/timer |
| 6 | `AiBuilder/technologies.per` | age advancement, escrow, upgrade research | root age/upgrade Goals |
| 7 | `AiBuilder/construction.per` | building/farm/drop-site execution and search geometry | root building Goals + working Goals + SNs/timers |
| 8 | `AiBuilder/militaryUnits.per` | unit-production execution | root unit Goals |
| 9 | `AiBuilder/militaryBehavior.per` | spread, target-player, land/naval attack behavior | root military Goals + working Goals + timers/SNs |

The root's explicit load sequence is `constantsUP → phaseUpdate → general → market → economy → technologies → construction → militaryUnits → militaryBehavior`.

## 3. Goal ABI — policy/state Goals 1–121

| Slot | Goal | Writer(s) | Reader(s) | Operation width | Evidence |
|---:|---|---|---|---|---|
| 1 | `current-phase` | phaseUpdate | phaseUpdate | 1 | DIRECT |
| 2 | `previous-phase` | — | phaseUpdate | 1 | DIRECT |
| 3 | `desired-military-explorers` | phaseUpdate | general | 1 | DIRECT |
| 4 | `desired-civilian-explorers` | phaseUpdate | general | 1 | DIRECT |
| 5 | `desired-naval-explorers` | phaseUpdate | general | 1 | DIRECT |
| 6 | `desired-food-gatherers` | phaseUpdate | economy | 1 | DIRECT |
| 7 | `desired-wood-gatherers` | phaseUpdate | economy | 1 | DIRECT |
| 8 | `desired-gold-gatherers` | phaseUpdate | economy | 1 | DIRECT |
| 9 | `desired-stone-gatherers` | phaseUpdate | economy | 1 | DIRECT |
| 10 | `desired-number-villagers` | phaseUpdate | economy | 1 | DIRECT |
| 11 | `desired-number-fishing` | phaseUpdate | economy | 1 | DIRECT |
| 12 | `desired-age` | phaseUpdate | technologies | 1 | DIRECT |
| 13 | `desired-ageup-villagers` | phaseUpdate | economy, technologies | 1 | DIRECT |
| 14 | `desired-number-carts` | phaseUpdate | economy | 1 | DIRECT |
| 15 | `desired-number-cogs` | phaseUpdate | economy | 1 | DIRECT |
| 16 | `desired-number-towncenters` | phaseUpdate | construction | 1 | DIRECT |
| 17 | `allow-houses` | phaseUpdate | construction | 1 | DIRECT |
| 18 | `dependent-farms` | phaseUpdate | construction | 1 | DIRECT |
| 19 | `desired-number-farms` | phaseUpdate, construction | construction | 1 | DIRECT |
| 20 | `desired-number-lumbercamps` | phaseUpdate | construction | 1 | DIRECT |
| 21 | `desired-number-mills` | phaseUpdate | construction | 1 | DIRECT |
| 22 | `desired-number-miningcamps` | phaseUpdate | construction | 1 | DIRECT |
| 23 | `desired-number-barracks` | phaseUpdate | construction | 1 | DIRECT |
| 24 | `desired-number-ranges` | phaseUpdate | construction | 1 | DIRECT |
| 25 | `desired-number-stables` | phaseUpdate | construction | 1 | DIRECT |
| 26 | `desired-number-workshops` | phaseUpdate | construction | 1 | DIRECT |
| 27 | `desired-number-blacksmiths` | phaseUpdate | construction | 1 | DIRECT |
| 28 | `desired-number-markets` | phaseUpdate | construction | 1 | DIRECT |
| 29 | `desired-number-docks` | phaseUpdate | construction | 1 | DIRECT |
| 30 | `desired-number-universities` | phaseUpdate | construction | 1 | DIRECT |
| 31 | `desired-number-monasteries` | phaseUpdate | construction | 1 | DIRECT |
| 32 | `desired-number-castles` | phaseUpdate | construction | 1 | DIRECT |
| 33 | `desired-number-outposts` | phaseUpdate | construction | 1 | DIRECT |
| 34 | `desired-number-watchtowers` | phaseUpdate | construction | 1 | DIRECT |
| 35 | `desired-number-bombardtowers` | phaseUpdate | construction | 1 | DIRECT |
| 36 | `upgrade-military-lines` | phaseUpdate | technologies | 1 | DIRECT |
| 37 | `upgrade-military-smith` | phaseUpdate | technologies | 1 | DIRECT |
| 38 | `upgrade-military-generic` | phaseUpdate | technologies | 1 | DIRECT |
| 39 | `upgrade-military-villager-requirement` | phaseUpdate | technologies | 1 | DIRECT |
| 40 | `upgrade-economy` | phaseUpdate | technologies | 1 | DIRECT |
| 41 | `upgrade-economy-villager-requirement` | phaseUpdate | technologies | 1 | DIRECT |
| 42 | `upgrade-fortifications` | phaseUpdate | technologies | 1 | DIRECT |
| 43 | `upgrade-fortifications-villager-requirement` | phaseUpdate | technologies | 1 | DIRECT |
| 44 | `upgrade-navy` | phaseUpdate | technologies | 1 | DIRECT |
| 45 | `upgrade-navy-villager-requirement` | phaseUpdate | technologies | 1 | DIRECT |
| 46 | `upgrade-other` | phaseUpdate | technologies | 1 | DIRECT |
| 47 | `upgrade-other-villager-requirement` | phaseUpdate | technologies | 1 | DIRECT |
| 48 | `desired-number-militias` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 49 | `desired-number-spearmen` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 50 | `desired-number-condottieri` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 51 | `desired-number-scoutcavalry` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 52 | `desired-number-knights` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 53 | `desired-number-battleelephants` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 54 | `desired-number-camelriders` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 55 | `desired-number-steppelancers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 56 | `desired-number-archers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 57 | `desired-number-skirmishers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 58 | `desired-number-cavalryarchers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 59 | `desired-number-handcannoneers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 60 | `desired-number-genitours` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 61 | `desired-number-uniqueunits` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 62 | `desired-number-monks` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 63 | `desired-number-missionaries` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 64 | `desired-number-petards` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 65 | `desired-number-flamingcamels` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 66 | `desired-number-batteringrams` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 67 | `desired-number-scorpions` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 68 | `desired-number-mangonels` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 69 | `desired-number-bombardcannons` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 70 | `desired-number-trebuchets` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 71 | `desired-number-siegetowers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 72 | `desired-number-galleys` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 73 | `desired-number-fireships` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 74 | `desired-number-demoships` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 75 | `desired-number-cannongalleons` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 76 | `desired-number-longboats` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 77 | `desired-number-turtleships` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 78 | `desired-number-caravels` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 79 | `desired-number-transports` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 80 | `desired-number-xolotls` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 81 | `desired-number-eaglescouts` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 82 | `desired-number-mercenarykipchaks` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 83 | `desired-number-slingers` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 84 | `military-spread-time` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 85 | `military-spread-interval` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 86 | `preferred-target-player` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 87 | `allow-wall-targeting` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 88 | `smart-wall-targeting` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 89 | `land-attack-delay` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 90 | `land-attack-interval` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 91 | `land-attack-requirement` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 92 | `land-attack-percentage` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 93 | `transport-destination-x` | phaseUpdate | — | 1 | DIRECT |
| 94 | `transport-destination-y` | phaseUpdate | — | 1 | DIRECT |
| 95 | `naval-attack-delay` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 96 | `naval-attack-interval` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 97 | `naval-attack-requirement` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 98 | `naval-attack-percentage` | phaseUpdate | militaryBehavior | 1 | DIRECT |
| 99 | `allow-cheating` | phaseUpdate | economy | 1 | DIRECT |
| 100 | `cheat-delay` | phaseUpdate | economy | 1 | DIRECT |
| 101 | `cheat-interval` | phaseUpdate | economy | 1 | DIRECT |
| 102 | `cheat-amount-wood` | phaseUpdate | economy | 1 | DIRECT |
| 103 | `cheat-amount-food` | phaseUpdate | economy | 1 | DIRECT |
| 104 | `cheat-amount-gold` | phaseUpdate | economy | 1 | DIRECT |
| 105 | `cheat-amount-stone` | phaseUpdate | economy | 1 | DIRECT |
| 106 | `scale-military-training` | phaseUpdate | — | 1 | DIRECT |
| 107 | `scale-civilian-training` | phaseUpdate | — | 1 | DIRECT |
| 108 | `mill-max-distance` | phaseUpdate | economy | 1 | DIRECT |
| 109 | `lumbercamp-max-distance` | phaseUpdate | economy | 1 | DIRECT |
| 110 | `miningcamp-max-distance` | phaseUpdate | economy | 1 | DIRECT |
| 111 | `max-hunt-distance` | phaseUpdate | — | 1 | DIRECT |
| 112 | `max-wood-distance` | phaseUpdate | — | 1 | DIRECT |
| 113 | `max-food-distance` | phaseUpdate | — | 1 | DIRECT |
| 114 | `max-gold-distance` | phaseUpdate | — | 1 | DIRECT |
| 115 | `max-stone-distance` | phaseUpdate | — | 1 | DIRECT |
| 116 | `disable-difficulty-level-scaling` | phaseUpdate | — | 1 | DIRECT |
| 117 | `cheat-amount-percentage` | phaseUpdate | — | 1 | DIRECT |
| 118 | `scale-attack-timer` | phaseUpdate | — | 1 | DIRECT |
| 119 | `desired-number-armored-elephants` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 120 | `desired-number-shirvamsha-riders` | phaseUpdate | militaryUnits | 1 | DIRECT |
| 121 | `desired-number-elephant-archers` | phaseUpdate | militaryUnits | 1 | DIRECT |

**Slot anomaly:** slots 72–83 are declared in a non-numeric textual order in the root, but the numeric assignments are unique. Slots 122–479 are not allocated by the current root.

## 4. Goal ABI — working/register block 480–510

| Slot | Goal | Writer(s) | Reader(s) | Operation width / span | Evidence |
|---:|---|---|---|---|---|
| 480 | `point-x` | construction | construction | 2-pair member | COMPOSED |
| 481 | `point-y` | construction | construction | 2-pair member | COMPOSED |
| 482 | `point2-x` | construction | construction | 2-pair member | COMPOSED |
| 483 | `point2-y` | construction | construction | 2-pair member | COMPOSED |
| 484 | `point3-x` | construction | construction | 2-pair member | COMPOSED |
| 485 | `point3-y` | construction | construction | 2-pair member | COMPOSED |
| 486 | `point4-x` | — | — | reserved 2-pair member | DIRECT |
| 487 | `point4-y` | — | — | reserved 2-pair member | DIRECT |
| 488 | `point5-x` | — | — | reserved 2-pair member | DIRECT |
| 489 | `point5-y` | — | — | reserved 2-pair member | DIRECT |
| 490 | `position-self-x` | AiBuilder.per | construction | 2-pair member | DIRECT/COMPOSED |
| 491 | `position-self-y` | AiBuilder.per | construction | 2-pair member | DIRECT/COMPOSED |
| 492 | `gl-game-time` | AiBuilder.per | economy, militaryBehavior | 1 | DIRECT |
| 493 | `spread-units` | AiBuilder.per, militaryBehavior | militaryBehavior | 1 | DIRECT |
| 494 | `villager-count` | AiBuilder.per | phaseUpdate, economy, technologies | 1 | DIRECT |
| 495 | `local-total` | general, construction | general, construction | member of 4-goal search-state span | DIRECT/COMPOSED |
| 496 | `local-last` | general, construction | — | member of 4-goal search-state span | DIRECT/COMPOSED |
| 497 | `remote-total` | general, construction | construction | member of 4-goal search-state span | DIRECT/COMPOSED |
| 498 | `remote-last` | general, construction | — | member of 4-goal search-state span | DIRECT/COMPOSED |
| 499 | `map-size` | AiBuilder.per | construction | 1 | DIRECT |
| 500 | *(unnamed)* | — | — | — | DIRECT |
| 501 | `temporary-goal10` | construction | construction | 1 | DIRECT |
| 502 | `temporary-goal9` | construction | construction | 1 | DIRECT |
| 503 | `temporary-goal8` | construction | construction | 1 | DIRECT |
| 504 | `temporary-goal7` | construction | construction | 1 | DIRECT |
| 505 | `temporary-goal6` | construction | construction | 1 | DIRECT |
| 506 | `temporary-goal5` | construction | construction | 1 | DIRECT |
| 507 | `temporary-goal4` | construction | construction | 1 | DIRECT |
| 508 | `temporary-goal3` | construction | construction | 1 | DIRECT |
| 509 | `temporary-goal2` | AiBuilder.per, construction | construction | part of 2-goal point span when used as `up-get-point` destination | COMPOSED |
| 510 | `temporary-goal` | AiBuilder.per, general, construction, militaryBehavior | general, construction, militaryBehavior | part of 2-goal point span when 509 is destination; otherwise scalar | COMPOSED |

## 5. Multi-slot operation ABI

| Operation | Observed destination | Width | Evidence status | Consequence |
|---|---|---:|---|---|
| `set-goal` / `up-modify-goal` / `up-compare-goal` / `goal` | one Goal | 1 | DIRECT | scalar Goal access |
| `up-get-point` | destination Goal pair | 2 | COMPOSED | starting Goal must have a valid adjacent partner |
| `up-copy-point` | destination Goal pair | 2 | COMPOSED | x/y pair must remain contiguous |
| `up-get-search-state` | `local-total` → `local-last` → `remote-total` → `remote-last` | 4 | COMPOSED | starting slot must own a contiguous four-Goal span |
| `up-get-point-distance` | one Goal | 1 | DIRECT | scalar distance result |
| `up-get-fact ... <goal>` | one Goal | 1 | DIRECT | scalar fact result |
| `up-find-player ... <goal>` | one Goal | 1 | DIRECT | scalar player result |
| `up-set-target-point <goal>` | point pair | 2 | COMPOSED | reads x/y pair beginning at supplied Goal |
| SN read/write operations | one SN | 1 | DIRECT | SN is symbolic in this corpus |
| timer operations | one timer | 1 | DIRECT | timer IDs 1–5 are explicit |

The strongest direct ABI example is `up-get-search-state local-total`: the root places `local-total`, `local-last`, `remote-total`, and `remote-last` contiguously at 495–498, and `general.per` consumes that state.

A critical alias is visible in `construction.per`: `up-get-point position-object 509` uses the temporary Goal block beginning at 509, so the adjacent 510 slot participates in the point pair. The same temporary slots are subsequently reused by the construction algorithm. This is a **source-level alias/reuse fact**, not by itself proof of a runtime bug.

## 6. Strategic Number ABI

| SN symbol | Writer(s) | Reader(s) | Width | Numeric slot | Evidence |
|---|---|---|---:|---|---|
| `sn-maximum-food-drop-distance` | AiBuilder.per | economy | 1 | not declared in repository | DIRECT |
| `sn-maximum-wood-drop-distance` | AiBuilder.per | economy | 1 | not declared in repository | DIRECT |
| `sn-maximum-gold-drop-distance` | AiBuilder.per | economy | 1 | not declared in repository | DIRECT |
| `sn-maximum-hunt-drop-distance` | AiBuilder.per | economy | 1 | not declared in repository | DIRECT |
| `sn-maximum-stone-drop-distance` | AiBuilder.per | economy | 1 | not declared in repository | DIRECT |
| `sn-food-gatherer-percentage` | AiBuilder.per, economy | economy | 1 | not declared in repository | DIRECT |
| `sn-wood-gatherer-percentage` | AiBuilder.per, economy | economy, construction | 1 | not declared in repository | DIRECT |
| `sn-gold-gatherer-percentage` | AiBuilder.per, economy | construction | 1 | not declared in repository | DIRECT |
| `sn-stone-gatherer-percentage` | AiBuilder.per, economy | construction | 1 | not declared in repository | DIRECT |
| `sn-cap-civilian-explorers` | AiBuilder.per, general | — | 1 | not declared in repository | DIRECT |
| `sn-percent-civilian-explorers` | AiBuilder.per, general | — | 1 | not declared in repository | DIRECT |
| `sn-defense-distance` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-sentry-distance` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-percent-enemy-sighted-response` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-number-explore-groups` | AiBuilder.per, general | — | 1 | not declared in repository | DIRECT |
| `sn-number-boat-explore-groups` | general | — | 1 | not declared in repository | DIRECT |
| `sn-percent-attack-soldiers` | AiBuilder.per, militaryBehavior | militaryBehavior | 1 | not declared in repository | DIRECT |
| `sn-percent-attack-boats` | militaryBehavior | militaryBehavior | 1 | not declared in repository | DIRECT |
| `sn-task-ungrouped-soldiers` | AiBuilder.per, militaryBehavior | militaryBehavior | 1 | not declared in repository | DIRECT |
| `sn-number-attack-groups` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-enemy-sighted-response-distance` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-total-number-explorers` | AiBuilder.per, general | — | 1 | not declared in repository | DIRECT |
| `sn-minimum-town-size` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-maximum-town-size` | AiBuilder.per, construction | construction | 1 | not declared in repository | DIRECT |
| `sn-mill-max-distance` | AiBuilder.per, economy | — | 1 | not declared in repository | DIRECT |
| `sn-lumber-camp-max-distance` | economy | — | 1 | not declared in repository | DIRECT |
| `sn-mining-camp-max-distance` | economy | — | 1 | not declared in repository | DIRECT |
| `sn-camp-max-distance` | construction | construction | 1 | not declared in repository | DIRECT |
| `sn-allow-adjacent-dropsites` | construction | construction | 1 | not declared in repository | DIRECT |
| `sn-focus-player-number` | construction, militaryBehavior | militaryBehavior | 1 | not declared in repository | DIRECT |
| `sn-target-player-number` | militaryBehavior | militaryBehavior | 1 | not declared in repository | DIRECT |
| `sn-wall-targeting-mode` | AiBuilder.per, militaryBehavior | militaryBehavior | 1 | not declared in repository | DIRECT |
| `sn-easiest-reaction-percentage` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-easier-reaction-percentage` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-enable-boar-hunting` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-enable-new-building-system` | AiBuilder.per | — | 1 | not declared in repository | DIRECT |
| `sn-consecutive-idle-unit-limit` | phaseUpdate | — | 1 | not declared in repository | DIRECT |

**SN ABI conclusion:** the current repository does **not** expose numeric strategic-number slot IDs analogous to Goal slots. `constantsUP.per` assigns numeric IDs to fact/object/etc. constants, but the `sn-*` channels remain symbolic native names. Therefore assigning numeric SN IDs from the Goal table would be an ABI error.

## 7. Timer ABI

| Slot | Timer | Writer(s) | Reader(s) | Operation | Evidence |
|---:|---|---|---|---|---|
| 1 | `town-size-timer` | construction | construction | enable/set + status | DIRECT |
| 2 | `unit-spread-timer` | militaryBehavior | militaryBehavior | set + status/trigger | DIRECT |
| 3 | `cheat-timer` | economy | economy | set + status | DIRECT |
| 4 | `land-attack-timer` | militaryBehavior | militaryBehavior | set + status | DIRECT |
| 5 | `naval-attack-timer` | militaryBehavior | militaryBehavior | set + status | DIRECT |

The timer IDs 1–5 are explicitly allocated by `AiBuilder.per`; `constantsUP.per` defines timer **states** (`timer-disabled=0`, `timer-triggered=1`, `timer-running=2`) separately. These state constants are not timer IDs.

## 8. Dependency matrix

| Module | Reads | Writes | Primary dependency role |
|---|---|---|---|
| `AiBuilder.per` | phase constants; working Goals; native facts/SNs | Goal initialization; working-state values; initial SNs | composition root / ABI owner |
| `constantsUP.per` | — | symbolic engine constants | primitive vocabulary |
| `phaseUpdate.per` | current-phase, previous-phase, phase constants | policy Goals 3–121 and scaling/attack/economy parameters | policy-state producer |
| `general.per` | desired explorer Goals; villager-count; search-state Goals | explorer SNs; search working state; temporary-goal | search/explorer projection |
| `market.per` | native resource/market facts | commodity actions only | reactive exception path |
| `economy.per` | gatherer, villager, fishing, trade, distance, cheat Goals | economy SNs; villager/trade requests; cheat timer | economy execution |
| `technologies.per` | age, age-up, upgrade, villager-count Goals | escrow/research actions | technology/resource authority |
| `construction.per` | building Goals; distance Goals; map-size; working Goals; SNs; timers | building requests; farm geometry; working Goals; construction SNs/timer | construction execution |
| `militaryUnits.per` | unit-count Goals | train requests | military production execution |
| `militaryBehavior.per` | attack/spread/target Goals; gl-game-time; temporary Goal; SNs; timers | spread/target Goals; military SNs; attack requests/timers | military control |

## 9. ABI findings that matter before Byzantine modification

- **Goal slots 1–121 are root-owned policy/state slots.** They should not be renumbered casually; the modules consume the symbolic names defined by the root.
- **Working slots 480–510 are a different class of ABI.** They are scratch/search/register channels, and several are deliberately reused.
- **`local-total` is not undefined in the composed AiBuilder program.** It is Goal 495, followed contiguously by 496–498. The standalone `general.per` file depends on the root composition for those definitions.
- **`temporary-goal2`/`temporary-goal` are an explicit multi-slot alias surface.** `up-get-point ... 509` spans 509–510 while both slots are also used as scratch Goals elsewhere.
- **`previous-phase` has a definition but no writer in the inspected AiBuilder corpus.** That is a real source-level ownership finding. Whether the engine or another included source mutates it is not established here.
- **Several phase policy Goals are written but have no consumer in the loaded modules.** In particular the distance/scaling controls around 111–118 should not be assumed to be functional merely because phaseUpdate assigns them.
- **Strategic-number numeric IDs are not present in this corpus.** Do not manufacture an SN numeric ABI from the Goal numbering.
- **Timer IDs 1–5 are explicit.** A new timer ID must not be invented merely because 6 appears unused; the safe allocation policy is still an engineering decision requiring broader collision analysis.

## 10. Evidence boundary

This is a **source ABI inventory**, not a runtime certification. It establishes what the current repository declares and references. It does not prove that every primitive is accepted by the target AoE2DE build, that every request completes, or that a Goal/SN transition has the intended strategic effect. Those require separate engine-semantic or runtime evidence.

### Source references

- `AiBuilder.per` — Goal/timer allocation and load order.
- `AiBuilder/general.per` — explorer/search working-state use.
- `AiBuilder/economy.per` — economy Goal/SN/timer use.
- `AiBuilder/construction.per` — construction Goal/SN/working-state use.
- `AiBuilder/militaryUnits.per` — production Goal reads.
- `AiBuilder/militaryBehavior.per` — military Goal/SN/timer use.
- `AiBuilder/constantsUP.per` — fact/object/research/timer-state constants.
