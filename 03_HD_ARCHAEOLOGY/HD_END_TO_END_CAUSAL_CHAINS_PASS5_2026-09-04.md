# Layer 2 — HD End-to-End Strategic Causal Chains Pass 5

**Date:** 2026-09-04  
**Status:** RECONSTRUCTION / WORKING KNOWLEDGE  
**Source authority:** verified `AI (HD version).per` + verified Promisory modules  
**Layer-1 boundary:** current DE machine semantics remain authoritative for execution behavior; this pass does not reopen Layer 1.

## 1. Purpose

Pass 4 reconstructed state channels and their apparent writer/reader relationships. Pass 5 follows the state across subsystem boundaries.

The objective is to recover the programmer's *game-level causal reasoning*:

`OBSERVATION -> INTERPRETATION -> STRATEGIC REQUIREMENT -> RESOURCE CONSEQUENCE -> PRODUCTION / INFRASTRUCTURE -> MILITARY CAPABILITY -> POSITION / ACTION -> OPPONENT RESPONSE -> REASSESSMENT`

This is the point at which the historical code becomes most useful as strategic knowledge rather than syntax knowledge.

## 2. Chain I — enemy cavalry -> counter-capability -> force posture

### Source ingredients

- HD enemy/threat classification includes cavalry-related threat state.
- `anti-cavalry-threat-goal` exists as strategic state.
- `units.per` controls production through strategic conditions and train flags.
- Technology, resource and production state feed the unit system.
- Attack state is separate from unit selection.

### Reconstructed chain

`ENEMY CAVALRY OBSERVED`
` -> cavalry threat classification`
` -> anti-cavalry requirement rises`
` -> resource demand changes`
` -> production authorization changes`
` -> counter-capability enters force composition`
` -> attack/defense posture changes`
` -> new military relationship`
` -> enemy composition reobserved`

### Game meaning

The programmer is not solving "cavalry exists." The real problem is that cavalry changes the set of viable engagements. The response therefore propagates through economy and production before it reaches combat.

### Important counterfactual

If cavalry detection directly changed only a unit queue, the AI would still be vulnerable to infrastructure, resource, timing and positional constraints. The historical coupling to strategic/unit/resource state suggests a broader control problem.

### AEGIS generalization

`threat -> required capability -> candidate responses -> resource tax -> timing -> force posture`

Do not hard-code one universal counter. Candidate responses can include counter-units, siege, fortification, mobility, avoidance, denial, or attack elsewhere.

**Evidence:** source mechanics CONFIRMED; end-to-end strategic interpretation PROBABLE.

## 3. Chain II — Castle Age objective -> economy -> escrow -> transition

### Source ingredients

- `escrow.per` begins with release/reset behavior.
- `escrow-flag` branches gate research.
- Castle Age research uses `can-research-with-escrow`.
- Current-age state is updated after the age transition.
- `gatherers.per` changes resource allocation according to age/technology/resource context.
- Production and building systems consume the changed capability state.

### Reconstructed chain

`CASTLE AGE IS STRATEGICALLY DESIRED`
` -> food/gold/other resource demand increases`
` -> gatherer allocation shifts`
` -> resources accumulate under reservation/escrow`
` -> research feasibility checked`
` -> Castle Age research committed`
` -> age state changes`
` -> escrow released/reallocated`
` -> new production/building/technology options become relevant`
` -> economy is rebalanced for the new state`

### Game meaning

Age-up is not a button press. It is a resource-flow transition that temporarily changes what the economy is allowed to spend on.

### Programmer insight

Escrow exists because the stockpile is contested by multiple future actions. The programmer therefore had to preserve a desired transition against competing local spending.

### AEGIS generalization

Treat age transitions as commitments with:

`required resources + deadline + competing uses + expected capability delta + release policy + failure/recovery`

**Evidence:** escrow/research mechanics CONFIRMED; strategic investment interpretation PROBABLE.

## 4. Chain III — fortification -> attack suppression -> siege transition -> restart

### Source ingredients

- `enemy-fortifications-goal` exists.
- Attack state includes attack-goal/status and restart state.
- Siege capability is represented in unit/production logic.
- Resource reservation supports siege and other priority spending.
- Timers and regroup/reset logic appear in attack control.

### Reconstructed chain

`DEFENSIVE STRUCTURE OBSERVED`
` -> attack relationship changes`
` -> direct attack becomes lower-value / suspended`
` -> siege capability requirement rises`
` -> resource/production commitment changes`
` -> siege infrastructure/units become available`
` -> attack lifecycle waits or regroups`
` -> capability threshold reached`
` -> attack restart becomes eligible`
` -> fortification relationship is tested again`

### Game meaning

The AI is not simply "afraid of castles." It is detecting that the current force-to-target relationship has changed and that the correct response is a capability transition.

### Strategic principle

