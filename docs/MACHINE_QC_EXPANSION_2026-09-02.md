# AEGIS Layer 1 — Deep Quality-Control Expansion

**Date:** 2026-09-02  
**Purpose:** Final-quality preservation expansion for the AoE2DE AI machine model.

## 0. Why this document exists

The Layer 1 corpus must not be judged by document length. The actual criterion is recoverability: an engineer who did not participate in the original investigation should be able to reconstruct the operational machine model, distinguish demonstrated behavior from inference, reproduce important investigations, and identify the next native experiment without relying on conversational memory.

This document records the second-order QC pass. The first twenty identified deficiencies are not merely a checklist; each is converted into a concrete preservation artifact, model, registry, or test requirement. A second set of twenty deeper questions then extends the investigation beyond the first-order model.

The governing epistemic rule is:

> A useful explanation is not automatically a proven explanation. Preserve the observation, inference, uncertainty, falsifier, and engineering consequence separately.

---

# Part I — Twenty first-order QC expansions

## 1. Machine ontology

The repository must model the machine as an ontology, not only as prose. The core entities are Runtime, Loader, Script, Interpreter, Rule, Trigger, Handler, RuleGroup, Scheduler, Goal, StrategicNumber, Timer, Fact, UP primitive, XS primitive, Action, Target, ExecutionResult, Diagnostic, Validator, Deployment, Observation, Verification, and Recovery.

Relationships must be explicit where supported: `loads`, `constructs`, `registers`, `schedules`, `observes`, `stores`, `mutates`, `authorizes`, `executes`, `invalidates`, `verifies`, `fails`, and `recovers`.

The ontology is intentionally typed because a large class of AI errors arises when conceptually different objects are represented as interchangeable integers or generic state.

## 2. UP API ledger

Maintain a machine-readable ledger for every recovered UP primitive. Each record should include primitive name, category, arity, argument positions, identifier domains, value domains, read/write behavior, persistence, side effects, failure behavior, validator behavior, runtime evidence, build scope, and open questions.

The ledger must distinguish observation, feasibility, search, mutation, and execution APIs. Similar names must not imply equivalent semantics.

## 3. Identifier-domain system

Treat identifiers as typed domains rather than bare integers. At minimum: ConcreteUnitID, UnitLineID, UnitClassID, BuildingID, BuildingLineID, TechnologyID, PlayerID, GoalID, StrategicNumberID, FactID, RuleID, RuleGroupID, TimerID, search/object handles, and target identifiers.

The `knight-line` investigation demonstrates why this is mandatory. A syntactically valid integer can still be semantically invalid if its domain is wrong.

## 4. Range/context matrix

Ranges must be recorded by API and context, not merely globally. A goal value may be legal for storage but illegal for a comparison interface; a validator may impose a narrower static range than the runtime; a parameter may have different semantic ranges depending on API position.

Every range claim therefore needs: identifier, nominal range, API, argument position, contextual range, validator range, runtime evidence, and confidence.

## 5. Rule lifecycle state machine

Preserve the hypothesized rule lifecycle explicitly:

`ALLOCATED → CONSTRUCTED → REGISTERED → VALIDATED → SORTED → ELIGIBLE → SELECTED → EXECUTING → RESULT → NEXT ELIGIBILITY`.

Failure exits must be represented independently: construction, registration, sorting, trigger interpretation, handler interpretation, execution, and scheduler failures.

The state machine remains partly inferential until native call-graph evidence closes each transition.

## 6. Scheduler mathematics

The scheduler must eventually be described as a function rather than vocabulary:

`next_rule = f(priority, enablement, group state, min interval, max interval, current time, last execution, current rule, sorted index, execution state)`.

Do not infer priority direction, interval units, fairness, starvation behavior, or ordering guarantees from symbol names alone. Each requires native or controlled behavioral evidence.

## 7. Trigger/handler separation

