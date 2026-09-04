# AoE2DE Historical Code-to-Strategy Implementation Lab — Deep QC Pass 1

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Target:** `AOE2DE_HISTORICAL_CODE_TO_STRATEGY_LAB_PASS9_2026-09-04.md`  
**Status:** DEEP QC / ACCEPT WITH CORRECTIONS  
**Primary evidence boundary:** verified `AI (HD version).per` + verified Promisory modules  
**Runtime boundary:** current DE execution semantics remain governed by frozen Layer-1 evidence  
**Method:** source archaeology + cross-artifact consistency audit + external semantic triangulation + implementation-readiness review

---

## 0. Executive verdict

**Pass 9 is strategically strong, directionally correct, and substantially better than Pass 8 as a bridge into implementation. It is not yet an evidence-grade “historical code-to-strategy implementation lab.”**

The central defect is decisive:

> **The artifact promises literal historical code traces, but the eight labs mostly provide source references, conceptual traces, and AEGIS pseudocode rather than the promised executable `.per` slices.**

This is not a cosmetic problem. It means the artifact currently teaches the reader **what to look for** and **how to interpret it**, but not yet reliably **how the actual historical code implements it**.

A second major issue is that several historical mechanisms are still described one semantic level above what the cited source proves. In particular:

- escrow is sometimes upgraded from a concrete mechanism to a generalized commitment doctrine;
- production flags are called authorization without consistently separating historical control state from the AEGIS authority plane;
- threat branches are treated as a classification system without a complete writer/reader trace;
- search machinery is called an optimization loop without an exact complete candidate lifecycle;
- scout path code is correctly recognized as sophisticated geometry, but the strategic “information acquisition” interpretation remains inference;
- attack/retreat/restart is correctly identified as stateful control, but physical movement and strategic preservation are not established by controller-state writes alone;
- building fallback is strong direct evidence for recovery engineering, but the broader recovery taxonomy is AEGIS design.

The artifact should therefore be **retained, not rejected**, but Pass 10 should now be treated as a required forensic extraction pass rather than an optional refinement.

### Overall disposition

**ACCEPT WITH CORRECTIONS — DO NOT PROMOTE AS CANONICAL IMPLEMENTATION MANUAL YET.**

---

# 1. Audit standard

Every historical lab should eventually prove the following chain:

`GAME PROBLEM → HISTORICAL SOURCE → EXACT CODE → RULE-BY-RULE EXECUTION → STATE WRITE → STATE READER → GUARD → SIDE EFFECT → RESET/RELEASE → POSTCONDITION → FAILURE/RECOVERY → STRATEGIC INTERPRETATION → AEGIS GENERALIZATION`

The historical and AEGIS layers must remain visibly separate.

### Evidence grades

- **DIRECT:** exact executable source demonstrates the stated relationship.
- **COMPOSED:** multiple DIRECT relationships form the larger relationship.
- **INFERRED:** strategic meaning reconstructed from repeated behavior/context.
- **AEGIS-GENERALIZATION:** new architecture derived from the historical pattern.
- **UNCERTAIN:** evidence insufficient.

### Anchor quality

Future traces must classify anchors as:

`EXACT | APPROXIMATE | MODULE-ONLY | NONE`.

A DIRECT claim with only an approximate/module-only anchor remains provisional.

---

# 2. Critical findings

## QC9-01 — The artifact does not yet satisfy its own “literal code” promise

**Severity: CRITICAL**

The Pass-9 objective says it will teach each mechanism from literal source code through strategic interpretation to AEGIS implementation. The actual labs mostly contain prose such as `can-research-with-escrow`, goal names, module names, and conceptual traces.

There is no complete historical code excerpt for each of the eight labs.

### Required correction

Each lab must contain a **bounded executable slice**, not merely a list of identifiers.

Minimum:

```text
SOURCE FILE
EXACT LINE RANGE
EXACT DEFCONST(S) REQUIRED
EXACT DEFRULE(S)
ALL GUARDS
ALL ACTIONS
IMMEDIATE WRITERS
IMMEDIATE READERS
RELEVANT RESET/RELEASE
```

Then explain the slice line by line.

**Disposition:** BLOCKS canonical promotion.

---

## QC9-02 — “Literal control trace” is currently conceptual, not literal

**Severity: CRITICAL**

Lab 1 calls its section a literal control trace but provides:

`escrow state → research feasibility → research command → strategic-age state update`.

