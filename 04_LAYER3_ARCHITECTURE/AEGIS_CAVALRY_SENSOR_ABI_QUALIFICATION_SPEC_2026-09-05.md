# AEGIS — Cavalry Sensor ABI Qualification Specification

**Date:** 2026-09-05  
**Status:** QUALIFICATION SPECIFICATION — NOT IMPLEMENTATION

## Purpose

Qualify the smallest engine-facing sensor needed to establish whether the current focus enemy has cavalry-line units, without committing the result to an AEGIS strategic channel prematurely.

## Candidate primitive family

`up-get-focus-fact` with a unit-count fact and a typed unit/unit-line parameter is the candidate family.

The exact accepted parameter combination must be tested on the target executable. Historical validator behavior is not sufficient.

## Required test variants

1. concrete knight unit ID;
2. knight-line ID;
3. another known cavalry-line ID;
4. zero-count case;
5. positive-count case;
6. changed-count case;
7. focus-player change;
8. unsupported/invalid typed argument case.

## Required observations

For each variant record:

- parser/validator result;
- runtime fact result;
- focus-player identity;
- expected count from controlled scenario state;
- observed count;
- zero/no-result distinction;
- timing;
- build fingerprint;
- whether the result is stable across repeated reads.

## Hard rule

Do not replace `knight-line` with `knight 38` merely to satisfy a historical validator complaint. The stock AI demonstrates legitimate unit-line usage, and official scripting history shows that typed scripting behavior can change through engine updates. The target build decides the result.

## Promotion

The sensor becomes implementation-qualified only when the exact target-build signature and result semantics are established and recorded in the ABI registry.
