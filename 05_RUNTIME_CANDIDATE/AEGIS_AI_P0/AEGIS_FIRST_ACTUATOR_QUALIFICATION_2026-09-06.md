# AEGIS First Actuator Qualification — 2026-09-06

## Objective

Qualify the first real Execution edge for the Cavalry Threat Containment vertical slice.

The selected command is the native `train spearman-line` action. This is a deliberately small actuator because the Byzantines receive a 25% Spearman-line cost reduction, and the command has a direct native precondition (`can-train`) plus an observable total-count boundary.

## Contract

```text
CURRENT COMMITMENT
    type = CONTAIN
        |
CURRENT EXECUTION
    generation = current WM generation
    stage = OPERATIONALIZED
        |
    can-train spearman-line
    unit-type-count-total spearman-line < 1
        |
    native action: train spearman-line
        |
EXECUTION = ISSUED
        |
observe unit-type-count-total spearman-line
        |
count > pre-action baseline
        |
EXECUTION = EVIDENCE
```

## Evidence semantics

`ISSUED` means the native `train` action executed from the AEGIS rule. It does not mean accepted, created, deployed, or effective.

The first verification boundary is intentionally weaker: an increase in `unit-type-count-total spearman-line` above the captured baseline establishes a training-queue/count effect. `unit-type-count-total` includes queued units, so this observation must not be promoted to battlefield creation without an independent world-state observation.

## Candidate artifacts

- `AegisProm/Aegis-actuator-train-candidate.per`
- `AegisProm/Aegis-verification-train-candidate.per`

Neither is loaded by the production entrypoint yet.

## Qualification procedure

1. Preserve untouched stock `/ai` as control.
2. Deploy the exact AEGIS candidate package to a disposable runtime location.
3. Use the same target build: AoE2DE `101.103.48987.0`, Steam BuildID `24094652`.
4. Start a minimal controlled Byzantine-vs-cavalry scenario with a stable barracks and sufficient resources, or otherwise arrange a reproducible `can-train spearman-line` state.
5. Load the candidate actuator and verification modules in the documented order.
6. Record raw AI diagnostics, process lifecycle, replay, and independent world-state evidence where available.
7. Require the observed sequence `AUTHORIZED -> OPERATIONALIZED -> ISSUED -> COUNT EFFECT`.
8. If any boundary is not observable, record `UNKNOWN`; never infer it.
9. Repeat the same experiment with stock AI as the control and without the candidate actuator.
10. Freeze the source/package hash only after repeatable target-build evidence exists.

## Promotion gate

The candidate is not production-qualified merely because it parses or loads. Promotion requires target-build runtime evidence of the native action, the count-effect observation, and clean separation from the stock control.
