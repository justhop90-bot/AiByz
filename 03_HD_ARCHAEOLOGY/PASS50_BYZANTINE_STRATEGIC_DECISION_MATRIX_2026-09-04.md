# AEGIS Layer 2 — Pass 50
# Byzantine Strategic Decision Matrix

**Date:** 2026-09-04  
**Layer:** 2 — research / archaeology only  
**Status:** **PASS — decision matrix established; historical-HD coverage mapped; implementation remains ZERO**  
**Implementation:** **ZERO** — no `.per`, controller, production policy, runtime code, or deployment created

---

## 0. Mission

Pass 49B established the Byzantine player/mechanics model and cross-referenced it with historical HD AI. Pass 50 turns that knowledge into a **research-grade decision matrix**.

The question is not:

> “What unit counters X?”

The question is:

> **Given the observed threat, required capability, Byzantine state, available infrastructure, timing, risk, and strategic horizon, which candidate response is actually feasible and valuable?**

This is a decision-archaeology artifact, not an implementation specification.

The Layer-2 boundary remains absolute:

```text
RESEARCH
→ FORMALIZE
→ COMPARE
→ IDENTIFY EVIDENCE
→ IDENTIFY GAPS

NO IMPLEMENTATION
```

---

# 1. Canonical decision chain

The archaeological unit remains the complete control/decision chain established in Pass 49:

```text
OBSERVE
↓
REPRESENT
↓
ASSESS
↓
OBJECTIVE
↓
REQUIRED CAPABILITY
↓
CANDIDATES
↓
HARD CONSTRAINTS
↓
EVALUATE
↓
COMMIT
↓
AUTHORIZE
↓
ACT
↓
VERIFY WORLD EFFECT
↓
UPDATE
↓
REASSESS
```

Pass 50 adds the Byzantine candidate-evaluation layer:

```text
THREAT
↓
REQUIRED CAPABILITY
↓
CANDIDATE SET
↓
HARD FEASIBILITY
↓
ECONOMIC / TEMPORAL / POSITIONAL EVALUATION
↓
RISK + TRANSITION BURDEN
↓
OPTION VALUE + COMMITMENT
↓
CHOOSE
```

No single factor is sufficient.

---

# 2. Evidence hierarchy

### DIRECT
Current game rule, installed data, or historical AI source explicitly establishes the proposition.

### COMPOSED
Multiple DIRECT observations form a control chain without requiring a new causal assumption.

### INFERRED
The strategic interpretation is strongly supported but not explicitly encoded.

### AEGIS-GENERALIZATION
A useful model derived from the evidence but not claimed as historical engine design.

### UNCERTAIN
Evidence is insufficient to close the proposition.

The distinction is mandatory. A useful strategy model must not be silently converted into a claim about historical AI behavior.

---

# 3. Candidate evaluation dimensions

Every serious Byzantine response candidate should eventually be evaluated against:

| Dimension | Research question |
|---|---|
| Required capability | What battlefield/strategic property actually solves the problem? |
| Current capability | What can Byzantines already field? |
| Hard feasibility | Is the candidate currently available at all? |
| Resource cost | What food/wood/gold/stone burden exists? |
| Tech cost | What research investment is required? |
| Infrastructure | What buildings must exist or be added? |
| Production continuity | Can existing production be reused? |
| Timing | How long until meaningful capability exists? |
| Mobility | Can it reach the threatened location in time? |
| Map dependence | Does the answer depend on terrain/resources/water? |
| Support | Does it require another unit/system to function well? |
| Risk | What happens if the assessment is wrong? |
| Transition burden | What economy/production/tech must be abandoned or changed? |
| Option value | Does the investment preserve useful future branches? |
| Commitment | How difficult is reversal? |
| Historical HD coverage | Is there evidence the old AI represented this choice? |
| Verification | Can world-state completion be directly observed? |

The matrix is intentionally multidimensional. “Best counter” is not a stable scalar property.

---

# 4. Threat class: enemy cavalry

