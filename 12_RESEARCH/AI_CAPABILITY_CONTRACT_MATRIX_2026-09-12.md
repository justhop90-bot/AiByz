# AEGIS Capability Contract Matrix — HD × Promisory × AIBuilder × AEGIS

**Date:** 2026-09-12  
**Status:** Research/architecture authority; no production behavior changes  
**Scope:** Ten competence mechanics identified in the comparative audit.  
**Implementation rule:** preserve AIBuilder execution ownership; import functional contracts, not historical topology.

---

## 0. Reading this matrix

This matrix distinguishes four different things:

1. **HD evidence** — what the stock `AI (HD version).per` demonstrably does.
2. **Promisory evidence** — how the later, substantially richer `.per` system operationalizes the same class of problem.
3. **AIBuilder capability** — what the preserved current execution substrate already supplies.
4. **AEGIS contract** — the behavior AEGIS should eventually implement, with explicit ownership and verification boundaries.

A primitive being available does **not** mean its semantics are fully understood. A historical implementation being successful does **not** mean its exact implementation should be copied. A command being issued does **not** mean the world changed.

Evidence classes used below:

- **DIRECT** — explicit source rule/primitive establishes the fact.
- **COMPOSED** — multiple direct source facts establish the contract.
- **INFERRED** — behavior inferred from rule relationships; requires qualification before promotion.
- **AEGIS-GENERALIZATION** — design contract derived from repeated historical patterns rather than a literal historical rule.
- **UNCERTAIN** — unresolved engine or historical semantics.

---

# 1. Master matrix

| # | Capability | HD | Promisory | AIBuilder | AEGIS target | Current disposition |
|---|---|---|---|---|---|---|
| 1 | Phase-driven policy | Mature | Mature + specialized | **Strong** | Preserve phase authority; add bounded policy overlays | **PROTECT** |
| 2 | Economic worker control | Strong baseline | **Much deeper** | Moderate | Objective-driven resource allocation + retasking + verification | **P1 BUILD** |
| 3 | Information scouting | Strong baseline | **Much deeper** | Native explorer substrate | Observation/classification without taking explorer ownership | **P1 BUILD** |
| 4 | Threat telemetry/reaction | Present | **Explicit telemetry layer** | Sparse | Threat observation → state → response authorization | **P1 BUILD** |
| 5 | Boar lifecycle | Mature | **Dedicated stateful subsystem** | Native baseline | Safe lure authorization + support + recovery | **P1 BUILD** |
| 6 | Escrow/feasibility | Strong | **Explicit production arbitration** | Strong research substrate | Resource reservation + feasibility before authorization | **P1 BUILD** |
| 7 | Pending/completion construction | Strong | **Very extensive** | **Present and operational** | request → pending → completion → verification | **P0 FORMALIZE** |
| 8 | Geometry/search | Present | **Heavy tactical use** | Sparse | bounded search + distance + terrain/exploration state | **P1 BUILD** |
| 9 | Dynamic military lifecycle | Strong baseline | **Much deeper** | Moderate | army readiness → attack → retreat/recovery → reassessment | **P1 BUILD** |
| 10 | Defense/infrastructure | Strong baseline | **Specialized/proactive** | Strong construction substrate | threat-conditioned defensive requirement + placement + recovery | **P1 BUILD** |

---

# 2. Capability 1 — Phase-driven policy projection

## Historical contract

### HD

Stock HD uses a large phase-control layer to project age/phase state into desired economic, construction, military, technology, and exploration settings.

**Functional contract:** phase is not merely a label; it is a policy projection mechanism.

### Promisory

Promisory retains phase/age-driven policy but layers specialized state machines over it. Its modules divide responsibility more sharply: initialization, dawn behavior, economy/gatherers, scouting, buildings, units, research, trade, and finaling.

### AIBuilder

AIBuilder provides the cleanest preserved control-plane baseline for AEGIS. `phaseUpdate.per` assigns phase-specific desired values including exploration, housing, town-center, economic, construction, and military policy.

The recent AEGIS regression proved the architectural consequence: removing the phase assignments can disable downstream behavior even when the construction and explorer execution rules remain intact.

## Contract

