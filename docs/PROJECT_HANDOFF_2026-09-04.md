# AiByz / AEGIS — Professional Engineering Handoff

**Date:** 2026-09-04  
**Repository:** `justhop90-bot/AiByz`  
**Active branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Layer-1 position:** 89%, investigation frozen for handoff  
**Layer-2 position:** active; strategic archaeology substantially recovered  
**Scenario-loader:** permanently retired

## 1. Purpose

This document is the recovery point for an engineer or AI that inherits AiByz after the conversational context is gone.

The goal is not merely to describe files. It records the current mental model of the project: what has been established, what remains uncertain, which investigations were intentionally stopped, which tools are available, and what architecture should be built next.

## 2. Primary mission

Build AEGIS, a high-quality Byzantine AI for Age of Empires II: Definitive Edition.

The intended bot is not a static build order and not a pile of tactical reactions. It should maintain strategic state, reason about uncertainty and competing objectives, acquire capabilities, manage resources and production capacity, act, verify consequences, recover from failure, and continuously reassess.

The central architecture is:

`WORLD → OBSERVE → CLASSIFY → BELIEVE → DETECT TRANSITION → DEFINE OBJECTIVE → DERIVE REQUIREMENTS → PROPAGATE CONSTRAINTS → GENERATE CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → CLASSIFY RESULT → UPDATE BELIEFS → RECOVER / REINFORCE → REASSESS`

This is an AEGIS architecture, not a claim that HD/Promisory implemented these semantic objects explicitly.

## 3. Strategic correction about HD

Do not inherit the mistaken framing that the HD source has little or no strategic success.

Project operating assessment: the historical HD AI is a **capable bot with a decent, if not high, level of strategic success; it is materially less capable than a decent human player**.

That assessment matters. HD/Promisory is valuable precisely because the programmer solved real AoE2 strategic problems well enough to produce a competent player under the severe constraints of `.per`. We should study what makes it competent, then identify where its abstractions, heuristics, engine limitations, and historical assumptions leave performance on the table.

Static source archaeology still cannot prove a specific match outcome. Keep that distinction. But do not confuse “cannot prove every outcome from source” with “the source lacks strategic competence.”

## 4. Layer status

### Layer 1 — Machine

Frozen at **89%**.

Established: rule/fact/search/action vocabulary, native state concepts, feasibility boundaries, UnitAI architecture, identity distinctions, `.pdata` function geometry, controlled executable identity, and multiple native negative findings.

Open only if implementation requires it: persistent-fact mutation/freshness; `CurrentOrder → CurrentAction`; rule/handler-to-action bridge; failure/completion propagation; required object lifecycle; one predictive end-to-end experiment.

Do not restart broad vocabulary collection.

### Layer 2 — Strategy / HD archaeology

Active.

The verified HD/Promisory source is the reconstruction authority. Current machine semantics remain Layer-1 authority.

Recovered themes:

- stateful controller;
- measurement compressed into reusable state;
- guard-before-side-effect;
- contextual resource allocation;
- protected strategic transitions via escrow;
- production as capability pipeline;
- threat classification and counter-capability response;
- search/candidate evaluation implemented through rule-state machinery;
- scouting as constrained geometry and information acquisition;
- attack/retreat/restart lifecycle;
- timers and persistent state as temporal control;
- explicit fallback/recovery behavior.

Latest Pass 35 created an evidence-edge ledger so strategic claims cannot silently jump from direct control evidence to unsupported outcome claims.

### Layer 3 — Byzantine doctrine

Not yet the primary implementation stream. It should begin after the general strategic ontology is stable enough to express Byzantine-specific advantages, weaknesses, transition priorities, counters, and map/economy doctrine.

### Layer 4 — Runtime implementation

Downstream. The minimal replay interpreter is a research instrument, not the bot runtime.

## 5. Historical strategic model

