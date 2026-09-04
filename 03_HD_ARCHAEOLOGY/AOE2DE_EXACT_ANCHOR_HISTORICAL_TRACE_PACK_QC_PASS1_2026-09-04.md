# AoE2DE Exact-Anchor Historical Trace Pack — Deep QC Pass 1

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Target:** `AOE2DE_EXACT_ANCHOR_HISTORICAL_TRACE_PACK_PASS10_2026-09-04.md`  
**Predecessors:** Pass-9 implementation lab + Pass-9 QC + Pass-8 masterclass QC + Pass-7 evidence-edge QC  
**Status:** **DEEP QC / ACCEPT WITH CORRECTIONS**  
**Primary evidence boundary:** verified historical source hierarchy; exact snippets in Pass 10 are explicitly identified as recovered ADPromisory reconstruction evidence where applicable.  
**Runtime boundary:** current DE execution semantics remain Layer-1 territory; Layer 1 remains frozen at 89%.

---

# 0. Executive verdict

Pass 10 is a **major improvement** over Pass 9. It does what the previous QC demanded: it introduces literal `.per` source, exact anchors for six recovered modules, rule-by-rule traces, explicit blocked/provisional states, and a stronger historical-vs-AEGIS firewall.

The artifact is **not yet canonical**.

The remaining problems are now narrower and more technical. The most important are:

1. the source package is a reconstructed ADPromisory package, so “exact” must always mean **exact within that package**, not pristine-historical proof;
2. several state-ownership declarations still outrun the demonstrated writer/reader/resetter evidence;
3. the search lab contains a potentially material semantic error: the shown comparison is `measured distance > stored value`, so calling the selected value a generic “best distance” is unsafe until the downstream objective is proven;
4. the search trace does not yet establish that goals 504/505 are actually consumed by the action that motivated the lab;
5. the threat lab proves measurement/aggregation, but not classification or response;
6. the scout lab proves group/path-safety machinery, but not final waypoint/action consequence;
7. the building fallback proves an explicit backup path, but the actual runtime failure boundary and completion verification remain open;
8. the age-research trace still risks implying that the `sn-current-age` write is a postcondition, despite correctly warning against that elsewhere;
9. the document's quantitative evidence-coverage table is a useful accounting device but should not be mistaken for measured completeness of the underlying causal graph;
10. Pass 10 itself contains enough evidence to identify the exact work for Pass 11, so another broad conceptual pass would now be inferior to downstream-consumer tracing.

**Disposition: ACCEPT WITH CORRECTIONS. Do not promote to canonical Layer-2 implementation manual yet.**

---

# 1. Audit standard

The canonical historical trace should be:

`GAME PROBLEM → SOURCE PACKAGE → EXACT MODULE/ANCHOR → EXACT RULE → READS → WRITES → SIDE EFFECT → IMMEDIATE READERS → RESET/RELEASE → WORLD-STATE OBSERVATION → STRATEGIC CONSEQUENCE`

Then separately:

`HISTORICAL EVIDENCE → INTERPRETATION → AEGIS GENERALIZATION`.

The following dimensions must remain independent:

- source provenance;
- executable syntax;
- engine primitive semantics;
- controller-state semantics;
- game-world consequence;
- strategic interpretation;
- AEGIS design.

This is consistent with the project archaeology standard that the logical architecture is reconstructed from distributed goals, strategic numbers, timers, escrow, production flags, search state, DUC state and modules, rather than assumed to be a clean object model. fileciteturn296file0L2-L2

---

# 2. Critical findings

## P10-QC-01 — “Exact” is package-exact, not necessarily historical-exact

**Severity: CRITICAL**

Pass 10 explicitly says its Promisory snippets were recovered from the ADPromisory reconstruction package and refuses to silently promote that package to a pristine archive. This is correct. fileciteturn308file0L2-L2

However, the lab headings repeatedly say `Exact source` and `Anchor quality: EXACT`. The qualifier “for recovered package” is present, but it must become impossible to miss.

### Required correction

Use a two-axis provenance label:

`SOURCE FIDELITY = EXACT WITHIN RECOVERED PACKAGE`

`HISTORICAL ARCHIVAL STATUS = VERIFIED / RECONSTRUCTED / UNKNOWN`

Do not allow a reader to interpret `EXACT` as “proven to be byte-identical to the pristine historical archive.”

**Status:** BLOCKS canonical provenance, not the research itself.

---

## P10-QC-02 — Pass 10 needs a source-package identifier/hash per lab

**Severity: HIGH**

The document identifies the package class but does not give a package-level immutable identifier for each exact extraction.

### Required correction

Add:

`PACKAGE ID | PACKAGE HASH | MODULE HASH | SOURCE PATH | LINE RANGE`.

If a package hash is unavailable, say `UNKNOWN`; never manufacture one.

This is especially important because the project has multiple Promisory/ADPromisory revisions.

---

## P10-QC-03 — “Successful rule eligibility leads to a research action” is semantically awkward

**Severity: HIGH**

In the age lab, the rule becoming eligible results in the `research` action being invoked. That is not the same as research success.

The Pass 10 document correctly says the subsequent `sn-current-age` write is not proof of completion, but the phrase “successful rule eligibility” still invites command-success confusion. fileciteturn308file0L2-L2

### Required correction

Use:

`RULE ELIGIBLE → ACTION INVOCATION → CONTROLLER STATE WRITE`

and reserve:

`ACTION SUCCESS / WORLD-STATE COMPLETION`

for independently observed completion evidence.

---

## P10-QC-04 — The age trace needs a completion-state edge, not merely a warning

**Severity: HIGH**

The canonical trace includes postcondition verification, but Lab 1 stops before the postcondition.

### Required correction

Search for the historical consumer(s) of `sn-current-age` and for actual age-state predicates. Determine whether the program intentionally predicts the transition, mirrors it, or confirms it.

The distinction is strategically significant: a controller can maintain an expected state ahead of the engine's completed state.

---

# 3. Lab 1 — Escrowed Age Research

## P10-QC-05 — Escrow mode values need semantic provenance

**Severity: MEDIUM**

`escrow-flag == 1` and `escrow-flag == 2` are accurately copied, but the lab treats them as “Castle mode” and “Imperial mode” without tracing the writers of those flag values.

The local rule proves the **reader meaning** in this context, not the complete lifecycle of the flag.

### Required correction

Trace:

`escrow-flag writer → value assignment → research reader → reset/replacement`.

---

## P10-QC-06 — `sn-current-age` ownership is still overstated

**Severity: MEDIUM**

The ownership table calls it “strategic-number state” and “overwritten by later age rules,” but a full writer set has not been demonstrated.

### Required correction

Change ownership to:

`OWNER STATUS = DISTRIBUTED / PARTIAL TRACE`

until all writers and resetters are enumerated.

This follows the project's state-channel standard: a file containing a writer does not establish sole ownership. fileciteturn296file0L2-L2

---

## P10-QC-07 — `sn-maximum-town-size` is a side-effect worth tracing, not a footnote

**Severity: MEDIUM**

The age rule does more than research: it changes `sn-maximum-town-size` to minimum 14 or 18.

This is potentially valuable evidence of the programmer coupling age transition to town-size/economic capacity.

### Required correction

Trace its immediate readers and determine whether the age transition is changing:

`population policy | villager production | housing | expansion | another control variable`.

Do not leave this strategic consequence unexamined.

---

# 4. Lab 2 — Contextual Gatherer Allocation

## P10-QC-08 — The regime trigger is not yet fully interpreted

**Severity: HIGH**

The trigger combines:

- age;
- Castle research availability and time;
- blacksmith;
- market;
- archery range.

The artifact correctly calls this contextual, but it does not yet determine whether these are alternative markers of a single strategic regime or merely several independent reasons to enter the same allocation state.

### Required correction

Trace the trigger's semantic alternatives separately:

`CASTLE-READINESS | MILITARY-INFRASTRUCTURE | ECONOMIC-INFRASTRUCTURE`.

