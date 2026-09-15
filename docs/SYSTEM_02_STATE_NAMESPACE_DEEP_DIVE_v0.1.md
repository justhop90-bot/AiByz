# System 02 — State / Namespace: Forensic Deep Dive of Shadow DC7

**Artifact:** `docs/SYSTEM_02_STATE_NAMESPACE_DEEP_DIVE_v0.1.md`  
**Repository:** `justhop90-bot/AiByz`  
**Branch:** `main`  
**Donor:** `Shadow DC7(1).per`  
**Donor SHA-256:** `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`  
**Donor:** 615,773 bytes; 22,603 physical lines.

## Executive verdict

Shadow does not contain one homogeneous state namespace. Its goals, strategic numbers, timers, coordinates, and constants form several distinct semantic layers that happen to share primitive storage. The forensic reconstruction identifies: **control-plane state, belief/classification state, derived metrics, transient procedural/FSM state, engine/effect-plane state, and historical/scratch state**.

The strongest Shadow control-plane candidates are:

- `gl-strategy`
- `gl-strategy-type`
- `gl-current-build-item`
- `gl-build-progress`
- `gl-progression-pause`
- `gl-enemy-strategy`
- `gl-enemy-strategy-type`
- `gl-target-age`
- `gl-dark-build`
- `gl-need-vills`
- `gl-attacking`
- `gl-defend-town`
- `gl-town-safe`
- `gl-find-new-target`
- `gl-raid-status`
- `gl-escrow-state`
- `gl-age-loading`
- `gl-position`

They do not all have equal authority. The first five form the strategic/progression nucleus; the others are belief, domain-control, or transaction state.

The central AEGIS conclusion is:

> **Do not transplant Shadow's namespace. Reconstruct its semantic state machine and re-home only state whose authority, lifetime, writers, readers, and causal effect can be demonstrated.**

The correct registry model is:

`SYMBOL → SEMANTIC TYPE → DOMAIN → WRITERS → READERS → INITIAL VALUE → RESET → LIFETIME → PRECEDENCE → EFFECT → EVIDENCE → OWNER`

---

## 1. Forensic basis

The donor itself reports `GOALS: 1-317, 392,478-479` and `TIMERS: 1-42, 46`, then defines the major state slots including `gl-town-under-attack`, `home-x/y`, `gl-position`, `gl-attacking`, `gl-town-safe`, `gl-find-new-target`, group state, raid state, threat state, and `gl-build-progress`.

The full lexical audit found approximately:

- **1,482 `defconst` definitions**
- **130 goal symbols with explicit `set-goal` writers**
- **76 goal symbols with recognizable goal predicates**
- **103 strategic-number symbols with explicit writes**
- **13 compile-time `#load-if-defined` branches**
- timers spanning the donor's declared 1–42 and 46 range.

These counts are inventory evidence, not semantic proof. Some variables are accessed through `up-compare-goal`, `up-modify-goal`, target-fact commands, point commands, and other engine operations. Classification therefore uses writer/reader topology and effect rather than frequency alone.

The AI scripting reference confirms that goals are mutable integer storage, while strategic numbers may alter built-in AI behavior and therefore cannot automatically be treated as generic storage. This distinction is fundamental to the audit.

---

## 2. The state classes

### A. Control-plane state

Persistent or semi-persistent values that select strategy, progression, objective, commitment, or domain authority.

### B. Belief/classification state

Values derived from observations and retained as the AI's current interpretation of the world.

### C. Derived state

Measurements, scores, evaluations, counters, or other values that can be recomputed from current observations/state.

### D. Transient procedural state

Finite-state-machine registers, target-search phases, movement/fire gates, group modes, waypoint state, scratch latches, and temporary coordinates.

### E. Engine/effect-plane state

Strategic numbers and timers that alter built-in engine behavior or enforce temporal guards.

### F. Historical/scratch state

Generic registers, debug identity constants, dead branches, aliases, compatibility residue, and variables with no justified live architectural role.

The critical distinction is that **storage primitive ≠ semantic type**. A goal can be strategic, derived, transient, or scratch. A strategic number can be an engine actuator rather than a strategic belief.

---

# 3. Core control plane

## 3.1 `gl-strategy`

**Classification:** CONTROL-PLANE / PRIMARY AUTHORITY.

