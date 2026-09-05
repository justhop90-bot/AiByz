# AEGIS Layer 3 — Pass 92 ABI Finalization and Allocation Gate

Date: 2026-09-05
Status: **PROVISIONAL ABI / PRE-CODE GATE — NUMERIC ALLOCATION NOT CLEARED**
Scope: `.per` architecture only. XS excluded.

## 1. Purpose

Pass 91 established the cross-module contract matrix and failure topology. Pass 92 resolves the next architectural question: how the typed AEGIS state contract becomes a concrete `.per` storage plan without silently colliding with legacy state, engine namespaces, validator assumptions, or build-dependent limits.

The central result is deliberately conservative:

> **The symbolic ABI is now frozen for the first Cavalry Threat Containment vertical slice; numeric allocation remains blocked until an authoritative constant inventory is available.**

This is not a delay caused by lack of design. It is an explicit safety boundary: a numeric ID that has not been collision-audited is not an implementation-ready ID.

## 2. Evidence baseline

Official AoE2DE Update 42848 documents that the maximum supported strategic-number index was extended from 303 to 511. citeturn0search0

Official Update Preview 125283 documents a later increase in available goals from 512 to 16000. citeturn0search1

Therefore:

- goal IDs and strategic-number IDs are separate namespaces;
- the historical `G0–G511` proposal cannot be treated as a safe goal allocation block;
- a high goal number is not automatically safe merely because it exceeds the historical 0–511 range;
- the actual imported package, legacy state, validator profile, and target build must be audited before a number is marked `CLEAR`.

The current workstation remains unavailable at the filesystem/process layer, so this pass does not pretend to possess the installed AI's authoritative constant inventory.

## 3. ABI freeze: symbolic fields

The first vertical slice is restricted to these state fields:

| ID | Symbol | Channel | Authority | Owner | Purpose |
|---|---|---|---|---|---|
| G-C01 | `OBS.ENEMY_CAVALRY` | goal | ENGINE_AUTHORITATIVE | Intelligence | measured enemy mounted capability |
| G-C02 | `OBS.ENEMY_CAVALRY_AGE` | goal | AEGIS_AUTHORITATIVE | Intelligence | observation age/staleness |
| F-C01 | `THREAT.CAVALRY_ACTIVE` | flag | DERIVED_CACHE | Threat | material-threat latch |
| G-C03 | `CAP.CAMEL_CURRENT` | goal | ENGINE_AUTHORITATIVE | Capability | current camel capability |
| G-C04 | `CAP.CAMEL_REQUIRED` | goal | AEGIS_AUTHORITATIVE | Capability | policy-required camel capability |
| G-C05 | `CAP.CAMEL_DEFICIT` | goal | DERIVED_CACHE | Capability | saturated capability deficit |
| G-C06 | `CAND.PRODUCER` | goal | AEGIS_AUTHORITATIVE | Candidate | selected production location/producer |
| G-C07 | `CAND.STATUS` | goal | AEGIS_AUTHORITATIVE | Candidate | candidate lifecycle state |
| F-C02 | `COMMIT.VALID` | flag | AEGIS_AUTHORITATIVE | Commitment | active commitment publication guard |
| G-C08 | `COMMIT.OWNER` | goal | AEGIS_AUTHORITATIVE | Commitment | consequential-state owner |
| G-C09 | `COMMIT.GEN` | goal | AEGIS_AUTHORITATIVE | Commitment | commitment generation |
| G-C10 | `COMMIT.STAGE` | goal | AEGIS_AUTHORITATIVE | Commitment | legal commitment lifecycle stage |
| G-C11 | `EXEC.STAGE` | goal | AEGIS_AUTHORITATIVE | Execution | execution lifecycle stage |
| G-C12 | `EXEC.EXPECTED_GEN` | goal | AEGIS_AUTHORITATIVE | Execution | stale-operation guard |
| G-C13 | `RES.RESERVED` | goal | AEGIS_AUTHORITATIVE | Resource | committed resources |
| G-C14 | `RES.DISCRETIONARY` | goal | DERIVED_CACHE | Resource | spendable resources after reservation |
| G-C15 | `ARB.EPOCH` | goal | AEGIS_AUTHORITATIVE | Arbitration | authoritative arbitration version |
| F-C03 | `ARB.DIRTY` | flag | DERIVED_CACHE | Arbitration | optimization hint only |
| G-C16 | `VERIFY.LEVEL` | goal | OBSERVATIONAL | Verification | evidence level V0–V8 |