## Required capability

The actual requirement is not “anti-cavalry unit.” It is some combination of:

```text
STOP / DETER / TRADE FAVORABLY AGAINST
MOBILE MOUNTED PRESSURE
```

Relevant Byzantine candidate classes include:

```text
SPEAR-LINE
CAMEL-LINE
STATIC DEFENSE
MONK / CONVERSION SUPPORT
OWN HEAVY CAVALRY
POSITIONAL RESPONSE
MIXED COMPOSITION
```

## Candidate matrix

| Candidate | Primary strength | Main burden | Timing profile | Strategic role | HD evidence |
|---|---|---|---|---|---|
| Spear-line | Low-cost anti-cavalry mass; defensive efficiency | Low mobility; vulnerable to ranged/support | Fast once barracks exists | Area denial / defensive mass | Historical production substrate; specific Byzantine decision chain incomplete |
| Camel-line | Mobile mounted response; dedicated anti-cavalry capability | Gold requirement; stable + tech/age constraints | Moderate; scales with stable production | Mobile interception / counter-pressure | **STRONG** historical Byzantine cavalry→camel chain |
| Static defense | Buys time; leverages Byzantine building durability | Location-bound; does not remove threat | Immediate if structures already exist | Delay / resource protection | Historical building fallback evidence; Byzantine-specific HP use not proven |
| Monk | Converts or heals; high strategic leverage in some fights | Fragile; micro/position dependent; gold | Slower and situational | High-value disruption/support | Historical monk systems exist; explicit Byzantine cavalry counter policy not closed |
| Own heavy cavalry | Mobility and direct combat; can contest map | Expensive; may not be ideal trade into dedicated counters | Moderate/slow | Counter-pressure / initiative | Historical cavalry production exists; no universal counter optimizer proven |
| Positional | Uses walls, choke points, TCs, terrain, buildings | Map dependent | Potentially immediate | Convert space into time | Historical positional/scout/building evidence; strategic causal layer inferred |
| Mixed | Combines anti-cavalry with support | Higher coordination/resource burden | Depends on components | Robust response | AEGIS-generalization; no universal historical optimizer proof |

### Byzantine-specific insight

The -25% food discount on Spearman and Camel families changes their feasibility frontier. It does **not** make every candidate equally cheap because wood/gold, infrastructure, and production remain constraints.

### Strong historical closure

The best-supported Byzantine-specific historical pattern remains:

```text
ENEMY MOUNTED OBSERVATION
→ CAVALRY / CAVARCHER AGGREGATION
→ CONTEXTUAL CAMEL CONDITIONS
→ PRODUCTION AUTHORIZATION
→ TRAIN CAMEL
```

Historical `threats.per` and `units.per` support this chain. Replay evidence independently corroborates that Byzantine camel-line production occurred after recorded enemy knight production in two analyzed games.

The replay evidence does **not** prove that the hidden threat aggregate caused those camel queues.

### Decision principle

```text
MOBILE THREAT
+
NEED FOR INTERCEPTION
→
CAMEL / MOBILE RESPONSE GAINS VALUE
```

But if immediate survival is the only objective and infrastructure is unavailable, static defense or spear mass can dominate on timing.

---

# 5. Threat class: enemy infantry

## Required capability

The required capability is:

```text
ANTI-INFANTRY DAMAGE
+
SUFFICIENT SURVIVABILITY
+
ABILITY TO ENGAGE THE ACTUAL MASS
```

Relevant Byzantine candidates:

```text
CATAPHRACT
ARCHER / SKIRMISHER SUPPORT
SIEGE
POSITION
MIXED COMPOSITION
```

## Candidate matrix