Do not collapse them into “Castle preparation” unless downstream consumers confirm it.

---

## P10-QC-09 — “Persistent-looking regime selector” is useful but should be formally graded

**Severity: MEDIUM**

The phrase is appropriately cautious. But the document should explicitly distinguish:

`PERSISTENCE IN SELECTED SLICE`
from
`PERSISTENCE ACROSS MODULE LIFECYCLE`.

### Required correction

Add `LIFETIME = UNKNOWN` until all writes/resets are traced.

---

## P10-QC-10 — The percentage regime does not establish the allocation mechanism's control authority

**Severity: HIGH**

Writing percentage SNs establishes an output state. It does not yet establish which downstream subsystem consumes them or how frequently they are re-evaluated.

### Required correction

Trace:

`percentage writer → gatherer allocator/consumer → villager reassignment → world-state result`.

Without the consumer, “feedback control” remains a system-level inference.

---

## P10-QC-11 — The two allocation vectors deserve a delta analysis

**Severity: MEDIUM**

The exact change:

`44/55/1/0 → 40/57/3/0`

is strategically informative. It should be analyzed as a resource-flow delta rather than only cited as proof of context sensitivity.

### Required correction

Record:

`wood -4 | food +2 | gold +2 | stone 0`.

Then identify the newly satisfied prerequisite (`mining-camp` or gold drop distance) and test whether the change corresponds to an observed capability demand.

Do not assign motive until the consumer/transition is traced.

---

# 5. Lab 3 — Production Control

## P10-QC-12 — The production example is historically valid but mismatched to the lab's original target

**Severity: HIGH**

Pass 9's Lab 3 target was production authorization from `units.per`. Pass 10 substitutes an escrow-gated `mangonel-line` / `monk` example from `escrow.per` because `units.per` is unavailable.

This is an honest fallback, but it means the lab has changed its question.

### Required correction

Rename the lab:

`Escrow-Gated Production`

until `units.per` is recovered.

Reserve:

`Production Control / Authorization`

for the original `units.per` trace.

---

## P10-QC-13 — `escrow-flag2` semantics are not established by the two constants alone

**Severity: HIGH**

The values `8388608` and `33554432` are opaque bit-like selectors. The code shows what happens when those values are present; it does not explain their generation or whether multiple bits can coexist.

### Required correction

Trace the writer(s) and compare the flag's use across the escrow subsystem.

If it is a bitmask, document bit semantics. If it is an enumerated mode, document that instead. Do not infer from the numeric shape alone.

---

## P10-QC-14 — “Production permission” should be distinguished from “production completion”

**Severity: HIGH**

`can-train-with-escrow → train` proves an execution gate, not that a unit entered the queue or completed training.

### Required correction

Trace:

`train invocation → pending/queue state → completed unit observation`.

This should become the production analogue of the age-transition postcondition distinction.

---

# 6. Lab 4 — Threat Measurement / Aggregation

## P10-QC-15 — The lab title still overstates “classification”

**Severity: HIGH**

The exact slice is correctly described internally as measurement and accumulation. The heading still says “Threat Classification / Aggregation.”

The code shown directly demonstrates:

`enemy unit-family measurement → accumulation into cavarchers`.

It does not yet demonstrate a classification decision in the strict sense.

### Required correction

Rename to:

`Threat Measurement / Aggregation`

until the downstream classifier is found.

---

## P10-QC-16 — The first aggregation operation may not be semantically independent

**Severity: HIGH**

The rule calls `up-get-focus-fact` repeatedly while using the same temporary goal and then modifies `cavarchers`. The trace assumes each call returns an independently usable measurement.

That is likely, but the exact primitive semantics should be cited from the project's engine-semantic evidence before making stronger claims about accumulator behavior.

### Required correction

Annotate:

`PRIMITIVE SEMANTICS = ENGINE-CORROBORATED`

separately from:

`PROGRAM BEHAVIOR = SOURCE-DIRECT`.

External documentation can corroborate the primitive; it does not prove the author's strategic purpose.

---

## P10-QC-17 — “Compact representation of enemy military composition” is slightly too broad