Native diagnostics distinguish trigger interpretation from handler interpretation. The preservation model must therefore distinguish `rule eligibility/evaluation` from `action interpretation/execution`.

A rule can fail before firing or after firing; those are different machine states and must not be collapsed into one generic rule failure.

## 8. Script-language grammar

Preserve the script language as a language: lexical identifiers, constants, rule declarations, condition expressions, action expressions, load directives, groups, declarations, comments, nesting, and parser/interpreter boundaries.

The eventual grammar reference should identify which constructs are established by source/runtime evidence and which are inferred from observed scripts.

## 9. Loader graph

Preserve the complete acquisition hypothesis:

`configuration → AI filename resolution → file acquisition → .ai bootstrap → load graph → .per parsing → rule construction → registration → grouping/sorting → scheduler`.

Each edge must have evidence and confidence. Loader facts must remain scoped to the target executable/build.

## 10. Native/source boundary registry

Every source-like artifact must be classified by relationship to the shipped executable. Editor, AGE, genieutils, extracted symbols, comments, stock source, and target-build binary evidence are not interchangeable.

The registry must specify what an artifact permits us to infer and what it explicitly does not permit us to infer.

## 11. Negative-evidence ledger

Negative searches are durable evidence. Preserve search term, scope, expected result, actual result, search method, interpretation, ruled-out hypothesis, non-ruled-out alternatives, and next experiment.

Examples include failure to recover direct BXS interpreter definitions and failure of intuitive source searches for scheduler functions. This prevents future engineers from repeating unproductive searches or mistaking absence of evidence for evidence of absence.

## 12. Ghidra evidence protocol

Native reverse engineering must follow:

`string → xref → function → callers/callees → control flow → data flow → hypothesis → independent validation`.

Decompiler output is evidence, not automatically truth. Function boundaries, repaired bodies, thunks, imports, and data types must be independently inspected when the conclusion is architecturally consequential.

## 13. Ghidra failure-mode preservation

The substantial function-body overlap/repair noise observed during broad analysis is itself a methodological constraint. Broad automatic analysis may establish useful vocabulary and candidates while still requiring targeted verification.

The repository must preserve analyzer version, project identity, command line, log, failure counts, target functions selected, and resulting confidence.

## 14. Engine fault taxonomy

Use a common fault taxonomy:

- F0 lexical/source failure
- F1 parse failure
- F2 interpretation failure
- F3 object-construction failure
- F4 registration failure
- F5 scheduler failure
- F6 feasibility failure
- F7 execution failure
- F8 target invalidation
- F9 path/geometry failure
- F10 postcondition failure
- F11 stale-belief failure
- F12 authority collision
- F13 deployment/loader failure
- F14 validator/runtime divergence

The taxonomy is intended to connect machine failures to architectural recovery behavior.

## 15. Belief/observation/fact separation

The machine's observation must not be conflated with the strategist's belief. Preserve the chain:

`OBSERVATION → MEASUREMENT → FACT → BELIEF → HYPOTHESIS → DECISION`.

Confidence belongs to beliefs and hypotheses, not to raw facts that are directly measured, unless measurement uncertainty itself is material.

## 16. State ownership and authority

Every consequential state variable should have an ownership declaration. Sensors observe; models infer; planners propose; authority authorizes; executors issue actions; verifiers certify postconditions; recovery can revoke stale plans.

This formalizes the lesson from V3's fragmented multi-writer architecture: capability to write a state variable does not establish authority to own it.

## 17. Command/postcondition registry

Every consequential command should define:

`intent → preconditions → feasibility → authorization → command → execution → observation → postcondition → verification → recovery`.

The registry should eventually cover training, building, research, movement, attack, walling, resource assignment, and other consequential actions.

## 18. Temporal semantics

Timers must be modeled as temporal control primitives: cooldown, hysteresis, dwell time, retry interval, maximum dwell, delayed transition, observation cadence, action cadence, and commitment duration.

