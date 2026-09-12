# Competency 5.2 — Byzantine Military Technology Synchronization

**Status:** STATICALLY QUALIFIED / IMPLEMENTED  
**Implementation:** `AiBuilder/ByzBot.per` v1.3  
**Commit:** `16a7dc44a9347c63dbcd8ed3cf94d4b1c8d6546b`

## Contract

Composition policy now writes the existing AIBuilder military-policy Goals when a military threat class is active:

- `upgrade-military-lines = 1`
- `upgrade-military-smith = 1`
- `upgrade-military-generic = 1`
- `upgrade-military-villager-requirement = 10`

No research action was added to `ByzBot.per`.

## Executor audit

`technologies.per` directly consumes all four referenced Goals. `upgrade-military-lines` gates unit-line upgrades and unique-unit upgrades; `upgrade-military-smith` gates the blacksmith military-research block; `upgrade-military-generic` gates generic military/siege/other military research; `upgrade-military-villager-requirement` gates the minimum-villager precondition for these research rules.

The executor uses native `can-research-with-escrow` followed by `research`, with escrow release handled by the existing technology subsystem. This preserves AIBuilder as the research executor.

## External cross-reference

AIRef / AoE2 AI Scripting Encyclopedia confirms `set-goal` is a native action, `goal`/`up-compare-goal` read Goal state, and `can-research-with-escrow` is a native research-feasibility fact. It also documents the DE 32-element-per-rule limit.

The upstream AIBuilder `builder upgrades.per` confirms the intended architecture: a policy Goal enables military research while the upgrade library performs the actual `research` actions.

## Static qualification

The deployed file was downloaded from the committed source and checked locally:

- Parenthesis balance: **0**
- Rules: **12**
- Maximum rule element count: **30** (DE limit: 32)
- Rules over 32 elements: **none**
- Military-policy Goal writes: **6 each** across the active composition/mixed-policy synchronization rules
- No direct `train`, `build`, or `research` actions in `ByzBot.per`

## Evidence classification

- **DIRECT / CONFIRMED:** Goal definitions and phase writers exist in `AiBuilder.per` / `phaseUpdate.per`.
- **DIRECT / CONFIRMED:** `technologies.per` reads each referenced Goal and owns the research actions.
- **COMPOSED / CONFIRMED:** ByzBot composition observation can feed those existing research policy channels.
- **INFERRED / ENGINE-SPECIFIC:** Same-pass writer precedence and exact persistence when `phaseUpdate.per` and `ByzBot.per` both write the same Goal remain unqualified.
- **NOT CLAIMED:** Static qualification does not prove that a technology completed in the game world.

## Next boundary

Competency 5.2 is now structurally connected. The next practical production milestone is **5.3: composition → resource-cost profile → gatherer policy**, using the existing AIBuilder economy executor rather than adding a second economy engine.
