# AEGIS — Cavalry Threat Containment Vertical Slice Qualification Plan

**Date:** 2026-09-05
**Status:** QUALIFICATION PLAN — NO PRODUCTION IMPLEMENTATION
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Purpose

Use one deliberately narrow vertical slice to validate the full AEGIS semantic chain without implementing the complete bot.

## Chain

`OBSERVATION → WORLD STATE → BELIEF → SITUATION → OBJECTIVE → PLANNING → DECISION → COMMITMENT → EXECUTION → VERIFICATION → RECOVERY`

## Scenario contract

Threat:
- opposing player fields or is credibly believed to be fielding cavalry.

Required response concept:
- preserve viable response capability against cavalry.

The slice must never assume that a command, queued unit, pending object, or created object is equivalent to strategic success.

## Qualification stages

### Stage A — Observation

Establish target-build behavior for cavalry-related fact/search inputs. Record player scope, object/unit-line identity, zero/no-result behavior, and timing.

### Stage B — World publication

Publish only qualified observations. Prove invalid-before-publish and generation coherence.

### Stage C — Belief

Introduce inference only where observation is insufficient. Preserve the distinction between observed fact and inferred threat.

### Stage D — Situation

Produce a bounded cavalry-threat interpretation. Do not invent an omniscient enemy model.

### Stage E — Objective

Produce an outcome such as preserving viable anti-cavalry capability. Do not choose units or commands here.

### Stage F — Planning

Generate a bounded set of feasible response courses. Do not commit resources or issue commands.

### Stage G — Decision

Select a course or deliberately defer/refuse. Preserve objective generation and candidate identity.

### Stage H — Commitment

Accept responsibility for attempting the selected course only after current-context validation.

### Stage I — Execution

Operationalize the commitment. Test can-vs-issue, acceptance, pending, creation, availability, cancellation, and duplicate suppression.

### Stage J — Verification

Determine what actually happened. Distinguish operational completion from strategic success.

### Stage K — Recovery

If execution failed, deviated, or remains unknown, continue, retry within a bound, or reassess. Do not silently rewrite the objective or decision.

## Minimum shared gates exercised

Q-01 through Q-12 should be exercised where materially relevant. The slice is not required to prove every possible engine primitive.

## Promotion rule

The slice becomes implementation-qualified only when every consequential transition used by the slice has either:

1. direct target-build evidence; or
2. an explicit UNKNOWN/BLOCKED disposition whose consequence is safe and bounded.

## Anti-overbuild rule

Do not implement adjacent subsystems merely to make the slice look complete. Build only enough machinery to test the semantic chain and expose false assumptions.