| Candidate | Primary strength | Main burden | Strategic role | HD evidence |
|---|---|---|---|---|
| Cataphract | Mobile heavy anti-infantry cavalry | Food/gold + Castle infrastructure + upgrades | Direct heavy anti-infantry | Historical production/cavalry substrate; explicit infantry→Cataphract decision chain not yet closed |
| Archer/skirmisher | Ranged anti-infantry pressure; kiting/position potential | Vulnerable if caught; support/position required | Ranged damage layer | Historical ranged production is established; specific Byzantine policy mapping incomplete |
| Siege | Area damage / mass punishment | Expensive, vulnerable, positioning dependent | Mass-destruction capability | Historical siege control exists; target-selection policy requires more archaeology |
| Position | Choke/terrain/walls/Towers can reduce effective mass | Map dependent; does not itself destroy army | Damage avoidance / delay | Historical position/building systems; strategic interpretation inferred |
| Mixed | Reduces single-counter failure modes | Expensive and coordination-heavy | Robust composition | AEGIS-generalization |

### Cataphract invariant

This pass preserves the Pass-47 invariant:

```text
MECHANICAL FAMILY = CAVALRY
STRATEGIC ROLE = ANTI-INFANTRY / HEAVY COMBAT
```

Calling Cataphracts “anti-cavalry” merely because they are durable against some mounted threats is an ontology error.

### Logistica decision dimension

Logistica should be treated as a **role-amplifying investment**, not a universally mandatory upgrade.

The player question is:

```text
EXPECTED VALUE OF TRAMPLE / ANTI-INFANTRY IMPROVEMENT
vs
FOOD + GOLD + RESEARCH TIME + LOST ALTERNATIVE INVESTMENT
```

Current structured reference lists Logistica as adding trample functionality and +6 attack versus Infantry; official historical balance notes establish its 800 food / 600 gold cost after reduction. These are current/reference data and historical patch evidence respectively; they are not substitutes for a fresh installed-data join.

---

# 6. Threat class: enemy ranged mass

## Required capability

```text
REACH
+
MOBILITY OR RANGE
+
SURVIVABILITY UNDER FIRE
```

Candidate classes:

```text
OWN CAVALRY
CAMELS WHERE APPROPRIATE
SIEGE
SKIRMISHER
POSITION / TERRAIN
MIXED
```

The critical research conclusion is that “ranged” is insufficiently specific.

The decision changes according to:

```text
ARCHER
CROSSBOW
HAND CANNONEER
RANGED UNIQUE UNIT
CAVALRY ARCHER
SIEGE SUPPORT
```

Therefore future decision research should use **capability signatures**, not only unit-line labels.

### Byzantine advantage

The broad technology tree gives multiple candidate families, but the candidate must still satisfy infrastructure, resource, timing, and battlefield requirements.

Historical HD mapping is presently partial. Historical production and threat systems are known; explicit Byzantine ranged-threat candidate scoring is not proven.

---

# 7. Threat class: enemy siege

## Required capability

```text
LOCATE
REACH
AND REMOVE HIGH-VALUE SIEGE
```

Candidate classes:

```text
MOBILE CAVALRY
RANGED FIRE
OWN SIEGE
MONK / CONVERSION IN SPECIAL CASES
POSITIONAL AVOIDANCE
```

The strategic problem is fundamentally different from a normal unit-vs-unit counter because siege often acts as a **force multiplier**.

Therefore candidate evaluation must include:

```text
TARGET VALUE
+
PROTECTION
+
ACCESS
+
TIME TO CONTACT
+
RISK OF OVERCOMMITMENT
```

Historical HD archaeology has attack groups, target objects, target points, and attack/retreat state, but a complete generic siege-target optimizer is not yet demonstrated.

---

# 8. Threat class: economic pressure / raiding

The required capability may be:

```text
DETECTION
+
INTERCEPTION
+
STATIC DEFENSE
+
VILLAGER SURVIVAL
+
COUNTER-RAID
```

This is where Byzantine information and building bonuses interact strongly at the player level:

```text
EARLIER DETECTION
+
MORE DURABLE DEFENSIVE INFRASTRUCTURE
→
MORE RESPONSE WINDOW
```

The relationship is strategically compelling but must not be mislabeled as a historically encoded Byzantine optimization unless direct evidence is found.

