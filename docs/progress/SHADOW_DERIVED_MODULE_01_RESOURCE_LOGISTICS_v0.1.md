# Shadow-Derived Module 01 — Resource Logistics & Worker Control v0.1

**Parent:** Shadow-Derived Next Model v0.1  
**Reference:** Shadow DC7 / `TheByzantineShadow/SourceShaRef`  
**Status:** DESIGN SPECIFICATION — NOT PRODUCTION-CLEARED  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652

## Mission

Reconstruct Shadow's resource/worker control loop while preserving its `.per` mechanisms and repairing only demonstrated weaknesses: ambiguous ownership, stale state, implicit completion, missing expiry/recovery, and uncontrolled cross-domain mutation.

This is deliberately **Shadow-derived**, not an AEGIS service abstraction.

## Canonical loop

```text
RESOURCE DEMAND
→ WORKER CENSUS
→ ROLE DEFICIT
→ ELIGIBLE WORKER SEARCH
→ SOURCE SEARCH
→ DROPSITE SEARCH
→ FILTER
→ RANK
→ TASK
→ OBSERVE ENGINE STATE
→ VERIFY RESOURCE SERVICE
→ RECONCILE
→ REASSESS
```

## Shadow mechanisms to preserve

1. Explicit search/filter/aggregate/select loops.
2. Scratch goals/SNs for local arithmetic, counters, coordinates and loop state.
3. Point/coordinate geometry where target-build ABI evidence supports it.
4. Timers for hysteresis, cooldown, retry suppression and periodic reassessment.
5. Direct engine tasking at the execution boundary.
6. Integrated interaction between workers, resources, dropsites, construction and progression.

Do not hide these mechanisms behind an opaque abstraction.

## Modifications

### Assignment lifecycle

```text
UNASSIGNED → ASSIGNING → ASSIGNED → WORKING
                         ↓           ↓
                      INVALID    INTERRUPTED
```

Assignment is not proof of successful gathering.

### Consequential generation

Long-lived economic targets and assignments carry a generation. A result from an obsolete generation cannot overwrite current state.

Transient arithmetic/search scratch remains lightweight and does not receive unnecessary lifecycle machinery.

### Source validity

A source is not valid merely because it was found previously.

```text
source-id
source-type
position
observed-status
last-observed
serviceable
failure-state
generation
```

### Dropsite validity

Existence is not equivalent to serviceability.

```text
dropsite-id
type
position
operational-state
last-observed
service-distance
```

Do not call service distance exact path distance without evidence.

## Worker allocation pipeline

```text
ALL WORKERS
→ REMOVE PROTECTED
→ REMOVE HIGHER-AUTHORITY / COMMITTED WORKERS
→ REMOVE INVALID / INCOMPATIBLE STATE
→ RETAIN TASKABLE WORKERS
→ RANK
→ ASSIGN
```

Material exclusions should have an attributable reason.

## Source pipeline

```text
ALL KNOWN SOURCES
→ RESOURCE TYPE
→ AVAILABILITY
→ SERVICEABILITY
→ THREAT
→ DROPSITE COMPATIBILITY
→ DISTANCE / LOAD RANKING
→ SELECT
```

Identical observed state must produce deterministic selection.

## Demand interface

The module consumes a desired worker vector; it does not invent civilization-wide strategy.

```text
food = N
wood = N
gold = N
stone = N
```

Operational deficit:

```text
DEFICIT = DESIRED − VERIFIED/OBSERVED
```

Global priority arbitration remains outside this module.

## Hysteresis

Normal reassignment requires explicit thresholds:

- minimum reassignment interval;
- minimum deficit magnitude;
- priority override;
- emergency override;
- source-failure override.

Emergency bypass must be explicit. One-unit stock fluctuations must not cause perpetual worker churn.

## Interruption handling

```text
WORKING
→ INTERRUPTION OBSERVED
→ CLASSIFY
   ├─ temporary
   ├─ threat
   ├─ source unavailable
   ├─ higher-authority operation
   └─ unknown
→ RECOVER / WAIT / REASSIGN
```

An external higher-authority operation may legitimately supersede an economic assignment.

## Failure handling

### Source failure

```text
invalidate
→ cooldown
→ alternate source
→ reassess
```

### Dropsite failure

```text
invalidate endpoint
→ search replacement
→ reassess
```

### Command failure

```text
mark failed
→ classify
→ bounded retry
→ alternate candidate or recovery
```

Repeated failure enters a quarantine/cooldown state rather than an infinite retry loop.

## Verification contract

Every consequential assignment declares its verification condition before execution.

| Stage | Evidence | Result |
|---|---|---|
| Demand | worker census | OPEN / NONE |
| Candidate | search/object data | VALID / INVALID |
| Assignment | executor state | ISSUED |
| Working | action/order/target | WORKING / FAILED |
| Service | periodic observation | ACTIVE / INTERRUPTED |
| Resource result | income/cargo/context | CONFIRMED / PARTIAL / UNKNOWN |
| Reassessment | fresh census | MAINTAIN / CHANGE |

Raw stockpile increase is **not** sufficient proof of worker productivity because simultaneous expenditure can mask valid gathering.

## Ownership

### Module owns

- operational worker allocation state;
- source and dropsite candidate state;
- assignment lifecycle;
- local timers/cooldowns;
- assignment verification;
- allocation reconciliation.

### Module reads

- strategic resource demand;
- reservation pressure;
- worker census;
- construction/progression state;
- threat state;
- engine object state.

### Module does not own

- strategic objectives;
- civilization-wide priority arbitration;
- military objectives;
- research selection;
- global capital policy.

## Qualification tests

`RLOG-01` Stable allocation — no unnecessary churn.  
`RLOG-02` Single-resource deficit — bounded reassignment.  
`RLOG-03` Competing deficits — deterministic arbitration at the operational layer.  
`RLOG-04` Source invalidation — alternate source recovery.  
`RLOG-05` Dropsite invalidation — endpoint recovery.  
`RLOG-06` Worker interruption — classified and controlled reassignment.  
`RLOG-07` Stale generation — old result cannot overwrite new assignment.  
`RLOG-08` Command failure — bounded retry/failure classification.  
`RLOG-09` Simultaneous spending — no false failure from stockpile delta alone.  
`RLOG-10` Recovery — broken assignment returns to a valid operational state.

## Production gate

No production runtime implementation until:

```text
ABI evidence
+ namespace audit
+ writer/reader audit
+ parser qualification
+ isolated runtime load
+ RLOG-01..10 evidence
+ no unresolved critical stale-state path
+ no unresolved command/completion conflation
```

## Why this is Module 01

This is the closest high-value transplant of Shadow's core civilization-control machinery. It exercises searches, scratch state, geometry, timers, worker tasking, source selection, dropsite logistics, economic feedback, interruption, recovery and verification before the project attempts the much more coupled production and military controllers.

The objective is not to make Shadow look cleaner. The objective is to prove that Shadow's demonstrated control architecture can survive disciplined modernization without losing the mechanisms responsible for its competence.
