# Layer 2 — HD / Promisory Evidence-Edge Ledger — Pass 7

**Date:** 2026-09-04  
**Status:** FORENSIC PROVENANCE PASS / working ledger  
**Target:** `HD_STRATEGIC_TRANSITION_TABLE_PASS6_2026-09-04.md`  
**QC basis:** `HD_STRATEGIC_TRANSITION_TABLE_QC_PASS1_2026-09-04.md`  
**Primary source:** verified `AI (HD version).per` + verified Promisory source supplied for Layer 2  
**Runtime authority:** frozen Layer-1 machine evidence for current AoE2DE execution semantics

## 0. Purpose

Pass 6 represented eight strategic transitions. Pass-6 QC identified the remaining epistemic risk: a correct source observation can silently acquire an unsupported causal meaning when several relationships are compressed into one arrow.

This ledger audits the **edges**, not merely the nodes.

Canonical record:

`Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status`

### Evidence grades

- **DIRECT** — executable source or explicit source comment supports the relationship.
- **COMPOSED** — multiple direct relationships form the relationship; no single rule necessarily states the complete edge.
- **INFERRED** — strategic interpretation reconstructed from repeated behavior.
- **AEGIS-GENERALIZATION** — proposed AEGIS design derived from the historical pattern.
- **UNCERTAIN** — current evidence is insufficient; must not be promoted.

### Provenance rule

A source location is an anchor, not proof of every downstream interpretation. Where only an approximate location is available from the prior forensic extraction, that limitation is retained. **TBD is preferable to fabricated precision.**

---

# 1. ST-01 — Dark → Feudal

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST01-E01 | economic/resource state | age-transition readiness | `gatherers.per` + age/research state | exact Feudal writer not yet isolated | RESOURCE/RESEARCH | COMPOSED | gatherer rules may only optimize local resource needs | exact Feudal transition could be independent of gatherer state | VERIFY |
| ST01-E02 | protected resources | research authorization | `escrow.per` | approx. lines 1–40; Castle/Imperial rules use `can-research-with-escrow` | RESOURCE/RESEARCH | DIRECT | escrow may be implementation mechanism rather than strategic valuation | remove escrow and show identical authorization path | INHERIT PATTERN |
| ST01-E03 | `can-research-with-escrow castle-age` | Castle research action | `escrow.per` | approx. line 26 | RESEARCH | DIRECT | feasibility does not prove timing rationale | inspect action/pending chain | INHERIT |
| ST01-E04 | `can-research-with-escrow imperial-age` | Imperial research action | `escrow.per` | approx. line 35 | RESEARCH | DIRECT | same limitation | inspect action/pending chain | INHERIT |
| ST01-E05 | resource allocation context | transition readiness | `gatherers.per` | contextual allocation rules; exact age-up chain TBD | RESOURCE | COMPOSED | allocation may respond to immediate deficit | trace a complete age-up cycle | VERIFY |
| ST01-E06 | age transition | new strategic capability | HD + Promisory age/research state | exact end-to-end Feudal world-state proof TBD | STRATEGIC | INFERRED | age completion may occur without usable infrastructure | compare completed age with capability availability | AEGIS VERIFY |
| ST01-E07 | age as capability conversion | opportunity-cost evaluation | distributed source behavior | no single historical formula | STRATEGIC | AEGIS-GENERALIZATION | programmer may use threshold logic | locate marginal-value comparison | DESIGN ONLY |

**Conclusion:** controlled Castle/Imperial research is directly evidenced; the Dark→Feudal chain is not yet exact enough to call DIRECT.

---

# 2. ST-02 — Feudal pressure → Castle

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST02-E01 | age/resource context | gatherer percentage changes | `gatherers.per` | contextual rules distributed through module | RESOURCE | DIRECT | rules may be reactive rather than age-strategic | remove age/unit guards and compare writes | INHERIT |
| ST02-E02 | escrow/resource-control state | Castle research authorization | `escrow.per` | approx. line 26 | RESOURCE/RESEARCH | DIRECT | authorization does not prove strategic timing | identify independent trigger | INHERIT |
| ST02-E03 | Feudal military state | decision to age | distributed HD strategy/unit/control + resource/research | exact single trigger not isolated | STRATEGIC | INFERRED | subsystems may not use marginal-value comparison | find explicit comparison/counterexample | AEGIS MODEL |
| ST02-E04 | attack state | resource/age commitment | HD attack + resource systems | exact writer chain TBD | CONTROL/RESOURCE | COMPOSED | simultaneous operation may be independent | trace branch where attack overlaps age commitment | VERIFY |
| ST02-E05 | Castle transition | superior capability set | age/research + production infrastructure | world-state proof required | STRATEGIC | INFERRED | age may complete before exploitation | verify post-age readiness | AEGIS VERIFY |
| ST02-E06 | marginal Feudal value | Castle timing value | no single historical formula | none | STRATEGIC | AEGIS-GENERALIZATION | historical AI may use thresholds | locate explicit scoring | DESIGN ONLY |

