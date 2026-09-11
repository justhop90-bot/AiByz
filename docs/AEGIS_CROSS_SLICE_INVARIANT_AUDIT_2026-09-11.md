# AEGIS Cross-Slice Invariant Audit — 2026-09-11

**Status:** NORMATIVE CROSS-SLICE AUDIT / IMPLEMENTATION GAP RECORD
**Authority:** `docs/AEGIS_CANONICAL_LIFECYCLE_CONTRACT_V0_1.md`
**Concrete contract authority:** `schemas/AEGIS-VERTICAL-SLICE-CONTRACTS-1.0.json`
**Scope:** all seven registered AegisProm verticals, including the blocked `military_production` candidate.
**Method:** inspect current `main/AegisProm` source after the request/authorization implementation passes and compare source semantics against the canonical invariants. Runtime-only copies are not promoted into source authority.

## 1. Executive verdict

The request/authorization passes materially improved all six qualification slices, but the cross-slice audit finds **four architectural blockers that must be resolved before qualification promotion**:

1. **Global numeric goal collisions exist across source modules.** The worker recovery block uses goals 550–554 while economic arbitration uses goal 550 and worker target selection uses goal 551. Anti-Cavalry uses goals 630–633 while Military Production already owns 630–637. In a shared `.per` goal namespace these are not harmless local variables; they are competing slots. This is a **P0 source-integrity defect**.
2. **Generation-based authorization expiry is mostly self-comparison and therefore inert.** In Worker Command, Villager Production, Housing, Age Transition, and Anti-Cavalry, authorization-generation is initialized from the same local lifecycle generation that the expiry rule compares against. Nothing changes the local generation while the authorization remains active, so the advertised expiry condition cannot actually expire an authorization. Tactical Micro has the same limitation for its authorization-generation unless the tactical request generation itself changes.
3. **Worker Task Command and Villager Production can supersede an active lifecycle with a newer upstream generation.** Their admission rules test generation mismatch but do not require `valid == 0`; a newer upstream generation can therefore overwrite an active request. Housing and Tactical Micro correctly block new request admission while an active lifecycle remains valid.
4. **Reassessment is still mostly local invalidation rather than a canonical cross-slice reassessment boundary.** The registry requires terminal `REASSESS`; source commonly clears `valid` or enters a local reassess stage without publishing a new authoritative reassessment event to a named owner.

Therefore:

> **Lifecycle boundary implementation: materially improved but NOT cross-slice conformant. Qualification remains blocked.**

No source architecture is promoted merely because the new fields exist. The audit deliberately preserves the stricter contract.

## 2. Invariant matrix

| Vertical | Request identity | Authorization owner | Expiry | Idempotency | Evidence monotonicity | Reassessment | Current verdict |
|---|---|---|---|---|---|---|---|
| `worker_economy` | PRESENT, propagated EDA → WTS → WTC → verification | WTC at physical boundary | **BROKEN / self-comparison** | **BROKEN: active request can be superseded** | PARTIAL / conservative | Recovery closes locally; no canonical reassess publication | **P0** |
| `villager_production` | PRESENT from civilian-demand generation through reconciler | VP production boundary | **BROKEN / self-comparison** | **BROKEN: active request can be superseded** | GOOD discipline; causal gate remains closed | Reconciler closes locally; higher-level reassessment assumed | **P0/P1** |
| `housing` | PRESENT from civilian-demand generation | Housing construction boundary | **BROKEN / self-comparison** | GOOD bounded one-shot request | GOOD; world evidence cannot manufacture causality | Local terminal state; canonical reassess owner absent | **P1** |
| `age_transition` | PRESENT from World Model generation | Age-transition requirement/authorization owner | **BROKEN / self-comparison** | GOOD one-shot research dispatch | GOOD; direct `current-age` evidence preserved | Retry/replan delegated upward | **P1** |
| `anti_cavalry` | PRESENT from threat generation | Cavalry-response module | **BROKEN / self-comparison** | GOOD one-attempt dispatch | GOOD pending/world evidence separation; causal gate closed | Local terminal state; no canonical reassess publication | **P0/P1** |
| `tactical_micro` | PRESENT at Micro Control and propagated through bridge/verification | Execution Bridge | **PARTIAL / not independently expiring while request remains active** | GOOD physical one-shot guard | GOOD conservative partial/failed evidence | Best of seven locally, but still not a canonical reassessment publication | **P1** |
| `military_production` | **MISSING** | Conflated local authorized stage | MISSING | Partial attempt guard only | **TOO WEAK: count delta becomes confirmed** | MISSING | **CANDIDATE BLOCKED** |

