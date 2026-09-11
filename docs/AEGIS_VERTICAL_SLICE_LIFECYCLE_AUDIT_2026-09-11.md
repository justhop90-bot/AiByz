# AEGIS Vertical-Slice Lifecycle Audit — 2026-09-11

**Status:** NORMATIVE AUDIT / IMPLEMENTATION GAP RECORD  
**Authority:** `docs/AEGIS_CANONICAL_LIFECYCLE_CONTRACT_V0_1.md`  
**Concrete contract authority:** `schemas/AEGIS-VERTICAL-SLICE-CONTRACTS-1.0.json`  
**Scope:** all seven registered AEGIS vertical slices, including the blocked military-production candidate  
**Method:** compare the canonical lifecycle semantics against the authoritative `main/AegisProm` source and the existing registry/qualification framework. Runtime-generation behavior is not promoted into source architecture by this audit.

## 1. Executive verdict

The seven registered slices are **not yet lifecycle-conformant implementations**. Their registry contracts describe the intended lifecycle, but the source `.per` implementations currently realize only portions of that contract.

The strongest recurring gap is **authorization identity and ownership**. Several source modules enter an `authorized` stage directly from demand/feasibility predicates and then issue a physical command without a separately represented authorization record containing request identity, generation, owner, and expiry. The registry can describe the missing semantic stage, but the source does not yet implement the full boundary.

The second recurring gap is **reassessment**. Several modules terminate by invalidating their own state rather than publishing a consequential outcome to a canonical reassessment owner.

The third recurring gap is **causal verification**. Count increases and pending-object observations establish useful world evidence, but do not necessarily establish that the particular AEGIS request caused the observed transition.

The fourth recurring gap is **request identity**. Generation and attempt counters provide partial duplicate protection, but they are not equivalent to a stable request identity carried from authorization through physical action, pending state, and verification.

**No `.per` source implementation is promoted by this audit.** The purpose is to make the missing contract explicit before implementation work begins.

## 2. Severity model

- **P0 — architectural blocker:** current implementation violates a mandatory lifecycle invariant or cannot safely represent the required state boundary.
- **P1 — qualification blocker:** capability is physically present but the lifecycle cannot yet be promoted.
- **P2 — evidence gap:** behavior may be real, but required evidence or causal attribution is incomplete.
- **P3 — structural improvement:** contract metadata or implementation clarity is incomplete but does not by itself establish failure.

## 3. Cross-slice result matrix

| Slice | Preconditions | Ownership | Authorization | Physical action | Evidence / verification | Postcondition | Failure | Expiry | Idempotency | Reassessment | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `worker_economy` | **PARTIAL** | **PARTIAL** | **MISSING/CONFLATED** | **PRESENT** | **PARTIAL** | **MISSING** | **PARTIAL** | **MISSING** | **PARTIAL** | **MISSING** | P1/P2 blocked |
| `villager_production` | **PARTIAL** | **PARTIAL** | **CONFLATED** | **PRESENT** | **PARTIAL** | **PARTIAL** | **PRESENT** | **MISSING** | **PARTIAL** | **MISSING** | P1/P2 blocked |
| `housing` | **PARTIAL** | **PARTIAL** | **CONFLATED** | **PRESENT** | **PARTIAL** | **PARTIAL** | **PRESENT** | **MISSING** | **PARTIAL** | **MISSING** | P1/P2 blocked |
| `age_transition` | **PRESENT/PARTIAL** | **PARTIAL** | **CONFLATED** | **PRESENT** | **PRESENT for age transition, attribution incomplete** | **PARTIAL** | **PRESENT** | **MISSING** | **PARTIAL** | **MISSING** | P1/P2 blocked |
| `anti_cavalry` | **PARTIAL** | **PARTIAL** | **PRESENT AS STAGE, NOT FULL IDENTITY** | **PRESENT** | **PARTIAL** | **MISSING** | **PRESENT** | **MISSING** | **PARTIAL** | **MISSING** | P0/P1 blocked |
| `tactical_micro` | **PARTIAL** | **DISTRIBUTED** | **PRESENT IN BRIDGE** | **PRESENT** | **MISSING COMPLETE WORLD PROOF** | **MISSING** | **PARTIAL** | **MISSING** | **PARTIAL** | **PRESENT AS LOCAL STATE ONLY** | P0/P1 blocked |
| `military_production` | **PARTIAL** | **PARTIAL** | **CONFLATED** | **PRESENT** | **PARTIAL** | **MISSING** | **PRESENT** | **MISSING** | **PARTIAL** | **MISSING** | P0/P1 blocked |