**Conclusion:** historical ingredients for a competing Feudal/Castle resource problem are strong; a unified historical Castle-timing optimizer is not proven.

---

# 3. ST-03 — Castle → Imperial

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST03-E01 | escrow flag/state | Imperial research authorization | `escrow.per` | approx. line 35 | RESEARCH | DIRECT | none material if exact rule/action confirmed | remove Imperial branch | INHERIT |
| ST03-E02 | Imperial research | strategic current-age state | `escrow.per` | approx. lines 35–40; prior audit identified age-state update | RESEARCH/CONTROL | DIRECT | state update may be bookkeeping | inspect readers of current-age state | INHERIT |
| ST03-E03 | gatherer allocation | Imperial resource accumulation | `gatherers.per` | contextual allocation rules | RESOURCE | COMPOSED | allocation may serve another objective | trace reservation/resource arrival | INHERIT PATTERN |
| ST03-E04 | Imperial completion | usable post-Imperial capability | research + production + infrastructure | exact world-state chain TBD | STRATEGIC | INFERRED | infrastructure/production may lag research | verify actual capability readiness | AEGIS VERIFY |
| ST03-E05 | Imperial timing | opponent timing relationship | threat/attack/resource systems | no predictive edge isolated | STRATEGIC | INFERRED | controller may be reactive only | identify predictive branch | AEGIS HYPOTHESIS |
| ST03-E06 | opportunity cost | age timing choice | no universal historical evaluator | none | STRATEGIC | AEGIS-GENERALIZATION | threshold policy may dominate | locate explicit scoring | DESIGN ONLY |

**Conclusion:** Imperial authorization is one of the strongest direct age-transition edges; strategic timing interpretation remains separate.

---

# 4. ST-04 — Enemy composition change → counter-composition

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST04-E01 | enemy military population / unit facts | enemy focus/target state | `threats.per` | approx. lines 31–52 | THREAT/CONTROL | DIRECT | focus selection may be target filtering, not classification | inspect downstream readers | INHERIT |
| ST04-E02 | focus player | military population measurement | `threats.per` | approx. lines 34–48 | THREAT | DIRECT | measurement may only support target selection | trace threat writers | INHERIT |
| ST04-E03 | enemy state | threat classification | `threats.per` | distributed branches | THREAT | DIRECT | classifications may be operational heuristics rather than persistent beliefs | show no downstream persistence | INHERIT |
| ST04-E04 | threat classification | response family | `threats.per` + production/strategy modules | distributed; exact cross-file chain TBD | THREAT/PRODUCTION | COMPOSED | independent rules may react to same observation | trace one cavalry branch end-to-end | VERIFY |
| ST04-E05 | observed composition | future enemy transition hypothesis | HD enemy/building/age/timing machinery | predictive branch not isolated | STRATEGIC | INFERRED | controller may remain present-state reactive | demonstrate explicit future-state branch | AEGIS HYPOTHESIS |
| ST04-E06 | requirement | candidate response tournament | distributed historical responses | none | STRATEGIC | AEGIS-GENERALIZATION | programmer may hard-code preferred responses | find shared candidate scorer | DESIGN ONLY |
| ST04-E07 | counter selection | changed capability relationship | production + military state | world-state validation required | STRATEGIC | INFERRED | counter may arrive too late | verify composition and outcome | AEGIS VERIFY |
| ST04-E08 | uncertainty | confidence-weighted belief | no explicit general confidence object established | none | STRATEGIC | AEGIS-GENERALIZATION | historical logic may be binary/threshold | find confidence persistence | DESIGN ONLY |

**Conclusion:** typed threat response is historically strong; unified counter tournaments and explicit predictive opponent models are not established.

