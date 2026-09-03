# AEGIS Machine Evidence Matrix and Uncertainty Register

This register is deliberately conservative. It records what was actually observed, what it supports, what it does not prove, and what evidence would promote or demote the claim.

| Domain | Claim | Evidence | Confidence | Does not prove | Promotion test |
|---|---|---|---|---|---|
| Runtime | AoE2DE_s.exe is the controlled build | installed file metadata + SHA-256 | CONFIRMED | behavior of other builds | hash same executable |
| Script | `.ai/.per` are AI script substrate | installed source + stock loads + engine vocabulary | CONFIRMED | exact parser implementation | native parser call graph |
| Loading | player AI rules filename is resolved by engine | `getOrExtractPlayerAiRulesFileName` vocabulary | STRONG | complete acquisition sequence | verified caller/callee chain |
| Strategy loading | expert rules participate in strategy AI | `loadExpertRules`, TribeStrategyAIModule | STRONG | exact timing/order | native call graph |
| Rules | rules have IDs | `ruleID`, `mCurrentRuleID`, invalid-ID diagnostics | CONFIRMED | allocation algorithm | function body |
| Rules | rules have priority | `mPriority`, xs priority APIs, duplicate-priority diagnostics | CONFIRMED | comparator direction | comparator implementation |
| Rules | rules have min/max intervals | interval fields + XS APIs + duplicate diagnostics | CONFIRMED | scheduling formula | scheduler implementation |
| Rules | sorted rule representation exists | `mSortedRules`, `mNextSortedRuleIndex`, sorting diagnostics | STRONG | exact sorting key | native sort routine |
| Groups | rule groups are first-class | group fields, group APIs, allocation diagnostics | CONFIRMED | exact scheduler interaction | group update implementation |
| Lifecycle | rules can be enabled/disabled | XS APIs | CONFIRMED | persistence across reloads | runtime experiment |
| Lifecycle | current rule can disable itself | `xsDisableSelf` signature | CONFIRMED | exact point of state mutation | experiment |
| Diagnostics | execution failure is observable | `ruleID=%d failed execution` | CONFIRMED | recovery policy | controlled failing rule |
| Diagnostics | malformed scheduler metadata is rejected | duplicate priority/min/max diagnostics | CONFIRMED | whether failure aborts whole module | runtime test |
| State | goals are persistent script state substrate | widespread goal references/writes | CONFIRMED | exact storage lifetime | controlled lifecycle experiment |
| State | strategic numbers are a separate state substrate | SN vocabulary + script use | CONFIRMED | whether all SNs share identical semantics | API-level test |
| State | timers are explicit state | `up-get-timer`, `up-set-timer`, stock usage | CONFIRMED | exact timer resolution | runtime timing experiment |
| UP | fact queries exist | `up-get-*fact` family | CONFIRMED | exact fact table | interface ledger |
| UP | focus-player queries exist | `up-get-focus-fact` | CONFIRMED | exact focus-selection lifecycle | experiment |
| UP | feasibility predicates exist | `up-can-build`, `up-can-research`, `up-can-train` | CONFIRMED | all hidden prerequisites | controlled scenarios |
| UP | resource state is queryable | resource amount/percent vocabulary | CONFIRMED | exact economic model | runtime probes |
| UP | pending production is queryable | `up-pending-objects` and train-site vocabulary | STRONG | complete queue semantics | production probe |
| UP | search state is mutable | reset/filter/find family | STRONG | exact lifetime | repeated-query experiment |
| UP | group creation is bounded/fallible | bounds diagnostics for `up-create-group` | CONFIRMED | exact maximum in every build | build-specific test |
| UP | point geometry is queryable | distance/elevation/terrain/zone vocabulary | CONFIRMED | exact coordinate system | controlled map probe |
| UP | path distance exists | `up-get-path-distance`, path diagnostics | STRONG | exact pathfinding implementation | runtime measurement |
| UP | target/object state is queryable | object/target/type data families | CONFIRMED | complete object schema | API ledger |
| Actions | actions have explicit result states | completed/failed/invalidated/search-needed strings | STRONG | exact enum values | native state map |
| Actions | orders and actions are distinct | order/action vocabulary and diagnostics | STRONG | complete class hierarchy | native call graph |
| Combat | target selection can retarget | better-target/current-target/invalidation strings | STRONG | exact scoring function | tactical experiment |
| Movement | pathability can invalidate action | cannot-path diagnostics | CONFIRMED | exact path algorithm | runtime test |
| Production | train/build are engine actions | `up-train`, `up-build` plus native action strings | CONFIRMED | queue timing | experiment |
| Research | research has status and cost state | research status/cost vocabulary | CONFIRMED | exact failure semantics | experiment |
| XS | rule control is script-addressable | explicit XS signatures | CONFIRMED | complete XS internals | native implementation |
| Validator | validator may reject runtime-valid semantic forms | observed corpus/runtime distinction | PROBABLE | universal validator behavior | paired runtime/validator test |
| Unit identity | unit ID, unit line, class ID differ | `unit-type-count` use + project investigation | CONFIRMED | every API's accepted categories | per-API ledger |
| Temporary state | argument range is API-context-sensitive | temporary-goal 3500 vs narrower compare context | PROBABLE | exact universal range table | exhaustive API testing |
| Native source | BXS definitions unavailable in recovered source | Pass 21 negative results | CONFIRMED | absence from shipped binary | Ghidra search |
| Native source | source archive is not automatically shipped-runtime source | mixed AGE/editor/genieutils provenance | CONFIRMED | no relationship whatsoever | provenance matching |
| Ghidra | full analysis may produce function-repair noise | Pass 33 log | CONFIRMED | that analysis is invalid | targeted function verification |
| AIExpert | native rule loader/parser vocabulary exists | `AIExpertEngine.cpp`, `loadRules`, parser/error diagnostics | CONFIRMED at vocabulary level | exact function ownership/call graph | recovered native function boundary |
| AIExpert | facts and actions are explicit rule-engine definitions | `Defining Fact`, `Defining Action`, indexed IDs | CONFIRMED at vocabulary level | exact registration timing | native definition/registration trace |
| AIExpert | rule representation contains indexed elements and debug metadata | `ruleElementsPtr`, `rule[j].element`, `ruleDebugInfo[j]` | STRONG | exact struct layout/ownership | data-structure recovery |
| AIExpert | persistent facts have a distinct evaluation phase | `Evaluating Persistent Facts`, completion, evaluated-fact diagnostic | CONFIRMED at vocabulary level | cadence/storage/snapshot semantics | runtime/native control-flow trace |
| AIExpert | rule navigation/debugging is explicit | `Next Rule`, `ResolveBreakPoint`, `AIDebugger`, jump bounds | STRONG | exact execution loop | native control-flow trace |
| AIExpert | native semantic layer exposes broad typed game-state vocabulary | fact, comparison, player-scope, feasibility, resource, unit, research, timer, strategic-number strings | STRONG | all symbols share one implementation table | registration/dispatch trace |
| UnitAI | update state exposes separate order/action/target/notification concepts | `CurrentOrder`, `CurrentAction`, target fields, queue sizes, update diagnostics | STRONG | exact storage/lifetime | mutation-chain trace |
| UnitAI | notifications can alter control flow | notify processing diagnostics and `stop or new action, breaking` | STRONG | synchronous vs deferred implementation | native call graph/runtime experiment |
| UnitAI | retryable work can trigger search/replacement actions | `ProcessRetryableOrder::`, new target, hunt/gather issuance diagnostics | STRONG | exact retry policy | native state transition trace |
| UnitAI | search is constrained candidate evaluation | LOS, search radius, object care, ownership classification, pathability, range, walls, current-target retention | STRONG | exact score formula | search function recovery |
| AI architecture | AI is decomposed into expert/rule, UnitAI, action, and search modules | retained native source-path corpus | STRONG inference | recovered programmer intent | caller/ownership/implementation trace |
| AI diagnostics | tested UnitAI diagnostic string region lacks direct RIP-relative consumers | full `.text` Capstone scan | CONFIRMED negative for tested representation | indirect/indexed/unused alternatives | alternate representation tests |
| AI diagnostics | tested UnitAI diagnostic string region lacks embedded absolute 64-bit pointers | executable-wide pointer scan | CONFIRMED negative for tested representation | relative/indexed/encoded alternatives | representation archaeology |

