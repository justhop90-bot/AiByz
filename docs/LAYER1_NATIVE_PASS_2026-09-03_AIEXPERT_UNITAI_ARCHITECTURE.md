# Layer 1 — Native Pass — AIExpert / UnitAI Architecture — 2026-09-03

## Executive result

This pass produced the strongest native-vocabulary evidence yet for the boundary between the AI rule engine and the UnitAI execution subsystem.

The executable contains retained source-path and diagnostic material naming a coherent AI implementation decomposition:

- `ai\Actions\ActionHeroPower.cpp`
- `ai\Actions\ActionMissile.cpp`
- `ai\Actions\ActionMove.cpp`
- `ai\Actions\ProjectileData.cpp`
- `ai\aiexpert.cpp`
- `ai\AIExpertEngine.cpp`
- `ai\Modules\ObjectSpawnData.cpp`
- `ai\Modules\TribeInformationAIModule.cpp`
- `ai\Modules\TribeUnitAIModule.cpp`
- `ai\Modules\UnitAIModule.cpp`
- `ai\Searching\aisearch.cpp`

This does not by itself prove that every retained source-path string corresponds to a live callable implementation in the tested build. It is native-vocabulary evidence. Its value comes from the unusually coherent set of neighboring diagnostics and field names.

## 1. AIExpertEngine: rule representation and loading surface

The native corpus contains the following structural vocabulary in the `AIExpertEngine.cpp` region:

- `loadRules for listId=%d, file=%s`
- `Defining Constant`
- `Defining Fact[%d] ...`
- `Defining Action[%d] ...`
- `ruleElementsPtr`
- `list->ruleElements[list->ruleElementsPtr]`
- `(*list->rule[j].element)`
- `ruleDebugInfo[j].cString()`
- `defRule(`
- `Next Rule:`
- `Evaluating Persistent Facts`
- `Finished Evaluating Persistent Facts`
- `Fact[%d] evaluated persistently to %s`
- `AIExpertEngine::ResolveBreakPoint`
- `AIDebugger`

The same region contains parser/loader failures for missing identifiers, invalid keywords, malformed directives, missing rule parentheses, missing rule sides, invalid identifiers, list capacity, rule length, string-table capacity, and missing files.

### Evidence interpretation

**Confirmed at vocabulary level:** the native binary contains a rule loading/parsing subsystem with explicit fact/action definition concepts, rule-element storage, rule-debug information, persistent-fact evaluation, and rule navigation/debugging concepts.

**Not yet proven:** the exact in-memory structure, ownership, allocation algorithm, execution dispatcher, or function call graph connecting these concepts.

## 2. The rule substrate is richer than a flat trigger/handler list

The combination of `ruleElementsPtr`, indexed `rule[j].element`, `ruleDebugInfo`, `listId`, and `loadRules` supports a stronger model than a simple array of opaque callbacks.

Current model:

`AI file -> lexical/parser stage -> definitions (constants/facts/actions) -> rule/list representation -> rule elements/debug metadata -> evaluation`

The model remains a hypothesis where implementation ownership is concerned, but the vocabulary establishes multiple distinct native objects/concepts that must be accounted for by any accurate reconstruction.

## 3. Persistent facts are an explicit evaluation phase

`Evaluating Persistent Facts` and `Finished Evaluating Persistent Facts` are distinct native diagnostics, followed by `Fact[%d] evaluated persistently to %s`.

This establishes a native distinction between ordinary rule processing vocabulary and a persistent-fact evaluation phase.

It does **not** yet establish:

- whether persistent facts are recomputed every scheduler pass;
- when they are invalidated;
- whether they are stored in the same table as ordinary facts;
- whether rule evaluation observes a snapshot or live mutable fact state.

These are now explicit predictive questions.

## 4. Native fact/action vocabulary is directly tied to the engine contract

The same native region contains a large fact vocabulary including:

