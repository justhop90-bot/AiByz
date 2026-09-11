# ACAP v0.1 — Existing AegisProm Implementation / Evidence Gap Audit

**Audit target:** source `AegisProm/` only. Runtime copies are excluded from architectural authority.
**Purpose:** map the normative ACAP v0.1 contract to currently demonstrated native `.per` behavior before implementation changes.
**Audit posture:** evidence first; no promotion of mechanisms merely because filenames or variable names suggest they exist.

## 1. Executive finding

The source tree contains a useful partial anti-cavalry vertical slice, but it does **not** yet satisfy ACAP v0.1.

The strongest existing path is:

```text
world observation
  -> cavalry threat classification
  -> bounded response stage
  -> native up-train spearman-line
  -> pending-object observation
```

The missing or insufficiently proven portions are:

```text
threat
  -> capability demand
  -> verified deficit
  -> independent feasibility decision
  -> strategic authorization
  -> accepted production
  -> completion/capability verification
  -> reassessment
```

The existing `AEGIS-military-production-v0.per` contains a stronger production confirmation attempt than `AEGIS-cavalry-response-v0.per`, but its unit selector is not initialized in the file, and its confirmation is not yet proven to be the authoritative ACAP verification boundary.

## 2. Evidence observed in source

### 2.1 World observation

`AEGIS-foundation.per` samples game time, population, resources, and several unit-line counts on a five-second timer. It writes a generation/cycle and marks the observation valid. The same file records spear, camel, skirmisher, knight-line, and archer-line counts. fileciteturn13file0L2-L2

**ACAP classification:** DIRECT observation evidence.

**Limitation:** this establishes an observation frame, not a strategic threat by itself.

### 2.2 Threat classification

`AEGIS-scouting-threat-v0.per` derives cavalry-related counts using `scout-cavalry-line`, `cavalry-archer-line`, and `knight-line`. It establishes cavalry threat when scout cavalry >= 3, cavalry archers >= 2, or knights >= 2, and raises its confidence state. fileciteturn11file0L2-L2

**ACAP classification:** DIRECT inputs + COMPOSED threat classification.

**Status:** PASS for the bounded threat-establishment portion.

**Gap:** the current model has only `NONE` and `CAVALRY`; it does not yet implement the richer demand semantics of ACAP threat pressure/context modifiers.

### 2.3 Existing cavalry response

`AEGIS-cavalry-response-v0.per` has explicit lifecycle stages `IDLE`, `AUTHORIZED`, `ISSUED`, `PENDING`, and `FAILED`. It moves to `AUTHORIZED` when cavalry threat exists and `can-train spearman-line` is true, then issues `up-train escrow-state c: spearman-line`, moves to issued, and recognizes pending objects. fileciteturn9file0L2-L2

**ACAP classification:** real physical execution endpoint; partial lifecycle state.

**Critical finding:** the file's `AUTHORIZED` state is not yet ACAP strategic authorization. It is a local response-stage label established by threat + `can-train`. That conflates feasibility with authorization.

### 2.4 Military production lifecycle

`AEGIS-military-production-v0.per` defines `AUTHORIZED`, `ISSUED`, `PENDING`, `CONFIRMED`, and `FAILED` stages. It takes a spearman baseline, issues `up-train escrow-state c: spearman-line`, observes pending objects, then observes total spearman count and marks confirmation when observed count exceeds baseline. fileciteturn12file0L2-L2

**ACAP classification:** candidate completion/capability verification evidence.

**Critical finding 1:** `aegis-mp-unit` is declared and compared against `aegis-mp-unit-spearman`, but this source file does not initialize `aegis-mp-unit`. Therefore the production authorization rule is not demonstrated as live solely from this file. fileciteturn12file0L2-L2

**Critical finding 2:** `observed > baseline` proves that the observed total increased; it does not, by itself, prove that the increase was causally attributable to the particular pending request. The attribution requirement of ACAP T13 therefore remains unproven.

