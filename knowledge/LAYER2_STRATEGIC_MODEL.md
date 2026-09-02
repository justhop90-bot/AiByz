# Layer 2 Strategic Intelligence Model

## Thesis

AoE2 strategy is not a build-order lookup problem. It is a partially observed control problem in which the AI repeatedly chooses actions that transform an uncertain game state.

The strategic state should therefore be modeled as a vector rather than a single strategy label.

`S(t) = Economy + Production + Military + Technology + Map + Position + Information + Timing + Infrastructure + Logistics + Reserves + Threats + Commitments + Opportunities + Confidence`

## Seven primary strategic dimensions

1. **Economy** — income, stockpiles, worker allocation, sustainability, and conversion capacity.
2. **Military** — composition, mass, quality, survivability, reinforcement, and combat capability.
3. **Information** — what is observed, inferred, unknown, stale, or deliberately hidden.
4. **Production** — production buildings, throughput, queues, prerequisites, and replacement capacity.
5. **Position** — map control, defensive geometry, attack vectors, resource access, and local advantage.
6. **Timing** — relative capability windows, arrival times, technology completion, and transition deadlines.
7. **Objective** — what the AI is currently trying to make true about the game.

## Capabilities over unit counts

A unit count is evidence. A capability is a strategic object.

Example:

`10 crossbows` is a count.

`ranged anti-light-infantry capability with sufficient mass to punish an exposed infantry transition` is a capability.

Capabilities connect composition, technology, production, resources, position, and timing. This makes them more useful for planning than isolated counters.

## Strategic objective hierarchy

The hierarchy is deliberately broader than attack/defend:

1. survive;
2. preserve core capability;
3. stabilize economy;
4. secure critical map/resource access;
5. establish military advantage;
6. deny an enemy transition;
7. impose resource/production/timing tax;
8. break enemy production or logistics;
9. convert advantage into irreversible position;
10. end the game.

The same army can therefore be strategically correct or incorrect depending on objective and timing.

## Resource economics

Resources have **state-dependent marginal value**.

The question is not simply:

> How much food, wood, gold, and stone exist?

It is:

> What conversion does each resource enable right now, what does it prevent, and which conversion preserves the greatest future option value?

This implies a resource-demand model:

`objective -> capability demand -> composition -> production demand -> technology demand -> resource demand -> allocation -> conversion`

## Production as a capability pipeline

Production should be reasoned about as:

`objective -> required capability -> composition -> production capacity -> prerequisites -> resource demand -> queue -> reinforcement -> replacement`

A queue is therefore not an isolated economic action. It is a commitment against future strategic demand.

## Technology as investment

A technology should be evaluated by:

- immediate capability gain;
- scaling gain;
- composition dependency;
- timing;
- resource cost;
- opportunity cost;
- counter effect;
- transition effect;
- replacement effect.

The correct question is not "is the technology good?" but "is this conversion superior to the best alternative conversion in this state?"

## Opponent model

Represent a distribution of beliefs rather than one prediction:

- observed composition;
- inferred economy;
- production infrastructure;
- technology state;
- map position;
- current commitment;
- likely objective;
- required next resources;
- likely transition;
- vulnerabilities;
- confidence;
- alternative hypotheses.

A useful opponent model predicts **what the opponent must make true next**, not merely what unit they might build.

## Transition signatures

Strategic transitions leave evidence:

- new production buildings;
- resource allocation changes;
- prerequisite technologies;
- unit-mix changes;
- map movement;
- timing patterns;
- defensive investment;
- market use;
- military mass changes.

A transition engine should learn signatures and estimate:

`P(transition | observed evidence)`

Then ask what counter-transition changes the opponent's expected value.

## Information value

Information is valuable when it changes the expected value of available actions.

Conceptually:

`VOI = E[max(action value | new information)] - max(action value | current information) - acquisition cost`

The model should scout when the expected decision improvement exceeds the opportunity cost of scouting.

## Initiative and tempo

Initiative is the ability to force the next meaningful decision onto the opponent.

Tempo can be created through:

- earlier arrival;
- threat creation;
- denial;
- forced defense;
- production disruption;
- information asymmetry;
- superior transition timing.

A player with initiative can often trade raw efficiency for strategic control.

## Conversion tax

The central AEGIS strategic lens is **conversion tax**.

Every enemy commitment consumes some combination of:

- resources;
- production capacity;
- worker time;
- technology slots;
- map access;
- military attention;
- timing;
- information;
- replacement capacity.

The goal is to select responses that make the enemy spend more to preserve the commitment than the commitment is worth.

Byzantine doctrine will specialize this general principle.

## Failure-state reasoning

Every major commitment should define:

- primary hypothesis;
- expected result;
- failure signature;
- abort condition;
- recovery path;
- fallback objective.

A failed action is also information. The AI should update beliefs rather than simply repeat the same action.

## Strategic evaluation

A conceptual strategic value function is:

`V = military + economy + map + technology + production + information + timing + initiative + reserve - exposure - transition_cost - replacement_cost - economic_damage - uncertainty`

The terms are not fixed constants. Their weights depend on objective and state.

## AEGIS design consequence

The runtime architecture should eventually separate:

`observe -> estimate -> classify -> evaluate -> choose objective -> choose transition -> authorize -> execute -> verify -> learn`

This is intentionally more abstract than historical rule systems. Historical code is evidence for these concepts, not a template to reproduce line-for-line.
