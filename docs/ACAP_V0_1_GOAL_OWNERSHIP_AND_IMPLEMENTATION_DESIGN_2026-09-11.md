# ACAP V0.1 — Goal Ownership and Exact `.per` Implementation Design

**Date:** 2026-09-11  
**Scope:** `main/AegisProm` source only  
**Status:** DESIGN / EVIDENCE GATE — **NOT IMPLEMENTATION**  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652 where applicable  
**Excluded:** `runtime/AegisProm`, ADProm, byzwarcouncil, XS

## 1. Purpose

This document defines the smallest implementable ACAP vertical slice for:

`enemy cavalry observation → demand → deficit → feasibility → authorization → existing physical production endpoint → pending → world-state capability verification → reassessment`.

No production `.per` file is changed by this design document.

The design deliberately preserves the existing physical production endpoint in `AEGIS-cavalry-response-v0.per` rather than routing through `Aegis-execution-final.per`, because the latter is a control-state propagation layer rather than a proven physical executor.

## 2. Proven existing goal ownership

The current source graph establishes these owners:

| Goal range | Owner | Meaning | Status |
|---|---|---|---|
| 300–309 | `AEGIS-foundation.per` | world-model frame | existing |
| 310–319 | `AEGIS-foundation.per` | world-model observations | existing |
| 610–617 | `AEGIS-scouting-threat-v0.per` | threat observation/classification | existing |
| 620–624 | `AEGIS-cavalry-response-v0.per` | bounded cavalry-response lifecycle | existing |
| 630–637 | `AEGIS-military-production-v0.per` | separate production candidate lifecycle | existing, not selected as ACAP endpoint |
| 670–679 | micro-control | tactical control | existing |
| 680–689 | micro-state | tactical state | existing |
| 690–699 | micro-groups | tactical groups | existing |
| 700–709 | micro-geometry | tactical geometry | existing |
| 710–719 | micro-governor | tactical governance | existing |
| 720–729 | micro-verification | tactical verification candidate | existing |
| 730–739 | micro-execution bridge | tactical execution bridge | existing |

The graph audit found no major absent Aegis-local namespace declaration among the 49 source files. It did find declared-but-uninitialized state, most importantly `aegis-mp-unit` in the separate military-production candidate.

## 3. ACAP candidate namespace

The next unused-looking namespace is proposed as **candidate only**:

`740–759`

This range is **not implementation-qualified**. The existing Goal Namespace Operation Qualification Specification requires direct qualification of every operation actually used (`set-goal`, `up-modify-goal`, `up-compare-goal`, and fact-to-goal output where applicable) on the target build before promotion.

No stock goal is to be repurposed.

### Proposed scalar goals

| ID | Symbol | Owner | Type / allowed meaning |
|---:|---|---|---|
| 740 | `aegis-acap-generation` | ACAP | publication generation |
| 741 | `aegis-acap-valid` | ACAP | 0/1 validity |
| 742 | `aegis-acap-state` | ACAP | ACAP FSM state |
| 743 | `aegis-acap-required` | ACAP | required anti-cavalry capability for this slice |
| 744 | `aegis-acap-current` | ACAP | verified current anti-cavalry capability |
| 745 | `aegis-acap-deficit` | ACAP | non-negative capability deficit |
| 746 | `aegis-acap-candidate` | ACAP | candidate response kind |
| 747 | `aegis-acap-quantity` | ACAP | authorized production quantity |
| 748 | `aegis-acap-feasible` | ACAP | 0/1 feasibility result |
| 749 | `aegis-acap-authorized` | ACAP | 0/1 strategic authorization |
| 750 | `aegis-acap-requested` | ACAP | 0/1 physical request issued |
| 751 | `aegis-acap-pending` | ACAP | 0/1 production pending |
| 752 | `aegis-acap-baseline` | ACAP | pre-request verified spearman count |
| 753 | `aegis-acap-observed` | ACAP | latest observed spearman count |
| 754 | `aegis-acap-reassess-at` | ACAP | game-time deadline / reassessment point |
| 755 | `aegis-acap-failure` | ACAP | bounded failure code |
| 756 | `aegis-acap-evidence` | ACAP | evidence-strength code |
| 757 | `aegis-acap-threat-generation` | ACAP | threat generation consumed |
| 758 | `aegis-acap-attempts` | ACAP | bounded request attempts |
| 759 | `aegis-acap-permit` | ACAP | handoff permit read by physical endpoint |

## 4. FSM state values

State values are deliberately small integers because `up-compare-goal` compares the stored scalar value, not the semantic name.

```text
0  NO_DEMAND
1  THREAT_ESTABLISHED
2  DEMAND_ESTABLISHED
3  DEFICIT_ESTABLISHED
4  FEASIBILITY
5  AUTHORIZATION
6  PRODUCTION_REQUESTED
7  PRODUCTION_PENDING
8  CAPABILITY_VERIFICATION
9  REASSESSMENT
10 DEMAND_CLOSED
11 DEFERRED
12 PRODUCTION_FAILED
13 COMPLETION_UNVERIFIED
14 AUTHORIZATION_EXPIRED
```