No numeric value is assigned by this table.

## 4. Numeric allocation policy

### 4.1 Required audit order

Numeric allocation must occur in this order:

1. enumerate all imported `defconst` goal identifiers;
2. enumerate all existing goal channels retained by the implementation package;
3. enumerate all temporary/scratch goals;
4. enumerate all legacy AEGIS/PORPHYRA channels actually imported;
5. enumerate engine-reserved goal symbols known to the target build;
6. enumerate validator-recognized goal constraints;
7. enumerate existing strategic-number identifiers separately;
8. enumerate flags separately;
9. enumerate timer IDs separately;
10. enumerate search IDs/state variables separately;
11. compare candidate allocations against every collision domain;
12. record the exact build/profile for which the result is valid.

### 4.2 Allocation rule

A numeric assignment becomes `CLEAR` only when its complete audit record is present:

`symbol | channel | numeric_id | source | owner | readers | writers | lifetime | sentinel | build_min | build_max_tested | validator_status | collision_status`

Allowed collision states:

- `CLEAR`
- `COLLIDES_LEGACY`
- `COLLIDES_ENGINE`
- `COLLIDES_VALIDATOR`
- `BUILD_DEPENDENT`
- `UNRESOLVED`

Only `CLEAR` can be emitted into implementation constants.

### 4.3 No blanket range reservation

Do not reserve an arbitrary block such as `G0–G511`, `G12000–G12031`, or any similar range merely because it appears unused in a partial snapshot.

A range can become a project-owned allocation band only after the complete imported namespace has been inventoried and the target build's semantics are fixed.

## 5. First-slice storage minimization

The first executable vertical slice requires only 16 goal-like fields and 3 flags from the symbolic ABI above.

The implementation must not allocate additional strategic state merely because future modules may need it. Future fields are added through the same ABI audit rather than by preallocating an enormous block.

This minimizes:

- collision surface;
- validator ambiguity;
- initialization complexity;
- stale-state interactions;
- writer overlap;
- debugging burden;
- migration cost if the target build changes.

## 6. Representation rules

### Goals

Goals are the preferred scalar persistent-state channel for AEGIS state, subject to the final collision/build audit. They are not interchangeable with strategic numbers.

### Strategic numbers

SNs are treated as the preferred engine-facing control plane where a primitive specifically requires an SN. They are not general-purpose AEGIS memory merely because they contain integers.

### Flags

Each flag requires an explicit representation contract:

`symbol | numeric identity | initial state | setter | clearer | readers | compare semantics | build profile`

A flag is not allocated until all of these are known.

### Timers

Timers require:

`timer_id | owner | generation | purpose | initial state | enable rule | trigger consumer | disable/restart rule`

Timer expiration does not itself terminate a commitment.

## 7. Publication protocol

For any multi-field record:

`VALID=0 → populate payload → write generation → write owner → write stage → write remaining metadata → VALID=1`

Every consumer must check at minimum:

`VALID=1 AND OWNER=EXPECTED_OWNER AND GENERATION=EXPECTED_GENERATION`

This is a state-coherence protocol, not a claim that `.per` provides hardware-style atomic publication.

## 8. Generation protocol

`COMMIT.GEN` is the authoritative execution-instance generation.

A new commitment must produce a new generation before consequential execution state becomes valid.

Delayed operations must carry `EXEC.EXPECTED_GEN` and may act only when:

`COMMIT.VALID=1 AND COMMIT.GEN=EXEC.EXPECTED_GEN`

The final implementation must specify:

- zero meaning;
- increment operation;
- maximum representable value;
- wraparound behavior;
- comparison semantics;
- reuse after wraparound;
- initialization and reset behavior.

Until these are mechanically represented, generation is an architecture contract rather than a runtime guarantee.

