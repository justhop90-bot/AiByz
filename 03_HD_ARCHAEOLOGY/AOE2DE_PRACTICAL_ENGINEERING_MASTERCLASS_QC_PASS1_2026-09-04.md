# AoE2DE Practical Engineering Masterclass — Deep QC Pass 1

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Audited artifact:** `AOE2DE_PRACTICAL_ENGINEERING_MASTERCLASS_PASS8_2026-09-04.md`  
**Status:** ACCEPT WITH CORRECTIONS  
**Primary evidence:** verified `AI (HD version).per` and verified Promisory source; Layer-1 machine evidence for current-engine semantics  

---

## 0. Executive verdict

Pass 8 is a substantial improvement over the catalogue-style practical knowledge base. It successfully teaches a reader to begin with a **game relationship**, decompose it into observations/state/requirements/constraints/candidates/commitment/action/verification, and recognize that `.per` rule networks can express algorithms through persistent state and control flow.

It is **not yet canonical as a practical engineering manual**.

The principal problem is no longer conceptual weakness. The problem is **boundary precision**: several passages move too quickly from historical source behavior to a unified AEGIS architecture, and several practical statements are stronger than the evidence currently established. A second issue is pedagogical: the document teaches the architecture well, but it still gives the reader too little actual `.per` syntax and too few complete historical code traces to bridge from conceptual design to implementation.

### Verdict

**ACCEPT WITH CORRECTIONS — DO NOT REJECT.**

The document should remain in the branch as the Pass-8 teaching artifact, but the next revision must:

1. tighten historical-vs-AEGIS attribution;
2. distinguish state ontology from architectural interpretation;
3. attach source anchors to important historical claims;
4. stop treating some useful AEGIS concepts as if they were already demonstrated by HD;
5. add concrete `.per` implementation patterns and complete source traces;
6. distinguish engine semantics from source-programming conventions;
7. add explicit failure/verification mechanics;
8. preserve the strategic-game framing that is the strongest part of the pass.

---

# 1. What Pass 8 gets right

## QC-01 — Strategic framing is correct and should be preserved

**Severity:** NONE / STRENGTH  
**Finding:** The opening reframes AI programming around changing a game relationship rather than writing an isolated rule. The `GAME PROBLEM → ... → REASSESSMENT` chain is an effective teaching abstraction.

**Evidence:** This is consistent with the Layer-2 charter and the composed transition architecture established in earlier passes.

**Judgment:** Keep. This is the core pedagogical thesis.

---

## QC-02 — The mastery questions are excellent but need evidence tags where historical claims begin

**Severity:** LOW  
**Finding:** The WHO/WHAT/WHEN/WHERE/WHY/HOW test is an AEGIS design rubric, not a recovered statement of HD programming doctrine.

**Correction:** Label it explicitly as an **AEGIS teaching rubric derived from source archaeology**. Do not imply the historical programmers used this exact checklist.

---

# 2. Historical-source attribution audit

## QC-03 — “That sequence is the practical core of the HD/Promisory codebase” is too strong

**Severity:** HIGH  
**Finding:** The sequence is a **composed reconstruction** of many distributed mechanisms. The document immediately qualifies this, but the opening sentence still reads as though the source itself establishes the complete pipeline.

**Correction:** Replace with language equivalent to:

> “That sequence is the practical control model reconstructed from the combined HD/Promisory mechanisms; the source implements its pieces through distributed rule networks rather than one literal pipeline.”

**Evidence grade:** COMPOSED, not DIRECT.

---

## QC-04 — “The historical source often encodes” observation/classification/belief/requirement/commitment as separate state types is partially over-broad

**Severity:** HIGH  
**Finding:** The source clearly contains separate goals, threat state, production state, timers, escrow/resource-control state, etc. It does **not** establish a clean universal ontology matching the five categories.

**Correction:** Say that the source provides **distributed examples corresponding to these roles**, then state that the explicit typed ontology is an AEGIS architecture.

**Required distinction:**

`historical storage channel` ≠ `historical semantic type`.

---