---

# 5. ST-05 — Attack → retreat → regroup → restart

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST05-E01 | unfavorable attack condition | `retreat-now-goal` state | HD attack/retreat subsystem | approx. lines 32578–32595 from prior extraction | CONTROL | DIRECT | trigger may be narrower than generic unfavorable combat | inspect complete guard | INHERIT |
| ST05-E02 | retreat state | clear `attack-goal` | HD attack/retreat subsystem | approx. 32578–32595 | CONTROL | DIRECT | clearing may only terminate current attack | trace restart state | INHERIT |
| ST05-E03 | retreat | attack timer/reset lifecycle | HD attack/retreat subsystem | approx. 32578–32595 | CONTROL/RECOVERY | DIRECT | timer may be generic cooldown | trace timer readers/writers | INHERIT |
| ST05-E04 | reset state | restart eligibility | HD attack subsystem | `restart-attack-goal`; exact line TBD | RECOVERY | DIRECT | restart may be tied to another reset condition | isolate all writers/readers | VERIFY |
| ST05-E05 | retreat command/state | physical unit disengagement | no world-state proof in action sequence alone | none | WORLD-STATE | UNCERTAIN | units can remain in contact/path poorly | observe unit positions after command | VERIFY |
| ST05-E06 | tactical retreat | preserved military capital | distributed military state | no explicit preservation metric | STRATEGIC | INFERRED | retreat may satisfy only local rule | find downstream preservation objective | AEGIS MODEL |
| ST05-E07 | preserved objective | later attack restart | attack/restart state | exact chain TBD | STRATEGIC | COMPOSED | restart may be independently triggered | trace objective identity through reset | VERIFY |
| ST05-E08 | local engagement failure | strategic reassessment | reset machinery | no universal reassessment object | RECOVERY | AEGIS-GENERALIZATION | rule evaluation may simply resume | locate explicit reclassification | DESIGN ONLY |

**Conclusion:** controller-state retreat/reset behavior is direct; physical disengagement and strategic preservation require world-state evidence.

---

# 6. ST-06 — Fortification → siege

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST06-E01 | enemy fortification observation | `enemy-fortifications-goal` | HD fortification/attack state | exact line TBD; prior extraction confirms goal | CONTROL/MAP | DIRECT | flag may affect only attack delay | inspect readers | INHERIT |
| ST06-E02 | fortification state | attack delay/suppression | HD attack logic | prior casebook anchor; exact line TBD | CONTROL | DIRECT | delay may be timer-specific | inspect guard semantics | INHERIT |
| ST06-E03 | fortification | siege production | `units.per` + siege strategy rules | exact cross-file chain TBD | PRODUCTION | COMPOSED | siege may be produced for unrelated reasons | isolate fortification-conditioned siege writer | VERIFY |
| ST06-E04 | siege capability | changed objective conversion efficiency | military/attack outcome | no explicit universal efficiency metric | STRATEGIC | INFERRED | siege can fail from timing/position/target choice | measure objective progress | AEGIS VERIFY |
| ST06-E05 | repeated failed assault | capability mismatch diagnosis | no exact historical longitudinal counter | none | STRATEGIC | AEGIS-GENERALIZATION | source may simply retry with altered timers | find repeated-loss memory/threshold | DESIGN ONLY |
| ST06-E06 | mismatch diagnosis | change capability/route/target | distributed attack/threat/production behavior | exact chain TBD | STRATEGIC | AEGIS-GENERALIZATION | historical response may be narrower | identify alternatives | DESIGN ONLY |

**Conclusion:** fortification-aware attack suppression is direct; fortification→siege is composed, not a proven single historical rule.

---

