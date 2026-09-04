# AoE2DE Exact-Anchor Historical Trace Pack — Pass 10

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Predecessor:** `AOE2DE_HISTORICAL_CODE_TO_STRATEGY_LAB_PASS9_2026-09-04.md`  
**QC predecessor:** `AOE2DE_HISTORICAL_CODE_TO_STRATEGY_LAB_QC_PASS1_2026-09-04.md`  
**Purpose:** forensic extraction of the smallest useful historical `.per` slices, with literal source, exact anchors, state ownership, lifecycle, side effects, postconditions, and explicit separation from AEGIS design.  
**Status:** FORENSIC EXTRACTION / ACCEPT WITH LIMITATIONS  

> **Important source boundary:** the exact Promisory snippets in this pass were recovered from the project's ADPromisory reconstruction package. They are treated as source-bearing evidence for the named modules, but the package itself is not silently promoted to a pristine historical archive. Where the pristine verified package or exact HD source is unavailable in the extraction environment, the trace is explicitly marked `BLOCKED`, `PROVISIONAL`, or `CORROBORATED` rather than fabricated.

---

# 0. Forensic method

Pass 9 identified eight implementation windows. Pass 10 extracts the code where exact source is presently available.

Canonical trace:

`GAME PROBLEM → EXACT SOURCE → GUARDS → STATE READS → STATE WRITES → ACTION → RESET/RELEASE → POSTCONDITION → STRATEGIC INTERPRETATION → AEGIS TRANSLATION`

Evidence grades:

- **DIRECT:** exact executable source demonstrates the relationship.
- **COMPOSED:** multiple direct relationships are required to establish the larger chain.
- **INFERRED:** strategic meaning reconstructed from source behavior/context.
- **AEGIS-GENERALIZATION:** new AEGIS design derived from the pattern.
- **UNCERTAIN:** evidence is insufficient.

Anchor quality:

`EXACT | APPROXIMATE | MODULE-ONLY | NONE`.

A direct code excerpt below is not automatically evidence for every sentence surrounding it. The semantic claim is graded separately from the code itself.

---

# 1. Lab 1 — Escrowed Age Research

## 1.1 Exact source

**Module:** `escrow.per`  
**Anchor:** lines 24–40 in recovered ADPromisory source  
**Anchor quality:** EXACT for the recovered package  
**Mechanism:** escrow-gated age research

```text
; Research
;=============================================================
(defrule
	(up-compare-flag escrow-flag == 1)
	(can-research-with-escrow castle-age)
=>
	(research castle-age)
	;(chat-to-player every-ally text-advancing-castle); "I am advancing to the Castle Age."
	(chat-to-player my-player-number text-advancing-castle); "I am advancing to the Castle Age."
	(set-strategic-number sn-current-age fcastlea)
	(up-modify-sn sn-maximum-town-size c:min 14))
(defrule
	(up-compare-flag escrow-flag == 2)
	(can-research-with-escrow imperial-age)
=>
	(research imperial-age)
	;(chat-to-player every-ally text-advancing-imperial); "I am advancing to the Imperial Age."
	(chat-to-player my-player-number text-advancing-imperial); "I am advancing to the Imperial Age."
	(set-strategic-number sn-current-age imperial)
	(up-modify-sn sn-maximum-town-size c:min 18))
```

## 1.2 Literal rule trace

### Castle

1. `up-compare-flag escrow-flag == 1` reads escrow control state.
2. `can-research-with-escrow castle-age` is a live feasibility gate.
3. `research castle-age` invokes the research action.
4. `set-strategic-number sn-current-age fcastlea` writes controller-side age state.
5. `up-modify-sn sn-maximum-town-size c:min 14` modifies another strategic control variable.

### Imperial

1. `up-compare-flag escrow-flag == 2` selects the Imperial escrow mode.
2. `can-research-with-escrow imperial-age` checks feasibility.
3. `research imperial-age` invokes research.
4. `set-strategic-number sn-current-age imperial` writes controller-side age state.
5. `up-modify-sn sn-maximum-town-size c:min 18` modifies town-size control.

## 1.3 State ownership

| State | Role | Writer | Reader | Reset/lifecycle | Grade |
|---|---|---|---|---|---|
| `escrow-flag` | control selector | escrow subsystem | research rules | broader escrow lifecycle | DIRECT/COMPOSED |
| `sn-current-age` | strategic-number state | age research rule | downstream strategy/economy rules | overwritten by later age rules | DIRECT |
| `sn-maximum-town-size` | control parameter | multiple rules | economy/building systems | contextual | DIRECT |

## 1.4 What the code proves

