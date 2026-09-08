# P0 Threat → Military Lifecycle Closure — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Branch:** `aegis/control-plane-2026-09-08-v2`
**Status:** STATIC LIFECYCLE RECONCILIATION / RUNTIME QUALIFICATION INCOMPLETE

## 0. Purpose

This pass closes the next major P0 lifecycle: enemy observation → threat interpretation → military response → observed battlefield state.

It is based on direct inspection of the untouched target-build `Promisory/threats.per` and `Promisory/tsa.per`, plus the repository's existing cross-system, authority, and state/service evidence.

This is forensic reconstruction, not implementation and not a claim of runtime equivalence.

## 1. Direct source evidence

Target machine evidence:

- `Promisory/threats.per` — 1,822 lines
- `Promisory/tsa.per` — 12,769 lines

The threat source directly performs:

- enemy/focus/target player selection;
- closest-enemy searches;
- enemy-pocket detection;
- population/civilian/military observation;
- weighted composition aggregation;
- cavalry/archer/skirmisher/cavalry-archer/gunpowder/infantry/monk/siege estimates;
- military-superiority calculation;
- team-superiority calculation;
- naval strength estimation;
- counter-condition generation.

The TSA source directly performs:

- attack authorization;
- under-attack detection;
- retreat decisions;
- target retargeting;
- attack/retreat priority changes;
- scout reset/return behavior;
- tactical search and movement operations;
- strategy-specific attack/retreat policy.

## 2. Canonical lifecycle

The combined evidence supports this minimum military control loop:

```text
ENGINE / SCOUT OBSERVATION
        ↓
ENEMY CONTEXT
        ↓
THREAT INTERPRETATION
        ↓
MILITARY / STRATEGIC DEMAND
        ↓
COMPOSITION + PRODUCTION REQUIREMENT
        ↓
ATTACK / DEFEND / RETREAT POSTURE
        ↓
TACTICAL EXECUTION
        ↓
OBSERVED FORCE / BATTLEFIELD STATE
        ↓
THREAT REASSESSMENT
```

This must be treated as a feedback controller rather than a one-way target-selection pipeline.

## 3. Enemy identity is not threat state

`threats.per` repeatedly changes `sn-focus-player-number` and `sn-target-player-number` through closest-enemy searches, enemy-pocket selection, attacking-enemy selection, and temporary saved values.

Therefore:

```text
EnemyIdentity ≠ ThreatAssessment ≠ TargetSelection
```

A player number is only an identity/reference. It does not itself encode the meaning of the enemy or the correct military response.

This confirms the authority-boundary decision to split historical `enemy-goal`/focus channels into typed AEGIS state.

## 4. Focus-player selection is an active service

The threat source temporarily changes focus to evaluate different opponents, measures military population, compares those values, and restores the previous focus.

Examples include:

```text
save focus
  ↓
find closest enemy
  ↓
measure military population
  ↓
find next enemy
  ↓
measure military population
  ↓
select / skip target
  ↓
restore focus
```

The existence of temporary focus switching is architecturally important: the historical focus player is a working context, not a stable semantic state.

AEGIS should therefore represent evaluation context explicitly and avoid exposing a mutable global focus register as a public service contract.

## 5. Enemy-pocket detection is spatial threat context

`threats.per` searches around an enemy focus using building-class filters including town centers, farms, towers, walls and gates. It records an `enemy-pocket`, then observes population, civilian population, military population and stables for that pocket.

The resulting abstraction is:

```text
EnemyIdentity
      ↓
SpatialPocket / operating area
      ↓
Local civilian + military + infrastructure state
      ↓
Localized threat assessment
```

This is materially richer than global enemy-player statistics.

## 6. Military composition is an interpreted model

The source constructs separate strategic-number estimates for multiple military categories.

Observed categories include:

```text
camels
cavalry
infantry
spears
husks
 eagles
hoplites
archers
skirms
skirmsarchers
cavarchers
gunpowder
siege
moenche
moenchesiege
```

The estimates are not raw counts. The source applies category-specific transformations, including caps, divisions, multipliers and combined-unit treatment.

Examples include:

- armored elephants contributing to cavalry and siege models with reduced weight;
- war elephants receiving increased weighting;
- organ guns receiving reduced siege weight;
- battering rams receiving reduced siege weight;
- certain unique units being counted directly or with special treatment.

