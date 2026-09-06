# AEGIS Architecture QC — 2026-09-06

## Finding 1 — load-order symbol visibility

**Symptom:** `Line 44 carpenter. Invalid Identifier`.

**Cause:** `AEGIS-BYZ.per` loaded Carpenter before defining shared World Model symbols such as `aegis-wm-time`, `aegis-wm-population`, `aegis-wm-cavalry`, and `aegis-wm-observed-at`.

**Fix:** all shared World Model `defconst` declarations now precede every child load.

**Status:** structurally corrected; target-build runtime load proof still required.

## Finding 2 — downstream observation marker mismatch

**Symptom discovered during source audit:** Architect publication changed `aegis-wm-observed-at` from `1` to `2`, while Belief/Situation/Objectives/Planning required `observed-at == 1` for completion.

**Consequence:** even if the package loaded, the downstream state machine could fail to mark itself valid.

**Fix:** marker contract is now explicit:

```text
1 = Carpenter native acquisition complete; not published
2 = Architect publication/qualification complete
```

Belief, Situation, Objectives, and Planning consume marker `2`.

**Status:** structurally corrected.

## Finding 3 — generation ordering

**Symptom discovered during source audit:** all downstream modules were parsed before the Architect publication coordinator. Therefore Carpenter could acquire an observation, downstream rules could consume generation N, and the coordinator could then publish N+1, leaving consumers one generation behind.

**Fix:** runtime parse order is now:

```text
shared ABI
  -> Carpenter
  -> Architect bootstrap/publication/qualification
  -> Belief
  -> Situation
  -> Objectives
  -> Planning
  -> Decision
  -> Commitment
  -> Execution
  -> Verification
  -> Recovery
```

This is designed so the current published generation is consumable by the downstream state machine in the same rule-evaluation pass.

**Status:** structurally corrected; runtime N/N+1 proof still required.

## Finding 4 — goal-copy operator misuse

**Symptom discovered during a second semantic source audit:** Decision and Commitment used `up-modify-goal ... g:= <literal>` where `<literal>` was intended as a literal value, for example `g:= 1` to set a validity/stage flag.

In the AEGIS goal ABI, `g:` denotes a goal operand. A literal `1` in that position is therefore a goal reference, not the literal value one. The affected assignments could silently copy the value of goal 1 instead of writing `1`.

**Fix:** literal stage/validity writes now use `set-goal`. Goal-to-goal transfers continue to use `g:=`.

**Status:** corrected in Decision and Commitment; this pattern is now a mandatory QC rule for future modules.

## Finding 5 — unit-type-count-total

Public AI scripting evidence establishes `unit-type-count-total` as the total count including queued units, and official AoE2DE update notes document fixes to this family of counting operations. This supports the syntax and intended semantics, but does not substitute for target-build runtime qualification of the exact `up-get-fact unit-type-count-total` path used by AEGIS.

**Status:** candidate; target-build proof required.

## Finding 6 — first actuator

A disposable actuator pair now exists for a single native command:

```text
train spearman-line
```

It captures a pre-action `unit-type-count-total` baseline, issues the native command, marks Execution `ISSUED`, and has a separate candidate verification rule for a post-action count increase.

A dedicated disposable entrypoint now loads the complete AEGIS architecture followed by these two candidate modules. The candidate is deliberately not loaded by production.

**Status:** ready for controlled runtime qualification.

## Promotion rule

No source-level correction is considered fully closed until the target AoE2DE build demonstrates the intended behavior under controlled conditions. Static acceptance, public documentation, and replay evidence are supporting evidence classes, not substitutes for target-engine semantic proof.
