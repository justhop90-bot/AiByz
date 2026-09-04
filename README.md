# AiByz — AEGIS Byzantine AI Engineering Repository

> A professional research, reverse-engineering, strategy-modeling, and implementation repository for building a high-quality Byzantine AI for Age of Empires II: Definitive Edition.

## Project mission

AiByz is the institutional memory and engineering base for **AEGIS**, a planned next-generation Byzantine AI for **Age of Empires II: Definitive Edition (AoE2DE)**.

The project is built in layers because a strong bot requires more than a large collection of rules. We first establish the machine contract, then recover how competent historical AI code reasons about the strategy game, then formulate Byzantine doctrine, and finally implement and validate the resulting architecture.

The durable product is **knowledge with provenance**: evidence, failures, corrections, strategic interpretation, architecture, implementation requirements, and validation criteria must survive independently of any single engineer or model.

---

# Current project state — 2026-09-04

| Layer | Purpose | Status |
|---|---|---|
| **Layer 1 — Machine** | AoE2DE execution/runtime semantics | **Investigation frozen at 89%; handoff complete, certification incomplete** |
| **Layer 2 — Strategy / HD archaeology** | Recover the programmer's strategic model and reusable engineering patterns | **Active; major architecture recovered; moving toward formal AEGIS specifications** |
| **Layer 3 — Byzantine doctrine** | Convert general strategy into Byzantine-specific strategic doctrine | **Next major downstream phase** |
| **Layer 4 — Implementation** | Build, validate, benchmark, and promote the runtime `.per` AI | **Downstream** |

### Critical boundary decisions

- **Layer 1 remains frozen at 89%.** Do not reopen broad machine archaeology unless a new implementation requirement specifically demands one of the recorded closure targets.
- **Scenario-loader automation/testing is permanently retired.** Do not resurrect it as a validation strategy.
- **CaptureAge/CADE is retained as an optional future validation backend, not as a project dependency or unquestioned oracle.**
- **Historical HD/Promisory source is the Layer-2 reconstruction authority.** Current runtime semantics remain governed by Layer-1 evidence.
- The historical HD source should **not** be characterized as strategically unsuccessful merely because it is below competent human play. The project operating assessment is that it is a **capable bot with a decent level of strategic success, but materially below a decent human player**. Static source cannot prove a particular match outcome, but the architecture clearly embodies meaningful game-playing strategy and is worth mining rather than treating as a toy ruleset.

---

# What we now understand

## Layer 1 — machine boundary

The controlled Layer-1 investigation established a bounded machine model rather than a complete native specification.

Key findings include:

- `.ai/.per` are the relevant AI script substrate.
- Native rule state includes IDs, priorities, intervals, sorted-rule state, and rule-group concepts.
- Native AI vocabulary establishes fact initialization and a distinct persistent-fact evaluation phase.
- Feasibility/validation is a machine-executability boundary separate from strategic desirability.
- UnitAI exposes distinct order/action/target/notification/search/recovery concepts.
- Native search includes filtering, ownership, LOS, pathability, range, and target-selection machinery.
- Unit/object/copy/class/type/owner identities must not be conflated merely because they are numeric.
- The controlled PE contains **166,730 non-zero `.pdata` runtime-function records across 166,741 physical slots**.
- CodeView `RSDS` data identifies a PDB GUID/age, but no authenticated matching PDB was found locally.
- The controlled `AoE2DE_s.exe` build SHA-256 is `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`.
- The latest qualified stock-AI corpus measurement is **7,831 syntactically reachable `defrule` definitions across 28 reachable `.per/.per2/.xs` files**, under conservative conditional-branch inclusion. The former 7,715 figure is retired.

Layer-1 completion targets remain explicitly recorded rather than guessed closed: persistent-fact mutation/freshness, `CurrentOrder -> CurrentAction`, rule/handler-to-action bridge, failure/completion propagation, required object lifecycle edges, and one predictive end-to-end `.per` experiment.

## Layer 2 — the programmer's strategic model

The historical source is not merely a pile of tactical rules. Repeated archaeology reveals a capable, stateful controller designed to play the strategy game through constrained engine primitives.

The strongest recovered motifs are:

1. **Measure → compress → reuse.** Enemy and world observations are converted into reusable state channels.
2. **Guard before side effect.** Feasibility and contextual predicates precede commands.
3. **Search before commitment.** Candidate objects, workers, positions, and targets are filtered and evaluated before action.
4. **Protect strategic transitions.** Escrow and state controls prevent competing spending from trivially destroying intended transitions.
5. **Treat production as capability acquisition.** Desired units are enabled, constrained, searched, and produced through a distributed pipeline.
6. **Treat attacks as lifecycles.** Attack, retreat, regroup/reset, and restart are distinct control states.
7. **Use geometry operationally.** Scouting and movement contain explicit safety/path/candidate geometry.
8. **Recover from failure.** Building and other subsystems contain fallback behavior rather than assuming commands always succeed.
9. **Use timers and persistent state to create temporal control.** Loops are distributed through eligibility, state, jumps, and timers rather than conventional procedural loops.
10. **Continuously convert one capability into another.** Economy, technology, production, military pressure, information, and position form a coupled system.

The project now treats the central historical pattern as:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION/BELIEF → REQUIREMENT → CAPABILITY CANDIDATES → RESOURCE/TIMING EVALUATION → COMMITMENT → AUTHORITY → ACTION → POSTCONDITION → FAILURE/RECOVERY → REASSESSMENT`

This is an AEGIS architecture derived from historical evidence; it is not claimed to be a literal module diagram of HD/Promisory.

---

# Strategic architecture recovered so far

## Stateful player

`FACTS → OBSERVATIONS → GOALS / SNs / FLAGS / TIMERS → INTERNAL STATE → RULE TRANSITIONS → ACTIONS → WORLD`

The programmer's key adaptation is to represent strategic state using the primitive channels available to `.per`, then let many small rules act as a distributed controller.

## Resources as future capability commitments

Resources are not just current quantities. Their strategic value depends on what the player is trying to purchase next, what has already been committed, and what alternative capability is sacrificed by spending them.

AEGIS therefore distinguishes:

`RAW STOCK | INCOME | COMMITTED STOCK | RESERVE | NEAR-TERM DEMAND | OPPORTUNITY COST`

The explicit formulae are AEGIS generalizations, not claims that HD computes them mathematically.

## Capability/candidate evaluation

The recovered strategic abstraction is:

`OPPONENT CAPABILITY → THREAT VECTOR → REQUIRED COUNTER-CAPABILITY → CANDIDATE RESPONSES → COST/TIMING/POSITION/RISK → COMMITMENT`

Candidate responses need not be limited to a counter unit. They may include:

`COUNTER_UNIT | FORTIFICATION | MOBILITY | POSITIONAL_DENIAL | ECONOMIC_RELOCATION | RETREAT | COUNTER_ATTACK | SIEGE | TECHNOLOGY | DELAY`

## Closed-loop control

AEGIS inherits the most important engineering correction from the archaeology:

`DECIDE → COMMIT → ATTEMPT → OBSERVE WORLD → VERIFY POSTCONDITION → UPDATE STATE → CONTINUE / MODIFY / ABORT`

A command is never treated as proof that the desired world transition occurred.

---

# Four primary AEGIS strategic chains

### C1 — Threat → capability

`OBSERVE ENEMY → CLASSIFY THREAT → DEFINE REQUIRED CAPABILITY → RESERVE → PRODUCE → VERIFY → REASSESS`

This is the first formal transition to implement because it has the strongest historical causal closure and broadest implementation leverage.

### C2 — Strategic transition

`DESIRE AGE/TECH → PROTECT RESOURCES → CHECK FEASIBILITY → RESEARCH → VERIFY NEW CAPABILITY → REALLOCATE`

### C3 — Military lifecycle

`CAPABILITY → ATTACK COMMITMENT → ENGAGE → ASSESS → RETREAT/CONTINUE → REGROUP → RESTART/ABANDON`

### C4 — Information → action

`INFORMATION GAP → SCOUT CANDIDATES → SAFETY/UTILITY EVALUATION → MOVE → OBSERVE → UPDATE BELIEF`

---

# Evidence discipline

Evidence grades used throughout Layer 2:

- **DIRECT** — executable source or explicit source statement establishes the relationship.
- **COMPOSED** — multiple DIRECT relationships form the larger relationship.
- **INFERRED** — strategic meaning reconstructed from repeated behavior/context.
- **AEGIS-GENERALIZATION** — new design derived from historical evidence.
- **UNCERTAIN** — evidence is insufficient.

Closure levels are independent:

- **CONTROL** — state reaches a command/control consequence.
- **WORLD** — resulting game-state change is independently observed/proven.
- **STRATEGIC** — intended game relationship improves and is demonstrated.

The distinction matters. The HD source provides a meaningful strategic controller and is a capable player, but source archaeology alone cannot turn every command into a demonstrated world-state or match-outcome claim.

Never promote a claim because it sounds strategically sensible. Trace the edge.

Canonical research unit:

`OBSERVATION → CLASSIFICATION → STATE WRITE → AUTHORITY EFFECT → RESOURCE / PRODUCTION CONSEQUENCE → TEMPORAL GUARD → REASSESSMENT`

---

# Historical strategic discoveries

### Threat → camel response

`threats.per` measures cavalry/cavalry-archer-related enemy pressure into reusable aggregates. `units.per` consumes those states through `traincamel` conditions, stable search, `can-train` guards, and camel production actions.

This demonstrates a context-sensitive counter-capability architecture. Do **not** overstate it as a universal counter-composition optimizer.

### Escrow → age/technology transition

`escrow.per` uses escrow flags and `can-research-with-escrow` before issuing age research, while strategic age state is updated for downstream controller use.

The strategic interpretation is that the programmer understood resource protection around capability transitions. `research` remains a command, and `sn-current-age` remains controller state unless separately verified as world state.

### Attack → retreat → restart

HD contains distinct `attack-goal`, `attack-status-goal`, `retreat-now-goal`, timers, and `restart-attack-goal` behavior. Fortification/threat conditions can suppress or redirect pressure. This is a real lifecycle controller, not a single attack Boolean.

### 504/505 geometry

`general.per` initializes a comparison sentinel and preserves the candidate pair when the measured distance is greater than the prior best. The recovered algorithm therefore selects the **maximum-distance pair**, then derives a midpoint/centerward movement point. The precise strategic purpose remains open.

### Scout control

`scoutcontrol.per` uses candidate paths, quarterstep safety analysis, pivot geometry, interpolation, and waypoint/action machinery. The exact information-value objective is not fully proven, but the operational sophistication is direct evidence that scouting was treated as a constrained movement problem rather than random exploration.

### Resource allocation

`gatherers.per`, escrow, production, technology, and strategic state form a distributed resource-control network. The strongest defensible lesson is contextual allocation toward capability requirements, not a proven universal optimizer.

---

# Replay / state reconstruction

The project investigated raw replay parsing, richer replay models, playback implementations, and CaptureAge.

Reference replay:

- Raw `body.bin` SHA-256: `4269461f0cd488ae034f0371e7ef4a083d7f28bd60ae1054f1510e7daa519f3d`
- Normalized JSONL SHA-256: `3a5ceff2654d86155407dfe98acbab37c3c8432121228d5d0a5959b68c78b9f3`
- Parsed operations: **597,681**
- ACTION: **6,858**
- SYNC: **295,407**
- VIEWLOCK: **295,407**
- CHAT: **8**
- POSTGAME: **1**
- Unknown/fallback operation IDs in reference body: **0**

The minimal deterministic replay interpreter is:

`05_RUNTIME_CANDIDATE/minimal_replay_interpreter_pass23.py`

It deliberately distinguishes:

`DIRECT_REPLAY | PARSED_SNAPSHOT | DERIVED | HEURISTIC | UNKNOWN`

and does not promote `DE_QUEUE`, `BUILD`, `RESEARCH`, or `DELETE` commands into completed world transitions without evidence.

Current closure remains:

`W0 CLOSED | W1 OPEN | W2 OPEN | W3 OPEN`

### CaptureAge status

Installed CaptureAge version investigated: **1.25.0**.

Native module:

`C:\Users\justh\AppData\Local\Programs\CaptureAge\cade.node`

SHA-256:
`C64832B06229D445B4E735BB1A768100B044B64A6A74A32C45710853725BCC61`

The installed CADE runtime exposes rich state vocabulary including `GameState`, `Entity`, `BuildingEntity`, `ProductionQueueRecord`, `Technology`, `ResearchState`, and lifecycle event names such as villager/combat-unit creation, technology researched, age-up, attack, victory, and defeat.

Pass 32 established the bootstrap topology:

`Electron main/bootstrap → cade.node → native CADE → named pipe / IPC → renderer`

The installed application logs also demonstrate replay loading and patch/world-time activity. What remains unresolved is a clean, supported external replay→lifecycle extraction contract. Therefore CADE is retained as a **future validation adapter candidate**, not as a core dependency.

---

# Engineering tools and working environment

The project has used the following practical toolchain:

- **GitHub** — canonical source control, commits, branches, PRs, review, provenance.
- **Remote Desktop Commander** — authorized Windows workstation inspection, filesystem access, process execution, local searches, runtime experiments, and artifact creation.
- **AoE2DE** — target runtime and manual validation environment.
- **mgz-fast / aoc-mgz** — replay parsing and normalization.
- **CaptureAge / CADE** — optional rich playback/state validation candidate.
- **Python** — deterministic replay interpretation, data processing, hashing, and analysis.
- **PowerShell** — Windows runtime inspection and file/process automation.
- **Git** — local reproducibility and repository-wide integrity checks.
- **GitHub API/connector** — remote repository inspection and controlled writes.

Known local reference locations used during investigation include:

`C:\Users\justh\Desktop\AEGIS-AI-LAB\06_REPLAYS\08_FORENSIC_RUNS\2026-09-02_REFERENCE\body.bin`

`C:\Users\justh\Games\Age of Empires 2 DE\76561198093432383\savegame\mgz-fast-master\mgz-fast-master\mgz\fast\__init__.py`

These are workstation-specific evidence locations, not repository-relative dependencies.

---

# Repository navigation

Start here:

1. `README.md` — this orientation and current state.
2. `docs/PROJECT_HANDOFF_2026-09-04.md` — full six-month recovery handoff.
3. `docs/QC_FULL_REPOSITORY_2026-09-04.md` — repository-wide integrity/QC record.
4. `RESEARCH_INDEX.md` — detailed navigation map.
5. `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md` — Layer-1 boundary.
6. `docs/QC_THREE_PASS_2026-09-03_PASS1_REPOSITORY_INTEGRITY.md`
7. `docs/QC_THREE_PASS_2026-09-03_PASS2_EXTERNAL_CROSS_REFERENCE.md`
8. `docs/QC_THREE_PASS_2026-09-03_PASS3_PROMOTION_AND_ACTION_PLAN.md`
9. `03_HD_ARCHAEOLOGY/` — historical AI/programmer archaeology.
10. `03_HD_ARCHAEOLOGY/AOE2DE_PRACTICAL_CODING_KNOWLEDGE_BASE.md` — problem-first engineering catalogue.
11. `03_HD_ARCHAEOLOGY/AOE2DE_STRATEGIC_PROBLEM_MATRIX.md` — compact strategic lookup.
12. `03_HD_ARCHAEOLOGY/PASS35_HD_EVIDENCE_EDGE_LEDGER_AUDIT_2026-09-04.md` — latest causal provenance audit.
13. `05_RUNTIME_CANDIDATE/` — runtime candidate/interpreter work.
14. `knowledge/` — atomic institutional memory.
15. `12_RESEARCH/` — supporting research and provenance.

---

# Next engineering direction

The next priority is **not** another broad archaeology pass.

The next priority is to formalize C1 — Threat → Capability — into a testable AEGIS transition specification.

Required objects:

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

The implementation should be capable of answering:

> What does the bot believe is happening, why does it care, what capability does it require, what alternatives can satisfy that requirement, what will each alternative cost, what does it commit, what authorizes execution, how does it verify success, and what does it do when reality disagrees with the plan?

That is the bridge from **understanding HD** to **building AEGIS**.

---

# Six-month recovery rule

A future engineer or AI must be able to resume this project without relying on conversational memory.

Read the root README, then `docs/PROJECT_HANDOFF_2026-09-04.md`, then the full-repository QC, then the Layer-1 handoff, then the Layer-2 archaeology index and latest evidence-edge ledger.

Do not assume that a long document is correct merely because it is long. Follow provenance. Preserve failed experiments. Maintain evidence grades. Distinguish historical fact from AEGIS design. Keep current-runtime authority separate from historical archaeology.

**The project is not finished. It is now substantially better defined. The next AI should know exactly where we stopped, why we stopped there, what we believe, what remains uncertain, what tools exist, and what should be built next.**