That is a normalized semantic trace, not a literal execution trace.

### Required correction

Use two explicitly labeled traces:

**Historical literal trace**

`escrow-flag == 1 → can-research-with-escrow castle-age → research castle-age → set-strategic-number sn-current-age fcastlea`

**AEGIS normalized trace**

`reservation state → live feasibility → side effect → observed transition state`.

The first is source evidence; the second is interpretation/design.

---

## QC9-03 — Source anchors are still too weak for an implementation lab

**Severity: HIGH**

The document repeatedly names modules but does not provide exact line anchors in the lab body.

The verified source confirms, for example, that `escrow.per` contains the Castle and Imperial research blocks. The recovered source slice is exact enough to anchor them at the opening research rules; Pass 9 should have used that evidence directly rather than referring to a “recovered source index.”

### Required correction

Replace source-index prose with exact anchors wherever available. Preserve the source-index artifact as provenance, but make the actual source file the primary citation.

---

## QC9-04 — The source package used for forensic extraction must be named explicitly

**Severity: HIGH**

The project contains verified historical source, reconstructed ADPromisory packages, current AEGIS packages, and multiple revisions. Pass 9 says “verified Promisory modules” but does not identify the exact package/version used for every excerpt.

### Required correction

Every lab header should include:

`SOURCE PACKAGE | VERSION/REVISION | HASH IF AVAILABLE | MODULE | ANCHOR`

This prevents accidental mixing of historical and current AEGIS code.

---

# 3. Lab 1 — Escrowed Age Research

## QC9-05 — “Escrowed” is correct as a mechanism, but the strategic interpretation is one step too strong

**Severity: MEDIUM**

The source directly demonstrates an escrow flag gating `can-research-with-escrow`, followed by `research` and a strategic-number age-state update. This is strong direct evidence of escrow-mediated research control.

What it does **not** directly prove is the full AEGIS interpretation:

> resources are being consciously protected because the programmer is optimizing competing future capability claims.

That interpretation is strong and defensible, but it is COMPOSED/INFERRED.

### Required correction

Label the layers:

- `escrow flag + can-research-with-escrow → research`: DIRECT;
- `escrow protects a future conversion`: COMPOSED/PROBABLE;
- `resource opportunity-cost doctrine`: AEGIS-GENERALIZATION.

---

## QC9-06 — Castle and Imperial should not be presented as evidence for every age transition

**Severity: HIGH**

The exact recovered `escrow.per` block demonstrates Castle and Imperial research control. It does not establish that Dark→Feudal is implemented by the same exact rule path.

### Required correction

The lab should explicitly say:

> “Castle and Imperial are directly demonstrated here. Feudal requires its own age-specific trace.”

This carries forward the correction already established in the transition-table QC.

---

## QC9-07 — The age-state write is not completion verification

**Severity: HIGH**

`set-strategic-number sn-current-age ...` is a controller-side state mutation. It is not, by itself, proof that the engine has completed the age transition.

### Required correction

The trace must distinguish:

`research command → controller state update → pending/world state → completion evidence`.

If the historical program deliberately writes the expected state before actual completion, that is itself valuable archaeology and must be documented rather than silently treated as verification.

---

## QC9-08 — “Release/reset after conversion” needs the exact release rule

**Severity: MEDIUM**

Pass 9 states that reservations are released/reset after execution, but does not show the exact source path.

### Required correction

Show the actual release/reset rules and identify whether they are:

`NORMAL COMPLETION | FAILURE | TIMEOUT | MODE CHANGE | INITIALIZATION | OTHER`.

Do not assume every reset is a successful-completion release.

---

# 4. Lab 2 — Contextual Gatherer Allocation

## QC9-09 — `temporary-goal10 985795` is correctly interesting, but its semantic status needs a source trace

**Severity: HIGH**

The verified source contains the exact pattern:

`set-goal temporary-goal10 985795`

followed by rules guarded by:

`goal temporary-goal10 985795`

and then gatherer-percentage writes.

This establishes a regime selector/marker pattern. It does not by itself prove that the goal is merely scratch state.

### Required correction

Classify it as:

`GOAL STORAGE CHANNEL | REGIME SELECTOR / MODE MARKER | TEMPORAL LIFETIME TBD`

until its reset/replacement lifecycle is traced.

This is precisely the distinction between “temporary-looking” and proven scratch state.

---

## QC9-10 — “Feedback controller” is a valid synthesis but not a direct historical label

