# AEGIS — Cavalry Symbolic-to-Numeric Candidate Map

**Date:** 2026-09-05  
**Status:** PROVISIONAL STATIC CANDIDATES — NOT IMPLEMENTATION-CLEARED  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Purpose

The symbolic Cavalry Threat Containment ABI is frozen. The target-build channel-aware audit now permits a provisional numeric candidate map for scalar goals.

This document is **not** the final ABI allocation. It records candidates so that later validator/runtime evidence can adjudicate them deterministically rather than choosing numbers ad hoc.

## 2. Candidate goal assignments

| Symbol | Candidate goal | Use class | Static collision result | Status |
|---|---:|---|---|---|
| `OBS.ENEMY_CAVALRY` | 10000 | scalar-only | no resolved stock goal operand at 10000 | CANDIDATE |
| `OBS.ENEMY_CAVALRY_AGE` | 10001 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `CAP.CAMEL_CURRENT` | 10002 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `CAP.CAMEL_REQUIRED` | 10003 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `CAP.CAMEL_DEFICIT` | 10004 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `CAND.PRODUCER` | 10005 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `CAND.STATUS` | 10006 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `COMMIT.OWNER` | 10007 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `COMMIT.GEN` | 10008 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `COMMIT.STAGE` | 10009 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `EXEC.STAGE` | 10010 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `EXEC.EXPECTED_GEN` | 10011 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `RES.RESERVED` | 10012 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `RES.DISCRETIONARY` | 10013 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `ARB.EPOCH` | 10014 | scalar-only | no resolved stock goal operand | CANDIDATE |
| `VERIFY.LEVEL` | 10015 | scalar-only | no resolved stock goal operand | CANDIDATE |

## 3. Remaining symbolic fields

`THREAT.CAVALRY_ACTIVE`, `COMMIT.VALID`, and `ARB.DIRTY` remain unassigned because their symbolic contract specifies flag semantics. Their numeric representation is intentionally deferred until the flag inventory/build/validator gates are qualified.

## 4. Why 10000 remains a candidate despite `heavy-wood=10000`

The stock HD closure contains conditional `defconst heavy-wood` values including 10000 and 14000. This is **not** a goal-channel collision by itself.

The channel-aware audit resolved all operands in the goal-typed operations `set-goal`, `goal`, `up-modify-goal`, and `up-compare-goal`. It found zero resolved high goal operands in 512–16000.

Therefore the relevant static question is not “does any defconst contain the integer 10000?” but:

> “Does the target package use goal identifier 10000 in a goal-typed state position that would collide with this allocation?”

Current static evidence says no. Runtime/validator evidence remains open.

## 5. Operation restriction

These candidate goals are intended only for scalar goal operations whose target-build legality is separately qualified.

They must **not** be passed blindly to commands that consume multiple consecutive extended goals, such as cost/point/search-state operations, until those command-specific ranges are qualified. The specialist Data Limits reference documents special restrictions for multi-goal operations. citeturn4search1

## 6. Promotion requirements

Each candidate remains `CANDIDATE` until:

1. validator accepts the exact symbolic declaration and use;
2. target engine accepts the exact operation;
3. no imported implementation state collides;
4. writer/reader ownership is clear;
5. generation/publication semantics are representable;
6. build scope is recorded;
7. the candidate survives a controlled runtime test.

Only then may status become `CLEAR`.

## 7. Current conclusion

The first Cavalry slice now has a deterministic provisional numeric map rather than an undefined allocation problem.

**No production `.per` constants are generated from this document yet.**
