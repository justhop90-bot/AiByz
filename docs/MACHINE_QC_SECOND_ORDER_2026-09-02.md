# AEGIS Layer 1 — Second-Order QC Findings

This is a deliberate adversarial review performed after the forty-plus-item preservation expansion. It asks not merely what is missing from the machine model, but what classes of misunderstanding could still survive even if the existing ledgers were read carefully.

## 51. Tick-boundary semantics

Determine precisely when the AI scheduler is evaluated relative to simulation ticks, pathing, production completion, resource collection, and other engine updates. A state snapshot without tick-boundary semantics can produce false causal conclusions.

## 52. Rule re-entrancy and recursion constraints

Determine whether a rule can indirectly cause itself or its group to become eligible again within the same evaluation window. Record safeguards against re-entrancy, recursive enablement, or repeated side effects.

## 53. Maximum action-block semantics

Determine whether action count limits are syntactic, interpreter limits, scheduler limits, or validator conventions. Preserve distinctions between source limits and runtime limits.

## 54. Transactional versus partial action sequences

Determine whether a multi-action handler behaves transactionally or can partially execute before failing. This determines whether recovery can safely retry an entire handler or must reconcile partial state first.

## 55. Feasibility snapshot consistency

Determine whether `can-*` predicates and subsequent commands evaluate against the same state snapshot. A feasibility result may become stale between observation and execution.

## 56. Resource arithmetic and rounding semantics

Document integer truncation, rounding, percentage conversion, overflow/underflow behavior, and comparison semantics wherever strategic numbers or resource calculations are used. Small arithmetic differences can create persistent threshold bias.

## 57. Equality/ordering edge cases

Preserve the semantics of `<`, `<=`, `>`, `>=`, equality, zero, negative values where legal, and boundary values for each relevant primitive. Threshold-heavy AI is unusually sensitive to off-by-one behavior.

## 58. String/name resolution semantics

Determine whether rule names, group names, constants, and load paths are case-sensitive, normalized, interned, scoped, or resolved dynamically. Name identity can be a hidden source of collision or failure.

## 59. Namespace collision model

Document whether constants, goals, strategic numbers, rules, groups, and local declarations occupy separate namespaces or share resolution rules. Preserve collision behavior and shadowing semantics where observable.

## 60. Include/load ordering semantics

Determine whether repeated loads are legal, whether load order affects symbol visibility or registration order, and whether duplicate declarations overwrite, reject, or coexist. This is critical for modular architecture.

## 61. Failure atomicity of scheduler metadata

Determine what happens when priority or interval modification succeeds partially or is attempted redundantly. Native diagnostics indicating duplicate modifications should be connected to actual state behavior.

## 62. Starvation and fairness analysis

Test whether high-priority or frequently eligible rules can starve lower-priority rules. If fairness exists, identify its mechanism; if not, preserve starvation as an architectural hazard.

## 63. Interval interaction matrix

Do not study minimum and maximum intervals independently. Determine their interaction with priority, rule enablement, group state, failure, and execution success. Build a matrix of expected scheduler behavior.

## 64. Group/rule state synchronization

Determine whether changing a group state immediately changes member-rule eligibility or whether synchronization occurs at a scheduler boundary. This affects safe subsystem activation.

## 65. Observability completeness

For every consequential action, identify whether success, failure, partial success, or invalidation is directly observable. If an outcome is not observable, define the inference mechanism and confidence degradation.

## 66. Semantic versioning of knowledge

Machine knowledge itself needs versioning. When an interpretation changes, preserve the old interpretation, evidence delta, new interpretation, and architecture impact instead of editing history into a single timeless claim.

## 67. Evidence dependency graph

Knowledge records should be able to depend on other knowledge records. If claim A depends on assumptions B and C, invalidating B must automatically mark A for review. This converts epistemic uncertainty into a manageable graph.

## 68. Experiment-design quality gate

Every controlled experiment should specify hypothesis, independent variable, dependent variables, controls, expected observations, confounders, stopping condition, falsification criterion, and interpretation rule before execution where practical.

## 69. Reproducibility across machines

Distinguish machine-local reproduction from environment-independent reproduction. Preserve OS, executable path, tool versions, Java/Python/Node versions where material, locale/encoding, and filesystem assumptions for investigations whose output depends on environment.

## 70. Preservation completeness metric

Create a measurable Layer-1 preservation score. Suggested dimensions: runtime identity, loader coverage, grammar coverage, scheduler coverage, state substrate coverage, API coverage, identifier typing, execution semantics, failure semantics, native evidence, reproducibility, contradiction handling, and re-entry-test performance.

A score is not a substitute for judgment, but it prevents the project from declaring completion merely because the documentation feels comprehensive.

---

# Adversarial conclusion

The first expansion primarily closed **missing topics**. This second-order review closes **missing relationships and failure modes**.

The central risk now is no longer that the repository lacks facts. It is that facts may remain disconnected. A future engineer could read every document and still fail to understand which state transitions cause which scheduler decisions, which observations become stale, which commands are atomic, which failures leave partial state, and which conclusions depend upon which evidence.

Therefore the next maturity stage is not another prose dump. It is **integration**:

`ontology + ledgers + evidence graph + state machines + experiments + replay alignment + invariants + re-entry examination`.

Only after those components cross-reference one another should Layer 1 be considered preservation-complete.
