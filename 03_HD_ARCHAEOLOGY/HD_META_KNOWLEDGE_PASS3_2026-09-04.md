# Layer 2 — HD Meta-Knowledge & Strategic Programmer Reconstruction

**Date:** 2026-09-04  
**Status:** RECONSTRUCTION / WORKING KNOWLEDGE  
**Source authority:** verified `AI (HD version).per` + verified Promisory substrate  
**Layer 1 dependency:** machine behavior remains the authority for current-build execution semantics; Layer 1 is frozen at 89% and is not being reopened by this pass.

## 1. Purpose

Pass 1 recovered what the HD program explicitly represents. Pass 2 reconstructed recurring strategic principles. This pass asks the next question:

> **Why would an experienced AoE2 programmer structure a strategy controller this way, what game problems were they actually solving, and what does the implementation reveal about the programmer's mental model of proficient play?**

The target is not a romantic reconstruction of author intent. The target is a falsifiable engineering model that connects:

`GAME PROBLEM -> HUMAN STRATEGIC IDEA -> REPRESENTATION -> RULE-MACHINE ENCODING -> CONTROL EFFECT -> GAME CONSEQUENCE`

The source is treated as verified historical code. The *interpretation* of why it exists remains graded.

## 2. Methodology extension

The existing forensic method remains mandatory. This pass adds three dimensions that must be applied to every major subsystem:

### 2.1 Game-strategy lens

Ask the seven operational questions at the level of the game, not merely the programming language:

- **WHO** matters? Self, ally, enemy, target, flank, pocket, group, worker, building, resource site, or tactical object?
- **WHAT** capability or relationship is changing? Economy, production, technology, military, position, information, infrastructure, logistics, reserves, threat, or initiative?
- **WHEN** is the decision valuable? Age, timing window, transition, attack cycle, resource arrival, technology completion, regroup interval, or recovery window?
- **WHERE** does the decision apply? Home economy, forward position, enemy base, resource site, route, defensive perimeter, water, or local tactical neighborhood?
- **WHY** does the action improve the player's strategic position? What capability is gained, protected, denied, delayed, or converted?
- **WHAT IF** the opponent changes the situation? Which assumption becomes false and which alternative becomes available?
- **WHAT DOES FAILURE TEACH US?** Is the failed action evidence of insufficient capability, stale information, bad position, unavailable infrastructure, or execution failure?

### 2.2 Programmer-mind lens

For every mechanism reconstruct:

`problem -> abstraction -> state -> trigger -> action -> feedback -> workaround -> tradeoff`.

The question is not merely "why did they write this rule?" but "what problem did the programmer need the rule machine to solve that a human player normally solves mentally?"

### 2.3 Architecture lens

Classify each mechanism as primarily:

1. **Strategic model** — game reasoning that should survive a rewrite.
2. **Control mechanism** — state, hysteresis, commitment, recovery, or arbitration.
3. **Engine adaptation** — encoding forced by `.per`/UP semantics or performance.
4. **Historical artifact** — compatibility, experiment, obsolete path, debugging, or accumulated debt.

A mechanism can have more than one label.

## 3. Core reconstructed architecture

The HD source is best understood as a distributed stateful player:

`WORLD`
`  -> OBSERVATION`
`  -> CLASSIFICATION`
`  -> STRATEGIC STATE`
`  -> REQUIREMENT / CAPABILITY NEED`
`  -> RESOURCE + PRODUCTION COMMITMENT`
`  -> ACTION`
`  -> WORLD CHANGE`
`  -> REOBSERVATION`

The historical implementation spreads this loop across goals, strategic numbers, timers, feasibility predicates, search state, DUC state, production flags, and specialized modules.

The most important conceptual separation is:

`observation != belief != requirement != commitment != action`

This is partially explicit in the source and is a required AEGIS architectural generalization.

## 4. The programmer's apparent game model

### 4.1 The game is a changing relationship, not a static state

The density of timers, attack states, reservations, pending operations, resets, enemy classifications, and strategic transitions indicates a model in which the meaning of a fact changes with context.

