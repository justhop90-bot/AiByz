# AEGIS — Belief Model Five-Pass Closure

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Status:** CLOSED — ARCHITECTURE  
**Target build:** AoE2DE `101.103.48987.0`

## Mission
Given what AEGIS has observed and retained, determine what it currently has reason to believe may be true, how strong that belief is when strength matters, and what should trigger revalidation.

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
WORLD STATE → BELIEF → SITUATION
```

The core semantic object is only what behavior requires: **PROPOSITION + SUPPORT + STRENGTH where needed + STATE where required + REVALIDATION**. The architecture rejects a universal belief database, universal confidence/decay/provenance managers, and mandatory record machinery.

## Load-bearing rules

- Inference never silently becomes World State.
- Scope cannot be generalized without evidence.
- Repeated evidence is not automatically independent evidence.
- Strength is not truth.
- Stale inference is not current evidence.
- UNKNOWN must not collapse into FALSE when consequences differ.
- Contradictory hypotheses may remain unresolved.
- Belief may request attention but cannot command the Scheduler.
- Opponent priors remain hypotheses.
- Execution success/failure does not automatically validate/invalidate a belief.
- Consequential use may require revalidation.
- One semantic state has one owner.
- Numeric identity is not semantic identity.

## Evidence model

Native AoE2DE facts, player/focus/target facts, searches, object data, and scalar state can support observation and inference. There is no established native belief primitive. Representation of generation, strength, currentness, persistence, decay, contradiction, and atomic publication remains an empirical/ABI question.

## Ownership

**Belief owns:** inference, uncertainty, hypotheses, belief strength where behaviorally necessary, and revalidation requirements.  
**World Model owns:** world-state publication.  
**Situation owns:** strategic interpretation.  
**Attention owns:** information priority.  
**Scheduler owns:** timing/workload.

Belief has no direct command, execution, commitment, or scheduling authority.

## Assurance trace

```text
World → Belief → Situation → Opponent/Attention
→ Objectives → Planning → Decision → Commitment
→ Execution → Verification → World/Belief
```

Feedback must preserve epistemic status rather than laundering predictions into facts.

## Scientific gates

Open empirical questions include representation of UNKNOWN/false, belief strength, generation, persistence/decay, contradiction, publication atomicity, search absence semantics, current-vs-last-known behavior, and target-build qualification.

## Implementation boundary

No ABI allocation or production `.per` representation is authorized by this closure.

**Verdict: BELIEF MODEL — CLOSED: ARCHITECTURE.**
