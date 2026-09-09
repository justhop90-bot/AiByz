# AEGIS / AiByz — Final Reconstruction Audit

**Date:** 2026-09-09
**Status:** canonical unresolved-proof register
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`
**Purpose:** Reconcile the accumulated GitHub research, eliminate duplicated/obsolete interpretation, and define the definitive set of machine/semantic claims that still require proof before production `.per` implementation.

---

## 0. Audit conclusion

The repository is substantially farther along than a casual reading of the directory tree suggests.

The broad discovery phase is complete enough that another general-purpose HD archaeology pass would mostly duplicate existing work. The repository already contains:

- canonical project governance and handoff material;
- extensive Layer-2 historical strategy archaeology;
- Pass 9–13 causal/control/world-state reconstruction;
- a stock subsystem reconstruction map;
- stock runtime import-closure findings;
- a substantial ABI inventory;
- construction OS forensic and runtime ABI work;
- replay parsing/indexing infrastructure and calibration evidence;
- explicit evidence-level and lifecycle boundaries;
- a defined AEGIS architecture and first executable vertical slice.

**The remaining frontier is qualification and reconciliation.**

The purpose of this audit is therefore not to invent another architecture. It is to identify the exact unresolved cells between the existing model and a machine-qualified AEGIS implementation.

---

# 1. Authority hierarchy

When documents disagree, apply this order:

1. Exact target-build evidence from the untouched installed package/executable.
2. Verified repository snapshot of that exact package.
3. Current canonical project documents and P0 reconstruction artifacts.
4. Recent forensic/qualification passes.
5. Historical HD/Promisory source archaeology.
6. Experiments and candidate implementations.
7. Inference/generalization.

Historical and experimental material is retained because it explains the investigation. Retention does not make it current authority.

---

# 2. Project state after reconciliation

| Area | Current disposition | Audit judgment |
|---|---|---|
| Mission/scope | stable | CLOSED |
| Target build identity | recorded | CLOSED, re-fingerprint before new runtime claims |
| Layer 1 broad archaeology | frozen at 89% | CLOSED for broad discovery |
| Layer 2 historical strategy archaeology | major reconstruction closed | CLOSED for broad discovery |
| Layer 3A architecture | five-pass architecture closed | CLOSED for design; qualification remains |
| Stock subsystem map | present | SUBSTANTIALLY CLOSED |
| Stock runtime import closure | mapped at high level | PARTIALLY CLOSED |
| Conditional compilation effective set | not fully machine-joined | OPEN |
| Fact/class/foundation ABI inventory | strong | SUBSTANTIALLY CLOSED |
| ObjectData ABI inventory | strong | SUBSTANTIALLY CLOSED |
| Numeric AEGIS allocation | candidates exist, not cleared | OPEN |
| GOAL/SN/FLAG/TIMER ownership | evidence exists across many files | OPEN as a complete authoritative matrix |
| Writer/reader/resetter/lifetime matrix | partial across research | OPEN as a unified ledger |
| Construction semantics | heavily investigated | PARTIALLY CLOSED; runtime lifecycle still matters |
| Civilian production semantics | strong historical/control evidence | PARTIALLY CLOSED |
| Economy/escrow semantics | strong historical/control evidence | PARTIALLY CLOSED |
| Research completion semantics | control evidence stronger than world proof | OPEN |
| Unit production completion semantics | control evidence stronger than world proof | OPEN |
| Threat/camel chain | control path strongly reconstructed | OPEN at world/strategic realization |
| Attack/retreat/restart | control path strongly reconstructed | OPEN at world/strategic realization |
| Scouting/information | architecture and historical evidence strong | PARTIALLY CLOSED |
| TSA military execution | identified as major service | OPEN for complete ownership/semantic closure |
| Water/trade/boar/interaction/general/init/orb/resign | identified and partially mapped | OPEN/targeted |
| Replay command stream | real calibrated evidence | CLOSED as an indexer boundary |
| Replay lifecycle completion | not proven by command alone | OPEN |
| Strategic effect | limited direct proof | OPEN |
| Production AEGIS `.per` | intentionally blocked | BLOCKED until required gates close |

---

# 3. What has already been established — do not rediscover unless a dependency requires it

## 3.1 Stock provenance model

The stock system must be understood through three layers:

1. `AI (HD version).per` — flattened behavioral controller.
2. Promisory source corpus — reconstruction/provenance material.
3. Active runtime substrate — the target stock load closure, chiefly `defaultConstants`, `finalingConstants`, and conditional `finaling`, plus only proven nested imports where applicable.

A file existing under `Promisory` is not proof that the normal flattened runtime loads it.

## 3.2 Historical control model

The recovered historical pattern is:

`OBSERVE → CLASSIFY → STATE WRITE → AUTHORITY EFFECT → RESOURCE/PRODUCTION CONSEQUENCE → TIMER/RESET → REASSESS`

The more complete AEGIS reconstruction is:

`WORLD → OBSERVE → CLASSIFY/BELIEVE → TRANSITION → OBJECTIVE → REQUIREMENTS → CONSTRAINTS → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → FAILURE/SUCCESS → UPDATE BELIEFS → REASSESS`

## 3.3 Vertical evidence boundaries

The repository already distinguishes:

- control closure;
- world-state closure;
- operational capability closure;
- strategic closure.

Do not collapse them.

## 3.4 Replay boundary

The replay indexer intentionally establishes command/synchronization evidence without inventing accepted, queued, created, available, or effective state.

This conservative boundary is correct and must be preserved.

---

# 4. Definitive unresolved-proof register

The following are the remaining proof obligations. They are deliberately phrased as falsifiable engineering questions rather than broad research topics.

## R1 — Effective stock load/conditional compilation closure

**Question:** What exact rule/symbol set exists in the effective stock program for the target build after all relevant preprocessing/conditional branches are resolved?

**Already known:** the principal stock closure is `AI (HD version).per` plus `defaultConstants`, `finalingConstants`, and conditional `finaling`; important nested imports have been identified.

**Still unproven:** a machine-readable effective rule/load graph including conditional branches, symbol availability, duplicate/redefinition behavior, and load-order effects.

**Minimum closure evidence:** deterministic parser/preprocessor reconstruction against the exact stock package, with every active load and conditional branch recorded.

**Do not solve by:** assuming all Promisory files are active or treating commented historical loaders as runtime dependencies.

**Status:** OPEN.

---

## R2 — Complete mutable state ownership matrix

**Question:** For every AEGIS-relevant mutable channel, who declares it, initializes it, writes it, reads it, resets it, and owns its semantic lifetime?

**Required channels:** GOAL, SN, FLAG, TIMER, GROUP, escrow state, temporary scratch state, and relevant object/search state.

**Still unproven:** one authoritative deduplicated ledger covering the complete relevant stock state surface.

**Minimum closure evidence:** symbol-level inventory with:

`channel → symbol → declaration → initializer → writers → readers → guards → resetters → lifetime → owner → authority effect → downstream consumers → evidence grade`.

**Status:** OPEN.

---

## R3 — Semantic typing of numeric channels

**Question:** Which numeric values are safe for which exact operations, and which apparent gaps are unsafe because of typed reuse, engine interpretation, or hidden consumers?

**Known:** numeric equality is not semantic identity; candidate AEGIS scalar block `10000–10015` is not cleared.

**Still unproven:** complete allocation proof for each intended AEGIS-owned numeric channel.

**Minimum closure evidence:** stock typed census + all intended AEGIS operations + collision/semantic validation + target-build runtime/validator qualification where necessary.

**Status:** OPEN / ABI GATE.

---

## R4 — Conditional/state initialization semantics

**Question:** When and under what conditions do important state channels acquire their first meaningful values?

**Why it matters:** declaration, default value, and active runtime initialization are not interchangeable.

**Minimum closure evidence:** effective rule graph plus controlled runtime observation for channels whose initialization semantics cannot be proven statically.

**Status:** OPEN.

---

## R5 — Command lifecycle: issued → accepted/queued → pending → created → available → effective

**Question:** What observable evidence distinguishes each lifecycle stage for the target build?

**Known:** replay ACTION records establish command issuance only.

**Still unproven:** reliable target-build markers for selected BUILD, DE_QUEUE, RESEARCH, TRAIN, MOVE/ORDER and related operations.

**Minimum closure evidence:** a bounded retail-safe experiment for each lifecycle family, with immutable input, command timestamp, independent world observation, and explicit falsifiers.

**Status:** OPEN and central.

---

## R6 — Construction lifecycle realization

**Question:** What exact sequence proves that a construction request becomes a foundation, gains builder assignment, progresses, completes, fails, or is abandoned?

**Known:** construction OS and ABI boundaries have been deeply investigated.

**Still unproven:** complete runtime mapping from controller-side state to world-side completion/failure for the target build.

**Minimum closure evidence:** controlled single-building lifecycle with independent observation of foundation/object identity/progress/completion and failure cases.

**Status:** PARTIALLY CLOSED → OPEN runtime boundary.

---

## R7 — Civilian production realization

**Question:** What exact evidence proves a `trainvillager`/`up-train` path has created the intended worker and made it available to the civilian state model?

**Known:** historical authorization, escrow, production-site search, pending-state and worker-allocation relationships are strongly reconstructed.

**Still unproven:** target-build completion and reconciliation semantics.

**Minimum closure evidence:** isolated TC production experiment with pre/post population, pending production, object identity where observable, and worker census.

**Status:** OPEN.

---

## R8 — Research realization

**Question:** What exact runtime observation proves a research command was accepted, completed, and made its capability available?

**Known:** historical reservation/escrow and `can-research-with-escrow` control chains.

**Still unproven:** world-state completion semantics and reliable postcondition observation for selected technologies.

**Minimum closure evidence:** controlled research experiment with precondition, issue, pending state, completion marker, and capability postcondition.

**Status:** OPEN.

---

## R9 — Threat aggregate semantic calibration

**Question:** What precisely does a stock threat aggregate such as `cavarchers` mean at runtime: count, weighted count, transformed strength, or a context-specific score?

**Known:** source-level writers/readers and threshold consumers are reconstructed.

**Still unproven:** complete semantic calibration against actual world composition in the target build.

**Minimum closure evidence:** controlled enemy-composition cases with known unit populations and observed state outputs.

**Status:** OPEN.

---

## R10 — Cavalry-threat → camel capability realization

**Question:** Does the reconstructed threat/camel control chain reliably produce the intended camel capability under target runtime conditions?

**Known:** control path reaches `traincamel`, stable search, `can-train`, and train command.

**Still unproven:** production completion, surviving camel stock, usable capability, and strategic containment effect.

**Minimum closure evidence:** vertical experiment closing W0→W3 at minimum; W4 requires combat/strategic evidence and is not mandatory for initial ABI clearance.

**Status:** OPEN.

---

## R11 — Attack/retreat/restart world realization

**Question:** Do attack/retreat/restart state transitions produce the intended physical group behavior and recovery outcome in the target build?

**Known:** historical control state, retreat triggers, restart goals, timers and group resets are strongly reconstructed.

**Still unproven:** physical movement/formation/engagement consequences and robust recovery success.

**Minimum closure evidence:** controlled attack-threat experiment with independent unit/world observation.

**Status:** OPEN.

---

## R12 — Land-nomad/farthest-pair geometric realization

**Question:** Does the `general.per` 504/505 algorithm result in the intended physical relocation and strategic effect?

**Known:** candidate selection, midpoint, centerward displacement and move command are source-visible.

**Still unproven:** exact scratch-index semantics, physical movement completion, and strategic purpose.

**Minimum closure evidence:** controlled geometry experiment with known candidate units and post-move coordinates.

**Status:** OPEN / lower priority unless required by implementation.

---

## R13 — Scouting/information semantic closure

**Question:** Which scout-control state is authoritative for discovery, threat/path analysis, reinforcement, retreat and retargeting, and what survives across rule passes?

**Known:** scouting is an information-processing subsystem with geometry, path analysis, enemy strength estimates, timers and groups.

**Still unproven:** complete state ownership and runtime semantic closure across all relevant scout state.

**Minimum closure evidence:** state matrix plus targeted runtime observation for unresolved transitions.

**Status:** PARTIALLY CLOSED.

---

## R14 — TSA military service ownership/semantics

**Question:** What is the complete ownership and transition model for military task scheduling, target selection, group state, micro-system selection, reinforcement and retreat?

**Known:** multiple interacting military state machines exist; architecture recognizes TSA as a major service.

**Still unproven:** complete symbol-level ownership and runtime closure.

**Minimum closure evidence:** focused TSA reconstruction matrix followed by only the runtime probes required to resolve semantic unknowns.

**Status:** OPEN.

---

## R15 — Undercovered stock service closure

The following services have been identified but do not yet have the same proof depth as economy/escrow/threat/civilian/construction work:

- `researches.per`
- `tsa.per`
- `scoutcontrol.per`
- `trade.per`
- `watercontrol.per`
- `boarhunting.per`
- `interaction.per`
- `general.per`
- `init.per`
- `orb.per`
- `resign.per`

**Rule:** do not reopen all of them broadly. Only reconstruct enough of each to close an AEGIS dependency or prove that it is outside the first implementation boundary.

**Status:** OPEN, dependency-driven.

---

## R16 — Replay clock semantic calibration

**Question:** What exact unit/relationship do parsed replay clock fields represent relative to displayed game time and real execution time?

**Known:** the parser preserves exact emitted values and deliberately refuses to call them milliseconds.

**Still unproven:** semantic unit and reliable conversion.

**Minimum closure evidence:** controlled replay anchors tied to known game-time events.

**Status:** OPEN.

---

## R17 — Aggregate-to-individual object identity

**Question:** Can individual object lineage be established reliably across replay synchronization records?

**Known:** aggregate object counts/TTL fields exist but do not prove identity continuity.

**Still unproven:** robust object identity reconstruction.

**Minimum closure evidence:** replay cases with independently known object creation/deletion and stable identifiers, if the format exposes sufficient information.

**Status:** OPEN; only required where an implementation/verification feature depends on it.

---

## R18 — Strategic-effect qualification

**Question:** Which reconstructed behaviors demonstrably alter the intended strategic relationship rather than merely executing commands?

**Known:** many historical control paths are closed.

**Still unproven:** W4 strategic outcomes for most individual chains.

**Minimum closure evidence:** targeted scenario/replay/live evidence showing the intended operational capability changed the relevant game relationship.

**Important:** strategic-effect proof is not required for every ABI primitive before implementation. It is required before claiming that AEGIS reproduces or improves a strategic behavior.

**Status:** OPEN.

---

## R19 — Canonical-document consistency audit

**Question:** Are any older handoffs, passes, or implementation notes still making claims contradicted by the current canonical P0/reconstruction model?

**Known:** the repository intentionally preserves historical documents and failed designs.

**Still required:** explicit labels/indexing so an AI cannot mistake archived conclusions for current authority.

**Minimum closure evidence:** repository-wide terminology/status audit and canonical supersession table.

**Status:** OPEN, documentation gate.

---

# 5. Obsolete / rejected interpretations that must never be revived

The following are not current architecture:

- `ADprom` as a production architecture.
- `byzwarcouncil` as a production architecture.
- Any assumption that `V2_2`/`V3-4` experimental architecture is grandfathered into the final design.
- Broad scenario-loader automation as the primary runtime test strategy.
- XS-based implementation.
- Copying the stock flattened AI into AEGIS as the reconstruction method.
- Treating the entire Promisory directory as the stock runtime load graph.
- Treating embedded native test-harness symbols as proof of retail invocability.
- Treating AoE2Control/invasive runtime attachment as AEGIS core authority.
- Treating numeric vacancy as permission to allocate a channel.
- Treating commands, queue/dequeue events, BUILD, or RESEARCH as completion proof.

These items should remain documented as historical/negative evidence where useful, but they must be visibly marked obsolete/rejected rather than presented as live options.

---

# 6. Duplicate-research disposition

The project has accumulated multiple passes that sometimes approach the same subject from different evidence layers. That is useful for triangulation, but the next phase must stop generating parallel explanations.

Use this consolidation rule:

- **Historical strategy finding** → retain the strongest source-anchor document.
- **Causal chain** → retain the latest vertical/world-state closure artifact.
- **Machine substrate** → retain the P0 substrate/reconstruction map.
- **Runtime qualification** → retain the latest experiment/qualification artifact with immutable evidence.
- **Governance/status** → canonical handoff + this audit.
- **Old duplicate** → archive as historical evidence; do not cite it as current authority.

Do not create another document merely because an existing document already answers the question.

---

# 7. Definitive next engineering sequence

The shortest evidence-respecting path is:

```text
CURRENT GITHUB CORPUS
        ↓
