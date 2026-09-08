# P0 Civilian + Construction Lifecycle Closure — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Branch:** `aegis/control-plane-2026-09-08-v2`  
**Status:** STATIC LIFECYCLE RECONCILIATION / RUNTIME QUALIFICATION INCOMPLETE

## 0. Purpose

This pass reconciles the already-completed P0 civilian, worker, escrow, and construction investigations with the new AEGIS authority and state/service matrices. It is deliberately not a new broad census and does not promote any implementation candidate to production.

The objective is to close the known civilian/construction control loops far enough to define:

- observable state;
- requested state;
- authorization/admission;
- engine command;
- pending/execution state;
- completion evidence;
- failure evidence;
- supersession/cancellation;
- reconciliation ownership;
- runtime gaps that prevent ABI freeze.

## 1. Evidence base

This closure pass relies on the repository's prior P0 evidence, including:

- `docs/forensics/P0_CIVILIAN_LIFECYCLE_FORENSICS.md`
- `docs/P0_CIVILIAN_LIFECYCLE_RECONCILER_IMPLEMENTATION_PASS_2026-09-07.md`
- P0 worker-tasking and worker-loop qualification artifacts;
- P0 resource-source/dropsite/escrow investigations;
- `docs/forensics/P0_CONSTRUCTION_OS_FORENSICS_2026-09-08.md`;
- `docs/stock/AUTHORITY_BOUNDARY_MATRIX_2026-09-08.md`;
- `docs/stock/STATE_SERVICE_DEPENDENCY_MATRIX_2026-09-08.md`;
- `docs/forensics/P0_TOTAL_SUBSTRATE_DECONSTRUCTION_PASS_2026-09-08.md`.

The construction investigation independently establishes that `buildings.per` is a distributed construction OS and that its native construction primitives remain runtime-qualified only at the static boundary. The civilian investigation independently establishes that villager production, economic policy, integer worker accounting, source selection, infrastructure, escrow, and physical execution are distinct stages.

## 2. Reconciled civilian lifecycle

The evidence supports the following canonical civilian control loop:

```text
STRATEGIC / TECHNOLOGY STATE
        |
        v
CIVILIAN DEMAND
        |
        v
RESOURCE / ESCROW AUTHORIZATION
        |
        v
PRODUCTION AUTHORIZATION
        |
        v
ENGINE PRODUCTION REQUEST
        |
        v
PENDING / QUEUED STATE
        |
        v
PHYSICAL CIVILIAN CENSUS
        |
        v
ROLE VECTOR
        |
        v
ECONOMIC POLICY
        |
        v
SOURCE + DROPSITE SERVICEABILITY
        |
        v
WORKER TASKING
        |
        v
OBSERVED PRODUCTIVITY / TASK STATE
        |
        +--------------------+
        |                    |
        v                    v
INFRASTRUCTURE DEMAND    STRATEGIC FEEDBACK
        |                    |
        v                    |
CONSTRUCTION LIFECYCLE ----+
```

This is the minimum architecture consistent with the evidence. AEGIS must not collapse these stages into one worker allocator or one villager-production rule.

## 3. Villager production lifecycle

### Established source behavior

`units.per` initializes and conditionally mutates `trainvillager` based on population, food, age, strategy, military state, infrastructure, research, map/water state, dropsite conditions, and escrow-related conditions.

The civilian reconciler then establishes a stronger downstream invariant:

```text
REQUESTED -> AUTHORIZED -> ISSUED -> PENDING -> CENSUS DELTA -> CONFIRMED
                                             |
                                             +-> NO DELTA -> FAILED
```

### Architectural ownership

| Stage | Proposed owner | Evidence status |
|---|---|---|
| Civilian demand | Strategy/Economy | static supported |
| Affordability/reservation | Economy/Escrow | interaction supported; exact semantics pending |
| Production authorization | Civilian/Production service | static supported |
| Queue/command issuance | Production service / engine ABI | command semantics require runtime qualification |
| Pending observation | World Model / Production observer | static observation pattern supported |
| Completed villager census | World Model | native census supported |
| Lifecycle reconciliation | Verification & Recovery | architectural translation |

### Important invariant

A `can-train` result, a production authorization flag, an `up-train` command, and a pending queue object are **not equivalent to a completed villager**.

Completion requires physical-state evidence. The existing candidate deliberately uses a discrete villager census delta and does not infer completion from population or pending-object disappearance.

## 4. Generation fencing

The existing civilian reconciler identifies a major concurrency hazard: a census increase can be caused by another production request. Therefore a lifecycle record needs a generation fence.

The minimum conceptual record is:

```text
production_generation
baseline_civilian_census
issued
pending_observed
observed_civilian_census
attempt_count
observation_epoch
terminal_status
```

The V0 candidate assumes one active villager-production generation. That is a qualification constraint, not a final architectural limitation.

Before allowing multiple concurrent production endpoints, AEGIS must prove how completion attribution can be made unambiguous with engine-observable state.

## 5. Worker-role lifecycle

The civilian forensic evidence establishes that gatherer percentages are policy outputs and `dawn.per` converts those outputs into integer role targets.

