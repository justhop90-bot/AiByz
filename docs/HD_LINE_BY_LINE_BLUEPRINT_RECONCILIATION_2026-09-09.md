# AEGIS / ByzBot — HD Source Line-by-Line Blueprint Reconciliation

**Date:** 2026-09-09  
**Branch:** `aegis/final-build-readiness-2026-09-08`  
**Purpose:** final red-team reconciliation of the authoritative AEGIS blueprint against the recovered `AI (HD version).per` source inventory and its verified Promisory closure.  
**Status:** OPEN for source-anchor closure; no runtime implementation authorized by this document.

## 1. Decision

The **20-slice blueprint remains structurally correct**, but the source reconciliation identifies several historical mechanisms that must be made explicit rather than left implicit inside broad slices.

The most important correction is this:

> **HD is not merely a collection of capability domains. It is a large collection of strategic regimes, resource-control states, transition states, search machines, timers, and communication/control rules that continuously change which capability rules are eligible.**

Therefore a final AEGIS blueprint is incomplete if it models only the nouns — economy, military, monks, construction, water — without explicitly modeling the operational control plane that switches, protects, suppresses, resets, and re-enters those domains.

This reconciliation does **not** justify adding dozens of new top-level slices. It strengthens the cross-cutting architecture and several existing slices.

## 2. Source-closure observations

The recovered source inventory confirms the HD root's direct Promisory closure through:

- `Promisory\\defaultConstants`
- `Promisory\\finalingConstants`
- `Promisory\\finaling`

The recovered inventory records the finaling load at a high source line and shows the HD file continuing through large late-game/terminal sections. The project should continue treating the immutable installed target snapshot as the authoritative line-count/hash source rather than relying on secondary pasted inventories for exact file length.

The public depot inventory independently corroborates that `AI (HD version).per` is the principal stock AI source and that the Promisory directory contains the major operational modules, including `boarhunting`, `buildings`, `escrow`, `gatherers`, `general`, `interaction`, `researches`, `resign`, `scoutcontrol`, `threats`, `trade`, `tsa`, `units`, and `watercontrol`. This is corroboration only; filename presence is not semantic proof.

## 3. Blueprint correction #1 — Strategic regime selection must be explicit

The HD source repeatedly conditions behavior on strategic age/transition state and contains distinct regime-style branches. Recovered line inventories show extensive use of `sn-current-age`, including explicit transition states such as `fc-transit`, and strategy-oriented comments/branches in the surrounding historical source.

The existing blueprint has age advancement in Slice 2 and strategic arbitration in Slice 20, but it does not explicitly name **REGIME / STRATEGY STATE** as a first-class cross-cutting control object.

### Required blueprint addition

AEGIS must explicitly model:

`REGIME = current strategic operating mode`

with at least:

- regime identity;
- generation;
- entry condition;
- exit condition;
- protected commitments;
- enabled capability families;
- suppressed/deferred capability families;
- resource-control posture;
- timing posture;
- transition state;
- failure/recovery path.

Examples are architectural categories, not frozen historical names:

`OPENING | TRANSITION | ECONOMIC_BUILD | MILITARY_PRESSURE | DEFENSE | RECOVERY | WATER | LATE_GAME | TERMINAL`.

Do not assume HD uses these exact names. They are an AEGIS generalization of the demonstrated state-machine structure.

## 4. Blueprint correction #2 — Resource control is more than economy + market

The recovered HD source inventory contains extensive use of `sn-resource-control`, including branches that condition resource use on research/unit requirements and anticipatory defensive requirements. One recovered source anchor explicitly comments on anticipating knight defense; other branches condition market/resource behavior on resource-control state.

This matters because the historical AI is not merely measuring stock and assigning gatherers. It also maintains a **resource-control posture** that changes what resource expenditure is allowed or preferred.

### Required blueprint addition

Slice 4 and Slice 6 must explicitly distinguish:

`RAW STOCK`

from:

`CONTROLLED / PROTECTED / PURPOSE-BOUND STOCK`.

AEGIS must model at least:

- resource-control posture;
- protected reserves;
- strategic commitments;
- anticipated near-term demands;
- emergency conversion authority;
- expenditure restrictions;
- release conditions;
- stale commitment invalidation.

