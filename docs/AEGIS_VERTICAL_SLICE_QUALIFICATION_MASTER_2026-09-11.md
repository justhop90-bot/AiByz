# AEGIS Vertical-Slice Qualification Master — 2026-09-11

**Status:** NORMATIVE QUALIFICATION FRAMEWORK
**Scope:** every bounded, engine-facing vertical slice identified by the `main/AegisProm` forensic graph.
**Excluded:** strategic/control-plane skeletons are not called vertical slices; qualification/probe modules remain evidence instruments, not production slices.
**Runtime constraint:** pure `.per`; no XS, hooks, injection, memory modification, undocumented harness, or runtime patching.

## 1. Vertical-slice inventory

1. **Civilian worker economy** — worker-role census/vector → demand → arbitration → target/source selection → task command → task/productivity observation → recovery.
2. **Villager production** — civilian demand → villager train request → pending observation → lifecycle reconciliation.
3. **Housing construction** — housing demand → build authorization → physical build → pending/foundation observation → completed-house observation → failure/retry ownership.
4. **Age transition** — current age + resources + research feasibility → age-up request → observed age transition → failure/reassessment.
5. **Anti-cavalry response** — enemy cavalry observation → threat classification → capability requirement → deficit/feasibility/authorization → spearman production → pending/completion/capability verification → reassessment.
6. **Tactical micro** — tactical intent → target preparation → geometry/fallback → command governor → execution authority → physical dispatch → bounded observation → reassessment/recovery.

The World Model is common substrate. The strategic `Belief → Situation → Objectives → Planning → Decision → Commitment → Execution → Verification → Recovery` chain remains a control-plane skeleton until it has a real physical endpoint and world-state verification chain.

## 2. Common lifecycle contract

Every vertical MUST preserve the semantic sequence:

```text
OBSERVE → CLASSIFY / RECONCILE → DEMAND / INTENT → FEASIBILITY
→ AUTHORIZATION → PHYSICAL REQUEST → ENGINE ACCEPTANCE / PENDING
→ WORLD-STATE VERIFICATION → REASSESS
→ satisfied/CLOSE | changed/REPLAN | failed-or-unknown/RECOVER
```

These need not be literal `.per` states, but the distinctions cannot be collapsed.

## 3. Universal invariants

1. Observation is not classification.
2. Classification is not demand/intent.
3. Feasibility is not authorization.
4. Authorization is not command issuance.
5. Command issuance is not queue acceptance.
6. Queue acceptance/pending is not completion.
7. Completion is not automatically strategic success.
8. Unknown completion remains unknown.
9. Failed execution receives no success credit.
10. Repeated rule firing cannot create duplicate requests.
11. Stale generations cannot authorize current actions.
12. Recovery requires new/current-state evidence.
13. Physical endpoints remain isolated from strategic policy.
14. Every consequential state has an identifiable owner.
15. Runtime qualification is required before promotion.
16. Static source inspection alone cannot establish runtime behavior.

## 4. Civilian worker economy

**Chain:** role census → role deficit → economic demand → arbitration → worker selection → source/dropsite qualification → task command → task verification → productivity observation → recovery.

**Physical endpoint:** `AEGIS-worker-task-command-v0.per` uses real `up-target-objects` dispatch for wood, gold and stone.

**Evidence boundaries:** census is DIRECT; deficit/demand/arbitration are COMPOSED; command issuance is DIRECT; task-state observation is DIRECT/ENGINE-SPECIFIC; productivity is weaker and does not prove resource income; recovery is a disposition, not proof of successful replacement.

**Current blockers:** worker-role V0 targets are zero unless another policy writer supplies them; worker selection does not preserve persistent worker identity; food has no physical endpoint in this slice; several search semantics remain runtime-unqualified.

**Promotion:** prove one non-food allocation from positive demand through physical tasking and observed task state, plus interruption/source-failure without uncontrolled churn.

## 5. Villager production

**Chain:** civilization state → villager demand → authorization → `up-train villager` → pending observation → completion observation → lifecycle reconciliation.

**Existing evidence:** `AEGIS-villager-production-v0.per` has a real villager training endpoint and separates issued from pending. The lifecycle reconciler captures a baseline and observes census increase.

**Current blockers:** pending is not completion; census increase is not automatically causal attribution when concurrent production is possible; demand is consumed on pending, so closure is not proof of completion.

**Promotion:** direct command, pending, and world-state completion evidence; if attribution is insufficient, preserve `COMPLETION_UNVERIFIED`.

## 6. Housing construction

**Chain:** housing pressure → demand → feasibility → house baseline → build → pending/foundation → completed-house observation → confirm/fail → next demand.

