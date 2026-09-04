# Layer 2 — HD / Promisory Evidence-Edge Ledger — QC Pass 1

**Date:** 2026-09-04  
**Target:** `HD_EVIDENCE_EDGE_LEDGER_PASS7_2026-09-04.md`  
**Status:** FORENSIC QC / ACCEPT WITH CORRECTIONS  
**Primary evidence boundary:** verified `AI (HD version).per` + verified Promisory source  
**Runtime authority:** frozen Layer-1 machine evidence

---

## 0. Verdict

**ACCEPT WITH CORRECTIONS.**

Pass 7 is materially stronger than Pass 6 because it audits causal edges instead of allowing a transition label to carry unsupported meaning. It correctly introduces evidence grade, alternative explanation, falsifier, and AEGIS status.

However, the ledger is not yet a forensic-grade provenance database. Several records still use approximate source locations where exact anchors are required, some `DIRECT` classifications are stronger than the stated provenance supports, and several falsifiers are phrased as hypothetical experiments rather than source-level falsification tests. A few edges also conflate a **state write**, a **reader relationship**, and a **game-world consequence**.

The artifact should therefore be retained as a working ledger, but **no historical edge should be promoted to canonical doctrine until the corrections below are applied.**

---

# 1. Major findings

## QC7-01 — Approximate source locations are too weak for a provenance ledger

**Severity:** HIGH  
**Affected:** ST-01 through ST-08, especially attack, fortification, role, and food transitions.

The ledger explicitly says `TBD` is preferable to fabricated precision, which is correct. But a provenance ledger whose purpose is to prove edges should distinguish:

- exact source line/rule;
- approximate prior-extraction anchor;
- module-level evidence;
- no anchor.

Current records sometimes label an edge `DIRECT` while its location is only approximate.

**Required correction:** add `Anchor quality` with values `EXACT / APPROXIMATE / MODULE-ONLY / NONE`. `DIRECT + APPROXIMATE` may remain provisional but must not be treated as canonical proof.

**Falsifier:** an exact-source audit cannot recover the claimed relationship at the cited anchor.

---

## QC7-02 — `DIRECT` must mean the complete edge is executable-source-observable

Several rows correctly identify direct facts but still phrase the edge at a higher semantic level than the source demonstrates.

Examples:

- `escrow state → research authorization` can be DIRECT if the exact rule guard/action is anchored.
- `enemy state → threat classification` can be DIRECT only when the classification write and its guard are anchored.
- `retreat → attack timer/reset lifecycle` can be DIRECT for controller-state writes, but not for the strategic concept “regroup.”

**Required correction:** split each direct edge into:

`source observation → state write → state reader/effect`

and reserve strategic consequences for COMPOSED or INFERRED.

---

## QC7-03 — The ledger still occasionally treats a goal as a belief

A goal/SN may represent state, intent, requirement, classification, scratch data, or an execution control flag. The source does not automatically establish the epistemic category.

This matters particularly for:

- threat classifications;
- `position-goal`;
- `enemy-fortifications-goal`;
- `retreat-now-goal`;
- `restart-attack-goal`.

**Required correction:** add a `State ontology` column:

`OBSERVATION / CLASSIFICATION / BELIEF / REQUIREMENT / COMMITMENT / AUTHORITY / ACTION-STATE / SCRATCH / UNKNOWN`.

Only call something a belief when persistence and downstream epistemic use are demonstrated.

---

## QC7-04 — Falsifiers need to target the claimed edge, not merely the surrounding system

Some falsifiers currently say things like “inspect action path,” “trace timer reader,” or “observe outcome.” Those are verification tasks, not falsifiers.

A true falsifier should state what observation would make the claimed relationship false.

Example:

> Claim: fortification state suppresses attack authorization.
>
> Falsifier: identify an executable path where the fortification state is active, the same relevant guards remain satisfied, and attack authorization is granted without any intervening state change.

**Required correction:** rewrite falsifiers as explicit counterexamples to the edge.

---

## QC7-05 — Alternative explanations need causal competitors

The ledger's alternatives are useful, but some are too generic:

> “allocation may serve another objective.”

That does not distinguish competing explanations.

**Required correction:** classify alternatives as:

- `REACTIVE`: response to immediate resource deficit;
- `STRATEGIC`: explicit long-horizon objective;
- `OPERATIONAL`: infrastructure/production constraint;
- `TACTICAL`: immediate combat response;
- `BOOKKEEPING`: state synchronization only;
- `COINCIDENTAL`: two rules triggered by the same fact.

Then state the specific competing explanation.

---

## QC7-06 — Source directionality must be established before calling an edge causal