**Severity: MEDIUM**

The source visibly changes resource percentages in response to age, buildings, resource state, and strategic conditions. Calling the aggregate mechanism a feedback controller is a useful systems interpretation.

It is not literal source terminology.

### Required correction

`Historical mechanism: DIRECT`  
`Controller interpretation: COMPOSED/INFERRED`.

---

## QC9-11 — “Capability acquisition” should not be asserted for every gatherer rule

**Severity: MEDIUM**

Some gatherer rules are plainly contextual resource balancing. The document currently tends to interpret all such allocation as downstream of future capability demand.

### Required correction

For each representative rule, identify whether its immediate cause is:

`STRATEGIC OBJECTIVE | RESOURCE DEFICIT | AGE/TECH STATE | INFRASTRUCTURE | UNIT STATE | MAP CONDITION | OTHER`.

Only promote capability-demand interpretation where the dependency is demonstrated.

---

## QC9-12 — The actual gatherer percentages should be shown

**Severity: HIGH**

The source contains concrete percentage writes. Those numbers are precisely the kind of material a practical implementation lab should teach.

For example, the recovered regime includes 44% wood, 55% food, 1% gold, 0% stone, followed by context-specific 40/57/3/0 and later changes.

### Required correction

Show at least one complete percentage regime and explain:

`why these values fire | what changes them | who consumes the SNs | what later rules overwrite them`.

---

# 5. Lab 3 — Production Authorization

## QC9-13 — “Authorization” remains an AEGIS semantic interpretation

**Severity: HIGH**

The source clearly uses production flags, unit goals, strategic conditions, `can-train`, and `train` actions. That is strong evidence for production control/permission.

It does not establish a universal historical “authorization plane.”

### Required correction

Use:

`HISTORICAL: production control / permission state`

and:

`AEGIS: explicit production authority plane`.

Never collapse them.

---

## QC9-14 — Production is not just “desired capability → authorization”

**Severity: HIGH**

The historical source contains guards that include current unit counts, resource-control state, strategy/unit goals, age, technology, map conditions, and `can-train`.

Therefore a more faithful trace is:

`STRATEGIC/OPERATIONAL STATE → PRODUCTION CONDITION → LIVE FEASIBILITY → TRAIN`

The “authorization” interpretation should not hide the substantial context encoded in the guards.

### Required correction

Choose one concrete historical production rule and annotate every guard by category.

---

## QC9-15 — Production capacity is introduced but not historically traced

**Severity: MEDIUM**

Pass 9 correctly says production capacity matters, but the lab does not demonstrate the exact historical path from desired unit to required production infrastructure.

### Required correction

Add a second trace:

`desired unit → existing production building count → pending build state → can-train → train`

if the source provides that chain. Otherwise mark the missing edge UNCERTAIN.

---

## QC9-16 — Current AEGIS production work must remain separated from historical evidence

**Severity: HIGH**

The project now has a substantial AEGIS Production Director. That current implementation should not be used as retroactive evidence for what historical Promisory meant.

Current AEGIS code can be an **implementation comparison**, not a historical source.

This separation is especially important because current AEGIS production code explicitly models deficits, capacity pressure, technology pressure, resource posture, reserve priority, switch cost, and related state. That is valuable AEGIS design evidence, not proof of historical Promisory semantics.

---

# 6. Lab 4 — Threat Classification → Response

## QC9-17 — The threat lab needs one complete representative branch

**Severity: CRITICAL**

The source contains concrete threat-measurement machinery. For example, `threats.per` contains rules that use `sn-target-player-number`, `up-get-focus-fact unit-type-count`, and then accumulate counts into strategic-number threat measures such as cavalry-archer, gunpowder, and infantry categories.

This is much stronger evidence than the prose currently shows.

### Required correction

Pick one class—preferably cavalry or cavalry-archer—and show:

`focus/target selection → exact unit measurements → accumulator writes → consumer → response rule`.

Until the consumer is traced, the lab should not claim a complete threat→response causal chain.

---

## QC9-18 — Threat classification and threat scoring are being conflated

**Severity: HIGH**

The source visibly accumulates threat-related strategic-number values. That does not necessarily mean it has a normalized “threat score” in the AEGIS sense.

### Required correction

Separate:

`COUNT / AGGREGATE`
from
`CLASSIFICATION`
from
`PRIORITY / SCORE`
from
`RESPONSE AUTHORIZATION`.