Historical timer usage is evidence that the AI designers were controlling temporal state, not merely delaying code arbitrarily. Exact semantics still require validation per timer family.

## 19. Machine invariants catalog

Preserve properties that should never be violated, such as:

- identifiers must match the argument domain of the primitive consuming them;
- feasibility is not execution success;
- execution success is not strategic success;
- consequential state has one declared authority;
- observations do not silently mutate strategic state;
- runtime claims are build-scoped;
- validator acceptance does not imply semantic correctness;
- restricted artifacts are never promoted merely for convenience.

These invariants should later become automated review and test gates.

## 20. Layer-1 re-entry test

The ultimate test is not whether the monograph is persuasive. It is whether an independent engineer can answer, from repository evidence alone:

1. What executable/build is targeted?
2. How are AI files acquired?
3. What is the `.ai/.per` relationship?
4. What constitutes a rule?
5. How are rules registered and scheduled?
6. What do priority and intervals mean, and what remains unknown?
7. What are rule groups?
8. What are goals, strategic numbers, timers, and facts?
9. What does UP observe, test, search, and mutate?
10. What does XS expose and under what qualification boundary?
11. How are identifier domains distinguished?
12. What constitutes command success?
13. What constitutes verified success?
14. What invalidates a command?
15. What failure classes exist?
16. What did source archaeology fail to recover?
17. What did native analysis establish?
18. What remains hypothetical?
19. Why is the architecture organized around observation/intent/authority/execution/verification/recovery?
20. What is the next experiment?

Passing this test is the preservation gate.

---

# Part II — Twenty second-order expansions

The first QC pass exposed a deeper issue: a machine model can still be incomplete even when its API inventory is excellent. The following twenty areas therefore extend from interface knowledge into semantics, causality, reproducibility, and eventual optimization.

## 21. Execution budget and scheduler cost model

Determine whether the engine imposes practical per-cycle, per-rule, per-player, or per-tick execution budgets. Establish whether expensive searches, nested conditions, and large action blocks consume materially different runtime resources.

This matters because an AI can be logically correct but operationally weak if its reasoning architecture exhausts scheduler or interpreter budget.

## 22. Evaluation atomicity and side-effect visibility

Determine when state changes become visible to subsequent conditions: immediately within a rule, after the handler, after the rule cycle, or after a larger engine update boundary.

This is essential for reasoning about sequences such as `set goal → test goal → issue action` and for avoiding accidental assumptions about intra-rule causality.

## 23. Rule ordering and determinism

Establish whether identical machine state produces deterministic rule selection. Identify hidden tie-breakers such as rule ID, source order, registration order, group order, or sorted-list index.

Determinism is foundational for replay reproducibility and debugging.

## 24. Concurrency illusion / subsystem interleaving

Even if the script machine is effectively single-threaded from the AI's perspective, the game engine may update world state between AI evaluations. Document which subsystems can change the observed state independently of the script.

This defines the difference between a stable internal state machine and an externally moving environment.

## 25. Observation latency model

Not every observation is necessarily contemporaneous with the world state. Determine whether searches/facts represent current engine state, cached state, last simulation tick, last network update, or delayed strategic information.

The resulting latency must feed confidence and decision timing.

## 26. Action commitment semantics

Distinguish command issuance from commitment. A train command may reserve resources; a build command may create a pending object; a movement order may remain active; a research order may occupy a production slot.

The machine model needs a formal concept of `pending commitment` rather than only `issued command`.

## 27. Resource reservation semantics

Determine when food, wood, gold, stone, population space, production capacity, and builder capacity become reserved versus actually consumed.

This is critical for any deficit planner. A planner that sees unspent resources without accounting for pending reservations can systematically overestimate available capacity.

## 28. Pending-object state machine

Native evidence indicates pending objects are observable. Reconstruct their lifecycle:

`requested → pending → placement/building → completed → invalidated/cancelled`.

Determine what observations distinguish each state and what actions can safely be retried.