`counter-mechanism -> counter-capability -> resumed initiative`

This is the same pattern that appears in many AoE2 interactions: the right response to a defense is often not more of the same army, but a transition that changes the relationship.

### AEGIS generalization

Represent attack suppression as a commitment-preserving state, not a panic response. A suppressed attack retains its objective while changing the required capability and timing.

**Evidence:** fortification/attack state CONFIRMED; causal interpretation PROBABLE.

## 5. Chain IV — map classification -> economic posture -> infrastructure -> military posture

### Source ingredients

- `nr-map-goal` explicitly identifies map contexts where economy/defense should adapt.
- `position-goal` distinguishes flank/pocket roles.
- Water-control is a distinct subsystem.
- Building and gatherer logic respond to map/resource conditions.
- Attack and production behavior depend on map/position context.

### Reconstructed chain

`MAP / ROLE CLASSIFIED`
` -> expected resource access / exposure changes`
` -> economic posture changes`
` -> infrastructure requirements change`
` -> production priorities change`
` -> military posture changes`
` -> scouting / attack routes change`
` -> observed map control changes`
` -> posture is reassessed`

### Game meaning

The map is an upstream strategic variable. It does not merely affect where units walk; it changes the expected economics, defensive requirements, military timing and viable strategy family.

### Programmer insight

This is a strong reason to classify map context early. If map information remains trapped inside tactical code, every downstream subsystem must rediscover the same strategic fact.

### AEGIS generalization

`map_context` should be a typed strategic belief consumed by economy, production, military, scouting and infrastructure.

**Evidence:** explicit map/position state CONFIRMED; cross-system causal interpretation PROBABLE.

## 6. Chain V — scouting -> belief -> target -> tactical action -> feedback

### Source ingredients

`scoutcontrol.per` contains explicit comments describing:

- group creation;
- path safety analysis;
- quarterstep analysis around obstacles and threats;
- pivot-point generation;
- candidate points at rotated angles;
- interpolation toward candidate points;
- waypoint selection;
- action selection;
- a default move action when no other condition dominates.

### Reconstructed chain

`INFORMATION GAP`
` -> scout objective / target region`
` -> path candidates generated`
` -> safety / threat evaluation`
` -> waypoint selected`
` -> scout action executed`
` -> new world information obtained`
` -> enemy / map belief updated`
` -> strategic or tactical target changes`
` -> next information gap identified`

### Game meaning

Scouting is treated as a decision-support activity. The path itself is a candidate-selection problem because information has value only if the scout survives and reaches a useful observation point.

### Performance lesson

The source explicitly acknowledges that more complete path analysis has performance cost. Therefore information quality has an execution cost even before considering in-game opportunity cost.

### AEGIS generalization

Choose scouting actions by expected decision value:

`information gained * probability of changing a decision - scouting risk - time cost - attention cost`

The equation is AEGIS design, not a historical formula.

**Evidence:** tactical search mechanics CONFIRMED; decision-value interpretation PROBABLE.

## 7. Cross-chain pattern — the programmer's recurring move

Across the five chains, the same transformation appears:

`RAW GAME FACT`
` -> `CONTEXTUAL INTERPRETATION`
` -> `STRATEGIC STATE`
` -> `RESOURCE / PRODUCTION CONSEQUENCE`
` -> `CAPABILITY CHANGE`
` -> `TACTICAL CONSEQUENCE`
` -> `NEW OBSERVATION`

The programmer repeatedly turns a local observation into a state transition that can affect distant subsystems.

This is why the source should not be reconstructed as a flat collection of rules. The strategic unit is the causal chain.

## 8. Three levels of programmer reasoning

### Level 1 — tactical

"What object should this unit act on?"

Examples: target selection, waypoint, retreat point, local enemy strength.

### Level 2 — operational

"What capability or production state must change to support the tactical objective?"

Examples: train flags, siege production, resource allocation, building prerequisites.

### Level 3 — strategic

"Which transition changes the overall relationship with the opponent or the map?"

Examples: age transition, attack suspension/restart, enemy classification, map posture, resource reservation.

### Reconstruction

The historical source contains all three levels. The architectural weakness is that they are often represented in the same primitive namespace (goals, flags, SNs, timers), making the hierarchy difficult to see from syntax alone.

**Evidence:** PROBABLE.

## 9. Opportunity cost is the hidden connector

The causal chains repeatedly imply competition:

- gold can fund age-up, technology, military or siege;
- wood can fund farms, houses, production, defense or infrastructure;
- production capacity can train one capability instead of another;
- military units can attack, defend, scout or escort;
- time spent regrouping is time not spent pressuring;
- scouting risk can trade safety for information.

Escrow, save-wood state, production flags, timers and attack-state controls are therefore different implementations of the same strategic problem:

> **Every action consumes scarce future optionality.**