Therefore the AEGIS military model must preserve the distinction:

```text
ObservedComposition
        ↓
InterpretedStrengthModel
```

It must not silently equate unit count with combat strength.

## 7. Threat signal → military policy

The previously established controller rules 6858–6868, 6882–6892 and 6906–6916 convert enemy composition observations into `sn-archer-threat` levels.

The direct military consequence is not necessarily in the same rule. The correct architectural interpretation is:

```text
EnemyObservation
      ↓
ThreatAssessment
      ↓
Counter / Composition Policy
      ↓
MilitaryDemand
```

The exact scheduling boundary remains runtime-unqualified.

## 8. Military superiority is a derived state

`threats.per` computes a difference between local and target military population and then maps the result into a discrete superiority scale.

For Castle-age-or-later contexts, the source uses bands including:

```text
>= 28        → +4
20..27       → +3
12..19       → +2
6..11        → +1
-3..5        → 0
-10..-4      → -1
-18..-11     → -2
<= -19       → -3
```

A different threshold set is used before Castle Age.

This state is then further modified by strategic conditions, technology state, enemy composition, team superiority, assistance, siege state and special situations.

Therefore `sn-military-superiority` is not a raw population difference. It is an interpreted policy signal.

AEGIS should expose:

```text
MilitaryStrengthAssessment
RelativeMilitaryAssessment
Urgency / Confidence
```

rather than reproducing one mutable numeric strategic number as universal state.

## 9. Team superiority is separately interpreted

The source scans ally military populations and subtracts enemy military population from local military population to create `teamsuperiority-number`.

It then maps the result into a discrete team-superiority scale.

This establishes a second military assessment axis:

```text
Local military superiority
        ≠
Team military superiority
```

Military policy may depend on either or both.

## 10. Under-attack lifecycle

TSA provides a concrete defensive lifecycle.

Observed sequence:

```text
civilian casualties / enemy presence
        ↓
under-attack evidence
        ↓
defend = yes
        ↓
underattack = yes
        ↓
defensive tactical response
```

The source detects an attack when enemy units are in the town, the town is under attack, the civilization is marked for defense, and local enemy pressure is sufficiently high relative to military population or superiority.

It later clears `underattack` when enemy presence falls below the relevant threshold or other recovery conditions become true.

Thus `underattack` is a lifecycle state, not a permanent strategic mode.

## 11. Attack authorization is policy, not execution

TSA contains multiple rules that set `attacking := yes` based on:

- military population;
- enemy military population;
- military superiority;
- strategy;
- map and building conditions;
- current age;
- unit composition;
- enemy defenses;
- population capacity.

The source therefore supports:

```text
MilitarySituation
      ↓
AttackAuthorization
      ↓
Tactical Execution
```

`attacking=yes` must not be treated as proof that units are attacking.

This is the military equivalent of the civilian `trainvillager` distinction.

## 12. Retreat is a first-class response

TSA contains numerous explicit retreat triggers.

Examples include:

- enemy military population exceeding local capacity;
- negative military superiority;
- insufficient spears against knight pressure;
- insufficient counters against eagle/camel/skirmisher mass;
- enemy mangonels/scorpions;
- enemy castles/towers under dangerous projectile conditions;
- inadequate siege/knight support;
- strategy-specific counter thresholds.

The source sets `retreatnow=yes` and, in some cases, clears `attacking`.

This establishes:

```text
AttackIntent
      ↓
Continuous viability evaluation
      ├── continue
      ├── retarget
      └── retreat
```

Attack is therefore a revocable state, not a committed one-shot action.

## 13. Retreat execution crosses the service boundary

The strongest direct execution evidence includes `up-retreat-now` and target-point movement operations with `stance-no-attack`.

The source also uses search/filter operations to locate military units and dangerous structures before adjusting tactical posture.

This creates a clear distinction:

```text
Threat / Military Policy
      ↓
Retreat Decision
      ↓
Tactical Service
      ↓
Engine movement/stance operation
      ↓
Observed unit state
```

The engine-facing command remains an execution boundary; it does not itself establish successful relocation.

## 14. Retargeting is a separate lifecycle transition