It is written only a few times but read across economy, military, scouting, progression, technology, and production. Its values include `FLUSH` and `KRUSH`. This is a classic low-writer/high-fanout authority variable.

**Disposition:** preserve the concept, replace the raw two-value integer model with typed strategic state. AEGIS should record doctrine, objective, priority, reason, confidence, start time, expiry, and predecessor/successor.

---

## 3.2 `gl-strategy-type`

**Classification:** CONTROL-PLANE / SECONDARY STRATEGIC DIMENSION.

The donor uses values such as `FLUSH` and `FC`. It appears to distinguish strategic subtype/progression mode from the primary strategy.

**Disposition:** preserve only after confirming that it is semantically distinct from `gl-strategy`; otherwise collapse after proof of equivalence.

---

## 3.3 `gl-current-build-item`

**Classification:** CONTROL-PLANE / PROCEDURAL AUTHORITY / SCHEDULER CURSOR.

Approximately 61 writes and 138 recognizable reads. Values include `IRONCASTING`, `FORGING`, `CHAINBARDING`, `SCALEBARDING`, `CUP`, `FLTCH`, `LAA`, `PAA`, `BODKIN`, `EXTRA-STABLES`, `MONASTERY`, `MARKET1`, `RANGES`, `ESKIRMS`, `SW1/SW2`, `RAX`, `SMITH`, `FARMS`, `LC1–LC4`, `MILL1`, mining camps, `UNIVERSITY`, and `BALLISTICS`.

This is not merely status. It is the cursor through an implicit strategic/economic scheduler.

**Disposition:** GENERALIZE and preserve. Model conceptually as `commitment.current_objective`, not as a donor-specific enumeration.

---

## 3.4 `gl-build-progress`

**Classification:** CONTROL-PLANE / PROGRESSION STATE.

Approximately 59 writes. It is paired with `gl-current-build-item` and carries progression counters such as `IronCastingNumber`, `ForgingNumber`, `Stable1Number`, `RangesNumber`, `UniversityNumber`, etc.

The pair forms an implicit progression machine:

`strategy → current item → progress → pause → resource/escrow gate → executor → next item`

**Disposition:** preserve the progression abstraction; replace opaque integer encodings with explicit commitment/progress state.

---

## 3.5 `gl-progression-pause`

**Classification:** CONTROL-PLANE / PREEMPTION-SERIALIZATION STATE.

Approximately 15 writes and 68 reads. Values include progression targets and `-1`. Production rules test it to suppress competing actions.

This is effectively a hidden **lock/preemption mechanism**.

**Disposition:** preserve the mechanism but formalize it as `UNLOCKED | RESERVED_FOR(X) | PREEMPTED_BY(X) | SUSPENDED`, with explicit owner, priority, expiry, and release semantics.

---

# 4. Belief and world-model state

## 4.1 `gl-enemy-strategy`

**Classification:** BELIEF / CLASSIFICATION STATE.

Values include `POSSIBLE-KRUSH`, `KRUSH`, `DRUSH`, `FLUSH`, and `SCRUSH`.

The donor converts enemy age, buildings, units, and timing into these classifications. The raw facts are observations; `gl-enemy-strategy` is the AI's retained hypothesis.

**Disposition:** PRESERVE + GENERALIZE + IMPROVE.

AEGIS should add confidence, evidence provenance, observation time, freshness, competing hypotheses, and invalidation/hysteresis. A stale classification must not masquerade as world truth.

## 4.2 `gl-enemy-strategy-type`

**Classification:** BELIEF SUBTYPE / DERIVED CONTROL INPUT.

Values include `FC`, `FLUSH`, and `RANGED-FLUSH`. Treat it as a dependent classification, not independent strategic truth.

## 4.3 `gl-target-age`

**Classification:** RETAINED EXTERNAL-STATE BELIEF.

The donor initializes it to `DA`, then advances it as observed enemy age changes. This is stateful observation memory rather than the raw engine fact `players-current-age target-player`.

**Disposition:** preserve as a belief cache with freshness and confidence.

## 4.4 `gl-town-safe`

**Classification:** SAFETY BELIEF / DOMAIN INPUT.

It represents a classification of current defensive safety. It should not itself become an objective.

## 4.5 `gl-dark-build`, `gl-need-vills`, `gl-age-loading`

