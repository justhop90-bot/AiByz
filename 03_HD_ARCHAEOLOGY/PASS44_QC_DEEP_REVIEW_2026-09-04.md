# AEGIS Layer 2 — Pass 44 QC
# Deep Hostile Review / Errata

**Date:** 2026-09-04
**Reviewed artifact:** `PASS44_BYZANTINE_STRATEGIC_PROFILE_2026-09-04.md`
**Reviewed commit:** `a4d2eae0bcc980945dcc4e6510464fb47030207f`
**Layer:** 2 — research / archaeology only
**QC disposition:** **PASS WITH CORRECTIONS**
**Implementation status:** **ZERO** — this QC authorizes no `.per` work.

---

## 1. Executive QC verdict

Pass 44 is directionally strong and correctly respects the Layer-2 boundary, but it is **not clean enough to serve as an unqualified research authority**.

The core thesis survives hostile review:

> Byzantine strength is better understood as a broad response surface combined with discounted counter-capability, defensive persistence, information advantages, and multiple transition paths than as merely a defensive identity.

However, several claims are stronger than their evidence warrants. The most important corrections are:

1. Do not describe Cataphracts as a direct response to mounted threats without matchup evidence.
2. Do not describe saved food as automatically becoming capacity for other resources/technology; call it reduced food pressure instead.
3. Do not claim Byzantines can change composition “without abandoning the existing economic/military base” as an established fact. That is an AEGIS hypothesis.
4. Do not equate broad technology access with lower risk of dead-end composition. Broad access creates more transition possibilities, but the risk claim requires a defined metric.
5. Treat water-information chains and some map-role statements as generic strategic hypotheses, not Byzantine-specific facts.
6. The source/citation layer is not durable enough for a research baseline: the document contains tool-session citation tokens rather than stable repository source records.
7. Pass 44 itself correctly leaves the major quantitative matrix unresolved; therefore its opening claim of a “substantially mapped” capability surface should be read as **qualitative profile**, not completed capability matrix.

No fatal engine-semantic error was found in the reviewed Pass-44 text.

---

## 2. Boundary audit

### Result: PASS

The document explicitly states that the pass is research-only and that no `.per` implementation is authorized.

This is consistent with the corrected Layer-2 boundary: architecture and executable implementation remain Layer 3 work.

The reviewed commit adds a research document only. No runtime candidate or `.per` implementation belongs in this pass.

---

## 3. Current-data roster audit

### Result: PASS

The installed current `BYZANTINES.json` was checked directly.

The current file contains entries for:

- Arbalester
- Skirmisher / Elite Skirmisher
- Spearman / Halberdier
- Knight / Cavalier / Paladin
- Camel Rider / Heavy Camel Rider
- Onager
- Bombard Cannon
- Dromon
- Cataphract / Elite Cataphract
- Trebuchet
- Monk
- Siege Onager

The important correction is that **presence in the technology-tree JSON is not equivalent to availability**. The direct data check shows:

- `Onager`: `ResearchedCompleted`
- `Siege Onager`: `NotAvailable`

Therefore Pass 44's statement that Onager is available while Siege Onager is unavailable is correct.

Likewise:

- `Heavy Camel Rider`: `ResearchedCompleted`
- `Camel Rider`: `ResearchedCompleted`
- `Halberdier`: `ResearchedCompleted`
- `Paladin`: `ResearchedCompleted`
- `Dromon`: `ResearchedCompleted`
- `Bombard Cannon`: `ResearchRequired`

The last distinction matters: `ResearchRequired` means the capability exists in the civilization tree but is not initially completed. It should not be described as immediately available without the prerequisite/research state.

---

## 4. Civilizational bonus audit

### 4.1 Naval bonus — PASS

Official Update 169123 states that the Byzantine Fire Ship and Dromon attack-speed bonus increased from +20% to **25%**. citeturn1search7

Official Update 83607 records that Byzantines received Dromons and that the Fire Ship attack-speed bonus also applied to Dromons. citeturn1search5

