# AEGIS Knowledge — Institutional Memory

`knowledge/` is the project's **durable reasoning layer**. Source code is implementation; this directory preserves the reasoning, evidence, models, experiments, and lessons that make implementation intelligible.

## Governing transformation

`source artifact → observation → evidence → reconstructed logic → generalized principle → abstraction → architecture → implementation requirement → validation`

The original source artifact may remain outside GitHub. The project should preserve the useful knowledge extracted from it without turning the public repository into a copy of restricted material.

## What belongs here

### Machine knowledge

Verified or explicitly qualified knowledge about the AoE2DE AI execution substrate: loading, rule execution, state, facts, goals, strategic numbers, timers, actions, native interfaces, diagnostics, validation, deployment constraints, and failure behavior.

### Strategic knowledge

General AoE2 reasoning: economy, production, military capability, technology, map and position, timing, information, opponent modeling, transitions, opportunity cost, initiative, tempo, conversion efficiency, and failure recovery.

### Archaeological knowledge

Reconstructed knowledge from historical AI implementations. This includes visible behavior, implicit principles, engineering intent, and lessons from obsolete approaches.

### Replay knowledge

Empirical observations and adjudication rules derived from replay data. Replay records are evidence about observed game history, not a guaranteed window into hidden native state.

### Negative knowledge

Failed experiments, disproven hypotheses, misleading approaches, validator failures, engine workarounds, and historical behavior that should **not** be carried forward.

## Epistemic classes

- `FACT` — directly established by authoritative evidence.
- `MECHANICAL_FACT` — runtime/native behavior established by strong evidence.
- `HEURISTIC` — repeated conditional behavior without universal proof.
- `STRATEGIC_PRINCIPLE` — generalized decision principle.
- `TACTICAL_PRINCIPLE` — local combat/position principle.
- `TRANSITION_PRINCIPLE` — rule governing strategic state changes.
- `ECONOMIC_PRINCIPLE` — resource, production, opportunity-cost, or conversion principle.
- `META_KNOWLEDGE` — knowledge about how an earlier system was designed and why.
- `ENGINE_WORKAROUND` — behavior imposed by machine constraints.
- `HISTORICAL_ARTIFACT` — obsolete, experimental, debug, or superseded material.
- `HYPOTHESIS` — plausible but insufficiently demonstrated explanation.
- `DISPROVEN` — tested and rejected.
- `LESSON` — project-level conclusion derived from evidence.

## Evidence strength

`DIRECT > REPRODUCED > CORROBORATED > PROBABLE > PLAUSIBLE > UNCERTAIN`

Evidence strength and epistemic class are separate dimensions. A hypothesis can be well supported without becoming a fact; a historical fact can be well established without becoming current architecture.

## Claim-record requirements

A useful knowledge record should answer:

1. What is being claimed?
2. What evidence supports it?
3. What exactly was observed?
4. What is interpretation rather than observation?
5. What alternative explanations exist?
6. What would falsify the claim?
7. What practical engineering consequence follows?
8. What should be tested next?

## Important distinctions

- A symbol name is vocabulary, not semantics.
- A declaration is an interface, not proof of implementation.
- A replay field is an observation, not necessarily complete internal state.
- A command being issued is not proof of execution success.
- Execution success is not proof of strategic success.
- Absence is not proof of destruction.
- A failed search is not proof that a mechanism is absent.
- Repetition of an inference does not upgrade it to fact.

## Current high-value ledgers

- `LAYER1_MACHINE_FACTS.jsonl` — atomic machine facts.
- `MACHINE_ONTOLOGY.jsonl` — machine concepts and relationships.
- `MACHINE_INVESTIGATION_HISTORY.jsonl` — chronological investigation record.
- `MACHINE_EXPERIMENT_SCHEMA.json` — experiment structure.
- `LAYER2_STRATEGIC_AXIOMS.jsonl` — strategic axioms for later layers.
- `knowledge/replay/` — replay event, temporal, lifecycle, and production evidence.

## Six-month recovery rule

If you return after forgetting the project, do not start by reading implementation code. Start at `../RESEARCH_INDEX.md`, then the current status and evidence matrix, then the machine monograph, then the investigation/QC records, and finally the atomic ledgers.

The repository should make it possible to reconstruct **what we know, why we know it, what we do not know, and what to do next** without conversational memory.