Historical AI contains scouting, town-under-attack, building fallback, attack, and threat systems. The full Byzantine-specific economic-defense policy remains an open research question.

---

# 9. Water / naval pressure

The current naval system must be used; older naval assumptions are invalidated where the 2026 overhaul changed the topology.

Official Update 169123 introduced a new Hulk-line counter to Fire Ships and increased the Byzantine Fire Ship/Dromon attack-speed bonus to +25%. citeturn0search4

Greek Fire currently provides Fire Ships +1 range and increases Dromon/Bombard Tower blast radius. citeturn0search0

Therefore naval decision research must distinguish:

```text
ANTI-FIRE-SHIP
ANTI-FAST-SHIP
ANTI-SHIP
ANTI-BUILDING
SHORELINE SIEGE
```

Dromon is especially important because its role is anti-building/area effect rather than a generic close-range ship. Official documentation describes it as a long-range area-effect anti-building siege warship that cannot attack at close range. citeturn0search9

### Research status

Current Byzantine naval mechanics are understood sufficiently to prevent old-system contamination, but the historical HD naval policy mapping is **not closed**.

---

# 10. Cross-candidate decision model

The most important result of Pass 50 is that the candidate set should not be ranked by a single static counter table.

A candidate's research score should be thought of as:

```text
VALUE
=
CAPABILITY FIT
×
FEASIBILITY
×
TIMING VALUE
×
SURVIVABILITY
×
OPTION VALUE
```

with deductions conceptually arising from:

```text
RESOURCE COST
+
TECH COST
+
INFRASTRUCTURE COST
+
TRANSITION COST
+
RISK
+
COMMITMENT
+
POSITIONAL DEPENDENCE
```

This is an **AEGIS-generalization**, not a claim that historical HD AI literally computed this equation.

The exact numerical form is intentionally not fixed in Layer 2.

---

# 11. Hard constraints versus soft evaluation

This distinction is essential.

## Hard constraints

Examples:

```text
WRONG AGE
NO REQUIRED BUILDING
TECH NOT AVAILABLE
UNIT NOT AVAILABLE
INSUFFICIENT RESOURCES
NO PRODUCTION CAPACITY
POPULATION BLOCK
MAP / LOCATION IMPOSSIBILITY
```

A candidate failing a hard constraint is not merely “lower score.” It is **currently infeasible**.

## Soft evaluation

Once feasible, evaluate:

```text
COST
TIMING
TRADE QUALITY
MOBILITY
SUPPORT
RISK
OPTION VALUE
COMMITMENT
NEXT-THREAT COMPATIBILITY
```

This separation prevents an important category error:

```text
AVAILABLE
≠
GOOD
```

and:

```text
UNAVAILABLE
≠
BAD
```

The second candidate may become the best response after an enabling transition.

---

# 12. Transition decision

A Byzantine player often chooses not merely among current units but among **current response** and **future response**.

Transition burden is modeled as:

```text
RESOURCE COST
+
TECH COST
+
INFRASTRUCTURE COST
+
PRODUCTION DISRUPTION
+
ECONOMIC REALLOCATION
+
TIMING LOSS
+
LOST MOMENTUM
+
RISK
```

Transition benefit is:

```text
NEW CAPABILITY
+
COUNTER VALUE
+
TEMPO
+
OPTIONALITY
+
STRATEGIC ACCESS
```

Thus:

```text
CURRENTLY BEST
≠
BEST AFTER TRANSITION
```

This is particularly important for Byzantines because broad technology access increases the number of plausible future branches.

---

# 13. Commitment and reversibility

A response should be classified by how strongly it commits the player.

### Low commitment

Examples:

```text
small defensive wall
limited spear addition
small scout detour
```

### Medium commitment

Examples:

```text
additional production building
sustained camel production
ranged support mass
```

### High commitment

Examples:

```text
large Cataphract investment
Logistica
major technology transition
large infrastructure expansion
Imperial timing commitment
```

