# Layer 1 — AoE2DE AI Machine Knowledge

## Purpose

This document is the durable operational model for designing AI against the Age of Empires II: Definitive Edition rule-script machine. It records what the project has established, how that knowledge was established, and where the boundary between demonstrated behavior and unresolved native questions lies.

## Current completion standard

The project is currently using a **predictive machine-understanding** standard. Layer 1 is not considered complete merely because the scripting vocabulary, interface names, or high-level execution concepts are known.

For every material machine path, the desired model is:

`precondition → trigger → dispatch → processing → state transition → postcondition → next observable consequence`

Where the evidence is insufficient to make that chain predictive, the uncertainty must remain visible.

## Runtime substrate

The relevant AI surface consists of `.ai` loading/bootstrap behavior and `.per` rule scripts. The rule system is stateful: script predicates observe engine state; goals, strategic numbers, and timers retain decision state; actions mutate engine-visible state or request game actions; subsequent evaluation observes consequences.

The practical model is therefore a feedback loop:

`engine state → sensors/predicates → persistent state → rule scheduling → decisions/actions → changed engine state → next evaluation`.

This is a model of the observed execution surface, not a claim that every internal scheduler detail has already been recovered.

## Rule scheduling

Native extraction identified scheduler vocabulary including `mCurrentRuleID`, `mNextSortedRuleIndex`, `xsEnableRule`, `xsEnableRuleGroup`, `xsDisableRule`, `xsDisableRuleGroup`, `xsSetRulePriority`, `xsSetRulePrioritySelf`, and diagnostics associated with invalid rule IDs and rule execution or interval/priority changes.

These findings establish a native scheduling vocabulary and diagnostic surface. They do **not**, by themselves, prove every scheduler invariant. The remaining work is to connect the vocabulary to implementation behavior through references, analyzed functions, and runtime experiments.

The engineering consequence is that rule priority, enablement, intervals, and execution failure must be treated as first-class machine concepts rather than assumed to be simple source-order evaluation.

## State substrate

Goals are persistent script state. Strategic numbers are persistent engine/script control variables. Timers provide temporal persistence and hysteresis. Facts provide observations and queries. Historical AI designs repeatedly use persistent variables as state-machine latches whose values change when transition conditions occur.

A robust architecture should therefore distinguish:

1. observation;
2. belief/state storage;
3. intent/decision;
4. authorization;
5. command execution;
6. verification;
7. recovery.

## UP/native interface evidence

The project has identified UP-facing fact/action patterns and classified them by evidence strength. One important example is the `up-get-focus-fact` plus `unit-type-count` sensor pattern. The identifier `knight-line` is an abstract unit-line identifier rather than a civilization class identifier or a concrete unit ID.

Validator behavior and engine behavior are separate evidence domains. A validator's accepted corpus is not automatically proof of native semantics, and native vocabulary is not automatically proof that a particular script expression is accepted by a particular validator profile.

The engineering rule is to establish the actual deployment contract before changing a semantically meaningful abstraction merely to satisfy a narrower validation assumption.

## Loader and execution boundary

The AI should be treated as a loaded program with a finite consumable interface. Source correctness is insufficient: the `.ai` loader, included `.per` dependency graph, parser/validator, rule scheduler, command execution, and runtime observation chain all form part of the deployment contract.

Every runtime candidate should have:

- resolved load graph;
- syntax/validation evidence;
- target-version provenance;
- reproducible installation path;
- rollback artifact;
- runtime observation evidence.

## Error and recovery semantics

Native diagnostics identify invalid rule IDs and failures associated with rule execution and interval/priority changes. These are important because a production AI cannot assume every requested operation is accepted.

The preferred AEGIS architecture therefore treats command execution transactionally in the conceptual sense:

`intent → authorization → command → observation → acknowledgement → recovery on mismatch`.

This is an architectural safety model, not a claim that the engine itself implements ACID-style transactions.

## Object identity and lifecycle

Object identity is a current high-priority native research boundary. Native signature evidence identifies interfaces for unit/object object-ID and copy-ID retrieval, type/class queries, validity/availability checks, and garrison relationships. Native diagnostic/source strings also expose concepts such as `obj->id` and `uniqueID`.

These findings establish that the relevant concepts exist in the native evidence surface. They do not yet prove the complete equality/relationship topology among unit IDs, object IDs, copy IDs, ownership, type/class, creation, transformation, garrison, and removal.

Until that topology is demonstrated, strategic architecture must not rely on undocumented identity assumptions.

## Replay boundary

Replay parsing is an observation instrument. It can establish what was recorded and what a parser can decode, but it does not automatically expose hidden native state or prove the semantics of every numeric field.

In particular, object references, action payloads, sequence coordinates, lifecycle events, and production completion require explicit adjudication. A parser guess is evidence about the parser, not automatically a fact about the engine.

## Evidence hierarchy

The practical hierarchy is:

1. reproducible runtime behavior;
2. verified native implementation/call-path behavior;
3. native references and analyzed functions;
4. native diagnostic/error paths;
5. target-build script behavior;
6. embedded strings and vocabulary;
7. comments/documentation;
8. inference/hypothesis.

Evidence levels should never be silently collapsed.

## Layer 1 research status

The project has established a substantial machine evidence surface and a rigorous methodology, but the predictive completion gate remains open. Native research continues specifically where it can convert vocabulary-level evidence into implementation-level causal understanding.

The immediate frontier is instruction-level reference recovery into the embedded API signature region and end-to-end tracing of representative object-identity APIs.

## Non-negotiable architectural consequence

Layer 2 may propose strategically desirable state transitions, but Layer 4 implementation may only realize transitions that can be represented, authorized, executed, observed, and recovered through the demonstrated Layer 1 machine contract.
