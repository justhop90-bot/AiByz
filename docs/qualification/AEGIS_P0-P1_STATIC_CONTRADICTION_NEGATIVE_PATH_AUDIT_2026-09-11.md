# AEGIS P0/P1 Static Contradiction & Negative-Path Audit — 2026-09-11

## Purpose

This pass attacks the seven previously identified P0/P1 findings **before any target-engine runtime qualification attempt**. It is deliberately adversarial: a finding is considered cleared only when the source contract, writer/reader graph, initialization path, and negative behavior agree. Static inspection does not promote anything to S5.

Target: AoE2DE `101.103.48987.0` / BuildID `24094652` where source files declare that target.

## Verdict

**No P0/P1 finding is promoted to CLEARED by this pass.**

The audit distinguishes four outcomes:

- **CONFIRMED** — contradiction/weakness exists in current source.
- **CONTAINED** — architecture explicitly prevents the failure, but target behavior remains unproven.
- **TESTABLE** — the source defines a negative-path predicate that can be exercised, but runtime evidence is required.
- **BLOCKED** — an upstream unknown prevents meaningful qualification.

The correct conclusion is that the project is ready to move from broad architecture work into **targeted remediation + controlled qualification**, but not to declare runtime success.

---

## Finding P0-1 — Cavalry-response reservation unit-binding gap

**Status: CONFIRMED STATIC DEFECT**

`AEGIS-production-reservation-authority-v0.per` has explicit unit binding in the Military Production grant:

```text
(up-compare-goal aegis-mp-unit == aegis-mp-unit-spearman)
```

The Cavalry Response grant does **not** contain the corresponding `aegis-cr` unit predicate before it grants the spearman resource reservation. It requires CR validity, authorized stage, authorization generation, and request/authorization identity, then writes:

```text
aegis-pr-resource-key = aegis-pr-resource-spearman-line
aegis-pr-unit-line = aegis-pr-unit-spearman-line
```

Therefore the reservation authority can currently convert a valid CR authorization into a spearman reservation without the reservation grant itself proving that CR's requested capability is spearman.

Downstream dispatch does check the resource/unit identity, but that is too late: the reservation has already been granted. The contract's ownership boundary therefore has a missing precondition.

**Required remediation:** add an explicit CR capability/unit identity predicate to the grant rule, or revise the CR contract so the requested unit identity is independently bound and verified. Do not merely add a test that assumes the current behavior is correct.

**Negative cases:**
1. CR authorized for non-spearman capability → reservation must remain FREE.
2. CR authorization identity valid but unit identity absent → reservation must remain FREE.
3. CR unit identity mismatched with spearman resource → reservation must remain FREE.
4. MP and CR simultaneously authorized → exactly one reservation may be granted; loser remains denied/deferred.

No code change is made in this audit because intended CR capability binding must be confirmed by the contract, not guessed from the resource destination.

---

## Finding P0-2 — Reservation negative behavioral coverage is incomplete

**Status: CONFIRMED TEST-COVERAGE GAP**

The reservation source contains useful fail-closed predicates for stale generation, zero expiry token, producer ownership, request identity, authorization identity, and release identity. However, static source inspection does not demonstrate that the complete cross-product of invalid identities is rejected.

Required adversarial matrix:

| Case | Expected result |
|---|---|
| wrong owner | no dispatch / no release credit |
| wrong reservation ID | no release |
| wrong request ID | no dispatch |
| wrong authorization ID | no dispatch |
| wrong authorization generation | stale/release-pending; no physical action |
| wrong resource key | no dispatch |
| wrong unit line | no dispatch |
| invalid producer | no grant |
| duplicate reservation request | no second valid reservation |
| competing MP/CR request | one owner maximum |
| stale reserved reservation | release-pending, never dispatched |
| stale in-flight reservation | release-pending, never credited as success |
| zero expiry token | fail-closed release-pending |
| repeated release | idempotent; no state resurrection |
| released + stale metadata | cannot resurrect reservation |

**Result:** architecture contains many predicates, but this is not the same as executing negative behavioral tests. The test suite must model state transitions, not merely grep for predicates.

---

## Finding P0-3 — First-load initialization is not proven

**Status: CONFIRMED BLOCKER**

The reservation authority's initialization rules require the state to already be `FREE` or `RELEASED` before initializing the rest of the reservation fields. That is a circular assumption about initial engine state.

Likewise, Military Production declares `aegis-mp-unit` and branches on `aegis-mp-unit-spearman`, but its initialization rule does not establish an initial unit selector. The source therefore cannot prove which producer capability is selected on first use.

The correct distinction is:

```text
DECLARED != INITIALIZED != VALIDATED
```

**Required remediation:** define an explicit first-load initialization contract and identify the authoritative writer for every selector/state field that must exist before the first branch can fire.

**Negative cases:**
1. arbitrary/unknown initial selector → no production authorization.
2. arbitrary reservation state → no physical dispatch until canonical initialization occurs.
3. first generation observed → exactly one initialization transition.
4. repeated initialization trigger → no destructive reset of an active valid reservation.

No runtime claim is made until the engine's initial values and rule firing semantics are observed.

---

## Finding P1-4 — Worker-role vector is structurally live but policy-starved

**Status: CONFIRMED STATIC BEHAVIOR**

`AEGIS-worker-role-vector-v0.per` explicitly defines all V0 desired role targets as zero:

```text
aegis-wrv-target-food 0
aegis-wrv-target-wood 0
aegis-wrv-target-gold 0
aegis-wrv-target-stone 0
aegis-wrv-target-builder 0
```

