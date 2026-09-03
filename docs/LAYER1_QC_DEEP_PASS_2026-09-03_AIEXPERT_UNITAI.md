# Layer 1 QC Deep Pass — AIExpert / UnitAI Findings — 2026-09-03

## Purpose

This pass quality-controls the preceding AIExpert/UnitAI native reconstruction, rechecks evidence boundaries, identifies missed practical implications, and converts the surviving findings into discriminating engineering tests.

## Executive QC result

The preceding pass contains substantial new value, but two corrections are required.

1. The retained AIExpert/UnitAI source-path and diagnostic corpus is strong native-vocabulary evidence, but it is not an implementation call graph.
2. The targeted disassembly artifacts produced during the follow-up investigation contain malformed instruction decoding at several selected anchors. They must not be used as function-boundary or control-flow evidence.

The core architectural findings survive because they were established from independent native vocabulary and diagnostic relationships rather than those malformed instruction windows.

## Evidence that survives QC

### AIExpert

The binary contains coherent native vocabulary for AIExpertEngine, rule loading, fact/action definition, rule elements, debug metadata, persistent-fact evaluation, rule navigation, and parser/loader failures.

This supports a native rule-engine subsystem with semantic construction and evaluation concepts. It does not yet establish exact object ownership, allocation, dispatch, or scheduler control flow.

### UnitAI

The binary contains coherent vocabulary for CurrentOrder, CurrentOrderPriority, CurrentAction, CurrentState, CurrentTarget, CurrentTargetType, target position, NotifyQueue, OrderQueue, update processing, notification processing, miscellaneous processing, search, retryable orders, invalidation, completion, and retargeting.

This supports a strong behavioral model of stateful unit execution and recovery. Exact state ownership and mutation order remain open.

### Search

The native search vocabulary exposes LOS, search radius, object-interest filters, ownership classification, defend-target restrictions, pathability, attack range, wall handling, current-target retention, and candidate selection diagnostics.

This supports constrained candidate evaluation rather than a simplistic nearest-object model. Exact scoring and ordering remain open.

## QC correction: targeted disassembly

`ai_region_disasm.txt` and `ai_anchor_disasm.txt` contain instruction sequences that are internally inconsistent with normal x64 code at multiple selected anchors. Examples include implausible instruction streams, suspicious absolute addresses, and control-flow targets that do not form defensible function boundaries.

Therefore `ai_cluster_refs.txt` cannot be treated as valid native reference evidence merely because a decoder emitted hits. A decoder result becomes evidence only after instruction-boundary plausibility and surrounding control flow are independently validated.

Correct evidence status:

- `native_disassembly_refs.txt`: usable as a negative result for the exact metadata addresses under its scan method, subject to implementation limitations.
- `ai_rip_data_refs.txt`: usable as a negative result for the tested representation.
- `ai_region_disasm.txt`: retained, but non-evidentiary for implementation semantics until re-decoded from verified code regions.
- `ai_anchor_disasm.txt`: retained, but non-evidentiary for implementation semantics until anchors are independently proven as instruction boundaries.
- `ai_cluster_refs.txt`: hypothesis-generation artifact only; its six hits must not be cited as native call/reference evidence.

## Why the correction matters

This prevents a critical archaeology failure mode: turning a byte-pattern match into a fictitious function graph. Native evidence requires valid decoding, plausible basic blocks, and preferably corroborating call-target or cross-reference evidence.

The architectural conclusions do not depend on the malformed windows and remain intact.

## Practical consequence: commands are requests, not guaranteed outcomes

The UnitAI evidence implies a safer ByzBot execution contract:

`INTENT → REQUEST → ACCEPTED/QUEUED → EXECUTING → RESULT → RECONCILE → RETAIN/RETARGET/REPLACE/ABANDON`

Do not collapse this into `DECISION → COMMAND → SUCCESS`. Native diagnostics explicitly distinguish failed, invalidated, completed, and search-required action states.

## Practical consequence: recovery belongs below strategic intent

If native execution preserves order state while an execution action fails or becomes invalid, strategic reasoning should not micromanage every transient path or target failure.

A future execution layer should own target validation, path failure, target loss, retargeting, retry policy, local search, action replacement, and completion reconciliation. This is an architecture recommendation, not a claim about exact native implementation.

## Practical consequence: search is a policy boundary

Native search vocabulary makes it inappropriate to model search as merely `findNearestEnemy()`.

ByzBot should separate:

`eligible candidates → hard filters → tactical features → score → hysteresis/current-target policy → selected target`