## Negative evidence that must survive

The project repeatedly searched recovered source archives for direct definitions of `BXSRuleModule`, `BXSRuleEntry`, `BXSRuleGroupEntry`, `mRules`, `mSortedRules`, `mRuleGroups`, `mCurrentRuleID`, and related interpreter methods without obtaining a clean source implementation. This is not a failure to be hidden. It establishes a boundary between source-contract archaeology and shipped-binary evidence.

Similarly, broad source searches for intuitively named functions such as `UpdateAI`, `EvaluateRules`, `ExecuteRule`, `ScheduleRule`, `InterpretRule`, and `InterpretTrigger` returned no direct matches in the recovered source material. The absence does not imply those concepts do not exist; it means naming-based source recovery was insufficient.

The latest native pass adds a second negative boundary: the broad AI diagnostic region was scanned for direct RIP-relative and absolute-pointer consumers without finding one. This does not justify declaring the diagnostics dead or the metadata indirect; it only eliminates the tested direct representations and requires competing representations to be enumerated.

## Machine questions still open

### Scheduler
- What is the exact priority comparator?
- Are higher numeric priorities always earlier, or is ordering context-dependent?
- How do min/max intervals interact with priority and starvation?
- What is the precise sorted-rule rebuild trigger?
- What happens to a rule's position when it is dynamically enabled?
- What happens when a rule changes its own priority while executing?
- Are interval fields measured in world time, simulation ticks, frames, or another unit?

