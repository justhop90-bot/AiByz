# AEGIS Knowledge — Institutional Memory

This directory is the project's **memory layer**. Source code is implementation; this directory preserves the reasoning that makes the implementation intelligible.

## The governing idea

AEGIS learns from historical and stock-derived code without becoming a public copy of that code.

The repository therefore preserves the transformation:

`source artifact -> observation -> evidence -> reconstructed logic -> generalized principle -> abstraction -> architecture -> implementation requirement -> validation`

The source artifact may remain outside GitHub. The knowledge extracted from it should not.

## What belongs here

### 1. Machine facts

Verified facts about the AoE2DE AI substrate: loaders, rule execution, goals, strategic numbers, timers, facts, actions, UP/native interfaces, XS boundaries, diagnostics, validation behavior, deployment constraints, and recovery semantics.

### 2. Strategic principles

General AoE2 reasoning that survives beyond one implementation: economy, production, military capability, technology, map/position, timing, information, opponent modeling, transitions, resource opportunity cost, initiative, tempo, conversion efficiency, and failure-state reasoning.

### 3. Archaeological knowledge

Reconstructed knowledge from HD/2013, Promisory, V3, and other historical implementations. This includes explicit behavior, implicit strategy, meta-knowledge about engineering choices, and historical artifacts.

### 4. Evidence exhibits

Small, isolated, attributed source snippets when necessary to explain a claim. Every exhibit must have context and an interpretation. A snippet is an **evidence exhibit**, not a replacement source tree.

### 5. Cross-layer mappings

Links between historical behavior and the AEGIS architecture: what should be preserved, generalized, rejected, or reimplemented differently.

### 6. Negative knowledge

Failed experiments, disproven hypotheses, misleading approaches, validator failures, engine workarounds, and things that appear sophisticated but are actually historical debris.

## Epistemic classes

Use explicit labels:

- `FACT` — directly established by an authoritative artifact or reproducible observation.
- `MECHANICAL_FACT` — engine/runtime behavior established by native or controlled evidence.
- `HEURISTIC` — repeated conditional behavior without proof of universal validity.
- `STRATEGIC_PRINCIPLE` — generalized decision principle supported by multiple observations or strong causal reasoning.
- `TACTICAL_PRINCIPLE` — local combat/position principle.
- `TRANSITION_PRINCIPLE` — rule governing movement between strategic states.
- `ECONOMIC_PRINCIPLE` — resource, production, opportunity-cost, or conversion principle.
- `META_KNOWLEDGE` — knowledge about how the original designers structured the decision system and why.
- `ENGINE_WORKAROUND` — behavior required by implementation constraints rather than strategy.
- `HISTORICAL_ARTIFACT` — obsolete, experimental, debug, or superseded behavior.
- `HYPOTHESIS` — plausible but not yet adequately evidenced.
- `DISPROVEN` — tested and rejected.
- `LESSON` — project-level conclusion derived from evidence and experiments.

## Evidence strength

`DIRECT > REPRODUCED > CORROBORATED > PROBABLE > PLAUSIBLE > UNCERTAIN`

Never silently upgrade an inference to a fact.

## Snippet policy

When a historical implementation materially clarifies an idea, a small excerpt may be published when appropriate. The excerpt must answer:

1. What is the source?
2. What behavior is visible?
3. What state does it read?
4. What state does it write?
5. What action or consequence follows?
6. Why does the behavior appear to exist?
7. What are the limits/counterexamples?
8. What does AEGIS learn from it?

Avoid publishing large contiguous source sections or complete historical/vendor-derived modules.

## Returnability standard

An engineer returning years later must be able to reconstruct:

- what was known,
- why it was believed,
- where the evidence came from,
- what alternative explanations existed,
- what was rejected,
- what remains uncertain,
- how the insight changed architecture,
- and what experiment should come next.

If a document cannot support that reconstruction, it is incomplete regardless of length.

## Current high-value ledgers

- `LAYER1_MACHINE_FACTS.jsonl`
- `LAYER2_STRATEGIC_AXIOMS.jsonl`
- `MACHINE_ONTOLOGY.jsonl`
- `MACHINE_INVESTIGATION_HISTORY.jsonl`
- `MACHINE_EXPERIMENT_SCHEMA.json`

The knowledge directory is intentionally expected to grow much larger than the runtime code. A mature AEGIS repository should contain substantially more explanation of the intelligence than implementation required to execute it.
