# AEGIS Resource Portfolio — Five-Pass Closure

Date: 2026-09-05
Status: CLOSED — ARCHITECTURE

## Mission
Determine whether current qualified resource conditions materially constrain or support an upstream requirement without becoming a strategic arbiter, production planner, market decision-maker, or resource truth owner.

## Five-pass result
1. Architect — PASS
2. Carpenter — PASS
3. Adversary — PASS WITH TARGETED CORRECTIONS
4. Scientist — PASS WITH OPEN EMPIRICAL QUESTIONS
5. Systems Assurance — PASS; subsystem closed for architecture

## Contract
Resource Portfolio owns resource-side posture, pressure, requirement-relative feasibility, qualified reserve constraints, resource-side uncertainty, and necessary temporal qualification.

It consumes qualified resource state, current obligations, upstream requirements, reserve constraints, relevant timing, and relevant accessibility context.

It does not own resource truth, observation, obligations, Objectives, Planning, Decision, Commitment, Capability, Production policy, Market policy, gathering policy, Map Control, Risk policy, Doctrine, Execution, Verification, Recovery, Attention, Scheduler, or Memory.

## Load-bearing invariants
- Resource truth ≠ resource posture.
- Current resource ≠ usable resource.
- Resource obligation ≠ resource state.
- Reserve constraint ≠ reserve policy.
- Feasibility ≠ reservation, capability feasibility, executability, or desirability.
- Resource existence ≠ accessibility ≠ gatherability ≠ availability to a course.
- UNKNOWN ≠ ZERO.
- Stale state/requirements/obligations cannot silently become current.
- Candidate feasibility does not allocate resources.
- Deficit does not authorize market, gathering, production, or Commitment changes.
- Portfolio cannot arbitrate Objectives or become an economic optimizer/simulator.
- Aggregation is allowed only where semantic identity is behaviorally irrelevant.
- Timing is bounded and requirement-specific.
- Numeric identity is not semantic identity.
- All production representations remain subject to target-build ABI qualification.

## Scientific gates retained
Resource observation, freshness, zero/unknown semantics, precision, obligation encoding, reserve encoding, concurrent-demand isolation, temporal feasibility, accessibility qualification, publication atomicity, and runtime budget remain empirical/ABI gates.

## Closure
Architecture is closed. ABI allocation, runtime implementation, and production `.per` are explicitly deferred to later qualification gates.
