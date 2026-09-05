# AEGIS Layer 3 — Pass 91 Failure Topology and Integration Test Plan

Date: 2026-09-05
Status: ARCHITECTURE / TEST DESIGN / NO RUNTIME CLAIM
Scope: `.per` architecture only. XS excluded.

## 1. Purpose

A complex bot fails most dangerously at seams: stale state, competing writers, partial execution, vanished objectives, queue blockage, resource contention, and false verification. This plan turns those seams into explicit adversarial test families before implementation.

## 2. Failure taxonomy

F1 Observation failure — threat missing, stale, contradictory, or invalid.
F2 Assessment failure — wrong classification, confidence, or objective mapping.
F3 Capability failure — required capability malformed, obsolete, or incorrectly measured.
F4 Arbitration failure — competing commitments, starvation, procedural priority, or lost epoch.
F5 Resource failure — reservation conflict, underfunding, or discretionary-resource miscalculation.
F6 Producer failure — no eligible producer, producer disappears, or producer becomes invalid.
F7 Queue failure — queue full, request not accepted, pending state persists, or queue semantics change.
F8 Execution failure — command issued but no accepted/queued evidence appears.
F9 World-transition failure — completion occurs outside expected timing or observation window.
F10 Verification failure — aggregate evidence mistaken for exact object/battlefield evidence.
F11 Staleness failure — delayed observation or timer acts on an old generation.
F12 Ownership failure — unauthorized writer mutates consequential state.
F13 Lifecycle failure — commitment never exits, exits too early, or cannot be replaced.
F14 Integration failure — two individually valid modules create an invalid combined transition.
F15 Build/ABI failure — engine, validator, and project semantics diverge.

## 3. Minimum adversarial suite

| ID | Scenario | Expected protection |
|---|---|---|
| T01 | cavalry observation disappears immediately after authorization | invalidate/reassess; no blind execution |
| T02 | cavalry count is stale but objective remains valid | observation age prevents silent reuse beyond policy |
| T03 | required capability falls to zero after commitment | commitment may be released/replanned; no automatic success claim |
| T04 | two production candidates become feasible in same controller cycle | explicit policy or best-so-far arbitration |
| T05 | lower-ranked candidate becomes feasible before higher-ranked command | documented arbitration policy determines outcome |
| T06 | resource reservation is partially consumed elsewhere | command gate rejects or recomputes; reservation never negative |
| T07 | selected producer disappears | producer failure → release/reselection |
| T08 | selected producer becomes busy | feasibility recheck before consequential command |
| T09 | train command issued but queue does not change | remain below queued evidence; recover/retry policy required |
| T10 | queue changes but completion does not occur | remain PENDING; timeout policy required |
| T11 | unit count rises but exact identity is unavailable | accept only aggregate creation evidence, not object identity |
| T12 | created unit exists but has not deployed | objective/effect cannot be marked complete |
| T13 | deployed counter unit fails to affect threat | battlefield/effect verification fails; reassess |
| T14 | timer fires for prior commitment generation | generation guard rejects stale mutation |
| T15 | competing module writes same commitment field | writer-exclusivity violation is detected/rejected by design audit |
| T16 | objective replaced while old execution remains pending | old generation becomes stale; successor cannot inherit blindly |
| T17 | commitment reaches maximum duration | watchdog forces review/release/re-arbitration |
| T18 | arbitration dirty bit is missed | authoritative epoch still detects changed arbitration state |
| T19 | record reader observes invalid/unpublished record | VALID guard prevents consumption |
| T20 | same-pass state changes before downstream rule | allowed only where declared; no atomic-handoff assumption |
| T21 | build supports primitive but validator rejects syntax | support matrix blocks promotion; no workaround silently changes semantics |
| T22 | validator accepts primitive but engine support differs by build | build profile blocks promotion |
| T23 | high numeric goal collides with existing symbol | namespace audit blocks implementation |
| T24 | deficit reaches zero while objective postcondition remains unmet | verification continues; zero deficit is not success |

## 4. State-machine safety properties

### S1 — No phantom completion

No transition may increase evidence level without an observed predicate supporting the new level.

### S2 — No stale mutation

A delayed operation with a non-current generation cannot mutate active consequential state unless a declared stale-data policy explicitly permits it.

### S3 — No unauthorized consequential write

Every consequential state field has one declared owner or a structurally exclusive mutation phase.

### S4 — No negative reservation

`RESERVED >= 0` must remain invariant. Underfunding is an explicit state, not an arithmetic accident.

### S5 — No dead commitment

Every commitment has a legal path to success, release, replacement, expiry/watchdog, or recovery/re-arbitration.

### S6 — No false objective success

Capability satisfaction is necessary evidence at most; objective success requires its own postcondition.

### S7 — No accidental scheduler semantics

If candidate selection is ordered, order must be intentional. If optimized, an incumbent/best-so-far state must exist.

### S8 — No buildless ABI assumption

A primitive is not implementation-cleared until its exact build scope and validator representation are known.

## 5. Failure handling policy

Failure does not imply retry. Each failure must classify into:

`RECOVER → WAIT → RELEASE → REPLACE → RE-ARBITRATE → ABANDON`

The choice depends on failure class, commitment debt, objective validity, resource opportunity cost, and current capability. These are AEGIS policy constructs, not claims about historical HD semantics.

## 6. Test promotion ladder

T0 = static schema test.
T1 = deterministic state-transition test.
T2 = source/lint/validator test.
T3 = controlled engine execution test.
T4 = replay corroboration.
T5 = battlefield validation.

A test cannot promote a higher layer if the lower-layer contract is unresolved.

## 7. First implementation test target

The first executable integration test should exercise the entire Cavalry Threat Containment path with injected failures at T01, T07, T09, T14, T16, and T24. This gives maximum architectural coverage with minimum subsystem count.

Runtime execution is currently blocked because the authorized workstation connection is unavailable. Therefore all T3+ status remains OPEN.

## 8. Exit criterion

Layer-3 implementation may begin only when:

1. cross-module contract matrix is accepted;
2. state ABI numeric allocations are collision-audited;
3. primitive signatures are build-profiled;
4. ownership/writer matrix is complete for the first slice;
5. generation and record-publication protocols are encoded;
6. transition legality is mechanically representable;
7. failure tests have expected outcomes;
8. validator support is separately documented from engine support;
9. exact installed build is recorded before runtime promotion.

Current verdict: **ARCHITECTURE READY FOR ABI FINALIZATION; CODE GENERATION STILL BLOCKED BY ABI COLLISION AUDIT AND RUNTIME BUILD VERIFICATION.**