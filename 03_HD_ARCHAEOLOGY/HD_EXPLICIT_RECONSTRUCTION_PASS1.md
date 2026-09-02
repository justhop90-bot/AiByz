# HD/2013 Explicit Knowledge Reconstruction — Pass 1

**Date:** 2026-09-02  
**Status:** ACTIVE RESEARCH — derived knowledge only; no runtime implementation authority  
**Source:** `AI (HD version).per`  
**Source SHA-256:** `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`  
**Source bytes:** 1,167,238  
**Source lines:** 36,141  
**Recovered active `defrule` blocks:** 2,429

## 1. Publication and evidence policy

This repository preserves the designer's *knowledge*, not a mirror of proprietary game files. The public record therefore contains derived measurements, schemas, control-event reconstructions, state graphs, short isolated source excerpts, and implementation-neutral explanations. Full game/vendor source, binaries, and complete historical directories remain outside the public repository.

A source excerpt is included only when it materially demonstrates a semantic point. The excerpt is isolated, attributed to its historical source, and is not intended to substitute for the source artifact.

Evidence levels used throughout this pass:

- **CONFIRMED** — directly established by source syntax or an explicit source comment.
- **PROBABLE** — repeated executable pattern with strong semantic consistency.
- **PLAUSIBLE** — useful interpretation requiring independent validation.
- **UNCERTAIN** — evidence is insufficient for promotion.
- **OBSOLETE** — the source explicitly marks the mechanism obsolete/unused.
- **ENGINE-SPECIFIC** — behavior tied to the historical AoE2 rule/UP substrate.
- **DISPROVEN** — contradicted by stronger evidence.

## 2. What Pass 1 reconstructs

Pass 1 answers: **What did the historical program explicitly represent and do?**

It deliberately does not answer the deeper question "why did the designers choose this mechanism?" That causal explanation belongs to Pass 2/3. The atomic research unit is a control event:

`OBSERVATION -> CLASSIFICATION -> STATE WRITE -> AUTHORITY EFFECT -> ACTION -> RESOURCE/PRODUCTION CONSEQUENCE -> TEMPORAL GUARD -> REASSESSMENT`

This is more faithful than treating a line or a defrule as the unit of knowledge because strategic meaning frequently crosses multiple rules.

## 3. Global executable profile

| Measure | Result |
|---|---:|
| Source lines | 36,141 |
| `defrule` blocks | 2,429 |
| Rules containing active action boundary | 2,429 |
| Rules writing goals | 1,048 |
| Rules writing strategic numbers | 642 |
| Active goal-write actions | 2,095 |
| Active strategic-number writes | 1,749 |
| Active `train` actions | 253 |
| Active `research` actions | 323 |
| Active `build` actions | 102 |
| Active `attack-now` actions | 1 |
| Timer-enable actions | 233 |
| Self-disable actions | 356 |

The active/commented distinction is essential. A naive text search counts historical experiments and disabled alternatives as if they were live behavior. Pass 1 therefore records active executable expressions while retaining limited commented evidence for archaeology.

## 4. Explicit strategic state ontology

The source explicitly separates these control concepts:

1. **`strategy-goal`** — strategic mode selection.
2. **`unit-goal`** — preferred military capability/unit family.
3. **`control-goal`** — secondary control, reservation, or response mode.
4. **`position-goal`** — strategic spatial role such as pocket/flank.
5. **`enemy-goal`** — classified enemy strategy/state.
6. **`attack-goal`** — offensive permission/request/state.
7. **`attack-status-goal`** — attack lifecycle state, including regroup/retreat.
8. **`retreat-now-goal`** — explicit retreat policy/state.
9. **`under-attack-goal`** — defensive emergency state.
10. **`forward-threat-goal`** — forward pressure/threat classification.
11. **`enemy-fortifications-goal`** — fortification-related strategic state.
12. **`save-wood-goal`** — spending suppression/reservation state.
13. **`escrow-purpose-goal`** — purpose of resource reservation.
14. **`spread-military-goal`** — military distribution posture.
15. **`restart-attack-goal`** — restoration of offensive state after interruption.

The key architectural observation is that **strategy, capability, reservation, threat, position, and attack lifecycle are separate state dimensions**. AEGIS should preserve that conceptual separation even if its implementation is radically different.

## 5. State-control measurements

