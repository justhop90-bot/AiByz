# AoE2DE Consumer / Provenance Closure — Deep QC Pass 1

**Date:** 2026-09-04  
**Target:** `AOE2DE_CONSUMER_PROVENANCE_CLOSURE_PASS11_2026-09-04.md`  
**Status:** DEEP QC / ACCEPT WITH CORRECTIONS  
**Audit mode:** source-forensic, cross-artifact, adversarial semantic, provenance, external-semantic triangulation, repository-integrity

---

# 0. Executive verdict

Pass 11 is a **major advancement** over Pass 10. It successfully closes several downstream edges that were previously only hypothesized. In particular, the `cavarchers` chain now reaches camel-production control, the 504/505 search now reaches an actual movement action, scout path analysis reaches movement control, and attack retreat state reaches `up-retreat-now`.

However, the artifact contains several claims that are stronger than the exact evidence currently shown. The largest issues are:

1. the `cavarchers → traincamel → train` chain is real, but the text sometimes calls it a fully strategic counter-composition chain when the exact chain proves a thresholded production/research response, not a complete force-composition optimizer;
2. the 504/505 interpretation correctly identifies a maximum-distance comparator, but the phrase “specific spatial objective” remains partly inferred until the land-nomad routine's higher-level objective is traced;
3. scout path analysis reaches movement, but the displayed chain does not prove that the selected pivot is always caused by danger, nor that information value is optimized;
4. attack/retreat claims depend on exact HD source evidence that the artifact says is available, but the repository diff does not itself include the source archive, so the provenance path must be explicit and independently recoverable;
5. escrow release is directly observed as a reset, but its causal timing relative to successful conversion remains unresolved;
6. ownership classifications remain partly inferred from module-level writer/reader patterns;
7. several “closed causal chain” labels need a distinction between **control causality** and **strategic causality**;
8. the quantitative coverage table is useful but currently labels many partially proven chains as `YES` at the reader/consumer/action level while world-state verification remains partial.

**Disposition: ACCEPT WITH CORRECTIONS.**

Pass 11 should become the downstream-provenance baseline, but it is not yet the final historical causal graph.

---

# 1. Audit standard

A genuinely closed historical chain requires separate proof of:

`SOURCE → STATE WRITE → STATE READ → GUARD → CONTROL EFFECT → ACTION → WORLD-STATE EFFECT → STRATEGIC EFFECT`.

A chain may close at one level while remaining open at another.

Use these grades:

- **DIRECT:** exact executable source demonstrates the relationship.
- **COMPOSED:** multiple direct relationships establish the larger chain.
- **INFERRED:** strategic meaning reconstructed from source behavior.
- **AEGIS-GENERALIZATION:** new design derived from the historical pattern.
- **UNCERTAIN:** insufficient evidence.

Add a second axis:

`CONTROL | WORLD | STRATEGIC`.

This prevents a direct state transition from being mistaken for a proven strategic outcome.

---

# 2. Critical finding — “closure” is level-dependent

## QC11-01 — Several chains are control-closed but not world/strategic-closed

**Severity: CRITICAL**

Pass 11 calls several chains “closed” after reaching an action. But the project-wide postcondition doctrine says:

`command ≠ world-state result ≠ strategic success`.

For example:

`cavarchers → traincamel → train`

is closed at the **control/action level**.

It is not closed at the **world-state level** until a camel actually appears in the production state, and not closed strategically until the local capability relationship changes.

### Required correction

Every closure should state:

`CONTROL CLOSURE = YES/NO`

`WORLD CLOSURE = YES/NO`

`STRATEGIC CLOSURE = YES/NO`.

This is now mandatory for Pass 12 onward.

---

# 3. Closure A — `cavarchers`

## QC11-02 — The threat → response chain is real, but “counter-composition” remains too broad

**Severity: HIGH**

The source evidence supports:

`enemy unit-family measurement`
→ `cavarchers`
→ threshold
→ `traincamel yes`
→ `can-train`
→ camel train action.

It also supports camel-related research conditions.

This is strong.

But it does not prove that the resulting camel production constitutes a globally optimized **counter-composition**. The chain does not yet show:

- total friendly composition;
- competing unit candidates;
- candidate scoring;
- minimum/target camel ratio;
- strategic objective comparison;
- post-production composition verification.

### Required correction

Use the precise historical claim:

> **Enemy composition aggregate → thresholded camel response control → camel production/research eligibility.**

Reserve “counter-composition optimizer” for AEGIS.

---

## QC11-03 — “Increase the probability/eligibility” is ambiguous in a deterministic rule system

**Severity: MEDIUM**

The Pass 11 strategic interpretation says the signal “increases the probability/eligibility” of camel production.

There is no probability mechanism shown. The actual evidence is deterministic thresholding.

### Required correction

Use:

`increases eligibility / activates response conditions`

unless a stochastic selection mechanism is directly shown.

---

## QC11-04 — Direct `cavarchers` initialization does not prove the complete accumulator reset lifecycle

**Severity: HIGH**

`init.per` initializes `cavarchers` to zero. That proves startup initialization.

It does not prove whether the value is reset to zero before every threat measurement cycle, incrementally accumulated, or partially overwritten elsewhere.

### Required correction

Find all writers and resetters. Classify lifecycle:

`STARTUP | PER-CYCLE | EVENT-DRIVEN | MONOTONIC | OVERWRITE | UNKNOWN`.

Until then, use `OWNER = PROBABLE` and `LIFETIME = PARTIAL`.

---

## QC11-05 — Threat aggregation weights need semantic treatment

**Severity: MEDIUM**

The elephant-archer branch doubles/composes values before adding them to `cavarchers`. This is significant.

It means the aggregate is not simply a raw unit count.

### Required correction

Document:

`input unit family | transformation | contribution to cavarchers`.

This may reveal an implicit historical weighting scheme and is potentially more strategically informative than the threshold itself.

Do not call the aggregate “count” without qualification; use **weighted threat aggregate** where the arithmetic proves weighting.

---

# 4. Closure B — goals 504/505

## QC11-06 — The maximum-distance result is correctly identified

**Severity: STRENGTH**

The Pass 11 correction from generic “best candidate” to maximum-distance selection is exactly right.

The literal evidence is:

`best sentinel = -1`

plus:

`new distance > stored distance`

therefore:

`stored candidate = argmax(distance)`.

This should remain one of the canonical forensic examples.

---

## QC11-07 — “Specific spatial objective” still requires a semantic boundary

**Severity: HIGH**

The search demonstrably selects the farthest pair and derives a movement point. It does not, by itself, prove the programmer's full strategic reason for selecting that point.

### Required correction

Separate:

**DIRECT:** farthest-pair selection and movement-point construction.

**INFERRED:** central relocation heuristic / robustness objective.

**STRATEGIC:** land-nomad strategic purpose, pending complete higher-level trace.

The distinction matters because the same geometric operation can serve multiple purposes.

---

## QC11-08 — Goal 505 arithmetic needs explicit indexing semantics

**Severity: HIGH**

The chain states:

`505 = temporary-goal5 - 1`.

The exact reason is likely conversion from a one-based candidate counter to a zero-based search index, but this is an interpretation.

### Required correction

Trace the preceding increment and subsequent `up-set-target-object` call to prove the indexing convention.

Do not state the indexing rationale until that trace is explicit.

---

## QC11-09 — Search consumer closure must include the complete action context

**Severity: MEDIUM**

The movement action is direct, but the excerpt should record:

`target point source | selected player/unit group | action target list | action parameters`.

Otherwise “move” can be misread as a player-wide action when the engine may apply it to the current search set.

External scripting references corroborate that `up-target-point` applies an action to units in the relevant search result set, which strengthens the semantic interpretation but does not substitute for source-specific behavior. fileciteturn324file0L3-L5

---

# 5. Closure C — Scout path → movement

## QC11-10 — The source supports danger inspection, but the causal path to pivot selection needs tighter proof

**Severity: HIGH**

Pass 11 gives:

`danger-object search → reinforcing-group state → two geometric candidates → closer pivot → action-move`.

The concern is that `reinforcing-group state` may be influenced by more than danger, and the exact condition connecting danger results to the pivot branch needs to be shown.

