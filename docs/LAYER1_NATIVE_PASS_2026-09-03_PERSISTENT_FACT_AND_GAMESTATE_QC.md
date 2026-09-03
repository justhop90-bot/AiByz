# LAYER 1 — NATIVE PASS: PERSISTENT FACT AND GAME-STATE QC

Date: 2026-09-03
Status: ACTIVE / NOT COMPLETE
Working completion estimate: 89%

## Purpose

This pass extracts additional implementation-relevant information from the existing controlled native archaeology artifacts. The objective is institutional memory: a future engineer should be able to reconstruct what was learned, what remains uncertain, and why the next experiment exists without relying on conversational context.

## Scope

ByzBot remains a pure `.per` implementation. XS is not an implementation dependency or completion gate. Native XS material remains machine archaeology only.

## Controlled build

All native conclusions remain scoped to the controlled AoE2DE executable fingerprint already recorded in the repository. Native addresses and structures must not be generalized across builds without re-verification.

## New observation: AI fact initialization boundary

The controlled AIExpert context artifact contains the diagnostic boundary:

`Init AI Facts ---------------------------------------------------------------------------------`

followed by comparison operators and player-scope fact vocabulary including `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `not-equal`, `any-*`, `every-*`, and `this-*` forms.

This is stronger than a simple inventory of individual fact names. It establishes native vocabulary for an explicit fact-initialization phase and a structured family of comparison/scope operators.

Evidence class: native-vocabulary / diagnostic evidence.

It does not prove the exact initialization function, table layout, allocation mechanism, or whether all listed symbols are initialized in one routine.

## New observation: game-state semantic layer is initialized alongside AI facts

The same artifact records game-mode, player, civilization, map-size, victory-condition, starting-age, difficulty, resource-setting, and feature-state symbols around game-start processing, followed by:

`Finished applying game settings to new game start`

and then `Init AI Facts`.

The safe interpretation is that the executable contains a semantic initialization surface connecting game configuration to the AI fact environment. This does not prove that game settings are themselves stored in the fact table or that initialization is performed by one function.

## New observation: 60 FPS processing is an explicit AI-visible concept

The native vocabulary contains `UP-PROCESS-60FPS` alongside other game-mode/environment symbols.

This creates a concrete predictive question: whether an AI script can observe or adapt to a processing-rate mode through the normal UP fact/constant substrate, and whether that mode changes rule evaluation cadence.

Do not infer that `UP-PROCESS-60FPS` means the rule scheduler literally runs at 60 evaluations per second. The name establishes vocabulary, not cadence semantics.

## New observation: feasibility and validation form a distinct semantic layer

The same native context contains validation diagnostics for invalid goals, point goals, unit types, building types, attributes, resources, player numbers, technology IDs, timers, search sources, and target objects. It also contains feasibility predicates such as `up-can-build`, plus resolved-unit validation.

This supports a useful machine model:

`script argument -> semantic resolution -> validation -> operation/result`

This is preferable to treating every UP operation as an unchecked integer interface.

## Predictive consequence

A future `.per` authority layer should validate machine-visible prerequisites before issuing strategic requests where the relevant native feasibility predicate exists.

However, a feasibility predicate answers whether the engine considers an operation possible under its semantics. It does not answer whether the operation is strategically desirable.

Therefore:

`strategy decides desirability -> native feasibility gates executability -> execution result is reconciled`

## New fact taxonomy

The current native vocabulary supports at least these useful categories:

1. Direct state: population, resources, age, player state.
2. Derived state: population headroom, unit counts, research-completion state.
3. Feasibility: can-build, can-research, can-train.
4. Relational scope: any/every/this player groups.
5. Event/timer state: trigger/timer vocabulary.
6. Environment/game configuration: game mode, map size, victory mode, resource mode, processing mode.

This taxonomy is an engineering classification, not a recovered internal class hierarchy.

## Persistent-fact causal target

The existing native diagnostics remain the highest-value boundary:

`Evaluating Persistent Facts`
-> fact evaluation
-> `Fact[%d] evaluated persistently to %s`
-> `Finished Evaluating Persistent Facts`

The next native promotion requires locating a verified function boundary and identifying the result storage/read path.

## Runtime experiment design

The preferred first experiment is a freshness test using one direct-state fact and one feasibility/derived fact.

Control variables:

- executable/build;
- map;
- player configuration;
- AI script;
- rule priorities;
- intervals;
- game speed;
- starting resources;
- unrelated units/actions.

Independent variable: one world-state prerequisite.

Dependent observations: fact-visible behavior and resulting rule action timing.

Competing hypotheses:

A. facts are evaluated live at each rule decision;
B. facts are refreshed on a scheduler cadence;
C. persistent facts are cached until invalidated;
D. different fact classes use different refresh boundaries.

Promotion requires observations that distinguish at least two hypotheses. Merely observing that a rule eventually reacts is insufficient.

## Security and provenance

No local installation path, credential, replay content, user identifier, or private machine artifact is included in this public research record.

All negative results remain preserved. No malformed disassembly artifact is promoted. Source/debug vocabulary remains distinct from implementation-level call-graph evidence.

## Architecture consequence

The machine appears to provide a substantial semantic substrate before strategic `.per` logic executes: typed resolution, validation, facts, comparisons, player scopes, feasibility, timers, and game-state/environment predicates.

The ByzBot architecture should therefore concentrate its complexity where the machine does not already provide the required abstraction: strategic valuation, prioritization, Byzantine doctrine, conflict arbitration, long-horizon planning, and reconciliation policy.

## Promotion status

New claims promoted this pass:

- native vocabulary establishes an explicit `Init AI Facts` semantic boundary;
- comparison and player-scope operators are part of the native fact vocabulary;
- game configuration/environment state is exposed in the same AI semantic region;
- `UP-PROCESS-60FPS` is a native AI-visible concept, but its scheduling semantics remain unproven;
- validation and feasibility should be treated as separate from strategic desirability.

No native implementation call edge was promoted in this pass.

## Next pass

Recover the smallest verified persistent-fact state mutation or scheduler-state mutation. Prefer one implementation-level edge over another vocabulary inventory.
