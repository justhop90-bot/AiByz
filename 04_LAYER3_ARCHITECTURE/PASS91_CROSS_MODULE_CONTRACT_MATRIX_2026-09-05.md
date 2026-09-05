# AEGIS Layer 3 — Pass 91 Cross-Module Contract Matrix

Date: 2026-09-05
Status: ARCHITECTURE / IMPLEMENTATION GATE
Scope: `.per` architecture only. XS excluded.

## 1. Purpose

Pass 90 established primitive and state contracts. Pass 91 addresses the higher-risk boundary: interactions among multiple controllers. AEGIS is treated as a distributed rule-driven control system whose correctness depends on inter-module contracts, not merely local rule correctness.

The governing invariant is:

> No module may infer completion of another module's responsibility. A consumer may only act on a producer's explicitly defined state contract, including validity, provenance, generation, ownership, stage, and evidence level where applicable.

## 2. System-of-systems pipeline

`ENGINE OBSERVATION → INTELLIGENCE → ASSESSMENT → OBJECTIVE → FORCE/CAPABILITY DEMAND → PRODUCTION ARBITRATION → EXECUTION AUTHORITY → ENGINE COMMAND → QUEUE/PENDING → WORLD OBSERVATION → VERIFICATION → RECOVERY/REASSESSMENT`

The arrows are contracts, not implied synchronous calls. Controller-clock state changes and world-clock transitions remain distinct.

## 3. Contract matrix

| Boundary | Producer | Consumer | Producer may claim | Consumer may assume | Required contract | Forbidden inference |
|---|---|---|---|---|---|---|
| C01 | Intelligence | Assessment | observation record published | record is valid only if VALID/owner/generation checks pass | threat type, magnitude, observation age, confidence/evidence | observation = enemy intent |
| C02 | Assessment | Objective | strategic assessment published | assessment is current for expected generation | objective id/version, validity, priority class | assessment = authorization |
| C03 | Objective | Force | capability requirement emitted | requirement is demand, not execution | objective id, capability family, required mass, deadline/latency class | demand = production order |
| C04 | Force | Production | capability demand emitted | demand is eligible for production evaluation | demand validity, objective owner, generation, current deficit | demand = commitment |
| C05 | Production | Arbitration | candidate/load/deficit proposal emitted | proposal is not authority until admitted | candidate id, deficit, feasibility, resource load, epoch | proposal = authorization |
| C06 | Arbitration | Execution | commitment/authority granted | only matching owner+generation+valid stage may execute | commitment id, owner, generation, stage, veto state | resource reservation = ownership |
| C07 | Execution | Engine | command issued | engine may accept, queue, delay, or reject | command identity, producer, target/type, issue evidence | issued = accepted |
| C08 | Engine | Execution | world/queue observation | observed transition corresponds to a defined evidence level | temporal/aggregate/object evidence | pending = created |
| C09 | Execution | Verification | execution evidence published | evidence level is exact and bounded | V-level, provenance, generation, observation time | created = deployed |
| C10 | Verification | Assessment | postcondition result published | result applies to objective generation | success/failure/unknown, evidence level | deficit zero = objective success |
| C11 | Recovery | Arbitration | commitment released/reduced/replaced | arbitration must reconsider alternatives | reason code, release state, generation increment | failure = automatic retry |
| C12 | Timer/controller | Any consumer | temporal event/status published | timer belongs to declared owner/generation | timer id, owner, generation, purpose, state | timer expiry = commitment expiry |
| C13 | Memory/state | Any writer | mutable state channel exposed | writer has declared authority | field schema, writer set, initialization, sentinel | writable = authorized |
| C14 | Network/map | Force/Objective | map/network observation | evidence age and provenance are known | observation timestamp/epoch, confidence | current observation = permanent truth |
| C15 | Market/economy | Production | economic feasibility signal | signal is advisory unless authority contract says otherwise | resource state, reservation, epoch | affordability = guaranteed queue slot |

## 4. Mandatory state envelope

Where a cross-module record can become stale or contested, the minimum envelope is:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Additional fields are required when the domain needs them: objective identity, candidate identity, arbitration epoch, timer association, resource reservation, failure code, observation age.

`VALID=0 → populate payload → generation/owner/stage → VALID=1` is the publication pattern. This is a coherence protocol, not a claim of hardware/runtime atomicity.

## 5. Ownership rule

Ownership is a project contract. It must be made mechanically auditable by an explicit writer matrix or structurally exclusive controller phase. A goal being writable does not establish authority.

For mutable consequential state, the implementation must identify:

`FIELD → OWNER → WRITERS → READERS → CLEARER → LIFETIME → INVALIDATION → GENERATION SOURCE`

## 6. Generation rule

Every delayed action or asynchronous world observation that can arrive after a strategic decision changes must carry or be checked against the expected generation. A stale observation may be recorded for archaeology/telemetry but may not mutate the active commitment without an explicit stale-data policy.

Generation policy must define zero, wraparound, comparison semantics, and reuse before implementation.

## 7. Arbitration rule

Candidate selection must not accidentally collapse into first-feasible-wins. The implementation must explicitly choose one of:

1. ordered policy, where ordering is intentional and documented; or
2. best-so-far selection, where an incumbent candidate and comparison state are explicit.

Hard feasibility precedes soft evaluation. An infeasible candidate never wins because its soft score is high.

## 8. Evidence rule

Evidence states are monotonic only within a defined execution instance. A later contradiction can invalidate the commitment even when an earlier evidence level was genuine.

Minimum evidence ladder:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

No consumer may silently upgrade evidence.

## 9. Cavalry Slice cross-module contract

`Intelligence` publishes enemy mounted-pressure observation.

`Assessment` determines whether the observation is sufficiently current and material.

`Objective` declares cavalry-containment capability requirement.

`Force` emits required camel capability.

`Production` measures current capability and computes `max(0, REQUIRED-CURRENT)` while retaining surplus separately.

`Arbitration` selects and admits a feasible producer/counter candidate.

`Execution` is the sole consequential training authority for the slice.

`Verification` distinguishes queue, creation, availability, deployment, and battlefield effect.

`Assessment` then decides whether the objective postcondition was actually achieved.

## 10. Integration gate

No module is implementation-cleared merely because its own static source is clean. A module is integration-cleared only when every inbound/outbound contract has:

- named producer and consumer;
- field schema;
- validity semantics;
- owner/writer matrix;
- generation semantics;
- legal stages;
- evidence level;
- initialization and invalidation;
- collision-audited storage;
- build profile;
- validator representation;
- failure behavior.

Current status: **OPEN — architecture substantially specified; numeric ABI and runtime validation remain outstanding.**