The module computes `desired - observed` and clamps negative deficits to zero. Consequently, absent another policy writer, the normal worker demand vector is zero regardless of the observed worker population.

This is not an engine bug. It is a **policy-input starvation condition**.

Adversarial tests:

1. observed workers > 0 with all targets zero → all deficits must remain zero.
2. external target writer absent → no downstream worker task request may be inferred.
3. target changed to positive value → deficit becomes positive only after a fresh census generation.
4. stale census generation → no new deficit generation.

**Disposition:** retain as explicit V0 qualification fixture, but do not call the civilian worker loop operationally effective until strategic target ownership is supplied and qualified.

---

## Finding P1-5 — `Aegis-execution-final` is not physical execution

**Status: CONFIRMED SEMANTIC BOUNDARY**

`Aegis-execution-final.per` only copies `aegis-commitment-kind` into execution state and marks execution valid. It contains no physical command such as `up-train`, `up-build`, `up-target-objects`, attack-move, stop, or move.

This is not itself a defect. It becomes a defect only if any documentation or integration path treats this module as proof that a physical command was issued.

The source graph confirms the distinction: actual game-facing execution is in bounded adapters such as worker-task command, housing construction, villager production, cavalry response, and the micro physical adapter.

**Negative cases:**
1. commitment becomes valid → execution state may advance, but no physical-success claim is permitted.
2. execution state changes without a physical adapter → no W1/W2 credit.
3. physical command issued elsewhere → execution-final receives no causal credit merely because its state was valid.

**Disposition:** architecture boundary is correct; documentation must continue to prohibit semantic promotion of this skeleton.

---

## Finding P1-6 — Target-runtime evidence remains absent for the first vertical slice

**Status: CONFIRMED QUALIFICATION BLOCKER**

The civilian modules contain enough structure to define a controlled runtime experiment, but the repository still lacks the evidence chain required for S5:

```text
exact target source loaded
→ observation
→ authorization
→ physical request
→ engine acceptance/pending
→ world transition
→ causal attribution
→ reassessment
```

Static source, GitHub Actions, command traces, replay command records, and pending-object observations cannot substitute for that chain.

The first controlled experiment should remain the **Civilian Production Loop**, not military/threat or tactical micro.

Minimum negative runtime cases later required:

- insufficient resource;
- no legal producer;
- duplicate request;
- stale generation;
- authorization expiry;
- command issued but pending absent;
- pending disappears without world transition;
- world delta occurs without request attribution;
- competing producer exists;
- repeated terminal verification.

Until these are observed on the exact target build, civilian modules remain S3/S4 at most.

---

## Finding P1-7 — Repository policy success is not engine qualification

**Status: CONFIRMED GOVERNANCE BOUNDARY**

The policy workflow can establish repository invariants such as candidate-load separation, no XS scope creep, required files, and working-layer markers. It cannot establish that AoE2DE loaded the source, accepted a command, created a pending object, completed a world transition, or attributed that transition causally.

Therefore:

```text
CI PASS ≠ runtime PASS
static test PASS ≠ runtime PASS
source presence ≠ load proof
command issued ≠ accepted
pending ≠ spawned
world delta ≠ causal success
```

No CI result should be used as evidence for S5 or S6.

---

## Cross-finding contradiction sweep

### C1 — Authorization can exist without capability identity

Confirmed in CR reservation grant. This is the most concrete current contract contradiction.

### C2 — Initialization predicates can depend on pre-existing state

Confirmed in reservation authority. This creates a first-load ambiguity.

### C3 — Selector is consumed before local initialization

Confirmed in Military Production for `aegis-mp-unit`.

### C4 — Policy output can be formally valid while operationally zero

Confirmed in Worker Role Vector. This is an intentional V0 policy state, not evidence of a functioning worker economy.

### C5 — Control-plane execution can be mistaken for physical execution

Confirmed as a semantic hazard; source itself contains only state propagation in `Aegis-execution-final`.

### C6 — World evidence can be mistaken for causal evidence

Still explicitly prevented in the stronger military/cavalry contracts, but the causal producer for CR remains external/unqualified.

### C7 — Candidate code can be structurally clean while target ABI remains unknown

Confirmed across numeric channels, timer 42, stock constants, and target-engine command lifecycle.

---

## Negative-path qualification pack

Before runtime promotion, every bounded physical slice should be able to answer these seven questions:

1. **Can it refuse an invalid request?**
2. **Can it refuse stale authorization?**
3. **Can it refuse a duplicate request?**
4. **Can it distinguish issued from accepted/pending?**
5. **Can it distinguish pending disappearance from success?**
6. **Can it reject causal attribution when an alternative producer exists?**
7. **Can it recover without resurrecting stale state?**

If any answer is unknown, the slice cannot advance to S5.

---

## Required remediation order

1. Repair/clarify CR capability-to-resource binding.
2. Build behavioral reservation negative tests covering identity, owner, generation, resource, unit, race, release, and stale-state cases.
3. Establish explicit first-load initialization for reservation state and military selector state.
4. Keep worker-role targets explicitly classified as policy inputs; do not silently invent production targets.
5. Preserve `Aegis-execution-final` as a control-plane state layer; do not convert it into a fake physical authority.
6. Prepare the civilian runtime evidence bundle and negative-path stimulus set.
7. Keep CI/policy evidence in the structural gate only; never promote runtime maturity from it.

## Promotion decision

**S5 target-runtime qualification: BLOCKED.**

**S6 strategic qualification: BLOCKED by S5 absence.**

**Production promotion: NOT AUTHORIZED.**

This pass intentionally makes no runtime claim and does not modify production/runtime source merely to make tests pass.