**DIRECT:** escrow state can gate research through `can-research-with-escrow`; successful rule eligibility leads to a research action and strategic-state writes.

**DIRECT:** Castle and Imperial are represented by distinct escrow modes.

**NOT PROVEN:** the `sn-current-age` write is actual world-state completion verification.

**NOT PROVEN:** the same exact mechanism handles Dark→Feudal.

## 1.5 Strategic interpretation

**COMPOSED/INFERRED:** the programmer protects a strategic transition from unrestricted spending by routing the purchase through an escrow-aware feasibility condition.

The stronger statement “the programmer explicitly modeled opportunity cost” is not a literal source statement. It is an AEGIS interpretation of why reservation machinery is strategically useful.

## 1.6 AEGIS translation

`OBJECTIVE: AGE_TRANSITION`  
`REQUIREMENT: research feasible`  
`COMMITMENT: reserve required resources`  
`AUTHORITY: transition owner may consume reservation`  
`ACTION: research`  
`VERIFY: pending + actual current-age state`  
`FAILURE: resource diversion / prerequisite failure / action failure / transition mismatch`

The explicit authority object is **AEGIS-GENERALIZATION**, not historical source terminology.

---

# 2. Lab 2 — Contextual Gatherer Allocation

## 2.1 Exact source

**Module:** `gatherers.per`  
**Anchor:** lines 32–65 in recovered ADPromisory source  
**Anchor quality:** EXACT for the recovered package  
**Mechanism:** contextual resource-allocation regime

```text
(defrule
	(strategic-number sn-current-age >= dfeudal)
(or	(and	(research-available castle-age)
		(current-age-time >= 90))
(or	(building-type-count-total blacksmith >= 1)
(or	(building-type-count-total market >= 1)
	(building-type-count-total archery-range >= 1))))
=>
	(set-goal temporary-goal10 985795))
(defrule
	(goal temporary-goal10 985795)
=>
	(set-strategic-number sn-wood-gatherer-percentage  44)
	(set-strategic-number sn-food-gatherer-percentage  55)
	(set-strategic-number sn-gold-gatherer-percentage   1)
	(set-strategic-number sn-stone-gatherer-percentage  0))
(defrule
	(strategic-number sn-current-age >= feudal)
	(goal temporary-goal10 985795)
(or	(building-type-count-total mining-camp >= 1)
	(dropsite-min-distance gold s:<= sn-maximum-gold-drop-distance))
=>
	(set-strategic-number sn-wood-gatherer-percentage  40)
	(set-strategic-number sn-food-gatherer-percentage  57)
	(set-strategic-number sn-gold-gatherer-percentage   3)
	(set-strategic-number sn-stone-gatherer-percentage  0))
```

## 2.2 Literal trace

`age/resource/building context`
→ `set-goal temporary-goal10 985795`
→ subsequent rule sees `goal temporary-goal10 985795`
→ writes 44/55/1/0 allocation
→ a later condition can overwrite with 40/57/3/0.

The exact values matter because they prove that the historical controller did not merely carry a static gather template.

## 2.3 State classification

`temporary-goal10` is **not automatically “scratch.”** In this slice it is a persistent-looking regime selector until its lifecycle is traced.

| State | Type | Role | Grade |
|---|---|---|---|
| `temporary-goal10` | GOAL CHANNEL | regime marker | DIRECT |
| `sn-wood-gatherer-percentage` | SN | resource allocation output | DIRECT |
| `sn-food-gatherer-percentage` | SN | resource allocation output | DIRECT |
| `sn-gold-gatherer-percentage` | SN | resource allocation output | DIRECT |
| `sn-stone-gatherer-percentage` | SN | resource allocation output | DIRECT |

## 2.4 What the code proves

**DIRECT:** contextual conditions select a regime that writes concrete gatherer percentages.

**DIRECT:** later conditions can alter those percentages.

**INFERRED:** the aggregate mechanism behaves like feedback control.

**NOT PROVEN:** a unified demand forecast or explicit marginal-value optimizer.

## 2.5 Strategic meaning

The programmer is making villagers solve a changing resource constraint. That is a stronger statement than “the AI has an economy template,” but the exact strategic objective of every ratio remains rule-specific.

## 2.6 AEGIS translation

`RAW_STOCK → COMMITTED_STOCK → NEAR_TERM_DEMAND → RESOURCE_DEFICIT → ALLOCATION`

The explicit demand/commitment model is AEGIS-GENERALIZATION.

---

# 3. Lab 3 — Production Control

## 3.1 Exact source available

