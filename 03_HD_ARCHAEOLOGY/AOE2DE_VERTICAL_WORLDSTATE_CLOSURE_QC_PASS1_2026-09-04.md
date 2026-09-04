# Pass 13 QC — Vertical World-State Closure

**Date:** 2026-09-04
**Target:** `AOE2DE_VERTICAL_WORLDSTATE_CLOSURE_PASS13_2026-09-04.md`
**Mode:** adversarial source/evidence QC
**Verdict:** ACCEPT WITH CORRECTIONS — WORKING CANON, NOT EMPIRICALLY CLOSED

## 1. Scope audit

Pass 13 correctly changes the research question from command reachability to postcondition realization.

The four selected vertical traces are appropriate:

- resource reservation → research;
- threat aggregate → camel capability;
- attack threat → retreat/recovery;
- land-nomad geometry → relocation.

No scenario-loading automation was required. This is consistent with the project's current decision to shelve automated scenario testing.

## 2. Evidence-grade audit

### QC13-01 — Source-package provenance

**Severity: HIGH**

The artifact cites recovered source behavior but does not embed cryptographic provenance for every source excerpt.

**Correction:** when promoted to canonical status, attach source-package filename, hash, extraction identity, and exact line anchor for every critical excerpt.

### QC13-02 — Research chain

**Status: PASS**

The distinction among availability, escrow feasibility, command issuance, and completion is precise and valuable.

`research` must not be treated as completion.

### QC13-03 — Resource opportunity cost

**Status: PASS WITH BOUNDARY**

Resource protection is source-supported. Formal scalar opportunity-cost optimization remains unproven.

### QC13-04 — Camel chain

**Status: PASS WITH BOUNDARY**

The artifact correctly treats `cavarchers` as a weighted threat aggregate and `traincamel` as response control.

It correctly refuses to call the chain a complete composition optimizer.

### QC13-05 — Camel world closure

**Status: OPEN**

No evidence yet proves that the `train` command results in completed camel stock under a controlled observation.

### QC13-06 — Retreat chain

**Status: PASS WITH BOUNDARY**

The artifact distinguishes retreat-state control from physical movement.

`up-retreat-now` is not treated as proof of successful physical retreat.

### QC13-07 — Restart chain

**Status: PASS WITH BOUNDARY**

Attack-group reset and timer re-enablement are correctly identified as controller preparation rather than renewed attack success.

### QC13-08 — Land-nomad chain

**Status: PASS WITH BOUNDARY**

The local algorithmic objective is correctly identified as maximum pair distance.

The higher-level strategic purpose remains unresolved.

### QC13-09 — 505 indexing

**Status: OPEN**

The artifact explicitly preserves the indexing uncertainty rather than asserting an unsupported one-based/zero-based explanation.

### QC13-10 — World-state hierarchy

**Status: STRENGTH**

The W0–W4 hierarchy is a useful addition:

`command → pending → world state → operational capability → strategic effect`.

It should become canonical for later empirical passes.

## 3. Major methodological finding

Pass 13 demonstrates that source archaeology has reached a natural boundary.

Source can establish:

`decision representation → eligibility → control mutation → command invocation`.

It generally cannot establish, by itself:

`command invocation → physical game-state realization → strategic consequence`.

That second half requires runtime/replay evidence or stronger native-engine evidence.

This is not a failure of the archaeology. It is the evidence boundary.

## 4. Empirical frontier

The next pass should not attempt to reopen the failed scenario-loader workflow.

Instead establish a small observation protocol around stable game surfaces:

1. identify one source behavior;
2. establish its precondition;
3. observe relevant game state before activation;
4. trigger or capture the control event;
5. observe pending/queue state;
6. observe realized state;
7. record timing;
8. record whether the intended capability became operational;
9. record strategic effect only when directly observable;
10. preserve failure cases.

## 5. Closure score

| Layer | Current strength | Status |
|---|---:|---|
| Source/control provenance | High | STRONG |
| State-channel causality | High | STRONG |
| Command reachability | High | STRONG |
| Pending-state proof | Medium | PARTIAL |
| World-state realization | Low | OPEN |
| Operational capability | Low | OPEN |
| Strategic effect | Low | OPEN |

## 6. Verdict

**ACCEPT WITH CORRECTIONS.**

Pass 13 is a valid Layer-2 working-canon artifact and materially improves epistemic discipline. It does not close world-state causality yet.

The next pass should build the empirical observation pack, not another abstract graph.