This strengthens the existing escrow/commitment architecture; it does not replace it.

## 5. Blueprint correction #3 — Transition is a first-class state machine

The HD source contains explicit transition states such as `fc-transit` and extensive age-dependent gating around them. The blueprint already models age transition, but transition currently reads too much like a single research event.

The historical machine shows that transition affects many downstream rules simultaneously.

### Required blueprint addition

Every major strategic transition must have:

`PRE-TRANSITION → COMMIT → TRANSITION-IN-PROGRESS → DETECTED-COMPLETE → POST-TRANSITION-REALLOCATION → STABILIZED`

with failure/timeout recovery.

Examples include:

- age transition;
- military composition transition;
- economic source transition;
- water-to-land or land-to-water operational transition;
- emergency-to-normal recovery;
- attack-to-retreat-to-reengage transition.

The exact engine evidence for each transition remains separately qualified.

## 6. Blueprint correction #4 — Search is a reusable machine service

The historical `general.per` search machinery is not an isolated scouting trick. The recovered archaeology shows persistent scratch state, candidate enumeration, measurement, target selection, best-candidate preservation, advancement, reset, and termination.

The blueprint already requires candidate generation/evaluation, but the architecture should explicitly treat **search as a reusable constrained engine service**.

### Required blueprint addition

A reusable AEGIS search contract should support:

`RESET → INITIALIZE → ENUMERATE → MEASURE → HARD-GUARD → SCORE → PRESERVE-BEST → ADVANCE → TERMINATE → RETURN`

and expose:

- search generation;
- candidate cursor/state;
- scope;
- hard constraints;
- measurement set;
- score;
- uncertainty;
- early-exit condition;
- timeout/budget;
- invalidation/reset.

This service will be used by construction, scouting, target selection, placement, resource-source selection, and potentially tactical positioning.

## 7. Blueprint correction #5 — Control-plane hygiene must be mandatory, not incidental

The HD source's basic machinery repeatedly relies on state guards, timers, temporary goals, conditional compilation, resets, and re-entry. The red-team conclusion is that these are not implementation details; they are part of the strategy engine's correctness.

The blueprint must therefore treat the following as mandatory cross-cutting capabilities:

- pending-operation suppression;
- duplicate-command suppression;
- target invalidation;
- timer/hysteresis state;
- temporary/scratch state isolation;
- reset-after-transition;
- self-disable/re-entry control;
- stale-state expiry;
- fallback/recovery;
- bounded search/rule cost;
- strategy-regime handoff;
- terminal-state handling;
- communication/operator-control isolation.

## 8. Blueprint correction #6 — Communication is an actual control interface

The HD source contains explicit ally/player communication, including strategic announcements such as a fast-Imperial declaration. The project already recognizes cooperation/tribute, but the blueprint should distinguish:

`INTERNAL STRATEGIC STATE`

from:

`EXTERNAL COMMUNICATION / COORDINATION STATE`.

Communication must never be treated as proof that the underlying strategic transition occurred.

The contract should be:

`DECISION → COMMUNICATION INTENT → MESSAGE ACTION → NO STATE AUTHORITY`

unless separate world-state evidence verifies the communicated claim.

## 9. Blueprint correction #7 — Difficulty/execution scaling deserves an explicit contract

The blueprint already names difficulty/execution scaling in historical lessons, but it is not yet a formal architectural contract.

AEGIS should separate:

`STRATEGIC INTENT`

from:

`EXECUTION POLICY`.

Execution policy can constrain:

- observation cadence;
- search depth;
- number of candidate evaluations;
- reaction latency;
- tactical aggressiveness;
- retry budget;
- communication frequency;
- rule-budget allocation.

Difficulty must not silently change the semantic meaning of strategic state.

## 10. Blueprint correction #8 — Civilian/economic continuity remains a hard requirement

The red-team source audit remains correct that the broad economy slice is insufficient unless it closes the mundane lifecycle:

`CREATE → QUEUE → AVAILABLE → ASSIGN → WORK → IDLE → REASSIGN → DEATH → REPLACEMENT`

and infrastructure/source continuity:

`SOURCE AVAILABLE → SERVICEABLE → SATURATED/DEPLETING → RELOCATE/REPLACE → NEW SOURCE ACTIVE`.