## 3. Normative ACAP transition mapping

| ACAP transition | Existing source evidence | Status | Promotion interpretation |
|---|---|---|---|
| T01 NO_DEMAND -> THREAT_ESTABLISHED | scouting threat observation/classification | PASS | Bounded cavalry detection exists |
| T02 THREAT -> DEMAND | no explicit capability-demand state | FAIL | Threat currently jumps toward response |
| T03 DEMAND -> DEFICIT | no explicit required-vs-verified deficit | FAIL | No verified capability deficit calculation |
| T04 DEFICIT -> CLOSED | no ACAP demand closure | FAIL | No demand lifecycle closure |
| T05 DEFICIT -> FEASIBILITY | `can-train` exists at response/production boundary | PARTIAL | Feasibility primitive exists, but not as independent ACAP stage |
| T06 FEASIBILITY -> AUTHORIZATION | local response stage called authorized | FAIL | `can-train` is being treated as authorization |
| T07 FEASIBILITY -> DEFERRED | no explicit bounded defer state | FAIL | No semantic deferral state |
| T08 AUTHORIZATION -> REQUESTED | real `up-train` exists | PASS WITH CONDITIONS | Physical execution exists, authority boundary must be repaired |
| T09 REQUESTED -> PENDING | `up-pending-objects` path exists | PASS WITH CONDITIONS | Acceptance/pending semantics need explicit evidence boundary |
| T10 REQUESTED -> FAILED | pending <= 0 after attempt path exists | PARTIAL | Failure signal is useful but not a general rejection proof |
| T11 PENDING -> VERIFICATION | pending -> observed count path exists in military production | PARTIAL | Verification candidate exists |
| T12 PENDING -> COMPLETION_UNVERIFIED | no explicit uncertainty state | FAIL | Unknown is not represented distinctly |
| T13 VERIFICATION -> CAPABILITY_VERIFIED | observed count > baseline | PARTIAL | World-state increase is observed, causal attribution remains unproven |
| T14 VERIFIED -> REASSESSMENT | no explicit closed-loop reassessment state | FAIL | Verification does not feed a normative ACAP reassessment |
| T15 REASSESSMENT -> CLOSED | absent | FAIL | No verified closure |
| T16 REASSESSMENT -> DEFICIT | absent | FAIL | No recalculated deficit |
| T17 REASSESSMENT -> THREAT | threat can be recomputed by generation | PARTIAL | Observation loop exists, but no ACAP invalidation semantics |
| T18 CLOSED -> NO_DEMAND | absent | FAIL | No demand lifecycle endpoint |
| T19 AUTHORIZATION -> EXPIRED | no authorization expiry | FAIL | Existing authorization is not time-bounded |
| T20 PENDING -> FAILED | bounded failure exists in production file | PARTIAL | Needs clean failure ownership and recovery path |

## 4. Ownership audit

### Threat / Intelligence

**Existing:** `AEGIS-scouting-threat-v0.per` owns the threat facts it creates. This is the correct direction.

**Required next step:** keep threat classification separate from capability demand.

### Capability / Reasoning

**Existing:** no authoritative ACAP demand/deficit owner has been demonstrated.

**Required next step:** create the smallest semantic layer necessary to own:

```text
required_capability
verified_current_capability
committed_capability
available_capability
deficit
```

Do not create a giant military optimizer for v0.1.

### Feasibility / Production

**Existing:** `can-train` is demonstrated.

**Required next step:** treat it as a feasibility predicate, not authority.

### Strategic Authority

**Existing:** no clean ACAP authority boundary is demonstrated.

**Required next step:** create an explicit authorization state that is downstream of deficit and feasibility.

### Execution

**Existing:** `up-train escrow-state c: spearman-line` is a genuine physical execution action. fileciteturn9file0L2-L2

**Required next step:** preserve this endpoint rather than routing it through a fictitious execution service.

### Verification

**Existing:** military production observes total spearman count and compares it to a baseline. fileciteturn12file0L2-L2