**Module:** `escrow.per`  
**Anchor:** lines 635–644 in recovered ADPromisory source  
**Anchor quality:** EXACT for recovered package  
**Mechanism:** escrow-gated production

```text
(defrule
	(up-compare-flag escrow-flag2 == 8388608)
	(can-train-with-escrow mangonel-line)
=>
	(train mangonel-line))
;=============================================================
(defrule
	(up-compare-flag escrow-flag2 == 33554432)
	(can-train-with-escrow monk)
=>
	(train monk))
```

## 3.2 Literal trace

`escrow-flag2`
→ `can-train-with-escrow`
→ `train`

This is a cleaner historical example of conditional production permission than the absent `units.per` extraction in the current package.

## 3.3 Evidence limitation

The project's pristine historical Promisory inventory included `units.per`, but that file is not present in the recovered ADPromisory extraction used for this pass. Therefore this pass **does not fabricate a units.per trace**.

Status:

`units.per exact production slice = BLOCKED`.

## 3.4 What the available code proves

**DIRECT:** production can be gated through escrow-specific feasibility and then train.

**COMPOSED:** production control is distributed through goals/flags/feasibility and action rules.

**NOT PROVEN:** a universal historical “production authority plane.”

## 3.5 AEGIS translation

Historical:

`CONTROL STATE → LIVE FEASIBILITY → TRAIN`

AEGIS:

`OBJECTIVE → REQUIREMENT → CANDIDATE → PRODUCTION AUTHORITY → CAN-TRAIN → TRAIN → VERIFY`

The authority-plane terminology is AEGIS design.

---

# 4. Lab 4 — Threat Classification / Aggregation

## 4.1 Exact source

**Module:** `threats.per`  
**Anchor:** lines 618–634 in recovered ADPromisory source  
**Anchor quality:** EXACT for recovered package  
**Mechanism:** enemy unit-family measurement and accumulation

```text
(defrule
	(strategic-number sn-target-player-number > 0)
=>
	(up-get-focus-fact unit-type-count war-wagon-line temporary-goal)
	(up-modify-sn cavarchers g:+ temporary-goal)
	(up-get-focus-fact unit-type-count cavalry-archer-line temporary-goal)
	(up-modify-sn cavarchers g:+ temporary-goal)
	(up-get-focus-fact unit-type-count mangudai-line temporary-goal)
	(up-modify-sn cavarchers g:+ temporary-goal)
	(up-get-focus-fact unit-type-count elephant-archer temporary-goal)
	(up-get-focus-fact unit-type-count elite-elephant-archer temporary-goal8)
	(up-modify-goal temporary-goal g:+ temporary-goal8)
	(up-modify-goal temporary-goal c:* 2)
	(up-modify-goal temporary-goal c:max 0)
	(up-modify-sn cavarchers g:+ temporary-goal)
	(up-get-focus-fact unit-type-count camel-archer temporary-goal)
	(up-modify-goal temporary-goal c:max 0)
	(up-modify-sn cavarchers g:+ temporary-goal))
```

## 4.2 Literal trace

1. `sn-target-player-number > 0` establishes target context.
2. `up-get-focus-fact` measures concrete enemy unit families.
3. results are accumulated into `cavarchers`.
4. temporary values are clamped/combined before addition.

## 4.3 Critical semantic correction

The code proves **measurement and aggregation**.

It does not, in this slice, prove:

`measurement → normalized threat score → counter selection`.

Therefore the historical semantic categories must remain separate:

`MEASUREMENT ≠ AGGREGATION ≠ CLASSIFICATION ≠ PRIORITY ≠ RESPONSE`.

## 4.4 State ownership

| State | Role | Writer | Reader | Grade |
|---|---|---|---|---|
| `sn-target-player-number` | target context | target-selection subsystem | threat measurement | DIRECT |
| `temporary-goal` | measurement scratch/accumulator | threat rule | threat calculations | DIRECT |
| `cavarchers` | aggregated threat-related SN | threat rule | downstream threat consumers | DIRECT |

Whether `temporary-goal` is truly scratch across the complete module requires lifecycle tracing.

## 4.5 Strategic interpretation

**DIRECT:** the programmer wants a compact representation of enemy military composition.

**INFERRED:** that representation exists to enable threat-sensitive strategic decisions.

**UNCERTAIN until consumer trace:** exactly which counter or strategic change follows.

## 4.6 AEGIS translation

`OBSERVE enemy composition`
→ `CLASSIFY capability family`
→ `BELIEF/confidence`
→ `DERIVE counter-requirement`
→ `GENERATE responses`
→ `EVALUATE`
→ `COMMIT`.

