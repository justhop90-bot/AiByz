# AEGIS Authoritative Bot Blueprint — 2026-09-09

**Status:** AUTHORITATIVE CONSTRUCTION BLUEPRINT
**Authority:** This document governs the construction order and completeness criteria for the final AEGIS Byzantine bot. It supersedes earlier informal vertical-slice lists.
**Runtime:** Pure `.per`; no XS; Promisory is reference/source material, never a runtime dependency.

## 1. Construction principle

AEGIS is constructed as permanent vertical slices. A slice is not a disposable prototype. Each slice must connect the relevant path from observation/state through policy, authorization, engine execution, verification, recovery, and strategic reassessment.

The stock AI(HD)+Promisory corpus is the adversarial reference model: whenever this blueprint appears to omit a capability that the stock system demonstrably possesses, the omission is a defect to be investigated rather than assumed away.

## 2. Complete construction domains

### A. Engine and state substrate
1. Engine ABI / primitive qualification
2. Initialization and civilization startup
3. Persistent state, timers, flags, groups and scratch-state discipline
4. Civilization-state reconciliation
5. Spatial/entity/world model

### B. Civilization operating substrate
6. Villager production and civilian-population control
7. Housing / population-cap continuity
8. Idle-villager detection and recovery
9. Resource-site discovery and serviceability
10. Dropsites and economic logistics
11. Worker roles and discrete allocation
12. Food-source portfolio and transitions
13. Hunting / boar / deer handling
14. Farming and food fallback transitions
15. Wood economy
16. Gold economy
17. Stone economy
18. Resource income measurement/model update
19. Economic demand vectors
20. Escrow / resource reservation
21. Economic arbitration / opportunity cost
22. Allocation hysteresis / anti-oscillation
23. Civilian production queues
24. Construction placement
25. Builder allocation
26. Foundation/progress/completion tracking
27. Construction failure/retry/rebuild
28. Production-building and queue maintenance

### C. Technology and capability
29. Age advancement
30. Research prerequisites/affordability
31. Research queue and reservation
32. Economic technology policy
33. Military technology policy
34. Civilization-specific technologies
35. Capability-state reconciliation

### D. Information and world understanding
36. Scout production/continuity
37. Exploration and map discovery
38. Enemy-player identification
39. Resource/infrastructure discovery
40. Military observation
41. Information freshness / staleness
42. Threat classification
43. Military-strength estimation
44. Spatial threat/path analysis
45. Opponent model
46. Belief update and transition detection

### E. Military operating system
47. Military production requests
48. Force composition
49. Army formation/grouping
50. Reinforcement
51. Task assignment
52. Target selection/evaluation
53. Movement/route execution
54. Local advantage evaluation
55. Micro/tactical execution
56. Defense
57. Retreat
58. Attack lifecycle
59. Attack restart/recovery
60. Siege/counter-siege
61. Capture/forward operations
62. Military idle recovery
63. Cavalry Threat Containment vertical slice
64. Archer/skirmisher threat containment
65. Infantry threat containment
66. Cavalry-archer threat containment
67. Gunpowder threat containment
68. Monk/religious threat containment
69. Siege threat containment
70. Combined-arms response
71. Naval military operations
72. Naval/economic interaction
73. Map control / mobility / positioning

### F. Strategic operating layer
74. Situation classification
75. Objective management
76. Requirements derivation
77. Candidate generation
78. Candidate evaluation
79. Decision/commitment
80. Strategic resource commitment
81. Timing / initiative / tempo
82. Transition management
83. Economic↔military arbitration
84. Technology↔military arbitration
85. Map-position↔economy arbitration
86. Defensive↔offensive posture arbitration
87. Opponent-aware adaptation
88. Late-game / population-saturation management
89. Wonder/ending-state management
90. Trade / market / resource conversion
91. Ally coordination
92. Resource requests / interaction control signals
93. Communication/taunt strategy where behaviorally relevant

### G. Reliability and integration
94. Command evidence ladder
95. Verification supervisor
96. Failure classification
97. Retry/recovery/replan
98. Generation/lifetime management
99. Cross-service arbitration
100. Regression protection
101. Stress/failure scenarios
102. Full-system strategic integration
103. Final Byzantine tuning and behavioral qualification

## 3. Vertical-slice construction order

The implementation order is deliberately dependency-driven rather than merely thematic:

**Slice 0 — ABI + initialization + state spine**

**Slice 1 — Villager continuity:** villager production + housing + idle recovery.

**Slice 2 — Food continuity:** food-source portfolio + hunting/boar + farms + transitions.

**Slice 3 — Worker/resource economy:** worker roles + resource sites + dropsites + wood/gold/stone + measured income.

**Slice 4 — Economic arbitration:** demand vectors + escrow + reservations + opportunity cost + hysteresis.

**Slice 5 — Construction OS:** placement + builders + foundations + completion + failure/rebuild.

**Slice 6 — Technology OS:** age-up + research + prerequisites + reservations + capability realization.

**Slice 7 — Information OS:** scouting + exploration + enemy identification + information freshness.

**Slice 8 — Threat model:** military observation + composition scoring + threat classification + belief updates.

**Slice 9 — Cavalry Threat Containment:** first complete strategic/military vertical slice using the already-established substrate.

**Slice 10 — Military production/composition:** production requests + force composition + reinforcement + grouping.

**Slice 11 — Movement/tasking:** routes + positioning + task assignment + local advantage.

**Slice 12 — Defense/retreat/recovery:** defensive posture + retreat lifecycle + restart/reinforcement.

**Slice 13 — Attack:** target evaluation + attack lifecycle + siege integration + recovery.

**Slice 14 — Other threat families:** archers, skirmishers, infantry, cavalry archers, gunpowder, monks, siege, then combined-arms responses.

**Slice 15 — Map/mobility:** spatial control, forward operations, capture, mobility and positioning.

**Slice 16 — Naval/water:** water economy, naval production, naval military behavior and land/water coupling.

**Slice 17 — Trade/market/conversion:** trade, market conversion and economic fallback.

**Slice 18 — Interaction/ally coordination:** resource requests, coordination, communication/control signals.

**Slice 19 — Strategic arbitration:** simultaneous competing objectives, opponent adaptation, timing, initiative, transitions and posture changes.

**Slice 20 — Late game:** population saturation, resource exhaustion, wonder/ending-state logic and late-game production/economy.

**Slice 21 — Recovery integration:** cross-system failure diagnosis, stale state, partial completion, conflicting commitments and replan.

**Slice 22 — Full-system integration:** complete civilization loop under sustained adversarial conditions.

**Slice 23 — Final qualification:** static, ABI, runtime, stress, regression and Byzantine behavioral qualification.

## 4. Mandatory slice contract

Every slice must document and qualify:

`OBSERVE/RECONCILE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENTS → CONSTRAINTS → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → FAILURE/RECOVERY → BELIEF UPDATE → REASSESS`

For operational actions, evidence must preserve the ladder:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

No lower evidence level may be reported as a higher one.

## 5. Stock-AI adversarial completeness rule

AI(HD)+Promisory is treated as a hostile senior reviewer. Before a slice is accepted, compare it against the relevant stock corpus and ask:

- What operational service exists in stock that AEGIS does not yet provide?
- What persistent state does stock maintain that AEGIS has omitted?
- What failure/retry/recovery behavior exists in stock that AEGIS lacks?
- What cross-system feedback path exists in stock that AEGIS has broken?
- What mundane continuity behavior keeps the civilization alive?
- What map, resource, military, technology, water, trade, interaction or late-game mode is absent?
- What rule-order, timer, queue, search, placement or serviceability dependency is unrepresented?

An omission is not acceptable merely because AEGIS has a higher-level strategic abstraction for it.

## 6. Evidence discipline

Stock source is historical/behavioral evidence, not runtime authority. Every AEGIS implementation requires its own provenance, ownership, ABI justification and qualification status. No state channel is allocated merely because a numeric scan says it is unused. No command is treated as completion. No historical-only symbol is promoted without qualification.

## 7. Completion definition

The bot is not complete when all files exist. It is complete when the civilization can sustain itself, perceive and interpret the world, choose and execute objectives, fight and recover, adapt to opponent behavior, handle the stock operating domains identified above, and survive adversarial integration/regression testing on the target build.

## 8. Governing construction rule

**Build the substrate that makes strategic intelligence executable; then continuously connect that substrate to cognition through permanent vertical slices. Use AI(HD)+Promisory to attack the blueprint at every slice. If stock knows how to do something that this blueprint does not, the blueprint is incomplete until the omission is explained and dispositioned.**
