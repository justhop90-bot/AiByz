# Layer 2 — End-to-End Causal Chains Deep QC Pass 1

**Date:** 2026-09-04  
**Target:** `HD_END_TO_END_CAUSAL_CHAINS_PASS5_2026-09-04.md`  
**Status:** Deep review / correction / expansion backlog  
**Source authority:** verified HD + Promisory source  
**Runtime boundary:** current DE engine semantics remain Layer-1 territory.

## 1. QC verdict

Pass 5 is strategically strong. It correctly moves the archaeology from subsystem inventory to causal chains. It is not yet sufficient as an implementation contract because several causal links are still stated at a higher confidence than the source directly warrants, and several important distinctions are compressed together.

The central idea survives QC:

> **The useful archaeological unit is a change in the game relationship, followed through the controllers that respond to it.**

However, the chain must be made more rigorous by distinguishing:

`OBSERVED FACT -> INTERPRETED STATE -> STRATEGIC REQUIREMENT -> CANDIDATE RESPONSE -> COMMITMENT -> EXECUTION -> OBSERVED OUTCOME -> BELIEF UPDATE`

from:

`historical source evidence -> architectural inference -> AEGIS design extrapolation`.

Those are three different layers and must not be silently merged.

---

# 2. Highest-value corrections

## QC-01 — "Causal chain" must not imply proven causality

**Problem:** A sequence such as cavalry -> threat -> resource demand -> production can be structurally plausible without every intermediate transition being caused by the same rule family.

**Correction:** Use three annotations for every edge:

- `DIRECT` — one source mechanism explicitly connects the states.
- `COMPOSED` — separate mechanisms connect through shared state.
- `INFERRED` — the relationship is reconstructed from repeated behavior rather than directly encoded.

This prevents architectural interpretation from being mistaken for source-level causality.

## QC-02 — Add edge evidence, not only node evidence

A chain can have well-supported nodes but an unsupported arrow between them.

For every edge record:

`source location -> writer -> state written -> downstream reader -> action`

If no direct bridge exists, mark the edge `INFERRED`.

This is the single most important upgrade to Pass 5.

## QC-03 — Separate strategic state from operational state

Attack status, pending construction and tactical target are not equivalent to strategic intent.

Use three temporal scales:

- **Strategic:** minutes / age transitions / broad posture.
- **Operational:** tens of seconds / production / attack preparation / regroup.
- **Tactical:** seconds / target / waypoint / local engagement.

The same event may propagate across all three scales, but the state should not be conflated.

## QC-04 — Add the missing "constraint propagation" layer

The current chain jumps from requirement to action too quickly.

A more precise chain is:

`REQUIREMENT -> CONSTRAINTS -> CANDIDATE SET -> EVALUATION -> COMMITMENT -> AUTHORITY -> ACTION`

Examples of constraints:

- age;
- resource availability;
- reserved resources;
- infrastructure;
- production capacity;
- position;
- enemy threat;
- timing window;
- population/housing;
- information confidence.

This makes the source's feasibility and escrow machinery logically necessary rather than incidental.

## QC-05 — Add "what changed the decision" to every reassessment

Reassessment is currently too generic.

The controller should distinguish:

- new observation;
- contradiction;
- timeout;
- resource state change;
- capability arrival;
- capability loss;
- target invalidation;
- opponent transition;
- failed execution;
- strategic objective completion.

This converts reassessment from a vague loop into a diagnostic mechanism.

---

# 3. Chain I QC — cavalry -> counter-capability

## What is strong

The source clearly contains cavalry-related threat concepts, anti-cavalry state, production control, resource/economic state and attack state.

## What must be corrected

Do not claim that every cavalry sighting automatically propagates into a resource-allocation change. That is an architectural hypothesis unless an exact source bridge is identified.

The stronger formulation is:

`CAVALRY EVIDENCE`
` -> `THREAT / COMPOSITION STATE`
` -> `IF STRATEGIC RESPONSE BRANCH ACTIVATES`
` -> `CAPABILITY REQUIREMENT`
` -> `PRODUCTION / RESOURCE CONSEQUENCE`
` -> `FORCE POSTURE`

The conditional branch matters. AoE2 strategy should not treat every observed unit as worthy of a macro transition.

## Deeper strategic insight

The real trigger is not unit identity but **change in the feasible engagement set**.

A cavalry force matters when it changes which engagements, routes, raids, defenses or economic positions are viable.

That suggests a future AEGIS quantity:

`relationship_delta = feasible_actions_after_threat - feasible_actions_before_threat`

This is conceptual design, not historical source behavior.

## Practical implementation rule

Never implement:

`if cavalry_seen -> make anti-cavalry`

Implement:

`if cavalry_belief crosses response threshold -> generate candidate responses -> evaluate timing/cost -> commit only if relationship improvement justifies transition.`

---

# 4. Chain II QC — Castle transition

## Correction: age-up is a commitment, not merely a research event

The source strongly supports escrow-gated research and contextual gatherer allocation. The deeper interpretation should be expanded to include **economic lock-in**.

During an age-up commitment, some resources cease being economically free because spending them elsewhere can delay the transition.

The useful model is:

`AGE OBJECTIVE`
` -> `RESOURCE TARGET`
` -> `RESERVATION`
` -> `COMPETING SPEND SUPPRESSION`
` -> `FEASIBILITY`
` -> `RESEARCH`
` -> `TRANSITION`
` -> `RESERVATION RELEASE`
` -> `NEW CAPABILITY BUDGET`

## Missing question

What happens when the age-up becomes strategically wrong before completion?

Possible causes:

- emergency defense;
- severe raid;
- opponent timing;
- resource collapse;
- changed strategic objective.

This requires an explicit **commitment-break policy** in AEGIS.

Historical source evidence supports release/reset machinery, but does not by itself prove that every historical commitment was strategically reevaluated in this manner.

---

# 5. Chain III QC — fortification -> siege -> restart

## Important distinction

"Attack suppression" can mean at least four different things:

1. units stop advancing;
2. attack authorization is removed;
3. production changes toward siege;
4. the strategic objective itself is abandoned.

These must not be treated as synonyms.

The historical attack/restart state strongly supports the first three as separate concepts. The fourth requires separate evidence.

## Better state machine

`ATTACK INTENT`
` -> `FORTIFICATION DETECTED`
` -> `DIRECT ASSAULT DEVALUED`
` -> `ATTACK HOLD / REGROUP`
` -> `SIEGE REQUIREMENT`
` -> `SIEGE CANDIDATES`
` -> `RESOURCE / PRODUCTION COMMITMENT`
` -> `SIEGE CAPABILITY`
` -> `ATTACK RE-ELIGIBILITY`
` -> `REASSESS TARGET`
` -> `RESUME / CHANGE PLAN / ABANDON`

This preserves the strategic objective while allowing the tactical method to change.

## Deeper principle

A good strategic controller should preserve **objective identity** through method changes.

`objective != method`.

That distinction is central to AEGIS.

---

# 6. Chain IV QC — map classification

## Strong point

The source contains explicit map/position abstractions and separate water control, building, economy and military systems.

## Missing variable: role

Map geometry is insufficient. Player role changes the meaning of geometry.

At minimum:

`map context + player role + resource topology + exposure + teammate geometry`

should influence strategic posture.

The historical `position-goal` distinction between flank/pocket is especially valuable because it demonstrates that the same map can imply different strategic obligations for different players.

## Practical expansion

Do not model:

`map -> strategy`.

Model:

`map + role + resources + enemy relation + timing -> strategy candidates`.

This avoids deterministic map scripts and better reflects strategic play.

---

# 7. Chain V QC — scouting -> belief -> target -> action

## Major correction

The source clearly supports sophisticated scouting/path candidate generation. It does not automatically prove that the historical programmer explicitly represented a modern probabilistic "belief" object.

Therefore:

- `scouting -> new information` = CONFIRMED;
- `information -> strategic interpretation` = PROBABLE;
- explicit probabilistic belief representation = AEGIS DESIGN.

## Deeper concept: information has decision value

A scout action should be evaluated by whether the information can change a decision.

Potential value components:

`expected decision improvement - scout risk - time cost - execution cost`

Again, this is AEGIS design, not a historical formula.

## Practical consequence

Do not scout merely because a scout is idle. Ask:

> Which unresolved strategic question could this scout answer, and what action would change if the answer were different?

That turns scouting into strategic reconnaissance rather than map painting.

---

# 8. Missing chain — food transition

Pass 5 should add the food-system transition because it exposes the economy as a lifecycle.

Candidate chain:

`FOOD SOURCE AVAILABLE`
` -> `SOURCE QUALITY / SAFETY / DISTANCE`
` -> `WORKER ALLOCATION`
` -> `SOURCE DEPLETION`
` -> `FORECASTED SHORTFALL`
` -> `NEXT FOOD SOURCE`
` -> `INFRASTRUCTURE`
` -> `FARM / HUNT / FISH / TRADE / OTHER TRANSITION`
` -> `RESOURCE CONTINUITY`

This is strategically important because economy failure is often a **transition failure**, not a shortage detected at the instant the stockpile reaches zero.

## AEGIS principle

Predict resource transitions before the current source fails.

Historical gatherer and food-system code provides evidence for contextual allocation; forecasting depletion is an AEGIS generalization until independently demonstrated.

---

# 9. Missing chain — production capacity itself

The current chains treat production as a consequence, but production is also a strategic state variable.

Add:

`CAPABILITY DEMAND`
` -> `PRODUCTION CAPACITY CHECK`
` -> `INFRASTRUCTURE REQUIREMENT`
` -> `BUILDING COMMITMENT`
` -> `QUEUE AUTHORITY`
` -> `UNIT DELIVERY`
` -> `CAPABILITY REALIZED`

This matters because "I want knights" and "I can produce knights at the required rate" are different strategic states.

## New metric

`capability_gap = required_delivery_rate - current_delivery_rate`

This is an AEGIS design abstraction, not a historical formula.

It provides a bridge between force composition and infrastructure planning.

---

# 10. Missing chain — attack feedback

The attack chain should explicitly distinguish:

`attack issued`
vs
`army moved`
vs
`contact achieved`
vs
`damage exchanged`
vs
`target objective changed`
vs
`strategic result achieved`.

A technically successful movement can still be a strategically failed attack.

## Required postcondition levels

### Tactical
Did the units reach/engage the intended local target?

### Operational
Did the attack alter the intended military/position relationship?

### Strategic
Did the attack improve the overall strategic objective enough to justify its cost?

This is a major AEGIS design requirement.

---

# 11. Missing concept — commitment elasticity

Not all commitments should have the same cancellation cost.

Define conceptually:

`commitment_elasticity = how cheaply a plan can be modified without wasting its prior investment`

Examples:

- changing a future gatherer ratio: high elasticity;
- changing a queued unit mix: moderate elasticity;
- cancelling an already-built forward infrastructure plan: low elasticity;
- sacrificing an army after a failed attack: very low elasticity.

This explains why the AI should not treat all decisions with identical reassessment frequency.

Historical source suggests different persistence and reset mechanisms; elasticity is an AEGIS abstraction.

---

# 12. Missing concept — sunk cost must not become strategic justification

Once resources are spent, the controller can become biased toward completing the original plan.

Example:

`forward siege investment -> enemy relocates -> original target loses value`.

The correct question is not "we already spent resources, so continue." It is:

> Is the remaining expected return still greater than the remaining cost?

Historical fallback/reset mechanisms provide evidence that plans can be redirected; the explicit sunk-cost principle is AEGIS strategy design.

---

# 13. Missing concept — optionality as a measurable strategic asset

Resources, production slots, army mobility, scouting capacity and time all preserve or destroy future options.

A candidate should therefore be evaluated not only by immediate gain but by:

`immediate capability gain + future optionality preserved - resource/timing/position tax`.

This is one of the strongest extrapolations from escrow + timers + candidate search + retreat.

It should become a core AEGIS evaluation dimension.

---

# 14. Missing concept — opponent transition prediction

The current chains mostly respond to observed enemy changes. A stronger strategic controller predicts likely next transitions.

Model:

`enemy evidence -> current capability -> committed investment -> constrained future choices -> candidate next transitions -> response preparation`

Example:

`stable cavalry investment + supporting infrastructure -> higher probability of continued cavalry pressure -> prepare anti-cavalry capacity before the full force arrives`.

This must remain an AEGIS extrapolation unless exact predictive logic is found in source.

---

# 15. Missing concept — transition thresholds are multidimensional

A transition should rarely be triggered by one threshold alone.

Example:

`castle commitment = resource readiness + military safety + information confidence + production readiness + strategic value`.

The historical source often uses multiple predicates around strategic transitions. AEGIS should make the dimensions explicit rather than burying them inside one oversized condition.

---

# 16. Missing concept — transition hysteresis should be asymmetric

Entering a strategy and leaving it need not use the same threshold.

Example:

`enter siege posture at fortification threat >= 60`
`leave siege posture only when fortification threat <= 30 or objective changes`.

This prevents flip-flopping.

The numeric example is illustrative only. Actual thresholds must come from evidence or tuning.

Historical timers and self-disabling patterns provide evidence for persistence; asymmetric threshold design is an AEGIS generalization.

---

# 17. Missing concept — strategic state has an invalidation set

Every state should declare what can make it false.

For example:

`enemy-cavalry-belief invalidated by:`
- sufficient contradictory evidence;
- long expiry;
- enemy composition transition;
- strategic context change.

`castle-commitment invalidated by:`
- impossible resource trajectory;
- emergency military crisis;
- opponent transition;
- changed objective.

This is more precise than generic "reassess periodically."

---

# 18. Missing concept — causal chains need conservation laws

A strategic controller should account for what cannot be created for free.

Examples:

- resources consumed by one commitment are unavailable elsewhere;
- production capacity assigned to one unit is unavailable for another;
- army sent forward is less available for home defense;
- scout sent to investigate one region is unavailable elsewhere;
- time spent regrouping delays pressure.

These constraints are the strategic equivalent of conservation laws.

They should be explicit in candidate evaluation.

---

# 19. Missing concept — local success can produce global failure

The source's distributed architecture makes this particularly important.

Examples:

- winning a local fight while delaying age-up;
- building a successful forward structure while starving housing/farms;
- producing the correct counter-unit while missing the attack window;
- scouting safely but learning something too late to matter.

Therefore evaluation must operate at multiple horizons:

`TACTICAL -> OPERATIONAL -> STRATEGIC`.

---

# 20. Practical transition-table schema

The next Pass 6 artifact should use exactly this schema for every major transition:

| Field | Required content |
|---|---|
| Transition ID | Stable identifier |
| Game problem | Human-readable strategic problem |
| Trigger | What changed |
| Evidence | Exact source evidence |
| Preconditions | What must already be true |
| Belief | Current interpretation + confidence |
| Objective | Desired relationship/capability change |
| Constraints | Resource, timing, position, production, information |
| Candidate set | Alternative responses |
| Evaluation | Strategic scoring dimensions |
| Commitment | What becomes reserved/authorized |
| Entry state | State entered |
| Actions | Execution mechanism |
| Tactical postcondition | Immediate proof |
| Operational postcondition | Capability/relationship change |
| Strategic postcondition | Objective result |
| Opponent response | Expected/adaptive response |
| Invalidation | What makes the transition stale |
| Exit condition | Normal completion |
| Failure signature | How failure appears |
| Failure class | Capability / feasibility / execution / position / information / timing / competition / obsolescence |
| Recovery | Alternate candidate / release / retreat / reset |
| Reassessment trigger | What causes reconsideration |
| Evidence grade | CONFIRMED / PROBABLE / PLAUSIBLE / etc. |
| AEGIS status | Preserve / generalize / reject / design |

This should become the canonical transition-record format.

---

# 21. Programmer reconstruction after QC

The strongest updated interpretation is:

> The programmer was building a controller for a game in which decisions compete across time, resources, production capacity, information, and position.

They therefore needed mechanisms for:

- persistence;
- classification;
- commitment;
- reservation;
- feasibility;
- search;
- temporal stabilization;
- tactical execution;
- failure recovery;
- reassessment.

The source does not prove that the programmer conceptualized these mechanisms using modern control-theory vocabulary. The architecture nevertheless exhibits many of the same functional requirements.

The key insight is not "the HD AI was secretly an advanced optimizer." The defensible claim is:

> **The source contains repeated local solutions to the same global problem: maintaining coherent strategic behavior while the game state changes faster than a static rule list can safely encode.**

That is the strongest version of the programmer-mind reconstruction.

---

# 22. New AEGIS architecture derived from QC

The previous architecture:

`OBSERVE -> BELIEVE -> REQUIRE -> CANDIDATES -> EVALUATE -> COMMIT -> ACT -> VERIFY -> RECOVER`

should be expanded to:

`OBSERVE`
` -> CLASSIFY`
` -> BELIEVE`
` -> DETECT TRANSITION`
` -> DEFINE OBJECTIVE`
` -> DERIVE REQUIREMENTS`
` -> PROPAGATE CONSTRAINTS`
` -> GENERATE CANDIDATES`
` -> EVALUATE COST / TIMING / OPTIONALITY / RISK`
` -> COMMIT`
` -> AUTHORIZE`
` -> EXECUTE`
` -> VERIFY TACTICAL POSTCONDITION`
` -> VERIFY OPERATIONAL POSTCONDITION`
` -> VERIFY STRATEGIC POSTCONDITION`
` -> CLASSIFY FAILURE / SUCCESS`
` -> UPDATE BELIEFS`
` -> RELEASE / MODIFY / REINFORCE COMMITMENT`
` -> REASSESS`

This is now the preferred AEGIS strategic control-loop hypothesis.

---

# 23. What should change in Pass 5 itself

Pass 5 should be amended in the eventual canonical version to:

1. mark every causal edge as DIRECT / COMPOSED / INFERRED;
2. add exact source anchors to major edges;
3. separate strategic, operational and tactical state;
4. insert constraints between requirement and candidates;
5. add commitment-break conditions;
6. distinguish tactical, operational and strategic postconditions;
7. add invalidation sets;
8. add opponent-response branches;
9. add optionality and opportunity-cost analysis;
10. add food-transition and production-capacity chains;
11. distinguish historical belief evidence from AEGIS belief design;
12. use the transition-table schema as the basis for Pass 6.

## Final QC verdict

**Pass 5 is promoted as a strong conceptual artifact, but not as a final evidence-grade causal model.**

Its central thesis survives. Its next evolution must become more formal, source-anchored and transition-oriented.

The highest-value next step is no longer another broad essay. It is the **evidence-backed strategic transition table**, built transition by transition and edge by edge.