| State | Active writes | Condition reads | Rules writing | Rules reading |
|---|---:|---:|---:|---:|
| `strategy-goal` | 328 | 693 | 311 | 610 |
| `unit-goal` | 432 | 1,493 | 409 | 889 |
| `control-goal` | 335 | 305 | 314 | 295 |
| `position-goal` | 3 | 224 | 3 | 191 |
| `enemy-goal` | 13 | 159 | 13 | 115 |
| `attack-goal` | 81 | 32 | 77 | 31 |
| `attack-status-goal` | 19 | 2 | 19 | 2 |
| `retreat-now-goal` | 14 | 13 | 14 | 13 |
| `under-attack-goal` | 7 | 63 | 7 | 44 |
| `forward-threat-goal` | 2 | 23 | 2 | 15 |
| `enemy-fortifications-goal` | 2 | 29 | 2 | 17 |
| `save-wood-goal` | 18 | 40 | 18 | 50 |
| `escrow-purpose-goal` | 24 | 38 | 24 | 35 |
| `spread-military-goal` | 6 | 0 | 6 | 6 |
| `restart-attack-goal` | 3 | 0 | 3 | 3 |

These counts are structural evidence, not authority scores. High writer counts may indicate deliberate distributed control, overloaded registers, or architectural debt. Writer-reader-transition analysis is required before promotion to semantic authority.

## 6. Dominant explicit control channels

### Strategy

`strategy-goal` is written 328 times and read 693 times in the recovered active rules. It is not merely a label. Strategy changes are frequently coupled to unit choice, control state, resource policy, position, and timers.

### Military capability

`unit-goal` is the most heavily used strategic goal in the recovered controller. This demonstrates an explicit separation between *what strategic mode is desired* and *what military capability is intended to implement it*.

### Resource reservation

`sn-resource-control` has 91 active writes and 654 detected condition reads in the structural extraction. The source repeatedly uses it around resource protection, escrow, technology, siege, unit, and naval decisions. This is explicit evidence of a reservation/priority channel rather than merely a resource threshold.

### Temporal control

The active source contains 233 timer-enable actions in this extraction. Timers appear around attack, scouting, defensive response, regrouping, micro, tribute, and reset behavior. Temporal state is therefore part of the controller.

## 7. Explicit control-event exemplars

### Event A — position becomes strategic state

Approximate source location: lines 5252–5262.

The controller tests `position-goal`, writes a positional classification, and in the pocket branch immediately changes `strategy-goal`, `unit-goal`, and `control-goal`, then disables itself.

**Explicit meaning:** spatial classification can directly alter strategy and military capability.  
**Evidence:** CONFIRMED / ENGINE-SPECIFIC.

Short isolated educational excerpt:

```lisp
(up-compare-goal position-goal != pocket)
=>
(set-goal position-goal pocket)
(set-goal strategy-goal pocket-strategy)
(set-goal unit-goal pocket-unit)
(set-goal control-goal 0)
```

This excerpt is an evidence exhibit, not a source replacement.

### Event B — retreat from fortification

Approximate source location: lines 32578–32595.

The controller combines team coordination, game time, siege availability, enemy defensive structures, military level, and population pressure. It then sets retreat state, changes attack status, clears attack permission, arms an attack timer, and raises a reset guard.

**Explicit meaning:** retreat is a coordinated lifecycle transition with temporal hysteresis, not a single strength comparison.  
**Evidence:** CONFIRMED.

Short isolated excerpt:

```lisp
(set-goal retreat-now-goal 1)
(set-goal attack-status-goal retreat)
(set-goal attack-goal 0)
(enable-timer attack-timer 60)
(set-goal reset 1)
```

### Event C — tower response

A separate rule responds to an enemy watch tower while in Feudal Age and without adequate siege. It sets retreat state and attack status, clears attack permission, sets a reset guard, and arms a shorter timer.

**Explicit meaning:** different threat classes can have different recovery windows.  
**Evidence:** CONFIRMED.

### Event D — resource reservation for research

Approximate source location: lines 14765–14785.

One rule sets `sn-resource-control` to `2` when a later research operation should be protected. Another waits for the required state and feasibility and then executes research after releasing escrow.

**Explicit meaning:** resource reservation and operation execution are separate control events.  
**Evidence:** CONFIRMED / ENGINE-SPECIFIC.

Short isolated excerpt:

```lisp
(set-strategic-number sn-resource-control 2)
```

### Event E — map-dependent production

Approximate source location: lines 16006–16065.

Water-map classification changes early dock construction. If the dock cannot be built, alternative infrastructure can be constructed and exploration capacity is adjusted.

**Explicit meaning:** map classification can change production and information-gathering capacity.  
**Evidence:** CONFIRMED.

