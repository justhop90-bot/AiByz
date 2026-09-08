# P0 Total Substrate Deconstruction Pass — 2026-09-08

## Purpose
This pass resumes the total-system rework. It does **not** implement or runtime-probe a subsystem. It establishes how the stock AI(HD) and original Promisory substrate actually fit together so the final AEGIS implementation can reproduce the complete behavior under AEGIS ownership.

## Evidence inspected on target machine
Authoritative stock directory:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

Inspected directly:
- `AI (HD version).per`
- `Promisory\const.per`
- `Promisory\customConstants.per`
- `Promisory\defaultConstants.per`
- `Promisory\finaling.per`
- `Promisory\gatherers.per`
- `Promisory\buildings.per`
- `Promisory\researches.per`
- `Promisory\units.per`
- `Promisory\tsa.per`
- `Promisory\scoutcontrol.per`
- `Promisory\threats.per`
- `Promisory\interaction.per`
- `AegisProm\AEGIS-foundation.per`

## Finding 1 — The substrate is a shared symbol/state ABI
The Promisory modules are not independent behavior files. They share a large namespace of:
- FactIds
- ObjectIds/classes
- foundation IDs
- research/timer/group/action/order constants
- ObjectData fields
- terrain/search/placement constants
- strategic numbers
- persistent goals
- temporary scratch goals
- cross-module state flags

Therefore the final reconstruction cannot simply copy each `.per` file into AegisProm and expect equivalent behavior. The shared ABI and state topology must be reconstructed first.

## Finding 2 — `const.per` and `defaultConstants.per` establish a substantial common ABI
Both files define the same foundational domains, including FactIds 0–49, ObjectData fields, placement/search/action/order constants, terrain constants, and extended AI concepts. `const.per` additionally carries later/development constants and version-dependent definitions.

This means the constants layer is itself part of the operating-system substrate. It is not mere cosmetic configuration.

## Finding 3 — `customConstants.per` is a second major semantic layer
`customConstants.per` adds and overrides a very large set of civilization/unit/research/line identifiers, strategy values, placement constants, Paphos/development definitions, and other runtime symbols. It also contains explicit comments distinguishing retail-safe definitions from development-only material.

A final AEGIS symbol layer therefore needs provenance for every imported identifier rather than a blind copy. In particular, development-only or conditional symbols must not silently become universal AEGIS ABI.

## Finding 4 — `finaling.per` is an active runtime service, not a terminal include
The inspected beginning of `finaling.per` immediately mutates strategic numbers, escrow percentages, facts, and AI state. It then contains persistent production, attack, capture, movement, scouting, siege, naval, and late-game rules.

The file therefore functions as an active policy/execution layer. The name `finaling` does not imply a simple finalization step.

## Finding 5 — Economic control is distributed and strategy-dependent
`gatherers.per` demonstrates that worker allocation is repeatedly rewritten according to:
- current age
- strategy
- villager population
- food thresholds
- building availability/counts
- research state
- escrow state
- excess resources
- town-center count
- civilization-specific conditions
- map/resource serviceability

Examples include many different food/wood/gold percentage vectors for feudal, castle, imperial, rush, fast-imp, boom, stonewall, sling, cavalry, archer, and other strategies.

Conclusion: a final AEGIS economy cannot be reduced to a single demand formula or static worker percentages. Those earlier V0 modules remain source material only.

## Finding 6 — Civilian production is a policy network
`units.per` contains numerous independent `trainvillager` rules. They combine:
- population/civilian limits
- food reserves
- age transition state
- strategy
- military policy
- research readiness
- pending villager objects
- escrow/research interactions
- dropsite serviceability
- town-center count
- special-map modes
- late-game reserve thresholds

Thus villager production is one node in a distributed economic scheduler, not an isolated producer.

## Finding 7 — Construction, economy, research, and military form closed control loops
The inspected modules show explicit cross-domain feedback:

`buildings.per` → construction state → town-size/placement/strategic state → economy

`researches.per` → age/technology state → gatherer vectors → production/construction

`tsa.per` → military posture/retreat/attack state → economy and production

`threats.per` → target/focus/threat state → military and defensive behavior

`scoutcontrol.per` → information/micro state → target selection and military action

`units.per` → production goals → military/civilian population → strategy/economy

The final architecture must preserve these feedback paths even if the implementation is reorganized behind AEGIS interfaces.

## Finding 8 — Scouting is an information-processing subsystem
`scoutcontrol.per` contains persistent state for waypoint generation, group formation, threat/path analysis, enemy-strength estimation, retreat logic, and specialized scout micro. It uses geometry operations, object searches, timers, groups, and enemy composition scoring.

This establishes that scouting is not merely movement. It is part of the stock information and threat-processing OS.

## Finding 9 — Threat processing is distributed
`threats.per` maintains focus-player, target-player, attacking-enemy, enemy-pocket, military-superiority, and composition estimates. It repeatedly scans players and modifies shared strategic state.

Threat handling is therefore not one centralized emergency rule. It is a distributed state machine coupled to targeting and military policy.

## Finding 10 — Military strength is an interpreted model
`threats.per` builds weighted estimates for cavalry, archers, skirmishers, cavalry archers, gunpowder, infantry, monks, and siege from multiple unit lines/types. Some units are explicitly weighted or divided/multiplied before aggregation.

Therefore AEGIS Military OS must eventually model **interpreted threat/strength**, not merely raw unit counts.

## Finding 11 — Interaction is part of the operating system
`interaction.per` handles taunts, strategy disclosure, ally coordination, resource requests, scouting communication, market requests, wonder coordination, and other control signals.

These are not just UI/chat features. Several interaction rules alter persistent goals and strategic behavior. AEGIS must account for them as external-control/input channels.

## Reconstruction consequence
The complete stock system should be reconstructed as a dependency graph with four distinct categories:

1. **Static ABI** — identifiers, constants, field meanings, domains.
2. **Persistent state** — goals, strategic numbers, timers, flags, groups, escrow state.
3. **Operating services** — economy, workers, construction, research, production, scouting, military, threat, trade, water, boar, interaction.
4. **Control topology** — rule ordering, jump topology, conditional compilation, state mutation, and cross-service feedback.

Only after those are mapped should AEGIS implementation proceed.

## Current status
This pass is **STATIC DECONSTRUCTION / ARCHITECTURAL EVIDENCE**, not runtime qualification and not final implementation.

No construction probe or worker-loop probe is introduced by this pass.

## Next reconstruction target
Continue downward through the stock subsystem graph, resolving the **load/conditional-compilation topology and shared-state ownership** across the remaining Promisory modules, then produce the complete AEGIS service/state reconstruction matrix.