The supported abstraction is:

```text
percentage policy
      |
      v
integer role targets
      |
      v
role reconciliation
      |
      v
individual worker selection
      |
      v
resource/source assignment
      |
      v
physical task execution
      |
      v
observed worker state
      |
      v
productivity / failure / recovery
```

The role vector is not itself tasking. This distinction is critical.

`food-villagers`, `wood-villagers`, `gold-villagers`, and `stone-villagers` represent allocation targets; they do not by themselves establish which individual villager is working which source.

## 6. Food is a two-stage lifecycle

The civilian evidence establishes that food is a portfolio of sources rather than one homogeneous resource class:

```text
food demand
   |
   +--> herdables
   +--> forage
   +--> boar
   +--> hunt
   +--> farms
   +--> fishing
   +--> civ/map-specific sources
```

Therefore the food controller has two distinct decisions:

1. how many workers should be allocated to food;
2. which food source should satisfy that allocation.

This is coupled to infrastructure and construction. Farms, mills, fishing infrastructure, and dropsite relationships alter the feasible source set.

## 7. Dropsite/serviceability closure

The prior civilian forensics establish that dropsite distance and infrastructure state participate in worker allocation decisions.

The resulting closed loop is:

```text
RESOURCE DEMAND
      |
      v
SOURCE DISCOVERY
      |
      v
SERVICEABILITY TEST
      |
      +--> usable -> worker assignment
      |
      +--> unusable -> infrastructure demand
                              |
                              v
                       CONSTRUCTION
                              |
                              v
                       COMPLETION
                              |
                              v
                       SERVICEABILITY
                              |
                              +----> worker assignment
```

This means Construction publishes a capability change to Economy rather than merely reporting that a building exists.

## 8. Housing closure

The civilian evidence shows housing pressure can alter worker allocation before construction occurs.

The closed loop is therefore:

```text
population pressure
      |
      v
housing deficit
      |
      v
wood allocation increase
      |
      v
house demand
      |
      v
construction lifecycle
      |
      v
housing capacity observed
      |
      v
civilian allocation restored
```

This is direct evidence that Economy and Construction cannot be independent authorities. They require an explicit contract.

## 9. Construction lifecycle

The construction forensic pass establishes a richer lifecycle than a generic `build()` abstraction:

```text
REQUESTED
   -> ADMITTED
   -> RESERVED
   -> PLACEMENT_SEARCH
   -> PLACEMENT_SELECTED
   -> AUTHORIZED
   -> COMMAND_ISSUED
   -> PLACEMENT_PENDING
   -> FOUNDATION_OBSERVED
   -> BUILDING_PROGRESS
   -> COMPLETE
```

Failure/supersession branches include:

```text
PLACEMENT_FAILED
PLACEMENT_CONFLICT
PLACEMENT_OUT_OF_RANGE
PLACEMENT_POLICY_REJECTED
PLACEMENT_RETRY_REQUIRED
BUILDER_UNAVAILABLE
BUILD_AUTHORIZATION_FAILED
COMMAND_NOT_OBSERVED
FOUNDATION_STALLED
CANCELLED
SUPERSEDED
```

These states are architectural labels, not claims that the engine exposes each state directly.

## 10. Construction authority boundary

The construction evidence establishes that `buildings.per` contains strategic demand, affordability/authorization, placement, native command issuance, builder assignment, pending-placement observation, retry/reset behavior, foundation/progress inspection, completion accounting, specialized placement, forward construction, and farm/dropsite logistics.

AEGIS therefore owns the lifecycle while retaining the engine's native construction ABI as an execution boundary.

The current `AEGIS-operations-final.per` direct-build behavior must not become a competing permanent construction authority. The prior construction pass classifies it as bootstrap/liveness material until replaced by a typed service-client architecture.

## 11. Construction feedback into Economy

The strongest civilian/construction coupling is:

```text
Economic demand
   |
   v
Infrastructure request
   |
   v
Construction admission
   |
   v
Placement / builders
   |
   v
Foundation / completion
   |
   v
Economic serviceability
   |
   v
Worker allocation
```

This establishes the semantic direction:

**Economy requests infrastructure; Construction provides infrastructure capability; Economy then re-evaluates serviceability.**

Construction should not directly dictate the final worker vector.

## 12. Farm lifecycle

Farms require a specialized contract because stock exposes dependent spatial placement rather than treating farms as ordinary buildings.

The evidence supports:

```text
FOOD DEMAND
   |
   v
FARM CAPACITY DEMAND
   |
   v
FARM ADMISSION
   |
   v
CANDIDATE GENERATION
   |
   v
LEGALITY / COLLISION TEST
   |
   v
PLACEMENT SELECTION
   |
   v
UP-BUILD-LINE / BUILD
   |
   v
PENDING / FOUNDATION
   |
   v
COMPLETE
   |
   v
FARM CAPACITY AVAILABLE
```

Farm placement therefore belongs to Construction's spatial service while the demand signal belongs to Economy/Food.

## 13. Escrow boundary

Civilian evidence shows explicit escrow interactions around Castle Age and resource allocation. The architecture must preserve three separate concepts:

```text
strategic commitment
        !=
economic reservation
        !=
engine execution authorization
```

The existence of an escrow flag is evidence of interaction, not proof of the exact reservation ledger semantics. Exact reserve, consume, release, and cancellation behavior remains a runtime qualification target.

## 14. Terminal-state model

Every civilian/construction request should be capable of reaching one terminal disposition:

```text
CONFIRMED
FAILED + CLASSIFIED
SUPERSEDED
EXPIRED
INVALIDATED
```

`CANCELLED` and `PLACEMENT_FAILED`, for example, are failure classifications or intermediate dispositions; they should not automatically imply the same recovery policy.

### Recommended reconciliation semantics

- **CONFIRMED** — physical evidence satisfies the request contract.
- **FAILED + CLASSIFIED** — expected evidence window closed or explicit failure evidence exists.
- **SUPERSEDED** — a newer generation intentionally replaced the request.
- **EXPIRED** — request remained valid but its deadline/utility window elapsed.
- **INVALIDATED** — prerequisite or policy assumption became false.

This gives AEGIS a common lifecycle language across civilian, construction, production, and later military systems.

## 15. What is actually closed now

### Closed at static architectural level

- civilian production is separated from completed-unit observation;
- villager census is a physical-state boundary;
- worker-role percentages are policy outputs, not task assignments;
- source selection is separate from role allocation;
- dropsite/serviceability feeds worker allocation;
- infrastructure creates an Economy↔Construction feedback loop;
- construction is a stateful lifecycle, not a primitive build call;
- farm construction is specialized spatial execution;
- construction requests are revocable/preemptible;
- generation fencing is required for civilian production attribution;
- direct AEGIS construction should not remain a competing authority.

### Not closed

The following remain runtime/ABI gaps:

1. exact command-to-engine state transition timing;
2. exact same-pass visibility guarantees;
3. exact queue admission/consumption semantics;
4. multiple simultaneous villager-production attribution;
5. exact escrow reservation/release timing;
6. complete worker assignment transition timing;
7. exact idle-worker recovery timing;
8. precise productivity measurement semantics;
9. exact construction pending-placement lifetime;
10. exact builder-assignment side effects;
11. placement reset timing and command persistence;
12. foundation/progress observation latency;
13. exact construction failure causality;
14. all water/trade/civilian interactions;
15. all civilization-specific lifecycle deviations.

## 16. Architectural consequence

The civilian/construction substrate is now mature enough to stop treating worker allocation and construction as isolated modules.

The minimum AEGIS service graph is:

```text
             WORLD MODEL / OBSERVATION
                       |
             +---------+---------+
             |                   |
             v                   v
        STRATEGY             RESEARCH
             |                   |
             +---------+---------+
                       v
                ECONOMIC DEMAND
                       |
              +--------+--------+
              |                 |
              v                 v
          ESCROW          INFRASTRUCTURE
              |                 |
              |                 v
              |          CONSTRUCTION OS
              |                 |
              |                 v
              |          SERVICEABILITY
              |                 |
              +--------> ECONOMY
                                |
                                v
                        ROLE ALLOCATION
                                |
                                v
                          WORKER TASKING
                                |
                                v
                       PHYSICAL EXECUTION
                                |
                                v
                         VERIFICATION
                                |
                                +----> WORLD MODEL
```

## 17. Implementation gate

No implementation should be promoted from candidate to production solely because this lifecycle is statically coherent.

Promotion requires:

- balanced parse;
- unique AEGIS definitions;
- zero undefined AEGIS symbols;
- zero goal collisions;
- unchanged production-root contract unless deliberately gated;
- target-build runtime start;
- controlled lifecycle probes;
- evidence capture for every claimed transition;
- explicit failure classification;
- regression against stock-compatible behavior.

## 18. Next P0 target

Civilian/construction lifecycle closure is now **architecturally sufficient to move upward**.

The next high-value lifecycle should therefore be:

```text
ENEMY OBSERVATION
      -> THREAT ASSESSMENT
      -> STRATEGIC / MILITARY DEMAND
      -> PRODUCTION / TACTICAL REQUEST
      -> OBSERVED FORCE STATE
      -> BATTLEFIELD EFFECT
      -> REASSESSMENT
      -> CONFIRMED / FAILED / SUPERSEDED / EXPIRED / INVALIDATED
```

This is the natural continuation because the stock substrate evidence already shows that `threats.per`, `scoutcontrol.per`, `tsa.per`, `units.per`, `finaling.per`, and strategic state form a coupled military feedback system.

The civilian lifecycle should not be reopened unless new runtime evidence contradicts this static contract.

## Final disposition

**P0 CIVILIAN + CONSTRUCTION LIFECYCLE: STATICALLY CLOSED AT THE ARCHITECTURAL CONTRACT LEVEL.**

**RUNTIME EQUIVALENCE: NOT CLAIMED.**

**AEGIS IMPLEMENTATION PROMOTION: NOT YET AUTHORIZED.**

**NEXT FORENSIC LIFECYCLE: ENEMY OBSERVATION → THREAT → MILITARY RESPONSE → OBSERVED BATTLEFIELD STATE.**
