# AEGIS Layer 3 — Pass 90 State ABI Registry

Date: 2026-09-04
Status: DESIGN CONTRACT; allocation not yet collision-cleared.

## 1. ABI rule

The AEGIS state ABI is schema-typed rather than language-level typed. Each field must have one channel, one owner, explicit writers/readers, legal values, sentinel/zero meaning, initialization, invalidation, stale protection, and build/profile scope.

Authority classes:
- ENGINE_AUTHORITATIVE — engine observation is source of truth.
- AEGIS_AUTHORITATIVE — AEGIS controller state is source of truth.
- DERIVED_CACHE — recomputable; never authoritative.
- OBSERVATIONAL — diagnostic/evidence only.

## 2. Minimal Cavalry Threat Containment ABI

The first vertical slice uses only the minimum fields necessary to demonstrate the full decision-to-verification chain. Numeric IDs below are symbolic names, not allocated goal numbers.

| Field | Channel | Authority | Owner | Writers | Readers | Legal values / sentinel | Lifecycle |
|---|---|---|---|---|---|---|---|
| `OBS.ENEMY_CAVALRY` | goal | ENGINE_AUTHORITATIVE | Intel | Intel sensor | Threat controller | >=0; 0=no measured cavalry | refresh every cycle |
| `OBS.ENEMY_CAVALRY_AGE` | goal | AEGIS_AUTHORITATIVE | Intel | Intel | stale detector | >=0 | generation/age update |
| `THREAT.CAVALRY_ACTIVE` | flag | DERIVED_CACHE | Threat | Threat | planner | 0/1 | recomputed from valid observation |
| `CAP.CAMEL_CURRENT` | goal | ENGINE_AUTHORITATIVE | Capability | Capability sensor | deficit controller | >=0 | refresh |
| `CAP.CAMEL_REQUIRED` | goal | AEGIS_AUTHORITATIVE | Capability | policy | deficit controller | >=0 | policy update |
| `CAP.CAMEL_DEFICIT` | goal | DERIVED_CACHE | Capability | deficit controller | candidate selector | >=0 | `max(0, required-current)` |
| `CAND.PRODUCER` | goal | AEGIS_AUTHORITATIVE | Candidate | producer selector | commitment/execution | producer ID or NONE | selected then invalidated/replaced |
| `CAND.STATUS` | flag/goal | AEGIS_AUTHORITATIVE | Candidate | selector/controller | executor | enumerated state | lifecycle-bound |
| `COMMIT.VALID` | flag | AEGIS_AUTHORITATIVE | Commitment | commitment controller | all side-effect rules | 0/1 | publish/invalidate |
| `COMMIT.OWNER` | goal | AEGIS_AUTHORITATIVE | Commitment | commitment controller | executor/recovery | owner enum or NONE | exclusive by contract |
| `COMMIT.GEN` | goal | AEGIS_AUTHORITATIVE | Commitment | commitment controller | delayed operations | generation | increments on new commitment |
| `COMMIT.STAGE` | goal | AEGIS_AUTHORITATIVE | Commitment | controller | command gates | finite stage enum | transition table constrained |
| `EXEC.STAGE` | goal | AEGIS_AUTHORITATIVE | Executor | executor | verification/recovery | finite stage enum | derived only where specified |
| `EXEC.EXPECTED_GEN` | goal | AEGIS_AUTHORITATIVE | Executor | executor | command/recovery | generation | must match current commitment |
| `RES.RESERVED` | goal | AEGIS_AUTHORITATIVE | Resource | resource controller | candidate gates | >=0 | reserve/release |
| `RES.DISCRETIONARY` | goal | DERIVED_CACHE | Resource | resource sensor | candidate scoring | >=0 | `max(0, actual-reserved)` |
| `ARB.EPOCH` | goal | AEGIS_AUTHORITATIVE | Arbitration | arbiter | dirty/event consumers | generation/epoch | authoritative event version |
| `ARB.DIRTY` | flag | DERIVED_CACHE | Arbitration | arbiter | optimization consumers | 0/1 | optimization only; cannot replace epoch |
| `VERIFY.LEVEL` | goal | OBSERVATIONAL | Verification | verifier | controller/reporter | V0–V8 | monotone within attempt unless reset |

## 3. State publication contract

For multi-field records:

`VALID=0 → populate fields → write generation → write owner → write remaining fields → VALID=1`

Readers must guard `VALID=1`, expected owner, and expected generation before using the record. This is a publication protocol, not a claim of runtime atomicity.

## 4. Generation contract

A new commitment increments `COMMIT.GEN`. Any delayed operation carries `EXPECTED_GEN`. It may mutate or execute only when:

`COMMIT.VALID=1 AND COMMIT.OWNER=EXPECTED_OWNER AND COMMIT.GEN=EXPECTED_GEN`

The implementation must define zero, wraparound, maximum representable generation, and comparison semantics before coding.

## 5. Resource invariant

`RES.RESERVED >= 0`

`RES.DISCRETIONARY = max(0, ACTUAL - RESERVED)`

If actual resources fall below reserved resources, discretionary spending is zero and the recovery/arbitration controller must decide whether to retain, repair, or release the commitment.

## 6. ABI allocation rule

Do **not** allocate a blanket `G0–G511` block. Official evidence shows strategic numbers reached 511, while a later official update preview raised available goals from 512 to 16000. Therefore goal IDs and SN IDs require separate namespaces and a collision audit against every imported constant and legacy package. citeturn0search1turn1search2

The first implementation should allocate only the minimal Cavalry Slice fields after the collision audit passes.
