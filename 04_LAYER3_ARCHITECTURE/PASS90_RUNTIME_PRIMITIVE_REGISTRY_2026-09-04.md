# AEGIS Layer 3 — Pass 90 Runtime Primitive Registry

Date: 2026-09-04
Status: ARCHITECTURE / NO RUNTIME CLAIM
Scope: AoE2:DE `.per` runtime only; XS excluded.

## 1. Purpose

This registry is the source-of-truth boundary between AEGIS operations and realizable AoE2:DE scripting primitives. A primitive is not implementation-ready merely because documentation names it: engine support, validator support, project support, and runtime validation are separate statuses.

## 2. Evidence grades

- E0 — direct engine/documentation evidence.
- E1 — strong operational inference from multiple artifacts.
- E2 — AEGIS-designed abstraction or composition.
- E3 — hypothesis/open.

Validation states: DOCUMENTED → ARCHAEOLOGICALLY_SUPPORTED → IMPLEMENTED → RUNTIME_VALIDATED → REPLAY_CORROBORATED → BATTLEFIELD_VALIDATED.

## 3. Registry

| ID | Primitive | Inputs / state | Runtime role | Engine evidence | Validator | Project status | Limits |
|---|---|---|---|---|---|---|---|
| RP-01 | `goal-read/write` | goal, integer | scalar persistent state | E0/E1 | must be audited | design-approved | legal range is build/profile dependent; do not assume legacy 0–511 |
| RP-02 | `sn-read/write` | strategic number | engine-facing control | E0 | must be audited | design-approved | official historical maximum was extended to 511; exact current build still unverified |
| RP-03 | `flag-read/write` | flag | Boolean state/control | E1 | must be audited | design-approved | semantics must record initial state and writers/readers |
| RP-04 | `timer-triggered` | timer id | temporal gate | E1 | must be audited | design-approved | timer expiry does not itself terminate a commitment |
| RP-05 | `enable-timer` / `disable-timer` | timer id | temporal control | E1 | must be audited | design-approved | owner and generation association required by AEGIS |
| RP-06 | `up-compare-goal` | goal/value | bounded comparison | E0/E1 | must be audited | design-approved | do not use high scratch goals here without profile proof |
| RP-07 | `up-modify-goal` | goal, delta | scalar mutation | E0/E1 | must be audited | design-approved | arithmetic saturation policy required |
| RP-08 | `up-get-focus-fact` | focus player, fact, subject, destination | observation/query | E0/E1 | must be audited | design-approved | subject type must match fact contract |
| RP-09 | `unit-type-count` | unit/line | population observation | E0/E1 | must be audited | design-approved | line IDs and concrete unit IDs are not interchangeable with class IDs |
| RP-10 | `unit-type-count-total` | unit/line | aggregate including queued objects | E0 | must be audited | design-approved | official Update 36202 expanded queued-object coverage |
| RP-11 | `up-pending-objects` | player/object type | pending/queue observation | E0 | must be audited | design-approved | pending is not completion |
| RP-12 | `can-train` / `up-can-train` | producer/unit | feasibility | E0 | must be audited | design-approved | eligibility is not a transaction receipt |
| RP-13 | `train` / `up-train` | producer/unit | side-effect command | E0 | must be audited | design-approved | accepted/queued/completed must be separately observed |
| RP-14 | producer search | search constraints | dynamic producer selection | E1 | must be audited | design-approved | search identity must be DURABLE/PROVISIONAL/UNKNOWN |
| RP-15 | feasibility predicate | facts/state | hard constraint | E1 | must be audited | design-approved | must run before soft candidate evaluation |
| RP-16 | command gate | commitment + feasibility | side-effect authorization | E2 | project-owned | design-approved | no command unless commit valid and command-eligible |
| RP-17 | postcondition observation | world facts | execution verification | E2 | project-owned | design-approved | must identify V-level achieved; command issue alone is insufficient |
| RP-18 | generation compare | generation scalar | stale-operation rejection | E2 | project-owned | design-approved | wraparound/zero policy required before coding |
| RP-19 | ownership guard | owner + phase | mutation authority | E2 | project-owned | design-approved | ownership is an AEGIS contract, not a historical engine primitive |
| RP-20 | record publication | VALID + generation + owner + fields | coherent state publication | E2 | project-owned | design-approved | use VALID=0 → populate → generation/owner/fields → VALID=1; do not call atomic |

## 4. Mandatory command-success ladder

`DESIRE → CAN-FACT → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

A later state must never be inferred merely from an earlier state. `train` does not prove acceptance, queueing, creation, deployment, or battlefield effect.

## 5. Current authoritative evidence

Official Update 36202 states that `unit-type-count-total` and `up-pending-objects` count additional objects in the unit queue. citeturn0search0

Official Update 47820 documents `can-train`, `up-can-train`, `train`, and `up-train` accepting `-1`, and introduces `sn-enable-research-queue`. citeturn1search1

Official Update 42848 extended the maximum supported strategic numbers from 303 to 511. citeturn0search1

Official Update Preview 125283 increased available goals from 512 to 16000. This is strong evidence that the old G0–G511 assumption is not a universal current goal limit. citeturn1search2

The latest major official update located for the current research baseline is Update 177723 (June 2, 2026), which identifies build 177723 and includes AI-engine fixes. The workstation build remains unverified. citeturn1search0

## 6. Gate for implementation

No primitive enters Layer-3 code as VERIFIED until its exact signature, legal inputs, side effects, build scope, validator representation, and observable postcondition are recorded in the ABI registry. Runtime validation remains blocked while the authorized workstation is disconnected.