```text
CURRENT PHASE
→ derive desired policy
→ expose desired goals/SNs
→ downstream subsystem reads policy
→ downstream executes
→ reassess on phase/state transition
```

## Preconditions

- phase/age state is valid
- phase owner has not been superseded
- required policy symbols exist

## Authority

**Owner:** `phaseUpdate.per` for phase-derived policy.  
**Non-owner:** AEGIS policy modules must not silently rewrite phase-owned outputs.

## Action

Set policy goals/SNs consumed by economy, construction, military, research, and exploration modules.

## Verification

Verify downstream consumer observes the desired value. Do not infer success merely because `set-goal` or `set-strategic-number` executed.

## Failure

If a phase output is absent or conflicting, preserve the known-good AIBuilder value and log/classify the conflict rather than replacing the control plane.

## AEGIS insertion point

**Above AIBuilder execution, below world-state classification.** AEGIS should produce narrow policy overlays, not a replacement phase machine.

**Evidence:** DIRECT/COMPOSED.

**Status:** **PRESERVE / PROTECTED INTERFACE.**

---

# 3. Capability 2 — Economic worker control

## Historical contract

### HD

HD manages resource allocation through gatherer counts, resource percentages, dropsite distances, farm/hunting controls, and economic goals.

### Promisory

Promisory materially extends this with explicit gatherer manipulation:

- `up-retask-gatherers`
- `up-drop-resources`
- `up-idle-unit-count`
- object cargo/state checks
- path/distance checks
- resource-class filtering

The UserPatch history explicitly describes `up-retask-gatherers` as a mechanism for requesting gatherers to transition to preferred resources after dropping resources, including hunting/foraging/fishing classes. citeturn0search10

### AIBuilder

AIBuilder has strong resource-percentage and phase-driven economic policy but does not demonstrate the same worker-level retasking density.

## Contract

```text
STRATEGIC OBJECTIVE
→ resource requirement
→ current stock + income state
→ worker requirement
→ feasibility
→ retask/allocate
→ verify worker/resource transition
→ reassess
```

## Preconditions

- objective exists
- resource requirement is defined
- worker/resource class is identifiable
- competing higher-priority reservation is absent

## Authority

**Current owner:** AIBuilder economy/gatherer machinery.  
**Future AEGIS owner:** a narrowly scoped economic policy layer; worker execution remains delegated.

## Action

Prefer native retasking/percentage mechanisms before direct unit-level control.

## Verification

Check worker counts, idle state, resource task, and/or cargo transition. A requested retask is not equivalent to successful reassignment.

## Failure

If the preferred resource is unavailable, dropsite/path constraint fails, or target worker count cannot be reached, retain the objective but mark feasibility failure and reassess.

## Expiry

Resource objectives expire when the strategic requirement disappears or phase/strategy changes.

## AEGIS insertion point

Between objective/requirements and AIBuilder economy execution.

**Evidence:** COMPOSED for the historical contract; AEGIS execution mapping is AEGIS-GENERALIZATION.

**Status:** **P1 — high-value vertical slice.**

---

# 4. Capability 3 — Information scouting

## Historical contract

### HD

HD uses explorer goals and explicit scout control. Scouting is tied to enemy discovery, map exploration, target selection, and military policy.

### Promisory

Promisory uses `up-send-scout`, `scoutcontrol.per`, exploration strategic numbers, player search, point exploration, and geometry. It can deliberately send scouts toward known enemy locations.

The UserPatch documentation is explicit that `scout-enemy` targets the nearest known building of the target enemy, but only after that enemy town has actually been located; it is not a cheat mechanism. citeturn0search10

The command index also documents `up-send-scout`, `up-reset-scouts`, `up-point-explored`, and `up-path-distance`. citeturn0search3

### AIBuilder

AIBuilder's native explorer ownership is important and currently functional when its phase policy is intact.

## Contract

```text
EXPLORER AVAILABILITY
→ observation task
→ route/target selection
→ send/explore
→ evidence acquired
→ classify
→ write observation state
→ return/reassign
```

## Preconditions

- explorer exists / explorer group is permitted
- target is valid under engine rules
- no higher-priority explorer task owns the scout

## Authority