The terms above mean implementation status, not registry status. The registry correctly retains six qualification slices and one blocked candidate; this audit does not change that classification.

## 4. Canonical field audit

### 4.1 Preconditions

**Required:** current generation, expected source state, required evidence, valid authorization where required, request not already satisfied, and no duplicate pending request.

**Finding:** every slice has some meaningful admission predicates, but none consistently represents the complete canonical precondition set as an explicit contract boundary.

- Worker economy checks selected worker, serviceability, freshness of worker-task generation, and resource relation. This is useful feasibility/admission logic, but it does not independently represent authorization or request identity.
- Villager production checks qualified civilian demand, `can-train`, town center availability, and bounded attempts.
- Housing checks qualified civilian demand, fresh generation, and `can-build`.
- Age transition checks current age, `can-research`, and resource thresholds.
- Anti-cavalry checks cavalry threat and `can-train`.
- Tactical micro checks intent, target/fallback readiness, governor command, execution authorization, and bounded attempts.
- Military production checks cavalry threat, selector, baseline, and `can-train`, but its selector is not initialized in authoritative source.

**Gap:** preconditions are generally embedded inside rules rather than normalized into an auditable request contract. This is acceptable as implementation style only if the semantic distinctions remain explicit. At present they do not fully remain explicit.

### 4.2 Ownership

The canonical contract requires one semantic owner for each authoritative state.

**Finding:** the registry names owners, but several source implementations distribute a mutable lifecycle across modules without an explicit ownership declaration at the source boundary.

- Worker economy crosses census, role vector, demand, arbitration, selection, serviceability, command, verification, productivity, and recovery.
- Tactical micro is especially distributed: micro control, targeting, geometry, groups, governor, execution bridge, physical adapter, and verification all participate in mutable lifecycle state.
- Anti-cavalry currently contains its own authorization/physical production lifecycle; later runtime work introduced an explicit `aegis-cr-*` authorization boundary, but that runtime generation is not source authority.

**Gap:** semantic ownership exists in the registry but is not yet enforced as a source-level single-writer rule.

### 4.3 Authorization

This is the most important common defect.

The canonical contract requires authorization to identify at least request, capability/action, generation, owner, creation sequence/time where available, and expiry condition.

**Worker economy:** the command module directly changes its stage to `authorized` when upstream selection/serviceability conditions hold. There is no distinct authorization identity or expiry field. **P0/P1 gap.**

**Villager production:** the first rule moves directly from qualified civilian demand to `authorized`; the next rule uses `can-train` before issuing `up-train villager`. This is a bounded admission mechanism, but authorization is conflated with admission and has no request identity or expiry. **P1 gap.**

**Housing:** baseline capture creates an `authorized` stage, and `can-build house` gates the physical command. Again, authorization is represented as a stage rather than an identifiable authorization record. **P1 gap.**

**Age transition:** affordability and `can-research` establish the authorized stage; physical research then checks `can-research` again. This is useful fail-closed behavior, but not a complete authorization object. **P1 gap.**

**Anti-cavalry:** explicit `authorized` state exists and the physical command is separated from threat classification, but request identity and expiry are absent. **P1 gap.**

**Tactical micro:** execution authority is materially better separated: the physical adapter requires `aegis-me-authorized == 1`. However, no stable request identity/expiry is carried into the physical adapter. **P1 gap.**

