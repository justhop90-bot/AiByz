# P0 Verification, Recovery & Reconciliation OS — 2026-09-08

## Status
STATIC ARCHITECTURAL CLOSURE: QUALIFIED WITH RUNTIME BOUNDARY

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.

This pass establishes the common verification/recovery layer across civilian,
construction, research, economy, scouting, threat, and military lifecycles.
It is a static reconstruction. Runtime timing and interpreter semantics remain
unqualified unless explicitly identified as previously machine-tested evidence.

## Executive finding

Stock Promisory does not expose one monolithic reconciliation service.
Instead, verification and recovery are distributed through subsystem rules,
pending predicates, research-status predicates, reset operations, goal resets,
timers, jump topology, and strategic cancellation/re-entry paths.

The architectural function is nevertheless common:

```text
COMMAND / INTENT
      ↓
PENDING / EXECUTION
      ↓
OBSERVATION
      ↓
RECONCILIATION
   ↙      ↓       ↘
CONFIRMED  UNRESOLVED  FAILED
              ↓          ↓
          WAIT / AGE   CLASSIFY
                         ↓
                   RECOVER / RETRY
                         ↓
                     REPLAN
```

## Core evidence

### 1. Pending state is an explicit control signal

`up-pending-objects` is heavily consumed by `buildings.per` for houses,
town centers, camps, walls, towers, and other infrastructure. This demonstrates
that stock controllers distinguish an outstanding engine-side object request
from the absence of a completed object.

`up-pending-placement` is separately used by construction recovery. It is
therefore not safe to equate generic pending objects with placement state.

### 2. Placement has explicit recovery

Stock construction contains repeated `up-reset-placement` paths for town
centers, houses, lumber camps, mining camps, mills, castles, and other cases.
This is direct evidence that placement state can become invalid or stalled and
that recovery is an explicit operation rather than an implicit retry.

### 3. Building state can be reset independently

`up-reset-building` occurs in `general.per`, `init.per`, and `researches.per`.
The reset target may be a building type and is distinct from placement reset.
Therefore AEGIS must not model all construction failure as one undifferentiated
"build failed" event.

### 4. Research has independently observable lifecycle states

Stock defines and consumes `research-pending` and `research-complete` through
`up-research-status`. Other rules also use `research-completed`. This confirms
that research admission, pending state, and completion are distinct semantic
states in the stock control network.

### 5. Strategic recovery is distributed

`underattack` and `attacking` are persistent goals consumed by construction,
economy, escrow, and military-related logic. Rules explicitly restore these
states to `no` as conditions change. These are recovery/reconciliation effects,
not merely one-shot alarms.

## Unified state model

AEGIS should preserve the following semantic separation:

```text
REQUESTED
  → ADMITTED
  → RESERVED
  → ENDPOINT_SELECTED
  → AUTHORIZED
  → COMMAND_ISSUED
  → EXECUTING / PENDING
  → OBSERVED
  → VERIFIED
```

Failure is not the only non-success branch. A request can become:

- `UNRESOLVED`: expected observation has not arrived;
- `FAILED`: contradictory or timeout evidence establishes failure;
- `SUPERSEDED`: a newer valid intent replaces the request;
- `EXPIRED`: its observation/recovery window elapsed;
- `INVALIDATED`: its preconditions or owning strategic generation ceased to be valid.

## Critical rule: unresolved is not failed

The verifier must not convert a missing immediate postcondition into failure.
Stock rules use pending predicates, timers, and later observations precisely
because engine-side operations can persist beyond the rule that requested them.

Therefore:

```text
no postcondition yet
        ≠ failure
```

Failure requires either explicit contradictory evidence, an established
failure predicate, or an empirically qualified watchdog boundary.

## Failure classification

AEGIS recovery should classify failures before choosing an action. The minimum
classes are:

| Class | Meaning | Typical recovery |
|---|---|---|
| PRECONDITION | authorization ceased to be valid | re-admit |
| RESOURCE | required resource/escrow unavailable | defer/re-arbitrate |
| ENDPOINT | target/placement unavailable | select another endpoint |
| EXECUTION | command did not establish expected state | retry/alternate path |
| STALL | pending state persists beyond qualified window | reset/retry |
| OBSERVATION | expected state cannot yet be verified | continue observing |
| SUPERSEDED | newer intent owns the objective | abandon old request |
| INVALIDATED | generation/owner no longer valid | release and replan |

These are AEGIS classifications, not claims that stock exposes these exact
labels. Stock evidence establishes the underlying behaviors; the typed labels
are an architectural normalization.

## Recovery is subsystem-specific

Construction recovery can reset placement, perturb a point, change builder
allocation, retry, or cancel the infrastructure objective. Research recovery
must instead reason about research status and prerequisite/building availability.
Military recovery can change posture, retreat, retarget, or regenerate force
demand. Economic recovery can release commitments and reallocate workers.

Consequently the common OS owns lifecycle truth, while each operating service
owns the domain-specific recovery action.

## Generation fencing

A request must not be allowed to complete against obsolete strategic state.
AEGIS therefore requires a generation/epoch concept at the control-plane level.
A newer strategic decision may supersede an older request even when the old
engine operation is still physically pending.