**Owner today:** AIBuilder general/phase explorer machinery.  
**AEGIS rule:** AEGIS must not become a second owner of `desired-military-explorers`, `sn-number-explore-groups`, or equivalent explorer controls without an explicit authority transition.

## Verification

Evidence is the newly observed map/player/object state, not the scout command.

## Failure

No target, blocked route, lost scout, invalid target knowledge, or conflicting explorer policy → record failure and retain/recompute exploration objective.

## Expiry

Observation state becomes stale; target knowledge requires refresh.

## AEGIS insertion point

**Observation/classification layer only initially.** Let AIBuilder own physical scout dispatch.

**Evidence:** DIRECT/COMPOSED.

**Status:** **P1 — high-value, but ownership-sensitive.**

---

# 5. Capability 4 — Threat telemetry → response

## Historical contract

### HD

HD exposes threat handling and military reaction through threat rules and attack/defense controls.

### Promisory

Promisory explicitly calls:

```text
up-get-threat-data
    → threat time
    → threat player
    → threat source
    → threat target
```

The Encyclopedia classifies `up-get-threat-data` as a high-value UP action and defines it as retrieving the elapsed time, player, source, and target of the last threat. citeturn0search3

## Contract

```text
THREAT EVENT
→ telemetry acquisition
→ threat classification
→ contextual threat state
→ response requirement
→ feasibility
→ authorize response
→ production/execution
→ verify
→ expire/reassess
```

## Preconditions

- threat telemetry available
- threat is temporally relevant
- threat source/target is classifiable

## Authority

**Observation owner:** threat telemetry module.  
**Response owner:** strategy/military policy.  
**Production owner:** existing AIBuilder military production channel.

These must not be collapsed into one writer.

## Action

Write a bounded threat state; do not immediately assert a strategic counter.

## Verification

Require subsequent evidence: military composition, attack state, defensive structure, or production state change.

## Failure

Threat stale, source unclassifiable, response unaffordable, production unavailable, or response already satisfied.

## Expiry

Threat state must decay/expire based on time and new observations. Exact decay constants require source-specific qualification.

## AEGIS insertion point

This is the cleanest Layer-2 → Layer-3 bridge currently available.

**Evidence:** DIRECT for telemetry; AEGIS response lifecycle = COMPOSED/AEGIS-GENERALIZATION.

**Status:** **P1 / flagship vertical slice.**

---

# 6. Capability 5 — Boar lifecycle and support

## Historical contract

### HD

HD has mature hunting/boar controls and specialized resource-management rules.

### Promisory

Promisory has a dedicated `boarhunting.per` state machine using boar distance, hunt/lure group sizes, minimum hunters, support requests, search state, and recovery.

UserPatch specifically distinguishes:

- `sn-minimum-boar-lure-group-size` — threshold for starting a lure
- `sn-minimum-boar-hunt-group-size` — desired active hunter group during a lure
- `sn-minimum-number-hunters` — hunter demand
- hunter-request behavior

The UserPatch documentation also states that `up-retask-gatherers` can be combined with `sn-minimum-number-hunters` to make forced hunting easier. citeturn0search10

## Contract

```text
BOAR OPPORTUNITY
→ safety/feasibility check
→ lure authorization
→ lurer assignment
→ support demand
→ hunt state
→ completion/depletion/loss
→ reset/reassign
```

## Preconditions

At minimum:

- sufficient villagers
- safe/valid lure conditions
- hunt group threshold satisfied
- food value still justifies action

Exact historical thresholds must remain source-specific.

## Authority

Boar subsystem owns boar-specific hunter policy. General economy owns final resource balancing.

## Action

Set native boar/hunter strategic numbers or invoke support behavior; do not manually force individual villagers unless justified by a later contract.

## Verification

Check hunter population, live boar state/distance, gatherer activity, and food acquisition.

## Failure

Lure lost, boar dead, insufficient hunters, unsafe distance, blocked path, or food objective no longer relevant.

## AEGIS insertion point

A narrowly scoped safety/authorization overlay on top of native hunting.

**Evidence:** DIRECT/COMPOSED.

**Status:** **P1; candidate only until qualification.**

---

# 7. Capability 6 — Escrow and feasibility