The most useful reconstruction is:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION → STATE → REQUIREMENT → COMMITMENT → AUTHORITY → ACTION → WORLD POSTCONDITION → STRATEGIC POSTCONDITION`

The programmer repeatedly works around the limited state/control primitives of `.per` by distributing a larger controller across goals, strategic numbers, flags, timers, searches, target points, and rule eligibility.

### Stateful player

`FACTS → OBSERVATIONS → GOALS/SNs/FLAGS/TIMERS → INTERNAL STATE → RULE TRANSITIONS → ACTIONS → WORLD`

### Resources

Resources behave strategically as future capability commitments. Quantity alone is insufficient; current objective, reservation, income, opportunity cost, and timing matter.

### Production

Desired capability becomes production authorization, then feasibility, then queue/action, then verification. A unit count is not the same thing as production capability.

### Threats

The source measures opponent composition and contextual conditions into reusable threat state. The strongest example is cavalry/cavalry-archer pressure feeding camel-response production.

### Military

Attack state, retreat state, restart state, timers, and fortification responses create a lifecycle controller rather than a one-shot attack rule.

### Information

Scout control contains path safety, quarterstep analysis, pivot candidates, interpolation, waypoint selection, and movement. The exact information-value objective remains partially unresolved.

### Search

Historical searches are distributed loops: reset, candidate acquisition, filtering, measurement, comparison, best-candidate preservation, state advancement, repeat/exit. This is not conventional procedural iteration but it is real algorithmic search.

## 6. Four strategic chains to implement

### C1 — Threat → capability

`OBSERVE ENEMY → CLASSIFY THREAT → DEFINE REQUIRED CAPABILITY → RESERVE → PRODUCE → VERIFY → REASSESS`

Highest priority because historical causal closure is strongest here.

### C2 — Strategic transition

`DESIRE AGE/TECH → PROTECT RESOURCES → CHECK FEASIBILITY → RESEARCH → VERIFY NEW CAPABILITY → REALLOCATE`

### C3 — Military lifecycle

`CAPABILITY → ATTACK COMMITMENT → ENGAGE → ASSESS → RETREAT/CONTINUE → REGROUP → RESTART/ABANDON`

### C4 — Information → action

`INFORMATION GAP → SCOUT CANDIDATES → SAFETY/UTILITY EVALUATION → MOVE → OBSERVE → UPDATE BELIEF`

## 7. Evidence rules

Grades:

- DIRECT
- COMPOSED
- INFERRED
- AEGIS-GENERALIZATION
- UNCERTAIN

Closure:

- CONTROL
- WORLD
- STRATEGIC

Never upgrade closure because a mechanism is strategically plausible.

Canonical research unit:

`OBSERVATION → CLASSIFICATION → STATE WRITE → AUTHORITY EFFECT → RESOURCE/PRODUCTION CONSEQUENCE → TEMPORAL GUARD → REASSESSMENT`

## 8. Replay archaeology

Reference body SHA-256:
`4269461f0cd488ae034f0371e7ef4a083d7f28bd60ae1054f1510e7daa519f3d`

Normalized JSONL SHA-256:
`3a5ceff2654d86155407dfe98acbab37c3c8432121228d5d0a5959b68c78b9f3`

The raw body produced 597,681 decoded operations: 6,858 ACTION, 295,407 SYNC, 295,407 VIEWLOCK, 8 CHAT, and 1 POSTGAME. Zero unknown/fallback operation IDs occurred in the reference corpus.

The minimal replay interpreter intentionally leaves W1/W2/W3 open. `DE_QUEUE`, `BUILD`, `RESEARCH`, and `DELETE` are command/pending evidence, not automatic completion proof.

## 9. CaptureAge / CADE

Installed version investigated: 1.25.0.

`cade.node` SHA-256:
`C64832B06229D445B4E735BB1A768100B044B64A6A74A32C45710853725BCC61`

The runtime exposes rich state vocabulary and lifecycle events and the application logs show replay loading and patch/world-time activity. Passes 31–33 did not establish a clean supported external replay→lifecycle extraction contract.

Disposition: **secondary validation candidate, not primary research path**.

Do not perform binary patching merely to continue this investigation. Do not revive scenario-loader automation.

## 10. Tools

### GitHub

Canonical repository, branch/commit history, PR #15, evidence artifacts, review comments, and remote provenance.

### Remote Desktop Commander

Authorized workstation inspection, filesystem access, PowerShell/Python processes, searches, runtime experiments, hashing, artifact creation, and local repository QC.

Remote device used for the latest runtime work:
`Weebo` — device ID `1aa2f154-9f15-4d83-94d1-dd0121f6bd29`.

### AoE2DE

Target runtime for eventual `.per` execution and manual/controlled validation.

### mgz-fast / aoc-mgz

Replay decoding and normalized evidence extraction.

### CaptureAge / CADE

Optional rich replay/state validation candidate.

### Python / PowerShell / Git

Deterministic analysis, hashing, Windows inspection, local QC, and source-control operations.

## 11. Important local evidence paths

Reference replay body:
`C:\Users\justh\Desktop\AEGIS-AI-LAB\06_REPLAYS\08_FORENSIC_RUNS\2026-09-02_REFERENCE\body.bin`

Local mgz-fast parser:
`C:\Users\justh\Games\Age of Empires 2 DE\76561198093432383\savegame\mgz-fast-master\mgz-fast-master\mgz\fast\__init__.py`

CaptureAge installation:
`C:\Users\justh\AppData\Local\Programs\CaptureAge`

These paths are machine-specific evidence locations, not portable project dependencies.

## 12. Key historical artifacts

- `03_HD_ARCHAEOLOGY/HD_META_KNOWLEDGE_PASS3_2026-09-04.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_PRACTICAL_CODING_KNOWLEDGE_BASE.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_STRATEGIC_PROBLEM_MATRIX.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_CROSS_SYSTEM_CONTROL_GRAPH_PASS12_2026-09-04.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_HISTORICAL_CODE_TO_STRATEGY_LAB_PASS9_2026-09-04.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_EXACT_ANCHOR_HISTORICAL_TRACE_PACK_PASS10_2026-09-04.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_RAW_REPLAY_OPCODE_LIFECYCLE_ARCHAEOLOGY_PASS21_2026-09-04.md`
- `03_HD_ARCHAEOLOGY/AOE2DE_MINIMAL_REPLAY_INTERPRETER_DESIGN_PASS22_2026-09-04.md`
- `03_HD_ARCHAEOLOGY/PASS35_HD_EVIDENCE_EDGE_LEDGER_AUDIT_2026-09-04.md`
- `05_RUNTIME_CANDIDATE/minimal_replay_interpreter_pass23.py`

## 13. Known open questions

- What is the exact information-value objective behind the full scout controller?
- What strategic purpose does the 504/505 maximum-distance construction serve?
- Which historical production/technology commitments are genuinely adaptive versus fixed heuristics?
- How does the historical AI detect and recover from false threat classification?
- How should AEGIS quantify capability value, opportunity cost, initiative, and optionality without creating an overfit optimizer?
- Which HD mechanisms are strategically valuable and which are historical implementation debt?
- How should Byzantine-specific doctrine modify the general transition architecture?

## 14. What not to do

- Do not reopen Layer 1 broadly.
- Do not revive scenario-loader testing.
- Do not turn CADE into the primary project.
- Do not treat parser guesses as engine truth.
- Do not equate command issuance with world completion.
- Do not equate world completion with strategic success.
- Do not equate a historical heuristic with universal optimality.
- Do not erase failed investigations.
- Do not replace an uncertain claim with a cleaner-sounding unsupported one.
- Do not write AEGIS as a direct transcription of HD.

## 15. Immediate next work

Formalize **C1 — Threat → Capability**.

Define and test:

`OBSERVATION`
`BELIEF`
`THREAT_VECTOR`
`OBJECTIVE`
`REQUIREMENT`
`CAPABILITY_CANDIDATE`
`RESOURCE_COMMITMENT`
`PRODUCTION_AUTHORITY`
`ACTION`
`EXPECTED_POSTCONDITION`
`VERIFIED_POSTCONDITION`
`FAILURE_SIGNATURE`
`RECOVERY_POLICY`
`REASSESSMENT`

The first implementation should demonstrate the complete loop on one strategically meaningful counter-capability case before broadening the ontology.

## 16. Handoff success criterion

A new AI should be able to answer, without conversational memory:

1. What are we building?
2. Why was Layer 1 stopped at 89%?
3. What do we actually know about the machine?
4. What do we actually know about HD/Promisory?
5. How strategically capable is the historical AI?
6. Which claims are direct versus inferred?
7. Which investigations were intentionally retired?
8. What tools and evidence are available?
9. What remains uncertain?
10. What should be built next?

If the answer to any of these requires remembering the old conversation, the repository handoff is incomplete.