**Existing evidence:** the housing module captures a baseline, issues `build house`, observes pending house objects, and compares completed-house count against baseline.

**Current blockers:** placement/site selection is not a complete explicit service; foundation and completion remain distinct; concurrent house completion can make count increase ambiguous.

**Promotion:** authorization, build command, pending/foundation observation, completion observation, and failed/pending-lost path. Never credit construction from `build` alone.

## 7. Age transition

**Chain:** current age → requirement → resource/research feasibility → authorization → `research castle-age` → observed age transition → reassessment.

**Existing evidence:** `AEGIS-research-age-v0.per` has idle/authorized/issued/confirmed/failed states, affordability checks, real research command, and confirmation through current age.

**Current blockers:** the foundation currently writes age as zero rather than acquiring a verified age fact; research/age ABI remains runtime qualification; current module covers one transition, not a general scheduler.

**Promotion:** verified precondition, command issuance, observed age transition, and failed/non-transition behavior.

## 8. Anti-cavalry response / ACAP

**Chain:** enemy cavalry → threat → demand → verified deficit → feasibility → strategic authorization → spearman request → pending → capability verification → reassessment → close/renew.

**Existing evidence:** bounded cavalry detector and physical `up-train spearman-line` endpoint exist. ACAP v0.1 supplies the missing semantic lifecycle contract.

**Current blockers:** demand/deficit/independent authorization, completion uncertainty, causal capability attribution, expiry and closed-loop reassessment remain incomplete. `AEGIS-military-production-v0.per` also has an uninitialized `aegis-mp-unit` selector and is not a safe replacement endpoint without tracing its actual writer.

**Promotion:** ACAP T01–T20 must be satisfied. First proof may require one attributable spearman increment; that proves lifecycle integrity, not strategic sufficiency.

## 9. Tactical micro

**Chain:** world/threat → intent → target selection → geometry/fallback → governor → execution authority → physical dispatch → bounded observation → reassessment/recovery.

**Existing evidence:** micro control establishes engage/retreat/regroup; targeting prepares candidates; geometry prepares target/fallback points; governor maps intent to bounded commands; execution bridge supplies authority; physical adapter contains attack-move/stop/move; verification preserves unknown/partial/failed outcomes.

**Current blockers:** stage ownership is distributed across control/targeting/governor/bridge/adapter; verification does not yet prove complete causal command→world-outcome; attack-move remains separately runtime-qualified; tactical groups are refreshed populations, not proven persistent engine groups.

**Promotion:** prove one bounded engage or retreat through physical dispatch and real post-dispatch observation, plus no-target/failure behavior. Dispatch alone is never tactical success.

## 10. Cross-slice dependency

```text
AEGIS FOUNDATION
   ├── CIVILIZATION STATE → ECONOMY → WORKER TASKING
   │                    ├→ VILLAGER PRODUCTION
   │                    └→ HOUSING
   ├── WORLD/AGE STATE → AGE TRANSITION
   ├── THREAT/INFO → ACAP → SPEARMAN RESPONSE
   └── WORLD/THREAT → TACTICAL MICRO → PHYSICAL DISPATCH
                                      ↓
                              WORLD REASSESSMENT
```

## 11. Qualification package for every slice

```text
01_STATIC_GRAPH
02_STATE_OWNERSHIP
03_ABI_EVIDENCE
04_SUCCESS_TRACE
05_FAILURE_TRACE
06_UNCERTAINTY_TRACE
07_REPEATABILITY
08_ADVERSARIAL_RESULTS
09_RUNTIME_ARTIFACTS
10_PROMOTION_DECISION
```

A slice is `QUALIFIED` only when its exact contract is demonstrated on the target build. Otherwise it remains `UNQUALIFIED`, `BLOCKED`, `FAILED`, or `UNRESOLVED`.

## 12. No disposable qualification code

Qualification does not authorize temporary `.per` probes or runtime harnesses. Existing production or explicitly permanent qualification artifacts may be exercised. If a required behavior cannot be tested without inventing disposable runtime code, the result is `UNQUALIFIED`.

## 13. Promotion order

1. Worker economy — one non-food task lifecycle.
2. Villager production — command → pending → completion/reconciliation.
3. Housing — demand → build → completion/failure.
4. Age transition — feasibility → research → observed transition.
5. ACAP — complete capability lifecycle.
6. Tactical micro — engage/retreat physical lifecycle.
7. Cross-slice integration and adversarial stress.

**No slice is promoted by this document.** It establishes the normative qualification framework and evidence boundaries only.