### Required correction

Split:

`danger measurement → state write`

and:

`state write → pivot branch`

with exact guards.

If the pivot branch only depends on `multi-group-reinforcing`, then the causal edge is different from “danger caused pivot.”

---

## QC11-11 — “Route-safety mechanism participates in actual movement control” is defensible but should be graded COMPOSED

**Severity: MEDIUM**

The source has path analysis and a later movement consumer. The exact causal connection is distributed.

### Required correction

Grade:

`path-analysis machinery = DIRECT`

`path-analysis → movement consequence = COMPOSED`

unless the exact state dependency is shown in one complete chain.

---

## QC11-12 — Scout group size and target semantics need closure

**Severity: MEDIUM**

The group can contain up to 12 scouts. The movement action's target population should be explicitly identified.

### Required correction

Record:

`group ID | membership | action target | group reset | group destruction/retasking`.

---

# 6. Closure D — Attack / retreat / restart

## QC11-13 — The artifact's provenance claim must be made reproducible

**Severity: CRITICAL**

Pass 11 states:

> “The verified HD source is now available from `AI (HD version).per`.”

But the artifact does not provide a repository-visible hash/path for the exact source used in this pass.

### Required correction

Record:

`SOURCE FILE | PACKAGE | FILE HASH | LINE RANGE | EXTRACTION METHOD`.

If the source is not repository-tracked, provide the project evidence-record identifier that identifies the exact external artifact.

This is necessary because attack/retreat claims are strategically important.

---

## QC11-14 — `up-retreat-now` closes command invocation, not physical retreat

**Severity: STRENGTH/CLARIFICATION**

Pass 11 correctly preserves this distinction.

The chain is:

`retreat state → timer/guard → up-retreat-now → reset state`.

World-state retreat remains unverified.

### Required correction

Add explicit closure flags:

`CONTROL = YES`

`WORLD = NO`

`STRATEGIC = NO/UNKNOWN`.

---

## QC11-15 — Restart closure is control-state closure, not renewed attack closure

**Severity: HIGH**

`restart-attack-goal` being consumed and cleared proves lifecycle state.

It does not yet prove:

`restart state → renewed movement → renewed engagement → same strategic objective`.

### Required correction

Trace the next attack execution consumer.

This becomes a Pass-12 high-priority edge.

---

# 7. Closure E — Escrow

## QC11-16 — The unconditional release rule is correctly treated as unresolved timing

**Severity: STRENGTH**

The artifact explicitly refuses to equate the release/reset rule with successful completion. This is correct.

### Required correction

Do not call it “release after conversion.” Call it:

`escrow reset/release event`.

Then trace scheduler/order/consumers to determine timing.

---

## QC11-17 — “Allocation → consumption → release” may not be one transaction

**Severity: HIGH**

The three mechanisms exist, but the evidence does not yet prove that one reservation instance travels through a transaction lifecycle without interference.

### Required correction

Introduce an instance-level question:

`Can reservation A be consumed by action B after being created by writer C?`

If no transaction identity exists, call the relationship **system-level composed**, not instance-level transactional.

---

# 8. Closure F — Production

## QC11-18 — The phrase “production control has at least these layers” is a useful synthesis, not a complete historical pipeline

**Severity: MEDIUM**

The source demonstrates strategic response condition, train goals, feasibility, production-building search, filtering and train action. It does not prove that all production paths share this exact sequence.

### Required correction

Label it:

`REPRESENTATIVE PRODUCTION PATH`,

not universal production architecture.

---

## QC11-19 — Production search filters deserve exact semantic annotation

**Severity: HIGH**

The path uses:

`object-data-progress-value >= 1`

and:

`object-data-under-attack >= 1`

followed by distance sorting and index filtering.

These are strategically meaningful filters. Pass 11 should explain what candidate production buildings are being excluded and why.

### Required correction

For each filter record:

`primitive | field | comparison | candidate removed | strategic rationale | evidence grade`.

This may reveal an implicit production-building availability heuristic.

---

# 9. State ownership audit

## QC11-20 — “Owner” should be confidence-rated everywhere