```text
Generation 17: build forward tower
        ↓
Generation 18: enemy attack changes defensive requirement
        ↓
request-17 = SUPERSEDED / INVALIDATED
        ↓
request-18 owns future arbitration
```

This is an AEGIS architectural requirement, not a claim that stock stores a
universal request generation ID.

## Ownership boundary

Verification must be independent from the service that issued the command.

```text
Strategy / Cognition
        ↓ intent
Operating Service
        ↓ command
Engine / World
        ↓ observation
Verification OS
        ↓ disposition
Arbitration / Recovery
        ↓
Operating Service
```

The issuer knows what it intended. The verifier determines what actually
happened. This prevents command issuance from being mistaken for completion.

The previously established authority matrix therefore remains intact:

- World Model owns observations and freshness.
- Strategy owns strategic intent.
- Economy owns resource allocation.
- Construction owns construction execution.
- Production owns production execution.
- Military owns force posture/execution.
- Research owns technology authorization/state.
- Verification & Recovery owns confirmation, failure classification, and
  reconciliation.

Historical producer/consumer relationships are evidence of coupling, not
permission to transfer semantic ownership wholesale.

## Common request ledger

AEGIS should eventually expose a typed internal request record containing at
least:

```text
request_id
generation
owner
intent
priority
preconditions
reservation
endpoint
command_path
issued_at
expected_postcondition
observation_window
observed_result
failure_class
retry_count
retry_policy
validity
terminal_disposition
```

The stock corpus does not establish that such a universal ledger exists.
It is therefore an AEGIS design proposal, not reconstructed stock behavior.

## Watchdogs and timers

Stock uses timers extensively around long-running control loops and retry
paths. Timer presence proves temporal gating exists, but does not by itself
prove a universal timeout duration or a single watchdog service.

AEGIS must consequently distinguish:

```text
timer observed in stock
        ↓
temporal control exists
        ↓
exact timeout semantics
        ↓
RUNTIME QUALIFICATION REQUIRED
```

No stock timer should be promoted into a universal AEGIS timeout without
measuring the relevant interpreter behavior on the target build.

## Jump topology

`up-jump-rule` is pervasive and is used both forward and backward. It forms
part of the execution topology of recovery/retry loops. A rule that appears
to be a linear state machine in source may therefore execute through nonlocal
control-flow transitions.

AEGIS must treat jump topology as control-flow semantics, not formatting.
Same-pass visibility and exact re-entry behavior remain runtime questions.

## Cross-lifecycle verification matrix

| Lifecycle | Pending evidence | Success evidence | Recovery evidence |
|---|---|---|---|
| Civilian | production/pending state | physical census delta | re-admit/reconcile |
| Construction | pending-object / pending-placement | foundation/structure state | reset placement/building, retry |
| Research | research-pending | research-complete / completed | re-evaluate prerequisites |
| Economy | reservations/worker state | resource/task convergence | release/reallocate |
| Scouting | mission/group state | contact/position observation | retask/search |
| Threat | interpreted threat state | refreshed observation/model | decay/recompute |
| Military | attack/retreat posture | battlefield state | retreat/retarget/regenerate demand |

This table is an AEGIS normalization of previously reconstructed subsystem
behavior. It does not imply identical stock predicates or identical timing.

## What static archaeology closes

The following architectural facts are now sufficiently supported:

1. consequential commands have distinct request/execution/observation phases;
2. pending state is semantically meaningful;
3. verification is distributed in stock rather than centralized;
4. recovery is explicit and domain-specific;
5. resets exist at multiple state layers;
6. timers and jumps participate in recovery topology;
7. strategic state can supersede an in-flight operation;
8. physical observation must remain distinct from AI bookkeeping;
9. command-path differences must survive AEGIS abstraction boundaries;
10. failure classification is necessary before recovery policy can be selected.

## What remains runtime-unqualified

Static source cannot establish:

- exact command-to-observation latency;
- same-pass visibility of state mutations;
- exact lifetime of pending predicates;
- exact semantics of reset operations after each failure mode;
- escrow consumption/restoration timing;
- exact jump/re-entry ordering;
- whether two apparently equivalent command paths produce identical engine state;
- the correct watchdog interval for any AEGIS timeout;
- whether a given observation is authoritative immediately or only after a
  synchronization boundary.

These questions belong in the runtime ABI qualification harness.

## AEGIS implementation gate

Do not implement a universal fire-and-forget command layer.

The eventual service contract should instead be conceptually:

```text
service.request(intent)
        ↓
service.admit()
        ↓
service.issue()
        ↓
verification.observe()
        ↓
verification.confirm / classify
        ↓
recovery.recover()
        ↓
arbitration.replan()
```

Each service retains its native command-path discriminator internally.
Verification consumes observations, not private success claims from issuers.

## Decision

P0 Verification / Recovery / Reconciliation is **structurally closed at the
architectural contract level**.

The project should now stop adding speculative subsystem architecture and
move to the next layer: **AEGIS ABI / runtime qualification**.

The first runtime target should be the smallest falsifiable interpreter
question shared by all services: the command → state mutation → observation
boundary, followed by pending-state lifetime and same-pass visibility.

No production `.per` promotion is authorized by this artifact alone.