This must remain explicit in Slices 3–5 and cannot be delegated to an abstract economy score.

## 11. Blueprint correction #9 — Military control is a lifecycle, not a unit catalog

The source reconciliation reinforces that production, threat classification, target/search state, attack control, retreat, and re-entry are coupled mechanisms.

Therefore Slice 10–17 must all expose the same operational contract:

`OBSERVE → CAPABILITY STATE → OBJECTIVE → AUTHORIZE → COMMAND → PENDING → WORLD EVIDENCE → VERIFY → RECOVER/RECOMMIT`.

A unit list, counter table, or production request is not a military controller.

## 12. Blueprint correction #10 — Terminal behavior is part of the bot

The historical source closure includes a dedicated resignation/terminal subsystem. The blueprint mentions terminal policy but should make the distinction explicit:

`STRATEGIC HOPELESSNESS ≠ ENGINE TERMINAL STATE`

The AEGIS terminal controller must separately model:

- game-over observation;
- resignation policy;
- defeat recognition;
- no-recovery state;
- communication policy;
- post-terminal disable/re-entry behavior.

No resignation rule should be implemented merely because a resource or army threshold looks bad.

## 13. Final reconciled architecture

The 20 vertical slices remain. Add one cross-cutting control plane across all 20:

```text
                    STRATEGIC DIRECTOR
                           |
                  REGIME / TRANSITION STATE
                           |
        +------------------+------------------+
        |                  |                  |
  RESOURCE CONTROL     SEARCH SERVICE     EXECUTION POLICY
        |                  |                  |
        +------------------+------------------+
                           |
                  CAPABILITY SLICES
                           |
      OBSERVE → AUTHORIZE → COMMAND → VERIFY
                           |
              RESET / RECOVER / REASSESS
```

The final bot therefore has:

1. **World model** — what is observed.
2. **Belief model** — what is believed under uncertainty.
3. **Regime/transition model** — what strategic mode and transition currently govern eligibility.
4. **Capability model** — what can be achieved now and what is missing.
5. **Resource-control model** — what can safely be spent, reserved, converted, or protected.
6. **Search service** — how candidates are generated and evaluated under bounded engine cost.
7. **Decision/commitment model** — what the bot intends and has authorized.
8. **Execution bridge** — the only engine-facing command authority.
9. **Verification/recovery model** — what actually happened and what to do when it did not.
10. **Execution policy** — cadence, budget, retry, and difficulty constraints.
11. **Communication/coordination interface** — messages and ally coordination without confusing communication for world state.
12. **Terminal controller** — explicit game-end semantics.

## 14. Reconciliation verdict

### GREEN — architecture

The 20-slice blueprint is still the correct high-level decomposition.

### YELLOW — explicitness

The blueprint must explicitly add the cross-cutting **REGIME / TRANSITION + RESOURCE CONTROL + SEARCH SERVICE + EXECUTION POLICY** plane and formalize communication/terminal semantics.

### RED — historical closure

The blueprint is **not yet historically closed**. A line-by-line source pass still has to produce exact rule/function anchors for each operational family before any capability is marked CLOSED in the HD coverage ledger.

### RED — runtime qualification

No finding here clears any machine ABI or runtime qualification gate.

## 15. Required next pass

The next archaeological pass is not another architecture brainstorm. It is a source-anchor ledger:

`AI (HD version).per LINE/RULE → OPERATIONAL FAMILY → OBSERVATION → STATE WRITE → STATE READER → GUARD → ACTION → POSTCONDITION → FAILURE → RECOVERY → STRATEGIC PURPOSE → AEGIS SLICE/OWNER`

Priority families:

1. strategy/regime selection;
2. resource-control and expenditure protection;
3. civilian production/housing/idle/death/replacement;
4. food-source lifecycle;
5. infrastructure/dropsite replacement;
6. production authorization/queue continuity;
7. unit target/search/invalidation;
8. attack/retreat/restart;
9. monk/relic/conversion/healing;
10. siege and fortification response;
11. water/fishing/transport/naval control;
12. market/trade/conversion;
13. ally/tribute/cooperation/communication;
14. technology/research/age transitions;
15. difficulty/execution scaling;
16. resignation/terminal behavior.

**No production `.per` should be written from this reconciliation.**
