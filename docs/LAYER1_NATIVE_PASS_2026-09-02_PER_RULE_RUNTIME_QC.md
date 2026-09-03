# Layer 1 Native Pass — 2026-09-02 — `.per` Rule Runtime QC

## Scope
This pass is `.per`-first. XS remains machine-archaeology context only and is not a ByzBot dependency.

## Findings

### 1. AIExpert diagnostic corpus is structurally richer than a simple parser
The native corpus exposes `loadRules`, `Defining Symbol`, `Defining Constant`, `Defining Fact`, `Defining Action`, `ruleElementsPtr`, `rule[j].element`, `ruleDebugInfo[j]`, and explicit persistent-fact evaluation diagnostics.

These terms support a native rule representation with separately tracked symbols, constants, facts, actions, rule elements, and debug information. They do not by themselves prove class layout, field offsets, or execution order.

### 2. Rule loading has identifiable phases
The diagnostic sequence exposes loading, lexical analysis, parsing, successful parsing, and rule-definition messages. It also exposes distinct failure families for lexical, syntax, preprocessor, capacity, and file I/O failures.

Working model:

`.per source → loading → lexical/preprocessor processing → semantic rule construction → stored rule list`

This is a model, not yet an implementation-level call graph.

### 3. Persistent facts are the highest-value causal target
The native strings `Evaluating Persistent Facts`, `Fact[%d] evaluated persistently to %s`, and `Finished Evaluating Persistent Facts` establish a named evaluation phase and per-fact result reporting.

The exact cadence, storage object, and relationship to the normal rule pass remain unproven. The next promotion test is to recover the state read/write path around one persistent fact and correlate it with controlled `.per` behavior.

### 4. Fact vocabulary separates semantic classes
The corpus contains direct state facts (`population`, resources), derived facts (`population-headroom`, `military-population`), feasibility predicates (`can-build`, `can-research`, `can-train`), event/timer facts, and player-scoped relational queries.

This supports an experimental matrix to determine whether these categories share a common dispatch mechanism or branch into distinct native evaluators.

### 5. UnitAI evidence remains native-vocabulary evidence
The corpus exposes `CurrentOrder`, `CurrentAction`, `CurrentTargetID`, `CurrentTargetType`, `processNotify`, `processMisc`, `processIdle`, order/notification queue diagnostics, retargeting, retryable-order processing, and action completion/failure messages.

These support the working state-machine model but do not establish a function-level call graph. String-only xref hunting is retired as the primary UnitAI method.

### 6. Address-analysis correction remains enforced
The executable section mapping must be derived from PE section virtual/raw offsets. Raw offsets must never be treated as RVAs by simple addition to image base. String addresses in the AI corpus are data addresses; they are not code anchors unless a verified code reference is recovered.

### 7. Negative evidence
Direct string-to-code reference scans for selected AIExpert and UnitAI diagnostic strings produced no usable direct references. This does not imply the diagnostics are unreachable; indirect references, table-based dispatch, optimized code, or other representations remain possible.

## Practical architecture consequence

The eventual ByzBot control architecture should preserve the distinctions visible in the native machine:

`strategic intent ≠ action request ≠ order ≠ current action ≠ target ≠ execution result`

`.per` should exploit native fact/goal/strategic-number control surfaces where they demonstrably provide useful machine behavior rather than reproducing native subsystems unnecessarily.

## Next promotion targets

1. Recover one persistent-fact state mutation chain.
2. Recover one rule-index/eligibility/selection chain.
3. Recover one `.per` handler-to-native-control edge.
4. Recover one UnitAI `CurrentOrder → CurrentAction` mutation chain.
5. Use a minimal runtime `.per` probe to falsify competing scheduler/state-lifetime models.

## Evidence status
No new implementation-level causal edge was promoted in this pass. Layer 1 remains at 89%.