TSA explicitly changes `sn-target-player-number` and `sn-focus-player-number` back to `enemy-pocket` under conditions involving target military strength, local strength, civilian population, and enemy age.

This proves that a military response can change target without becoming a new global strategic mode.

AEGIS should model:

```text
TargetSelection
  generation
  reason
  evidence
  validity
```

rather than treating target-player as permanent state.

## 15. Scouting ↔ Military is bidirectional

TSA can terminate or alter scouting behavior when military objectives take priority. One observed path resets scout exploration state, stops scouting, and retreats scout cavalry to a stable when military conditions and enemy infrastructure satisfy the rush policy.

Conversely, the broader stock graph already establishes scouting as an input to enemy/threat interpretation.

Therefore:

```text
Scouting → Military intelligence
Military priority → Scouting task allocation
```

Scouting is not a permanently independent background subsystem.

## 16. Production is downstream of military interpretation

The threat model feeds category-level strategic numbers and military-superiority signals. Existing cross-system evidence shows those signals participate in `unit-goal`, ranged-unit state, rush/flush transitions, and production infrastructure decisions.

The resulting AEGIS path is:

```text
ThreatAssessment
      ↓
CompositionDemand
      ↓
ProductionRequest
      ↓
PhysicalForceState
```

This is why Military cannot simply issue direct unit production commands without Strategy/Economy/Production arbitration.

## 17. Military force state is an observation boundary

A production request becomes meaningful only when the corresponding force exists and is observable.

The lifecycle must therefore distinguish:

```text
CompositionDemand
      ≠
ProductionAuthorized
      ≠
ProductionIssued
      ≠
UnitPending
      ≠
UnitObserved
      ≠
ForceAssembled
      ≠
TacticalObjectiveAchieved
```

The stock source strongly supports the first five distinctions. Exact endpoint attribution, queue timing and force-assembly semantics remain runtime qualification targets.

## 18. Battlefield effect must be measured independently

The next observation is not merely “my units exist.” The response must eventually be evaluated against the threat that caused it.

Conceptually:

```text
ThreatAssessment T0
      ↓
MilitaryResponse R0
      ↓
BattlefieldState B1
      ↓
ThreatAssessment T1
      ↓
ResponseDisposition
```

A response can therefore be:

- **CONFIRMED** — observed state satisfies the intended response contract;
- **FAILED + CLASSIFIED** — response did not produce required evidence;
- **SUPERSEDED** — strategic/target generation replaced it;
- **EXPIRED** — its tactical validity window elapsed;
- **INVALIDATED** — prerequisite assumptions became false.

These are AEGIS lifecycle semantics, not stock goal values.

## 19. Generation fencing is mandatory

Military state is particularly vulnerable to stale observations because the source can change focus and target repeatedly.

A typed response record should carry at minimum:

```text
request_id
generation
target_identity
threat_snapshot_id
composition_demand
priority
preconditions
created_from_evidence
valid_until
execution_state
observed_force_state
terminal_disposition
```

A later target selection must supersede an older response explicitly.

## 20. Navy is the same lifecycle on a different battlefield

`threats.per` separately estimates enemy navy using weighted ship categories and derives `maxnavy` from enemy strength and allied/local naval state.

The architectural pattern is therefore reusable:

```text
Water Observation
      ↓
Naval Threat Assessment
      ↓
Naval Demand
      ↓
Naval Production / Tactical Service
      ↓
Observed Navy
      ↓
Reassessment
```

Navy should not be treated as a wholly separate control philosophy; it is a domain specialization of the same observation → interpretation → response → verification lifecycle.

## 21. Counter-model is policy, not truth

The source contains counter logic that suppresses or adjusts strategic categories based on observed enemy composition, such as cavalry, archer, skirmisher, siege and special civilization units.

These are policy heuristics. They should not be elevated to immutable combat truth.

AEGIS should preserve:

```text
Observed fact
      ↓
Interpretation / estimate
      ↓
Counter recommendation
```

and retain provenance so later calibration can distinguish measurement from policy.

## 22. Byzantine architecture consequence

For AEGIS-BYZ, Byzantine-specific military cognition belongs above the substrate:

```text
Stock-compatible observation ABI
        ↓
Universal threat / strength model
        ↓
Byzantine strategic interpretation
        ↓
Counter-composition demand
        ↓
Economy / Production arbitration
        ↓
Military tactical execution
```