## Historical contract

### HD / Promisory

The historical systems distinguish ordinary resource checks from escrow-aware feasibility. Relevant predicates include:

```text
can-research-with-escrow
can-train-with-escrow
```

The conceptual contract is resource reservation: an objective can reserve or account for resources before competing systems consume them.

## Contract

```text
OBJECTIVE
→ cost requirement
→ reserved/escrowed resources
→ remaining availability
→ can-authorize?
→ commit
→ consume/release
→ reassess
```

## Preconditions

- cost is known
- reservation semantics are valid
- prerequisite technology/building exists

## Authority

Escrow/feasibility determines whether an action can be authorized. Production/build/research modules remain responsible for execution.

## Action

Use engine-supported escrow predicates rather than inventing a parallel resource accounting system where possible.

## Verification

Authorization must be followed by observable production/research/pending state.

## Failure

Cost changes, prerequisite disappears, competing commitment consumes resources, or action fails to enter pending/execution state.

## Expiry

Reserved purpose must be released when the objective expires or becomes infeasible.

## AEGIS insertion point

Between requirements and authorization.

**Evidence:** DIRECT for escrow predicates; broader AEGIS reservation lifecycle = COMPOSED/AEGIS-GENERALIZATION.

**Status:** **P1.**

---

# 8. Capability 7 — Pending/completion-aware construction

## Historical contract

### HD / Promisory / AIBuilder

This is one of the clearest native contracts.

The Encyclopedia documents:

```text
up-pending-objects
up-pending-placement
```

as distinct mechanisms. citeturn0search3

AIBuilder construction already uses pending-object checks for housing and other construction decisions.

## Contract

```text
DESIRED COUNT
→ candidate authorization
→ build request
→ pending object / pending placement
→ completed object
→ verify count
→ release requirement
```

## Critical invariant

```text
command issued ≠ pending ≠ completed
```

## Preconditions

- desired count > current completed count
- no sufficient pending object already exists
- build prerequisites valid
- placement can be attempted

## Authority

Construction module owns physical building execution. Policy modules own desired requirements.

## Verification

Completed object count is the authoritative postcondition for ordinary building completion.

## Failure

Placement rejected, builder unavailable, prerequisite absent, build canceled, or pending object disappears.

## Recovery

Reset/clear blocked placement when the engine permits it, then reassess.

## AEGIS insertion point

**Already inside the execution substrate.** AEGIS should formalize the lifecycle rather than replace it.

**Evidence:** DIRECT.

**Status:** **P0 — canonical reference slice.**

---

# 9. Capability 8 — Geometry/search intelligence

## Historical contract

Promisory makes extensive tactical use of:

- `up-get-search-state`
- `up-get-point-distance`
- `up-path-distance`
- `up-point-explored`
- `up-find-player`
- `up-get-fact`

The command index classifies search state and path-distance as very-high-value primitives, and point/exploration queries as high-value. citeturn0search3

## Contract

```text
SEARCH SPACE
→ filter candidate objects/points
→ geometric constraints
→ candidate set
→ select target
→ execute through native action channel
→ verify result
```

## Preconditions

- search state initialized/reset correctly
- target class exists
- geometry reference is valid

## Authority

Search module computes candidate evidence; policy module selects strategic intent; execution module performs action.

## Action

Use native search/geometry primitives before introducing external geometry machinery.

## Verification

Check selected target/state after action rather than trusting the search result as world state.

## Failure

No candidate, stale search state, invalid point, unreachable path, or target disappears.

## AEGIS insertion point

A reusable **observation/candidate-generation service**, not a monolithic tactical brain.

**Evidence:** DIRECT/COMPOSED.

**Status:** **P1.**

---

# 10. Capability 9 — Dynamic military lifecycle

## Historical contract

### HD

HD has explicit attack status, attack timing, retreat, scaling, and military group controls. Historical constants include:

```text
retreat-now-goal = 20
attack-status-goal = 24
restart-attack-goal = 27
```

The exact semantics of each state transition remain source-specific.

### Promisory

Promisory goes considerably further with attack-group sizing, targeting, projectile detection, resets, retreat, and scaling controls.