## QC-05 — “The historical source ... contains many intermediate state channels precisely because complex strategy cannot be represented safely as direct fact-to-action mappings” contains an intent claim

**Severity:** MEDIUM  
**Finding:** The existence of intermediate state channels is direct/composed evidence. The word **“precisely”** attributes design motivation that has not been directly documented.

**Correction:** Use:

> “The source contains many intermediate state channels, which is consistent with the need to decompose complex decisions rather than encode everything as direct fact-to-action mappings.”

Evidence grade: COMPOSED / INFERRED.

---

## QC-06 — Goal semantics are taught too uniformly

**Severity:** HIGH  
**Finding:** “A goal allows the AI to say: this is what I currently believe/intend/control” collapses several historical uses. Goals are a storage/control primitive; some are state, some flags, some scratch values, and some participate directly in engine actions.

**Correction:** Teach goals as **integer state channels whose semantic role is assigned by the program**. Then classify individual goals as observation-derived state, control state, intent, scratch, counter, etc.

This avoids turning “goal” into a semantic category it does not inherently possess.

---

## QC-07 — Strategic-number description risks conflating SNs with a general “API” abstraction

**Severity:** MEDIUM  
**Finding:** “Strategic number: an engine-facing control interface” is useful but too broad as a definition. Some SNs are configuration/behavior controls; not every strategic number should be described as if it were a generic API endpoint.

**Correction:** Define SNs as **engine-provided/configurable numeric controls with program-visible semantics**, then explain that AEGIS should document them as interfaces because changing them can alter engine behavior.

---

## QC-08 — Timer examples include AEGIS lifecycle semantics not proven for every historical timer

**Severity:** MEDIUM  
**Finding:** `expires = T; cooldown = C; invalidated by = X` is an AEGIS state model. Historical timers establish time gating and lifecycle behavior, but not a universal object with all four fields.

**Correction:** Explicitly label the structure as AEGIS representation; teach historical timers separately as primitive time gates/state.

---

## QC-09 — “High-numbered ... goals are useful as scratch registers” needs stronger qualification

**Severity:** HIGH  
**Finding:** The source contains high-numbered temporary goals and explicit scratch behavior, but **number alone does not prove scratch semantics**. A high goal can still be architectural state.

**Correction:** Say:

> “Goals explicitly designated or demonstrably used as temporary/intermediate channels can serve as scratch registers. Numeric range alone is not sufficient evidence of scratch status.”

This is important because Layer-2 evidence discipline already warns against assigning semantic ownership from naming/range alone.

---

# 3. Engine/source boundary audit

## QC-10 — `can-*` and pending-state section needs a three-way distinction

**Severity:** HIGH  
**Finding:** The section correctly says `DESIRE ≠ FEASIBILITY ≠ EXECUTION ≠ SUCCESS`, but “pending state answers whether an attempted conversion is already underway” is too generic. Pending mechanisms differ by action family and must be tied to exact predicates/facts.

**Correction:** Teach:

`DESIRE → CAN-FACT → SIDE-EFFECT COMMAND → PENDING/WORLD OBSERVATION → POSTCONDITION`

and explicitly state that the exact pending predicate is action-specific and engine/source-version dependent.

---

## QC-11 — Search/optimization claims need exact historical anchors

**Severity:** HIGH  
**Finding:** The document correctly reconstructs the `general.per` loop as an algorithm, but this is one of the most important practical claims and currently lacks an exact source trace in the chapter.

**Correction:** Add one complete historical trace with:

`reset → candidate acquisition → scratch state → score → best-candidate write → iteration advance → jump → termination → consumer`

and identify the actual goals/facts/actions used.

Evidence grade: DIRECT for individual operations; COMPOSED for the algorithmic loop.

---

## QC-12 — “Do not confuse a rule engine with a language incapable of algorithms” is pedagogically strong but should distinguish algorithmic expressiveness from conventional programming-language semantics

**Severity:** LOW  
**Finding:** The claim is reasonable, but the exact mechanism is **rule-network state transitions**, not conventional sequential execution.

**Correction:** Add:

> “The algorithm is distributed across rule eligibility, persistent state, jumps, and repeated evaluation; it is not a conventional function call stack or ordinary sequential loop.”

---

# 4. Worked-example audit

## QC-13 — Cavalry example is strategically excellent but candidate space is too broad without historical/AEGIS labels

**Severity:** HIGH  
**Finding:** “counter-unit, mixed composition, siege, fortification, mobility, avoidance, attack elsewhere, technology, or economic transition” is an excellent AEGIS candidate set. It is not a demonstrated single historical candidate generator.

**Correction:** Split into:

**Historical evidence:** distributed cavalry/threat classification and response mechanisms.  
**AEGIS candidate space:** the broader alternatives listed above.

This distinction already exists elsewhere in Layer 2 and should be repeated here.

---

## QC-14 — Cavalry “commitment” is too tightly connected to escrow

**Severity:** MEDIUM  
**Finding:** Historical escrow demonstrates resource reservation/control. It does not establish that every military commitment is represented through escrow.

**Correction:** Say escrow is **one historical mechanism for protecting a future conversion**, while AEGIS commitment is a broader architectural abstraction that may use escrow, production authorization, state ownership, or other mechanisms.

---

## QC-15 — Verification example needs concrete `.per` evidence

**Severity:** HIGH  
**Finding:** The conceptual distinction between command success and world-state success is correct, but the reader is not shown what an actual verification rule looks like.

**Correction:** Add a small historical pattern demonstrating:

`action issued → later fact/condition observed → state updated`

and separately show the AEGIS strengthened version with an explicit expected postcondition.

---

# 5. Resource/economy audit

## QC-16 — “Resource is strategically available only after accounting for commitments” is an AEGIS policy, not a historical invariant

**Severity:** MEDIUM  
**Finding:** Strong design principle, but historical code may still expose raw resource counts to many consumers.

**Correction:** Mark as **AEGIS-GENERALIZATION** and distinguish:

`engine resource stock` from `AEGIS strategically allocable stock`.

---

## QC-17 — Resource-tax formula is correctly labeled but needs operational variables

**Severity:** MEDIUM  
**Finding:**

`direct cost + infrastructure cost + opportunity cost + timing cost + risk cost`

is a useful conceptual formula, but it is not computable until each term has measurable variables.

**Correction:** Add a table mapping each term to measurable AoE2 variables, e.g. resource delta, builder-time, production idle time, expected arrival time, reserve reduction, probability/confidence, or opportunity displacement.

The formula should remain explicitly AEGIS design.

---

## QC-18 — Gatherer allocation claim is good but “demand forecast” is stronger than the historical evidence

**Severity:** MEDIUM  
**Finding:** `gatherers.per` clearly changes allocation contextually. A generalized “demand forecast” architecture is AEGIS design unless explicit forecasting is demonstrated.

**Correction:** Historical:

`strategic/contextual state → gatherer allocation`

AEGIS:

`objective → projected demand → allocation`

Keep both.

---

# 6. Production/technology audit

## QC-19 — Production as “authorization” is a useful reading but should not imply a universal historical authorization layer

**Severity:** HIGH  
**Finding:** `units.per` does use training flags/conditions as production control, but the term “authorization” is an AEGIS semantic interpretation.

**Correction:** State that historical production flags function as **production permissions/control state** and that AEGIS generalizes this into an explicit authorization plane.

---

## QC-20 — Technology candidate evaluation is entirely AEGIS design

**Severity:** LOW  
**Finding:** The technology cost/capability/opportunity-cost formula is correctly framed as a design proposal. It should be visually marked as such so a reader cannot mistake it for a recovered historical scoring equation.

**Correction:** Add an `AEGIS DESIGN` callout.

---

# 7. Geometry/scouting audit

## QC-21 — “Scouting is information acquisition” is a strategic inference, not direct source wording

**Severity:** LOW  
**Finding:** The historical scout controller clearly performs route/path/obstacle/candidate analysis. The information-value framing is a strong strategic interpretation.

**Correction:** Label:

`Historical mechanism: DIRECT`  
`Strategic interpretation: INFERRED`  
`Decision-value model: AEGIS-GENERALIZATION`.

This three-layer separation should become a recurring teaching pattern.

---

## QC-22 — “Distance is strategic information” needs one worked game example

**Severity:** LOW  
**Finding:** The claim is correct as strategic reasoning but remains abstract.

**Correction:** Add one numerical example showing how identical military forces produce different decisions when reinforcement distance changes the timing relationship.

---

# 8. Combat/transition audit

## QC-23 — Attack state-machine representation is strong, but “historical HD state includes distinct ...” should cite exact anchors

**Severity:** HIGH  
**Finding:** This is one of the strongest historical claims in the manual and should be tied directly to the known attack/retreat/restart/timer source anchors already documented in Pass 6/7.

**Correction:** Add source references for:

- `attack-goal`
- `attack-status-goal`
- `retreat-now-goal`
- `restart-attack-goal`
- attack timer/reset behavior.

Then explicitly distinguish the **historical state channels** from the **AEGIS state-machine representation**.

---

## QC-24 — “This is one of the strongest practical lessons in the historical architecture” is interpretive ranking

**Severity:** LOW  
**Finding:** Reasonable editorial judgment, not evidence.

**Correction:** Fine to retain as editorial judgment, but not inside an evidence claim. Prefer “One of the clearest practical patterns exposed by the source is...”

---

## QC-25 — Fortification section correctly distinguishes detection from siege, but “capability substitution” should be explicitly marked AEGIS

**Severity:** MEDIUM  
**Finding:** Historical source demonstrates fortification awareness and attack modification; separate siege machinery exists. The generalized response family is AEGIS architecture.

**Correction:** Add explicit labels for historical evidence vs AEGIS candidate substitution model.

---

# 9. Failure and verification audit

## QC-26 — Failure taxonomy is valuable but should be defined as a design contract

**Severity:** MEDIUM  
**Finding:** The seven failure classes are excellent AEGIS architecture, but the source does not yet establish this complete taxonomy.

**Correction:** Add a table:

`Failure class | observable signature | historical analogue | AEGIS use`

Do not imply the historical AI had this taxonomy.

---

## QC-27 — “Only later world-state observations establish what actually happened” is too absolute

**Severity:** MEDIUM  
**Finding:** World-state observations are the strongest basis for postcondition verification, but some engine-native state predicates may constitute authoritative state without waiting for a later visible-world observation.

**Correction:** Say:

> “Command issuance alone does not establish the intended postcondition. Verification requires an authoritative state predicate or subsequent world-state observation appropriate to the action.”

This is more precise and aligns with Layer-1 authority.

---

## QC-28 — Three postcondition levels should include action-specific examples

**Severity:** LOW  
**Finding:** The three levels are excellent but abstract.

**Correction:** Give one example for build, research, and military action.

Example:

`build command issued → building exists → production capacity changed`

This makes the model immediately usable.

---

# 10. Architecture audit

## QC-29 — State ownership section is excellent but historical ownership must be separated from AEGIS ownership

**Severity:** HIGH  
**Finding:** The document does say the sample `attack-goal` ownership is an AEGIS example, which is good. But the section should systematically teach the reader how to recover historical ownership rather than merely prescribe AEGIS ownership.

**Correction:** Add a mini-procedure:

`find writers → find readers → find resetters → trace lifecycle → identify side effects → classify owner → record ambiguity`.

This connects the manual directly to the Evidence Edge Ledger.

---

## QC-30 — Authority/intent separation is Porphyra-derived, not recovered HD architecture

**Severity:** HIGH  
**Finding:** The text correctly attributes this to Porphyra-derived AEGIS architecture, but because the manual is primarily framed as HD/Promisory archaeology, this needs stronger visual separation.

**Correction:** Add an explicit “AEGIS architecture” callout before the section and say historical source may distribute equivalent control effects without a separate authority plane.

---

# 11. Hysteresis and transition audit

## QC-31 — Hysteresis example is correct but incomplete without commitment state

