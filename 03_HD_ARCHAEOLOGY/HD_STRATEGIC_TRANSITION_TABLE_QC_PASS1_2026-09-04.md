# Layer 2 — Strategic Transition Table QC — Pass 1

**Date:** 2026-09-04  
**Status:** QUALITY CONTROL / CORRECTION PASS  
**Target:** `HD_STRATEGIC_TRANSITION_TABLE_PASS6_2026-09-04.md`  
**Primary evidence:** verified HD/Promisory source  
**Runtime authority:** frozen Layer-1 machine evidence for current AoE2DE execution semantics

## 1. QC verdict

Pass 6 is conceptually strong and substantially better than Pass 5, but it was **not yet evidence-grade in every field**. The largest problem is not the transition architecture; it is occasional promotion of an AEGIS interpretation into a historical claim by proximity.

**Disposition: ACCEPT WITH CORRECTIONS.**

No transition is rejected outright. Several causal edges and postconditions must be downgraded or made explicitly conditional.

## 2. Major findings

### QC-01 — ST-01 Dark → Feudal evidence is overstated

**Finding:** `escrow.per` directly demonstrates controlled Castle/Imperial research transitions, but that alone does not prove the same exact mechanism is used for Dark → Feudal.

**Correction:** classify the generic age-transition architecture as **COMPOSED / ANALOGICAL**, unless an exact Feudal rule is cited. Do not write that the source directly establishes the Dark → Feudal transition through the same escrow rule.

**Practical rule:** every age transition must cite its actual age-specific writer/reader chain.

### QC-02 — ST-01 objective is AEGIS strategy, not recovered historical doctrine

The statement that age advancement is a resource conversion whose future value must exceed opportunity cost is strategically sound, but the source does not expose a universal utility comparison.

**Correction:** retain it as **INFERRED**, and retain the explicit AEGIS evaluation formula as **AEGIS-GENERALIZATION**.

### QC-03 — ST-02 Feudal → Castle is plausible but its trigger is not a source trigger

The phrase “Feudal military/economic state reaches a point where additional Feudal investment competes with Castle timing” is an excellent strategic model but is not demonstrated as one explicit source transition predicate.

**Correction:** label the trigger **INFERRED FROM COMPOSED STATE**, not DIRECT/CONFIRMED. Distinguish “the code has both mechanisms” from “the programmer explicitly compares their marginal values.”

### QC-04 — ST-03 repeats the same age-transition problem

Castle → Imperial is directly represented as a controlled research transition, but “planned state conversion” and “post-Imperial capability relevance” are interpretations.

**Correction:** split evidence into:
- DIRECT: Imperial research authorization/state update exists;
- COMPOSED: resource/gatherer/military systems interact with age;
- INFERRED: designer treated Imperial timing as a strategic conversion decision.

### QC-05 — ST-04 counter-composition contains a category error risk

The historical source clearly contains threat classification and context-sensitive response machinery. It does **not** establish that every listed response—mobility, fortification, route change, infrastructure attack, technology, retreat—is selected by one unified counter-composition engine.

**Correction:** describe these as the **AEGIS candidate response space**, while separately listing historically evidenced response families. Do not collapse distributed rule families into one historical optimizer.

### QC-06 — ST-04 “opponent transition” must remain a hypothesis

Buildings, age, technology, military population, and timing can constrain future actions. That supports transition prediction as a strategic inference. It does not prove the historical programmer explicitly modeled opponent future transition as a predictive object.

**Correction:** retain as **INFERRED**, with a falsifier: if high-impact enemy classifications are purely present-state reactive, prediction should not be promoted.

### QC-07 — ST-05 tactical postcondition is too strong

Changing `retreat-now-goal`, `attack-status-goal`, `attack-goal`, timer, and reset state proves a **controller-state transition**. It does not by itself prove that the units actually disengaged.

**Correction:**
- Tactical command/state request: DIRECT;
- physical disengagement: requires world-state evidence;
- operational retreat lifecycle: DIRECT/COMPOSED depending on exact writer chain.

This follows the project-wide rule: **command issuance ≠ world-state postcondition**.

### QC-08 — ST-05 “preserve military capital” is strategic interpretation

The behavior is consistent with preservation of future capability, but the source does not necessarily state that rationale.

**Correction:** evidence grade INFERRED, not DIRECT.

### QC-09 — ST-06 siege transition is not fully direct

Fortification-aware attack suppression is directly supported. The full causal transition `fortification → siege production` is distributed and therefore **COMPOSED** unless an exact rule chain connects the two.

**Correction:** separate:
1. detect/represent fortification — DIRECT;
2. suppress/delay attack — DIRECT;
3. select/build siege — source-dependent and must be separately cited;
4. “change capability rather than commit harder” — INFERRED/AEGIS-GENERALIZATION.

### QC-10 — ST-06 failure signature is a proposed feedback criterion

“Repeated attacks produce losses without changing the defensive relationship” is an excellent AEGIS failure signature, but the historical source does not necessarily compute this exact longitudinal statistic.

**Correction:** mark it AEGIS-GENERALIZATION unless an explicit historical loop is found.

### QC-11 — ST-07 map role is strongest of the eight, but transient-vs-strategic classification needs proof

The casebook directly demonstrates `position-goal` driving strategy/unit/control state. However, the statement that the programmer explicitly distinguished strategic position from transient tactical location needs additional writer/reader evidence.

**Correction:** DIRECT for position-goal → strategy/unit/control coupling; INFERRED for the ontology “relational strategic state rather than coordinate.”

