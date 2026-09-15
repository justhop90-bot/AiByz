# Stock Symbol Ownership Candidate Matrix — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Purpose:** first symbol-level ownership join after module coupling reconstruction.

This document is deliberately a **candidate** registry. It does not authorize reuse of any stock numeric channel. The machine census remains authoritative for numeric occupancy.

## High-value shared goals

| Symbol | Numeric declaration | Dominant writers | Dominant readers | Candidate historical responsibility | AEGIS owner candidate | Status |
|---|---:|---|---|---|---|---|
| `strategy-goal` | 3 | strategy/civ-policy | strategy, production/military consumers | strategic policy selector | Cognition / Strategy Service | STATIC-QUALIFIED candidate |
| `unit-goal` | 4 | units/strategy-related rules | production/military | unit composition/production demand | Production Service | STATIC-QUALIFIED candidate |
| `control-goal` | 6 | distributed control rules | distributed control rules | broad operating arbitration | Demand Arbitration | UNRESOLVED shared-state candidate |
| `attack-goal` | 2 | military/strategy | military/attack | attack intent/state | Military Cognition | STATIC-QUALIFIED candidate |
| `ranged-unit-type-goal` | 19 | production/civ policy | production/military | ranged composition selector | Military Production | STATIC-QUALIFIED candidate |
| `increase-town-size-goal` | 1 | town-size/building logic | town-size/building consumers | infrastructure growth demand | Infrastructure Planning | STATIC-QUALIFIED candidate |
| `uu-up-goal` | 17 | civ/unit policy | production | unique-unit capability policy | Civilization Policy / Production | STATIC-QUALIFIED candidate |
| `train-civ-goal` | 5 | civ policy | production | civilization-specific production policy | Civilization Policy | STATIC-QUALIFIED candidate |
| `farm-goal` | 10 | economy/farm logic | economy/building | farm/food-infrastructure demand | Economy / Construction | STATIC-QUALIFIED candidate |
| `under-attack-goal` | 11 | threat/military | threat/military/economy | active defensive pressure | Situation / Threat Service | STATIC-QUALIFIED candidate |
| `enemy-goal` | 9 | scouting/military | military/strategy | enemy identity/selection | World Model / Information | STATIC-QUALIFIED candidate |
| `position-goal` | 46 | spatial/scouting/military | strategy/military/construction | strategic spatial target | World Model / Planning | UNRESOLVED shared-state candidate |
| `housing-goal` | 21 | economy/construction | economy/building | housing pressure | Economy / Construction | STATIC-QUALIFIED candidate |
| `escrow-purpose-goal` | 15 | escrow/production/research | escrow consumers | purpose of protected reservation | Reservation Service | STATIC-QUALIFIED candidate |

## High-value strategic numbers

| Symbol | Numeric declaration | Dominant function | Candidate owner | Status |
|---|---:|---|---|---|
| `sn-wood-gatherer-percentage` | target census | worker allocation | Economy / Worker Service | STATIC-QUALIFIED candidate |
| `sn-food-gatherer-percentage` | target census | worker allocation | Economy / Worker Service | STATIC-QUALIFIED candidate |
| `sn-gold-gatherer-percentage` | target census | worker allocation | Economy / Worker Service | STATIC-QUALIFIED candidate |
| `sn-stone-gatherer-percentage` | target census | worker allocation | Economy / Worker Service | STATIC-QUALIFIED candidate |
| `sn-resource-control` | 191 | resource arbitration | Economy / Demand Arbitration | STATIC-QUALIFIED candidate |
| `sn-maximum-town-size` | target census | infrastructure capacity | Infrastructure Service | STATIC-QUALIFIED candidate |
| `sn-focus-player-number` | target census | information focus identity | World Model / Information | STATIC-QUALIFIED candidate |
| `sn-target-player-number` | target census | target identity | Military / Information | STATIC-QUALIFIED candidate |
| `sn-current-age` | 205 | age/progression state | Civilization State | STATIC-QUALIFIED candidate |
| `sn-military-level` | 190 | military posture | Military Cognition | STATIC-QUALIFIED candidate |
| `sn-maximum-wood-drop-distance` | target census | service-distance constraint | Economy / Logistics | STATIC-QUALIFIED candidate |
| `sn-maximum-food-drop-distance` | target census | service-distance constraint | Economy / Logistics | STATIC-QUALIFIED candidate |
| `sn-maximum-gold-drop-distance` | target census | service-distance constraint | Economy / Logistics | STATIC-QUALIFIED candidate |
| `sn-camp-max-distance` | target census | infrastructure service constraint | Economy / Construction | STATIC-QUALIFIED candidate |
| `sn-number-explore-groups` | target census | exploration allocation | Information / Scouting | STATIC-QUALIFIED candidate |

## Timers as control-state channels

Timers require special treatment. A timer identifier is not equivalent to a timestamp variable: it participates in the engine's timer substrate and must be modeled as a control-state primitive.

| Stock timer | Historical use | Candidate AEGIS abstraction | Status |
|---|---|---|---|
| `increase-town-size-timer` | town-size growth cadence | infrastructure evaluation cadence | STATIC candidate |
| `reset-town-size-timer` | town-size reset/recovery | infrastructure state reset | STATIC candidate |
| `scouting-timer` | scouting cadence | information refresh cadence | STATIC candidate |
| `attack-timer` | attack cadence | military evaluation cadence | STATIC candidate |
| `under-attack-timer` | defensive response cadence | situation/threat refresh | STATIC candidate |
| `one-minute-timer` | coarse periodic maintenance | periodic service tick | STATIC candidate |
| `micro-timer` | tactical micro cadence | tactical service cadence | STATIC candidate |
| `retreat-timer` | retreat/recovery cadence | military recovery cadence | STATIC candidate |
| `hunting-timer` | hunting cadence | food acquisition cadence | STATIC candidate |

Exact timing guarantees remain target-build runtime questions.

## Symbol ownership rules

A stock symbol can only be promoted into an AEGIS implementation after all of the following are known:

1. channel type;
2. numeric identity, if applicable;
3. declaration source;
4. all known writers;
5. all known readers;
6. reset/clear behavior;
7. activation predicates;
8. lifecycle;
9. collision set;
10. AEGIS owner;
11. evidence status;
12. whether the historical semantics can be safely abstracted.

## Important discovery

The most dangerous stock channels are not necessarily the highest-frequency channels. `control-goal`, `position-goal`, and similar shared channels have **distributed writers and readers**, making them substantially more important from an ownership and race-analysis perspective than their raw frequency alone suggests.

Therefore AEGIS ABI design must optimize for **semantic isolation and lifecycle clarity**, not merely for avoiding duplicate numbers.

## Next static extraction

The next artifact should enumerate the actual writer and reader rule sites for the high-value shared channels, with source line ranges and activation predicates. That will expose where the stock controller relies on distributed mutation, jump topology, and implicit state coupling.

No runtime qualification is required for this extraction.