## 29. Target identity and target lifetime

Formalize target handles and target invalidation. A target can die, move, become unreachable, leave a zone, become hidden, or cease to satisfy the action's semantics.

The execution bridge should therefore never assume that a target selected at time t remains valid at time t+Δ.

## 30. Path/geometry semantics

Document path distance, terrain, elevation, zones, obstructions, and movement feasibility as separate concepts. A numerical path result should not automatically be treated as tactical accessibility.

This becomes particularly important for walling, retreat, siege positioning, and reinforcement routing.

## 31. Search semantics and selection stability

Reconstruct whether UP searches return a stable ordering, arbitrary ordering, nearest-first ordering, ID ordering, or engine-defined ordering. Determine whether filters are compositional and whether searches observe live state.

An optimizer must not depend on undocumented search ordering.

## 32. Fact freshness and cache invalidation

For each high-value fact family, determine how quickly changes become visible and whether the engine caches values. Record refresh assumptions explicitly.

This is the machine counterpart of stale-belief reasoning.

## 33. Rule-group semantics as architectural isolation

Determine whether groups provide meaningful subsystem lifecycle isolation, scheduling isolation, priority inheritance, or only collective enablement.

Only verified semantics should be used to partition future AEGIS subsystems.

## 34. Error recovery semantics

Map which machine failures are recoverable without rebuilding rule state. Determine whether failed actions leave partial state, whether the next rule cycle can safely retry, and whether failure changes scheduler state.

Recovery must be designed around actual machine behavior, not generic software assumptions.

## 35. Validator/runtime equivalence matrix

Maintain a three-column semantic comparison:

`validator accepts/rejects | runtime accepts/rejects | intended engine semantics`.

The matrix should record divergences as first-class evidence. The project has already demonstrated that static corpus assumptions can be narrower than runtime semantics.

## 36. Build/version semantic fingerprint

A machine fact must be attached to an executable fingerprint. Preserve SHA-256, version/product metadata, relevant DLL inventory, tool versions, and investigation date.

When a new executable appears, compare fingerprints before reusing native conclusions.

## 37. Reproducible investigation bundles

Every major native investigation should be reproducible from a bundle containing input identity, commands, tool versions, project configuration, logs, extracted artifacts, analysis outputs, and conclusion.

The repository should permit a future engineer to recreate the evidence path without reconstructing command syntax from memory.

## 38. Causal chain model

For every consequential AI behavior, distinguish correlation from causation:

`observation → decision condition → action → machine effect → world effect → next observation`.

A replay showing that two events co-occur does not prove the first caused the second. Controlled intervention is required where causal claims drive architecture.

## 39. Counterfactual machine reasoning

Preserve a framework for asking: if the rule had not fired, what state would have resulted? If the action had failed, what alternate branch should have occurred?

Counterfactuals become the bridge from debugging to strategic planning.

## 40. State snapshot and replay alignment

Define a canonical state snapshot schema that can be aligned with replay timestamps and AI execution cycles. This allows a future engineer to compare:

`machine observation ↔ actual replay state ↔ issued command ↔ resulting state`.

This is the strongest route to empirical verification of machine-level claims.

## 41. Action idempotence classification

Every command should be classified as idempotent, conditionally idempotent, or non-idempotent. Reissuing a harmless observation differs fundamentally from repeating a resource-spending command.

Recovery logic depends on this classification.

## 42. Command race and stale-plan model

A plan can become invalid between authorization and execution. Document the possible race window and identify which preconditions must be rechecked immediately before issuing a consequential action.

This is particularly important for resource spending and military targeting.

## 43. Strategic-number/goal semantic drift

Historical AI code may reuse variables whose meaning changed over generations. Preserve declaration history, writer/readers, observed values, and interpretation changes.

A variable's name is not sufficient evidence of its current semantics.

## 44. Hidden state and unobservable variables