## 8. Explicit causal chains recovered

### Chain 1 — position -> strategy

`position classification -> strategy-goal -> unit-goal/control-goal -> downstream production/economy`

A high-dimensional spatial fact is compressed into reusable state.

### Chain 2 — enemy observation -> reusable enemy state

`age/building/unit observations -> enemy-goal classification -> downstream strategy and unit rules`

Downstream controllers consume the classification instead of repeatedly reconstructing the entire observation predicate.

### Chain 3 — threat -> controlled interruption

`threat classification -> retreat-now-goal + attack-status-goal + attack-goal reset -> timer -> regroup/reassessment`

The tactical interruption is represented as state rather than automatically as abandonment of the broader strategic mode.

### Chain 4 — reservation -> operation

`need detected -> resource-control reservation -> escrow protection -> feasibility test -> action -> reservation release`

This is a historical implementation of opportunity-cost management.

### Chain 5 — map -> infrastructure -> capability

`map class -> dock/transport/exploration posture -> production -> military/economic capability`

## 9. Explicit production semantics

The source uses feasibility predicates such as `can-build` and `can-research`, pending-object counts, existing-building counts, villager thresholds, age state, and game-time conditions.

This establishes an important machine-facing contract:

**Decision to attempt an action is not equivalent to action completion.**

The program models pending state and availability rather than assuming commands complete synchronously.

## 10. Explicit economic semantics

Gatherer allocation is contextual rather than a single universal constant. The source contains many contextual writes to food, wood, gold, and stone allocation, and strategic decisions can alter those policies.

The explicit pattern is:

`strategic state -> resource policy -> gatherer allocation -> production/technology capacity`

This does not prove mathematical optimality. It does establish that resource allocation was treated as a strategic control variable.

## 11. Explicit offensive-state semantics

The attack controller has multiple dimensions:

- attack permission/state;
- attack lifecycle/regroup status;
- retreat state;
- target identity;
- threat source/type;
- military level;
- siege availability;
- target fortifications;
- population pressure;
- timers;
- reset/restart state.

The historical program therefore contains a small operational state machine around offensive operations.

## 12. Explicit priorities visible in the source

1. Represent important conclusions once and reuse them downstream.
2. Separate strategic mode from military implementation.
3. Treat resources as reservable for future purposes.
4. Treat production/research as asynchronous operations.
5. Use time to prevent oscillation and command spam.
6. Let map/position classification influence strategic posture.
7. Interrupt tactical operations without necessarily abandoning the broader plan.
8. Translate observations into reusable classifications.
9. Couple military, economy, production, and information when changing strategy.
10. Compensate for a weak rule-machine substrate with distributed control registers.

These are explicit design facts. Their deeper competitive rationale is not yet promoted to general strategic law.

## 13. Negative evidence and limits

Pass 1 does **not** prove that every threshold was optimal. It does not prove that a heuristic generalizes to every civilization, map, difficulty, or game phase. It does not infer designer intent merely from a variable name.

The source contains obsolete constants, commented experiments, debugging facilities, difficulty-specific branches, civilization-specific branches, and engine workarounds. They remain classified until cross-validated.

A repeated heuristic is evidence of a design decision; it is not automatically a general law of AoE2.

## 14. Reproducibility

Machine-readable companions:

- `HD_EXPLICIT_CONTROL_EVENTS_PASS1.jsonl` — one derived record per recovered rule.
- `HD_EXPLICIT_STATE_LEDGER_PASS1.json` — aggregate state/control metrics.
- `HD_SNIPPET_CASEBOOK_PASS1.md` — limited source excerpts used as evidence exhibits.
- `HD_PROGRAMMER_MACHINE_BRIDGE_PASS1.md` — mapping between designer abstractions and machine primitives.
- `HD_PASS1_PUBLICATION_MANIFEST.json` — provenance and publication classification.

The historical source is identified by SHA-256 rather than redistributed.

## 15. Pass 1 completion criterion

Pass 1 is complete when an engineer can answer from the public record:

- What major strategic states existed?
- Which variables represented strategy, capability, threat, position, resources, and attack lifecycle?
- How did observations become persistent classifications?
- How did classifications alter actions?
- Where were resources explicitly reserved?
- Where did timers intervene?
- Where did production feasibility/pending state enter decisions?
- Which statements are direct source facts versus interpretation?
- Which material is intentionally unpublished?

The next reconstruction layer is **implicit strategic principles**, followed by **meta-knowledge about why the designers structured the controller this way**.