Only the first measurement/aggregation portion is directly inherited from this slice.

---

# 5. Lab 5 — Candidate Search / Optimization-Like Loop

## 5.1 Exact source

**Module:** `general.per`  
**Anchor:** lines 17–75 in recovered ADPromisory source  
**Anchor quality:** EXACT for recovered package  
**Mechanism:** bounded candidate search over local villagers

```text
(defrule
	(goal landnomad yes)
=>
	(up-full-reset-search)
	(up-find-local c: villager-class c: 6)
	(up-get-search-state local-total)
	(up-modify-goal temporary-goal3 g:= local-last)
	(up-modify-goal temporary-goal6 g:= local-last)
	(up-modify-goal temporary-goal6 c:- 1)
	(set-goal temporary-goal4 0)
	(set-goal temporary-goal5 0)
	(set-goal temporary-goal2 -1)
	(set-goal temporary-goal3 0)
	(set-goal temporary-goal5 0)
	(disable-self))
(defrule
	(goal landnomad yes)
	(up-compare-goal temporary-goal6 > 0)
	(up-compare-goal temporary-goal4 g:< local-last)
	(up-compare-goal temporary-goal5 g:< local-last)
=>
	(up-set-target-object search-local g: temporary-goal4)
	(up-get-point position-object point-x)
	(up-set-target-object search-local g: temporary-goal5)
	(up-get-point position-object saved-point-x)
	(up-get-point-distance point-x saved-point-x temporary-goal)
	(up-modify-goal temporary-goal5 c:+ 1))
(defrule
	(goal landnomad yes)
	(up-compare-goal temporary-goal6 > 0)
	(up-compare-goal point-x > 0)
	(up-compare-goal saved-point-x > 0)
	(up-compare-goal temporary-goal g:> temporary-goal2)
=>
	(up-modify-goal temporary-goal2 g:= temporary-goal)
	(up-modify-goal 504 g:= temporary-goal4)
	(up-modify-goal 505 g:= temporary-goal5)
	(up-modify-goal 505 c:- 1))
(defrule
	(goal landnomad yes)
	(up-compare-goal temporary-goal3 > 0)
=>
	(up-modify-goal temporary-goal3 c:- 1)
	(up-jump-rule -3))
(defrule
	(goal landnomad yes)
	(up-compare-goal temporary-goal6 > 0)
=>
	(up-modify-goal temporary-goal4 c:+ 1)
	(set-goal temporary-goal5 0)
	(up-modify-goal temporary-goal3 g:= local-last)
	(up-modify-goal temporary-goal6 c:- 1)
	(up-jump-rule -4))
```

## 5.2 Literal algorithm

### Initialization

`up-full-reset-search` clears prior search state.

`up-find-local ...` creates the candidate population.

`up-get-search-state local-total` obtains the available count.

The code then initializes candidate indices and the best-distance sentinel.

### Candidate evaluation

The loop selects candidate objects by index, retrieves their points, calculates distance, and increments the candidate index.

### Best preservation

If the measured distance is greater than the stored best sentinel, the code writes the current indices into goals 504/505.

### Iteration

`temporary-goal3` and `temporary-goal6` act as counters; `up-jump-rule -3` and `-4` re-enter earlier rules.

## 5.3 Important semantic caution

The historical code is **optimization-like**, not proof of a generic optimizer abstraction.

It implements a distributed stateful search using goals, search primitives, rule eligibility and jumps.

## 5.4 Search invariant

At every iteration:

`candidate set must correspond to the current reset/search state`.

This makes `up-full-reset-search` a correctness boundary, not a cosmetic preparation step.

## 5.5 Failure modes

- stale search state;
- wrong candidate index;
- wrong best-value initialization;
- wrong jump destination;
- premature counter exhaustion;
- best candidate overwritten by a worse candidate;
- search state surviving into an unrelated search.

## 5.6 AEGIS translation

`RESET → GENERATE CANDIDATES → MEASURE → COMPARE → PRESERVE BEST → ADVANCE → REPEAT → TERMINATE → CONSUME BEST`.

The historical implementation remains primitive-specific; AEGIS may encapsulate the pattern.

---

# 6. Lab 6 — Scout Group / Path Safety / Waypoint Selection

## 6.1 Exact source

**Module:** `scoutcontrol.per`  
**Anchor:** lines 128–205 and 196–205 for path-analysis block  
**Anchor quality:** EXACT for recovered package  
**Mechanism:** group construction and path-safety analysis