The exact source semantics must decide which category applies.

---

## QC9-19 — `focus-player` / `target-player` context needs explicit temporal ownership

**Severity: HIGH**

The threat system repeatedly changes or depends on focus/target player state. That means the measurement context itself is stateful.

### Required correction

For the representative threat trace document:

`who sets focus | when | why | who reads it | who restores it | what happens if it changes mid-scan`.

This is a critical practical lesson that Pass 9 currently leaves implicit.

---

## QC9-20 — “Opponent belief” remains AEGIS architecture

**Severity: MEDIUM**

The source supports observed enemy measurements and threat categories. It does not establish a universal probabilistic belief object with confidence and expiry.

### Required correction

Keep:

`historical observation/classification`

separate from:

`AEGIS belief(confidence,evidence-age,alternatives,expiry)`.

---

# 7. Lab 5 — Candidate Search / Optimization

## QC9-21 — This is the most important missing exact-code lab after threat classification

**Severity: CRITICAL**

The source contains a genuine stateful search pattern in `general.per`, including search reset, local search, search-state retrieval, filtering, candidate handling, iteration counters, jumps, and placement/action selection.

Pass 9 currently summarizes that pattern but does not expose the complete slice.

### Required correction

Show the smallest complete loop that includes:

`INITIALIZE → SEARCH → MEASURE → COMPARE → PRESERVE BEST → ADVANCE → JUMP → TERMINATE → CONSUMER`.

The exact goals used in the loop must be named.

---

## QC9-22 — “Optimizer” must remain carefully qualified

**Severity: HIGH**

Calling the historical machinery an optimizer is useful pedagogically, but it can imply a general optimization abstraction that the source does not contain.

### Required correction

Use:

> “stateful candidate-search/evaluation routine that can implement optimization-like behavior.”

Then reserve “optimizer” for the AEGIS abstraction.

---

## QC9-23 — Search reset is a correctness condition, not an implementation detail

**Severity: HIGH**

The source explicitly resets searches and filters before new searches. Pass 9 mentions reset but does not teach the failure mode.

### Required correction

Show one stale-search counterexample:

`previous search results remain → new filter applied to old list → wrong candidate set → wrong action`.

This should be part of the lab because it is one of the most important `.per` implementation hazards.

---

## QC9-24 — Jump semantics require exact direction and destination

**Severity: HIGH**

`up-jump-rule` is not merely “loop.” Its exact target matters.

The source contains jumps such as `up-jump-rule -3`, `-4`, and other positive jumps. These can bypass portions of the rule list.

### Required correction

For the representative search loop document:

`current rule | jump value | destination | skipped rules | state required on re-entry | termination condition`.

---

## QC9-25 — Search performance needs measured complexity

**Severity: MEDIUM**

Pass 9 correctly says performance is part of correctness, but gives no measured historical example.

### Required correction

For the selected search:

`entry frequency | candidate cap | iterations | rules/iteration | reset operations | early exit | worst-case path`.

If exact evaluation cost cannot be measured, mark it UNKNOWN rather than inventing a number.

---

# 8. Lab 6 — Scout Path / Waypoint Selection

## QC9-26 — This lab contains unusually strong direct source material that should be exploited

**Severity: HIGH**

The source itself contains unusually explicit comments:

- create group;
- analyze path for safety;
- break into four quartersteps;
- inspect TC/spear/castle conditions;
- obtain pivot point;
- generate rotated candidate points;
- interpolate toward target;
- choose the closer point;
- calculate/select waypoints.

Pass 9 reports these facts but does not quote the actual executable slice.

### Required correction

This lab should become the model for all eight labs: exact comments + exact rules + exact state channels + exact geometric operation + strategic interpretation.

---

## QC9-27 — “Information acquisition” is a strategic interpretation

**Severity: MEDIUM**

The source demonstrates path safety and route selection. It does not literally say “maximize information value.”

### Required correction

Use three layers:

`path/waypoint mechanism = DIRECT`

`scouting as information acquisition = INFERRED`

`value-of-information scoring = AEGIS-GENERALIZATION`.

---

## QC9-28 — Scout safety and information value are separate objectives

**Severity: MEDIUM**

A safe route is not necessarily the most informative route. Pass 9 tends to merge the two.

### Required correction

Document at least:

`SAFETY SCORE`
versus
`INFORMATION VALUE`.