The Encyclopedia documents `up-retreat-now`, `up-reset-unit`, `up-reset-target-priorities`, `up-projectile-detected`, `up-projectile-target`, and attack/explorer group controls. citeturn0search3

### AIBuilder

AIBuilder provides attack-group policy, attack timing, military percentages, and production execution.

## Contract

```text
MILITARY OBJECTIVE
→ required army composition/size
→ production feasibility
→ readiness
→ attack authorization
→ movement/engagement
→ threat assessment
→ retreat/recovery if necessary
→ result assessment
→ restart/continue/terminate
```

## Preconditions

- army requirement defined
- sufficient/feasible military strength
- strategic attack authorization
- no overriding defense condition

## Authority

Military policy owns authorization. Military behavior owns unit behavior. Military production owns unit creation.

## Verification

Army existence, group size, target engagement, retreat state, and subsequent strategic state must be observed independently.

## Failure

Insufficient force, unfavorable threat, path failure, target disappearance, army loss, or retreat trigger.

## Expiry

Attack authorization expires when objective, target, timing window, or force condition changes.

## AEGIS insertion point

Above `militaryBehavior.per` and `militaryUnits.per`; never replace them wholesale.

**Evidence:** DIRECT/COMPOSED.

**Status:** **P1.**

---

# 11. Capability 10 — Defense and proactive infrastructure

## Historical contract

### HD

Defense is tied to threat, building, military, and strategic-number systems.

### Promisory

Promisory has specialized building/defensive behavior, placement handling, targeting priorities, and recovery controls.

The command index includes `up-set-defense-priority`, `up-reset-target-priorities`, `up-reset-placement`, and related defensive/search operations. citeturn0search3

### AIBuilder

AIBuilder has a robust construction substrate and phase-driven building targets. Housing demonstrated that this substrate depends heavily on upstream policy outputs.

## Contract

```text
THREAT / MAP / ECONOMIC CONDITION
→ defensive requirement
→ building/unit feasibility
→ authorization
→ placement/production
→ pending
→ completion
→ defensive effect
→ reassess
```

## Preconditions

- actual defensive requirement exists
- resource/building feasibility exists
- placement is legal

## Authority

Policy determines requirement; construction/military modules execute.

## Verification

Building completion, military presence, or defensive targeting state must be observed.

## Failure

Placement blocked, resources unavailable, threat disappears, or requirement becomes obsolete.

## Recovery

Clear blocked placement / alter requirement / defer and reassess.

## AEGIS insertion point

Threat/strategy layer feeding the existing AIBuilder construction and military channels.

**Evidence:** COMPOSED.

**Status:** **P1.**

---

# 12. Cross-mechanic state ownership matrix

| State | Primary owner | Readers | Forbidden duplicate owner |
|---|---|---|---|
| phase | phaseUpdate | all downstream policy | AEGIS behavioral modules |
| desired explorer count | phase/general | scout/explorer execution | ScoutControl candidate |
| worker allocation policy | economy | gatherers/construction | isolated behavior modules |
| threat telemetry | threat observation | strategy/military | production module |
| threat classification | strategy/policy | response modules | raw telemetry writer |
| boar hunt policy | boar subsystem | gatherers/economy | generic economy override |
| resource reservation | escrow/authorization | production/research | independent spenders |
| pending building | construction/engine | policy | strategy module |
| completed building | world observation | all policy | command issuer |
| search state | search operation | tactical consumer | unrelated module |
| attack authorization | military policy | military behavior | construction/economy |
| unit execution | military behavior | verification | strategy |
| defensive requirement | strategy | construction/military | direct builder |

---

# 13. Common failure modes exposed by the comparison

## Failure A — replacing phase policy

**Observed consequence:** houses and scouting degraded even though downstream mechanisms still existed.

**Rule:** never replace a proven upstream policy projection without reconstructing every downstream dependency.

## Failure B — one rule owns observation + strategy + execution

Promisory's competence is partly attributable to separating specialized concerns. AEGIS should preserve that separation.

## Failure C — command = completion

Every construction, production, scout, and military action must distinguish:

```text
requested
→ accepted/pending
→ world state changed
→ verified
```

## Failure D — static counters without feasibility