### Interpreter
- Where does lexical parsing end and semantic rule construction begin?
- Are triggers and handlers interpreted independently or through a common dispatcher?
- What object owns the final rule graph?
- When are identifiers resolved: parse time, registration time, or execution time?
- Which failures are fatal to the module versus local to one rule?

### UP
- What is the complete argument type/range table?
- Which functions consume concrete unit IDs, unit-line IDs, class IDs, or combinations?
- Which searches retain state across rules?
- Which outputs are goals versus strategic numbers versus transient registers?

### Execution
- What is the exact bridge from script action to UnitAI/game action?
- Which action results are observable back through script state?
- How are invalidated actions represented to the script scheduler?
- What happens when multiple rules issue conflicting actions in one cycle?

### XS
- What is the exact runtime implementation of rule-control APIs?
- Are group lifecycle changes immediate or deferred?
- Does disabling a rule remove it from the sorted structure immediately?

### AIExpert / UnitAI bridge
- What native function owns `loadRules` and the first rule-list construction?
- Where does the rule evaluator request or emit an action/order?
- Which function writes UnitAI `CurrentAction` after an order is accepted?
- Which function consumes an action result and changes order/target state?
- Is search invoked by UnitAI directly, by an action object, or through a shared AI search service?
- What representation connects native fact/action IDs to their callable implementations?

## Promotion rule

No open question may be silently promoted because it is intuitive. A claim moves from PROBABLE to CONFIRMED only when evidence demonstrates the proposition itself, not merely a neighboring proposition.

## Reopening rule

If Ghidra or runtime experiments falsify a critical Layer-1 architectural assumption, the affected contract section reopens. Otherwise new evidence is appended as a dated amendment. Historical reasoning remains intact.
