# AEGIS Knowledge Preservation Standard

## Mission

AiByz is the project's durable memory. The repository must preserve not only executable source but the reasoning, evidence, experiments, failures, constraints, and methodological discoveries required for independent continuation.

## Required record

A durable knowledge record should answer: **what was observed, where it came from, what it means, how strongly it is supported, what could falsify it, and what engineering consequence follows**.

## Provenance

Every research artifact should preserve source identity, source version/build, acquisition date where known, content hash where practical, and relationship to canonical/experimental material. Derived documents should identify the evidence from which they were derived.

## Epistemic status

Use explicit statuses: `CONFIRMED`, `PROBABLE`, `PLAUSIBLE`, `UNCERTAIN`, `OBSOLETE`, `ENGINE_SPECIFIC`, `DISPROVEN`.

Never upgrade a hypothesis merely because it is convenient for implementation.

## Knowledge taxonomy

`FACT` — externally or mechanically established statement.

`MECHANICAL_FACT` — property of the game/engine machine.

`HEURISTIC` — observed decision rule that may have exceptions.

`STRATEGIC_PRINCIPLE` — generalized competitive principle.

`TACTICAL_PRINCIPLE` — local battlefield principle.

`TRANSITION_PRINCIPLE` — principle governing movement between strategic states.

`ECONOMIC_PRINCIPLE` — resource/opportunity-cost principle.

`FAILURE_HEURISTIC` — recognizable failure signature or recovery rule.

`ENGINE_WORKAROUND` — behavior required because of machine constraints.

`HISTORICAL_ARTIFACT` — evidence of prior design intent, not necessarily current truth.

`BUG_COMPENSATION` — behavior created to compensate for a defect or limitation.

`HYPOTHESIS` — proposed explanation awaiting evidence.

`LESSON` — validated project-level learning from an experiment or outcome.

## Source separation

Maintain explicit separation between source-derived observation, model inference, and outside research. A derived interpretation must never be written as though the original source literally stated it.

## Cross-validation

Important strategic or machine claims should be cross-validated against independent evidence when available: runtime tests, native analysis, replay evidence, HD archaeology, V3 behavior, canonical Porphyra behavior, or other controlled experiments.

## Implementation traceability

A major implementation should be traceable backward to the knowledge records that justify it and forward to the machine interfaces that execute it. This prevents strategy from becoming disconnected from engine reality.

## Reproducibility

A future engineer should be able to reproduce important observations from preserved commands, scripts, inputs, versions, hashes, and expected outputs. If exact reproduction is impossible, document why.

## Failure preservation

Failures are first-class knowledge. Preserve rejected approaches, validator errors, runtime failures, false hypotheses, and the evidence that caused them to be rejected. Do not clean history by erasing useful failure information.

## Security and publication

Do not publish proprietary AoE2 binaries, stock AI source, credentials, private data, or other restricted material merely because the repository is the project's memory. Preserve hashes, manifests, derived analyses, and user-owned artifacts where publication is appropriate; retain restricted source locally unless separately authorized.

## Continuation test

The repository passes its knowledge-preservation standard only when a competent engineer who did not participate in the original session can determine:

- what the project is trying to build;
- what the machine permits;
- what the team learned about strategy;
- which claims are facts versus hypotheses;
- why major architectural decisions were made;
- what failed and why;
- what remains unknown;
- where the next experiment or implementation should begin.