These are best treated as **belief/progression inputs**, not universal strategic authority. Their meaning depends on current economic/progression phase and should be formalized rather than copied as free-floating goals.

---

# 5. Domain authority state

## `gl-attacking`

**Classification:** MILITARY CONTROL STATE.

It directly enters attack initiation and termination. In the donor, attack conditions set it to `YES`, activate TSA, and expand the town-size behavior; deterioration restores prior town-size behavior, retreats, sets `NO`, and disables TSA.

This is not telemetry. It authorizes a different military operating mode.

**Disposition:** preserve as military authority, but subordinate it to the higher objective/commitment model.

## `gl-defend-town`

**Classification:** MILITARY DOMAIN MODE.

It switches defensive behavior and group policy. Preserve, but make its authority relationship explicit.

## `gl-current-group`

**Classification:** TACTICAL DOMAIN SELECTOR.

It selects among `RangedGroup`, `KnightGroup`, and `RaidGroup`. This is an execution selector, not a strategic objective.

## `gl-ranged-style`

**Classification:** TACTICAL POLICY STATE.

`COMBINED`/`SEPARATE` behavior belongs below strategic authority.

---

# 6. Procedural/FSM state

The following are execution-state machines rather than strategic beliefs:

- `gl-find-new-target`
- `gl-raid-status`
- `gl-raid-retreat-type`
- `gl-ranged-group-state`
- `gl-knight-group-state`
- `gl-spear-group-state`
- `gl-raid-group-state`
- `gl-scouting-switch`
- `gl-sheep-scouting`
- `gl-scout-added`
- `gl-scout-stuck`
- `gl-getting-sheep`
- `gl-inside-forest`
- `gl-circle-direcion`
- `gl-deer-walking`
- `gl-dlure`

`gl-raid-status` is especially clear: values such as `CHOOSING-TARGET`, `CHOOSING-WAYPOINT-1`, `MOVING-TO-TARGET`, and `MOVING-TO-WAYPOINT-2` describe an FSM, not strategic intent.

**Disposition:** preserve as domain FSMs; do not allow them to become global strategic authority.

---

# 7. Transaction state: `gl-escrow-state`

**Classification:** TRANSACTION CONTROL STATE.

The donor switches it between `with-escrow` and `without-escrow` and passes it into escrow-aware training operations.

This proves an important architectural separation:

`STRATEGIC DECISION → TRANSACTION MODE → ESCROW-AWARE EXECUTION`

`gl-escrow-state` should not decide what the AI wants. It decides how an already-authorized economic transaction is funded/executed.

**Disposition:** KEEP + FORMALIZE.

This directly supports the AEGIS boundary:

`AUTHORITY → permitted action`  
`ESCROW → funded action`  
`EXECUTOR → performed action`

---

# 8. Derived metrics and evaluations

These are important but should not be promoted into the control plane:

- `gl-attack-efficiency`
- `gl-army-damage-potential`
- `gl-total-military-in-range`
- `gl-total-units-in-range`
- `gl-range-advantage`
- `gl-enemy-attack-size`
- `gl-enemy-group-size`
- `gl-enemies-in-town`
- `gl-enemy-skirms-nearby`
- `gl-enemy-archers`
- `gl-cavalry-in-town`
- `gl-skirm-vills`
- `gl-mangos-nearby`
- `gl-melee-in-range`
- `gl-target-distance`
- `gl-target-hp`
- `gl-ranged-eval`
- `gl-knight-eval`
- `gl-armor-advantage`
- `gl-tracking-range`
- group-range values.

`gl-army-damage-potential` is an evaluation accumulator modified from target-building values, enemy military conditions, and age-up timing. That is derived state, not strategic intent.

**AEGIS rule:** derived state should be recomputable whenever possible and must not acquire authority merely because many rules consume it.

---

# 9. Transient tactical state

Movement/fire/retreat state includes:

- `gl-can-move`
- `gl-can-fire`
- `gl-raid-can-move`
- `gl-raid-can-fire`
- `gl-ranged-retreat`
- `gl-knight-retreat`
- `gl-raid-retreat-type`
- `gl-march-type`

Geometry/target registers include:

- `target-id`, `target-x`, `target-y`
- `point-x`, `point-y`
- nearest TC/tower/castle coordinates
- raid target and waypoint coordinates
- enemy attack coordinates.