Pass 44 is correct on this point.

### 4.2 Free Town Patrol — PASS

Official Update 51737 states that Town Patrol became free and instantly researched. citeturn0search3

Pass 44 is correct to treat this as an information-cost advantage.

### 4.3 Broad technology tree — PASS

Official Age of Empires II learning material explicitly describes Byzantines as having an almost full Technology Tree and presents that breadth as enabling different unit/composition choices. citeturn3search0

Pass 44 is correct on the factual breadth claim.

### 4.4 Food discount — QUALIFIED PASS

The Byzantine discounted food cost for the relevant counter-unit families is consistent with the project's established game-data/archaeology record.

However, Pass 44's wording should be tightened from:

> “more room for other resources / technology”

to:

> “reduced food pressure, potentially increasing the feasible budget for competing expenditures.”

The former implies a realized macroeconomic conversion that has not been measured. The latter is a defensible economic consequence.

---

## 5. Counter-matrix audit

### Result: PARTIAL / RESEARCH GAP

Pass 44 correctly says that a full counter matrix remains unresolved.

But some individual response lists are too permissive for a document that is explicitly moving toward a data-backed counter matrix.

### 5.1 Mounted-threat response list — correction required

Pass 44 lists:

- Camel Rider / Heavy Camel Rider
- Spearman / Pikeman / Halberdier
- Cataphract in some positional/compositional roles
- Monks where conversion is strategically viable
- ranged support depending on exact mounted target

The first two families are defensible as anti-mounted capability families.

The Cataphract entry is **too vague and potentially misleading**. Cataphracts are a heavy cavalry line with anti-infantry specialization; their inclusion as a mounted-threat response cannot be treated as a direct counter without explicit matchup evidence.

**QC correction:** classify Cataphracts as an alternative heavy-combat capability, not as a direct anti-mounted counter, until the unit-vs-unit matrix proves a relevant matchup.

Monks should similarly be classified as **conversion/control capability**, not a conventional counter line.

“Ranged support” is too unconstrained for a matrix. It should be replaced by explicit unit classes once the damage/armor/range data are extracted.

---

## 6. Archer-threat audit

### Result: QUALIFIED PASS

Skirmishers are an obvious anti-archer capability family, and the Byzantine food discount makes the economic relationship civilization-specific.

However, the statement:

> “Sustained counter-mass”

is a strategic hypothesis, not a direct consequence of the discount alone.

Sustained mass also depends on:

- food income,
- wood availability,
- production count,
- gold allocation elsewhere,
- population capacity,
- technology requirements,
- opponent counterpressure,
- survival rate.

**QC grade:** COMPOSED / PROBABLE, not DIRECT.

---

## 7. Infantry-threat audit

### Result: PASS WITH SCOPE LIMIT

The listed response families are plausible, but “siege” is a capability class rather than a counter relationship.

Future matrix work must identify the specific target relationship:

```text
TARGET UNIT CLASS
→ DAMAGE MODEL
→ BONUS DAMAGE
→ TARGET ARMOR
→ RANGE / SPEED
→ PRODUCTION COST
→ EFFECTIVE RESPONSE
```

Do not allow “siege counters infantry” to survive as a generic truth in the final matrix without target-specific qualification.

---

## 8. Mounted-architecture audit

### Result: PASS

The separation between:

```text
Knight → Cavalier → Paladin
Camel Rider → Heavy Camel Rider
Cataphract → Elite Cataphract
```

is directly supported by the current technology-tree data.

The strategic conclusion that these should not be collapsed into one generic “cavalry” variable is a sound research abstraction and is compatible with the historical Promisory finding that `cavalry` can be a mutable aggregate channel.

The stronger phrase “not a sufficient strategic state variable for Byzantine planning” should be understood as an **AEGIS design hypothesis**, not as a discovered historical programmer rule.

---

## 9. Technology-tree reasoning audit

### Result: QUALIFIED PASS

The following inference is too strong:

```text
HIGH OPTION COUNT
→ LOWER RISK OF DEAD-END COMPOSITION
```

A high option count does not mathematically establish lower dead-end risk.

What is directly supported is:

```text
HIGH OPTION COUNT
→ MORE AVAILABLE TRANSITION PATHS
```

What is composed/inferred is:

```text
MORE TRANSITION PATHS
→ POTENTIALLY GREATER RECOVERY / ADAPTATION CAPACITY
```

The latter needs operational definitions and empirical testing.

---

## 10. Naval audit

### Result: PASS

The current official record supports the 25% attack-speed statement. citeturn1search7turn1search5

One wording correction remains:

> “Water information → Fire-Ship / Galley response”

is not a discovered Byzantine-specific controller chain. It is a strategic hypothesis combining generic scouting with Byzantine naval capabilities.

It should be labeled **AEGIS-GENERALIZATION** until supported by Byzantine-specific behavioral evidence.

---

## 11. Siege audit

### Result: PASS

The Pass-44 distinction between broad siege access and maximum siege access is useful.

The direct data check confirms the critical boundary:

```text
Onager        = available
Siege Onager  = unavailable
```

This is an important finding and should remain in the baseline.

However, the phrase “force substitution” is a strategic abstraction, not a direct game-data relationship. Keep the evidence grade explicit.

---

## 12. Monastery audit

### Result: QUALIFIED PASS

The current tree supports a substantial monastery technology surface and the monk healing bonus is historically/officially documented.

The strategic chain:

```text
SUPPORT / CONTROL
→ CONVERSION / HEALING / RELIC ECONOMICS
```

is reasonable but combines multiple distinct mechanisms.

Future research should separate:

- healing value,
- conversion value,
- relic value,
- technology cost,
- monk production cost,
- monk survival.

Do not collapse all monastery value into one scalar until the metric is defined.

---

## 13. “Without abandoning the existing base” — correction required

The executive characterization says Byzantine power is concentrated in the ability to change composition:

> “without abandoning the existing economic/military base.”

This is rhetorically strong but not established by the evidence.

A transition can still impose:

- new production buildings,
- new upgrades,
- different resource ratios,
- additional infrastructure,
- opportunity cost,
- idle production,
- population restructuring.

**QC replacement concept:**

> “with multiple paths for changing military capability while retaining some existing infrastructure and economic investment.”

Even that should remain COMPOSED rather than DIRECT.

---

## 14. Map-role audit

### Result: INFERENCE ONLY

The Open / Closed / Water map sections are useful hypotheses but are not data-backed map-role conclusions.

The wording “Likely values” is appropriate, but the sections should carry an explicit evidence grade:

**INFERRED / AEGIS-GENERALIZATION.**

The project must not later cite these sections as historical Byzantine doctrine.

---

## 15. Provenance audit

### Result: FAIL — documentation quality, not game-data correctness

The pass embeds citation tokens such as `citeturn...` that are valid within the research session but are not durable repository provenance identifiers.

The document does contain named official update numbers, which makes the claims recoverable, but a future engineer should not have to reconstruct tool-session references.

The durable baseline should record:

```text
SOURCE
TITLE
PUBLISHER
DATE
URL / REPOSITORY PATH
DATA VERSION
EXTRACTION DATE
HASH WHEN PRACTICAL
```

This is a **documentation QC failure**, not a factual failure.

---

## 16. Completeness audit against Pass-44's stated next step

### Result: PASS — intentionally incomplete

Pass 44 explicitly identifies these as remaining gaps:

- exact current Byzantine modifiers,
- complete unit-line cost matrix,
- counter matrix,
- production topology,
- Byzantine-specific historical AI behavior,
- replay corroboration,
- map-conditioned strategy,
- transition economics.

That is internally consistent with the document's conclusion that the next pass should construct the capability/counter/transition matrix.

Therefore the absence of those quantitative tables is not itself a defect in Pass 44. The defect would be claiming they had already been completed.

---

## 17. Six-month re-entry test audit

### Result: PASS

