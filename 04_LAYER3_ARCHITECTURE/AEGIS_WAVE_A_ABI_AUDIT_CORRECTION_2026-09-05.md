# AEGIS — Wave A ABI Audit Correction

**Date:** 2026-09-05  
**Status:** CORRECTION / QUALIFICATION CONTROL  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Finding

The first implementation of the deterministic ABI audit treated every numeric `defconst` value as if it occupied the goal namespace.

That was too broad and was corrected before any numeric ABI allocation was promoted.

The exact HD closure contains two numeric `defconst` values in the candidate range `10000–15999`:

- `heavy-wood = 10000`
- `heavy-wood = 14000`

These are **constant values**, not automatically goal identifiers.

## 2. Why the distinction matters

AoE2 AI scripting is strongly typed by command parameter position. The specialist reference explicitly distinguishes parameter types such as `Goal`, `Sn`, `ClassId`, `BuildingId`, and `Defconst`, and explains that the engine translates symbols according to the parameter type expected by each command. citeturn3search5turn3search4

Therefore:

`defconst heavy-wood 10000`

is not equivalent to:

`goal 10000`

unless `heavy-wood` is supplied in a goal-typed position.

## 3. Corrected audit result

The channel-aware v2 audit explicitly resolves operands of:

- `set-goal`
- `goal`
- `up-modify-goal`
- `up-compare-goal`

against their `defconst` definitions and separately handles literal goal operands.

Result for the exact four-file HD closure:

- declaration rows: **5,259**;
- unique symbols: **1,480**;
- numeric declarations: **4,892**;
- resolved goal operands: **5,490**;
- resolved high goal operands `512–16000`: **0**.

Thus the earlier Layer-2 conclusion is restored **in the narrower, correct sense**:

> No high numeric identifier was found in a goal-typed operand position in the exact normal HD runtime closure.

## 4. Important limitation

This does **not** mean `10000–15999` is globally reserved or safe for arbitrary AEGIS use.

It means only that the current stock HD closure contains no resolved high goal operand in the audited command families.

The allocation still requires:

- target-build operation legality;
- validator acceptance;
- ownership/writer clearance;
- generation/publication semantics;
- build-profile evidence;
- collision review against the complete implementation package.

## 5. Engineering lesson

The correction reinforces one of AEGIS's central rules:

> **Numeric equality is not semantic identity.**

A namespace audit must be typed by channel and parameter position. A raw numeric-value scan is useful for archaeology, but unsafe as an ABI allocator.

## 6. Disposition

- **Architecture:** unchanged.
- **Layer-2 symbolic conclusion:** preserved, narrowed and clarified.
- **Numeric ABI:** still not cleared.
- **Audit harness:** v2 promoted as the deterministic channel-aware implementation.
- **Production `.per`:** unchanged.

This correction is itself evidence that the qualification process is functioning: a tempting false collision was detected, investigated, and prevented from becoming an allocation rule.