Candidate implementation constants for these values must remain in the same ACAP module as the goal declarations so state-value ownership is unambiguous.

## 5. Existing symbols that ACAP must read, not own

### Threat source

`AEGIS-scouting-threat-v0.per` owns:

- `aegis-st-valid` = 611
- `aegis-st-threat` = 616
- `aegis-st-threat-cavalry` = 1
- `aegis-st-generation` = 610
- cavalry counts 613–615

The threat observer explicitly counts `scout-cavalry-line`, `cavalry-archer-line`, and `knight-line`; it classifies cavalry threat at scout cavalry ≥3, cavalry archers ≥2, or knights ≥2. ACAP must consume this classification rather than duplicate the detector.

### World-model source

ACAP may read the existing foundation-published resource and population facts needed for feasibility, but it must not overwrite foundation goals.

### Physical endpoint

`AEGIS-cavalry-response-v0.per` owns 620–624 and currently issues:

`(up-train escrow-state c: spearman-line)`

after its own local stage and `can-train spearman-line` checks.

ACAP must not claim ownership of 620–624.

## 6. Critical semantic separation

The current cavalry-response file labels a local stage `AUTHORIZED`, but that stage is reached merely from cavalry threat plus `can-train spearman-line`. That is **not** ACAP strategic authorization.

Therefore:

```text
ACAP AUTHORIZATION (goal 749)
        |
        v
ACAP PERMIT (goal 759)
        |
        v
AEGIS-cavalry-response local endpoint
        |
        v
(up-train escrow-state c: spearman-line)
```

`can-train` remains feasibility only. It cannot by itself create ACAP authorization.

The physical endpoint should receive a new ACAP permit condition while retaining its own existing feasibility and bounded-attempt protections. The endpoint must not write ACAP demand, deficit, or authorization state.

## 7. Exact transition design

### T01 — NO_DEMAND → THREAT_ESTABLISHED

**Writer:** ACAP 742, 757, 756  
**Read:** `aegis-st-valid == 1`, `aegis-st-threat == cavalry`  
**Evidence:** DIRECT threat classification  
**Mutation:** state=1; consume threat generation; evidence=direct.

Do not infer a threat from a unit vocabulary string outside the established threat observer.

### T02 — THREAT_ESTABLISHED → DEMAND_ESTABLISHED

**Writer:** ACAP 743, 746, 747, 742  
**V0 slice requirement:** `required=1`, `candidate=spearman`, `quantity=1`.

This is a **vertical-slice test requirement**, not a claim that one spearman is strategically sufficient against all cavalry threats.

**Evidence:** COMPOSED.  
**Mutation:** demand fields populated; state=2.

### T03 — DEMAND_ESTABLISHED → DEFICIT_ESTABLISHED

Before the request, acquire:

`baseline = unit-type-count-total spearman-line`.

Set:

`current = verified baseline`  
`deficit = max(0, required - current)`.

Only verified capability may reduce the deficit.

### T04 — DEFICIT_ESTABLISHED → DEMAND_CLOSED

If `deficit <= 0`, close without issuing production.

This path proves that an already-satisfied capability does not create a redundant command.

### T05 — DEFICIT_ESTABLISHED → FEASIBILITY

Read actual feasibility conditions, at minimum:

- `can-train spearman-line`
- required resource/escrow conditions exposed by the existing production path
- valid candidate
- valid quantity
- current threat still active

`can-train` is evidence of engine feasibility only.

### T06 — FEASIBILITY → AUTHORIZATION

**Writer:** 749 and 759.  
**Owner:** ACAP only.

Preconditions:

- deficit > 0;
- candidate valid;
- feasibility true;
- threat generation still current;
- no existing active authorization.

Authorization must carry a bounded validity interval using `aegis-acap-reassess-at` and the consumed threat generation. The exact interval must be chosen conservatively; it is not to be invented from an assumed engine timer rate.

### T07 — FEASIBILITY → DEFERRED

If feasibility fails, no physical command is emitted. Record a bounded failure/defer code and set a future reassessment point.

### T08 — AUTHORIZATION → PRODUCTION_REQUESTED

Set permit=1 only after authorization.

The physical cavalry endpoint reads permit=1 and performs its own existing `can-train` check before issuing the existing `up-train` command.

On successful command traversal, ACAP records requested=1 and state=6.

A goal write is not itself evidence that the engine accepted the command; the existing command must remain the physical event.

### T09 — PRODUCTION_REQUESTED → PRODUCTION_PENDING

Observe:

`up-pending-objects c: spearman-line >= 1`.

This is DIRECT/ENGINE-SPECIFIC pending evidence.

It is not completion and does not credit capability.

### T10 — PRODUCTION_REQUESTED → PRODUCTION_FAILED

If the bounded request was emitted but no pending object becomes observable within the qualified timeout/reassessment boundary, enter failure rather than treating absence of pending as completion.