**Military production:** source uses its own `authorized` stage and `can-train`; no request identity/expiry. In addition, `aegis-mp-unit` is declared but uninitialized in source. **P0/P1 gap.**

### 4.4 Physical action

All seven registered slices have a genuine or candidate physical endpoint:

- worker economy: `up-target-objects` for wood/gold/stone;
- villager production: `up-train ... villager`;
- housing: `build house`;
- age transition: `research castle-age`;
- anti-cavalry: `up-train ... spearman-line`;
- tactical micro: attack-move/stop/move physical adapter;
- military production: `up-train ... spearman-line`.

This is the strongest common part of the architecture.

**Invariant:** physical dispatch is not completion. The source comments and lifecycle stages generally recognize this distinction.

### 4.5 Engine acceptance / pending

- Worker economy: source has a `waiting` stage but no demonstrated rule that converts an issued worker task into engine-accepted pending evidence. **P1/P2.**
- Villager production: explicit pending observation exists through `up-pending-objects c: villager >= 1`. **P2:** pending is not completion.
- Housing: explicit pending house observation exists. **P2:** foundation/pending and completed house remain distinct, and count attribution is ambiguous under concurrency.
- Age transition: no explicit pending research state. The engine may expose research state, but this source does not preserve it. Because age transition is observable directly, this is not necessarily a defect in the final capability, but the contract must document the omission as an engine-specific semantic choice. **P2/P3.**
- Anti-cavalry: explicit pending spearman observation exists. **P2:** no causal completion proof.
- Tactical micro: no generic engine-accepted pending stage. For tactical commands, a pending queue may not be the correct semantic intermediate, but the source must still preserve an explicit `issued → world observation` distinction. Current implementation jumps from issued to local reassessment. **P1.**
- Military production: explicit pending state exists. **P2.**

### 4.6 World-state evidence and causal verification

The canonical contract requires independent world-state evidence and forbids silently equating it with causal attribution.

**Worker economy:** task verification/productivity observation exists as a concept, but persistent worker identity is not preserved. A later task observation therefore cannot automatically prove that the selected worker executed the command. **P2.**

**Villager production:** pending is observed; later census increase is useful but can be confounded by concurrent villager production. **P2.**

**Housing:** completed-house count increasing above baseline is useful direct world evidence but does not prove that this request caused the increment if another house could complete concurrently. **P2.**

**Age transition:** `current-age >= castle-age` is strong direct world-state evidence for the age transition itself. Attribution to this particular research request remains weaker if another mechanism could cause the transition. **P2.**

**Anti-cavalry:** pending spearman establishes an intermediate state; the source does not independently establish a completed spearman increment attributable to the request. **P1/P2.**

**Tactical micro:** the physical adapter explicitly refuses to infer completion from dispatch, but the verification chain does not yet establish a complete command-caused-world-transition proof. **P0/P1.**

**Military production:** baseline-plus-observed count is useful, but `observed > baseline` does not establish causal attribution to the specific production request. **P1/P2.**

### 4.7 Postconditions

The canonical contract requires declared destination state and required state mutations after successful transition.

**Finding:** source modules generally mutate a stage and sometimes clear `valid` or consume demand, but do not consistently expose a normative postcondition that can be independently audited.

The most serious example is demand consumption:

```text
villager production: demand is consumed when pending is observed
housing: demand is consumed when house count exceeds baseline
```

Consumption is a state mutation, not proof of strategic success.

**Action:** postconditions need to be represented in the machine-readable contract, not inferred from arbitrary `set-goal` operations.

### 4.8 Failure

Failure handling is comparatively mature but inconsistent.

- Worker economy explicitly fails the food branch because no physical food adapter exists.
- Villager production fails closed after bounded attempts with no pending object.
- Housing has `cannot-build` and `pending-lost` failure states.
- Age transition fails when the bounded research attempt does not result in an age change.
- Anti-cavalry fails when issuance is followed by no pending object.
- Tactical micro defines no-target and dispatch failure classes, but the physical adapter does not yet demonstrate a complete failure observation path.
- Military production fails when pending is absent after issuance.

