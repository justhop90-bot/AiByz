# HD Forensic Subsystem Workboard

This is the execution order for exhaustive archaeology. A subsystem is not
considered reconstructed when its rules have merely been summarized.

## Required passes per subsystem

### Pass F0 — Inventory

Identify source files/sections, constants, goals, strategic numbers, timers,
rules, actions, loads, comments, and external identifiers.

### Pass F1 — Mechanical reconstruction

Record exact predicates, operators, thresholds, action order, rule enable/disable
behavior, and temporal conditions.

### Pass F2 — State reconstruction

Build every read/write edge. Identify initialization, mutation, clearing,
override, and terminal states.

### Pass F3 — Control reconstruction

Determine feedback loops, hysteresis, rate limiting, event conversion,
reservation protocols, authority conflicts, and cross-subsystem dependencies.

### Pass F4 — Practical game behavior

Translate the mechanism into game-facing behavior: economy, military, map,
production, technology, scouting, attack, retreat, cooperation, and transitions.

### Pass F5 — Human-logic inference

Ask what strategic problem the designer was solving, what assumption was made,
what tradeoff was accepted, and why this implementation was practical in the
available rule language.

### Pass F6 — Counterfactuals

Test removal, delay, failure, enemy inversion, competing state writers, and
resource starvation. Record expected behavioral changes.

### Pass F7 — Cross-validation

Compare against other HD sections, V3, PORPHYRA, replay evidence, and native
engine evidence where applicable.

### Pass F8 — AEGIS abstraction

Extract the general principle independently of the historical implementation.
Specify what should be preserved, generalized, rejected, or marked
engine-specific.

## Major subsystem queue

1. Initialization / state bootstrap
2. Navy / map classification
3. Superiority and military evaluation
4. Enemy strategy classification
5. Strategy selection
6. Resource management
7. Age-up controller
8. Gatherer allocation
9. Production
10. Technology selection
11. Siege logic
12. Villager/building production
13. Military unit selection
14. Attack controller
15. Retreat controller
16. Threat model
17. Target selection
18. Scouting / exploration
19. Position model
20. Farm/fishing economy
21. Cooperation / diplomacy
22. Strategic-number control layer
23. Timer system
24. Human command interface
25. Optional cheats/debug controls
26. Historical/obsolete/experimental code

## Completion rule

A subsystem is complete only when its implementation, state graph, practical
behavior, inferred rationale, failure modes, historical context, evidence,
and AEGIS abstraction are all represented. "Summarized" is not equivalent to
"reconstructed."