A stable military count is not necessarily stable military power. A resource pile is not necessarily free. A building is not merely a building; it changes production capacity. A position is not merely geography; it changes the feasible strategy set.

**Reconstruction:** strategy is management of transitions between capability states.

**Evidence:** PROBABLE.

### 4.2 The opponent is modeled through commitments

The source observes age, military population, unit families, buildings, defensive structures, technology and timing, then compresses those observations into enemy state. This is more informative than counting units because an investment constrains the opponent's next options.

**Strategic abstraction:**
`observed commitment -> likely capability -> likely next transition -> response requirement`.

**Evidence:** PROBABLE.

### 4.3 Resources are claims on future actions

Escrow and resource-control behavior indicate that resources can be protected for a future conversion. This makes resource allocation a commitment problem, not a simple affordability check.

**Strategic abstraction:**
`resource stock -> protected capability -> opportunity cost -> release/execute`.

**Evidence:** PROBABLE.

### 4.4 Military strength is contextual capability

Target evaluation and threat logic repeatedly account for more than unit count: distance, HP, range, damage, rate of fire, siege, fortification, population pressure, target identity, timing and remembered force context all matter.

**Strategic abstraction:**
`force value = capability x timing x position x objective relevance`.

The formula is an AEGIS model, not a claim that the historical program used this exact equation.

**Evidence:** historical capability reasoning PROBABLE; formula AEGIS DESIGN.

### 4.5 Retreat is preservation, not necessarily surrender

The attack controller can clear attack permission, enter retreat state, arm timers, reset attack state, and later permit a restart. This strongly suggests a distinction between tactical interruption and strategic abandonment.

**Strategic abstraction:** preserve military capital and optionality when the current engagement is unfavorable.

**Evidence:** PROBABLE.

### 4.6 Time is memory

Timers encode the fact that a decision happened recently and therefore should not be immediately reconsidered. This is practical hysteresis and rate limiting.

**Strategic abstraction:** every important state needs entry, persistence, exit and cooldown conditions.

**Evidence:** implementation CONFIRMED; strategic rationale PROBABLE.

## 5. Four central principles carried forward

### P-A — Stateful player

The AI must remember conclusions, commitments and recent transitions. A stateless reaction engine repeatedly rediscovers the same facts and is vulnerable to oscillation.

`fact -> classification -> state -> commitment -> action -> verification -> update`

### P-B — Resources as future capability commitments

The correct question is not "can I buy this?" but "what future capability becomes unavailable if I buy this now?"

This is the historical seed for AEGIS resource-tax and opportunity-cost reasoning.

### P-C — Capability/candidate evaluation

The correct question is not "what unit counters X?" but "what candidate changes the strategic relationship at acceptable cost and timing?"

Candidate classes include unit, composition, technology, production infrastructure, fortification, route, target, retreat, denial, expansion and economic allocation.

### P-D — Closed-loop control

`DECIDE -> COMMIT -> ATTEMPT -> OBSERVE -> VERIFY -> UPDATE -> CONTINUE / MODIFY / ABORT`.

Command issuance is not proof of success. The world must be observed again.

## 6. New synthesis: strategy is transition management

The four principles combine into a higher-order model:

`current state -> desired capability transition -> commitment -> execution -> opponent response -> counter-transition -> reassessment`.

This explains why the historical source is saturated with:

- pending-state checks;
- timers;
- attack lifecycle state;
- resource reservations;
- enemy classifications;
- reset/restart states;
- map-dependent branches;
- capability substitutions;
- fallback construction;
- search and candidate evaluation.

The programmer appears to be controlling the *rate and direction of change* in the game, not merely selecting actions from a static menu.

**Status:** PROBABLE.

## 7. Engineering tradeoffs visible in the fossil

### Compression versus clarity

High-dimensional observations are compressed into goals/strategic numbers so downstream rules can reuse conclusions. This reduces repeated predicate cost but creates distributed state ownership.

