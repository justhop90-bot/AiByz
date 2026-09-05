# AEGIS — Cavalry Threat Containment Vertical Slice Qualification Contract

**Date:** 2026-09-05  
**Status:** ARCHITECTURE-READY / IMPLEMENTATION NOT AUTHORIZED  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Mission

Demonstrate the smallest end-to-end AEGIS behavior that converts qualified enemy-cavalry evidence into a bounded defensive commitment and verifies the resulting operational state.

## Required chain

`OBSERVATION → WORLD MODEL → BELIEF → SITUATION → OBJECTIVE → PLANNING → DECISION → COMMITMENT → EXECUTION → VERIFICATION → RECOVERY`

## Non-negotiable distinctions

- enemy cavalry observation is not an enemy-cavalry belief;
- belief is not situation;
- threat is not objective;
- objective is not plan;
- plan is not decision;
- decision is not commitment;
- commitment is not command;
- command is not acceptance;
- acceptance is not pending;
- pending is not created;
- created is not available;
- available is not effective;
- operational success is not strategic success.

## Minimum scenario

The first implementation-qualification scenario should contain:

1. a controlled enemy cavalry signal;
2. a controlled observation method;
3. a known baseline state;
4. a single bounded objective;
5. a deliberately small candidate set;
6. a deterministic decision point;
7. one commitment;
8. one operational action family;
9. observable postcondition;
10. verification;
11. a controlled failure/deviation case.

## Qualification prerequisites

The slice cannot be promoted until:

- Q-01 is qualified;
- the required Q-02 fields are qualified;
- Q-04 generation semantics are sufficient for stale-authority protection;
- Q-06 semantics are sufficient to avoid zero/unknown collapse;
- Execution lifecycle gates Q-09/Q-10 are qualified for the chosen action family.

## Success evidence

A passing slice must demonstrate, separately:

- observation correctness;
- belief publication;
- situation publication;
- objective publication;
- candidate validity;
- decision validity;
- commitment identity;
- command issuance;
- engine acceptance/queue state;
- pending/created state;
- availability where relevant;
- verification evidence;
- correct recovery on a controlled deviation.

## Failure evidence

The test must intentionally include at least one condition where:

- the desired action cannot be completed;
- the controller must not claim success;
- stale authority must not issue obsolete work;
- UNKNOWN must remain UNKNOWN when evidence is insufficient.

## Promotion rule

The slice is not a demo. It is a qualification instrument. Passing it establishes only the tested semantics for the tested build, action family, scenario, and ABI representation.