## 3. Finding A — global goal-number collisions (P0)

The source goal namespace is shared. Numeric allocation must therefore be globally unique across all loaded AegisProm modules.

Confirmed collisions introduced/exposed by the current boundary work:

### Collision A1 — 550

- `AEGIS-economic-demand-arbitration-v0.per`: `aegis-eda-request-id = 550`
- `AEGIS-worker-recovery-v0.per`: `aegis-wr-failure = 550`

The GitHub code search independently returns both source files for `defconst 550`. fileciteturn194file0L2-L24 fileciteturn194file2L52-L67

### Collision A2 — 551

- `AEGIS-worker-target-selection-v0.per`: `aegis-wts-request-id = 551`
- `AEGIS-worker-recovery-v0.per`: `aegis-wr-attempts = 551`

The current WTS source explicitly assigns request identity to goal 551. fileciteturn169file0L2-L2 GitHub search also returns the worker-recovery goal 551. fileciteturn195file0L2-L24 fileciteturn195file2L52-L67

### Collision A3 — 630–633

- Military Production owns goals 630–637.
- Anti-Cavalry now owns goals 620–633, including `aegis-cr-baseline-spears = 630`, `observed-spears = 631`, `world-evidence = 632`, and `causal-evidence = 633`.

Military Production's authoritative source confirms its 630–637 allocation. fileciteturn208file0L2-L2 Anti-Cavalry confirms the overlapping allocation. fileciteturn206file0L2-L2

**Required disposition:** stop all qualification work until a global goal-allocation pass assigns unique numeric slots. Do not resolve these by changing symbols only; the numeric goal namespace itself must be corrected.

## 4. Finding B — authorization expiry is not actually implemented

The canonical contract requires authorization to become unusable when expired, superseded, cancelled, invalidated, or no longer needed. fileciteturn181file0L2-L2

The current implementations create fields named `authorization-expiry`, but several expiry rules compare the authorization generation to the same local generation that was copied into the authorization record.

Example Worker Command:

```text
authorization-generation := wts-generation
expiry := wts-generation
expiry check: authorization-generation != wtc-generation
```

Since `wtc-generation` is set from `wts-generation` at request admission, the comparison is normally equal. fileciteturn219file0L2-L2

The same semantic pattern exists in Villager Production, Housing, Age Transition, and Anti-Cavalry. Their authorization records are real state, but the expiry condition is not an independently advancing or superseding condition.

Tactical Micro is structurally better because the Execution Bridge has a distinct governor epoch and checks authorization generation against Micro Control's request generation, but its active-request rule still prevents the tactical generation from changing while the request is open. The result is that expiry is still not a demonstrated independent lifecycle event. fileciteturn203file0L2-L2

**Disposition:** retain the explicit fields, but do not call generation equality an implemented expiry mechanism until there is a proven supersession/expiry event that can occur while authorization is live.

## 5. Finding C — active-request supersession

### Worker Command

The admission rule checks `aegis-wtc-generation != aegis-wts-generation`, then explicitly resets and recreates the local request. It does **not** require `aegis-wtc-valid == 0`. A new WTS generation can therefore replace an active WTC lifecycle. fileciteturn219file0L2-L2

That violates the canonical idempotency rule:

```text
R,G already issued AND still pending -> NO DUPLICATE PHYSICAL REQUEST
```

### Villager Production

The VP admission rule similarly checks only generation mismatch. It does not require `aegis-vp-valid == 0`. A newer civilian-demand generation can overwrite an active villager-production lifecycle. fileciteturn212file0L2-L2

### Housing and Tactical Micro

Housing correctly includes `aegis-hc-valid == 0` before opening a fresh request. fileciteturn205file0L2-L2 Tactical Micro also requires `aegis-mc-valid == 0` before opening a new request. fileciteturn207file0L2-L2

**Disposition:** Worker Command and Villager Production require the same active-request protection already used by Housing and Tactical Micro. This is a source correction, not a validator relaxation.

## 6. Finding D — authorization identity is often an alias, not an independent authorization record

Worker Command, Villager Production, Housing, Age Transition, and Anti-Cavalry set authorization identity equal to request identity.

