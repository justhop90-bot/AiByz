# AEGIS Team Candidate Selection — Subsystem Five-Pass Quality

**Date:** 2026-09-05  
**Phase:** Post-Layer-3A architecture / pre-implementation  
**Purpose:** Select one additional specialist role whose presence increases the quality of every five-pass subsystem review without lowering the standard or reopening the architecture loop.

## 1. Decision

**Selected team member: SYSTEMS ASSURANCE & INTEGRATION ENGINEER**

Mission:

> Act as the independent engineer responsible for proving that each subsystem survives contact with the rest of AEGIS, the AoE2DE engine model, resource/attention constraints, and the evidence standard—without taking ownership away from Architect, Carpenter, Adversary, or Scientist.

This is not a fifth architecture persona. It is a **quality-control and integration role** that participates across all five passes.

The four existing modes remain:

1. Architect — build the best useful conceptual structure.
2. Carpenter — remove complexity that does not earn its cost.
3. Adversary — construct failures and attack assumptions.
4. Scientist — determine what is actually true.

The new role is the **Systems Assurance Engineer**. It asks whether the four perspectives have converged on a subsystem that is actually ready to leave architecture and enter qualification/implementation.

## 2. Why this candidate wins

The project does not currently suffer from a shortage of ideas. It suffers from the risk of:

- excellent local reasoning producing weak interfaces;
- architecture becoming detached from engine reality;
- adversarial findings being documented but not closed;
- scientific evidence failing to propagate into architectural decisions;
- repeated passes producing diminishing returns;
- subsystems becoming individually elegant but globally incompatible;
- implementation discoveries being mistaken for reasons to restart architecture;
- acceptance criteria becoming vague or ceremonial.

A Systems Assurance Engineer directly attacks those failure modes.

The role does **not** add another room, another planner, another state system, or another layer of abstraction.

It adds a disciplined question to every pass:

> **What evidence and interface contract would make us willing to sign this subsystem off?**

## 3. The five-pass operating protocol

Every subsystem receives five passes, but each pass has a stronger cross-system obligation.

### Pass 1 — Architect

Build the minimum useful conceptual design.

Assurance question:

> What does this subsystem own, consume, publish, and explicitly refuse to own?

### Pass 2 — Carpenter

Remove unnecessary machinery.

Assurance question:

> Which remaining component has measurable behavioral return, and which is merely architectural decoration?

### Pass 3 — Adversary

Attack the design.

Assurance question:

> Which failure crosses a subsystem boundary, and who is responsible for containing it?

### Pass 4 — Scientist

Determine what is actually true.

Assurance question:

> Which claims are proven, documented, observed, inferred, proposed, or unknown—and which claims must be tested before implementation?

### Pass 5 — Systems Assurance / Integration

Perform the final integration examination.

Assurance question:

> Does the surviving subsystem have a coherent contract with every adjacent subsystem, a defensible evidence boundary, a defined failure response, and a clear implementation/qualification handoff?

The fifth pass does **not** redesign the subsystem by default. It signs off, requests a targeted correction, or rejects the closure.

## 4. Required output of every subsystem

Each subsystem must leave the five-pass process with:

```text
MISSION
OWNER
INPUTS
OUTPUTS
BOUNDARIES
DEPENDENCIES
STATE OWNERSHIP
FAILURE MODES
RECOVERY RESPONSIBILITY
EVIDENCE CLASSIFICATION
ENGINE QUESTIONS
RUNTIME QUESTIONS
COST CONSTRAINTS
ACCEPTANCE CRITERIA
OPEN ITEMS
IMPLEMENTATION HANDOFF
```

Not every item requires a literal data structure. These are review questions and contractual obligations.

## 5. The five-pass quality gate

A subsystem is **not CLOSED** because five documents exist.

It is CLOSED only when:

1. Architect can explain the subsystem in one coherent model.
2. Carpenter cannot remove meaningful complexity without losing behavior.
3. Adversary cannot find an unowned critical failure.
4. Scientist can distinguish fact from inference and identify all material unknowns.
5. Systems Assurance can trace the subsystem through its neighbors and define the exact next engineering action.

If #5 fails, the subsystem returns only to the **specific failed pass**. The entire five-pass cycle is not automatically restarted.

This is the principal mechanism for preventing endless review loops.

## 6. Independence rule

Systems Assurance must be willing to say:

- PASS;
- PASS WITH TARGETED CORRECTION;
- HOLD FOR EVIDENCE;
- REJECT;
- RETURN TO SPECIFIC PASS.

It must not manufacture consensus.

If Architect and Carpenter disagree, the Assurance Engineer does not vote based on preference. It identifies the missing acceptance criterion or evidence.

If Scientist says an engine behavior is unknown, Assurance prevents architecture from treating it as fact.

If Adversary finds a failure but nobody owns recovery, Assurance blocks closure.

If Carpenter identifies machinery that adds no behavioral return, Assurance supports its removal unless a concrete acceptance criterion depends on it.