A shared condition does not prove `A → B`.

For example, a resource state and an age state can both be read by a rule without resource state being the strategic cause of aging.

**Required correction:** add `Edge mechanism`:

`WRITE / READ / GUARD / ACTION / SIDE-EFFECT / SHARED-TRIGGER / TEMPORAL / SEARCH / UNKNOWN`.

`SHARED-TRIGGER` must not be promoted to causal evidence.

---

## QC7-07 — The ledger needs writer/reader ownership

The prior architecture work established that state ownership is a major unresolved issue. Pass 7 should now make that explicit.

For each state-bearing node, record:

`Writer rule(s) | Reader rule(s) | Reset/clear rule(s) | Authority effect | Lifecycle owner`.

Without this, a transition such as `retreat → restart` can appear coherent even when several unrelated rules write/read the same goal.

**Required correction:** add a state ownership appendix or columns rather than relying on narrative conclusions.

---

## QC7-08 — `ST04-E03` is potentially over-graded

`enemy state → threat classification` is marked DIRECT, but the ledger itself says the branches are distributed and exact class anchors remain required.

That is internally inconsistent.

**Disposition:** downgrade to `DIRECT-PROVISIONAL` or `VERIFY` until at least one representative threat class is anchored from guard → classification write → downstream reader.

Do not generalize one cavalry/gunpowder/infantry branch into the entire threat ontology without coverage evidence.

---

## QC7-09 — `ST05-E04` demonstrates a semantic ambiguity around restart

`restart-attack-goal` is correctly marked DIRECT as a state-level artifact, but “restart eligibility” is a semantic interpretation.

The source history already indicates restart can be associated with infrastructure/building-placement recovery. Therefore the label must not imply combat regroup universally.

**Required correction:** split:

`restart-attack-goal write → restart control state` = DIRECT.

`restart control state → combat regroup/relaunch` = VERIFY/INFERRED unless the same objective and causal path are proven.

---

## QC7-10 — `ST06-E02` should distinguish suppression from delay

`enemy-fortifications-goal` may cause attack logic to delay, alter, or suppress an attack. The current row calls this “attack delay/suppression,” which still compresses alternatives.

**Required correction:** identify the exact action/control effect. If the rule merely blocks a condition until a timer or siege condition changes, record `DEFER`. Use `SUPPRESS` only when the attack authorization is explicitly negated/cleared.

---

## QC7-11 — `ST07` risks overgeneralizing one role branch into map ontology

The direct evidence that `position-goal` changes `strategy-goal`, `unit-goal`, and `control-goal` is strong. The stronger claim that this constitutes a general relational map ontology is still INFERRED.

The ledger correctly marks that interpretation as inferred, but the evidence plan should enumerate the position values actually covered.

**Required correction:** add coverage:

`position value | writer | downstream goals | downstream actions`.

Do not call the ontology general until more than one role/path demonstrates it.

---

## QC7-12 — `ST08-E01` is not enough to establish depletion-driven substitution

Boar/hunting assignment is direct evidence for hunting behavior. It does not establish:

`finite food exhaustion → farms`.

The ledger correctly marks the farm edge COMPOSED, but the first edge risks being read as the first half of that causal chain.

**Required correction:** separate:

1. hunting procedure;
2. finite-source state;
3. food-demand projection;
4. farm authorization;
5. farm placement/production;
6. transition completion.

Only connect these if the source actually provides the relevant dependency.

---

## QC7-13 — Strategic consequence rows need explicit game-level variables

Rows such as:

- “new strategic capability”;
- “superior capability set”;
- “changed capability relationship”;
- “changed objective conversion efficiency”

are valuable AEGIS concepts, but they are not yet observable source variables.

**Required correction:** when retaining them, define the measurable game variable that instantiates them:

`production availability, military mass, technology availability, map access, resource throughput, attack progress, villager survival, infrastructure capacity, timing delta`, etc.

Otherwise retain them as AEGIS design vocabulary, not historical evidence.

---

## QC7-14 — Need distinction between historical response and AEGIS candidate space

The ledger correctly rejects a unified candidate tournament as historical fact. The same discipline must apply to all candidate lists.

Each candidate should carry:

`HISTORICAL-OBSERVED / HISTORICAL-POSSIBLE / AEGIS-PROPOSED`.

A historical AI's distributed rule network must not be retroactively represented as if it ran an explicit candidate optimizer.

---

## QC7-15 — Add temporal semantics to every transition edge

AoE2 control logic is heavily timer- and pending-state-driven. An edge without temporal semantics can be technically true but strategically misleading.

**Required fields:**

