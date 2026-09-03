# Layer 1 — AoE2DE AI Machine Knowledge — Final Investigation Baseline

## Purpose

This document is the durable operational model for designing AI against the Age of Empires II: Definitive Edition rule-script machine. It records what the project established, how that knowledge was established, and where the boundary between demonstrated behavior and unresolved native questions lies.

## Final Layer 1 position

**Working completion position: 89%. Investigation phase: CLOSED / HANDOFF. Completion gate: NOT SATISFIED.**

The remaining work is implementation-level causal closure rather than generic vocabulary collection. See `LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md` for the authoritative final investigation record.

## Current completion standard

The project uses a **predictive machine-understanding** standard. Layer 1 is not complete merely because scripting vocabulary, interface names, or high-level execution concepts are known.

For every material machine path, the desired model is:

`precondition -> trigger -> dispatch -> processing -> state transition -> postcondition -> next observable consequence`

Where evidence is insufficient to make that chain predictive, uncertainty remains visible.

## Runtime substrate

The relevant AI surface consists of `.ai` loading/bootstrap behavior and `.per` rule scripts. The rule system is stateful: script predicates observe engine state; goals, strategic numbers, and timers retain decision state; actions mutate engine-visible state or request game actions; subsequent evaluation observes consequences.

The practical model is a feedback loop:

`engine state -> sensors/predicates -> persistent state -> rule scheduling -> decisions/actions -> changed engine state -> next evaluation`.

This is a model of the observed execution surface, not a claim that every internal scheduler detail has been recovered.

## Rule scheduling

Native extraction identified scheduler vocabulary including `mCurrentRuleID`, `mNextSortedRuleIndex`, enable/disable controls, priority controls, rule groups, and diagnostics associated with invalid rule IDs and rule execution or interval/priority changes.

These findings establish a native scheduling vocabulary and diagnostic surface. They do not prove every scheduler invariant. The exact comparator, interval mathematics, rebuild triggers, fairness, and starvation behavior remain open implementation questions.

The engineering consequence is that rule priority, enablement, intervals, and execution failure must be treated as first-class machine concepts rather than assumed to be simple source-order evaluation.

## State substrate

Goals are persistent script state. Strategic numbers are persistent engine/script control variables. Timers provide temporal persistence and hysteresis. Facts provide observations and queries. The native corpus additionally establishes an explicit `Init AI Facts` boundary and a distinct persistent-fact evaluation diagnostic phase.

The highest-value unresolved state question is fact freshness: whether fact classes are live, scheduler-refreshed, cached until invalidated, or class-specific.

A robust architecture should distinguish:

1. observation;
2. belief/state storage;
3. intent/decision;
4. authorization;
5. command execution;
6. verification;
7. recovery.

## UP/native interface evidence

The project has identified UP-facing fact/action patterns and classified them by evidence strength. One important example is `up-get-focus-fact` plus `unit-type-count`. The identifier `knight-line` is an abstract unit-line identifier rather than a civilization class identifier or a concrete unit ID.

Validator behavior and engine behavior are separate evidence domains. A validator's accepted corpus is not automatically proof of native semantics, and native vocabulary is not automatically proof that a particular expression is accepted by a particular validator profile.

The engineering rule is to establish the actual deployment contract before changing a semantically meaningful abstraction merely to satisfy a narrower validation assumption.

## Loader and execution boundary

The AI should be treated as a loaded program with a finite consumable interface. Source correctness is insufficient: `.ai` loading, included `.per` dependency graph, parser/validator, rule scheduler, command execution, and runtime observation chain all form part of the deployment contract.

Every runtime candidate should have resolved load graph, syntax/validation evidence, target-version provenance, reproducible installation evidence, rollback artifact, and runtime observation evidence.

## Error and recovery semantics

Native diagnostics identify invalid rule IDs and failures associated with rule execution, interval/priority changes, action failure, invalidation, search requirements, and pathing. These are important because a production AI cannot assume every requested operation is accepted or completed.