A target number is not a commitment. Resource availability, prerequisites, pending state, and competing objectives matter.

## Failure E — competing explorer ownership

`up-reset-scouts` and explorer strategic numbers demonstrate that scout control is a shared engine mechanism. AEGIS must not fight AIBuilder's native explorer machinery.

## Failure F — threat classification without contextual verification

A cavalry-related observation does not by itself prove a cavalry army or require a specific counter.

## Failure G — over-copying Promisory topology

Promisory is evidence of functional solutions, not a requirement to reproduce its module tree.

---

# 14. AEGIS promotion ladder for all ten capabilities

Every candidate should progress through:

```text
HISTORICAL OBSERVATION
        ↓
SOURCE RULE IDENTIFIED
        ↓
FUNCTIONAL CONTRACT
        ↓
AIBuilder CHANNEL IDENTIFIED
        ↓
OWNERSHIP REVIEW
        ↓
SYMBOL/ABI CLEARANCE
        ↓
STATIC IMPLEMENTATION
        ↓
LOAD QUALIFICATION
        ↓
CONTROLLED BEHAVIOR QUALIFICATION
        ↓
FAILURE/RECOVERY QUALIFICATION
        ↓
PROMOTION
```

No stage may be skipped because a historical implementation “worked.”

---

# 15. Priority order

### P0 — Protect / formalize

1. AIBuilder phase policy
2. Pending/completion construction contract
3. Writer/reader ownership boundaries
4. Command-vs-world-state evidence boundary

### P1 — Build vertical slices

5. Threat telemetry → contextual threat state
6. Escrow/feasibility → authorization
7. Scout information lifecycle
8. Boar safety/support lifecycle
9. Gatherer retasking/resource continuity
10. Geometry/search candidate generation
11. Military attack/retreat lifecycle
12. Threat-conditioned defensive infrastructure

### P2 — Integrate

Only after individual slices are qualified should they be coupled into a general AEGIS arbitration loop.

---

# 16. Canonical AEGIS contract generated from the comparison

The ten mechanics converge on one common lifecycle:

```text
WORLD
 ↓
OBSERVATION
 ↓
CLASSIFICATION
 ↓
STATE / BELIEF
 ↓
TRANSITION DETECTION
 ↓
OBJECTIVE
 ↓
REQUIREMENTS
 ↓
CONSTRAINTS / FEASIBILITY
 ↓
CANDIDATES
 ↓
EVALUATION
 ↓
COMMIT / RESERVATION
 ↓
AUTHORIZE
 ↓
AIBuilder EXECUTION CHANNEL
 ↓
PENDING / TRANSITION EVIDENCE
 ↓
VERIFY
 ↓
SUCCESS / FAILURE
 ↓
RELEASE / RECOVER
 ↓
EXPIRY
 ↓
REASSESS
```

This is the principal architectural result of the four-way comparison.

The historical systems repeatedly solve variants of this lifecycle even when their source code does not express it as a formal state machine.

---

# 17. Evidence boundaries

### Confirmed

- AIBuilder phase policy is a critical upstream control plane.
- Native `.per` provides high-value scouting, threat, search, pending-object, resource-retasking, and military recovery primitives. citeturn0search0turn0search3
- Promisory uses specialized subsystems for threats, gatherers, scouting, boar hunting, buildings, and military behavior.
- UserPatch explicitly documents the operational contracts of scout-enemy and gatherer retasking. citeturn0search10

### Probable

- Promisory's specialization and state separation materially contribute to robustness.
- AEGIS can reproduce a large fraction of the functional advantages without XS.

### Unresolved

- Exact numeric thresholds and decay constants for individual historical mechanisms.
- Exact engine semantics where the source documentation is incomplete.
- Runtime causal success of new AEGIS writers.

---

# 18. Next audit artifact

The next artifact should be a **source-rule ledger**, not another architecture essay. For each of the ten capabilities it should enumerate:

```text
source file
line/rule identifier
primitive
symbol
writer(s)
reader(s)
input state
output state
precondition
action
postcondition
failure
expiry
reassessment
AIBuilder equivalent
AEGIS owner
ABI requirements
evidence class
promotion status
```

That ledger becomes the authoritative bridge from archaeology to implementation.