**Required next step:** establish whether this can be made authoritative without inventing causal attribution the engine cannot prove.

## 5. Immediate implementation blockers

### B1 — Authorization is semantically overloaded

Current cavalry response uses:

```text
cavalry threat
+ can-train spearman-line
-> stage-authorized
```

ACAP requires:

```text
threat
-> demand
-> deficit
-> feasibility
-> strategic authorization
-> execution
```

`can-train` MUST NOT be the authorization boundary.

### B2 — No demand/deficit state

There is currently no demonstrated calculation equivalent to:

```text
required_capability - verified_available_capability
```

Without this, production is a threat reaction rather than capability management.

### B3 — Military production selector is not initialized locally

`aegis-mp-unit` is declared and tested, but the source file shown does not set it. This must be resolved by tracing its actual writer before changing it. Do not simply add an initialization until ownership is established.

### B4 — Verification attribution is incomplete

`observed spearmen > baseline` is valuable direct world-state evidence, but it is not automatically proof that the observed increase came from this specific request. A concurrent or unrelated spearman creation could produce the same observation.

### B5 — Unknown completion is not a first-class state

The current production lifecycle has pending and failed/confirmed, but not a normative `COMPLETION_UNVERIFIED` state. ACAP requires preservation of uncertainty.

### B6 — No authorization expiry

A production authorization currently has no demonstrated expiration/invalidation semantics. This is required to prevent stale tactical commands surviving material state changes.

### B7 — No closed-loop reassessment

There is no demonstrated path:

```text
CAPABILITY_VERIFIED
-> REASSESSMENT
-> current threat + current capability
-> new deficit
-> close or produce again
```

This is the largest strategic gap after demand/deficit ownership.

## 6. What should NOT be changed yet

Do not:

1. Rewrite the threat detector merely to make it look more sophisticated.
2. Replace `spearman-line` with a different unit without behavioral evidence.
3. Route physical production through `Aegis-execution-final.per` merely because its filename says execution.
4. Treat `Aegis-verification-final.per` as world-state verification without evidence.
5. Introduce a universal composition optimizer.
6. invent a causal completion signal unsupported by the engine.
7. copy AI(HD) source code literally.
8. import ADprom or byzwarcouncil as architectural authority.
9. promote runtime copies over source `AegisProm`.

## 7. Recommended implementation order

The minimum safe order is:

```text
1. Preserve existing threat detector.
2. Establish ACAP demand owner.
3. Establish required capability.
4. Establish verified-current capability.
5. Calculate non-negative deficit.
6. Establish independent feasibility state.
7. Establish bounded authorization with expiry.
8. Consume authorization at existing physical up-train endpoint.
9. Preserve request/acceptance/pending distinctions.
10. Establish the strongest world-state completion evidence the engine actually supports.
11. Credit only verified capability.
12. Reassess from current threat + current verified capability.
13. Demonstrate closure and repeat-demand behavior.
14. Only then promote the vertical slice.
```

## 8. Promotion gate

The slice passes only if an auditor can trace one complete successful lifecycle and at least one failure/uncertainty lifecycle without semantic shortcuts.

Successful path:

```text
observation
-> threat
-> demand
-> deficit
-> feasibility
-> authorization
-> request
-> accepted/pending
-> verified capability
-> reassessment
-> closed OR renewed deficit
```

Failure/uncertainty path:

```text
authorization expiry
-> reassessment

OR

production rejection/failure
-> no capability credit
-> reassessment

OR

completion unverified
-> uncertainty preserved
-> reassessment
```

## 9. Final audit verdict

**Current ACAP status: NOT PROMOTED.**

The existing AegisProm source has enough native behavior to justify continuing the slice, especially the threat observation and physical `up-train spearman-line` endpoint. It does not yet justify claiming a complete capability contract.

The next code change should therefore be a **small, evidence-driven demand/deficit/authorization layer**, not a rewrite of the existing tactical production endpoint.
