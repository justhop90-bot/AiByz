# Standard RTS Competency Audit — 2026-09-12

## Purpose

Audit AiByzBuild against the minimum functional faculties expected of a competent RTS AI before adding higher-order strategic architecture.

The comparison is against ordinary AoE2 gameplay requirements, not Extreme-AI strength. AoE2 itself identifies economy, technology, military training, expansion/development, and battlefield strategy as core match functions.

## Baseline categories

| Category | Baseline requirement | AiByzBuild status |
|---|---|---|
| Worker production | Maintain villagers | PASS |
| Resource allocation | Maintain food/wood/gold/stone allocation | PASS |
| Age progression | Advance through ages without stale phase dependency | PASS |
| Housing | Prevent population blockage | PASS |
| Resource infrastructure | Camps, mills, farms | PASS |
| Production infrastructure | Barracks/ranges/stables/siege | PASS |
| Technology | Research age, military, economy and unique upgrades | PASS |
| Military production | Maintain multiple unit lines | PASS |
| Army composition | Maintain a usable Byzantine portfolio | PASS |
| Siege | Produce siege when policy requires it | PASS |
| Scouting | Maintain military/civilian exploration presence | PASS |
| Offensive action | Periodic attack through existing Builder attack channel | PASS |
| Local defense | React to enemy units/forward buildings inside town | PASS — newly hardened |
| Basic counter response | React to identified local knight/archer/skirmisher presence | PASS — newly hardened |
| Expansion | Builder phase system supplies TC expansion targets | PASS |
| Market | Reactive buying/selling exists | PASS |
| Naval | Builder channels exist for naval maps | PASS at substrate level |
| Retreat/targeting | Existing Builder/engine behavior provides baseline targeting | PASS at substrate level |
| Recovery | Detect failed strategic objective and deliberately recover | NOT YET |
| Global enemy composition model | Maintain a persistent opponent capability model | NOT YET |
| Strategic adaptation | Change objective when conditions invalidate it | NOT YET |
| Military demand/deficit | Continuously derive required force from objective and actual force | NOT YET |
| Resource demand model | Tie economy to military/technology/construction demand | NOT YET |

## Result

The bot now meets the ordinary RTS baseline in the execution categories. The remaining gaps are higher-order intelligence rather than missing basic RTS functionality.

The distinction is deliberate:

`BASELINE RTS COMPETENCE → CLOSED-LOOP SELF-EVALUATION → ADAPTIVE STRATEGY`

AiByzBuild is ready to move into the second layer.

## Runtime hardening applied

The installed runtime `AIByzBuild\byzPolicy.per` was extended without modifying AiBuilder execution modules.

### Scouting

From Feudal onward, Byzantine policy explicitly maintains:

- 2 military explorers
- 1 civilian explorer

### Local defense

When enemy units are actually detected inside the town-defense envelope, policy raises the cheap Byzantine counter-unit floor and requests one watchtower.

When an enemy building is detected in that envelope, the same defensive response is requested.

### Local counter response

Observed enemy unit types now produce bounded counter pressure:

- 2+ Knights → 18 spearmen and 8 camels
- 3+ Archers → 18 skirmishers
- 3+ Skirmishers → 18 archers

These rules intentionally use only enemy units that the engine's town-targeting facts expose. They do not claim omniscient knowledge of the opponent's army.

## Ownership boundary

The changes remain policy-side. `militaryUnits.per`, `construction.per`, `economy.per`, `technologies.per`, and `militaryBehavior.per` remain execution owners.

The next architectural upgrade should therefore not be another pile of static unit-count rules. It should be a closed-loop requirement/deficit controller that consumes the existing observations and goals.

## Qualification status

Static runtime validation after the hardening pass:

- `byzPolicy.per`: 183 opening parentheses / 183 closing parentheses before the latest additions; revalidation is required after any subsequent edits.
- Existing engine facts used by the new response include `up-enemy-units-in-town`, `up-enemy-buildings-in-town`, and `up-unit-type-in-town`.
- No new Goal or timer allocation was introduced.
- No XS dependency was introduced.

Runtime gameplay validation remains a separate gate; this audit does not claim that static qualification proves strategic success.