**Severity:** LOW  
**Finding:** Threshold hysteresis prevents rapid threshold crossing but does not by itself solve stale beliefs, conflicting writers, or commitment lifecycle.

**Correction:** Present hysteresis as one stabilizer among:

`hysteresis + cooldown + persistence + invalidation + ownership + commitment lifecycle`.

---

## QC-32 — “Every major commitment should have...” is a normative AEGIS contract

**Severity:** NONE / CLARIFY  
**Finding:** Correct and valuable, but purely architectural.

**Correction:** Mark `AEGIS REQUIREMENT`, not historical reconstruction.

---

## QC-33 — Strategy-as-transition claim is strong but should explicitly separate source evidence from synthesis

**Severity:** MEDIUM  
**Finding:** The transition chain is one of the strongest synthesized conclusions from Layer 2. It is not a literal source doctrine.

**Correction:** Label it `COMPOSED + INFERRED`, with links back to the transition table/evidence-edge ledger.

---

# 12. Pedagogical audit

## QC-34 — The document still lacks enough real `.per` code

**Severity:** CRITICAL FOR PURPOSE  
**Finding:** This is now called a **Practical Engineering Masterclass**, but most examples remain pseudocode and conceptual design. A reader can understand the architecture without yet being able to implement it in `.per`.

**Required correction:** The next revision must contain at least **8 complete historical code patterns**, each with:

1. original `.per` excerpt,
2. line/module anchor,
3. plain-English execution trace,
4. state written,
5. state read,
6. guard,
7. side effect,
8. lifecycle/reset behavior,
9. strategic meaning,
10. AEGIS improved pattern.

Suggested patterns:

- escrowed research,
- contextual gatherer allocation,
- production authorization,
- attack/retreat state transition,
- enemy threat classification,
- candidate search loop,
- scout waypoint selection,
- building placement/fallback.

This is the largest remaining gap.

---

## QC-35 — The reader needs syntax-to-strategy translation tables

**Severity:** HIGH  
**Finding:** The manual teaches architecture but not enough recognition of actual `.per` constructs.

**Required addition:** A compact table:

`Construct | What it literally does | What it means strategically | Typical failure | AEGIS use`

Include:

`defrule`, `defconst`, goals, SNs, timers, `set-goal`, `set-strategic-number`, `up-*`, `can-*`, escrow, DUC/search, `up-jump-rule`, pending facts, object targeting, and load order.

---

## QC-36 — No “read a rule backwards” debugging technique

**Severity:** HIGH  
**Finding:** A practical engineer needs to debug existing rules, not only design new ones.

**Required addition:** Teach reverse tracing:

`ACTION → preceding guards → state dependencies → writers → initialization → source/load order`

and forward tracing:

`FACT → eligible rule → action → mutation → next observable state`.

This directly supports Layer-1's unresolved causal spine without pretending that Layer 1 is solved.

---

## QC-37 — No explicit rule-engine execution caveat

**Severity:** HIGH  
**Finding:** The manual sometimes reads like a conventional imperative program. The reader needs a concise reminder that rule eligibility, evaluation order, jumps, persistent state, and engine scheduling determine behavior.

**Required addition:** A “What `.per` is not” box:

- not ordinary sequential code,
- not guaranteed one-pass execution,
- not safe to infer side-effect success from command issuance,
- not safe to infer ownership from proximity alone,
- not safe to infer lifecycle from a single writer.

---

# 13. Strategic-game audit

## QC-38 — Strong strategic framing should be expanded with opportunity cost and tempo examples

**Severity:** MEDIUM  
**Finding:** The manual correctly asks WHY, but some examples still collapse strategy into capability acquisition.

**Correction:** Add examples where the correct action is to **not** obtain the theoretically strongest capability because timing, economy, map, or opponent response makes it strategically inferior.

This is critical to the user's stated goal of understanding the programmer's mind as an AoE2 strategist rather than merely understanding code.

---

## QC-39 — Opponent response is underdeveloped

**Severity:** HIGH  
**Finding:** The manual says the opponent may transition after a response, but does not teach the reader to distinguish:

`observed response` vs `predicted response`.

