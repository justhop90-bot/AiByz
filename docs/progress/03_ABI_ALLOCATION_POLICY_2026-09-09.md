# AEGIS ABI Allocation Policy — 2026-09-09

**Status:** Binding policy until superseded by stronger target-build evidence  
**Parent:** FINAL_RECONSTRUCTION_AUDIT R3  
**Target:** AoE2DE 101.103.48987.0

## Core rules (non-negotiable)

1. **Numeric vacancy is never permission.**  
   An apparently unused number is not safe until typed context, operation legality, ownership, and observable postcondition are known.

2. **Numeric equality is not semantic identity.**  
   The same integer can appear in different operand classes (goal, SN, unit-line, fact parameter, etc.). Collision analysis must be type-aware.

3. **No production allocation without evidence class A1–A3 or an explicit residual-risk acceptance.**  
   Historical source (A4) and inference (A5) cannot clear an allocation by themselves.

4. **Candidate blocks remain candidates until cleared.**  
   The previously mentioned scalar block `10000–10015` is **not cleared**.

5. **Existing v0 numbers (e.g. 441–449 range used in civilian lifecycle) are experimental only.**  
   They must be re-validated before any production claim.

## Allocation procedure (required before any new production goal/SN)

1. Declare intended symbol, type (goal / SN / timer / flag), range, and owning service.
2. Search stock census + collision map for the exact numeric value in the same operand class.
3. Search for any known writer/reader of that value.
4. Record the evidence grade.
5. If any conflict or uncertainty remains, do not allocate; choose another candidate or leave as residual risk with explicit documentation.
6. After allocation, the channel must appear in the ownership matrix with generation/validity pattern.

## Temporary working policy for probes and candidates

- Probe scripts may use high, obviously experimental numbers or clearly documented local constants.
- All probe constants must be prefixed or namespaced so they cannot be mistaken for production allocations.
- Probe scripts must never be loaded by a production root.

## Cleared allocations

**None.**

## Engineering consequence

All new `.per` code written before a formal freeze must treat every numeric channel as provisional and must carry generation + validity guards.