These are essential execution state but not strategic authority.

---

# 10. Historical/scratch namespace

## Generic registers

`goal`, `goal1` through `goal8`, `rt`, and `lt` are heavily reused computation registers. Their high write counts do **not** make them strategic; their generic naming and reuse indicate scratch semantics.

**Disposition:** do not transplant as architecture.

## `SPLIT`

Approximately 280 writes and 231 reads. It is a reusable procedural latch used to stage resource allocation and production. Its activity is evidence of procedural reuse, not strategic authority.

**Disposition:** transient latch; replace with domain-local state.

## `UP-FIRST`

A temporary age-up timing/comparison flag that adjusts `gl-army-damage-potential` and transitions through `1/0/-1` states.

**Disposition:** transient/derived policy modifier.

## Identity/debug constants

The donor includes `Shadow`, `Doomsday`, `BruteForce3`, `Promi`, `Illuminati`, `Juggernaut`, `Unknown`, and other identity-like constants. These are not control-plane state.

**Disposition:** quarantine unless a live dependency is proven.

---

# 11. Strategic numbers: effect-plane, not belief-plane

Shadow's strategic-number namespace must be separated from its goal namespace.

Major actuator families include:

### Economic

- `sn-food-gatherer-percentage`
- `sn-wood-gatherer-percentage`
- `sn-gold-gatherer-percentage`
- `sn-stone-gatherer-percentage`

These demonstrate the chain:

`CONTROL STATE → ECONOMIC ACTUATOR`

### Military/exploration

- `sn-maximum-town-size`
- `sn-home-exploration-time`
- `sn-number-explore-groups`
- `sn-total-number-explorers`
- `sn-percent-attack-soldiers`
- `sn-number-attack-groups`
- `sn-allow-civilian-defense`
- `sn-allow-civilian-offense`
- `sn-disable-attack-groups`

### Placement/construction

- `sn-placement-zone-size`
- `sn-placement-fail-delta`
- `sn-dropsite-separation-distance`
- `sn-camp-max-distance`
- `sn-maximum-food-drop-distance`
- `sn-maximum-wood-drop-distance`
- `sn-maximum-stone-drop-distance`
- `sn-preferred-mill-placement`
- `sn-enable-new-building-system`
- `sn-disable-builder-assistance`

These are effect-plane actuators. AEGIS should put an authority layer in front of them rather than confusing them with strategic state.

The donor demonstrates this explicitly: attack mode changes `sn-maximum-town-size`, while economic strategy changes gatherer percentages. This is a causal actuator relationship, not merely a shared variable namespace.

---

# 12. Timers are temporal state

The donor defines timers for attack timing, target switching, boar handling, raid waypoint reevaluation, raid retreat, villager behavior, defense, economy, firing, command delay, failsafe, scouting, reluring, housing, direction changes, and TC dodging.

A timer should be modeled as:

`TEMPORAL GUARD = owner + trigger time + purpose + cancel/reset semantics`

Timers can create hysteresis and serialization, so they are part of the control system, but they are not strategic intent.

**Disposition:** preserve timer primitives; attach semantic ownership and lifecycle.

---

# 13. Reconstructed Shadow state graph

The donor can be reduced to these major causal chains:

### Strategic doctrine

`observations → classification/local conditions → gl-strategy → downstream policy`

### Progression

`gl-strategy → gl-current-build-item → gl-build-progress → gl-progression-pause → resource/escrow gates → executor`

### Military mode

`threat/evaluation → gl-attacking/gl-defend-town → SN actuators → tactical groups`

### Belief

`engine observation → belief goal → policy`

### Tactical FSM

`candidate selection → gl-find-new-target → target geometry → group state → movement/fire → retreat → next state`

### Economic actuator

`strategy/progression → gatherer/placement SNs → engine economic behavior`

### Transaction

`production decision → gl-escrow-state → can-X-with-escrow → up-X → observed result → next pass`

This proves that Shadow is a **distributed state machine**, not a collection of independent rules.

---

# 14. State classification tiers

## Tier A — Core strategic control plane

- `gl-strategy`
- `gl-strategy-type`
- `gl-current-build-item`
- `gl-build-progress`
- `gl-progression-pause`

## Tier B — Belief/control state

