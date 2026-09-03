# Layer 1 — Deep QC — `.pdata` Function Geometry Pass — 2026-09-03

## Status

ACTIVE / NOT COMPLETE

This document is an adversarial deep review of the `.pdata` function-geometry discovery from the preceding native pass. It separates what the discovery actually proves from what it merely enables, identifies missed implications, and converts the finding into a concrete archaeology and ByzBot engineering strategy.

## 1. What the `.pdata` discovery actually gives us

The controlled PE image contains 166,730 parsed runtime-function ranges. For this x64 executable, these records provide independently recoverable function start/end geometry for functions represented in the executable's exception/unwind metadata.

The important capability is not the number itself. The capability is a trustworthy coordinate system for native code bodies that does not depend on successful global Ghidra auto-analysis.

The resulting abstraction is:

`PE image -> section mapping -> .pdata runtime-function range -> bounded .text body`

This turns native archaeology from an unconstrained search into a finite candidate-enumeration problem.

## 2. What was missed in the previous pass

### 2.1 `.pdata` is more than a function-count source

The ranges can be used as a partition/index over `.text`. Every candidate string, data address, RIP-relative reference, indirect branch target, and suspicious code region can now be evaluated against a known function interval.

This permits questions that the earlier string-first method could not answer reliably:

- Which verified function contains an instruction at address X?
- Which functions read a bounded data interval?
- Which functions contain calls into a candidate subsystem?
- Which functions are unusually dense in references to AI data?
- Which functions share callers or callees with a candidate state transition?

### 2.2 Function geometry permits negative-space analysis

A failed string reference search is weak. A complete enumeration of verified functions over a bounded region is stronger.

If every function covering an AI-related region is examined and none accesses a candidate datum, that becomes a meaningful bounded negative result. The scope must still be stated precisely.

### 2.3 Function boundaries enable controlled disassembly validation

Malformed instruction decoding was a major problem in earlier targeted artifacts. A `.pdata` start/end pair provides a natural constraint: disassembly can be performed only inside a verified function range, with instruction boundaries validated sequentially from the function entry.

A candidate should not be promoted when an apparent reference begins in the middle of an instruction or crosses the verified function boundary.

## 3. New practical archaeology pipeline

The preferred pipeline is now:

1. Parse PE sections and `.pdata`.
2. Normalize all addresses to RVA and VA.
3. Build interval index for runtime-function ranges.
4. Map target data/string addresses into containing functions only when an actual code reference is found.
5. Disassemble bounded candidate functions from verified starts.
6. Recover direct calls, conditional branches, memory operands, and indirect-call sites.
7. Classify reads versus writes.
8. Identify repeated state fields and transition clusters.
9. Follow callers/callees one hop at a time.
10. Promote only after the semantic proposition is demonstrated.

The critical improvement is step 7: a reference is not enough. We specifically need to distinguish state observation from state mutation.

## 4. First implementation-level target should be a write, not a string

The most valuable native discovery would be a verified instruction sequence equivalent in semantics to:

`load CurrentOrder -> compare/branch -> store CurrentAction`

or:

`load current target -> validation/search -> store new target`

or:

`failure/completion -> invalidate current state -> enqueue/retry/search`

A state write establishes much more causal information than another diagnostic string because it identifies a machine transition boundary.

## 5. AIExpert implications

The known vocabulary `loadRules`, `Defining Fact`, `Defining Action`, `ruleElementsPtr`, `rule[j].element`, `ruleDebugInfo[j]`, `Evaluating Persistent Facts`, and `Finished Evaluating Persistent Facts` should now be treated as search anchors, not semantic endpoints.

The practical objective is to locate functions around the persistent-fact evaluation region, then identify:

`fact storage read -> fact evaluation -> result write/cache -> rule consumer`

If a persistent-fact result is cached, the cache lifetime becomes a major machine fact. It determines whether a rule sees a live simulation state, a sampled state, or a scheduler-cycle snapshot.

That distinction directly affects ByzBot architecture.

## 6. UnitAI implications

The known fields `CurrentOrder`, `CurrentOrderPriority`, `CurrentAction`, `CurrentState`, `CurrentTarget`, `CurrentTargetType`, `NotifyQueue`, and `OrderQueue` should be investigated as a state-machine neighborhood.