```text
;Create group
(defrule
   (goal modern-scout-micro yes)
   (unit-type-count scout-cavalry-line > 1)
   (strategic-number sn-five-turns == 2)
=>
   (up-full-reset-search)
   (up-find-local c: scout-cavalry-line c: 40)
   (up-set-target-point scout-group-x)
   (up-clean-search search-local object-data-distance search-order-asc)
)

(defrule
   (goal modern-scout-micro yes)
   (unit-type-count scout-cavalry-line > 1)
   (strategic-number sn-five-turns == 2)
   (up-set-target-object search-local c: 0)
=>
   (up-get-point position-object point-x)
   (up-set-target-point point-x)
   (up-full-reset-search)
   (up-filter-distance c: -1 c: 7)
   (up-find-local c: scout-cavalry c: 40)
   (up-modify-group-flag 0 c: 12)
   (up-reset-group c: 12)
   (up-create-group 0 0 c: 12)
   (up-modify-group-flag 1 c: 12)
)

;Analyze path to group to make sure it is safe
;We break it down into four quartersteps and analyze whether there is a TC, a massive group of spears/archers, a castle
(defrule
   (goal modern-scout-micro yes)
   (up-group-size c: 12 > 3)
   (strategic-number sn-twenty-turns == 12)
=>
   (up-full-reset-search)
   (set-goal temporary-goal 20)
   (set-strategic-number sn-focus-player-number 1)
   (set-goal remote-total 0)
   (set-goal temporary-goal3 0)
)

(defrule
   (strategic-number sn-twenty-turns == 12)
   (goal modern-scout-micro yes)
   (up-group-size c: 12 > 3)
   (player-valid focus-player)
   (players-stance focus-player enemy)
   (up-compare-goal temporary-goal < 100)
   (strategic-number sn-focus-player-number <= max-players)
   (up-compare-goal remote-total < 1)
   (up-compare-goal temporary-goal3 < 1)
=>
   (up-full-reset-search)
   (up-bound-point point-x position-self-x)
   (up-lerp-percent point-x enemy-x g: temporary-goal)
   (up-filter-distance c: -1 c: 9)
   (up-find-remote c: archer c: 25)
   (up-get-search-state local-total)
   (up-modify-goal remote-total c:- 10)
   (up-modify-goal remote-total c:max 0)
   (up-modify-goal temporary-goal3 g:max remote-total)
   (up-find-remote c: spearman-line c: 1)
   (up-find-remote c: town-center c: 1)
   (up-find-remote c: castle c: 1)
   (up-get-search-state local-total)
)
```

## 6.2 Literal trace

`scout count + timer`
→ reset local search
→ find scouts
→ clean/sort candidate objects
→ create group
→ reset path search
→ define point/path interval
→ inspect remote enemy objects
→ aggregate danger indicators.

The comments themselves are unusually strong programmer-intent evidence, but they are still comments; executable behavior must be traced separately.

## 6.3 What is directly demonstrated

- scout-group construction;
- object filtering;
- group lifecycle initiation;
- path interpolation;
- local/remote object searches;
- inspection for archer, spear, TC and castle presence;
- persistent state in goals.

## 6.4 What is not directly demonstrated

`safe route = maximum information value` is not proven.

The historical slice is much more directly about **route safety / tactical geometry** than an explicit value-of-information optimizer.

## 6.5 AEGIS translation

Separate two objectives:

`ROUTE SAFETY`

and

`INFORMATION VALUE`.

Only the first is historically demonstrated here.

---

# 7. Lab 7 — Attack / Retreat / Restart

## 7.1 Historical exact-anchor status

**Primary source:** verified `AI (HD version).per`  
**Exact source bytes:** not currently present in the extraction workspace for this pass.  
**Known prior anchor:** attack/retreat logic around approximately lines 32578–32595.  
**Anchor quality:** APPROXIMATE.  
**Status:** PROVISIONAL — no invented source excerpt.

The project evidence establishes that the historical HD source contains state around:

- `attack-goal`;
- `attack-status-goal`;
- `retreat-now-goal`;
- attack/retreat timers;
- clearing `attack-goal`;
- reset state;
- `restart-attack-goal`;
- enemy-fortification state.

A later independently surfaced copy of the AI scripting source also exposes the documented meanings of these channels, including `retreat-now-goal`, `attack-status-goal`, `enemy-fortifications-goal`, and `restart-attack-goal`. This is **secondary corroboration**, not substitution for the verified historical source.

## 7.2 What can safely be asserted

**DIRECT/previously established:** controller-state transitions exist for attack, retreat, reset and restart.

**NOT YET EXACT:** the complete contiguous source slice linking every writer, reader, timer, resetter and physical command.

## 7.3 Required Pass-10 continuation