### Reactivity versus stability

Immediate reaction is useful in combat, but unrestricted reaction creates oscillation. Timers and self-disabling behavior trade responsiveness for stability.

### Commitment versus optionality

A strong action can create future capability, but it also consumes resources and production capacity. Reservation and delayed execution preserve optionality until the commitment is justified.

### Search quality versus performance

`general.per` and `scoutcontrol.per` contain explicit candidate-search and path-analysis machinery. Comments acknowledge performance cost. The programmer therefore optimized not only strategic quality but rule-machine execution budget.

### Ideal plan versus recoverable plan

Fallback building branches, pending checks, reset paths and attack restarts show that a plan was not considered complete unless it could survive failure.

## 8. Meta-knowledge: what the source teaches about engineering AoE2 AI

1. **State ownership matters.** A variable read by many controllers but written by many unrelated controllers is strategically important and architecturally dangerous.
2. **Classify expensive facts once.** Reusable enemy/position/threat state is a cache of strategic meaning.
3. **Never confuse request with result.** Build, research, train and movement operations have pending and failure states.
4. **Separate tactical interruption from strategic cancellation.** Retreat, reset and restart states are distinct concepts.
5. **Make resource commitments explicit.** Otherwise production and research silently compete for the same stock.
6. **Rate-limit unstable decisions.** Timers are not decorative; they are control memory.
7. **Use candidate evaluation where local geometry matters.** The scout and water controllers demonstrate generated alternatives and local advantage analysis.
8. **Treat map classification upstream.** Geography can alter economy, production, information and military posture.
9. **Design fallbacks for known failure modes.** A failed placement or blocked action should lead to a defined alternate path.
10. **Preserve abandoned code as evidence.** Historical alternatives reveal constraints and failed approaches.

## 9. What AEGIS should preserve, reject, and generalize

| Historical mechanism | AEGIS treatment |
|---|---|
| Persistent strategic state | **PRESERVE / GENERALIZE** as typed state |
| Enemy classifications | **PRESERVE / GENERALIZE** as beliefs with confidence |
| Resource-control / escrow | **PRESERVE / GENERALIZE** as explicit reservations |
| Timers / hysteresis | **PRESERVE / GENERALIZE** as transition policies |
| Attack / retreat lifecycle | **PRESERVE / GENERALIZE** as state machine |
| Candidate search | **PRESERVE / GENERALIZE** with explicit scoring |
| Feasibility + pending checks | **PRESERVE** at action boundary |
| Distributed goal writers | **REJECT as architecture**; retain as evidence |
| Magic-number state registers | **REJECT as primary design**; replace with typed state |
| Self-disabling as ownership control | **REPLACE** with explicit ownership/authority |
| Repeated giant predicates | **REJECT**; use reusable facts/beliefs |
| Engine-specific jumps/workarounds | **PRESERVE only where required by runtime** |
| Historical dead/experimental branches | **PRESERVE as archaeology, not runtime design** |

## 10. Promotion gates

A reconstructed strategic principle is not implementation-ready until:

1. source evidence is identified;
2. the game problem is stated;
3. the strategic interpretation is graded;
4. counterevidence is recorded;
5. an independent validation path exists;
6. the machine implementation consequence is understood;
7. the AEGIS representation has an explicit owner;
8. the failure signature and recovery path are defined.

## 11. Next research targets

1. Reconstruct the HD writer/reader graph for major state channels.
2. Trace complete economy-to-production-to-military causal chains.
3. Map candidate-search patterns into a reusable AoE2 candidate ontology.
4. Inventory threat classes and the corresponding response transitions.
5. Reconstruct map/position strategy selection.
6. Reconstruct technology as investment and transition state.
7. Build the complete practical coding catalogue below this archaeology layer.

## 12. Boundary

This document does not claim current Definitive Edition runtime behavior beyond Layer-1 evidence. It does not claim optimality of the historical AI. It reconstructs the strategic and engineering knowledge encoded in the verified historical source and identifies what should be generalized for AEGIS.
