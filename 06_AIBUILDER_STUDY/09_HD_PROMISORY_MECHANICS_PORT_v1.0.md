# HD / Promisory Mechanics Port v1.0 — 2026-09-12

## Purpose

This document records the first deliberate transfer of functional mechanics from the historical HD/Promisory AI into the working AIByzBuild runtime.

The objective is not to copy the historical architecture. It is to recover mechanics that the reference bot uses, verify that the AoE2 scripting engine exposes the required facts/commands, and implement them through existing AiBuilder execution channels.

## Source basis

The historical source identifies dedicated state for enemy military level, infantry/archer/cavalry threats, under-attack status, escrow purpose, military spreading, retreat/attack status, forward threats, enemy fortifications, target selection, and victory/threat telemetry. It also uses threat-data and victory-data retrieval, closest-enemy selection, resource-control state, attack timing, military spreading, escrow control, and enemy composition observations. These patterns are visible in the public HD/Promisory source mirror. 

The AoE2 AI Scripting Encyclopedia is the engine-reference authority used to distinguish supported scripting primitives from source vocabulary. It documents the DE/HD/UserPatch shared AI engine and provides the command/fact/strategic-number reference. 

## Twenty mechanics ported

| # | Historical mechanic | AiByzBuild implementation |
|---|---|---|
| 01 | Enemy military-level comparison | `sn-military-level` plus `byz-enemy-military-state` |
| 02 | Enemy age awareness | `byz-enemy-age-state` from `players-current-age` |
| 03 | Nearest-enemy focus | `up-find-player` → `byz-focus-player-state` → focus/target SNs |
| 04 | Last-threat memory | `up-get-threat-data` → four dedicated policy goals |
| 05 | Under-attack state | `town-under-attack` → `byz-under-attack-state` |
| 06 | Cavalry-threat classification | `sn-cavalry-threat` plus Byzantine spear/camel demand |
| 07 | Archer-threat classification | `sn-archer-threat` plus skirmisher demand |
| 08 | Infantry-threat classification | infantry-line observations plus archer demand |
| 09 | Forward-tower threat | observed enemy watchtower count → `byz-forward-threat-state` |
| 10 | Enemy-fortification awareness | enemy castles/walls → `byz-fortification-state` |
| 11 | Siege resource reservation | fortification/forward pressure → `sn-resource-control=battering-ram` |
| 12 | Persistent attack target | focus player → `sn-target-player-number` / `sn-focus-player-number` |
| 13 | Attack cadence/minimum force | existing `militaryBehavior.per` attack channel receives delay, interval, requirement, percentage |
| 14 | Attack scaling against fortifications | lower attack percentage and raise minimum force when fortified |
| 15 | Periodic military spreading | existing `spread-units` / military spread timer channel |
| 16 | Escrow-purpose tracking | food/gold escrow is marked for Byzantine UU upgrade intent |
| 17 | Urgent escrow release | existing `can-research-with-escrow` path releases food/gold for UU upgrade |
| 18 | Dynamic farm/hunting response | low food increases farm requirement; nearby boar enables Builder hunting parameters |
| 19 | Emergency housing | population cap condition reasserts `allow-houses` |
| 20 | Naval-enemy awareness | enemy warboat observation increases naval exploration demand |

## Ownership

`byzPolicy.per` owns interpretation and policy state. `militaryUnits.per`, `construction.per`, `economy.per`, `technologies.per`, and `militaryBehavior.per` remain execution owners.

No XS was introduced. The new policy state uses strategic-number goals 121–143. Builder scratch goals 501–510 remain untouched.

## Important qualification boundary

Static syntax validation is not runtime proof. The installed files were checked for balanced parentheses and rule/action balance. Runtime gameplay qualification remains a separate gate.

Several mechanics are intentionally telemetry/state mechanisms rather than direct action. This preserves the historical pattern of separating observation, policy state, and physical execution.

## Result

AIByzBuild now contains a materially broader set of HD/Promisory control mechanics: opponent state, threat classification, threat memory, target selection, attack timing, fortification-aware attack pressure, siege resource reservation, military spreading, escrow intent, hunting/farming response, housing protection, and naval awareness.

The next architectural step is not another pile of independent rules. These mechanics now provide the observation and state substrate required for a closed-loop requirement/deficit controller.