Extract:

`writer of retreat-now-goal`
→ `reader`
→ `attack-goal clear`
→ `attack-status-goal`
→ `retreat timer`
→ `up-retreat-now` or equivalent
→ `restart-attack-goal`
→ `restart consumer`.

Do not promote “physical disengagement” from controller state alone.

## 7.4 Strategic interpretation

`retreat as preservation of future military capability` remains INFERRED.

`attack controller is temporal/stateful` is COMPOSED and strong.

---

# 8. Lab 8 — Building Placement / Fallback

## 8.1 Exact source

**Module:** `buildings.per`  
**Anchor:** lines 213–230 in recovered ADPromisory source  
**Anchor quality:** EXACT for recovered package  
**Mechanism:** primary TC build path plus secondary fallback

```text
(defrule
	(up-pending-objects c: town-center <= 0)
	(building-type-count-total town-center < 1)
(or	(players-military-population every-ally <= 0)
	(not	(player-in-game any-ally)))
	(game-time >= 600); no nomad
	(can-build town-center)
=>
	(set-strategic-number sn-placement-to-center 1);test
	(set-strategic-number sn-allow-adjacent-dropsites 1)
	(set-strategic-number sn-dropsite-separation-distance 2); 3
	(up-assign-builders c: town-center-foundation c: 1)
	(set-strategic-number sn-town-center-placement 0)
	(up-set-placement-data my-player-number -1 c: market-neg-dist); -50)
	(up-build place-control 0 c: town-center))

;Secondary backup for rebuilds - regular system occasionally fails (TODO: have up-build-line as primary backup)

(defrule
	(game-time > 600)
	(building-type-count-total town-center < 1)
	(timer-triggered two-mins)
	(up-pending-objects c: town-center < 1)
	(can-build town-center)
=>
	(build town-center)
)
```

## 8.2 Literal trace

### Primary path

1. no pending TC;
2. no completed TC;
3. ally/mode condition permits construction;
4. time constraint passes;
5. `can-build town-center` passes;
6. placement parameters are configured;
7. builders are assigned;
8. placement/build operation is invoked.

### Backup path

1. time passes;
2. TC still absent;
3. two-minute timer fires;
4. no pending TC;
5. `can-build town-center` passes;
6. simpler `build town-center` action fires.

## 8.3 Failure evidence

The comment explicitly identifies the primary mechanism as occasionally failing and supplies a backup.

This is one of the strongest direct pieces of evidence in the entire archaeology set for the programmer engineering against runtime failure.

## 8.4 Postcondition distinction

The command:

`up-build place-control ... town-center`

is a **COMMAND/CONTROL POSTCONDITION**.

The later observation:

`building-type-count-total town-center >= 1`

is a **WORLD-STATE POSTCONDITION**.

The strategic postcondition would be:

`TC capability restored / economic function recovered`.

That final claim requires further state/capability evidence.

## 8.5 AEGIS translation

`PRIMARY CANDIDATE`
→ `FEASIBILITY`
→ `EXECUTE`
→ `VERIFY WORLD STATE`
→ if failed:
`ALTERNATE PATH`
→ `VERIFY`
→ `REASSESS`.

Historical fallback is DIRECT; generalized recovery taxonomy is AEGIS-GENERALIZATION.

---

# 9. Cross-lab state ownership ledger

| Lab | Primary state | Historical semantic type | Owner status | Evidence |
|---|---|---|---|---|
| 1 | `escrow-flag` | control selector | distributed escrow subsystem | DIRECT/COMPOSED |
| 1 | `sn-current-age` | strategic state | distributed | DIRECT |
| 2 | `temporary-goal10` | regime marker | lifecycle not fully isolated | DIRECT/UNCERTAIN |
| 2 | gatherer-percentage SNs | economic control outputs | gatherer subsystem + readers | DIRECT |
| 3 | `escrow-flag2` | production/research selector | escrow subsystem | DIRECT |
| 4 | `cavarchers` | threat aggregate | threat subsystem | DIRECT |
| 4 | `sn-target-player-number` | target context | target-selection subsystem | DIRECT |
| 5 | goals 504/505 | best-candidate indices | search routine | DIRECT |
| 5 | `temporary-goal2/3/4/5/6` | counters / accumulators | search routine | DIRECT |
| 6 | `scout-group-*` | group/path state | scout controller | DIRECT |
| 6 | `temporary-goal3` | path-analysis counter | scout controller | DIRECT |
| 8 | `sn-town-center-placement` | placement control | building subsystem | DIRECT |
| 8 | pending TC state | execution/pending observation | engine/building interaction | DIRECT |