**Severity: HIGH**

Pass 11 lists:

`cavarchers → threat subsystem`

`504/505 → search routine`

`restart-attack-goal → TSA/building transition`.

These are useful provisional ownerships, but the evidence is not complete enough for categorical ownership in every case.

### Required correction

Use:

`OWNER = PROVEN | PROBABLE | DISTRIBUTED | AMBIGUOUS`

and:

`OWNER BASIS = writers + readers + resetters + side effects + lifecycle`.

---

## QC11-21 — `temporary-goal10` is correctly kept unresolved

**Severity: STRENGTH**

The artifact does not collapse the “temporary” name into a scratch classification. Keep this behavior.

The same rule should now be applied to all `temporary-goal*` channels.

---

# 10. Strategic interpretation audit

## QC11-22 — “Distributed pressure controller” is useful but should be explicitly synthesized

**Severity: MEDIUM**

The thresholded threat response is controller-like. But “pressure controller” is an architectural synthesis.

### Required correction

Mark:

`historical mechanism = DIRECT/COMPOSED`

`controller interpretation = INFERRED`.

---

## QC11-23 — “Programmer trying to derive robust central relocation point” is not yet proven

**Severity: HIGH**

This is plausible from farthest-pair → midpoint → center shift. But robustness is an inferred objective.

### Required correction

Use:

> “The code derives a movement point from the farthest candidate pair and then applies a center-directed geometric transformation. The strategic reason for this transformation remains an inference pending the surrounding land-nomad objective.”

That wording is more forensic.

---

## QC11-24 — “Preserve scout-group movement while avoiding dangerous local geometry” is plausible, not fully direct

**Severity: MEDIUM**

The source explicitly analyzes threats and computes movement geometry. It does not yet establish that preservation of scout-group movement is the governing strategic objective.

### Required correction

Grade `INFERRED`.

---

# 11. External semantic triangulation audit

## QC11-25 — External scripting references corroborate primitives, not author intent

**Severity: STRENGTH**

The external AI scripting references confirm useful primitive semantics:

- `up-full-reset-search` clears prior search IDs/filters;
- `up-find-local` populates the local search list;
- `up-get-search-state` reports search-list state;
- `up-target-point` acts on the relevant search result set;
- `unit-type-count` supports unit-line wildcard parameters;
- `can-train` checks whether training can start.

These sources are useful semantic triangulation. They do not prove why the historical programmer selected these primitives in a particular strategy.

The distinction should remain explicit. fileciteturn324file0L3-L5

---

## QC11-26 — Secondary historical copies must be labeled secondary

**Severity: MEDIUM**

The discovered historical HD AI mirror is useful for cross-checking terminology, but a mirror/copy is not equivalent to the project's verified archive.

### Required correction

Every external historical copy gets:

`PRIMARY / SECONDARY / MIRROR / UNKNOWN`.

Never allow a secondary copy to silently become the provenance root.

---

# 12. Repository / artifact integrity audit

## QC11-27 — Pass 11 is correctly on the Layer-2 branch

**Severity: STRENGTH**

The PR remains open, draft, and non-mergeable. The current head is `41be07355f618d225f3f154f019a43426efb9c0e`, with 17 commits and 19 changed files. This is appropriate while the evidence remains under active correction. fileciteturn319file0L2-L13

---

## QC11-28 — The PR contains both research artifacts and QC artifacts, which is good, but canonical status needs a manifest

**Severity: MEDIUM**

As the branch grows, it becomes difficult to know which artifacts are:

`CANONICAL | WORKING | QC | SUPERSEDED | BLOCKED | HISTORICAL SOURCE`

### Required correction

Add a Layer-2 artifact manifest with:

`artifact | predecessor | status | evidence class | commit | canonical? | supersedes | blocked by`.

This will prevent accidental use of a superseded research note as policy.

---

# 13. Quantitative closure score

A more rigorous Pass-11 coverage table should be:

| Lab | Control closure | World closure | Strategic closure | Provenance | Lifecycle | Status |
|---|---|---|---|---|---|---|
| Threat/cavarchers | YES | PARTIAL | PARTIAL | HIGH | PARTIAL | MAJOR CLOSURE |
| Search 504/505 | YES | PARTIAL | PARTIAL | HIGH | PARTIAL | MAJOR CLOSURE |
| Scout path | YES | PARTIAL | PARTIAL | HIGH | PARTIAL | MAJOR CLOSURE |
| Attack/retreat | YES | NO | NO | PROVISIONAL | PARTIAL | MAJOR CONTROL CLOSURE |
| Escrow | YES | PARTIAL | PARTIAL | HIGH | PARTIAL | STRONG |
| Production | YES | PARTIAL | PARTIAL | HIGH | PARTIAL | STRONG |
| Gatherer regime | PARTIAL | PARTIAL | PARTIAL | HIGH | OPEN | OPEN |
| Building fallback | YES | PARTIAL | PARTIAL | HIGH | PARTIAL | STRONG |

This is more honest than a binary “writer/reader/action = YES” table.

---

# 14. Pass-11 corrections required before canonical promotion

1. Add control/world/strategic closure levels.
2. Narrow “counter-composition” terminology.
3. Replace probability language with deterministic eligibility language.
4. Trace `cavarchers` reset/recompute lifecycle.
5. Document weighted threat aggregation.
6. Separate direct geometric behavior from inferred strategic purpose.
7. Prove 504/505 indexing semantics.
8. Include exact search action target context.
9. Trace danger state → scout pivot guard.
10. Trace scout group lifecycle.
11. Make HD source provenance reproducible with package/hash/anchor.
12. Trace restart state into renewed attack execution.
13. Rename escrow release as reset/release event until timing is proven.
14. Test whether escrow allocation/consumption/release is instance-level or merely subsystem-level.
15. Label production path as representative rather than universal.
16. Annotate production search filters.
17. Add owner-confidence fields.
18. Add historical-primary/secondary source classification.
19. Add Layer-2 artifact manifest.
20. Replace binary closure score with multidimensional closure score.

---

# 15. Pass-12 research priorities

## P0 — Close strategic meaning of already-closed control chains

### 1. `504/505 → land-nomad strategic objective`

Determine why maximum-distance pair selection, midpoint construction, and nine-tile center shift produce the desired strategic relocation.

### 2. `cavarchers → camel response → realized military capability`

Trace actual unit delivery and downstream force-composition state.

### 3. `scout danger → pivot → movement → information outcome`

Determine whether the route actually improves survival/information and under which branch conditions.

### 4. `retreat → renewed attack`

Close the operational attack lifecycle after controller reset.

## P1 — Close economic and production lifecycles

5. gatherer regime → worker allocation → resource inflow;
6. production search → queue/pending → unit completion;
7. escrow reservation → exact consumer → reset timing;
8. building fallback → completion/rebuild result.

## P2 — Build the cross-system graph

Only after the P0 edges close should the project construct the full:

`ECONOMY → THREAT → PRODUCTION → TECHNOLOGY → MILITARY → MAP → ATTACK → RECOVERY → ECONOMY`

network.

---

# 16. Final judgment

**PASS 11 — ACCEPT WITH CORRECTIONS.**

### Quality

- Downstream consumer tracing: **HIGH improvement**
- Historical source fidelity: **HIGH where exact source is provenance-locked**
- Control-level causal closure: **HIGH for four major chains**
- World-state closure: **PARTIAL**
- Strategic closure: **PARTIAL**
- Lifecycle ownership: **MODERATE / incomplete**
- External semantic triangulation: **GOOD**
- Strategic interpretation: **HIGH, but must remain evidence-graded**
- Canonical readiness: **NOT YET**

### Most important methodological result

Pass 11 has proven that several historical state channels are not dead-end bookkeeping. They are consumed by concrete downstream control decisions.

The project can now state, with strong evidence:

> **Promisory repeatedly converts measured game conditions into compact state, uses that state to alter downstream eligibility and control, and then invokes concrete game actions.**

What remains to be proven is the final layer:

> **Did those actions actually change the game relationship the programmer intended?**

That is the boundary between **control archaeology** and **strategic archaeology**.

Pass 12 should cross that boundary carefully.