**Correction:** Add:

`OBSERVED opponent change = evidence`  
`PREDICTED opponent change = belief/hypothesis`.

Then require a falsifier for predictive branches.

---

## QC-40 — Map/location reasoning should include the “where changes the answer” test

**Severity:** MEDIUM  
**Finding:** WHO/WHAT/WHEN/WHERE/WHY is introduced strongly, but WHERE is not sufficiently exercised in the worked examples.

**Correction:** Add one paired example:

same enemy composition + same resource state + different map geometry → different correct strategy.

This directly reinforces the user's requirement that the strategy-game layer not be reduced to code mechanics.

---

# 14. Evidence architecture additions required

## QC-41 — Add an evidence marker to every major historical paragraph

**Severity:** HIGH  
**Finding:** The document has a final evidence-discipline section, but evidence grading is not attached closely enough to claims.

**Required convention:**

`[DIRECT]` executable source demonstrates it.  
`[COMPOSED]` multiple direct mechanisms form the chain.  
`[INFERRED]` strategic meaning reconstructed.  
`[AEGIS-GENERALIZATION]` new architecture/design.

Do not force every sentence to carry a tag; tag each substantive historical claim/section.

---

## QC-42 — Add exact-anchor references to high-value source claims

**Severity:** HIGH  
**Finding:** Pass 8 relies heavily on earlier archaeology but is difficult to audit independently.

**Required anchors:**

- `escrow.per` Castle/Imperial research,
- `gatherers.per` resource allocation,
- `units.per` production permissions,
- `threats.per` threat classification,
- `general.per` search loop,
- `scoutcontrol.per` geometry/path analysis,
- attack/retreat/restart state in HD,
- fortification handling,
- building fallback.

Approximate anchors are acceptable where exact source tracing is not complete, but they must be labeled approximate.

---

# 15. Missing practical concepts

## QC-43 — Load order and namespace collision are absent

**Severity:** HIGH  
**Finding:** Practical `.per` engineering must teach that a correct rule can still fail because constants/modules load in an unexpected order or definitions are overwritten.

This is especially relevant to AEGIS because custom constants, Promisory modules, and load-order behavior are part of the actual engineering environment.

**Required addition:**

`load graph → definition order → override → collision → validator/runtime discrepancy`.

---

## QC-44 — Validator/runtime discrepancy is absent

**Severity:** HIGH  
**Finding:** The project has already encountered a concrete example where validator expectations and engine semantics can diverge (`knight-line` / `unit-type-count` context). The practical manual should teach the general engineering lesson without turning that one bug into universal doctrine.

**Required addition:**

`validator model ≠ runtime model`

unless independently proven equivalent.

Use the `knight-line` case as a clearly labeled project example if appropriate.

---

## QC-45 — Performance needs a more explicit rule-budget engineering method

**Severity:** MEDIUM  
**Finding:** The document says performance is correctness, but does not give the reader a method for estimating/searching budget cost.

**Required addition:**

For every search/control loop record:

`entry frequency | candidate count | rules per iteration | expected iterations | worst-case iterations | early exit | reset cost | persistent-state cost`.

This directly incorporates the prior Pass-7 search/performance findings.

---

# 16. Missing implementation safety concepts

## QC-46 — Initialization/lifecycle needs a concrete anti-oscillation example

**Severity:** HIGH  
**Finding:** The document discusses state ownership and hysteresis but does not show how an always-eligible initializer can overwrite live state.

**Required addition:** Show:

`ONE-SHOT INITIALIZER` vs `ALWAYS-ELIGIBLE WRITER`

and explain how a valid-looking rule can create oscillation by repeatedly restoring default state.

---

## QC-47 — Revocation/replacement needs an executable boundary example

**Severity:** MEDIUM  
**Finding:** The document defines authority and commitments but does not show where revocation should occur relative to a side effect.

**Required addition:**

`plan → commitment → authority check immediately before side effect → execute → verify`.

Then show why checking authority only during planning is insufficient.

---

## QC-48 — Candidate evaluation needs a worked numerical example

