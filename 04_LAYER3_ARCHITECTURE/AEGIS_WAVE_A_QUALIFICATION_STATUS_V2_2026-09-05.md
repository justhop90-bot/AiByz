# AEGIS — Wave A Qualification Status v2

**Date:** 2026-09-05  
**Status:** ACTIVE — STATIC SUBSTRATE QUALIFIED / RUNTIME OPEN  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Current disposition

Wave A has advanced from broad uncertainty to a split state:

- **Q-01:** qualified for testing;
- **Q-02:** substantially statically characterized, runtime/validator gates open;
- **Q-03:** ownership safety boundary established, numeric allocation still provisional;
- **Q-04:** open P1;
- **Q-05:** open P1;
- **Q-06:** open P1.

No architecture was reopened.

## 2. Q-02 — Typed ABI

Static target-package evidence now establishes:

- 5,259 declarations in the exact four-file HD closure;
- 1,480 unique symbols;
- 4,892 numeric declarations;
- 5,490 resolved operands in audited goal operations;
- 0 resolved high goal operands in 512–16,000.

The channel-aware audit also demonstrated why raw numeric declaration scans are insufficient: conditional `defconst` values of 10,000 and 14,000 exist, but they are not goal identifiers merely because the values are numerically high.

The specialist reference confirms parameter typing is semantic and command-position dependent. citeturn3search5turn3search6

**Disposition: STATIC PASS / TARGET-BUILD RUNTIME OPEN.**

## 3. Q-03 — Ownership/collision

The first-slice scalar-goal candidate map is now deterministic:

`10000–10015` are provisional candidates for the 16 scalar goal-like fields.

They are **not CLEAR**. They remain subject to validator, build, writer, generation, publication, and runtime qualification.

Three flag fields remain unallocated pending flag-domain qualification.

## 4. Q-04 — Generation

Architecture requires generation continuity and stale-operation rejection. No numeric generation field is yet promoted.

The candidate map proposes `COMMIT.GEN=10008` and `EXEC.EXPECTED_GEN=10011` only as provisional scalar candidates.

Required next evidence:

- increment semantics;
- equality semantics;
- initialization;
- wraparound;
- stale rejection;
- publication coherence.

## 5. Q-05 — Scope/freshness

The target package provides engine observations but no native AEGIS freshness envelope. Scope and freshness remain AEGIS-derived semantics.

Required next evidence:

- current vs last-known behavior;
- observation age representation;
- stale-read rejection;
- scope preservation through fact publication;
- revalidation behavior.

## 6. Q-06 — UNKNOWN / zero / absence

This remains the most important semantic gate before the first vertical slice.

Official history demonstrates that search/count/pending behavior has changed over time. For example, official Update 39284 changed search stacking and pending-object behavior, while Update 36202 changed queued-object counting semantics. citeturn0search3turn0search2

Therefore the AEGIS distinction:

`CONFIRMED ZERO ≠ NO RESULT ≠ UNKNOWN ≠ STALE`

must be target-build tested rather than inferred from historical documentation.

## 7. T05 static evidence improvement

The exact stock HD closure uses:

`up-get-focus-fact unit-type-count galley-line math-goal`

and analogous unit-line forms for multiple naval lines.

This proves the broader typed compound signature is part of the stock HD scripting substrate. It does **not** prove that every unit-line alias is accepted in every context.

The historical `knight-line` issue therefore remains a runtime/validator experiment, not a reason to replace the line symbol with a concrete unit ID.

## 8. Wave A next order

1. **T03–T06** — goal/SN/fact typed ABI.
2. **T09–T11** — generation.
3. **T15–T18** — UNKNOWN/zero/absence.
4. **T07–T08** — final channel ownership/publication checks.

The runtime harness remains a separate dependency until its invocation/result semantics are qualified.

## 9. Exit condition

Wave A remains open until every P1 gate has either:

- target-build evidence sufficient for an implementation contract; or
- an explicit UNKNOWN/BLOCKED disposition with owner and consequence.

No production `.per` implementation is promoted from Wave A alone.