`Temporal mode = IMMEDIATE / DELAYED / COOLDOWN / PERSISTENT / ONE-SHOT / UNTIL-CLEARED / UNKNOWN`.

Also record the relevant timer/pending state where known.

This is especially important for ST-05 and ST-06.

---

## QC7-16 — Add performance economics to search-derived edges

Search and geometry machinery is not just tactical cleverness; it is computationally budgeted behavior. Existing source comments explicitly discuss performance impact and rule-budget optimization.

For `SEARCH` edges, record:

`Search scope | reset requirement | candidate count | iteration mechanism | rule-budget cost | early-exit condition`.

This turns the programmer's implementation constraint into part of the reconstructed engineering knowledge.

---

## QC7-17 — Add commitment-break conditions

The transition model already identified commitment and revocation as important. Pass 7 should make them provenance-visible.

For every edge that leads toward an irreversible or costly action, record:

`Commitment introduced? | Commitment owner | Break condition | Revocation mechanism | Replacement commitment`.

This is especially relevant to age research, production, siege, attacks, and fortifications.

---

## QC7-18 — Add conservation-law checks

A strategic edge should be tested against the quantities it consumes or changes:

- resources;
- villager time;
- production capacity;
- military mass;
- map access;
- information quality;
- timing;
- optionality.

**Required correction:** add a conservation/impact appendix. This does not claim the historical programmer explicitly used conservation equations; it provides an audit for AEGIS reconstruction.

---

## QC7-19 — Add local / operational / strategic postconditions

The prior QC required this distinction, but Pass 7 only partially implements it.

Every causal chain that ends in an action should distinguish:

1. **Command/control postcondition** — goal/action/timer changed.
2. **World-state postcondition** — units/buildings/resources actually changed.
3. **Operational postcondition** — intended local capability exists.
4. **Strategic postcondition** — game objective improved.

Do not infer levels 2–4 from level 1.

---

## QC7-20 — Add confidence and evidence coverage metrics

The ledger has evidence grades but no quantitative coverage.

Add:

- number of edges by grade;
- number with exact anchors;
- number with world-state evidence;
- number with explicit falsifier;
- number with identified writer/reader;
- number with temporal semantics;
- number safe for inheritance;
- number design-only.

This makes future passes measurable instead of rhetorical.

---

# 2. Transition-specific disposition

| Transition | QC disposition | Canonical historical status |
|---|---|---|
| ST-01 Dark → Feudal | Corrections required | COMPOSED / VERIFY |
| ST-02 Feudal → Castle | Corrections required | COMPOSED / INFERRED components |
| ST-03 Castle → Imperial | Strongest transition | DIRECT authorization; strategic timing separate |
| ST-04 Composition → counter | Corrections required | DIRECT threat components; COMPOSED response |
| ST-05 Attack → retreat → restart | Corrections required | DIRECT controller-state loop; world-state consequence unproven |
| ST-06 Fortification → siege | Corrections required | DIRECT fortification-aware control; siege edge COMPOSED |
| ST-07 Map role → posture | Mostly accepted | DIRECT role-to-goal coupling; ontology INFERRED |
| ST-08 Food depletion → renewable food | Corrections required | hunting DIRECT; depletion substitution VERIFY |

---

# 3. Required Pass-7 revision contract

Before Pass 7 can be considered closed, revise the ledger schema to:

`Edge ID | Transition | From | To | State ontology | Source module | Exact anchor | Anchor quality | Evidence type | Evidence grade | Edge mechanism | Writer | Reader | Temporal semantics | Alternative explanation | Falsifier | Commitment effect | Postcondition level | AEGIS status`

And add appendices for:

1. **State ownership matrix**
2. **Exact-anchor coverage matrix**
3. **Falsifier register**
4. **Transition conservation/impact register**
5. **Historical vs AEGIS candidate register**
6. **Search/performance register**
7. **Evidence coverage metrics**

---

# 4. Final QC judgment

**ACCEPT WITH CORRECTIONS — DO NOT PROMOTE TO CANONICAL EVIDENCE YET.**

Pass 7 successfully changes the investigation from “does this transition make sense?” to the much more valuable question:

> **“Can we prove this particular causal edge, exactly where it lives, what mechanism creates it, what alternative explanation competes with it, and what observation would falsify it?”**

That is the correct forensic direction.

The next pass should therefore be **Pass 8 — Exact-Anchor + Edge-Mechanism Audit**, not another broad strategic synthesis.

Its job is to convert the working ledger into an evidence database by replacing approximate anchors with exact rules wherever possible, proving writer→reader directionality, separating state ontology from strategic interpretation, and constructing actual falsifiers for the highest-value edges.