The highest-value candidate transitions are:

- order accepted -> action initialized;
- current action completed -> next action selected;
- current action invalidated -> recovery/search;
- notification received -> order/action mutation;
- better target found -> target replacement;
- path failure -> search/recovery.

The goal is to recover one complete transition, not to reconstruct UnitAI globally in one pass.

## 7. A new hypothesis about machine architecture

The evidence increasingly supports multiple state lifetimes rather than one monolithic AI state:

`rule-cycle state`
`persistent fact/result state`
`strategic-number/goal state`
`per-unit order/action state`
`queued notification state`
`simulation object state`

This explains why the system can evaluate a strategic rule while a unit continues executing an older order/action. The two state machines can operate at different temporal granularities.

This is a hypothesis until native state ownership and update sites are recovered.

## 8. Practical ByzBot consequence: do not fight the machine's state machines

ByzBot should eventually maintain its own strategic state above native tactical state.

The architecture should therefore be:

`machine observations`
`-> strategic belief`
`-> Byzantine intent`
`-> tactical request`
`-> native acceptance/execution`
`-> observed outcome`
`-> reconciliation

The bot should not continuously micromanage a unit merely because it can issue commands. It should issue durable intent and allow native UnitAI to perform appropriate local execution where that improves robustness.

## 9. Search should become a policy boundary

Native `ai::search`, LOS, search radius, object-interest filters, ownership classification, defend-target restrictions, pathability, and target retention imply that target acquisition is already a substantial machine subsystem.

Therefore ByzBot should decide **what kind of target is strategically valuable** and when target policy should change, while using native search/tactical facilities where possible.

This avoids duplicating an already complex tactical search engine and gives the bot more compute budget for strategic reasoning.

## 10. `.pdata` limitations

`.pdata` does not guarantee:

- semantic function names;
- source-level class boundaries;
- complete call graph recovery;
- correct C++ object layout;
- that every executable code block is represented as a runtime-function record;
- that a function's exception metadata reveals its semantic purpose.

Compiler-generated helpers, thunks, tail calls, indirect dispatch, and optimized control flow still require independent analysis.

Therefore `.pdata` is a geometry layer, not a semantic oracle.

## 11. Programmer-intent deduction strengthened by function geometry

Once verified functions can be grouped by shared state accesses, we can infer programmer design more rigorously.

Useful signals include:

- fields repeatedly read together;
- fields written in the same transition;
- queue mutation followed by wake/retry logic;
- validation immediately before state replacement;
- cleanup immediately after completion;
- separate functions for search versus execution;
- repeated ownership checks around object access;
- timer reads preceding retarget/retry behavior.

These patterns can reveal intended responsibility boundaries without pretending to recover source code verbatim.

## 12. New promotion rule

A native AI claim should be promoted to implementation-level only when all of the following are satisfied where applicable:

1. verified function boundary;
2. valid sequential instruction decoding;
3. identified state/data operand;
4. demonstrated read/write direction;
5. demonstrated branch/condition or call relationship;
6. downstream or upstream consequence established;
7. alternative interpretations considered;
8. evidence scope recorded.

A string, pointer, nearby function, or plausible disassembly fragment alone is insufficient.

## 13. Predictive test enabled by this pass

For a recovered state mutation function, construct:

`pre-state -> triggering input -> function executes -> field changes -> downstream consumer -> post-state`

The strongest first experiment will be a UnitAI transition where an observable event forces action invalidation or retargeting. If the predicted field transition and subsequent behavior match, the model gains its first runtime-backed causal edge.

## 14. Six-month recovery conclusion

The lasting lesson of this pass is that `.pdata` should be remembered as an **address-space control layer**. It does not tell us what a function means; it tells us where a function begins and ends. That distinction is exactly what the earlier archaeology lacked.

The project should therefore stop asking only “where is this string used?” and begin asking “which verified native functions can explain this state transition?”

That is a substantially more direct route to predictive machine understanding.

## 15. Next pass

Primary: enumerate `.pdata` functions intersecting the AIExpert and UnitAI native regions, then recover one verified state write.

Fallback: construct a bounded data-access scanner over verified function bodies and rank functions by references to AI state candidates.

Do not raise Layer 1 completion percentage until an implementation-level causal edge is recovered.
