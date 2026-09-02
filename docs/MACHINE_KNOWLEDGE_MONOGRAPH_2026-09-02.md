# AEGIS Layer 1 Machine Knowledge Monograph

**Status:** Operational knowledge baseline; evidence-enrichment amendment expected from Ghidra Pass 33.
**Purpose:** Preserve enough machine understanding that a future engineer can reconstruct the current operational model without relying on conversational memory.
**Authority:** Derived from controlled AEGIS investigations, installed runtime evidence, archived forensic passes, script evidence, and qualified source-contract artifacts.

## 1. Epistemic rule

This document is not a claim of total reverse engineering. It is an operational model with explicit evidence boundaries. A symbol string establishes vocabulary, not semantics. A source declaration establishes a type surface. A method body establishes implementation. A call site establishes a relationship. An assignment establishes a state transition. A controlled runtime experiment establishes behavior. Independent convergence upgrades confidence. Where evidence stops, the claim remains a hypothesis.

Evidence classes used throughout AEGIS:

1. **RUNTIME-IDENTITY** — directly verified installed executable identity.
2. **SCRIPT-CONSUMED** — behavior demonstrably consumable by `.ai/.per` scripts.
3. **NATIVE-VOCABULARY** — embedded names, diagnostics, or signatures in the executable.
4. **SOURCE-CONTRACT** — independent source/archive material that describes engine structures or APIs.
5. **NATIVE-IMPLEMENTATION** — verified function body, call relationship, or state transition in the shipped binary.
6. **RUNTIME-EXPERIMENT** — observed game behavior under a controlled candidate.
7. **INFERENCE** — model-derived interpretation from convergent evidence.
8. **HYPOTHESIS** — plausible but insufficiently demonstrated.
9. **HISTORICAL** — preserved artifact whose relevance to the current runtime is not established.

## 2. Runtime identity

The controlled installed executable is `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`.

Verified properties:

- Length: `71,648,568` bytes.
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`.
- File version: `101.103.48987.0`.
- Product version: `101.103.48987.0`.
- Product name: `AoE2 DE`.
- Company: `Microsoft Corporation`.
- Internal name: `AoE2DE.exe`.
- Original filename: `AoE2DE.exe`.
- PE machine: `0x8664`.
- PE format: PE32+ / 64-bit.
- Section count observed: 8.

This identity is the reference frame for all native evidence. Evidence from another executable, another build, an extracted development archive, or a historical source package must not silently inherit this identity.

## 3. Script substrate

The AI system consumes an `.ai` profile/entry configuration and `.per` script material. The script layer is therefore not merely a text configuration layer: it is a rule-programming substrate whose declarations become runtime rule objects and whose actions mutate game/AI state or request engine operations.

The operational abstraction is:

`AI profile -> script acquisition -> interpretation/compilation -> rule representation -> rule registration -> scheduling -> trigger evaluation -> handler/action execution -> world/state change -> next evaluation cycle`.

The exact native function boundaries remain partly opaque. Earlier source-contract archaeology repeatedly failed to recover direct definitions for several high-value BXS symbols, so names such as `BXSRuleModule`, `BXSRuleEntry`, and `BXSRuleGroupEntry` are treated as native vocabulary plus diagnostic evidence rather than as independently recovered class implementations.

## 4. Rule representation and scheduler vocabulary

The shipped executable contains convergent vocabulary for a rule system with at least these conceptual fields:

- current rule ID;
- rule ID validity/range;
- rule priority;
- minimum interval;
- maximum interval;
- enabled/disabled state;
- rule groups;
- sorted rule collection;
- current sorted-rule position/index;
- total rule count;
- total sorted-rule count;
- rule-group count;
- execution-failure diagnostics.

Observed native vocabulary includes `mCurrentRuleID`, `mNextSortedRuleIndex`, `mPriority`, `mMinInterval`, `mMaxInterval`, `mRules`, `mSortedRules`, `mRuleGroups`, `numberRules`, `numberSortedRules`, and `numberRuleGroups`.

The existence of these fields strongly supports a scheduler architecture in which rule execution is not simply source-order interpretation. Priority and interval are first-class scheduling metadata, while sorted rules form an execution-order representation.

This matters architecturally: AEGIS must never assume that lexical source order equals runtime execution order. Any implementation relying on that assumption is machine-incompatible until experimentally demonstrated otherwise.

## 5. Rule-control interface

The executable contains explicit XS rule-control vocabulary:

- `xsEnableRule(string ruleName)`;
- `xsDisableRule(string ruleName)`;
- `xsDisableSelf(void)`;
- `xsEnableRuleGroup(string ruleGroupName)`;
- `xsDisableRuleGroup(string ruleGroupName)`;
- `xsIsRuleGroupEnabled(string ruleGroupName)`;
- `xsSetRulePriority(string ruleName, int priority)`;
- `xsSetRulePrioritySelf(int priority)`;
- `xsSetRuleMinInterval(string ruleName, int interval)`;
- `xsSetRuleMinIntervalSelf(int interval)`;
- `xsSetRuleMaxInterval(string ruleName, int interval)`;
- `xsSetRuleMaxIntervalSelf(int interval)`.

These are stronger than generic strings because the executable contains human-readable signature-like descriptions. They establish that rule lifecycle and scheduling metadata are script-addressable concepts in the shipped system.

They do **not**, by themselves, establish exact scheduling mathematics, priority ordering direction, interval units, or whether all calls are legal in all rule states. Those questions require implementation/call-graph evidence or controlled experiments.

## 6. Scheduler failure semantics

Native diagnostics expose multiple validation and failure boundaries:

- invalid rule ID;
- rule execution failure;
- rule priority set twice;
- minimum interval set twice;
- maximum interval set twice;
- failed rule-group creation;
- failed rule-group entry creation;
- failed rule insertion into a sorted-rule list;
- failure to retrieve a valid rule group by ID;
- invalid rule-group activation range;
- insufficient rules / inability to retrieve next sorted rule;
- failed trigger interpretation;
- failed handler interpretation;
- failed compilation/sorting.

This vocabulary establishes an important engineering law: **the native runtime has explicit structural validation and failure paths around rule construction and scheduling.** AEGIS must therefore treat malformed rule graphs, duplicate scheduler metadata, invalid IDs, and execution failure as expected classes of machine fault, not impossible conditions.

## 7. Rule groups

The native surface distinguishes individual rules from rule groups. Group operations can enable/disable collections and query group state. Diagnostics reference group allocation, group-entry creation, group activation, and rule membership.

The safest architectural interpretation is that groups are a scheduler/control abstraction, not merely comments or source-file folders. A future AEGIS architecture may exploit groups for subsystem lifecycle, but only after verifying group activation semantics and interaction with priorities/intervals.

## 8. Script acquisition and loader boundary

Native strings expose `mAiScriptBaseName`, `aiRulesFileSize`, `mAiRulesFileData`, and a function-like symbol containing `getOrExtractPlayerAiRulesFileName`. The binary also contains a `loadExpertRules` symbol associated with `TribeStrategyAIModule`.

This provides convergent evidence for a pipeline in which player/scenario configuration selects or resolves an AI rules filename, the engine acquires rule data, and strategy AI code participates in loading expert rules.

A historical source-contract pass also identified `AIScript`/`AI Script` UI vocabulary and a stock source entry point containing explicit `.per` loads. This demonstrates that the script system is integrated into the broader game AI stack rather than being an external tool invoked after the fact.

The exact sequence `file read -> parser -> interpreter -> BXS objects` is not considered fully native-proven until the Ghidra call graph or runtime instrumentation closes the chain.

## 9. Interpreter evidence boundary

The source-contract archive contains approximately 182 source-like files, including AGE/editor and genieutils code, but direct searches did not recover concrete definitions for the high-value BXS symbols. This is a critical negative result.

The absence of source definitions means AEGIS must not manufacture a pseudo-source implementation from symbol names. The correct model is evidence layering:

`binary vocabulary + diagnostics + script behavior + recovered source-adjacent contracts + Ghidra implementation evidence`.

The negative result itself is preserved because it prevents future engineers from mistaking an unrelated open-source/editor substrate for the shipped game interpreter.

## 10. Facts, goals, strategic numbers, timers

The script/native vocabulary establishes a state substrate composed of at least:

- facts/predicates queried from the engine;
- persistent goals;
- strategic numbers;
- timers;
- search/filter state;
- object/group state;
- player and enemy information;
- engine-mediated actions.

The UP surface contains families for fact retrieval, fact aggregation, player facts, focus facts, object data, object-target data, type data, path distance, terrain, elevation, zone, timers, signals, shared goals, indirect goals, research status, pending objects, resource amounts, resource percentages, and many other state queries.

This is best understood as a **distributed state machine substrate**. Goals and strategic numbers are not intrinsically equivalent: their use must be inferred from actual writes, reads, lifecycle, and downstream consequences.

## 11. UP interface taxonomy

Recovered vocabulary includes, among others:

`up-get-fact`, `up-get-focus-fact`, `up-get-player-fact`, `up-get-target-fact`, `up-get-fact-max`, `up-get-fact-min`, `up-get-fact-sum`, `up-get-timer`, `up-get-precise-time`, `up-get-rule-id`, `up-get-search-state`, `up-get-group-size`, `up-get-path-distance`, `up-get-point-terrain`, `up-get-point-elevation`, `up-get-point-zone`, `up-get-threat-data`, `up-get-victory-data`, `up-get-object-data`, `up-get-object-target-data`, `up-get-object-type-data`, `up-get-target-fact`, `up-get-shared-goal`, `up-get-indirect-goal`, `up-set-timer`, `up-set-signal`, `up-set-shared-goal`, `up-set-indirect-goal`, `up-modify-goal`, `up-modify-sn`, `up-resource-amount`, `up-resource-percent`, `up-pending-objects`, `up-research-status`, `up-can-build`, `up-can-build-line`, `up-can-research`, `up-can-train`, `up-train`, `up-build`, and `up-research`.

The taxonomy reveals that the engine exposes both observation and actuation primitives. It also exposes intermediate search/filter machinery, meaning some apparently atomic facts may actually be produced through an engine-side query state.

## 12. Unit-line versus unit-ID discipline

A particularly important validator/runtime distinction emerged during investigation. `unit-type-count` can consume concrete unit IDs and, in qualified UP contexts, unit-line identifiers such as `knight-line`. The latter denotes a developmental unit line rather than a single concrete unit type.

This distinction must remain explicit in the knowledge graph:

`unit ID != unit line ID != class ID`.

A validator rejecting a unit-line token does not automatically prove that the runtime rejects it. Conversely, runtime acceptance does not make every validator profile correct. AEGIS therefore distinguishes **engine semantic legality** from **validator corpus legality**.

This is an archetypal machine lesson: the development toolchain may implement a stricter or different lexical model than the runtime's semantic model.

## 13. Temporary state and range constraints

Temporary goals are used as scratch registers in inherited and experimental code. The project encountered `temporary-goal` mapped to goal `3500`. The operational model is that a goal value may be legal for storage/modification while being illegal for a narrower API context that imposes a smaller comparison range.

Therefore:

`argument legality is context-sensitive`.

Do not generalize one parameter's valid range to every operation accepting the same underlying numeric type. This principle applies broadly to goals, strategic numbers, IDs, indexes, group counts, and placement parameters.

## 14. Action execution state machine

Native action vocabulary is substantially richer than a simple command queue. Observed strings expose:

- current action;
- current order;
- order priority;
- current target ID/type;
- action state;
- action invalidation;
- action completion;
- action failure;
- action requiring a search;
- action execution result;
- action list creation/deletion;
- movement completion notifications;
- target movement;
- target destruction;
- retargeting;
- pathability checks;
- distance checks;
- defensive and offensive behavior.

The practical model is:

`ORDER -> ACTION -> EXECUTION -> RESULT -> STATE UPDATE`.

An order is not equivalent to an action; an action is not equivalent to successful completion. Native diagnostics explicitly distinguish completion, failure, invalidation, and search-required states.

This directly validates the AEGIS architectural distinction:

`PROPOSAL != COMMITMENT != AUTHORIZATION != EXECUTION != SUCCESS`.

## 15. Targeting and retargeting

Native evidence shows target selection is dynamic. Strings describe finding better targets, retaining an existing target under conditions, invalidating targets, checking pathability, distance, target type, attack range, building/wall status, and target movement.

This means tactical behavior cannot safely be modeled as a single static `attack(target)` primitive. The engine itself maintains target/action context and can reconsider or preserve targets based on internal conditions.

AEGIS should therefore separate **strategic target intent** from **native tactical target execution**.

## 16. Movement and pathability

Native action vocabulary includes movement to coordinates, movement to units, evasive movement, backing distance, pathability, black-tile detection, target distance, desired distance, and inability to path to desired points.

The machine consequently possesses geometric/pathfinding state that can invalidate an otherwise sensible strategic command. AEGIS's authority layer must therefore be capable of rejecting or transforming an intent when execution preconditions are not satisfied.

## 17. Build/gather/research execution

Native vocabulary distinguishes build, gather, hunt, repair, heal, trade, convert, movement, attack, retreat/run-away, transport, unload, defend, explore, and related orders. The UP layer also exposes `up-can-build`, `up-can-research`, `up-can-train`, pending objects, train-site readiness, and research status.

The important design consequence is that feasibility is a first-class engine question. AEGIS should prefer:

`intent -> feasibility observation -> authorized action -> postcondition verification`.

Blind issuance followed by hope is inferior and directly contrary to the exposed machine model.

## 18. Production semantics

Production must be modeled as a pipeline rather than isolated train statements:

`strategic objective -> capability requirement -> composition -> production capacity -> technology prerequisites -> resource demand -> feasibility -> train/build action -> completion -> reinforcement/replacement`.

The native machine can expose pending objects and train-site readiness, which means queue/capacity state can be observed. This supports a richer production director than V3's fragmented direct train writers.

## 19. Research semantics

Research is also a capability transition, not merely an action. The machine exposes research status and cost-related UP vocabulary. A research command can fail because the technology is invalid, unavailable, already completed, or otherwise infeasible.

The AEGIS architecture should represent research as an authorized investment with expected strategic return and postcondition verification.

## 20. Economy as machine state

The UP surface exposes resource amounts, resource percentages, allied resource amounts/percentages, cost data, research cost, tech cost, escrow, commodity buy/sell, tribute, and gatherer retasking. This is substantially richer than a static gather-percentage table.

An economy director can therefore reason over deficits, opportunity costs, production queues, technology commitments, map-access effects, and reserve requirements rather than simply maintaining fixed worker percentages.

## 21. Search/filter subsystem

The UP vocabulary includes reset/filter/create/search families: `up-reset-search`, `up-full-reset-search`, `up-reset-filters`, `up-filter-include`, `up-filter-exclude`, `up-filter-distance`, `up-filter-range`, `up-filter-status`, `up-filter-garrison`, `up-find-local`, `up-find-remote`, `up-find-player`, `up-find-resource`, and related calls.

This implies an engine-side query workflow where a script can construct a query context and then retrieve results. Search state must therefore be treated as mutable execution context. A rule that forgets to reset filters or assumes query state is stateless can generate nonlocal bugs.

## 22. Group and control-group semantics

Native and UP vocabulary exposes group creation, group size, group flags, group types, commanders, and group disband/reset operations. `up-create-group` has explicit diagnostics for control-group bounds, count bounds, starting-index bounds, and empty local lists.

The machine therefore constrains group operations numerically and structurally. AEGIS should treat group creation as a fallible allocation/selection operation, not as a guaranteed collection constructor.

## 23. Error model

The engine exposes errors at several layers:

`lexical/parse -> rule construction -> scheduler registration -> trigger/handler interpretation -> execution -> action result -> world-state verification`.

Representative diagnostics include invalid identifiers/IDs, invalid parameter ranges, duplicate scheduler metadata, failed rule-group construction, failed interpretation, failed sorting/compilation, action failure, action invalidation, path failure, target invalidation, and malformed AI files.

This supports a generalized AEGIS error taxonomy:

- **E0:** source/lexical fault;
- **E1:** interpretation/compilation fault;
- **E2:** registration/scheduler fault;
- **E3:** authorization/feasibility fault;
- **E4:** execution fault;
- **E5:** postcondition failure;
- **E6:** stale/contradicted belief;
- **E7:** architectural collision/non-unique authority.

## 24. Why V3 failed architecturally

V3 contains useful strategic knowledge but violates several principles exposed by the machine and by its own static analysis. It contains many independent train/research writers, contextual fixed gather percentages, simple attack/retreat thresholds, duplicate villager-production ownership, and logical reset/set collisions.

The machine does not require that architecture. It merely permits rules. Therefore the problem is not that V3 is "too many rules"; the deeper problem is **distributed authority without explicit ownership**.

AEGIS must establish one owner per consequential state/action domain wherever feasible.

## 25. Scheduler-aware architecture law

Because priority, intervals, enable/disable state, and sorted execution exist natively, AEGIS should deliberately use scheduler semantics rather than fighting them.

Subsystems should have:

- explicit lifecycle;
- explicit cadence;
- explicit priority rationale;
- explicit enable/disable conditions;
- explicit writer ownership;
- explicit failure recovery;
- explicit verification.

A subsystem that writes state without declaring its scheduling contract is architecturally incomplete.

## 26. Closed-loop control law

The combined machine evidence supports the following control loop:

`OBSERVE -> NORMALIZE -> UPDATE BELIEF -> FORM INTENT -> CHECK AUTHORITY -> EXECUTE -> VERIFY -> REMEMBER -> REPLAN`.

This is not merely a software style preference. It is the architecture that best respects the machine's separation between information retrieval, state representation, action execution, result states, and recurring rule evaluation.

## 27. Information/authority separation

The fundamental AEGIS law is:

**Information flows upward; authority flows downward.**

Observation rules may collect facts. Deliberation may transform observations into hypotheses and candidate plans. Authority determines whether a candidate may act. Execution performs side effects. Verification measures actual consequences. Memory records the episode.

No observation routine should secretly issue consequential side effects. No execution routine should invent strategic objectives. No verification routine should redefine success merely because an action was issued.

## 28. What the machine demonstrably permits us to build

With the established operational contract, AEGIS can safely design around:

- persistent state represented in goals/SNs;
- timer-driven and interval-driven cycles;
- scheduler priority;
- lifecycle-managed rule groups;
- engine fact observation;
- feasibility-gated production/research/build actions;
- search/filter workflows;
- group and target management;
- action/result verification;
- failure and recovery states;
- controlled XS usage where separately qualified.

## 29. What remains unknown

The following are explicitly not promoted to full machine facts:

- exact native priority comparator implementation;
- exact interval scheduling algorithm and units in every context;
- complete rule-group scheduling interaction;
- exact parser/interpreter call graph in the shipped binary;
- complete BXS class definitions from source;
- complete XS implementation internals;
- exact ordering of all AI module updates;
- every UP argument's precise type/range semantics;
- complete action state transition tables;
- exact native execution boundary for every script primitive.

These unknowns remain hypotheses/evidence targets. They do not block the operational Layer-2 architecture because the architecture is constrained to the demonstrated interface surface.

## 30. Ghidra amendment protocol

Pass 33 is an evidence-enrichment operation. When the active Ghidra project is finalized, its findings must be ingested as a delta against this document, not silently merged into existing claims.

For every strengthened claim record:

`claim -> prior evidence -> new evidence -> changed confidence -> changed architecture consequence`.

For every contradicted claim record:

`claim -> prior assumption -> falsifying evidence -> affected gates -> corrective interpretation -> implementation impact`.

This preserves the history of reasoning and prevents hindsight from erasing uncertainty.

## 31. Operational exit principle

Layer 1 is complete when AEGIS can answer the engineering question:

> What can the shipped AI machine observe, represent, schedule, execute, reject, invalidate, and verify—and which of those statements are facts versus inference?

The current answer is sufficiently strong for strategic architecture, while native reverse-engineering remains an evidence-enrichment stream.

## 32. Continuation test

A future engineer reading only this monograph plus the linked evidence ledgers should be able to reconstruct:

1. the runtime identity;
2. the script substrate;
3. the scheduler vocabulary;
4. the state substrate;
5. the UP observation/action surface;
6. the action-result model;
7. the error model;
8. the evidence hierarchy;
9. the architectural consequences;
10. the exact boundaries of remaining uncertainty.

If they cannot, this document has failed its purpose and must be expanded rather than declared complete.
