# AEGIS Project Status — 2026-09-02

## Executive status

**Current layer: Layer 1 — Machine Understanding**  
**State: active, not declared complete**  
**Working completion estimate: 89%**

The project has accumulated a substantial operational and research record, but the completion standard is deliberately stricter than familiarity with AI scripting vocabulary. The remaining work is to turn important machine-facing observations into causal, implementation-level, and experimentally predictive understanding.

## Scope clarification

ByzBot is a pure `.per` implementation. XS and XS qualification are outside the implementation scope and are not Layer 1 completion dependencies. Native XS material may be retained as machine archaeology when it helps explain the executable, but it must not determine ByzBot architecture or implementation priorities.

The governing predictive machine standard explicitly excludes XS from project scope.

## Newest QC result

The latest pass revalidated the PE section map and performed a fresh direct-reference experiment against the native AIExpert and UnitAI diagnostic strings. The selected `loadRules`, persistent-fact, rule-definition, `CurrentAction`, `CurrentOrder`, `processNotify`, and action-failure strings are in `.rdata`. The tested direct RIP-relative reference representation produced zero consumers for the selected strings.

This is useful negative evidence but not proof that the diagnostics are unused or that all references are indirect. The investigation must now use structural anchors rather than string-address anchoring.

## Project objective

Build a high-quality Byzantine AI for AoE2DE by establishing the machine contract first, reconstructing general strategic intelligence second, specializing that intelligence for the Byzantine civilization third, and implementing the validated architecture last.

## Current `.per` completion gaps

1. Recover the native rule-loader/parser boundary.
2. Recover rule representation ownership and mutation.
3. Recover persistent-fact evaluation and its state boundary.
4. Recover scheduler ordering, intervals, and rule-state transitions.
5. Recover the rule/handler-to-native-action bridge.
6. Recover one UnitAI `CurrentAction` or `CurrentOrder` mutation chain.
7. Recover action failure/invalidation/completion propagation.
8. Establish at least one experimentally predictive end-to-end `.per` causal path.

These are now the implementation-facing priorities.

## Key methodological rule

All native raw offsets must be converted through the PE section containing the byte. The `.rdata` section has RVA `0x313c000` and raw pointer `0x313ac00`. Results produced by treating raw offsets as universal RVAs are not admissible evidence.

## `.per` causal model

The current working machine path is:

`.per source`
 -> lexical/preprocessor handling
 -> rule construction
 -> rule storage
 -> scheduling/evaluation
 -> facts/goals/strategic numbers
 -> action/handler
 -> native AI control
 -> UnitAI
 -> simulation
 -> observable feedback

Each arrow remains individually graded. Native source/debug vocabulary establishes semantic boundaries but does not by itself establish call-graph edges.

## AIExpert / rule-engine model

Native vocabulary establishes rule loading, constant/fact/action definition, indexed rule elements, debug metadata, persistent-fact evaluation, rule navigation, breakpoints, and parser/error categories. The exact function ownership, scheduler comparator, state mutation sequence, and handler bridge remain open.

## UnitAI model

Native vocabulary continues to support separate order, action, target, notification, search, retry, retargeting, and completion/failure concepts. The next promotion target is a concrete native mutation chain showing read → condition/transition → write → downstream consumer.

## Practical architecture implication

ByzBot should classify machine capabilities into trusted observations, trusted native control surfaces, compensating wrappers, `.per` strategic logic, and unresolved capabilities requiring experiment. Native feasibility predicates and other machine-provided state should not be redundantly reimplemented without a demonstrated reason.

## Repository position

The public tree remains suitable for practical development, while historical source-derived material remains controlled exposure rather than certified-clean history. Malformed or unverified native disassembly remains quarantined.

## Immediate next sequence

1. Recover structural anchors for the AIExpert rule engine.
2. Recover one persistent-fact evaluation boundary.
3. Recover one UnitAI state mutation chain.
4. Recover the rule/handler-to-action bridge.
5. Recover failure/completion feedback.
6. Construct the first runtime falsification experiment.
7. Update atomic machine facts and predictive tests from demonstrated results.

## Status rule

The 89% estimate is a working progress estimate, not a completion claim. Layer 1 reaches completion only when the predictive machine-understanding gate is satisfied and material critical paths no longer depend on unacknowledged black boxes.