The Byzantine layer should be able to value defensive continuity, cost-effective counter units, map topology, timing windows, fortification and combined-arms transitions without contaminating the universal observation ABI.

## 23. Static lifecycle ledger

| Stage | Evidence | AEGIS owner | Status |
|---|---|---|---|
| Enemy identity | focus/target player selection | Scouting / World Model | static supported |
| Enemy observation | population, military, unit composition | World Model / Scouting | static supported |
| Spatial pocket | local building/object search | Scouting / Threat | static supported |
| Threat interpretation | weighted composition / threat signals | Threat OS | static supported |
| Relative strength | military/team superiority | Threat OS | static supported |
| Strategic response | attack/defend/retreat policy | Strategy + Military | static supported |
| Composition demand | category-level military state | Military / Production boundary | static supported |
| Production request | unit-goal / production policy | Production OS | static topology supported |
| Tactical command | attack/retreat/movement primitives | Military OS | command ABI runtime gap |
| Force observation | unit population/composition | World Model | static observation supported |
| Battlefield reassessment | new enemy/force measurements | Threat OS | architecture supported |
| Terminal disposition | confirmed/failed/superseded/etc. | Verification & Recovery | architecture target |

## 24. What is now statically closed

This pass establishes the military lifecycle contract at the architectural level:

- enemy identity is distinct from threat meaning;
- focus/target are mutable evaluation contexts;
- enemy pockets provide localized spatial threat state;
- military composition is an interpreted weighted model;
- military superiority is derived policy state;
- team superiority is a separate assessment axis;
- under-attack is a recoverable lifecycle state;
- attack authorization is distinct from tactical execution;
- retreat is a first-class, revocable response;
- retargeting is an explicit lifecycle transition;
- scouting and military influence one another;
- production is downstream of military interpretation;
- observed force state is separate from production authorization;
- battlefield effect must feed threat reassessment;
- generation/freshness fencing is mandatory;
- naval response follows the same general lifecycle.

## 25. What remains runtime-unqualified

The following are intentionally not frozen:

1. exact interpreter ordering across `threats.per` and `tsa.per`;
2. same-pass visibility of threat/military mutations;
3. exact focus-player restoration timing;
4. target/focus persistence epochs;
5. exact latency from attack authorization to tactical execution;
6. exact semantics and side effects of `up-retreat-now`;
7. exact movement completion evidence;
8. exact force-assembly definition;
9. endpoint attribution for production responses;
10. exact projectile-detection timing;
11. exact scout reset/return timing;
12. exact naval command completion semantics;
13. all conditional compilation branches and runtime modes;
14. civ-specific counter semantics;
15. exact terminal failure causality.

## 26. Architectural freeze decision

Freeze now:

```text
EnemyObservation
      ↓
EnemyContext
      ↓
ThreatAssessment
      ↓
Strategic / Military Demand
      ↓
Production / Tactical Request
      ↓
Engine Execution
      ↓
Observed Force / Battlefield State
      ↓
Verification / Recovery
```

Do not freeze yet:

```text
numeric threat thresholds
strategic-number slots
timer allocations
same-pass scheduling
command completion latency
focus/target persistence
combat-effect attribution
```

The stock numeric thresholds remain valuable calibration evidence, but they are not yet the AEGIS ABI.

## 27. Implementation gate

No military implementation should be promoted to production solely from this static closure.

Promotion requires:

- parser validation;
- unique AEGIS symbols;
- no undefined state references;
- no goal/strategic-number collisions;
- disposable target-build package;
- controlled enemy-composition probes;
- controlled attack/retreat probes;
- target-switch probes;
- force-observation probes;
- failure and recovery capture;
- stock-regression comparison.

## Final disposition

**P0 THREAT → MILITARY LIFECYCLE: STATICALLY CLOSED AT THE ARCHITECTURAL CONTRACT LEVEL.**

**RUNTIME EQUIVALENCE: NOT CLAIMED.**

**AEGIS MILITARY IMPLEMENTATION: NOT YET AUTHORIZED.**

The next high-value layer is the **Research → Capability Change → Strategy/Production/Military lifecycle**, followed by the cross-service verification/recovery pass that joins all four closed lifecycles.