# AEGIS — Planning Five-Pass Closure

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Status:** CLOSED — ARCHITECTURE  
**Target build:** AoE2DE `101.103.48987.0`

## Mission
Transform active Objectives into bounded, strategically meaningful courses that are feasible, blocked, or information-dependent without selecting, committing, or executing them.

## Five-pass result

| Pass | Owner | Result |
|---|---|---|
| 1 | Architect | PASS — provisional |
| 2 | Carpenter | PASS |
| 3 | Adversary | PASS WITH TARGETED CORRECTIONS |
| 4 | Scientist | PASS WITH OPEN EMPIRICAL QUESTIONS |
| 5 | Systems Assurance | PASS |

## Minimal pipeline

```text
OBJECTIVE
  ↓
REQUIRE
  ↓
CONSTRAIN
  ↓
ASSESS
  ↓
GENERATE
  ↓
FILTER
  ↓
SMALL CANDIDATE SET
  ↓
DECISION
```

Planning may return no feasible plan, partial feasibility, or information dependencies.

## Load-bearing rules

- Feasibility is not desirability.
- Planning generates candidates; Decision selects.
- Candidate generation is bounded.
- Unknown remains unknown.
- Objective scope and generation survive into candidates.
- Existing commitments, resources, production, map, risk, doctrine, opponent context, and transitions constrain planning.
- Planning does not reserve resources, schedule work, issue commands, or own risk policy.
- Candidate completion is not Objective satisfaction.
- Execution does not retroactively prove candidate feasibility.
- Material changes trigger reconsideration rather than permanent plan attachment.
- Strategic diversity is required enough to avoid candidate monoculture.
- Expensive evaluation occurs only after bounded cheap gates where possible.

## Ownership

**Planning owns:** requirement derivation, constraint application, candidate generation/filtering, feasibility assessment, and planning-context re-evaluation.

It does not own World State, Observation, Belief, Situation, Objectives, Capability truth, Resource policy/state, Production policy, Risk, Doctrine, Opponent Model, Decision, Commitment, Execution, Verification, Recovery, Attention, Scheduler, or Memory.

## Scientific boundary

AoE2DE goals, facts, searches, object data, and dynamic checks provide usable primitives. Search/object-data operations can be expensive. Candidate representation, multiple-candidate coexistence, scope/generation encoding, publication, candidate bounds, cost, atomicity, and replan thresholds require target-build qualification.

## Assurance trace

```text
World/Belief/Situation → Objectives → Planning
→ Capability/Resources/Production/Map/Commitment/Risk/Doctrine/Opponent
→ Decision → Commitment → Execution → Verification → World
```

Information dependencies return through Attention → Scheduler → Observation → World Model.

## Implementation boundary

No ABI allocation or production `.per` representation is authorized by this closure.

**Verdict: PLANNING — CLOSED: ARCHITECTURE.**