# 7. ST-07 — Map / role classification → economic and military posture

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST07-E01 | `position-goal` | `strategy-goal` | HD role logic | approx. lines 5252–5262 from prior extraction | MAP/CONTROL | DIRECT | writer may special-case pocket only | inspect all position values | INHERIT |
| ST07-E02 | `position-goal` | `unit-goal` | HD role logic | approx. 5252–5262 | MAP/CONTROL | DIRECT | unit choice may be side effect of strategy | trace reader ownership | INHERIT |
| ST07-E03 | `position-goal` | `control-goal` | HD role logic | approx. 5252–5262 | MAP/CONTROL | DIRECT | control change may be pocket-specific | inspect additional roles | INHERIT |
| ST07-E04 | map/position role | economic posture | HD economy + position systems | distributed; exact chain TBD | MAP/RESOURCE | COMPOSED | economy changes may have independent causes | trace role-conditioned writes | VERIFY |
| ST07-E05 | role classification | relational strategic state | `position-goal` usage | approx. 5252–5262 | STRATEGIC | INFERRED | goal may only be an enum for branching | show relational readers | AEGIS MODEL |
| ST07-E06 | water/map state | naval/exploration posture | `watercontrol.per` + map controls | distributed | MAP/PRODUCTION | COMPOSED | water logic may operate independently | trace map-conditioned authorization | INHERIT PATTERN |
| ST07-E07 | role change | posture invalidation | no universal historical invalidation set | none | STRATEGIC | AEGIS-GENERALIZATION | source may classify once | observe reclassification | DESIGN ONLY |

**Conclusion:** direct `position-goal → strategy/unit/control` coupling is strong; the richer relational ontology is reconstructed.

---

# 8. ST-08 — Food-source exhaustion → renewable food

| Edge ID | From | To | Source module | Source location | Evidence type | Evidence grade | Alternative explanation | Falsifier | AEGIS status |
|---|---|---|---|---|---|---|---|---|---|
| ST08-E01 | boar/hunting state | hunter/work assignment | `boarhunting.per` | hunting/search block; exact depletion trigger TBD | RESOURCE/SEARCH | DIRECT | hunting may be a static early-game procedure | locate depletion-conditioned branch | INHERIT |
| ST08-E02 | live-boar/drop-site distance | hunting feasibility | `boarhunting.per` | approx. lines 374–388 | SEARCH/RESOURCE | DIRECT | geometry may only optimize target choice | trace action guard | INHERIT |
| ST08-E03 | food-source condition | farm goal | HD/Promisory farm strategy | exact writer TBD | RESOURCE | COMPOSED | farms may be scheduled by wood/age/population | locate depletion predicate | VERIFY |
| ST08-E04 | `save-wood-goal` | farm timing | gatherer/farm logic | exact writer TBD | RESOURCE | COMPOSED | save-wood may protect unrelated infrastructure | isolate farm-conditioned use | VERIFY |
| ST08-E05 | finite food decline | anticipated future food demand | no explicit depletion-rate estimator established | none | STRATEGIC | AEGIS-GENERALIZATION | source may react only to current availability | find forecast calculation | DESIGN ONLY |
| ST08-E06 | renewable food infrastructure | stabilized food throughput | farms/gatherers | world-state proof required | STRATEGIC | INFERRED | farm construction may be mistimed/insufficient | measure post-transition throughput | AEGIS VERIFY |
| ST08-E07 | food-source substitution | trajectory model | distributed food systems | no single historical trajectory object | STRATEGIC | INFERRED | independent source-specific rules may coexist | identify explicit forecast state | AEGIS MODEL |

**Conclusion:** food acquisition is clearly contextual/stateful; a single historical `depletion → farms` transition is not yet proven.

---

# 9. Strongest historical edges

The current evidence set supports these as the cleanest historical substrate:

1. `escrow state → can-research-with-escrow age/technology authorization`.
2. `position-goal → strategy-goal/unit-goal/control-goal` in the documented pocket case.
3. `enemy observations → military-population/focus/target state` in threat logic.
4. `retreat state → attack-goal / attack-status / timer-reset state` in the documented attack/retreat block.
5. `fortification state → attack suppression/delay`.
6. `boar/hunting geometry → hunting feasibility/selection`.
7. contextual gatherer state → resource-percentage changes.

These are the relationships from which AEGIS may safely reconstruct higher-order architecture, provided the inference is labeled.

# 10. Do-not-promote list

The following must **not** currently be presented as historical source facts:

- universal utility maximization;
- explicit marginal-value comparison of Feudal pressure versus Castle timing;
- explicit predictive opponent-transition model;
- one unified counter-composition tournament;
- physical retreat guaranteed by goal mutation;
- automatic fortification→siege causal selection;
- explicit finite-food depletion forecasting;
- universal confidence-weighted belief objects;
- universal strategic postcondition verification;
- asymmetric hysteresis as historical threshold doctrine.

These remain AEGIS design hypotheses/generalizations until direct source evidence is found.