Identify state that materially influences behavior but is not directly exposed through the script interface. Examples may include scheduler internals, engine queues, AI-module state, or cached interpreter state.

Unobservable state must be represented as a latent variable in the architecture rather than silently ignored.

## 45. Machine capability ceiling

Create an explicit catalogue of what the script machine cannot do cleanly: unavailable information, delayed observations, action granularity, targeting limitations, scheduler limits, state-storage constraints, or unsupported operations.

Strategy must be designed around the machine's capability envelope rather than an imagined API.

## 46. Information-theoretic value of observations

Classify observations by decision value. An observation that merely confirms an already-certain fact has low value; an observation that distinguishes two strategically divergent hypotheses has high value.

This is the formal bridge between Layer 1 sensor design and Layer 2 Value of Information.

## 47. Machine-aware strategic complexity budget

Eventually define a complexity budget for reasoning: number of rules, search cost, state variables, action checks, observation cadence, and expected scheduler cost.

The strategic model must be compiled into a representation the machine can execute reliably.

## 48. Architecture-to-machine compilation model

Formalize implementation as compilation:

`strategic intent → abstract plan → executable policy → rule/state representation → native primitive sequence`.

This prevents the implementation layer from becoming a direct translation of prose strategy and provides a place to optimize for machine constraints.

## 49. Evidence decay and revalidation policy

Not all evidence remains equally trustworthy forever. Native facts may expire when the executable changes; replay observations may become irrelevant under balance patches; heuristics may fail at new skill levels.

Assign evidence a revalidation trigger: executable change, game patch, architecture change, contradictory observation, or elapsed research milestone.

## 50. Layer-1 exit is a living contract

Operational closure does not mean investigation is frozen. Layer 1 should remain closed as a dependency boundary while native research continues as evidence enrichment.

A new discovery may modify the machine contract only through controlled promotion: evidence → review → contradiction check → updated invariant/ledger → architecture impact analysis → versioned contract change.

This prevents endless reverse engineering from becoming an excuse to postpone strategic intelligence, while ensuring genuinely consequential native discoveries can still propagate upward.

---

# Part III — QC completion doctrine

The forty areas above define a much stronger preservation target than a monograph alone. The repository should eventually contain:

1. Machine ontology
2. UP API ledger
3. Identifier-domain ledger
4. Range/context matrix
5. Rule lifecycle model
6. Scheduler semantics
7. Script grammar
8. Loader graph
9. Native/source boundary registry
10. Negative-evidence ledger
11. Ghidra evidence protocol
12. Fault taxonomy
13. Belief/observation separation
14. State authority registry
15. Command/postcondition registry
16. Temporal semantics
17. Machine invariants
18. Re-entry examination
19. Execution budget model
20. Atomicity/visibility model
21. Determinism model
22. Interleaving model
23. Observation latency model
24. Commitment/reservation model
25. Pending-object lifecycle
26. Target lifetime model
27. Geometry/path model
28. Search semantics
29. Freshness/cache model
30. Group isolation semantics
31. Recovery semantics
32. Validator/runtime equivalence
33. Build fingerprinting
34. Reproducible investigation bundles
35. Causal/counterfactual model
36. Replay/state alignment
37. Idempotence/race classification
38. State semantic-drift registry
39. Capability ceiling
40. Machine-aware strategic compilation.

The purpose is not to produce forty documents for their own sake. The purpose is to eliminate classes of future misunderstanding. Where a subject is sufficiently mature, it should receive a dedicated machine-readable ledger or formal specification. Where evidence is insufficient, the repository must preserve the open question rather than inventing the missing semantics.

## Final QC question

Before calling Layer 1 preservation archival-final, ask:

> If the original conversation disappeared tomorrow, could an independent engineer reconstruct not only what we believe the machine does, but why we believe it, how strongly we believe it, what we tried that failed, how to reproduce the evidence, what the machine cannot do, and exactly where the remaining uncertainty lies?

If any answer is no, the preservation pass remains open.