## 7. Integration matrix

For every subsystem, Assurance reviews at least these interfaces:

```text
WORLD STATE
BELIEF
SITUATION
OBJECTIVES
PLANNING
DECISION
CAPABILITY
COMMITMENT / EXECUTION
VERIFICATION
RECOVERY
ECONOMY
PRODUCTION
INFRASTRUCTURE
TECHNOLOGY
MILITARY
OPERATIONS
MAP CONTROL
ATTENTION
SCHEDULER
MEMORY
RESOURCE LEDGER
DOCTRINE
RISK
STATE INTEGRITY
```

Only materially adjacent interfaces need detailed treatment; the list is a completeness check, not a mandate to create dependencies everywhere.

## 8. Anti-bloat rule

The new team member is expressly forbidden from becoming a fifth planner.

It may not:

- invent strategic policy;
- create duplicate state ownership;
- replace Architect;
- replace Carpenter;
- replace Adversary;
- replace Scientist;
- create universal metadata;
- demand a new subsystem merely for conceptual neatness;
- require implementation before evidence;
- reopen Layer 3A merely because implementation is inconvenient.

Its authority is **quality assurance**, not strategic design ownership.

## 9. Candidate pool — 100 possible specialists

The following are candidate team roles considered for the additional seat.

### Architecture / systems

1. Systems Assurance & Integration Engineer
2. Principal Systems Architect
3. Distributed Systems Architect
4. Control Systems Architect
5. Systems-of-Systems Engineer
6. Interface Contract Engineer
7. Architecture Decision Analyst
8. Requirements Systems Engineer
9. Systems Boundary Analyst
10. Complexity Management Engineer

### Verification / reliability

11. Formal Methods Engineer
12. Verification & Validation Engineer
13. Reliability Engineer
14. Safety-Critical Systems Engineer
15. Fault-Tolerance Engineer
16. Failure Analysis Engineer
17. Resilience Engineer
18. Test Architecture Engineer
19. Quality Systems Engineer
20. Independent Design Reviewer

### Adversarial / security mindset

21. Red-Team Systems Engineer
22. Chaos Engineer
23. Hostile Scenario Analyst
24. Failure Injection Specialist
25. Threat Modeling Engineer
26. Robustness Engineer
27. Defensive Systems Analyst
28. Game-Theoretic Adversary
29. Worst-Case Analyst
30. Counterexample Engineer

### AoE2 / game-AI specialization

31. AoE2 AI Scripting Specialist
32. AoE2 Engine Semantics Specialist
33. RTS AI Systems Engineer
34. Game AI Architecture Engineer
35. Competitive RTS Analyst
36. Build-Order Systems Engineer
37. Combat AI Specialist
38. Economic AI Specialist
39. Opponent Modeling Specialist
40. RTS Micro Systems Engineer

### Reverse engineering / ABI

41. Engine Reverse Engineer
42. ABI Research Engineer
43. Binary Interface Analyst
44. Runtime Semantics Engineer
45. Protocol Reverse Engineer
46. Compatibility Engineer
47. Build Provenance Engineer
48. Software Archaeologist
49. Static Analysis Engineer
50. Program Semantics Engineer

### Data / evidence

51. Evidence Systems Engineer
52. Data Provenance Engineer
53. Scientific Method Lead
54. Experimental Design Engineer
55. Measurement Systems Engineer
56. Telemetry Architect
57. Observability Engineer
58. Data Quality Engineer
59. Causal Analysis Engineer
60. Reproducibility Engineer

### Runtime / performance

61. Runtime Systems Engineer
62. Performance Engineer
63. Real-Time Systems Engineer
64. Scheduling Systems Engineer
65. Resource Allocation Engineer
66. Concurrency Analyst
67. Latency Engineer
68. Runtime Cost Auditor
69. Control-Loop Engineer
70. Embedded Systems Engineer

### Decision / control

71. Decision Systems Engineer
72. Control Theory Engineer
73. Planning Systems Engineer
74. Optimization Engineer
75. Operations Research Engineer
76. Constraint Systems Engineer
77. Policy Systems Engineer
78. Decision Theory Specialist
79. Multi-Agent Systems Engineer
80. Adaptive Systems Engineer

### Software engineering / maintainability

81. Principal Software Engineer
82. Refactoring Specialist
83. Codebase Archaeologist
84. Dependency Architect
85. API Design Engineer
86. Maintainability Engineer
87. Configuration Systems Engineer
88. Build Systems Engineer
89. Release Engineer
90. Technical Debt Analyst

### Strategic / organizational

91. Program Systems Engineer
92. Engineering Process Architect
93. Research Program Lead
94. Technical Review Chair
95. Engineering Standards Lead
96. Knowledge Systems Architect
97. Decision Governance Engineer
98. Project Risk Engineer
99. Integration Program Manager
100. Systems Engineering Lead

## 10. Selection scoring