# 11. Alternative-explanation discipline

For every reconstructed edge:

1. Could the observed writer be solving a narrower problem?
2. Could two co-occurring rules be independent rather than causal?
3. Could the apparent strategic state be only an implementation flag?
4. What observation would falsify the proposed interpretation?

A causal claim without a plausible alternative explanation and falsifier is incomplete.

# 12. Transition ownership reconstruction

Historical ownership is distributed and is **not** claimed to be centralized. The following is the AEGIS responsibility model extracted from that distribution:

| Responsibility | Historical evidence | AEGIS owner |
|---|---|---|
| Observation | facts, focus-player queries, object/search primitives | Observation controller |
| Classification | threat, enemy, map/role branches | Classification controller |
| Belief | distributed goals/SNs rather than explicit belief object | Belief controller |
| Objective | strategy/unit/control/attack goals | Strategic Objective controller |
| Commitment | escrow/resource-control/attack state | Commitment controller |
| Authorization | `can-*`, pending, goal/SN gates | Authority gate |
| Execution | train/build/research/attack/move actions | Execution adapter |
| Verification | subsequent observation/rules | explicit Verification controller |
| Recovery | reset/retreat/restart/fallback rules | Recovery controller |

# 13. Transition conservation invariant

Every AEGIS transition must account for scarce quantities:

| Dimension | Hidden cost | QC question |
|---|---|---|
| Resources | food/wood/gold/stone | What other capability lost this resource? |
| Villager time | travel/build/gather | Who pays the worker-time tax? |
| Production capacity | queue slots/buildings | What opportunity is displaced? |
| Military mass | units exposed/lost | Is enough force preserved? |
| Map access | routes/resources/territory | Did the transition surrender geography? |
| Information | stale/partial scouting | How much uncertainty remains? |
| Timing | delay to next capability | What window closes? |
| Optionality | locked resources/production | What alternatives become unavailable? |

A transition that appears to improve every dimension without a conversion cost is a QC warning.

# 14. Local / operational / global success invariant

Every AEGIS transition must distinguish:

`LOCAL SUCCESS → OPERATIONAL SUCCESS → GLOBAL STRATEGIC SUCCESS`

Examples:

- research accepted ≠ age transition strategically successful;
- siege unit trained ≠ fortification problem solved;
- retreat state entered ≠ army physically preserved;
- farm built ≠ food transition stabilized;
- role classified ≠ posture strategically correct.

# 15. Pass-8 falsification program

### Priority A — exact anchors

1. Isolate the exact Feudal-age writer/reader chain.
2. Isolate every `enemy-fortifications-goal` writer and reader.
3. Isolate every `restart-attack-goal` writer and reader.
4. Isolate exact `farm-goal` activation conditions.
5. Isolate all `position-goal` writers and downstream readers.
6. Isolate threat-class → production response for at least cavalry and ranged threats.
7. Isolate the complete Castle/Imperial age-state update chains.

### Priority B — causal falsifiers

8. Find cases where presumed upstream state changes but downstream action does not.
9. Find downstream actions that occur without the presumed upstream state.
10. Identify competing writers that explain the same action.
11. Identify self-disabling/reset rules that alter apparent causality.

### Priority C — programmer-mind reconstruction

12. Extract repeated `problem → workaround` comments.
13. Extract performance constraints explaining architectural compromises.
14. Identify where the programmer approximates a game concept because exact computation is too expensive.
15. Identify where the programmer preserves optionality versus deliberately locking resources/capability.

# 16. Pass-7 verdict

**PASS 7: ACCEPTED AS A PROVENANCE CONTROL LAYER; NOT YET COMPLETE AS AN EXACT SOURCE MAP.**

The important result is that the transition architecture survives stricter provenance control while several attractive historical claims are deliberately downgraded.

The historical programmer can safely be characterized as working with a recurring substrate of:

`game facts → compressed state → contextual resource/control changes → capability/attack behavior → reset/reassessment`.

The stronger architecture:

`OBSERVE → CLASSIFY → BELIEVE → DETECT TRANSITION → OBJECTIVE → REQUIREMENTS → CONSTRAINTS → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER → REASSESS`

is the **AEGIS design generalization**, not a claim that the historical code implemented centralized controllers in those terms.

**Next pass:** exact source-anchor extraction plus active falsification of the highest-value causal edges.
