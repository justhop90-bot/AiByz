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

The latest native pass established an independent function-boundary layer from the executable's PE `.pdata`: 166,730 valid runtime-function ranges were recovered for the controlled build. This allows native archaeology to proceed from verified function geometry even when broad Ghidra auto-analysis is incomplete or slow.

A correctly section-mapped metadata-region pointer was also demonstrated to target a `.pdata`-recognized function start. Direct disassembly showed that target function to be cleanup/destructor-like rather than an implementation of the adjacent XS API. The association is therefore explicitly rejected. This is a useful methodological result: pointer proximity and valid function-start membership are necessary but insufficient for semantic ownership.

The controlled Ghidra workspace exists and remains under a long-running analysis process. It must not be treated as a completed, clean analysis baseline until the process terminates and the resulting project is independently validated.

No new AIExpert or UnitAI implementation call edge was promoted in this pass. The working completion estimate therefore remains 89%.

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

The `.pdata` section now provides an additional independent function-boundary mechanism: its 12-byte runtime-function records can be mapped to executable virtual ranges. This is now the preferred structural substrate for targeted native archaeology.

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

Native vocabulary establishes rule loading, constant/fact/action definition, indexed rule elements, debug metadata, persistent-fact evaluation, rule navigation, breakpoints, parser/error categories, and an explicit AI-fact initialization boundary. The exact function ownership, scheduler comparator, state mutation sequence, and handler bridge remain open.

The next native search must use verified `.pdata` function geometry rather than widening string inventories.

## Fact semantic model

The native corpus supports a useful taxonomy of direct state, derived state, feasibility predicates, relational player scopes, event/timer state, and environment/game-configuration state. This is an engineering classification, not a recovered internal class hierarchy.

A key predictive question is fact freshness: whether individual fact classes are evaluated live, on a scheduler cadence, from persistent caches, or through class-specific invalidation.

## UnitAI model

Native vocabulary continues to support separate order, action, target, notification, search, retry, retargeting, and completion/failure concepts. The next promotion target is a concrete native mutation chain showing read → condition/transition → write → downstream consumer.

## Practical architecture implication

ByzBot should classify machine capabilities into trusted observations, trusted native control surfaces, compensating wrappers, `.per` strategic logic, and unresolved capabilities requiring experiment. Native feasibility predicates and other machine-provided state should not be redundantly reimplemented without a demonstrated reason.

The architecture should keep strategic desirability separate from machine feasibility: strategy decides what is desirable; native feasibility determines whether the requested operation is currently executable under engine semantics; execution must then be reconciled against observed results.

## Repository position

The public tree remains suitable for practical development, while historical source-derived material remains controlled exposure rather than certified-clean history. Malformed or unverified native disassembly remains quarantined.

Every substantive pass is expected to leave durable research memory in GitHub when the evidence supports a new record. Unverified findings must be recorded as hypotheses or negative results rather than omitted.

## Immediate next sequence

1. Use `.pdata` function geometry to partition AI-related executable regions into verified functions.
2. Recover the first defensible AIExpert state mutation.
3. Recover the first defensible UnitAI `CurrentOrder`/`CurrentAction` mutation.
4. Recover the rule/handler-to-action bridge.
5. Recover failure/completion feedback.
6. Construct the first runtime falsification experiment, beginning with fact freshness if practical.
7. Update atomic machine facts and predictive tests from demonstrated results.

## Status rule

The 89% estimate is a working progress estimate, not a completion claim. Layer 1 reaches completion only when the predictive machine-understanding gate is satisfied and material critical paths no longer depend on unacknowledged black boxes.
