# System 03 — Observation / Classification: Forensic Deep Dive of Shadow DC7

**Repository:** `justhop90-bot/AiByz`  
**Branch:** `main`  
**Donor:** `Shadow DC7(1).per`  
**Donor SHA-256:** `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`  
**Donor:** 615,773 bytes; 22,603 physical lines.

## Executive verdict

Shadow's observation system is a distributed classifier network, not a single sensor layer. Raw engine predicates are transformed into aggregates, beliefs, tactical flags, scalar metrics, procedural state, and sometimes immediate actions.

The central forensic conclusion is:

> Shadow has a real observation-to-classification pipeline, but its belief layer is implicit, heterogeneous, and frequently coupled directly to action. AEGIS should preserve the donor's observation repertoire while separating observation, classification, belief persistence, decision authority, and execution.

Canonical reconstruction:

`ENGINE OBSERVATION → NORMALIZATION → CLASSIFICATION → BELIEF/STATE WRITE → DERIVED METRIC → AUTHORITY EFFECT → EXECUTOR`

Shadow often compresses several stages into one rule. That is efficient `.per` engineering but obscures provenance, invalidation, hysteresis, and verification.

## 1. Observation substrate

Shadow observes through five major surfaces:

1. **Temporal:** game time, age time, timers, research status, pending objects, build/train progression.
2. **Spatial:** coordinates, distances, home/target positions, defensive structures, group geometry, scouting radius.
3. **Entities:** unit/building counts, military population, enemy composition, towers/castles/TCs, player validity.
4. **Events/state transitions:** research completion, training/building progression, taunts, age transitions.
5. **Resource/economic state:** resource amounts, escrow, affordability predicates.

The timer vocabulary is particularly significant: attack, defense, scouting, target-switch, retreat, build-delay, firing-delay, command-delay, failsafe, housing, age-cancel, and periodic evaluation timers show that temporal qualification is part of the sensing architecture rather than mere scheduling.

## 2. Direct observation versus derived state

A hard semantic distinction is required.

### DIRECT OBSERVATION

Engine-facing facts such as:

- `unit-type-count`
- `building-type-count`
- `current-age`
- `game-time`
- `research-completed`
- `up-pending-objects`
- resource amounts
- spatial/distance predicates
- player validity

### DERIVED OBSERVATION / METRIC

Computed state such as:

- `gl-enemy-attack-size`
- `gl-skirm-total`
- `gl-enemies-in-town`
- `gl-total-military-in-range`
- `gl-army-damage-potential`
- `gl-attack-efficiency`
- `SUPERIORITY`
- `gl-armor-advantage`

These must never be treated as raw world truth.

## 3. Enemy-strategy classifier

Shadow combines enemy age, buildings, units, military population, score, and timing into classifications such as DRUSH, FLUSH, KRUSH, FC, SCRUSH, and POSSIBLE-KRUSH.

Therefore:

`enemy has X units` = observation

`enemy is probably executing KRUSH` = belief/classification

The second requires provenance, confidence, age, contradiction, and invalidation. The donor contains much of the classification knowledge but does not expose a sufficiently explicit belief lifecycle.

**Disposition:** PRESERVE repertoire; REBUILD the belief interface.

## 4. Threat classifier

Shadow observes cavalry, archers, skirmishers, attack size, towers, castles, TCs, melee pressure, rams, dangerous proximity, and town safety. It then scalarizes consequences.

The donor's threat-cost constants demonstrate an explicit tactical consequence model: ignoring TC fire, allowing knights to roam, ignoring melee, ignoring TCs, and ignoring everything have distinct weights.

This is a major strategic asset. Shadow is not simply detecting threats; it is estimating the relative consequence of failing to respond.

AEGIS should transform this into:

`THREAT OBSERVATION → THREAT CLASS → THREAT SEVERITY → CAPABILITY DEFICIT → RESPONSE CANDIDATES`

rather than allowing threat severity itself to become a production command.

**Disposition:** PRESERVE + IMPROVE.

## 5. Town-safety classifier

`gl-town-safe` is a maintained belief/control variable, not literal world truth. Its validity depends on the observations and rules maintaining it.

AEGIS should attach:

- evidence sources
- classifier identity
- confidence
- last evidence time
- expiry
- contradiction condition
- consumers

**Disposition:** GENERALIZE into formal belief state.

## 6. Tactical state classifiers

`gl-attacking`, `gl-defend-town`, `gl-current-group`, and `gl-raid-*` convert observations into operational modes.

These occupy a higher layer:

`OBSERVATION → TACTICAL CLASSIFICATION → DOMAIN AUTHORITY STATE`

Shadow's initialization and group-switching rules demonstrate that these states are operational control variables rather than passive telemetry.

**Disposition:** Preserve tactical classifications; move strategic authority above them.

## 7. Temporal persistence and hysteresis

Shadow uses timers, age windows, threshold crossings, and delayed reevaluation to prevent purely instantaneous reactions. This is a hidden strength.

However, timer persistence is not equivalent to a formal belief lifecycle.

AEGIS should expose:

`created_at`

`last_evidence_at`

`confidence`

`expiry_at`

`contradiction_condition`

`reassessment_trigger`

**Disposition:** PRESERVE temporal mechanisms; formalize their semantics.

## 8. Research completion as an observation event

Research completion/status is used to update downstream capability state. For example, completed ranged technologies alter stored range/tracking parameters.

This demonstrates:

`ENGINE EVENT → CAPABILITY STATE UPDATE`

The completion event is observation; the changed range is derived capability state.

The same pattern should eventually close the military loop:

`production command → observed unit mutation → verified capability inventory`.

## 9. Escrow is downstream state

`gl-escrow-state` is transaction/control state, not sensor data. It belongs after objective and commitment selection.

Correct boundary:

`OBSERVATION → CLASSIFICATION → OBJECTIVE → COMMITMENT → ESCROW`

not:

`OBSERVATION → ESCROW`.

## 10. Critical coupling problem

Shadow frequently performs classification and action in the same rule. A representative production path can test strategy, superiority, unit counts, age/research state, set a procedural flag, modify a metric, train a unit, alter escrow state, and reset the flag.

This compresses:

`OBSERVE → CLASSIFY → PRIORITIZE → AUTHORIZE → FUND → EXECUTE → UPDATE`

into one or two rules.

AEGIS should recover those semantic stages conceptually without assuming every stage must become a separate `.per` module. **Decomposition for understanding is not necessarily decomposition for implementation.**

## 11. Historical and scratch state

Generic flags, temporary state, legacy constants, and ambiguous variables must not be promoted merely because they are frequently written.

Examples include `SPLIT`, `NEWSCOUTING`, `CROSS`, generic goal slots, identity/debug constants, obsolete/commented duplicates, and cross-domain reused values.

**Disposition:** QUARANTINE until writer/reader/lifetime analysis establishes semantic necessity.

## 12. Recovered architecture

### O0 — Engine evidence

Age, time, counts, research, resources, geometry, player validity, pending objects.

### O1 — Normalized evidence

Canonical counts, distances, capability flags, event predicates.

### C1 — Classification

Enemy strategy, threat class, town safety, target class, tactical situation.

### B1 — Belief state

Persistent hypotheses with confidence and temporal validity.

### A1 — Authority state

Attack/defend, current objective, current group, progression/commitment status.

### E1 — Effect/transaction

Escrow, train/build/research, movement, targeting, construction.

Shadow frequently jumps from O0 directly to A1/E1. AEGIS should retain efficient `.per` paths where appropriate while making the semantic boundary explicit.

## 13. What to preserve

1. Broad engine predicate coverage.
2. Entity-count observation.
3. Spatial geometry.
4. Temporal guards and timers.
5. Enemy-strategy classification repertoire.
6. Threat detection and scalarization.
7. Target acquisition.
8. Tactical safety/attack classifications.
9. Research-completion capability updates.
10. Useful derived combat metrics.
11. Procedural state machines that demonstrably prevent oscillation.

## 14. What to improve

- Type important state as `OBSERVATION | DERIVED | BELIEF | AUTHORITY | TRANSACTION | SCRATCH`.
- Make `SOURCE → RULE → STATE WRITE → CONSUMERS` provenance recoverable.
- Give strategic beliefs confidence rather than binary permanence.
- Add expiry and contradiction semantics.
- Keep threat interpretation separate from production authorization.
- Require observed state mutation before declaring acquired capability.

## 15. Canonical AEGIS observation contract

`RAW ENGINE EVIDENCE → NORMALIZE → CLASSIFY → WRITE BELIEF → CALCULATE DERIVED METRICS → DETECT TRANSITION → UPDATE AUTHORITY STATE → CREATE/UPDATE COMMITMENT → EXECUTOR → OBSERVE RESULT → VERIFY → REASSESS`

Critical invariant:

> No strategic belief is world truth merely because a rule asserted it, and no command is successful capability acquisition without a subsequent observation.

## 16. First application: THREAT → CAPABILITY

`enemy cavalry observed`

→ direct evidence: cavalry count/location  
→ derived evidence: cavalry pressure/severity  
→ belief: cavalry threat active  
→ requirement: anti-cavalry capability required  
→ deficit: current coverage insufficient  
→ candidate responses: spears / monks / walls / relocation / mobility / counterattack / denial / delay  
→ strategic arbitration  
→ Production Authority  
→ Shadow economic commitment/escrow  
→ AIByzBuild executor  
→ observed state mutation  
→ verified coverage  
→ residual deficit  
→ reassessment.

This is the principal bridge from Shadow's sensing/classification knowledge into AEGIS's capability-centered architecture.

## 17. Qualification gate

Every major classifier should pass:

**Q1:** exact engine predicates identified.  
**Q2:** derived variables separated from direct observations.  
**Q3:** classification rules identified.  
**Q4:** persistence/reset behavior identified.  
**Q5:** contradiction/invalidation paths identified.  
**Q6:** temporal behavior identified.  
**Q7:** consumers identified.  
**Q8:** classifier versus executor authority determined.  
**Q9:** generic engine knowledge separated from Vikings-specific policy.  
**Q10:** runtime state mutation/observation required before claiming closed-loop success.

## Final verdict

System 03 establishes that Shadow's strategic intelligence is distributed through a substantial sensing and classification network. Its weakness is that observation, belief, derived metrics, procedural state, authority, and execution are often collapsed into the same rule path.

AEGIS should therefore **extract the observation repertoire, recover the classification graph, type every important state write, preserve useful temporal machinery, promote important classifications into explicit beliefs, move strategic authority above those beliefs, and keep execution and verification downstream.**

The resulting architecture is:

`WORLD → OBSERVE → NORMALIZE → CLASSIFY → BELIEVE → DERIVE → DETECT TRANSITION → OBJECTIVE → CAPABILITY DEFICIT → ARBITRATE → COMMIT → EXECUTE → VERIFY → REASSESS`

System 02 identified the state sinks. System 03 identifies the evidence and classification paths feeding them.

**Next: System 04 — Objective / Strategic Arbitration.**