# Layer 1 Native Pass — Predictive Boundary QC

**Layer:** 1 — Machine Understanding  
**Status:** Active; no completion promotion  
**Scope:** AIExpert semantic validation, persistent facts, UnitAI control, and predictive boundary definition

## 1. Objective

This pass consolidates the strongest current evidence and attacks a more precise question: where does an AI-facing request stop being script syntax and become native machine state or execution?

The native corpus exposes explicit validation diagnostics for rule context, goals, points, unit/building types, attributes, resources, players, timers, search sources, target objects, technologies, idle types, and research/building constraints. It also exposes `Init AI Facts`, persistent-fact evaluation diagnostics, and UnitAI vocabulary for orders, actions, targets, notifications, search, retry, and completion/failure.

## 2. Strongest current causal model

The defensible model is now:

`.per text → parse/semantic construction → native validation/resolution → AI state/evaluation → control request → UnitAI execution state → simulation → observable feedback`

This is a causal hypothesis with several independently supported boundaries. It is not yet a recovered native call graph.

The critical engineering distinction is:

`syntactic acceptance ≠ semantic validity ≠ control acceptance ≠ execution ≠ strategic success`

## 3. Native validation boundary

The validation diagnostics are important because they reveal that native AI interfaces actively interpret arguments in context. Examples include invalid goal, invalid unit/building type, invalid player, invalid timer, invalid search source, invalid target object, and resolved unit type constraints.

Therefore the eventual ByzBot architecture must treat machine-facing operations as typed/validated requests rather than raw integer commands.

A practical request lifecycle is:

`construct → resolve → validate → accept/reject → execute/queue → observe result`

Only the first two stages are currently broadly supported by native vocabulary; exact state representation for acceptance and execution remains open.

## 4. Persistent-fact boundary

`Init AI Facts` is an explicit native diagnostic boundary. `Evaluating Persistent Facts`, per-fact result reporting, and `Finished Evaluating Persistent Facts` establish a named evaluation phase.

What remains unknown:

- exact cadence;
- storage owner;
- cache lifetime;
- invalidation mechanism;
- whether all fact classes share the same evaluator;
- whether rule evaluation consumes the stored result or reevaluates independently.

The next experiment must therefore measure freshness rather than infer it from naming.

## 5. UnitAI boundary

Native diagnostics distinguish `currentOrder`, `currentOrderPriority`, `CurrentAction`, target state, `OrderQueue`, and `NotifyQueue`. They also expose action failure/invalidation/search-required behavior and retargeting/search diagnostics.

The strongest current architectural hypothesis is:

`persistent intent/order → transient execution action → world interaction → invalidation/notification → reconciliation → continued execution or recovery`

This predicts that execution state must be treated as independently mutable from strategic intent.

## 6. Negative evidence that changes the investigation

A complete `.text` RIP-relative scan of the tested executable representation found no direct RIP-relative references to the exact addresses of selected API signature/name strings, nor to the widened surrounding metadata region. Selected UnitAI diagnostic strings likewise produced no direct references under that addressing-mode test.

This does **not** establish that the strings are unused. It falsifies only the narrow hypothesis that these semantics can be recovered by ordinary direct RIP-relative string references to those exact addresses.

The investigation must therefore prioritize metadata consumers, generated registration structures, compact indices, hashes, pointer tables, and initialization code.

## 7. Predictive test matrix

### Test P1 — fact freshness

`T0 state → evaluate fact → mutate source state → next evaluation`

Discriminate live evaluation, pass-boundary refresh, cache/invalidation, and class-specific freshness.

### Test P2 — order/action separation

`issue order → inspect action → perturb execution conditions → inspect order/action independently`

Prediction: an order can remain while its current action changes or becomes invalid.

### Test P3 — target-loss recovery

`valid target → invalidate target → observe notification/action state → search/retarget/recovery`

Prediction: invalid execution produces a reconciliation path rather than requiring strategic replanning for every mechanical failure.

### Test P4 — semantic rejection

Provide a controlled invalid argument while keeping the surrounding request valid.

Prediction: native validation rejects or defaults the operation before normal execution semantics.

### Test P5 — scheduler arbitration

Use two equivalent rules and vary one priority/interval/index parameter at a time.

Prediction: rule selection is deterministic under fixed state, revealing whether priority, interval, ordering, or another arbitration variable dominates.

## 8. Programmer-intent reconstruction

The accumulated evidence is consistent with a machine designed around multiple state lifetimes:

- game configuration and semantic initialization;
- persistent AI knowledge/facts;
- rule evaluation state;
- persistent unit intent/order;
- transient action/target execution state;
- event/notification state;
- simulation state.

This separation explains why a robust AI cannot be designed as a single monolithic `if condition then command` layer. The machine itself appears to mediate between persistent decisions and changing execution conditions.

This remains an intent inference until implementation-level ownership is recovered.

## 9. Architecture consequence

The future ByzBot should preserve these boundaries explicitly:

```text
OBSERVATION
    ↓
BELIEF / MACHINE FACTS
    ↓
STRATEGIC INTENT
    ↓
TACTICAL REQUEST
    ↓
NATIVE VALIDATION / ACCEPTANCE
    ↓
EXECUTION
    ↓
OBSERVED RESULT
    ↓
RECONCILIATION
    ├── retain
    ├── retry
    ├── retarget
    ├── replace
    └── abandon
```

This architecture is not yet implementation authority. It is the minimum conceptual structure required to avoid collapsing machine feasibility, execution state, and strategic desirability into one variable.

## 10. Promotion decision

No new implementation-level causal edge is promoted by this pass.

The most valuable unresolved bridge remains one real native state mutation chain. Vocabulary collection is now secondary.

Promotion requires:

`verified native entry/update → state read → condition → state write → downstream consumer`

A complete chain should then become the anchor for neighboring recovery.

## 11. Six-month recovery record

A future engineer should understand from this document that:

1. the project deliberately rejects string-name semantics as proof;
2. raw PE offsets must be mapped through section metadata;
3. malformed/unverified disassembly is quarantined;
4. XS is archaeology only and not a ByzBot dependency;
5. persistent facts and UnitAI are the two highest-value causal fronts;
6. the project has explicit falsification tests rather than relying on intuition;
7. 89% is a working progress estimate, not source reconstruction coverage or completion.

## 12. Next pass

Attack one verified state mutation boundary. Prefer the persistent-fact evaluator if a valid code/data owner can be recovered; otherwise pivot immediately to `CurrentOrder → CurrentAction` and trace an actual write/consumer chain. Do not spend another pass merely cataloguing strings unless they unlock that chain.