- `gl-enemy-strategy`
- `gl-enemy-strategy-type`
- `gl-target-age`
- `gl-town-safe`
- `gl-dark-build`
- `gl-need-vills`
- `gl-age-loading`

## Tier C — Domain authority

- `gl-attacking`
- `gl-defend-town`
- `gl-raid-status`
- `gl-find-new-target`
- `gl-escrow-state`
- `gl-current-group`
- `gl-ranged-style`

## Tier D — Derived/evaluation

Attack efficiency, army damage potential, range advantage, military counts, enemy counts, target HP/distance, and other computed metrics.

## Tier E — Tactical/transient

Group FSMs, movement/fire/retreat gates, scouting state, waypoint state, target coordinates, geometry registers, and reusable local latches.

## Tier F — Engine/effect plane

Most `sn-*` variables, especially gathering, placement, exploration, attack-group, and civilian-policy settings.

## Tier G — Historical/scratch

Generic `goal*` registers, `SPLIT`, `UP-FIRST`, identity/debug constants, disabled branches, compatibility residue, and state with no justified live reader/effect.

---

# 15. Hidden authority conflicts

State importance must be distinguished from state authority.

`gl-strategy` has low writer count and huge fan-out: it is a strategic authority candidate.

`gl-current-build-item` has many writers and readers: it is a scheduler arbitration point.

`gl-progression-pause` acts as a cross-domain lock.

`gl-enemy-strategy` has competing classification paths and therefore needs confidence/freshness/hysteresis.

`gl-town-safe` is a safety classification and needs a single semantic definition.

`SPLIT` has enormous write/read volume but is a reusable latch, not strategy.

Gatherer-percentage SNs have many writers; rule order therefore acts as hidden precedence.

This is precisely the type of hidden arbitration AEGIS should expose.

---

# 16. Rule order is part of state semantics

The effective transition is not simply:

`set-goal X Y`

It is:

`condition → write → jump/disable → suppress competing paths → next pass`

The engine reference documents `up-jump-rule` as a rule-set control-flow primitive. Therefore a state registry must include writer rule identity, ordering, jump destinations, self-disable behavior, timers, and actuator side effects.

A symbol-only graph is insufficient.

---

# 17. Initialization is not persistence

Shadow repeatedly uses:

`(true) → set-goal ... → disable-self`

A value written once may then persist by inertia until another rule mutates it.

Therefore AEGIS must distinguish:

- `INITIAL VALUE`
- `DEFAULT STATE`
- `CURRENT STATE`
- `LAST OBSERVED VALUE`
- `EXPIRED/STALE STATE`

This is particularly important for beliefs such as enemy strategy and target age.

---

# 18. AEGIS typed state model

Recommended semantic types:

### `STRATEGIC_MODE`

Doctrine/objective/priority/reason/confidence/entry/expiry.

### `BELIEF_CLASS`

Classification/confidence/evidence/freshness/invalidation.

### `COMMITMENT_CURSOR`

Objective/requirement/progress/blocker/priority/preemptor/expiry/verification.

### `DOMAIN_MODE`

Active mode/owner/activation/release/executor binding.

### `FSM_STATE`

State/allowed transitions/entry action/exit action/timeout.

### `DERIVED_METRIC`

Formula/inputs/recompute policy/valid horizon/consumers.

### `ENGINE_ACTUATOR`

Engine target/legal range/owner/desired value/current value/reconciliation/reset.

### `TRANSIENT_REGISTER`

Local scratch storage with no strategic authority.

---

# 19. What to preserve, generalize, improve, replace, quarantine

## KEEP

- strategic mode concept
- enemy-strategy classification
- target-age belief cache
- progression cursor
- progression progress
- progression pause/preemption concept
- military attack/defend state
- raid/scouting/group FSMs
- escrow transaction state
- timers
- engine actuator layer

## GENERALIZE

- `gl-current-build-item`
- `gl-build-progress`
- `gl-progression-pause`
- `gl-find-new-target`
- `gl-raid-status`
- tactical FSMs
- target-selection state

## IMPROVE

- writer ownership
- semantic typing
- transition validity
- expiry/invalidation
- belief confidence/freshness
- preemption semantics
- verification predicates
- actuator reconciliation

## REPLACE