That is not automatically wrong: a one-to-one authorization may be a valid implementation. But the canonical schema requires authorization to identify request, action/capability, generation, owner, and expiry. fileciteturn181file0L2-L2

Current source does not consistently encode the action/capability or owner as part of the authorization record. Instead those facts remain implicit in the module and stage.

Tactical Micro is the strongest implementation because the bridge owns authorization and assigns a separate authorization identity from the governor epoch while preserving the request identity separately. fileciteturn203file0L2-L2

**Disposition:** do not force every slice to copy Tactical Micro's data structure. Instead, the machine-readable contract must require semantic authorization identity and ownership, with the smallest pure-`.per` representation that can prove them.

## 7. Finding E — evidence monotonicity is mostly sound, but qualification evidence is uneven

The recent passes correctly preserve several important distinctions:

- Villager Production keeps queue admission separate from completion and delegates causal attribution to the lifecycle reconciler. fileciteturn212file0L2-L2
- Housing separates pending foundation, completed-house world evidence, and causal evidence. fileciteturn205file0L2-L2
- Age Transition uses direct `current-age >= castle-age` as the actual age-transition world-state evidence rather than treating `research castle-age` as completion. fileciteturn213file0L2-L2
- Anti-Cavalry keeps pending `spearman-line` production distinct from observed spearman count and leaves causal evidence closed unless independently supplied. fileciteturn206file0L2-L2
- Tactical Micro records partial tactical evidence rather than converting command dispatch into success. fileciteturn222file0L2-L2

The major exception is **Military Production**: it promotes `observed > baseline` directly to `confirmed`, without request identity, causal evidence, or an explicit authorization record. fileciteturn208file0L2-L2

That remains acceptable only because the registry correctly marks Military Production as `CANDIDATE_BLOCKED`; it must not be promoted.

## 8. Finding F — reassessment is not yet a shared semantic boundary

The registry requires `REASSESS` as the terminal stage. fileciteturn167file0L2-L2 The canonical contract says reassessment is mandatory after consequential success, failure, expiry, conflict, recovery, or material world-state change. fileciteturn181file0L2-L2

Current source generally does one of three things:

1. clears `valid`;
2. enters a local `reassess` stage;
3. delegates the next generation implicitly to an upstream observer.

Worker Recovery does perform bounded review/retry/upstream disposition, but closes locally and does not publish a canonical reassessment event. fileciteturn214file0L2-L2

Tactical Micro is closest: its physical adapter enters local `REASSESS`, and verification subsequently invalidates Micro Control after an observed result. fileciteturn216file0L2-L2 fileciteturn222file0L2-L2

**Disposition:** define one cross-slice reassessment publication/consumption contract. Do not create a monolithic controller; each vertical can retain its own internal architecture while publishing a normalized consequential outcome.

## 9. Slice-specific audit

### 9.1 Worker Economy — P0

**Good:** request identity now originates in arbitration and is propagated into worker selection, command, and verification. WTS currently uses request identity 551. fileciteturn169file0L2-L2 WTC carries request and authorization fields through the physical command boundary. fileciteturn219file0L2-L2 Verification preserves the same identities. fileciteturn182file0L2-L2

**Blockers:**
- WTS request ID 551 collides with Worker Recovery attempts 551.
- EDA request ID 550 collides with Worker Recovery failure 550.
- WTC can supersede an active request.
- Authorization expiry is not independently effective.
- Recovery closes locally instead of publishing canonical reassessment.
- Task observation remains task-state evidence, not productivity causality. fileciteturn182file0L2-L2

### 9.2 Villager Production — P0/P1

**Good:** request identity, authorization state, baseline villager count, pending queue evidence, and separate causal reconciliation are all present. fileciteturn212file0L2-L2 The reconciler explicitly requires request and authorization identity match plus separate causal evidence before confirmation. fileciteturn221file0L2-L2

**Blockers:**
- active VP request can be overwritten by a newer demand generation;
- expiry is self-comparison rather than independent expiry;
- reconciler closes by `valid = 0`, not canonical reassessment;
- no proven causal-evidence writer exists in source.

### 9.3 Housing — P1

**Good:** request identity, authorization, baseline, pending foundation, world evidence, and causal gate are cleanly separated. fileciteturn205file0L2-L2

**Blockers:**
- expiry condition is not independently advancing;
- authorization identity is currently an alias of request identity;
- completed-house count is not sufficient for request-specific causal attribution;
- local failure/confirmation terminates without publishing canonical reassessment.

