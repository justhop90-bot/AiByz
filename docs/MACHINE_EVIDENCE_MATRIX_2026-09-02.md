# AEGIS Machine Evidence Matrix and Uncertainty Register — Final Layer 1 Position

**Final investigation position:** 89%  
**Investigation phase:** CLOSED / HANDOFF  
**Completion certification:** NOT SATISFIED

This register records what was actually observed, what it supports, what it does not prove, and what evidence would promote or demote the claim. The final investigation phase stopped at 89% because no critical native causal edge was promoted without evidence demonstrating the proposition itself.

| Domain | Claim | Evidence | Confidence | Does not prove | Promotion test |
|---|---|---|---|---|---|
| Runtime | AoE2DE_s.exe is the controlled build | installed file metadata + SHA-256 | CONFIRMED | behavior of other builds | hash same executable |
| Script | `.ai/.per` are AI script substrate | installed source + stock loads + engine vocabulary | CONFIRMED | exact parser implementation | native parser call graph |
| Loading | player AI rules filename is resolved by engine | `getOrExtractPlayerAiRulesFileName` vocabulary | STRONG | complete acquisition sequence | verified caller/callee chain |
| Strategy loading | expert rules participate in strategy AI | `loadExpertRules`, TribeStrategyAIModule | STRONG | exact timing/order | native call graph |
| Rules | rules have IDs | `ruleID`, `mCurrentRuleID`, invalid-ID diagnostics | CONFIRMED | allocation algorithm | function body |
| Rules | rules have priority | `mPriority`, priority APIs, duplicate-priority diagnostics | CONFIRMED | comparator direction | comparator implementation |
| Rules | rules have min/max intervals | interval fields + APIs + diagnostics | CONFIRMED | scheduling formula | scheduler implementation |
| Rules | sorted rule representation exists | `mSortedRules`, `mNextSortedRuleIndex`, sorting diagnostics | STRONG | exact sorting key | native sort routine |
| Groups | rule groups are first-class | group fields, APIs, allocation diagnostics | CONFIRMED | exact scheduler interaction | group update implementation |
| Lifecycle | rules can be enabled/disabled | explicit lifecycle APIs | CONFIRMED | persistence across reloads | runtime experiment |
| State | goals are persistent script state substrate | goal references/writes | CONFIRMED | exact storage lifetime | lifecycle experiment |
| State | strategic numbers are a separate state substrate | SN vocabulary + script use | CONFIRMED | identical semantics for all SNs | API-level test |
| State | timers are explicit state | timer APIs + stock usage | CONFIRMED | exact resolution | runtime timing experiment |
| UP | fact queries exist | `up-get-*fact` family | CONFIRMED | exact fact table | interface ledger |
| UP | focus-player queries exist | `up-get-focus-fact` | CONFIRMED | focus lifecycle | experiment |
| UP | feasibility predicates exist | `up-can-build`, `up-can-research`, `up-can-train` | CONFIRMED | hidden prerequisites | controlled scenarios |
| UP | search state is mutable | reset/filter/find family | STRONG | exact lifetime | repeated-query experiment |
| UP | group creation is bounded/fallible | bounds diagnostics | CONFIRMED | universal maximum | build-specific test |
| UP | target/object state is queryable | object/target/type data families | CONFIRMED | complete object schema | API ledger |
| Actions | actions have explicit result states | completed/failed/invalidated/search-needed strings | STRONG | exact enum values | native state map |
| Actions | orders and actions are distinct | order/action vocabulary and diagnostics | STRONG | complete class hierarchy | native call graph |
| Combat | target selection can retarget | better-target/current-target/invalidation strings | STRONG | exact scoring function | tactical experiment |
| Movement | pathability can invalidate action | cannot-path diagnostics | CONFIRMED | exact path algorithm | runtime test |
| Production | train/build are engine actions | train/build APIs + action vocabulary | CONFIRMED | queue timing | experiment |
| Research | research has status and cost state | research status/cost vocabulary | CONFIRMED | exact failure semantics | experiment |
| Validator | validator may reject runtime-valid semantic forms | validator/runtime distinction | PROBABLE | universal validator behavior | paired runtime/validator test |
| Identity | unit ID, unit line, class ID differ | unit-type-count investigation | CONFIRMED | every API's accepted domains | per-API ledger |
| Temporary state | argument range is API-context-sensitive | temporary-goal storage vs narrower comparison context | PROBABLE | universal range table | exhaustive API testing |
| AIExpert | native rule loader/parser vocabulary exists | `AIExpertEngine.cpp`, `loadRules`, parser/error diagnostics | CONFIRMED at vocabulary level | exact ownership/call graph | verified native function |
| AIExpert | facts and actions are explicit definitions | `Defining Fact`, `Defining Action`, indexed IDs | CONFIRMED at vocabulary level | registration timing | native registration trace |
| AIExpert | rule representation contains indexed elements and debug metadata | `ruleElementsPtr`, `rule[j].element`, `ruleDebugInfo[j]` | STRONG | exact struct layout/ownership | data-structure recovery |
| AIExpert | persistent facts have a distinct evaluation phase | persistent-fact diagnostics | CONFIRMED at vocabulary level | cadence/storage/snapshot semantics | native/runtime trace |
| AIExpert | rule navigation/debugging is explicit | `Next Rule`, breakpoint/debug diagnostics | STRONG | exact execution loop | native control-flow trace |
| AIExpert | semantic layer exposes broad typed game-state vocabulary | facts, comparisons, player scopes, feasibility, resources, units, research, timers, SNs | STRONG | shared implementation table | registration/dispatch trace |
| UnitAI | update state exposes separate order/action/target/notification concepts | native diagnostics/state vocabulary | STRONG | exact storage/lifetime | mutation-chain trace |
| UnitAI | notifications can alter control flow | notify processing diagnostics | STRONG | synchronous/deferred implementation | native call graph/experiment |
| UnitAI | retryable work can trigger search/replacement | retry/search/retarget diagnostics | STRONG | exact retry policy | native transition trace |
| UnitAI | search is constrained candidate evaluation | LOS, radius, ownership, pathability, range, walls, target retention | STRONG | exact score formula | search recovery |
| AI diagnostics | selected AI anchors lack direct RIP-relative consumers | full `.text` Capstone scan | CONFIRMED negative for tested representation | indirect/indexed/unused alternatives | alternate representation tests |
| AI diagnostics | selected AI anchors lack exact absolute 64-bit pointers | executable-wide pointer scan | CONFIRMED negative for tested representation | relative/indexed/encoded alternatives | representation archaeology |
| PE | `.pdata` provides an independent native function coordinate system | 166,741 physical slots; 166,730 non-zero records; 11 padding slots | CONFIRMED | semantic function names | targeted body analysis |
| PE | valid `.pdata` ranges are structurally clean in tested image | unique monotonic starts; no interval overlaps | CONFIRMED | correctness of every decoded instruction | independent instruction validation |
| PE | runtime-function coverage is substantial but incomplete relative to raw `.text` | 45,879,189 bytes, ~88.88% of `.text` raw size | CONFIRMED | uncovered bytes are non-code | targeted section analysis |
| CodeView | executable embeds CodeView PDB identity | RSDS, GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`, age 1 | CONFIRMED | availability of matching PDB | obtain and GUID/age authenticate |
| Metadata | metadata-area pointer can lead to a valid native function | pointer `0x1417FF3E0` is a `.pdata` function start | CONFIRMED observation | semantic API ownership | caller/data-flow corroboration |
| Metadata candidate | `0x1417FF3E0` is an XS API implementation | direct disassembly is cleanup/destructor-like | REJECTED | all possible indirect associations | independent registration/call path |
| Ghidra | controlled import/save succeeded | headless report | CONFIRMED | complete clean analysis | terminated clean run |
| Ghidra | broad auto-analysis completed cleanly | timeout at 1800s during Disassemble Entry Points | NOT ESTABLISHED | native code is unanalyzable | targeted validation |
| Ghidra | broad analysis can produce repair noise | Pass33 logs | CONFIRMED | all results invalid | targeted function verification |
| XS | XS vocabulary describes runtime structures | embedded source/member/debug strings | CONFIRMED vocabulary | ByzBot dependency | not required; archaeology only |
| XS | XS is a Layer 1 completion dependency | project scope decision | REJECTED | usefulness as archaeology | none |

## Final negative-evidence boundary

The investigation repeatedly failed to recover clean implementation call graphs through naming-based source searches, direct string references, and broad auto-analysis. These failures are preserved because they constrain what can responsibly be claimed. The absence of direct RIP-relative or absolute-pointer references to selected AI strings eliminates those tested representations; it does not eliminate indirect, indexed, encoded, or table-mediated representations.

## Final implementation frontier

The remaining 11% is concentrated in: rule-loader/parser implementation; rule representation ownership; persistent-fact result mutation/freshness; scheduler comparator and interval transitions; rule/handler-to-native-action bridge; `CurrentOrder -> CurrentAction`; action failure/invalidation/completion propagation; required object lifecycle edges; and one predictive end-to-end `.per` path.

## Evidence promotion rule

No claim moves upward because it appears repeatedly in documentation. Promotion requires evidence that demonstrates the proposition itself. A native string, source filename, valid pointer, decompiler rendering, replay field, validator result, or numerical coincidence can motivate investigation but cannot substitute for implementation proof.

## Re-entry rule

If the project resumes, start with `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md` and target the smallest unresolved implementation edge. Do not restart broad vocabulary collection unless the new question specifically requires it.