- untyped shared namespace as the architecture
- undocumented writer precedence
- strategy encoded solely as a two-value integer mode
- enemy classifications without confidence/freshness
- progression arbitration hidden in rule order
- direct cross-domain writes without authority attribution

## QUARANTINE

- identity/debug constants
- dead/false-only branches
- donor-specific Viking policy state
- compatibility residue
- obsolete scratch registers
- state with no live reader and no verified side effect

---

# 20. AEGIS namespace architecture

```text
ENGINE ABI
   |
   v
STATE STORAGE PRIMITIVES
   |-- goals
   |-- strategic numbers
   |-- timers
   |-- point pairs
   |
   v
AEGIS TYPED STATE REGISTRY
   |-- BELIEF
   |-- STRATEGIC MODE
   |-- OBJECTIVE / COMMITMENT
   |-- DOMAIN MODE
   |-- FSM STATE
   |-- DERIVED METRIC
   |-- ENGINE ACTUATOR
   |-- TRANSIENT REGISTER
   |
   v
AUTHORITY / ARBITRATION
   |
   v
EXECUTORS
   |
   v
OBSERVED STATE CHANGE
```

The critical change is that **storage primitive and semantic type become separate concepts**.

A goal is not inherently strategic.

A strategic number is not inherently policy.

A timer is not inherently tactical.

The semantic owner is determined by the state graph.

---

# 21. State registry schema

Every nontrivial AEGIS state symbol should eventually have:

| Field | Meaning |
|---|---|
| SYMBOL | Engine/storage identifier |
| SEMANTIC TYPE | Belief/control/FSM/metric/actuator/transient |
| DOMAIN | Strategy/economy/military/scouting/construction/etc. |
| OWNER | Unique authoritative subsystem |
| WRITERS | All rule paths that mutate it |
| READERS | All rule paths that consume it |
| INITIAL VALUE | First assigned value |
| DEFAULT | Fallback semantics |
| LIFETIME | Persistent/pass/event/transaction/timer |
| RESET | Explicit reset condition |
| EXPIRY | Time/state expiry |
| PRECEDENCE | Competing-writer arbitration |
| JUMP EFFECT | Control-flow impact |
| ACTUATOR EFFECT | Engine behavior changed |
| EXECUTOR EFFECT | Downstream action changed |
| VERIFICATION | How mutation is confirmed |
| EVIDENCE | DIRECT/COMPOSED/INFERRED/etc. |
| STATUS | CONFIRMED/PROBABLE/etc. |
| TRANSFERABILITY | Byzantine suitability |

---

# 22. Qualification rules

A variable enters the AEGIS control plane only after:

1. definition is established;
2. every active writer is identified;
3. meaningful readers are identified;
4. lifetime and reset semantics are known;
5. authority effect is demonstrated;
6. derivation versus observation is classified;
7. procedural/FSM role is distinguished from strategic role;
8. engine coupling is identified;
9. competing writers and precedence are mapped;
10. completion/verification semantics are identified;
11. historical contamination is checked;
12. Byzantine transferability is established.

---

# 23. Final disposition

**System 02 — State / Namespace is a reconstruction target, not a transplant target.**

The donor's most reusable knowledge is that its strategic state is sparse and high-fanout; progression state acts as a scheduler; pause state acts as hidden preemption; enemy strategy is belief classification; target age is retained observation state; attack/defend variables are domain authority; raid/scouting/group variables are FSMs; escrow state is transaction control; strategic numbers are primarily effect-plane actuators; generic goals are frequently scratch storage; timers are temporal guards; and rule order/jumps are part of effective state semantics.

### AEGIS verdict

**PRESERVE the semantic mechanisms.**  
**GENERALIZE the state machines.**  
**IMPROVE authority, typing, lifetime, confidence, expiry, and verification.**  
**REPLACE the untyped shared namespace as an architectural model.**  
**QUARANTINE historical/scratch state until live dependency is proven.**

The immediate implementation consequence is a **State Registry**, not new behavior. The next forensic step should convert the donor's state topology into machine-readable records and cross-reference every candidate control-plane variable against writers, readers, `up-jump-rule` relationships, timers, strategic-number actuators, and production/construction executors.

That registry becomes the authority boundary from which AEGIS can reconstruct Shadow's useful control plane without reproducing Shadow's namespace debt.