**Severity: MEDIUM**

`cavarchers` is a specific aggregate category. The shown rule samples selected ranged/cavalry-related unit families and applies special treatment to elephant archers.

### Required correction

Say:

> “The rule constructs a compact aggregate for a specific cavalry-archer-related threat category.”

Then generalize only after sibling categories are traced.

---

## P10-QC-18 — The temporary-goal lifecycle is the central unresolved threat edge

**Severity: HIGH**

The same `temporary-goal` is repeatedly overwritten and transformed inside the rule. Calling it “measurement scratch” is plausible, but its broader lifecycle is unresolved.

### Required correction

Trace all writers/readers of `temporary-goal` in the relevant module and determine whether this numeric channel is safely reused between rule passes.

This is particularly important because the project's own archaeology standard warns against assuming that high-numbered or “temporary” goals are automatically scratch. 

---

# 7. Lab 5 — Candidate Search / Optimization-Like Loop

## P10-QC-19 — **Potential material error: “best distance” direction is not established**

**Severity: CRITICAL**

The exact source initializes:

`temporary-goal2 = -1`

and updates it when:

`temporary-goal > temporary-goal2`.

Therefore the shown routine retains the **largest measured distance**, not the smallest, assuming the comparison operators have their ordinary numeric meaning.

Pass 10 repeatedly calls this a “best-distance” or generic best-candidate routine. That is unsafe without the downstream objective.

### Required correction

Replace:

`best distance`

with:

`current extremum / selected distance`

until the consumer establishes whether the desired candidate is actually the farthest point.

This may be completely intentional. For example, a land-nomad placement routine might prefer maximizing separation. The archaeology must not decide the objective before following goals 504/505 to their consumer.

**This finding materially changes the next-pass priority.**

---

## P10-QC-20 — The search excerpt contains a duplicate initialization

**Severity: LOW/MEDIUM**

The initialization rule contains:

`set-goal temporary-goal5 0`

and later repeats:

`set-goal temporary-goal5 0`.

This may be harmless redundancy, a copied artifact, or evidence of a deliberately defensive initialization pattern.

### Required correction

Do not normalize it away. Record it as:

`REDUNDANT WRITE = PRESENT`

and check the original source context before interpreting its purpose.

This is exactly the sort of small historical coding habit the project is trying to recover.

---

## P10-QC-21 — “Candidate population” needs precise semantics

**Severity: MEDIUM**

`up-find-local c: villager-class c: 6` is interpreted as creating a candidate population. More precisely, it performs a search that populates/updates search state with local matching objects, with a maximum/search parameter.

### Required correction

Use:

`SEARCH RESULT SET`

rather than “candidate population” unless the primitive's exact semantics establish a materialized collection.

---

## P10-QC-22 — The search loop is incomplete at its consumer boundary

**Severity: CRITICAL**

Pass 10 acknowledges this, but still describes the loop as:

`RESET → GENERATE CANDIDATES → MEASURE → COMPARE → PRESERVE BEST → ADVANCE → REPEAT → TERMINATE → CONSUME BEST`.

The `CONSUME BEST` edge is not actually present in the shown historical slice.

### Required correction

Split the chain:

**PROVEN:** `RESET → SEARCH → MEASURE → COMPARE → WRITE 504/505 → ITERATE`

**UNPROVEN:** `504/505 → consumer → action`.

The latter becomes a Pass-11 closure target.

---

## P10-QC-23 — `up-jump-rule` requires exact target reconstruction

**Severity: HIGH**

The excerpt gives `-3` and `-4`, but the lab does not explicitly calculate the target rule indices.

Because jump targets depend on current rule position, exact target reconstruction is necessary to prove the loop structure.

### Required correction

Record:

`SOURCE RULE INDEX → DELTA → TARGET RULE INDEX → RULES SKIPPED → REENTRY STATE`.

External AoE2 scripting documentation confirms that `up-jump-rule` jumps relative to the current rule set and can be used for loops/skips, while warning about load blocks and performance. citeturn0search2turn0search3

---

