# AEGIS — Decision Five-Pass Closure

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Status:** CLOSED — ARCHITECTURE  
**Target build:** AoE2DE `101.103.48987.0`

## Mission
Given an active Objective, qualified strategic context, and a bounded set of feasible candidates, select which course—if any—should be selected now, or deliberately refuse/defer.

## Five-pass result

| Pass | Owner | Result |
|---|---|---|
| 1 | Architect | PASS — provisional |
| 2 | Carpenter | PASS |
| 3 | Adversary | PASS WITH TARGETED CORRECTIONS |
| 4 | Scientist | PASS WITH OPEN EMPIRICAL QUESTIONS |
| 5 | Systems Assurance | PASS |

## Minimal architecture

```text
CANDIDATES
   ↓
ELIGIBILITY
   ↓
COMPARISON
   ↓
SELECTION / NO SELECTION
```

Comparison may use hard exclusion, dominance, contextual preference, and deterministic tie handling. No universal utility optimizer is required.

## Load-bearing rules

- Decision is selection, not Objective formation.
- Decision consumes candidates; it does not generate them.
- Feasibility and preference remain distinct.
- Decision may refuse or defer deliberately.
- Unknown is not false.
- Objective generation and candidate identity survive the handoff.
- Stale candidates cannot silently become current.
- Decision validity is distinct from Objective validity.
- Decision does not reserve resources or issue commands.
- Risk, Doctrine, Opponent Model, Capability, and Resource state are context/inputs, not Decision ownership.
- Candidate count and comparison work must be bounded.
- Material context change can trigger reconsideration.
- Deterministic tie-breaking cannot hide an unrecorded strategic preference.
- Cross-domain conflicts require one bounded authoritative resolution path, not a universal optimizer.
- Candidate success is not Objective success.
- Commitment rejection does not retroactively prove the Decision wrong.
- Numeric identity is not semantic identity.

## Ownership

**Decision owns:** authoritative current selection/refusal/deferral, bounded candidate comparison, elimination, dominance/contextual preference/tie handling, and enough identity to protect downstream stale state.

It does not own World Model, Belief, Situation, Objectives, Planning, Candidate generation, Capability truth, Resource state/reservation, Production, Risk, Doctrine, Opponent Model, Commitment acceptance, commands, Execution, Verification, Recovery, Attention, Scheduler, or Memory.

## Scientific boundary

AoE2DE supports goal storage/comparison, facts, dynamic checks, searches, and object data, but there is no native Decision primitive. Candidate representation, multiple candidates, generation isolation, publication atomicity, no-selection encoding, comparison bounds, hysteresis, search isolation, stale rejection, and runtime cost remain empirical/ABI gates.

## Assurance trace

```text
World → Belief → Situation → Objectives → Planning
→ Capability/Resources/Production/Map/Risk/Doctrine/Opponent
→ Decision → Commitment → Execution → Verification → World
```

Information dependencies return through Attention → Scheduler → Observation.

## Implementation boundary

No ABI allocation or production `.per` representation is authorized by this closure.

**Verdict: DECISION — CLOSED: ARCHITECTURE.**
