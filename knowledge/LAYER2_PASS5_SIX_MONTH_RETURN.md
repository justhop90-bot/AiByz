# Layer 2 Pass 5 — Six-Month Return and Resumption Index

## Purpose

This document is a restart protocol, not a summary. A future researcher should be able to return after six months and resume the project without reconstructing the reasoning from memory.

## Where we are

Layer 2 has completed five conceptual stages:

1. **Historical extraction** — recovered strategic control events from HD/2013 source.
2. **Explicit reconstruction** — mapped state reads/writes/actions and control surfaces.
3. **Implicit/meta reconstruction** — inferred recurring strategic and engineering principles while preserving uncertainty.
4. **Generalization** — converted historical implementation patterns into an implementation-independent AoE2 strategic ontology.
5. **Cross-validation** — challenged the generalized claims using independent rationale, boundary conditions, counterexamples, measurement requirements, and falsifiers.

The project is now crossing from **ontology construction** into **empirical strategic science**.

## Canonical reading order

Read these in order:

1. `knowledge/KNOWLEDGE_PRESERVATION_STANDARD.md`
2. `knowledge/LAYER2_STRATEGIC_MODEL.md`
3. `knowledge/LAYER2_GENERAL_AOE2_ONTOLOGY_PASS4.md`
4. `knowledge/LAYER2_PASS4_QUALITY_AUDIT_AND_DEEPENING.md`
5. `knowledge/LAYER2_GENERALIZATION_LEDGER_PASS4.jsonl`
6. `knowledge/LAYER2_GENERAL_AOE2_ONTOLOGY.jsonl`
7. `knowledge/LAYER2_STRATEGIC_AXIOMS.jsonl`
8. `knowledge/LAYER2_PASS5_CROSS_VALIDATION.md`
9. `knowledge/LAYER2_PASS5_CROSS_VALIDATION_MATRIX.jsonl`
10. `03_HD_ARCHAEOLOGY/` when a historical claim needs source tracing.

## What changed in Pass 5

Pass 5 did not simply confirm Pass 4. It introduced stricter epistemic boundaries.

The central correction is:

`claim = relationship + conditions + objective + horizon + uncertainty boundary`

A claim that lacks its domain of validity is incomplete.

## Current strongest strategic model

AoE2 strategic control can currently be represented as:

```text
WORLD
  ↓
OBSERVATION
  ↓
STATE ESTIMATION
  ↓
BELIEF / HYPOTHESES
  ↓
OBJECTIVE PRIORITY
  ↓
FEASIBILITY SET
  ↓
TRANSITION GENERATION
  ↓
BEST-ALTERNATIVE / COUNTERFACTUAL TEST
  ↓
ROBUST EVALUATION
  ↓
COMMITMENT
  ↓
AUTHORIZED EXECUTION
  ↓
VERIFICATION
  ↓
OUTCOME / FAILURE SIGNATURE
  ↓
DIAGNOSTIC BELIEF UPDATE
  ↓
WORLD
```

This is a research model, not yet a runtime specification.

## Concepts added or materially strengthened

- feasibility set;
- best feasible alternative;
- regret/opportunity cost;
- state value vs transition value;
- option value;
- reversibility;
- substitutable capability paths;
- diagnosticity of evidence;
- robustness under hidden-state uncertainty;
- action-set restriction as a measurable form of initiative/denial;
- dependency graphs for capabilities and transitions;
- explicit decision horizons;
- conditional rather than universal strategic laws;
- distinction between causal and correlational evidence;
- non-additive strategic interactions.

## What is currently supported

The following broad claims are currently classified as probable or context-dependent rather than universal axioms:

- strategy is adaptive state transformation;
- capability is a stronger strategic abstraction than raw unit count at planning level;
- resource value depends on alternative conversions and timing;
- production is a capability pipeline;
- transitions are strategically important;
- opponent models benefit from alternatives and uncertainty under partial observability;
- enemy commitments can impose multiple forms of tax;
- information has decision-dependent value;
- initiative changes response demand;
- consequential commitments need failure/recovery semantics;
- epistemic state should be separated from control state;
- position can modify capability value;
- commitments consume option value but may rationally sacrifice it for irreversible gain;
- temporal hysteresis stabilizes multiscale reactive control;
- retreat can preserve strategic value but can also destroy objectives;
- transition-aware counterplay is generally stronger at strategic horizon;
- demand-responsive resource allocation is preferable to static ratios when state changes materially;
- diagnostic failures should update beliefs;
- historical state compression is a useful meta-model;
- timers/resets must be interpreted per subsystem rather than universally.

## What remains explicitly unproven

Do not silently treat these as calibrated facts:

- exact capability weights;
- exact resource shadow prices;
- universal conversion-tax coefficients;
- universal timing-window durations;
- exact map-control valuation;
- uncertainty penalties;
- optimal scouting thresholds;
- combat-exchange coefficients;
- production-throughput coefficients;
- universal retreat thresholds;
- universal initiative measurements;
- Byzantine-specific strategic weights.

## Immediate next empirical program

The next stage should create a **decision-opportunity corpus**.

Do not start by collecting only wins/losses.

For each strategically meaningful decision point record:

- timestamp;
- actor;
- observable state;
- hidden-state uncertainty;
- belief hypotheses;
- objective;
- feasible alternatives;
- selected transition;
- commitment;
- predicted result;
- actual result;
- opponent response;
- resource delta;
- capability delta;
- production delta;
- position delta;
- timing delta;
- information gained/lost;
- failure signature;
- recovery;
- downstream state.

The unit of analysis remains the **decision/control event**.

## How to use the uploaded stock AiBuilder material

`AiBuilder.per` is useful as tooling/context evidence because it demonstrates configurable phase-based parameters, gatherer allocations, caps, infrastructure limits, prerequisites, and other exposed knobs. It must not be treated as AEGIS source code or copied into the project wholesale.

The correct use is:

`stock tooling observation -> explain mechanism/purpose -> independent abstraction -> validate`

Never:

`stock tooling -> copy implementation -> call it architecture`.

## Provenance boundary

HD/2013 is the historical strategic evidence source.

AiBuilder is stock tooling context.

Promisory and failed user-derived projects are not strategic evidence for AEGIS.

Public repository artifacts should preserve knowledge about historical code while avoiding large contiguous reproduction of stock/proprietary source.

## Resumption rule

If returning after six months, do not immediately code.

First:

1. read the preservation standard;
2. read the strategic model;
3. read the Pass-4 ontology;
4. read the Pass-5 adjudication;
5. inspect the cross-validation matrix;
6. identify claims lacking empirical evidence;
7. choose the highest-value falsification experiment;
8. only then design runtime state or implementation.

## Final six-month test

A future engineer is considered successfully reoriented only when they can explain, without external memory:

- what the historical AI actually did;
- what we inferred from it;
- what we generalized;
- what we tested;
- what survived;
- what was weakened;
- what remains uncertain;
- what observations would falsify the surviving claims;
- how those claims become measurable runtime state;
- why the next work is empirical rather than another layer of unsupported abstraction.

If that cannot be reconstructed from the repository, the institutional-memory system has failed.