## P10-QC-24 — Search performance cannot be called “bounded” solely from a counter

**Severity: MEDIUM**

The presence of counters strongly suggests bounded iteration, but a complete bound requires understanding how `local-last`, `temporary-goal3`, `temporary-goal6`, and jump re-entry interact.

### Required correction

Derive an actual upper bound symbolically if possible:

`N_candidates × N_iterations × rules_per_iteration`.

If the bound depends on runtime search semantics, mark it UNKNOWN.

---

# 8. Lab 6 — Scout Path Safety

## P10-QC-25 — “Persistent state in goals” is not yet proven for all listed goals

**Severity: MEDIUM**

A goal persists beyond a single action unless overwritten, but “persistent state” as an architectural claim requires lifecycle evidence.

### Required correction

Use:

`GOAL CHANNEL WITH CROSS-RULE USE`

until reset/overwrite lifecycle is traced.

---

## P10-QC-26 — The scout excerpt proves safety checks more strongly than waypoint selection

**Severity: HIGH**

The document title includes waypoint selection, but the exact excerpt shown ends during path analysis and danger aggregation. The final waypoint/action consumer is explicitly unresolved.

### Required correction

Rename the lab temporarily:

`Scout Group / Path Safety Analysis`

until the waypoint consumer is extracted.

---

## P10-QC-27 — The programmer comment is direct evidence of stated intent, not executable evidence

**Severity: MEDIUM**

Pass 10 says the comments are “strong programmer-intent evidence,” which is correct in a limited sense.

### Required correction

Use a separate evidence type:

`COMMENTARY-INTENT`

rather than folding comments into `DIRECT EXECUTABLE` evidence.

Comments can be stale, aspirational, or incomplete. Their value is high, but their evidentiary category should remain distinct.

---

## P10-QC-28 — “Route safety” should be tied to an actual decision threshold

**Severity: MEDIUM**

The excerpt counts nearby archers and checks spears, TCs, and castles, but the shown slice does not yet demonstrate how those observations alter a route or action.

### Required correction

Find the consumer of `remote-total` / `temporary-goal3` and identify the exact threshold or branch that changes behavior.

Then the statement “path safety” becomes a complete causal edge rather than a comment-supported interpretation.

---

# 9. Lab 7 — Attack / Retreat / Restart

## P10-QC-29 — The provisional treatment is correct and should not be weakened

**Severity: STRENGTH**

Pass 10 refuses to invent the exact HD source excerpt and retains an approximate anchor. This is exactly the correct behavior under the project's evidence rules. fileciteturn301file0L2-L2

### Required action

Recover the pristine/verified HD bytes before exact closure.

---

## P10-QC-30 — “Controller-state transitions exist” needs writer/reader decomposition

**Severity: HIGH**

The statement is probably correct from prior source archaeology, but Pass 10 has not shown the exact writer/reader chain.

### Required correction

For each channel:

`attack-goal | attack-status-goal | retreat-now-goal | restart-attack-goal`

record:

`writer | reader | resetter | timer | side effect | postcondition`.

---

## P10-QC-31 — Secondary documentation must not become historical substitute

**Severity: MEDIUM**

Pass 10 correctly calls external documentation “secondary corroboration.” Keep that boundary.

Official/secondary scripting documentation can support primitive meaning, but the verified historical HD source remains the authority for what this particular AI actually did. This separation is consistent with the project README's source hierarchy. fileciteturn299file0L2-L2

---

# 10. Lab 8 — Building Placement / Fallback

## P10-QC-32 — The primary path's “failure” is not directly detected by the backup rule

**Severity: HIGH**

The backup rule waits for:

`game-time > 600`
+ `TC count < 1`
+ `two-mins timer`
+ `pending TC < 1`
+ `can-build TC`.

That establishes a condition under which the fallback becomes eligible. It does not prove the fallback can distinguish:

`primary command failed`
from
`primary command never fired`
from
`primary command fired but foundation failed`
from
`primary command completed then TC was destroyed`.

### Required correction

Trace the causal alternatives and label the fallback trigger as:

`ABSENCE-OF-EXPECTED-STATE / TIMEOUT-LIKE CONDITION`

unless a direct failure flag is found.

---

## P10-QC-33 — The backup comment is strong but comments need their own evidence class

**Severity: MEDIUM**

The comment says the regular system occasionally fails. That is valuable direct evidence of what the author believed about the implementation.

It is not, by itself, a runtime frequency measurement.

### Required correction

Classify:

`COMMENTARY-INTENT = DIRECT`

`FAILURE FREQUENCY = UNKNOWN`

unless logs or source metrics establish frequency.

---

## P10-QC-34 — The primary and backup actions may have different placement semantics

**Severity: HIGH**

Primary:

`up-build place-control ... town-center`

Backup:

`build town-center`.

The lab correctly treats them as different mechanisms. It should explicitly avoid assuming that the backup is equivalent in placement quality, location, builder assignment, or safety.

### Required correction

Trace the expected spatial/economic consequences separately.

---

## P10-QC-35 — `up-pending-objects` is an observation/eligibility predicate, not necessarily proof of “execution pending” in the generic sense

**Severity: MEDIUM**

The lab labels pending TC state an “execution/pending observation.” That is reasonable but should remain primitive-specific.

### Required correction

Use:

`ENGINE PENDING-OBJECT PREDICATE`

and only generalize to a universal AEGIS pending-state abstraction after multiple action families are traced.

---

# 11. Cross-lab state ownership

## P10-QC-36 — Ownership table still mixes “writer present” with “owner”

**Severity: HIGH**

The document itself warns that ownership means lifecycle responsibility, but several rows still name a subsystem as owner without proving lifecycle responsibility.

Examples:

- `escrow-flag → escrow subsystem`;
- `cavarchers → threat subsystem`;
- `temporary-goal3 → scout controller`.

### Required correction

Add:

`OWNER CONFIDENCE = PROVEN / PROBABLE / DISTRIBUTED / AMBIGUOUS`.

Until writer+reader+resetter+side-effect evidence converges, use `PROBABLE` or `DISTRIBUTED`.

---

## P10-QC-37 — State ontology is missing from the cross-lab table

**Severity: HIGH**

Pass 10 lists “historical semantic type,” but not the full ontology required by Pass-7 QC.

### Required correction

Add:

`OBSERVATION | CLASSIFICATION | BELIEF | REQUIREMENT | COMMITMENT | AUTHORITY | ACTION-STATE | SCRATCH | UNKNOWN`.

Most current rows should likely be `UNKNOWN` or `ACTION-STATE/CONTROL` until lifecycle tracing is complete.

---

# 12. Historical-vs-AEGIS separation

## P10-QC-38 — The AEGIS translations are good but sometimes skip the historical boundary

**Severity: HIGH**

For example, Lab 1 jumps from the historical escrow rule to:

`COMMITMENT → AUTHORITY → VERIFY`.

The document says authority is AEGIS-generalization, but the visual adjacency can still make the pipeline look historical.

### Required correction

Use an explicit divider in every lab:

`=== HISTORICAL SOURCE ===`

`=== INTERPRETATION ===`

`=== AEGIS DESIGN ===`.

This should become mandatory for all future archaeology artifacts.

---

## P10-QC-39 — “AEGIS may encapsulate the pattern” needs a capability-preservation rule

**Severity: MEDIUM**

The design translation should not merely say “encapsulate.” It should state what must remain observable so the abstraction does not erase the historical implementation's important constraints.

### Required correction

Every abstraction must preserve:

`inputs | outputs | lifecycle | invalidation | side effects | performance budget | failure signatures`.

---

# 13. Evidence coverage audit

## P10-QC-40 — “6/8 exact” is useful but not sufficient as a quality score

**Severity: MEDIUM**

A lab can have exact source and still have an unproven causal chain. Conversely, an approximate anchor can support a strong historical conclusion if independently corroborated.

### Required correction

Replace the single coverage score with separate dimensions:

`SOURCE COVERAGE | ANCHOR COVERAGE | CAUSAL COVERAGE | LIFECYCLE COVERAGE | POSTCONDITION COVERAGE | CONSUMER COVERAGE | STRATEGIC COVERAGE`.

---

## P10-QC-41 — “8/8 alternative explanations” is a framework count, not evidence completeness

**Severity: MEDIUM**

The table says alternatives are “8/8 frameworked.” That means each lab has an alternative-explanation field, not that the alternatives have been exhaustively searched.

### Required correction

Rename:

`ALTERNATIVE-EXPLANATION FIELD PRESENT = 8/8`.

Do not call it “coverage” without qualification.

---

## P10-QC-42 — Falsifiers are generally good but some are still too abstract

**Severity: MEDIUM**

A falsifier such as “source interpretation contradicts measurement semantics” is useful, but stronger falsifiers identify the exact observation that would overturn the claim.

### Required correction

For each major claim, write a falsifier in observable form:

`If X source reader uses Y state for Z unrelated purpose, interpretation A is rejected.`

---

# 14. Performance audit

## P10-QC-43 — Qualitative performance risk is not itself DIRECT evidence

**Severity: MEDIUM**

The use of repeated searches and jumps is direct. Calling the resulting performance risk “DIRECT” is a category error.

### Required correction

Use:

`SEARCH/ITERATION MECHANISM = DIRECT`

`PERFORMANCE RISK = INFERRED`

`MEASURED RUNTIME COST = UNKNOWN`.

External documentation independently warns that jump loops can increase rule processing and that search behavior has performance implications. citeturn0search3

---

## P10-QC-44 — Performance should distinguish source-level bound from engine-level cost

**Severity: HIGH**

Even if candidate count and loop iterations are bounded, the cost of each primitive can vary.

### Required correction

Record both:

`ALGORITHMIC BOUND`

and:

`ENGINE PRIMITIVE COST = UNKNOWN/MEASURED`.

This matters especially for `up-find-remote`, object-data sorting, DUC/search and path analysis.

---

# 15. Cross-artifact consistency

## P10-QC-45 — Pass 10 successfully closes the largest Pass-9 deficiency

**Severity: STRENGTH**

Pass 9's central QC criticism was the absence of literal historical source. Pass 10 adds literal excerpts for six recovered mechanisms and explicitly blocks the two unavailable areas rather than fabricating them. fileciteturn306file0L2-L2

This requirement is substantially satisfied, though not complete.

---

## P10-QC-46 — Pass 10 correctly preserves the historical-vs-AEGIS firewall

**Severity: STRENGTH**

The document repeatedly says that authority objects, belief/confidence objects, generalized recovery taxonomies, and generic optimizer abstractions are AEGIS designs rather than historical source terminology. This directly addresses the Pass-8/Pass-9 QC concern. fileciteturn291file0L2-L2

---

## P10-QC-47 — Pass 10 exposes a new search semantic question that is more valuable than additional abstraction

**Severity: CRITICAL/STRENGTH**

The exact comparison direction means we cannot safely call the retained candidate “best” until its downstream purpose is known.

This is precisely the kind of discovery a forensic code trace is supposed to produce.

The correct next move is not to patch the wording only. It is to trace goals 504/505 to their consumer.

---

# 16. Required corrections before canonical promotion

1. Add package/module provenance identifiers.
2. Separate package-exact from pristine-historical status.
3. Replace action-success wording with action-invocation wording.
4. Trace `sn-current-age` completion evidence.
5. Trace `escrow-flag` lifecycle.
6. Rename Lab 3 to escrow-gated production until `units.per` is recovered.
7. Trace `escrow-flag2` writers/semantics.
8. Rename Lab 4 to measurement/aggregation until classification is proven.
9. Trace `temporary-goal` lifecycle in threats.
10. Correct/qualify the search “best distance” language.
11. Trace goals 504/505 to their consumer.
12. Reconstruct exact `up-jump-rule` destinations.
13. Derive search bounds rather than assuming boundedness.
14. Rename Lab 6 until waypoint/action consumer is found.
15. Separate comment-intent evidence from executable evidence.
16. Recover exact HD attack/retreat source.
17. Recover pristine `units.per`.
18. Trace building fallback trigger causality.
19. Add full state ontology and owner-confidence columns.
20. Replace evidence-coverage percentages with multidimensional coverage.
21. Separate algorithmic complexity from primitive runtime cost.
22. Attach Pass-7 edge IDs and Pass-4 state-channel IDs to each lab.