The exact classification is contextual.

A response with high commitment should require stronger evidence or higher expected value before selection.

---

# 14. Information and decision quality

Pass 49B established that information value is not simply “more vision.”

A useful conceptual relation is:

```text
VALUE OF INFORMATION
≈
EXPECTED DECISION IMPROVEMENT
−
INFORMATION ACQUISITION COST
```

For Byzantines, free baseline vision increases the potential value of timely observation because a broad candidate set exists.

But information can become stale:

```text
OBSERVATION
+
AGE
+
LAST CONFIRMATION
=
INFORMATION QUALITY
```

Therefore the decision matrix should eventually distinguish:

```text
CONFIRMED THREAT
LIKELY THREAT
STALE THREAT
UNKNOWN
```

The historical HD threat aggregate demonstrates classification/aggregation, not a proven probabilistic belief model.

---

# 15. Strategic substitution

The matrix confirms a major Byzantine property:

```text
ONE OBJECTIVE
→
MULTIPLE CAPABILITY PATHS
```

Example:

```text
OBJECTIVE = SURVIVE CAVALRY RAID

PATH A = SPEARS
PATH B = CAMELS
PATH C = STATIC DEFENSE
PATH D = MONKS
PATH E = MIXED
PATH F = POSITIONAL DENIAL
```

The best path changes with state.

This is the strategic meaning of a broad technology tree: **not all choices are equally good; many choices can satisfy different versions of the same requirement.**

---

# 16. Historical HD correspondence map

| Strategic concept | Historical evidence | Status |
|---|---|---|
| Enemy threat aggregation | `threats.per` | DIRECT |
| Cavalry aggregate | `threats.per` | DIRECT |
| Camel production ladder | `units.per` / `traincamel` | DIRECT |
| Cavalry→camel contextual chain | threats + units | COMPOSED / STRONG |
| Feasibility gates | age, resources, availability, research, population | DIRECT / COMPOSED |
| Escrow | `escrow.per` | DIRECT |
| Search before commitment | attack/scout search systems | DIRECT / COMPOSED |
| Attack state | attack goals/status/timers | DIRECT |
| Retreat/restart lifecycle | attack/retreat goals/timers | DIRECT |
| Production authorization | train conditions and production flags | DIRECT / COMPOSED |
| Building fallback | `buildings.per` | DIRECT |
| Byzantine building-HP optimization | no direct causal chain yet | OPEN |
| Byzantine free-vision optimization | no direct causal chain yet | OPEN |
| Byzantine Imperial-cost optimization | no direct causal chain yet | OPEN |
| Infantry→Cataphract strategic decision | not closed | OPEN |
| Multi-candidate counter scoring | not demonstrated | OPEN |
| Probabilistic belief | not demonstrated | OPEN |
| Full world-outcome verification | partial | OPEN |
| Current naval decision policy | historical mapping incomplete | OPEN |

---

# 17. New research invariant: counter quality is state-relative

The phrase:

```text
X COUNTERS Y
```

should be treated as shorthand for a conditional statement.

A more correct representation is:

```text
X PROVIDES CAPABILITY C
WHICH CAN SATISFY REQUIREMENT R
UNDER CONDITIONS S
AT COST K
WITH TIMING T
AND RISK Q
```

Therefore:

```text
NOMINAL COUNTER
≠
EFFECTIVE RESPONSE
```

This is now a canonical AEGIS research invariant.

---

# 18. New research invariant: capability fit precedes unit choice

The correct order is:

```text
THREAT
↓
REQUIRED CAPABILITY
↓
CANDIDATE CLASSES
↓
SPECIFIC UNIT
```

Not:

```text
THREAT
↓
FAVORITE UNIT
```

This distinction is critical for a professional AI system because it prevents hard-coding unit labels into strategic concepts.

---

# 19. New research invariant: feasibility is not evaluation

The system should conceptually perform:

```text
CAN I DO IT?
↓
IF YES:
IS IT GOOD?
```