The candidate was judged against the actual need, not prestige.

| Criterion | Weight | What matters |
|---|---:|---|
| Improves all five passes | 25% | Must raise the quality of every subsystem review |
| Cross-system integration | 20% | Must catch interface failures, not just local defects |
| Evidence discipline | 15% | Must prevent inference from becoming fact |
| Anti-complexity | 15% | Must not become another architecture-expansion engine |
| Engine/implementation handoff | 10% | Must identify what happens next |
| Failure ownership | 10% | Must expose unowned failure/recovery paths |
| Independence | 5% | Must be willing to block closure |

### Highest-value alternatives

**#1 Systems Assurance & Integration Engineer** — best overall fit.

**#11 Formal Methods Engineer** — exceptionally strong for invariants, but too narrow and potentially too formal for the `.per`/runtime boundary.

**#12 Verification & Validation Engineer** — excellent, but less naturally responsible for architecture-wide interface coherence.

**#32 AoE2 Engine Semantics Specialist** — extremely valuable, but overlaps heavily with Scientist and is most useful during qualification rather than every architectural pass.

**#42 ABI Research Engineer** — crucial later, but not the missing capability in every subsystem's architecture review.

**#64 Scheduling Systems Engineer** — important, but subsystem-specific rather than architecture-wide.

**#69 Control-Loop Engineer** — excellent fit for feedback and timing, but narrower than the integration problem.

**#79 Multi-Agent Systems Engineer** — interesting conceptually, but risks introducing abstractions the project does not need.

**#81 Principal Software Engineer** — broad enough, but insufficiently specialized toward evidence and independent assurance.

**#100 Systems Engineering Lead** — very close, but the title is broader and more managerial than the precise role we need.

## 11. Why not simply add another Adversary?

Because the existing Adversary is already tasked with breaking the design.

The missing question is different:

> After the design has been attacked, what proves that the surviving design is ready to cross into engineering?

Systems Assurance fills that gap.

## 12. Why not simply add another Scientist?

Because Scientist determines what is true.

Systems Assurance determines whether the **truth, architecture, interfaces, failure handling, and next engineering step form a coherent whole**.

Those are complementary functions.

## 13. Why not make the new member a formal-methods specialist?

Formal methods are valuable, especially for invariants and state-machine reasoning. But the project currently has a more immediate systems problem:

`ENGINE EVIDENCE ↔ ARCHITECTURE ↔ INTERFACES ↔ IMPLEMENTATION`

A pure formal-methods specialist risks optimizing rigor inside the wrong boundary.

Formal methods can become a tool used by Systems Assurance where they earn their cost.

## 14. Operating rhythm

The team should now operate as:

```text
                ┌───────────────┐
                │   ARCHITECT   │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │   CARPENTER   │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │   ADVERSARY   │
                └───────┬───────┘
                        ↓
                ┌───────────────┐
                │   SCIENTIST   │
                └───────┬───────┘
                        ↓
          ┌──────────────────────────┐
          │ SYSTEMS ASSURANCE /      │
          │ INTEGRATION              │
          └────────────┬─────────────┘
                       ↓
                 SUBSYSTEM CLOSED
                       ↓
             QUALIFICATION / BUILD
```

The important change is that Systems Assurance is not another round in an endless loop. It is the **exit gate**.

## 15. Return-to-pass rule

If Assurance identifies a problem:

```text
ASSURANCE FINDING
       ↓
WHICH PASS OWNS THE DEFECT?
       ↓
TARGETED RETURN
       ↓
CORRECTION
       ↓
ASSURANCE RECHECK
```

Not:

```text
ASSURANCE FINDING
       ↓
START FIVE PASSES AGAIN
```

This is how we preserve quality without allowing review recursion to become infinite.

## 16. Definition of done

A subsystem is ready for the next engineering phase when Systems Assurance can answer YES to all of these:

- Is its purpose unambiguous?
- Is ownership unambiguous?
- Are its inputs and outputs bounded?
- Are its neighbors known?
- Are failure modes owned?
- Are recovery paths owned?
- Are material assumptions explicit?
- Are engine facts separated from architecture proposals?
- Are unresolved engine questions explicitly listed?
- Are runtime-cost questions identified?
- Are implementation questions separated from architecture questions?
- Can the subsystem be tested independently enough to produce useful evidence?
- Does it preserve the global AEGIS invariants?
- Does it avoid duplicate state ownership?
- Does it provide meaningful behavioral return for its complexity?
- Is there a clear next action?

If yes: **CLOSED.**

If no: targeted correction.

## 17. Final recommendation

**Add Systems Assurance & Integration Engineer to the team.**

Do not add another architect.
Do not add another generic adversary.
Do not add another generic scientist.
Do not add a manager.

Add the person whose job is to make the other four better **without becoming a fifth source of design authority**.

The objective is not five voices.

The objective is a higher-quality five-pass process.

That is the distinction that makes this addition worthwhile.
