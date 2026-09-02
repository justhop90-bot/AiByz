# Layer 1 — AoE2DE AI Machine Knowledge

## Purpose

This document is the durable operational contract for designing AI against the Age of Empires II: Definitive Edition rule-script machine. It deliberately records what the project has established, the evidence classes used to establish it, and the boundary between demonstrated behavior and unresolved reverse-engineering questions.

## Closure standard

Layer 1 is operationally complete when the engineering team can design, validate, deploy, observe, and recover an AI implementation without relying on unsupported assumptions about the script machine. It does **not** mean every native instruction or proprietary implementation detail has been reverse engineered.

## Runtime substrate

The relevant AI surface consists of `.ai` loading/bootstrap behavior and `.per` rule scripts. The rule system is stateful: script predicates observe engine state; goals, strategic numbers, and timers retain decision state; actions mutate engine-visible state or request game actions; subsequent rule evaluation observes the consequences.

The practical model is therefore a closed feedback loop:

`engine state -> sensors/predicates -> persistent state -> rule scheduling -> decisions/actions -> changed engine state -> next evaluation`.

## Rule scheduling evidence

Native extraction identified embedded scheduler vocabulary including `mCurrentRuleID`, `mNextSortedRuleIndex`, `xsEnableRule`, `xsEnableRuleGroup`, `xsDisableRule`, `xsDisableRuleGroup`, `xsSetRulePriority`, `xsSetRulePrioritySelf`, and diagnostics for invalid rule IDs, rule execution failure, and rule interval/priority modifications. These strings establish native vocabulary and diagnostic surfaces; they are not, by themselves, proof of every scheduler invariant.

The engineering consequence is that rule priority, enablement, intervals, and execution failure must be treated as first-class machine concepts rather than assumed to be simple source-order evaluation.

## State substrate

Goals are persistent script state. Strategic numbers are persistent engine/script control variables. Timers provide temporal hysteresis and state persistence across evaluations. Facts provide observations and queries. The project has repeatedly observed designs where the AI uses a goal or strategic number as a state-machine latch, then modifies it when a transition condition occurs.

This means a robust architecture should distinguish:

1. observation;
2. belief/state storage;
3. intent/decision;
4. authorized action;
5. execution;
6. verification;
7. recovery.

## UP/native interface evidence

The project has observed UP-facing fact/action patterns and has classified them according to evidence strength. A critical example is the `up-get-focus-fact` plus `unit-type-count` sensor pattern. The `knight-line` identifier is an abstract unit-line identifier, not a civilization class identifier. It is semantically different from a concrete unit ID such as `knight` and from class identifiers. Validators may have narrower corpus expectations than the engine itself; validator behavior must therefore be recorded separately from runtime semantics.

The project rule is: never alter a semantically correct engine-level abstraction merely to satisfy an unverified validator assumption. Instead, establish whether the validator corpus, local constants, or engine vocabulary is authoritative for the specific deployment path.

## XS boundary

XS is treated as a capability surface, not as blanket permission. Only specifically qualified XS capabilities, for specifically approved purposes, on specifically evidenced builds, may enter the AEGIS runtime. Native extraction demonstrated rule enable/disable, priority, and interval-related XS vocabulary. Any additional XS behavior requires evidence before architectural dependence.

## Loader and execution boundary

The AI must be considered a loaded program with a finite consumable interface. Source correctness is insufficient: the `.ai` loader, included `.per` dependency graph, parser/validator, rule scheduler, action execution, and runtime observation chain all form part of the deployment contract.

Therefore every runtime candidate must have:

- resolved load graph;
- syntax/validation evidence;
- version provenance;
- reproducible installation path;
- rollback artifact;
- runtime observation evidence.

## Error and recovery semantics

Native diagnostics identified invalid rule IDs, failed rule execution, and invalid rule interval/priority modifications. These are important because a production AI cannot assume every requested action is accepted. Execution failure is an observable state requiring policy.

The preferred AEGIS architecture therefore treats command execution as transactional in the conceptual sense:

`intent -> authorization -> command -> observation -> acknowledgement -> recovery on mismatch`.

## Evidence hierarchy

The project uses the following practical evidence hierarchy:

1. reproducible runtime behavior;
2. verified native call graph / analyzed function behavior;
3. native signatures and cross-references;
4. native diagnostic/error paths;
5. script usage confirmed on the target build;
6. embedded strings and symbol vocabulary;
7. comments/documentation;
8. inference/hypothesis.

A lower evidence class must not silently override a higher one.

## Ghidra status

The final Ghidra analysis pass is treated as evidence enrichment. It may strengthen, weaken, or invalidate individual claims in this contract. It does not reopen Layer 1 wholesale unless a critical exit-gate assumption is falsified.

## Layer 1 exit principle

The purpose of Layer 1 is safe engineering leverage, not exhaustive archaeology. Once the machine contract is sufficiently reliable to constrain architecture, the project moves upward to strategy while continuing targeted machine research in parallel.

## Non-negotiable architectural consequence

Layer 2 may propose any strategically desirable state transition, but Layer 4 implementation may only realize transitions that can be represented and executed through the Layer 1 machine contract.