### 9.4 Age Transition — P1

**Good:** the implementation correctly protects an issued request from being reset by every new World Model frame; completion is based on direct `current-age` evidence. fileciteturn213file0L2-L2 This is the strongest source-specific evidence model among the civilian verticals.

**Blockers:**
- expiry is not actually demonstrated;
- request identity and authorization identity are aliases;
- no explicit reassessment publication;
- causal-attribution field exists but is intentionally not used for age-transition verification.

### 9.5 Anti-Cavalry — P0/P1

**Good:** threat classification remains upstream and the response module now separates capability demand, feasibility, authorization, physical `spearman-line` production, pending state, world-state count, and causal evidence. fileciteturn184file0L2-L2 fileciteturn206file0L2-L2

**Blockers:**
- goals 630–633 collide with Military Production's 630–637 block;
- expiry is self-comparison;
- authorization identity aliases request identity;
- no canonical reassessment publication;
- causal evidence has no proven writer.

### 9.6 Tactical Micro — P1

**Good:** this is currently the best distributed authorization architecture. Micro Control owns request identity; Governor selects command; Execution Bridge owns authorization; Physical Adapter owns dispatch; Verification owns post-dispatch evidence. fileciteturn207file0L2-L2 fileciteturn203file0L2-L2 fileciteturn216file0L2-L2

**Blockers:**
- expiry is still not demonstrated as an independently advancing condition;
- verification only reaches partial world evidence for engage, not complete tactical success;
- pursuit exists at Governor level but has no corresponding authorization/physical adapter path, so it must remain unqualified;
- local `REASSESS` is not yet a normalized cross-slice reassessment event.

### 9.7 Military Production — candidate remains blocked

The source still declares `aegis-mp-unit` at goal 633 and does not initialize it. fileciteturn208file0L2-L2 The registry therefore correctly remains `CANDIDATE_BLOCKED` with `SELECTOR_INITIALIZATION`. fileciteturn167file0L2-L2

It also lacks the canonical request identity/authorization boundary and directly promotes a spearman count increase to `confirmed`. It must remain outside the six-slice qualification set.

## 10. Required correction order

The audit establishes the following order. **Do not skip ahead.**

### P0-1 — Global goal namespace repair

Build a repository-wide numeric goal allocation table for all AegisProm source files and eliminate every duplicate consequential-state slot.

Known immediate repairs:

```text
550: EDA request-id vs Worker Recovery failure
551: WTS request-id vs Worker Recovery attempts
630–633: Anti-Cavalry vs Military Production
```

This must be solved before further lifecycle implementation.

### P0-2 — Active-request protection

Add the equivalent of:

```text
local-valid == 0
```

to any request-admission rule that can currently supersede an active lifecycle, specifically Worker Command and Villager Production.

### P0-3 — Real expiry semantics

Do not invent a clock.

Define the smallest engine-proven pure-`.per` expiry condition that can invalidate a live authorization without relying on a comparison that is guaranteed to remain equal.

### P1-1 — Canonical reassessment publication

Define one normalized consequential-outcome record that each vertical publishes after success, failure, expiry, conflict, or recovery. The observer/world-model remains the authority for current world state; reassessment consumes the outcome and re-evaluates requirements.

### P1-2 — Authorization semantic schema

Extend the machine-readable registry so authorization records explicitly carry or reference:

```text
request_id
capability/action
authorization_id
owner
generation
expiry
consumption state
```

Do not require identical `.per` structure across verticals.

### P1-3 — Qualification re-run

Only after P0/P1 corrections, rerun the seven-slice validator and promotion gate. No vertical should be promoted merely because the source now contains more fields.

## 11. Final disposition

**Overall: RED / QUALIFICATION BLOCKED.**

The recent implementation work was directionally correct: the project now has explicit request identities, explicit authorization state, bounded physical actions, pending-state preservation, and stronger evidence separation across the six active slices. But the cross-slice audit exposed a more fundamental issue that individual slice audits could not see: **the shared goal namespace and lifecycle-generation semantics are not yet globally coherent.**

The correct next step is therefore **not another vertical implementation**. It is a global invariant repair pass, beginning with numeric goal allocation and active-request supersession, followed by real expiry and normalized reassessment.

No runtime-only behavior is used to clear these source blockers.