The preferred AEGIS architecture therefore treats command execution transactionally in the conceptual sense:

`intent -> authorization -> command -> observation -> acknowledgement -> recovery on mismatch`.

This is an architectural safety model, not a claim that the engine itself implements ACID-style transactions.

## Object identity and lifecycle

Object identity remains a bounded native research frontier. Native signature evidence identifies interfaces for unit/object object-ID and copy-ID retrieval, type/class queries, validity/availability checks, and garrison relationships. Native diagnostic/source strings also expose concepts such as `obj->id` and `uniqueID`.

These findings establish that the relevant concepts exist in the native evidence surface. They do not prove complete equality/relationship topology among unit IDs, object IDs, copy IDs, ownership, type/class, creation, transformation, garrison, and removal.

Until required topology is demonstrated, strategic architecture must not rely on undocumented identity assumptions.

## Replay boundary

Replay parsing is an observation instrument. It can establish what was recorded and what a parser can decode, but it does not automatically expose hidden native state or prove the semantics of every numeric field.

Object references, action payloads, sequence coordinates, lifecycle events, and production completion require explicit adjudication. A parser guess is evidence about the parser, not automatically a fact about the engine.

## Native function geometry

The controlled PE `.pdata` provides an independent function-coordinate layer: 166,741 physical 12-byte slots were inspected; 166,730 contain non-zero runtime-function records and 11 are trailing zero padding. Valid starts are unique and monotonically ordered, with no interval overlaps. Aggregate valid interval coverage is 45,879,189 bytes, approximately 88.88% of `.text` raw size.

This is structural evidence, not a semantic function inventory. Its practical value is that native archaeology can begin from mechanically bounded function ranges and then inspect instruction/data flow without trusting guessed function ownership from strings.

## CodeView/PDB boundary

The executable embeds CodeView `RSDS` data identifying PDB GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`, age `1`, and a path ending in `AoE2DE_s.pdb`. No matching local PDB was established. A future PDB is evidence only after GUID/age authentication against the controlled executable.

## Direct-reference negative evidence

Correct section-aware mapping plus full `.text` Capstone scanning found zero RIP-relative references to seven selected AI diagnostic/source anchors, and executable-wide exact 64-bit-pointer scanning found zero occurrences. This is bounded negative evidence for those representations only. It does not prove absence of the AI subsystem or exclude indirect/indexed/encoded/table-mediated references.

## Metadata false-positive control

A correctly mapped metadata-area pointer reached a `.pdata`-recognized function at `0x1417FF3E0`. Direct disassembly showed cleanup/destructor-like behavior, so the association was rejected as an XS API implementation. The permanent rule is:

`metadata proximity + valid pointer + valid function boundary != semantic ownership`

Semantic ownership requires caller/callee, data-flow, state-effect, or equivalent independent evidence.

## Ghidra boundary

Historical Pass33 remains preserved. It contains genuine analysis activity but substantial function-body repair noise. The separate controlled headless analysis imported and saved the exact executable but timed out at 1800 seconds during `Disassemble Entry Points` with a `CreateThunkFunctionCmd` / `body must contain the entry point` error. Broad analysis is therefore index generation, not automatic semantic proof.

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

## Final investigation frontier

The remaining 11% is concentrated in: verified rule-loader/parser boundary; rule-representation ownership/mutation; persistent-fact result mutation and freshness; scheduler comparator/interval transitions; rule/handler-to-native-action bridge; `CurrentOrder -> CurrentAction`; action failure/invalidation/completion propagation; required object-identity lifecycle edges; and one predictive end-to-end `.per` path.

These are implementation-closure targets. Do not restart broad vocabulary collection merely because these edges remain open.

## Non-negotiable architectural consequence

Layer 2 may propose strategically desirable state transitions, but Layer 4 implementation may only realize transitions that can be represented, authorized, executed, observed, and recovered through the demonstrated Layer 1 machine contract. Where unresolved behavior must be used, isolate it behind an explicitly replaceable interface and label the assumption.