**Important:** ownership means lifecycle responsibility, not merely “the file contains the writer.” Where competing writers/resetters are not fully traced, ownership remains distributed/ambiguous.

---

# 10. Historical vs AEGIS semantic separation

| Concept | Historical evidence in this pass | AEGIS treatment |
|---|---|---|
| Observation | facts/search/unit counts | typed observation objects |
| Classification | threat/resource/group categories | explicit classifiers |
| Belief | distributed persistent interpretations, not universal object | confidence-bearing belief state |
| Requirement | implicit in guards/control conditions | explicit requirement derivation |
| Commitment | strongest direct example is escrow/control reservation | explicit commitment contract |
| Authority | historical control/permission effects | separate authority plane |
| Action | direct `.per` actions | side-effect executor |
| Verification | some state/pending checks; not universal | command/world/operational/strategic postconditions |
| Recovery | direct fallback exists in building code | generalized failure/recovery taxonomy |
| Reassessment | repeated rule eligibility/state changes | explicit reassessment triggers |

---

# 11. “Read the rule backwards” worked examples

## 11.1 Building fallback

Start at:

`(build town-center)`

Backwards:

`build`
← `can-build`
← `pending == 0`
← `TC count < 1`
← `two-mins timer`
← `game-time > 600`.

Then ask:

`Who writes pending state?`

`Who creates TC count?`

`What happens if build command succeeds but foundation never completes?`

The historical code supplies some of the answers but not all. The unresolved edges become explicit research tasks.

## 11.2 Search

Start at:

`best candidate write to 504/505`

Backwards:

`best write`
← `distance > stored best`
← `candidate point retrieval`
← `candidate index`
← `search-local`
← `up-full-reset-search`.

Then forward:

`best candidate`
→ downstream consumer
→ actual building/placement action.

The convergence point is the consumer. If backward and forward traces do not meet, the state interpretation is incomplete.

---

# 12. Performance audit

Historical `.per` search cost must be treated as an engineering variable.

For every search trace record:

`entry frequency | candidate count | iterations | search resets | jump iterations | early exit | worst-case path | downstream action`.

### Pass-10 current evidence

- Search primitives are demonstrably used.
- Explicit candidate counters are demonstrably used.
- Explicit resets are demonstrably used.
- Jump-based iteration is demonstrably used.
- Exact runtime cost has **not** been measured here.

Therefore:

`qualitative performance risk = DIRECT`

`quantitative historical complexity = UNKNOWN`.

Do not invent a complexity number from source length alone.

---

# 13. Falsifier register

| Claim | Current grade | Falsifier |
|---|---|---|
| Escrow gates age research | DIRECT | exact source lacks gate/action relationship |
| Gatherer allocation is contextual | DIRECT | same percentages prove invariant/static behavior across all contexts |
| `temporary-goal10` is scratch-only | UNCERTAIN | persistent reader/writer lifecycle outside selected slice |
| Threat code performs enemy measurement | DIRECT | source interpretation of `up-get-focus-fact` contradicts measurement semantics |
| Threat code performs complete counter selection | UNCERTAIN | no downstream response consumer |
| Search code is optimization-like | COMPOSED | no candidate comparison/best-preservation chain in full trace |
| Scout path code is safety-oriented | DIRECT/INFERRED | executable consumer shows path analysis serves unrelated purpose |
| Retreat controller is stateful | COMPOSED | full source shows single-shot stateless command with no lifecycle |
| Building system engineers around failure | DIRECT | backup comment/path is inactive historical artifact only |
| Generic recovery taxonomy is historical | AEGIS-GENERALIZATION | source reveals unified historical taxonomy |

---

# 14. Evidence coverage after Pass 10

| Requirement | Status |
|---|---|
| Exact source excerpt | **6/8 strong; 2/8 blocked/provisional** |
| Exact anchors | **6/8 exact; 2/8 approximate/blocked** |
| Complete rule trace | **6/8 substantially traced** |
| Writer/reader map | **partial; full lifecycle remains open** |
| Reset/release trace | **strong for search/build/scout; incomplete elsewhere** |
| Historical postcondition | **partial** |
| Failure/recovery | **strong for building; incomplete elsewhere** |
| Historical-vs-AEGIS split | **8/8** |
| Alternative explanations | **8/8 frameworked** |
| Falsifiers | **8/8 frameworked** |
| Performance note | **8/8 qualitative; quantitative incomplete** |
| Pass-7 linkage | **conceptual; edge IDs should be attached in next provenance revision** |
| Source-state graph linkage | **conceptual; exact IDs should be attached next** |