`building-count`, `building-type-count`, `can-afford-unit`, `can-build`, `can-research`, `can-train`, `civilian-population`, `current-age`, `game-time`, `military-population`, `population-headroom`, `players-unit-count`, `players-unit-type-count`, `research-completed`, `resource-found`, `strategic-number`, `timer-triggered`, `unit-count`, `unit-type-count`, `victory-condition`, and related player/resource/game-state queries.

It also contains the complete comparison vocabulary:

`less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `not-equal`.

Player-scope vocabulary includes `any-*`, `every-*`, and `this-*` forms.

This strongly supports the model that the rule engine is not merely dispatching precomputed booleans. It has a native semantic layer that exposes typed game-state queries and comparison/scope operators to the rule system.

## 5. AI strategy numbers are visible at the same native boundary

The native fact/constant corpus contains a substantial strategic-number surface, including attack-group sizing, exploration, defense distance, target evaluation weights, gatherer percentages, attack timing, build frequency, retasking, dropsite distances, cooperation, and other strategic controls.

Examples include:

- `sn-minimum-attack-group-size`
- `sn-number-attack-groups`
- `sn-target-evaluation-distance`
- `sn-target-evaluation-hitpoints`
- `sn-target-evaluation-damage-capability`
- `sn-target-evaluation-kills`
- `sn-target-evaluation-range`
- `sn-attack-intelligence`
- `sn-initial-attack-delay`
- `sn-intelligent-gathering`
- `sn-food-gatherer-percentage`
- `sn-gold-gatherer-percentage`
- `sn-wood-gatherer-percentage`
- `sn-retask-gather-amount`

This is native vocabulary evidence for a broad strategic-control layer beneath the rule engine. It is not evidence that these values are all consumed by the same scheduler or at the same cadence.

## 6. UnitAI: order/action/notify sequencing is more explicit than previously recorded

The UnitAI diagnostics contain a particularly informative sequence:

`UnitAIModule got an update of %d, idleTimer=%d.`

followed by state inspection including:

- `CurrentOrder`
- `CurrentOrderPriority`
- `CurrentAction`
- `CurrentState`
- `CurrentTarget`
- `CurrentTargetType`
- `CurrentTargetPosition`
- `NotifyQueueSize`
- `OrderQueueSize`
- order-history records

The same corpus contains:

`Processing %d notifies ...`

`Notify processing returned stop or new action, breaking.`

`Calling processMisc:`

`Calling lookAround.`

`Leaving Update:`

and explicit order reception diagnostics:

`UNIT AI: I got an order from %d at worldTime=%u.`

with order type, target, target owner, target position, range, immediate flag, front/priority, queue insertion, and old-order preservation behavior.

### Stronger provisional causal model

`Update entry`

-> inspect current order/action/target state

-> process queued notifications

-> notification may stop processing or produce a new action

-> continue into miscellaneous processing

-> check timers/patrol/target conditions

-> search/recovery where required

-> execute or transition action/order state

-> leave update with updated idle/timing state

This is still not a native call graph. The ordering is reconstructed from diagnostics and must remain labeled as native-vocabulary behavioral inference until implementation-level control flow is recovered.

## 7. Action invalidation has a defined recovery vocabulary

The native corpus contains:

- `Action %d has failed.`
- `Action %d has been invalidated or requires a search.`
- `Action %d has completed, currentActionValue=%d.`
- `ActionExecuted`
- `TargetUnderMinRange`
- `ProcessRetryableOrder::`
- `Retargeting`
- `Found a better target to attack`

The retryable-order path explicitly describes discovering a new target and issuing hunt/gather actions.

This strengthens the earlier model:

`requested order -> execution action -> world interaction -> result/invalidation -> recovery/search/retarget -> replacement action`

The critical distinction remains: the native corpus demonstrates that these concepts exist as diagnostic states; it does not yet prove their exact storage ownership or synchronous execution order.

## 8. Search is an explicit decision subsystem, not merely nearest-object lookup

The native search diagnostics expose:

- LOS
- search radius
- cared-about object types
- defend-target restrictions
- object population counts
- GAIA/SELF/FRIEND/NEUTRAL/ENEMY classification
- current-target retention
- pathability
- attack-range capability
- wall capability
- quick-path checks
- moveable-target counts
- attack-work state
- fallback to walls or `-1`

The native corpus names `ai::search` and `aisearch.cpp`.

This supports a high-confidence behavioral model in which target selection is a constrained candidate-evaluation process with pathability and current-target retention, not simply a nearest-enemy query.

## 9. Programmer architecture reconstruction

The retained source-path corpus reveals a deliberate-looking decomposition into at least four major concerns:

1. **AIExpert / AIExpertEngine** — rule loading, parsing, definitions, evaluation, debugging.
2. **UnitAI / TribeUnitAI** — per-unit control state, orders, actions, notifications, recovery.
3. **AI Actions** — concrete action implementations such as movement, missile/hero-power behavior, and projectile data.
4. **AI Searching** — candidate discovery and target selection.

This is a **constraint-driven architectural inference**, not recovered intent. The evidence supports the existence of separate conceptual modules; it does not justify claims about why the original programmers chose every boundary.

The strongest programmer-intent hypothesis is that the system separates declarative strategic reasoning from stateful per-unit execution because those layers have different lifetimes, inputs, and failure modes. This remains a hypothesis until callers, ownership, and state transitions are recovered.

## 10. Important negative result: direct string-to-code linkage remains absent

A full Capstone scan of the executable `.text` region found zero RIP-relative references into the broad AI diagnostic string region tested in this pass.

A separate absolute-pointer scan found zero 64-bit absolute pointers into that region.

Therefore the simple model

`AI diagnostic string -> direct RIP-relative code consumer`

is not supported for the tested representation.

Possible explanations remain open:

- indirect/indexed logging metadata;
- registration tables;
- generated logging infrastructure;
- encoded/relative references;
- diagnostics retained but not referenced by live code;
- Ghidra/decoder representation limitations.

No explanation is promoted without a discriminating test.

## 11. New predictive questions

### AIExpertEngine

- At what point does lexical parsing become semantic rule construction?
- What owns `listId` and `ruleElementsPtr`?
- Are facts/actions assigned stable IDs at parse time or registration time?
- Are persistent facts evaluated before every rule pass or on a separate cadence?
- How does a rule jump alter the sorted-rule cursor?
- What exact failure boundary separates one malformed rule from module-wide abort?

### UnitAI

- Where are `CurrentAction`, `CurrentOrder`, and target fields physically stored?
- Which function writes `CurrentAction` after an order is accepted?
- Which function invalidates an action after target/path failure?
- Does `processNotify` mutate action state directly or request a transition through another owner?
- Is `ProcessRetryableOrder` a method, helper, or diagnostic label from a larger function?
- When is the order queue consumed relative to `processNotify` and `processMisc`?

### Search

- Which function owns the candidate collection?
- Where are candidate classifications produced?
- Which state feeds `BESTUNITTOATTACK` scoring?
- Is pathability evaluated before or after target scoring?

## 12. Next pass

The next pass should stop widening vocabulary scans and instead exploit the completed `.text` disassembly when available.

Priority order:

1. Recover the first defensible `AIExpertEngine` function boundary around rule loading/evaluation.
2. Recover the first defensible UnitAI mutation chain for `CurrentAction` or `CurrentOrder`.
3. Recover the actual search function boundary associated with `ai::search`/`aisearch.cpp` vocabulary.
4. Trace one end-to-end path:

`rule/fact evaluation -> action/order request -> UnitAI state mutation -> notification/result -> recovery/search`

5. Use the result to design the first true predictive runtime experiment.

## Evidence status

- Native vocabulary: **CONFIRMED** for the retained strings and source-path corpus.
- Architectural decomposition: **STRONG inference**.
- Order/action/notify behavioral model: **STRONG inference**.
- Exact native call graph: **OPEN**.
- Exact state ownership: **OPEN**.
- Direct string-to-code representation: **negative for tested direct forms**.
- Layer 1 completion: **NOT MET**.