### QC-12 — ST-08 food exhaustion → renewable food is under-evidenced

The existence of boar hunting, farm goals, save-wood logic, and gatherer allocation does not automatically prove a single causal depletion transition.

**Correction:** downgrade the transition trigger and causal edge to **COMPOSED / INFERRED** until the exact depletion detector → farm authorization → gatherer redistribution chain is cited.

Also distinguish **finite-source depletion** from **food-source substitution**. The historical AI may react to several food conditions without explicitly forecasting depletion as a trajectory.

## 3. Cross-cutting QC findings

### QC-13 — Preconditions are partly normative

Many preconditions use phrases such as “military state can survive,” “opportunity cost is acceptable,” or “expected capability remains relevant.” These are excellent AEGIS constraints but are not all historical predicates.

**Required convention:** prefix fields with one of:
- `HISTORICAL:` directly source-supported;
- `RECONSTRUCTED:` strong inference from distributed source;
- `AEGIS:` design requirement/generalization.

### QC-14 — Candidate sets mix historical actions with AEGIS actions

Candidate lists currently read as though the historical AI evaluated every listed candidate in one common tournament. That is not established.

**Correction:** split candidate sets into:
- `Historical candidate/action families evidenced`;
- `AEGIS generalized candidate set`.

### QC-15 — Evaluation formulas are design proposals

Expressions such as:
`capability value = combat power × timing relevance × objective relevance`
and
`objective progress / total strategic commitment cost`
are useful AEGIS mathematics, not recovered formulas from HD.

They must never appear under a historical “evaluation” heading without an explicit `AEGIS-GENERALIZATION` label.

### QC-16 — Postconditions require three distinct evidentiary layers

Every transition should distinguish:
1. **command/control postcondition** — goals/state/command changed;
2. **world-state postcondition** — game object/resource/technology/unit state changed;
3. **strategic postcondition** — intended capability or objective relationship improved.

Only the first can normally be established from a rule's action sequence alone.

### QC-17 — Opponent response is not historical unless explicitly modeled

Opponent responses are useful for AEGIS simulation and evaluation, but a listed response must not be read as evidence that the HD controller predicted it.

Use `EXPECTED AEGIS RESPONSE SPACE` unless source evidence demonstrates predictive branching.

### QC-18 — Invalidation sets are an AEGIS strengthening

The invalidation lists are excellent and should remain, but they should be marked as AEGIS architecture unless an exact historical reset/reclassification condition supports them.

### QC-19 — Transition entry and exit need asymmetric hysteresis

The table currently identifies timers/cooldowns but should explicitly record that entry and exit thresholds need not be identical.

AEGIS should support:
`enter when E > T_enter; remain while E > T_exit; exit only when E < T_exit`, with `T_enter != T_exit` where appropriate.

This is a design generalization, not a claim about a specific HD threshold.

### QC-20 — Transition ownership is missing

Every transition should eventually identify:
- observation owner;
- belief owner;
- objective owner;
- commitment owner;
- authorization owner;
- execution owner;
- verification owner;
- recovery owner.

This directly addresses the distributed-writer fragility observed in the historical architecture.

## 4. New practical requirement: evidence-edge ledger

Pass 6 should be followed by an edge ledger. Every arrow in a transition must have a row:

`Edge ID | From | To | Source module | Approx source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status`

Example:

`ST05-E03 | retreat-state request | physical disengagement | HD attack/retreat rules | TBD | world-state behavior | UNCERTAIN | units may remain in contact | observe unit positions after command | VERIFY`

This prevents the common failure mode in which a true first-order source fact silently acquires an unsupported second- or third-order causal meaning.

## 5. New practical requirement: transition conservation laws

For each transition, track what cannot be created for free:

- resources;
- villager time;
- production capacity;
- military mass;
- map access;
- information quality;
- timing;
- strategic optionality.

A transition that appears to improve every dimension simultaneously should trigger a QC warning unless the source/game mechanics identify the conversion that paid for the improvement.

## 6. New practical requirement: local success vs global success

Every transition must be tested at three levels:

`LOCAL: did the action execute?`

`OPERATIONAL: did the capability/process complete?`

`GLOBAL: did the strategic relationship improve?`

Examples:
- Castle research completed ≠ Castle transition succeeded.
- Siege unit trained ≠ fortification problem solved.
- Retreat command issued ≠ army preserved.
- Farm built ≠ food transition stabilized.
- Position classified ≠ chosen posture is strategically correct.

This should become a permanent AEGIS QC invariant.

## 7. Revised evidence policy

A transition is **evidence-grade** only when:

1. every historical edge has a source anchor;
2. every inferred edge names its inference basis;
3. every AEGIS addition is explicitly labeled;
4. command postconditions are not confused with world-state postconditions;
5. opponent response is separated from historical prediction;
6. candidate sets distinguish historical behavior from generalized action space;
7. entry/exit/invalidation conditions are explicit;
8. ownership and authority are identifiable;
9. failure signatures are observable rather than purely conceptual;
10. a falsifier exists for every major inference.

## 8. QC conclusion

Pass 6 is **valuable and structurally correct**, but its greatest remaining risk is epistemic compression: too many true observations, strong interpretations, and AEGIS design ideas are packed into the same transition record.

The correction is not to simplify the model. It is to add another layer of provenance.

The correct next artifact is therefore an **Evidence-Edge Ledger / Pass 7**, built from exact source anchors for each transition.

**Recommendation:** do not merge the Layer-2 PR yet. The transition model should pass the edge-ledger audit first.