This lets Byzantine tactical doctrine alter scoring and policy without contaminating low-level candidate discovery.

## Practical consequence: target hysteresis should be explicit

Current-target retention plus better-target and retargeting diagnostics suggest that switching targets may have a cost. Exact native policy is unproven.

ByzBot should nevertheless model target choice as:

`current target value + switching cost + new target advantage + reachability`

rather than blindly selecting the highest instantaneous score on every evaluation.

## Practical consequence: queues and notifications are distinct research channels

`OrderQueue` and `NotifyQueue` should remain separate in our model until implementation evidence proves otherwise.

Research state should distinguish requested work, world/event notifications, transient execution state, and reconciliation state. Whether notifications are synchronous, deferred, or another mechanism remains open.

## Practical consequence: rule evaluation and UnitAI have different likely lifetimes

AIExpert vocabulary concerns rule lists, facts, actions, definitions, evaluation, and debugging. UnitAI vocabulary concerns per-unit orders, actions, targets, queues, and world interaction.

That difference is a strong architectural constraint and supports keeping strategic evaluation state separate from per-unit execution state. The bridge must still be recovered before this becomes a machine contract.

## External corroboration, not native proof

Official AoE2DE update notes independently document UnitAI/pathfinding behavior involving retargeting, queued commands, target tracking, exploration, and repeated-order/path failures. This corroborates the practical importance of stateful execution and recovery but does not prove the internal implementation recovered here.

Public AI scripting research likewise treats facts/actions as explicit interfaces of the rule engine. This is corroboration only.

## Falsification matrix

### Test A — action/order separation

Question: does accepting an order produce a separately observable action state?

Promotion: native or runtime trace showing order state retained while CurrentAction changes, followed by an action-result consumer.

Falsifier: both fields are proven to be duplicate views of one underlying state.

### Test B — invalidation/recovery

Question: does target/path failure mutate execution state and invoke search/replacement without necessarily deleting originating order state?

Promotion: native read → failure branch → action/target write → subsequent search/retry consumer.

Falsifier: order is always destroyed before recovery, or recovery is external to UnitAI.

### Test C — target hysteresis

Question: does current-target retention suppress switching to a marginally better candidate?

Promotion: controlled runtime experiment varying only candidate advantage while holding reachability and current target constant.

Falsifier: target always switches to the highest current score.

### Test D — notification timing

Question: are notifications processed before or after ordinary action progression within an update?

Promotion: native control flow or controlled runtime probe producing distinguishable outcomes.

Falsifier: an independent event loop is demonstrated with no ordering relationship to UnitAI Update.

### Test E — rule-to-order bridge

Question: where does rule/action evaluation cross into UnitAI order issuance?

Promotion: native call edge or runtime instrumentation connecting a known rule action to an order/state mutation.

Falsifier: strategic actions are shown to bypass UnitAI through an independent command subsystem.

## Metadata-dispatch QC

The negative direct-reference result is useful but narrow. The next search tree is:

1. recover metadata record geometry;
2. test relative offsets and 32-bit displacement tables;
3. test monotonic indices and fixed-size records;
4. locate initialization routines iterating over the region;
5. identify hash/index construction;
6. recover one API identifier lookup;
7. follow its callable target.

Do not assume a `{name, signature, function-pointer}` array.

## Object identity QC

The identity API family gives a useful topology:

`unit ID → object ID / copy ID / class / type / validity / availability / garrison`

Equal numeric values must not be interpreted as equal identity. The next experiment should follow one known unit through creation, lookup, transformation, garrison, and removal while recording every exposed identifier.

## Version/provenance QC

All native conclusions remain build-qualified. No native address, structure, or dispatch relationship should be presented as version-stable without a matching executable identity check.

## Updated engineering priorities

1. Recover valid native function boundaries in verified code regions.
2. Recover one UnitAI state mutation chain.
3. Recover one AIExpert rule-evaluation-to-action bridge.
4. Recover one API metadata lookup/dispatch path.
5. Run the first predictive runtime experiment against target loss/recovery.
6. Expand identity/lifecycle tracing after one representative path is closed.

## Completion assessment

Layer 1 remains active and incomplete.

The 86% figure remains a project-progress estimate, not a percentage of source reconstruction. The QC pass does not justify completion because implementation-level causal closure and runtime prediction are still missing.

The principal gain is epistemic discipline: malformed disassembly is explicitly quarantined, strong native-vocabulary findings survive, and practical architecture is translated into falsifiable tests.

## Final rule

Never allow a malformed decode, convenient variable name, parser interpretation, replay observation, or architectural intuition to become a machine fact without a promotion test.