## 9. Deficit semantics

For the Cavalry Slice:

`DEFICIT = max(0, REQUIRED - CURRENT)`

Surplus is retained separately:

`SURPLUS = max(0, CURRENT - REQUIRED)`

Therefore:

- deficit zero means measured capability meets the stated capability requirement;
- deficit zero does **not** mean the strategic objective succeeded;
- objective success remains a verification/postcondition decision;
- underflow and negative storage are prohibited by design.

## 10. Candidate-selection semantics

The first slice must explicitly choose one of two legal arbitration implementations:

### Ordered-policy mode

Candidates are evaluated in an intentional, documented order. The order is itself policy.

### Best-so-far mode

The controller maintains an incumbent candidate and explicit comparison state. Each feasible candidate is compared against the incumbent.

The implementation may not accidentally derive scheduling semantics from textual rule order while calling the mechanism an optimizer.

Hard feasibility always precedes soft evaluation.

## 11. Authority classes

Every ABI field is assigned exactly one authority class:

- `ENGINE_AUTHORITATIVE`: world/engine observation is source of truth.
- `AEGIS_AUTHORITATIVE`: AEGIS state is the policy/commitment source of truth.
- `DERIVED_CACHE`: recomputable convenience state; never authoritative.
- `OBSERVATIONAL`: evidence/diagnostic state; never silently promoted to authority.

This prevents a derived deficit, dirty bit, or verification cache from becoming an accidental source of truth.

## 12. Engine / validator / project support separation

For each primitive or state representation, three independent statuses are required:

| Dimension | Meaning |
|---|---|
| Engine support | target AoE2DE build actually implements the primitive/semantics |
| Validator support | the project's validator/parser accepts the representation |
| AEGIS support | the project has a defined contract and implementation for it |

`ENGINE=YES` and `VALIDATOR=NO` is not implementation-ready.

`VALIDATOR=YES` and `ENGINE=NO` is not implementation-ready.

Both may be true while `AEGIS=NO`; that still blocks implementation.

## 13. Current gate matrix

| Gate | Status | Reason |
|---|---|---|
| Symbolic ABI | **PASS** | first-slice fields frozen |
| Cross-module contracts | **PASS** | Pass 91 contract matrix |
| Failure topology | **PASS** | Pass 91 T01–T24 / S1–S8 |
| Goal numeric allocation | **BLOCKED** | authoritative imported constant inventory unavailable |
| SN numeric allocation | **BLOCKED** | separate namespace audit required |
| Flag allocation | **BLOCKED** | exact representation/build audit required |
| Timer allocation | **BLOCKED** | existing timer inventory required |
| Generation implementation | **BLOCKED** | numeric/state representation unresolved |
| Validator ABI | **OPEN** | source-of-truth validator profile required |
| Exact installed build | **BLOCKED** | workstation connection unavailable |
| Runtime validation | **BLOCKED** | workstation connection unavailable |

## 14. What this pass changes

Pass 92 closes the architectural ambiguity around **what** must be allocated and **how** it becomes safe to allocate it. It intentionally does not fabricate the missing numeric evidence.

The next implementation-enabling artifact is therefore not another abstract design: it is a **machine-auditable authoritative namespace inventory** generated from the actual target package/build (or an explicitly accepted equivalent snapshot).

Once that inventory exists, the symbolic table above can be mechanically joined to it and each field can receive a numeric assignment with a defensible `CLEAR` status.

## 15. Implementation gate

No `.per` state constants from this ABI may be emitted yet.

The implementation gate opens only when:

1. the authoritative goal/SN/flag/timer inventories are captured;
2. every proposed numeric assignment is collision-audited;
3. each assignment has an owner/writer/reader/lifetime record;
4. generation semantics are numerically representable;
5. validator and engine support are separately recorded;
6. the exact target build is identified;
7. the resulting allocation table is committed as the new ABI source of truth.

**Final Pass 92 verdict: SYMBOLIC ABI FINALIZED; NUMERIC ABI NOT CLEARED. CODE GENERATION REMAINS CORRECTLY BLOCKED.**