CANONICAL CONSISTENCY / SUPERSESSION AUDIT
        ↓
EFFECTIVE LOAD + CONDITIONAL GRAPH
        ↓
COMPLETE RELEVANT STATE OWNERSHIP MATRIX
        ↓
ABI / NUMERIC ALLOCATION GATES
        ↓
TARGETED RUNTIME LIFECYCLE PROBES
        ↓
CAVALRY THREAT CONTAINMENT VERTICAL QUALIFICATION
        ↓
ABI FREEZE
        ↓
FIRST PRODUCTION .PER IMPLEMENTATION
```

The key optimization is **targeted qualification**. Do not attempt to close every historical subsystem to W4 before implementing anything. Close the machine semantics required by the first vertical slice, while maintaining the unresolved register for everything else.

---

# 8. Definition of “ready to implement”

Production `.per` implementation may begin only when all of the following are true for the first vertical slice:

1. Target package/build identity is freshly verified.
2. Required loads and conditional branches are resolved.
3. Required GOAL/SN/FLAG/TIMER channels have explicit ownership and collision disposition.
4. Required ABI operations have semantic evidence at the appropriate level.
5. Command lifecycle states needed by the slice are distinguished.
6. Required world postconditions have observable verification methods.
7. Recovery/re-arbitration behavior has an explicit state contract.
8. No unresolved assumption is hidden inside a “helper” primitive.
9. Static QC passes.
10. Runtime qualification passes for the bounded slice.

Only then should an implementation claim be made.

---

# 9. Final audit verdict

**The project is not missing another grand theory. It is missing a finite set of machine-proof closures.**

The GitHub corpus already contains most of the conceptual and historical machinery needed to understand the stock AI and design AEGIS. The remaining job is to turn that distributed knowledge into a single auditable machine model and close only the unresolved cells that matter to implementation.

The next AI should therefore begin here, not by rereading the entire repository from scratch and not by starting another broad archaeology campaign.

**Start with R1–R5. Then close only the vertical-slice dependencies.**

That is the current engineering frontier.