If the historical code only implements safety/geometry, say so explicitly. AEGIS may later add information value.

---

## QC9-29 — Group lifecycle is under-traced

**Severity: HIGH**

The source creates a group, assigns units, computes group points, analyzes the path, and later acts. Pass 9 should identify the exact lifecycle.

### Required correction

Record:

`group creation → membership → target → geometry → action → regroup/reset/destruction`.

---

# 9. Lab 7 — Attack → Retreat → Restart

## QC9-30 — Controller-state evidence is strong, but physical retreat remains unproven

**Severity: HIGH**

The HD source directly changes `retreat-now-goal`, `attack-status-goal`, clears `attack-goal`, enables timers, and manipulates reset/restart state.

That proves a controller-state transition.

It does not prove that the military units physically disengaged at that exact moment.

### Required correction

Separate:

`controller retreat request = DIRECT`

from:

`physical disengagement = WORLD-STATE EVIDENCE REQUIRED`.

---

## QC9-31 — Restart identity is not yet fully traced

**Severity: HIGH**

The presence of `restart-attack-goal` is direct evidence of restart-related state. It does not prove that every restart corresponds to the same combat objective that preceded retreat.

### Required correction

Trace:

`restart-attack-goal writer → readers → resetters → target identity → re-entry conditions`.

If objective identity is not preserved, state that explicitly.

---

## QC9-32 — “Preserve military capital” is an inference

**Severity: MEDIUM**

This is strategically compelling but remains a reconstruction.

### Required correction

`retreat/reset/restart mechanism = DIRECT`

`preservation of future military capability = INFERRED`

unless a source comment or downstream objective proves the rationale.

---

## QC9-33 — The attack state machine should distinguish state from normalized phase labels

**Severity: MEDIUM**

`PREPARE → AUTHORIZE → MOVE → ENGAGE → ASSESS → REGROUP → RETREAT` is an AEGIS-normalized state machine. The historical source uses multiple goals, flags, timers, and rule conditions rather than necessarily naming these phases.

### Required correction

Show a mapping table:

`AEGIS phase | historical channel(s) | exact evidence | confidence`.

---

# 10. Lab 8 — Building Placement → Fallback / Recovery

## QC9-34 — This lab has the strongest explicit failure evidence in Pass 9

**Severity: STRENGTH**

`buildings.per` literally documents a secondary backup because the regular system occasionally fails. This is unusually valuable programmer-mind evidence.

The lab should make this a centerpiece rather than merely paraphrasing it.

### Required correction

Show:

`primary placement path → failure condition → backup rule → alternate action → resulting state`.

---

## QC9-35 — Generic recovery taxonomy is AEGIS, not historical source taxonomy

**Severity: HIGH**

The proposed classes such as retry, alternate candidate, change position, change objective, capability substitution, and abort commitment are excellent AEGIS architecture.

They are not established as a unified historical recovery taxonomy.

### Required correction

Label:

`historical fallback/rebuild mechanisms = DIRECT`

`general failure taxonomy = AEGIS-GENERALIZATION`.

---

## QC9-36 — `extremebuildings2.per` needs historical status classification

**Severity: HIGH**

The project already knows this module contains disabled/non-development or specialized historical code in places. Pass 9 should not simply treat it as active production architecture.

### Required correction

For every excerpt from it record:

`ACTIVE | CONDITIONAL | DISABLED | EXPERIMENTAL | HISTORICAL PACKAGING VARIANT`.

---

# 11. Cross-lab architecture audit

## QC9-37 — The cross-lab table still overstates “belief” and “commitment” as historical semantic categories

**Severity: HIGH**

The table maps historical mechanisms to:

`Observation | Classification | Belief | Requirement | Candidate | Evaluation | Commitment | Authority | Action | Verification | Recovery | Reassessment`.

That is an excellent AEGIS normalization, but several of these categories are not explicit historical types.

### Required correction

Add a `Historical semantic evidence` column with values:

`DIRECT | COMPOSED | INFERRED | NONE`.

For example:

`belief = distributed interpretation / no universal explicit belief object`.

---

## QC9-38 — Authority is the largest cross-lab semantic risk

**Severity: HIGH**

The historical source often uses control state and conditional guards, while AEGIS deliberately separates intent, commitment, authority, and execution.

The cross-lab table should not imply that historical Promisory had a separate authority plane.

### Required correction

Rename the historical column to:

`CONTROL/PERMISSION EFFECT`