---

# 17. Revised evidence model for Pass 11

Every closure record should use:

`LAB | EDGE ID | SOURCE PACKAGE | MODULE | EXACT ANCHOR | SOURCE TEXT | STATE READ | STATE WRITE | STATE ONTOLOGY | WRITER | READER | RESETTER | TEMPORAL SEMANTICS | ENGINE PRIMITIVE | ACTION | COMMAND POSTCONDITION | WORLD POSTCONDITION | STRATEGIC POSTCONDITION | FAILURE SIGNATURE | RECOVERY | ALTERNATIVE | FALSIFIER | EVIDENCE GRADE | AEGIS STATUS`.

### Additional search-specific fields

`SEARCH RESET | SEARCH SCOPE | SEARCH ORDER | CANDIDATE COUNT | ITERATION COUNTER | COMPARISON DIRECTION | EXTREMUM TYPE | BEST-STATE WRITER | BEST-STATE CONSUMER | JUMP TARGET | TERMINATION CONDITION | ENGINE COST`.

The **comparison direction / extremum type** fields are now mandatory because of P10-QC-19.

---

# 18. Pass-11 priority order

The original Pass-10 priority should be tightened:

### Priority 1 — Search consumer

`504/505 → reader → actual action`

Reason: P10-QC-19 potentially changes the interpretation of the entire search routine.

### Priority 2 — Threat consumer

`cavarchers → every reader → first concrete response`

Reason: closes measurement → strategic-response boundary.

### Priority 3 — Scout consumer

`remote-total / temporary-goal3 → waypoint/action`

Reason: closes safety analysis → movement decision.

### Priority 4 — Exact HD attack lifecycle

`retreat-now-goal → attack-goal → timer → physical command → restart`

### Priority 5 — Pristine `units.per`

Restore the original production-control lab.

### Priority 6 — Escrow lifecycle

`escrow-flag / escrow-flag2 → writers → release/reset → consumers`.

### Priority 7 — Gatherer lifecycle

`temporary-goal10 → percentage outputs → gatherer consumer → world-state result`.

---

# 19. Final disposition

## PASS 10 — **ACCEPT WITH CORRECTIONS**

### Quality assessment

| Dimension | Judgment |
|---|---|
| Historical source extraction | **HIGH where recovered exact slices exist** |
| Provenance discipline | **HIGH, but package identity needs strengthening** |
| Literal `.per` literacy | **HIGH improvement over Pass 9** |
| Strategic interpretation | **HIGH, generally well graded** |
| State ownership | **MODERATE / incomplete** |
| Consumer tracing | **LOW-MODERATE / next bottleneck** |
| Lifecycle closure | **MODERATE-LOW** |
| Postcondition verification | **MODERATE-LOW** |
| Performance analysis | **QUALITATIVE; quantitative open** |
| Historical-vs-AEGIS separation | **HIGH** |
| Canonical readiness | **NOT YET** |

### The central QC conclusion

Pass 10 is doing what good archaeology should do: **the exact code did not merely confirm our theories; it exposed places where the theories may be wrong.**

The search comparison is the clearest example. We began with a generic “best candidate” interpretation. The literal code shows a `>` comparison against `-1`, which means we must now determine whether the programmer is deliberately selecting a maximum-distance candidate or whether another semantic layer changes the meaning.

That is a real research discovery, not a documentation defect.

The correct Layer-2 posture is therefore:

> **Do not make the code fit the architecture. Make the architecture explain the code.**

Pass 10 should be retained as the current forensic extraction layer, corrected as above, and followed by a narrowly targeted **Pass 11 — Consumer / Provenance Closure** rather than another conceptual synthesis.