The score is intentionally not rounded upward.

---

# 15. Pass-10 findings

## Finding P10-01 — Exact source changes the quality of the archaeology

**DIRECT observation:** the escrow, gatherer, threat, search, scout, and building mechanisms become substantially more informative when their literal syntax is visible.

**Consequence:** future Layer-2 research should prefer bounded source slices over broad prose summaries.

## Finding P10-02 — Intermediate state is the common implementation language

Across the exact slices, the programmer repeatedly uses:

`flags → goals → strategic numbers → search state → pending state → groups → timers`.

This is **COMPOSED** evidence for an intermediate-state architecture.

## Finding P10-03 — Search is an actual programming technique, not merely an API call

The `general.per` slice demonstrates initialization, candidate iteration, measurement, comparison, best preservation, decrement, and jump re-entry.

This is one of the strongest implementation lessons recovered so far.

## Finding P10-04 — Failure-aware engineering is directly visible

The building fallback comment and secondary path demonstrate that the historical programmer expected the primary mechanism to fail sometimes and designed around it.

## Finding P10-05 — Semantic compression is the main archaeology hazard

The largest risk is turning:

`measurement`
into
`belief`,

`control flag`
into
`authority`,

`research command`
into
`transition complete`,

`search loop`
into
`generic optimizer`,

or
`fallback rule`
into
`universal recovery architecture`.

Pass 10 should therefore become the project's semantic firewall between source and AEGIS design.

---

# 16. What remains blocked

### B1 — Pristine `units.per` exact extraction

The recovered package used for this pass lacks `units.per` despite the historical Promisory inventory containing it.

**Action:** recover from the pristine verified Promisory archive before closing Lab 3.

### B2 — Pristine HD attack/retreat exact extraction

The historical HD source is verified by project provenance but its exact bytes were not available in this extraction workspace.

**Action:** recover the exact verified `AI (HD version).per` and extract the contiguous attack/retreat/restart slice.

### B3 — Downstream threat consumer

The cavalry-archer aggregation is exact, but its complete downstream response chain has not yet been traced.

**Action:** identify every reader of `cavarchers` and follow the first concrete response.

### B4 — Search consumer

The best-candidate state is exact, but the complete downstream consumer must be traced to establish the game-level purpose of this particular search.

### B5 — Scout waypoint consumer

The safety-analysis slice is exact; the final waypoint/action consumer remains to be connected.

---

# 17. Canonical Pass-10 doctrine

From this point forward, no historical subsystem should be promoted to implementation guidance unless it can answer:

1. **What exact code fires?**
2. **What exact facts/values does it read?**
3. **What exact state does it write?**
4. **Who reads that state?**
5. **Who resets or replaces it?**
6. **What side effect does it invoke?**
7. **What proves that side effect actually happened?**
8. **What game-state relationship was changed?**
9. **What alternative explanation fits the same code?**
10. **What would falsify the interpretation?**
11. **What performance cost does the mechanism impose?**
12. **What part is historical and what part is AEGIS invention?**

That is the implementation-grade standard.

---

# 18. Final disposition

**PASS 10 — ACCEPT WITH LIMITATIONS.**

### Quality

- Historical source fidelity: **HIGH where exact recovered slices are shown**
- Forensic reproducibility: **HIGH for six extracted mechanisms**
- Literal `.per` literacy: **HIGHER than Pass 9**
- Strategic interpretation: **HIGH, but explicitly graded**
- State ownership: **IMPROVED / still incomplete**
- Lifecycle tracing: **PARTIAL**
- Runtime verification: **PARTIAL**
- Quantitative performance: **OPEN**
- Canonical implementation readiness: **NOT YET**

### The decisive improvement

Pass 9 taught:

> “Here are the historical mechanisms and how to think about them.”

Pass 10 begins teaching:

> “Here is the actual code, here is exactly what it reads and writes, here is how it iterates, and here is where our knowledge stops.”

That is the correct progression.

### Next pass

**Pass 11 — Cross-Lab Provenance Closure / Consumer Tracing**

The next objective is not more new theory. It is to close the open edges:

`STATE WRITER → EVERY READER → FIRST STRATEGIC CONSUMER → ACTION → WORLD-STATE POSTCONDITION`.

Priority order:

1. `cavarchers` threat consumers;
2. search best-candidate consumers;
3. scout path/waypoint consumer;
4. exact HD attack/retreat/restart slice;
5. pristine `units.per` production slice;
6. escrow release/reset lifecycle;
7. gatherer regime lifecycle.

Only after those edges close should the eight labs be promoted toward a canonical Layer-2 implementation manual.