The re-entry questions are appropriate and explicitly preserve the Layer-2/Layer-3 boundary.

One addition is required for future auditability:

> Which claims in the profile are DIRECT, which are COMPOSED, which are INFERRED, and which are AEGIS-GENERALIZATION?

This classification is more important than memorizing the prose.

---

## 18. Hostile disposition by claim class

| Claim class | QC result | Disposition |
|---|---|---|
| Layer-2 boundary | PASS | Retain |
| Current Byzantine roster | PASS | Retain |
| Onager available / Siege Onager unavailable | PASS | Retain |
| Dromon current access | PASS | Retain |
| 25% Fire Ship/Dromon attack-speed bonus | PASS | Retain |
| Free Town Patrol | PASS | Retain |
| Broad tech-tree characterization | PASS | Retain |
| Discounted counter-unit economics | QUALIFIED PASS | Retain with stronger evidence labeling |
| Cataphract as mounted-threat response | WEAK | Reclassify |
| Food savings → other-resource capacity | OVERSTATED | Reword |
| Broad tech → lower dead-end risk | UNPROVEN | Reword |
| Composition change without abandoning base | OVERSTATED | Reword / mark composed |
| Map-role sections | INFERRED | Mark explicitly |
| Optionality as measurable strategic value | AEGIS hypothesis | Retain as hypothesis |
| Historical programmer intent | PASS | Correctly not claimed |
| Durable source provenance | FAIL | Improve in subsequent artifact |

---

## 19. Severity ranking

### P0 — none

No P0 correctness or Layer-2 boundary violation found in Pass 44.

### P1 — three wording/evidence problems

1. Cataphract included too loosely in mounted-threat response set.
2. “Without abandoning the existing economic/military base” overstates transition evidence.
3. Citation tokens are not durable provenance.

### P2 — several inference-strength issues

- saved food → other resource capacity,
- broad tech → lower dead-end risk,
- generic water information chain,
- generalized siege/counter statements,
- map-role hypotheses lacking explicit evidence labels.

### P3 — presentation only

Some capability descriptions could be normalized into a structured matrix earlier, but this is appropriate work for Pass 45 rather than a reason to reject Pass 44.

---

## 20. Final QC verdict

**PASS 44 remains accepted as a qualitative Byzantine strategic profile, but it is not a clean quantitative capability authority.**

The central thesis survives.

The following statements are now considered authoritative QC constraints for Pass 45 and later work:

```text
1. UNIT AVAILABILITY ≠ STRATEGIC PRIORITY
2. UNIT PRESENCE ≠ COUNTER RELATIONSHIP
3. LOWER FOOD COST ≠ FREE CAPABILITY
4. TECH-TREE BREADTH ≠ AUTOMATIC FLEXIBILITY IN PRACTICE
5. MAP ROLE ≠ HISTORICAL DOCTRINE
6. CONTROL MECHANISM ≠ STRATEGIC INTENT
7. OPTION COUNT ≠ OPTION VALUE
8. NOMINAL COUNTER BONUS ≠ EFFECTIVE BATTLEFIELD RESULT
9. UNIT COST ≠ TRANSITION COST
10. TRANSITION PATH ≠ LOW-COST TRANSITION
```

The next pass must therefore replace qualitative capability language with **directly extracted unit/technology/building/resource/transition evidence** wherever possible.

No `.per` implementation is authorized by this QC.

---

## 21. Six-month re-entry checkpoint

A future engineer should be able to state, without relying on memory:

- which Byzantine claims are directly data-backed;
- which are official-patch-backed;
- which are composed consequences;
- which are inference;
- which are AEGIS hypotheses;
- why Siege Onager is unavailable despite appearing in the technology-tree JSON;
- why a discounted counter unit is not automatically the cheapest total strategic response;
- why a unit's nominal counter relationship is insufficient without cost, timing, production, and battlefield-effect evidence;
- why Pass 45 must build the matrix before Layer 3 architecture begins.

**QC status: ACCEPTED WITH ERRATA.**
