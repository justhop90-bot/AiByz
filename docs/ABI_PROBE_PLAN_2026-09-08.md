# AEGIS-BYZ — TARGET-BUILD ABI PROBE PLAN
## First Implementation Gate — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Purpose:** Establish the minimum interpreter facts required before production substrate code depends on same-pass mutation, scheduling, or command visibility.

## Gate rule

No architecture may treat same-pass state visibility as proven until a target-build probe demonstrates it. Static syntax and stock precedent are evidence, not runtime qualification.

## Probe A — Goal mutation

Question: when rule A mutates a goal, when can rule B observe the new value?

Variants:
- adjacent rule evaluation;
- timer-separated evaluation;
- jump-separated evaluation;
- repeated-cycle evaluation.

Record old value, mutation, first observed new value, and rule/control-flow position.

## Probe B — Strategic-number mutation

Question: does a strategic-number mutation become visible to another rule in the same evaluation context, and under what scheduling boundary?

Use a harmless dedicated probe SN and explicit sentinel values.

## Probe C — Command visibility

Question: after issuing a harmless command, when does object/action/order state become observable to subsequent rules?

Measure command-issued versus first engine-observed state. Do not equate command acceptance with success.

## Probe D — Timer behavior

Question: exact relationship among enable-timer, timer-triggered, repeated firing, and rule traversal.

Measure first trigger, repeat interval, interaction with jumps, and whether timer state survives control-flow transitions.

## Probe E — Jump behavior

Question: how does up-jump-rule alter rule traversal and re-entry?

Measure forward and backward jumps separately. Establish whether a backward jump causes immediate re-entry, next-pass scheduling, or another bounded behavior.

## Probe F — Rule re-entry

Question: after mutation/jump/timer activity, which rules are eligible again and when?

Use a minimal finite state machine with unmistakable state transitions. Avoid giant relative-jump structures.

## Required evidence record

For every probe:
- target build;
- runtime executable identity if available;
- script SHA-256;
- probe identifier;
- expected behavior;
- observed behavior;
- log/debug evidence;
- interpretation;
- confidence;
- architectural consequence;
- falsification condition.

## Instrumentation

Use official DE AI debugging facilities where available, including AIDEBUGGING, fe-break-point, AISCRIPTDEBUGGING, and LogSystems=AIScript. Capture exact script position/state when possible.

## Acceptance

A probe is ABI-qualified only when target-build evidence distinguishes competing interpretations. If ambiguity remains, preserve it and design the next minimal probe.

## Architectural dependency

The first civilian vertical slice depends on:

```text
Civilization State
→ Demand
→ Worker Allocation
→ Source/Dropsite Service
→ Task Command
→ Observation
→ Verification
→ Recovery
```

Only the minimum ABI needed by each link should be qualified before implementation. Research remains targeted rather than broad.