**Gap:** failure often invalidates the local lifecycle but does not publish a canonical failure outcome to a reassessment owner. This makes recovery an external assumption rather than a complete slice property.

### 4.9 Expiry

**Finding: universal gap.** None of the seven authoritative source implementations has a complete authorization expiry mechanism carrying a request-specific expiry condition.

Generation freshness is not the same thing as authorization expiry.

The validator can reject an expired `expires_at` field in a trace, but the source `.per` modules do not consistently generate or enforce such an authorization boundary.

**P0/P1 architectural work item:** define the smallest pure-`.per` representation of authorization validity that can be proven on the target engine. Do not simulate wall-clock expiry with an unproven unit or sequence semantic.

### 4.10 Idempotency

Current source uses several partial mechanisms:

- generation mismatch gates admission;
- attempt counters bound physical commands;
- `valid` gates local lifecycle execution;
- tactical adapter requires `attempts < 1`.

These are useful and should be preserved.

**Contradiction:** canonical idempotency is request-identity based, while source idempotency is primarily generation/attempt based. A generation can identify a new demand publication without uniquely identifying a physical request.

**Required improvement:** carry stable request identity through authorization → physical request → pending → verification, while retaining bounded attempt counters as a secondary safety mechanism.

### 4.11 Reassessment

**Finding: major universal gap.**

The registry requires terminal `REASSESS`, and the canonical lifecycle makes reassessment mandatory after consequential outcomes. The source implementations commonly terminate by setting `valid = 0` or moving to a local `reassess` stage, but do not consistently publish a new world-model observation/reassessment generation.

Tactical micro is closest because its physical adapter has an explicit local `stage-reassess`, but that remains local state, not proof of a cross-slice reassessment boundary.

The other production slices often rely on a later generation to re-admit the capability. That is a useful mechanism, but it is not equivalent to an explicit canonical reassessment event.

**P0/P1 work item:** establish a common reassessment publication/consumption contract without turning the system into a monolithic controller.

## 5. Contradictions between registry and implementation

### C1 — Registry says `AUTHORIZATION`; source often implements admission

The registry correctly separates `FEASIBILITY → AUTHORIZATION → PHYSICAL_REQUEST`. Several source modules collapse authorization into a local stage transition based on feasibility predicates.

**Resolution:** retain the registry contract; do not weaken the contract to match current source. The source must eventually conform.

### C2 — Registry requires terminal `REASSESS`; source often invalidates instead

The validator now enforces terminal `REASSESS` in traces, but source lifecycle code frequently ends by clearing `valid` or setting a local terminal state.

**Resolution:** source needs an explicit reassessment publication path. Do not remove the validator gate.

### C3 — Registry requires request identity for pending/physical lifecycle; source uses generation/attempts

Generation and attempts are safety mechanisms but are not a complete request identity.

**Resolution:** introduce request identity at the lifecycle boundary before qualification. Do not treat generation as a substitute.

### C4 — Registry's `qualified` concept is stronger than current source evidence

The validator correctly separates `contract_valid`, `promotion_eligible`, and `qualified`. The source does not yet satisfy the world-state/cause requirements for several slices.

**Resolution:** preserve the stricter promotion gate.

### C5 — Military production is registry-blocked while runtime contains an initializer

Authoritative source declares `aegis-mp-unit` without initialization. Runtime contains an intentional initializer, but runtime is not source authority.

**Resolution:** retain `CANDIDATE_BLOCKED`. Resolve ownership/source initialization only after the runtime generation is reconciled deliberately.

## 6. Slice-specific action registers

### Worker economy — P1

1. Supply a real positive demand writer without changing the current zero-target finding merely to make the test pass.
2. Introduce stable request identity.
3. Separate authorization from admission.
4. Preserve selected worker/source identity where engine semantics permit.
5. Establish issued → engine/task-state evidence.
6. Establish failure → recovery → reassess.
7. Keep productivity separate from task-state verification.

### Villager production — P1/P2