### T11 — PRODUCTION_PENDING → CAPABILITY_VERIFICATION

Once the pending lifecycle leaves the request/pending condition, capture a fresh observed spearman-line count.

Do not infer completion merely from a queue transition unless the target build directly qualifies that transition as completion evidence.

### T12 — PRODUCTION_PENDING → COMPLETION_UNVERIFIED

If the pending state disappears but no sufficiently strong world-state completion evidence exists, preserve uncertainty.

No capability credit is allowed.

### T13 — CAPABILITY_VERIFICATION → CAPABILITY_VERIFIED

Strongest V0 available evidence:

`observed spearman-line > baseline`.

This proves that the observed capability count increased; it does **not** prove causal attribution to the specific request if concurrent spearman production is possible.

Therefore V0 capability verification is classified COMPOSED unless concurrent-production exclusion is separately proven.

### T14 — CAPABILITY_VERIFIED → REASSESSMENT

Set `current = observed`, clear the physical permit, and recompute from the current threat state.

### T15 — REASSESSMENT → DEMAND_CLOSED

If current threat is absent or deficit <= 0, close demand.

### T16 — REASSESSMENT → DEFICIT_ESTABLISHED

If threat remains and deficit > 0, return to deficit calculation without assuming the previous request remains valid.

### T17 — REASSESSMENT → THREAT_ESTABLISHED

If the threat classification changed or its generation advanced, invalidate the old demand and consume the new threat generation.

### T18 — DEMAND_CLOSED → NO_DEMAND

Clear transient ACAP fields and permit=0.

### T19 — AUTHORIZATION → AUTHORIZATION_EXPIRED

If `game-time >= reassess-at` before physical request, clear permit and require fresh feasibility/authorization.

### T20 — PRODUCTION_PENDING → PRODUCTION_FAILED

If the pending request exceeds its qualified lifecycle boundary without completion evidence, fail or move to completion-unverified according to the strongest evidence available. Never convert pending absence into success.

## 8. Rule placement

The preferred source placement is a single new ACAP module loaded **after threat observation and before the physical cavalry response**.

Conceptual load order:

```text
AEGIS-foundation
    ↓
AEGIS-scouting-threat-v0
    ↓
ACAP V0.1 demand/deficit/authorization
    ↓
AEGIS-cavalry-response-v0
    ↓
ACAP verification/reassessment
```

If the repository's final loader cannot guarantee this ordering, the implementation must instead use generation/state guards so that same-cycle rule ordering cannot create a false dependency.

## 9. Timer policy

Do not introduce a new timer merely because the FSM contains a timeout concept.

The source already uses `enable-timer` in the foundation and other vertical slices, while the repository separately maintains an ABI probe plan because timer firing/re-entry behavior requires qualification.

For ACAP V0, prefer a `game-time` snapshot in `aegis-acap-reassess-at` for bounded expiry. A timer may be used only after the exact timer operation required by ACAP has been qualified on the target build.

## 10. Forbidden shortcuts

The implementation must not:

1. call `up-train` directly from threat detection;
2. equate `can-train` with authorization;
3. equate `DE_QUEUE` or pending-object disappearance with completion;
4. credit queued/pending units as verified capability;
5. use `Aegis-execution-final.per` as a physical executor;
6. use `Aegis-verification-final.per` as proof of world-state completion;
7. replace `spearman-line` with a concrete unit ID merely because the symbols look similar;
8. import ADProm/byzwarcouncil architecture;
9. modify `aegis-mp-unit` as an incidental fix to this slice;
10. assume one spearman is strategically optimal against every cavalry composition;
11. add timers before timer semantics are qualified;
12. use an unqualified goal ID in production.

## 11. Promotion gates

### Gate A — static

Before implementation:

- prove no collision in the candidate goal range;
- prove every ACAP goal has one writer;
- prove every ACAP reader has a declared owner;
- prove every state transition has a unique writer;
- prove physical command ownership remains in the existing endpoint;
- prove no forbidden module is imported.

### Gate B — runtime/engine qualification

Before promotion:

- qualify every used goal operation on the target build;
- qualify the exact fact-to-goal operation for baseline/observed counts;
- qualify `up-pending-objects` semantics used by this slice;
- qualify the chosen expiry mechanism;
- capture build fingerprint and exact observed values.

### Gate C — lifecycle

Promotion requires one complete positive lifecycle and at least these negative paths:

- infeasible request;
- expired authorization;
- rejected/blocked production;
- pending without verified completion;
- already-satisfied capability;
- threat escalation/reassessment.

## 12. Current implementation verdict

**NOT IMPLEMENTED. NOT PROMOTED.**

The architecture is now sufficiently specified to implement the smallest ACAP slice without inventing a strategic control plane, but the candidate goal namespace and timer behavior remain operation-qualified prerequisites.

The existing cavalry observer and physical spearman endpoint are preserved as evidence-backed vertical components. The missing work is specifically the semantic middle and the independent lower verification/reassessment boundary.