and reserve:

`AUTHORITY PLANE`

for AEGIS.

---

## QC9-39 — Verification needs historical examples, not only AEGIS doctrine

**Severity: HIGH**

The cross-lab table says “verification = pending/state checks and subsequent rules.” This is directionally correct but too broad.

### Required correction

For each action family, provide one actual historical verification pattern or mark it UNCERTAIN:

`BUILD | RESEARCH | TRAIN | MOVE | ATTACK | RETREAT | TRANSPORT`.

Do not infer a universal verification architecture from the existence of pending checks.

---

## QC9-40 — Recovery and reassessment are being combined

**Severity: MEDIUM**

A fallback can recover execution without changing strategic state. Reassessment can change strategy without an execution failure.

### Required correction

Keep:

`FAILURE → RECOVERY`

and:

`NEW INFORMATION / STATE CHANGE → REASSESSMENT`

as separate pathways.

---

# 12. Read-a-rule-backwards audit

## QC9-41 — Excellent technique, but it needs one complete demonstration

The Pass-9 “read a `.per` rule backwards” procedure is one of the strongest practical additions:

`ACTION ← GUARDS ← STATE DEPENDENCIES ← WRITERS ← INITIALIZATION ← LOAD ORDER`.

However, it remains instructional prose rather than a worked forensic example.

### Required correction

Apply it completely to one historical rule, preferably the Imperial research rule or one production rule.

Show every writer and reader found, including competing writers and resetters.

---

## QC9-42 — Forward and backward traces must converge

**Severity: HIGH**

A practical archaeology test should require:

`backward dependency trace`

and:

`forward causal trace`

to meet at the same state/action boundary.

If they do not, the discrepancy becomes a finding rather than being silently reconciled.

---

# 13. “What `.per` is not” audit

## QC9-43 — Strong section; add one critical caveat

The artifact correctly warns against treating `.per` as ordinary sequential code and against equating command issuance with success.

Add:

> **Textual order is not by itself causal order.**

But also avoid the opposite error: rule ordering can still matter through eligibility, jumps, state mutation, and repeated evaluation.

The correct statement is:

`textual adjacency ≠ automatic causality`, not `textual order never matters`.

---

# 14. State ownership audit

## QC9-44 — AEGIS ownership contract is good but historical ownership is not actually recovered

The state ownership schema is appropriate:

`STATE_ID | TYPE | OWNER | WRITERS | READERS | RESETTER | AUTHORITY_EFFECT | LIFETIME | INVALIDATION | SIDE_EFFECTS | EVIDENCE`.

But most Pass-9 labs still leave owner/writer/reader fields at narrative level.

### Required correction

For each of the eight labs, fill at least one complete state-ownership record from actual source.

---

## QC9-45 — “Owner” must not be inferred from the file name

**Severity: HIGH**

A module containing a state variable is not necessarily its sole owner.

### Required correction

Owner inference requires:

`writer set + resetter set + downstream effect + lifecycle responsibility`.

If multiple modules write it without arbitration, record `DISTRIBUTED/AMBIGUOUS` rather than assigning a clean owner.

---

# 15. Commitment audit

## QC9-46 — Commitment contract is correctly AEGIS, but historical mapping is incomplete

The AEGIS commitment schema is excellent:

`owner | objective | cost | timing | deadline | break | replacement | authority | release | verification`.

But only escrow is directly demonstrated as a resource-protection mechanism in the historical evidence currently used by Pass 9.

### Required correction

Create a mapping table:

`AEGIS commitment field | historical analogue | evidence grade | exact anchor`.

Do not fill missing historical fields by inference without labeling them.

---

# 16. Evidence / external triangulation audit

## QC9-47 — External documentation supports the primitive vocabulary, not the historical strategic interpretation

Independent AI scripting references corroborate the existence and general use of goals, search/DUC primitives, timers, attack mechanisms, and scripting constructs. That is useful semantic triangulation.

It does not independently prove the reconstructed intent of the Promisory authors.

### Required correction

Use external sources for:

`ENGINE/SCRIPTING SEMANTICS`

and the verified historical source for:

`WHAT PROMISORY ACTUALLY DID`.

Keep the two evidence classes distinct.

---

## QC9-48 — Search-engine agreement is not independent proof

**Severity: MEDIUM**

Web, Exa, and Tavily can find the same historical discussion or mirrored documentation. Agreement increases discovery confidence, not causal proof.