not:

```text
EVERYTHING GETS ONE SCORE
```

The first formulation respects engine legality and avoids nonsensical candidate comparisons.

---

# 20. New research invariant: transition is itself a candidate

The decision set is not only:

```text
SPEAR vs CAMEL vs CATAPHRACT
```

It may also be:

```text
CURRENT RESPONSE
vs
TRANSITION TO NEW RESPONSE
```

This is especially relevant to Byzantines because the civilization's broad technology tree and cheaper Imperial Age create meaningful future capability branches.

---

# 21. Six-month re-entry test

A future engineer should be able to answer all of the following without relying on this document's prose:

1. Why is “counter” an insufficient strategic primitive?
2. What is the required capability for cavalry pressure?
3. Which Byzantine candidates can satisfy it?
4. Which candidates are mobile versus positional?
5. Why does the -25% discount not eliminate wood/gold/infrastructure constraints?
6. What is the Cataphract mechanical-family/strategic-role invariant?
7. Why can Cataphract be anti-infantry without being classified as an anti-cavalry unit?
8. What historical Byzantine cavalry→camel chain is actually proven?
9. What does replay evidence corroborate and what does it fail to prove?
10. Why are hard constraints separated from soft evaluation?
11. What constitutes transition burden?
12. What constitutes option value?
13. Why is information quality time-dependent?
14. Why is a broad technology tree an option-space property rather than a guarantee of strategic superiority?
15. Which Byzantine-specific strategic mappings remain open in historical HD AI?
16. What changed in current naval decision research after the 2026 naval overhaul?
17. Why must Dromon be treated as a specialized long-range anti-building/area-effect capability rather than a generic warship?
18. What is the difference between DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, and UNCERTAIN?
19. Was any Layer-3 implementation created by this pass?
20. What should Pass 51 investigate?

Expected final answer to #19:

```text
NO.
IMPLEMENTATION REMAINS ZERO.
```

---

# 22. Pass 50 verdict

**PASS.**

Pass 50 establishes a research-grade Byzantine strategic decision matrix and confirms that counter selection is fundamentally a **state-relative capability-selection problem**, not a static lookup table.

The strongest historical closure remains the mounted-threat → cavalry aggregate → camel production pathway.

The most important unresolved mappings are:

```text
INFANTRY → CATAPHRACT DECISION
BYZANTINE BUILDING HP → STRATEGIC POLICY
FREE VISION → STRATEGIC POLICY
IMPERIAL DISCOUNT → TIMING POLICY
MULTI-CANDIDATE COUNTER SCORING
BELIEF / CONFIDENCE
CURRENT NAVAL POLICY
WORLD-OUTCOME VERIFICATION
```

These gaps are now explicit rather than silently assumed.

**Layer-2 implementation count: 0.**

---

# 23. Sources

Current official Byzantine/naval mechanics:

- Age of Empires II: Definitive Edition Update 169123 — Naval Overhaul and Byzantine +25% Fire Ship/Dromon attack speed.
- Age of Empires II: Definitive Edition Update 87863 — current Greek Fire effects.
- Age of Empires II: Definitive Edition Update 51737 — Town Patrol free/instant.
- Age of Empires II: Definitive Edition Update 83607 — Dromon and Byzantine naval topology.

Current structured Byzantine reference:

- AoE2 Insights — Byzantines civilization page.

Historical AI sources and installed/local archaeology are the primary evidence for the HD control-chain conclusions; they remain distinguished from current game-balance sources.

---

# 24. Layer boundary declaration

```text
LAYER 2
========
RESEARCH       YES
ARCHAEOLOGY    YES
MATRIX         YES
EVIDENCE       YES
STRATEGIC MODEL YES

.PER CREATION  NO
CONTROLLER     NO
RUNTIME CODE   NO
DEPLOYMENT     NO

LAYER 3
========
IMPLEMENTATION AUTHORITY
```

**Pass 50 closes as research only.**
