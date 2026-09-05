# AEGIS — Wave A Shared Qualification Status

**Date:** 2026-09-05  
**Status:** ACTIVE — PARTIAL QUALIFICATION  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Purpose

This is the first evidence disposition against the shared qualification register. It does not claim that unresolved gates are failures. It records exactly what is currently established and what remains target-build empirical work.

## 2. Q-01 — Build Identity & Semantic Scope

**Disposition: PASS FOR TESTING**

Direct workstation evidence establishes:

- executable: `AoE2DE_s.exe`;
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`;
- Steam AppID: `813780`;
- Steam BuildID/TargetBuildID: `24094652`;
- untouched stock AI file count: `516`;
- normal HD AI closure: four files.

This qualifies the identity of the test target. It does not qualify any particular AI primitive.

## 3. Q-02 — Typed ABI Identity & Legal Range

**Disposition: PARTIAL — STATICALLY QUALIFIED / RUNTIME OPEN**

Strong evidence establishes that parameter type is semantically material. The specialist Parameter Index distinguishes `BuildingId`, `ClassId`, `Age`, `ActionId`, and other typed parameters; the Commands Index separately classifies `goal`, `set-goal`, `up-compare-goal`, `up-get-focus-fact`, `up-get-object-data`, and related primitives. citeturn0search5turn2search0

Official update history also demonstrates that engine behavior is operation-specific: strategic-number capacity changed over time, garrison accepted unit lines, and several `up-*` primitives received semantic fixes. citeturn0search3turn0search1

Goal capacity is documented as 16,000 in current-era evidence, but the AEGIS reserved namespace and operation-specific legal behavior still require target-build qualification. The old 512-goal assumption is rejected as a universal current limit.

**Remaining P1 tests:** T03–T06.

## 4. Q-03 — State-Channel Ownership & Collision

**Disposition: STATICALLY QUALIFIED AS A SAFETY BOUNDARY / RUNTIME ALLOCATION OPEN**

The A1 collision map remains authoritative. No stock channel is cleared for core AEGIS ownership merely because its numeric value is convenient.

The machine rule is therefore:

`numeric identity ≠ semantic ownership`.

Before allocation, each proposed channel must have a writer/reader/lifecycle/collision record and target-build ABI identity.

**Remaining P1 tests:** T07–T08.

## 5. Q-04 — Identity & Generation Continuity

**Disposition: OPEN — P1**

Architecture is closed, but no target-build machine representation has yet been promoted as the authoritative generation mechanism.

**Required tests:** T09–T11.

No implementation may treat a convenient goal/SN/timer value as a qualified generation field until these tests succeed.

## 6. Q-05 — Scope, Freshness & Current-vs-Last-Known

**Disposition: OPEN — P1**

The World Model and Belief contracts require scope and freshness distinctions, but the machine representation remains unqualified.

**Required tests:** T12–T14.

## 7. Q-06 — UNKNOWN / FALSE / ZERO / Absence

**Disposition: OPEN — P1**

Historical/specialist evidence documents important distinctions in counting/search behavior. For example, specialist patch notes explicitly distinguish sighted counts, pending counts, and queued-unit semantics, and document changes to `up-find-remote` and focus/target fact behavior. citeturn1search0turn0search1

This is useful evidence but does not prove the complete AEGIS unknown model on the current build.

**Required tests:** T15–T18.

## 8. Wave A overall disposition

| Gate | Status | Evidence level |
|---|---|---|
| Q-01 | PASS FOR TESTING | E0 direct workstation |
| Q-02 | PARTIAL | E0/E1/E2; runtime open |
| Q-03 | PARTIAL | E0 static stock baseline + project ABI evidence |
| Q-04 | OPEN | architecture only |
| Q-05 | OPEN | architecture only |
| Q-06 | OPEN | E1/E2 partial; runtime open |

**Wave A is therefore not closed.**

That is intentional. The project has successfully converted broad uncertainty into a finite, auditable set of P1 experiments instead of guessing.

## 9. Next execution priority

The highest-value next experiments are:

1. T03–T06: typed goal/SN/fact ABI boundaries;
2. T07–T08: channel ownership/collision confirmation;
3. T09–T11: generation representation;
4. T15–T18: UNKNOWN/zero/absence semantics.

The runtime harness itself remains an unresolved qualification dependency; its invocation and result semantics must be established before using it as the primary automated evidence mechanism.

## 10. Engineering rule

No failed or blocked test silently changes architecture. No successful static observation silently becomes runtime truth.