This sentence is an AEGIS synthesis, not a historical quotation.

## 10. Failure becomes a diagnostic signal

The chains also imply a useful distinction between action failure and strategic failure.

### Example: siege plan fails

Possible explanations:

1. siege resource commitment was not funded;
2. infrastructure was unavailable;
3. production was blocked;
4. enemy pressure changed the required capability;
5. target became irrelevant;
6. position became unsafe;
7. information was stale.

A robust controller must not respond identically to all seven.

### Historical evidence

Fallback building logic, placement reset, attack restart, retreat, search alternatives and escrow release show that the source contains multiple forms of recovery.

**Evidence:** recovery mechanisms CONFIRMED; diagnostic taxonomy AEGIS GENERALIZATION.

## 11. The programmer's likely optimization target

The source appears to optimize three scarce budgets simultaneously:

### Game budget

Resources, villagers, production, army, map control and time.

### Information budget

What the AI has seen, remembered, and can afford to inspect again.

### Rule-engine budget

Rule evaluations, search work, control-flow jumps and tactical computation.

The explicit performance comments in scouting and search machinery make the third budget especially important. The programmer was not merely optimizing the game plan; they were optimizing a strategy program executing inside a constrained rule machine.

**Evidence:** performance-aware implementation CONFIRMED; three-budget synthesis PROBABLE.

## 12. AEGIS decision contract extracted from the chains

Every strategic decision should be expressible as:

`CURRENT RELATIONSHIP`
` + `BELIEF / UNCERTAINTY`
` + `OBJECTIVE`
` + `AVAILABLE CAPABILITIES`
` + `RESOURCE / TIME CONSTRAINTS`
` + `POSITION`
` + `OPPONENT TRANSITION`
` -> `CANDIDATES`
` -> `EVALUATION`
` -> `COMMITMENT`
` -> `AUTHORIZED ACTION`
` -> `POSTCONDITION`
` -> `FAILURE CLASSIFICATION`
` -> `RECOVERY / REASSESSMENT`

This is the most useful generalization of the historical architecture so far.

## 13. What not to copy

The causal structure should be preserved, but several historical implementation patterns should not become AEGIS architecture by default:

- distributed writers for the same strategic variable;
- magic-number scratch registers without semantic typing;
- hidden search state;
- oversized predicates;
- self-disabling as the primary ownership mechanism;
- assumptions that issuing an action proves success;
- timers whose purpose is not documented;
- tactical rules that silently override strategic commitments.

These are implementation artifacts or constraints, not necessarily strategic principles.

## 14. What should be inherited

The following should survive the rewrite:

1. classify before reacting;
2. persist important strategic interpretations;
3. reserve resources for high-value transitions;
4. treat production as capability generation;
5. evaluate candidates rather than memorizing one response;
6. treat attack as a lifecycle;
7. use retreat to preserve future capability;
8. use timers to stabilize transitions;
9. model map and position upstream;
10. verify world-state postconditions;
11. recover from known failure modes;
12. reassess when the opponent changes the relationship.

## 15. Promotion status

### CONFIRMED

- The source contains strategic goals, threat state, resource/escrow state, production state, attack state, timers, search state and specialized tactical controllers.
- `escrow.per` gates research and explicitly releases/reset escrow.
- `gatherers.per` changes resource allocation contextually.
- `units.per` uses production flags/goals to control training.
- `general.per`, `scoutcontrol.per` and `watercontrol.per` contain explicit search/candidate/tactical machinery.
- Building code contains fallback/rebuild behavior.

### PROBABLE

- These mechanisms form a distributed closed-loop strategic controller.
- The programmer modeled capability transitions rather than isolated actions.
- Resource reservation, timers and attack state are compensating for persistent competition between decisions.
- The historical controller manages game-state transitions under rule-engine constraints.

### AEGIS DESIGN

- typed beliefs;
- explicit requirement/candidate layers;
- explicit resource reservation ledger;
- explicit authority and commitment ownership;
- postcondition verification;
- failure taxonomy and recovery policy;
- candidate scoring with opportunity cost and uncertainty.

## 16. Next research target

The next pass should build the **strategic transition table**:

`TRIGGER -> PRECONDITIONS -> STATE ENTRY -> RESOURCE EFFECT -> CAPABILITY CHANGE -> OPPONENT RESPONSE -> EXIT CONDITIONS -> FAILURE -> RECOVERY`

Prioritize the transitions that cross the most subsystems:

1. Dark -> Feudal;
2. Feudal pressure -> Castle transition;
3. Castle -> Imperial;
4. enemy composition change -> counter-composition;
5. attack -> retreat -> regroup -> restart;
6. fortification -> siege transition;
7. map/role classification -> economic/military posture;
8. food-source exhaustion -> renewable food transition.

These transitions should become the bridge from HD archaeology to the eventual AEGIS strategic ontology.