### Required correction

For each external corroboration record:

`source independence | primary/secondary | exact claim supported | whether it confirms semantics or historical behavior`.

---

# 17. Strategic-game audit

## QC9-49 — The strategic framing is excellent and should be retained

**Severity: STRENGTH**

The labs consistently ask the game question rather than stopping at code mechanics. This is exactly the correct Layer-2 direction.

The strongest formulation is:

> **What game relationship is the historical mechanism trying to change, and what capability does it make available or protect?**

Keep this.

---

## QC9-50 — “Capability transition” is a powerful synthesis, but not every mechanism is a transition

**Severity: MEDIUM**

Some rules are bookkeeping, synchronization, tactical maintenance, or engine adaptation. Not every rule needs to be elevated into a strategic transition.

### Required correction

Classify each lab mechanism as:

`STRATEGIC TRANSITION | OPERATIONAL CONTROL | TACTICAL CONTROL | BOOKKEEPING | ENGINE ADAPTATION | HISTORICAL ARTIFACT`.

This prevents over-strategizing low-level code.

---

## QC9-51 — Opportunity cost is present but should be tied to actual source behavior

**Severity: MEDIUM**

Pass 9 repeatedly explains resource competition, which is strategically correct. But the historical evidence should show exactly where a competing spend is blocked, delayed, or deprioritized.

### Required correction

For at least two labs, identify a concrete competing action and show the guard/state that protects the higher-priority conversion.

---

## QC9-52 — Opponent response remains mostly AEGIS forward modeling

**Severity: HIGH**

Pass 9 correctly mentions that the opponent can transition. But this should not be interpreted as proof that historical Promisory explicitly predicts the opponent.

### Required correction

Use:

`OBSERVED OPPONENT RESPONSE = historical evidence`

`PREDICTED OPPONENT RESPONSE = AEGIS model/hypothesis`

unless an exact predictive source branch is found.

---

# 18. Implementation-readiness audit

## QC9-53 — Pass 9 is not yet ready to serve as a direct coding specification

**Severity: HIGH**

A professional engineer reading Pass 9 could understand the architecture and know where to investigate, but could not yet reproduce each historical subsystem from the document alone.

That means it is currently a **research lab**, not yet a **coding manual**.

This is acceptable for the current phase if stated honestly.

### Required correction

Change the status to:

> “Historical implementation lab / working forensic training artifact.”

Keep “implementation specification” for the post-Pass-10 version.

---

## QC9-54 — Each lab needs a minimum reproducibility packet

**Severity: HIGH**

Required per lab:

1. source file;
2. exact lines;
3. excerpt;
4. dependencies;
5. rule-by-rule trace;
6. state ownership;
7. lifecycle;
8. engine primitive semantics;
9. strategic interpretation;
10. alternative explanation;
11. falsifier;
12. failure/recovery;
13. AEGIS translation;
14. confidence/evidence grade.

Anything missing remains a research gap.

---

# 19. Cross-artifact consistency audit

## QC9-55 — Pass 9 correctly inherits the Pass-8 requirement but does not close it

Pass 8 QC explicitly required eight complete historical code patterns. Pass 9 names the eight patterns but largely provides prose descriptions rather than complete patterns.

**Disposition:** PASS-8 QC requirement is **not yet fully closed**.

---

## QC9-56 — Pass 9 should link directly into Pass 7/8 evidence records

The document currently describes evidence grades but does not systematically reference the exact edge IDs that justify each claim.

### Required correction

For each lab, add:

`RELATED EDGE LEDGER IDS | RELATED TRANSITION IDS | RELATED STATE-CHANNEL IDS`.

This creates bidirectional provenance.

---

## QC9-57 — The inheritance matrix needs a historical evidence column

The current matrix says what to preserve/improve/reject. That is design guidance, not proof.

### Required correction

Add:

`Historical evidence grade | Source anchor | AEGIS treatment`.

---

# 20. Quantitative evidence coverage

Pass 9 should not be promoted until the following coverage metrics are calculated.

| Metric | Required target before canonical promotion |
|---|---:|
| Labs with exact source excerpt | 8/8 |
| Labs with exact line anchors | 8/8 |
| Labs with complete rule trace | 8/8 |
| Labs with writer/reader map | 8/8 |
| Labs with reset/release trace | 8/8 where applicable |
| Labs with historical postcondition | 8/8 where applicable |
| Labs with failure/recovery trace | 8/8 where applicable |
| Labs with explicit historical-vs-AEGIS split | 8/8 |
| Labs with alternative explanation | 8/8 |
| Labs with falsifier | 8/8 |
| Labs with performance note | 8/8 where search/geometry is involved |
| Labs linked to Pass-7 edge IDs | 8/8 |
| Labs linked to source-state graph | 8/8 |

