# Runtime Policy Fix — 2026-09-12

## Scope

Applied directly to the installed runtime candidate at:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\AIByzBuild\`

This change is deliberately policy-side. The AiBuilder execution machinery remains authoritative for research, training, construction, and execution.

## Confirmed root cause: Imperial Age stall

`phaseUpdate.per` writes `desired-age` and `desired-ageup-villagers`, but its later phases depend on `phase2-aisignal`, `phase3-aisignal`, etc. No Byzantine runtime module was found generating those phase signals. Therefore the bot could reach Castle Age while still retaining Phase 1's Castle-age ceiling.

The existing `technologies.per` age-up chain was already valid: it checks the desired age, villager threshold, `can-research-with-escrow`, releases escrow, and executes `research`. Manual Imperial research succeeding confirmed that execution was not the failure point.

### Fix

`byzPolicy.per` now makes actual `current-age` authoritative for age intent:

- Dark Age → desired Feudal, 22 villagers
- Feudal Age → desired Castle, 30 villagers
- Castle Age → desired Imperial, 45 villagers
- Imperial Age → desired Imperial, 60 villagers

This removes the dependency on a stale phase signal for age advancement without replacing the Builder's research executor.

## Confirmed Cataphract gap

The runtime already contains generic unique-unit production through `my-unique-unit-line` and generic unique-unit upgrade through `my-unique-unit-upgrade`. The AI scripting reference identifies Elite Cataphract as the Byzantine Castle-age unique-unit upgrade.

The missing component was Byzantine policy demand: the existing phase caps set `desired-number-uniqueunits` to zero.

### Fix

`byzPolicy.per` now requests a bounded Byzantine unique-unit portfolio:

- Castle Age: 6 unique units
- Imperial Age: 10 unique units
- Imperial Age: 3 stables to provide production capacity for both Cataphracts and the existing camel portfolio

The existing generic production and research paths remain unchanged.

## Additional policy hardening

The runtime root default for `desired-number-uniqueunits` was changed from `61` to `0`. This is a safer initialization value because unique-unit demand is now explicitly owned by Byzantine policy rather than relying on a generic sentinel/default.

Castle and Imperial policy also explicitly retain one monastery and one university so these requirements do not depend on phase-transition timing.

## Validation performed

- `AIByzBuild.per`: 1327 opening / 1327 closing parentheses.
- `byzPolicy.per`: 145 opening / 145 closing parentheses after the change.
- `byzPolicy.per`: 28 `defrule` forms and 28 `=>` action separators.
- No literal escaped-newline artifacts remain.
- Runtime backups created before modification:
  - `AIByzBuild\byzPolicy.per.pre_autonomy_20260912.bak`
  - `AIByzBuild.per.pre_autonomy_20260912.bak`

## Engineering basis

The design follows the established AEGIS/AegisProm lesson of separating requirement/policy from execution: observe authoritative state, write bounded requirements, then let the existing execution machinery act. It does **not** import AegisProm's production-director architecture or introduce new engine primitives.

The AoE2 AI Scripting Encyclopedia confirms that strategic numbers and commands must be treated as engine-defined interfaces and that effectiveness varies by primitive; accordingly, this change uses only primitives already demonstrated by the installed Builder runtime.