**Severity:** MEDIUM  
**Finding:** The abstraction `candidate → features → constraints → score → uncertainty → decision` is excellent, but without a numerical example it remains conceptual.

**Required addition:** Compare at least three candidates for a real AoE2 problem using approximate values for cost, arrival time, capability, risk, and opportunity cost. Explicitly label the score as AEGIS design, not historical code.

---

# 17. Required Pass-8 revision architecture

The next revision should preserve the existing 15-part structure but insert the following practical layers:

## Layer A — Syntax

What does the construct literally do?

## Layer B — Control semantics

How does the rule network use it?

## Layer C — Game semantics

What AoE2 relationship is being controlled?

## Layer D — Historical intent

What can we actually infer the original programmer was trying to accomplish?

## Layer E — AEGIS improvement

How should the modern architecture preserve or improve the mechanism?

Each worked example should visibly move through A→E.

---

# 18. Canonical practical example format

Every major example should eventually use:

```text
GAME PROBLEM
↓
HISTORICAL SOURCE
↓
LITERAL CODE
↓
RULE-BY-RULE TRACE
↓
STATE CHANNELS
↓
CONTROL RELATIONSHIP
↓
AOE2 STRATEGIC PURPOSE
↓
FAILURE MODES
↓
AEGIS DESIGN LESSON
↓
AEGIS IMPLEMENTATION PATTERN
```

This is the most important pedagogical change recommended by this QC.

---

# 19. Evidence coverage assessment

| Dimension | Pass-8 status | QC judgment |
|---|---|---|
| Strategic framing | Strong | Preserve |
| Architecture | Strong | Preserve, tighten attribution |
| `.per` vocabulary | Good | Add exact mechanics |
| Historical source grounding | Moderate | Add anchors |
| Historical-vs-AEGIS separation | Moderate | Strengthen throughout |
| Worked strategic examples | Good | Add source traces |
| Actual `.per` examples | Weak | Major addition required |
| Search/optimization teaching | Good conceptually | Add literal trace |
| Resource/production reasoning | Strong | Add measurable variables |
| Combat lifecycle | Strong | Add exact anchors |
| Verification | Strong conceptually | Add executable patterns |
| Failure model | Strong AEGIS design | Separate historical evidence |
| State ownership | Strong AEGIS design | Add archaeology procedure |
| Performance engineering | Moderate | Add quantitative method |
| Lifecycle/initialization | Moderate | Add concrete failure example |
| Load order | Missing | Add |
| Validator/runtime discrepancy | Missing | Add |
| Opponent modeling | Moderate | Add observed vs predicted |
| Map/WHERE reasoning | Moderate | Add paired example |
| Strategic opportunity cost | Good | Deepen |
| Reader implementation readiness | Moderate | Major practical code pass required |

---

# 20. Final QC judgment

**Pass 8 succeeds as a strategic engineering primer. It does not yet fully succeed as the promised `.per` practical field manual.**

The conceptual architecture is now strong enough that the next revision should **stop expanding abstract theory** and spend its effort on executable evidence and implementation literacy.

The next practical pass should therefore be:

# PASS 9 — HISTORICAL CODE-TO-STRATEGY IMPLEMENTATION LAB

Target: take the eight highest-value mechanisms already identified in Layer 2 and teach each one from literal source code through strategic interpretation to AEGIS implementation.

Required eight labs:

1. Escrowed Castle/Imperial research
2. Contextual gatherer allocation
3. Production authorization
4. Threat classification → response
5. Candidate search/optimization
6. Scout path/waypoint selection
7. Attack → retreat → restart
8. Building placement → fallback/recovery

Each lab must contain:

`exact source anchor → literal code → rule trace → state ownership → strategic purpose → failure modes → evidence grade → AEGIS redesign → implementation pattern`.

Only after these labs are complete should the manual be considered ready for a final prose polish/QC cycle.

---

## Bottom line

The Masterclass now teaches **how to think about building an AoE2 controller**.

Pass 9 must teach the reader **how to open the `.per` file and actually build one**.

That is the remaining gap between “dense and understandable” and “professional field manual.”