1. Preserve current real `up-train villager` endpoint.
2. Add explicit request/authorization identity.
3. Preserve pending as queue evidence.
4. Establish completion evidence and causal attribution, or explicitly preserve `COMPLETION_UNVERIFIED`.
5. Stop treating demand consumption as completion.
6. Publish failure/success into reassessment.

### Housing — P1/P2

1. Preserve baseline-before-command logic.
2. Make site/placement qualification explicit if the engine permits it.
3. Preserve pending/foundation distinction.
4. Strengthen completion attribution.
5. Add request identity and authorization expiry.
6. Publish failed/pending-lost and confirmed outcomes to reassessment.

### Age transition — P1/P2

1. Replace unverified world-model age initialization with a verified observation boundary where possible.
2. Preserve direct `current-age` verification.
3. Separate feasibility/authorization from research issuance.
4. Decide, with engine evidence, whether research pending must be represented or whether direct transition observation is sufficient.
5. Add request identity/expiry and explicit reassessment.

### Anti-cavalry / ACAP — P0/P1

1. Preserve the bounded cavalry detector and physical spearman endpoint.
2. Implement ACAP authorization as a real boundary, not merely a local stage.
3. Carry request identity through spearman request/pending/verification.
4. Establish attributable completion/capability evidence.
5. Implement expiry and close/renew semantics.
6. Publish capability outcome to reassessment.
7. Keep the runtime `aegis-cr-*` generation as experimental evidence until deliberately reconciled with source.

### Tactical micro — P0/P1

1. Preserve the physical adapter isolation.
2. Explicitly define ownership of mutable micro lifecycle state.
3. Carry request/authorization identity into physical dispatch.
4. Establish a real post-dispatch world observation path.
5. Distinguish command issued from tactical effect.
6. Preserve no-target/failed/unknown outcomes.
7. Convert local reassess state into a genuine cross-slice reassessment boundary.

### Military production — P0/P1 / BLOCKED

1. Do not initialize `aegis-mp-unit` merely to clear the blocker.
2. Reconcile source ownership against the intentional runtime initializer generation.
3. Keep the candidate blocked until selector ownership is resolved.
4. Preserve pending and baseline evidence.
5. Add request identity, authorization expiry, causal verification, and reassessment before promotion.

## 7. What should NOT be changed

The audit deliberately does **not** recommend:

- copying runtime files into `AegisProm` wholesale;
- reviving ADProm or byzwarcouncil;
- introducing XS;
- resurrecting the retired scenario loader;
- weakening the registry to match incomplete source;
- declaring command issuance to be success;
- declaring count increase to be causal proof without ruling out concurrent causes;
- replacing generation/attempt safety mechanisms before a better mechanism is proven;
- creating disposable runtime probes merely to manufacture qualification evidence.

## 8. Canonical implementation order

The evidence-driven order is now:

```text
1. Canonical lifecycle contract
       ↓
2. Request identity + authorization boundary
       ↓
3. Explicit expiry semantics
       ↓
4. Idempotent physical request ownership
       ↓
5. Pending/engine acceptance identity
       ↓
6. World-state verification
       ↓
7. Causal attribution where required
       ↓
8. Failure/recovery publication
       ↓
9. Reassessment boundary
       ↓
10. Cross-slice qualification
       ↓
11. Strategic integration
```

This order prevents the common failure mode of building more strategic policy on top of an unproven execution contract.

## 9. Final determination

**Current state:** AEGIS has multiple real engine-facing vertical capabilities, but none should be represented as fully conformant to the canonical lifecycle contract yet.

The architecture is therefore best classified as:

> **PHYSICAL CAPABILITY PRESENT; LIFECYCLE CONTRACT PARTIALLY IMPLEMENTED; QUALIFICATION BLOCKED BY AUTHORIZATION IDENTITY, EXPIRY, CAUSAL VERIFICATION, AND REASSESSMENT GAPS.**

The registry remains the contract authority, the canonical lifecycle document remains the cross-slice semantic authority, and this audit becomes the implementation-gap authority for the seven registered slices.