Current Pass-9 status: **insufficient evidence to claim these targets are met.**

---

# 21. Recommended Pass-10 extraction protocol

Pass 10 should now be executed as a forensic extraction pass, not another conceptual essay.

## For each lab

### Step 1 — Select one narrow historical slice

Do not trace an entire module.

### Step 2 — Extract exact source

Capture:

`defconst dependencies → defrule(s) → immediate readers → immediate writers → reset/release`.

### Step 3 — Build literal execution trace

For every guard/action:

`LITERAL SYNTAX → ENGINE MEANING → STATE EFFECT`.

### Step 4 — Build ownership map

`writer → reader → resetter → lifecycle → side effect`.

### Step 5 — Build game-strategy interpretation

`WHO → WHAT → WHEN → WHERE → WHY`.

### Step 6 — Challenge the interpretation

Record:

`alternative explanation → falsifier → unresolved edge`.

### Step 7 — Separate AEGIS design

Only after historical tracing, derive:

`preserve | improve | reject | new AEGIS abstraction`.

### Step 8 — Record computational cost

Especially for search, scouting, geometry, and aggregate threat measurement.

---

# 22. Eight exact extraction targets

| Lab | Primary exact slice | Secondary exact slice |
|---|---|---|
| 1 | `escrow.per` Castle/Imperial research rule | escrow release/reset |
| 2 | `gatherers.per` `temporary-goal10` regime | one downstream percentage regime |
| 3 | `units.per` representative production rule | writer of its unit-goal/production flag |
| 4 | `threats.per` cavalry/cavalry-archer accumulator | one downstream consumer |
| 5 | `general.per` bounded search loop | best-candidate consumer |
| 6 | `scoutcontrol.per` quarterstep/path analysis | waypoint/action consumer |
| 7 | HD attack/retreat block | `restart-attack-goal` consumer |
| 8 | `buildings.per` backup/rebuild rule | primary placement path it backs up |

This set is small enough to be forensic and large enough to satisfy the practical purpose of Pass 9.

---

# 23. Final disposition

## What survives intact

1. The game-problem-first framing.
2. The eight selected mechanisms.
3. The historical-vs-AEGIS evidence hierarchy.
4. The “read a `.per` rule backwards” method.
5. The state-ownership emphasis.
6. The recognition that search and geometry are algorithmic infrastructure.
7. The recognition that attack is temporal state rather than a Boolean.
8. The explicit building fallback evidence.
9. The strategic focus on capability, timing, position, resources, and opponent response.
10. The conclusion that AEGIS should inherit problem-solving knowledge rather than copy historical architecture.

## What must change

1. Add exact code.
2. Add exact anchors.
3. Add complete rule traces.
4. Add writer/reader/resetter maps.
5. Separate historical control/permission from AEGIS authority.
6. Separate observation/classification from AEGIS belief.
7. Separate aggregate measurement from scoring/classification.
8. Separate command/control postconditions from world-state postconditions.
9. Separate recovery from reassessment.
10. Separate observed opponent response from predicted response.
11. Add alternative explanations and falsifiers.
12. Add performance measurements.
13. Add bidirectional provenance links to Pass 7/8 artifacts.
14. Add quantitative evidence-coverage metrics.

## Final QC judgment

**PASS 9: ACCEPT WITH CORRECTIONS.**

**Research quality:** HIGH  
**Strategic interpretation:** HIGH, with appropriate evidence grading  
**Historical source fidelity:** MODERATE-HIGH  
**Forensic reproducibility:** MODERATE  
**Literal `.per` implementation literacy:** MODERATE-LOW  
**AEGIS design value:** HIGH  
**Canonical readiness:** NOT YET

The central lesson is important:

> **Pass 9 successfully identifies the right historical mechanisms, but it has not yet extracted them deeply enough to teach implementation from source.**

The next pass should therefore become deliberately concrete. It should contain less prose and more exact source: code, anchors, state writes, readers, resets, side effects, and trace tables.

That is the correct point at which the archaeology becomes an implementation-grade knowledge base.
