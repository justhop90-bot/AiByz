# AEGIS Layer 2 — Pass 47
# Cataphract Anti-Infantry Role & Matchup Archaeology

**Date:** 2026-09-05  
**Layer:** 2 — research / archaeology only  
**Predecessor:** Pass 46 — Direct Combat / Economic Matrix  
**Status:** PASS — STRATEGIC ROLE CONFIRMED; LOCAL-DATA EXTRACTION DEFERRED  
**Implementation:** **ZERO** — no `.per`, no controller, no production policy, no runtime deployment

---

## 0. Mission

Pass 47 resolves the specific ontology issue raised during Pass 46:

> **Cataphract is anti-infantry in strategic terms, regardless of its mechanical/game-ID classification as cavalry.**

This is now treated as an AEGIS research invariant.

The purpose of this pass is not to make Cataphract an anti-infantry *game class*. It is to document why a strategic capability model must represent Cataphract as an anti-infantry capability while preserving the engine's cavalry identity and its actual combat mechanics.

---

# 1. Core ontology

```text
ENGINE ONTOLOGY
    ↓
mechanical family / armor classes / unit IDs

COMBAT MECHANICS
    ↓
attack / bonus / armor / rate / trample / mobility

STRATEGIC FUNCTION
    ↓
what problem the unit solves in an army
```

These layers must never be collapsed.

For Cataphract:

```text
mechanical family = cavalry
strategic role    = anti-infantry
production        = Castle
```

**Evidence:** mechanical identity DIRECT; strategic role DIRECT/COMPOSED from current reference material and explicit anti-infantry combat properties.

---

# 2. Direct combat evidence

Current reference material reports:

| Capability | Cataphract | Elite Cataphract |
|---|---:|---:|
| Food | 70 | 70 |
| Gold | 75 | 75 |
| HP | 110 | 150 |
| Base melee attack | 9 | 12 |
| Bonus vs Infantry | +9 | +12 |
| Melee armor | 2 | 2 |
| Pierce armor | 1 | 1 |
| Reload | 1.8 s | 1.7 s |
| Speed | 1.35 | 1.35 |
| Production | Castle | Castle |
| Production time | 20 s | 15 s |
| Anti-cavalry bonus resistance | +12 | +16 |

Reference: Age of Empires Series Wiki Cataphract entry and current unit reference pages. These values are external research evidence and must be reconciled against the installed `.dat` before becoming local-data authority.

The key strategic signal is not merely that Cataphract is cavalry. It is the combination of:

```text
HIGH MELEE COMBAT
+ INFANTRY BONUS
+ ANTI-CAVALRY BONUS RESISTANCE
+ MASS-COMBAT / TRAMPLE CAPABILITY
```

That combination explains why strategic classification cannot be generated from the cavalry ID alone.

---

# 3. Infantry specialization

The current reference identifies Cataphract explicitly as an anti-infantry cavalry unit. It reports +9 attack against Infantry for the standard unit and +12 for Elite, with Logistica adding +6 attack against Infantry to the Elite/technology package.

The anti-infantry target surface includes the militia-line and spear-line armor class families, with additional civilization-specific infantry classes represented in the reference data.

This gives AEGIS a much stronger representation than:

```text
Cataphract → cavalry
```

The correct research representation is:

```text
Cataphract
├── mechanical_family: cavalry
├── strategic_role: anti-infantry
├── target_family: infantry
├── anti-cavalry resistance: yes
└── mass-combat effect: trample / splash capability where enabled
```

**Evidence:** DIRECT/COMPOSED.

---

# 4. Logistica is a capability transition

Logistica must be represented separately from the Cataphract's base identity.

Research evidence reports that Logistica provides:

```text
+6 attack vs Infantry
+ trample damage / area effect
```

Therefore:

```text
BASE CATAPHRACT
→ anti-infantry capability

LOGISTICA
→ materially strengthens that capability
→ adds mass-infantry damage mechanism
```

This is a technology-enabled capability transition, not a change of unit ID.

The distinction matters for later transition economics:

```text
UNIT COST
≠
TECHNOLOGY COST
≠
TOTAL CAPABILITY COST
```

A future evaluator must account for the full transition burden before calling an Elite/Logistica Cataphract investment efficient.

---

# 5. Anti-cavalry resistance does not redefine the role

Cataphract has a special anti-cavalry defensive property. Current reference material reports +12 bonus-defense against anti-cavalry attacks for the standard unit and +16 for Elite.

This produces an important strategic asymmetry:

```text
ATTACK FUNCTION
→ strongly anti-infantry

DEFENSIVE PROPERTY
→ unusually resistant to anti-cavalry bonus damage
```

The second fact does not turn Cataphract into an anti-cavalry unit.

It instead changes the set of threats that can efficiently remove the anti-infantry capability.

This is a critical distinction for future AEGIS reasoning:

```text
OFFENSIVE ROLE
≠
DEFENSIVE RESILIENCE
≠
COUNTER RELATIONSHIP
```

---

# 6. Counter model correction

A conventional counter table may incorrectly produce:

```text
Cataphract = cavalry
→ Halberdier = counter
→ therefore Cataphract is anti-cavalry
```

This is invalid.

The correct model is target-specific:

```text
Enemy infantry detected
        ↓
Cataphract candidate
        ↓
measure infantry damage
        ↓
measure production / technology burden
        ↓
measure survivability
        ↓
measure mass-combat effect
        ↓
compare against alternatives
```

Meanwhile:

```text
Enemy cavalry detected
        ↓
Cataphract may be a candidate
        ↓
but candidate status must be evaluated separately
```

Cataphract's anti-cavalry resistance is evidence of survivability against a counter mechanism, not evidence that the unit's strategic job is to counter cavalry.

---

# 7. Infantry matchup surface

The most valuable next quantitative comparisons are against representative infantry categories rather than generic cavalry:

### Militia-line
- Man-at-Arms
- Long Swordsman
- Two-Handed Swordsman
- Champion

### Spear-line
- Spearman
- Pikeman
- Halberdier

### Civilization-specific infantry
Where relevant, the matrix should separately capture infantry armor classes for unique units such as:
- Huskarl
- Samurai
- Jaguar Warrior
- Woad Raider
- Teutonic Knight
- Berserk
- Kamayuk
- Throwing Axeman
- Shotel Warrior
- Gbeto

The purpose is not to assume all infantry are equivalent. The purpose is to determine whether Cataphract's strategic anti-infantry role remains effective across the target distribution.

---

# 8. Damage model

The next local-data extraction should calculate at minimum:

```text
effective_attack
= base_attack
+ applicable_attack_bonus
+ applicable_technology_bonus
- target_relevant_armor
```

For each representative target, preserve:

```text
raw attack
bonus damage
armor mitigation
final damage / hit
attack interval
estimated hits to kill
estimated time to kill
```

For mass infantry, add a separate area-effect term rather than hiding it inside single-target DPS.

Conceptually:

```text
SINGLE TARGET EFFECT
+
MULTI-TARGET / TRAMPLE EFFECT
=
CATAPHRACT COMBAT VALUE
```

This is research methodology only, not an implementation formula.

---

# 9. Economic interpretation

The reported base Cataphract cost is 70 food + 75 gold. This is **not** subject to the Byzantine -25% food discount because the civilization discount applies to the Spearman, Skirmisher, and Camel Rider families, not Cataphracts.

Therefore a strategic evaluator must not generalize:

```text
Byzantines have -25% food units
→ Cataphracts are -25% food
```

That would be a civilization-bonus category error.

Cataphract economic burden remains distinct from the cheaper Byzantine counter families.

---

# 10. Strategic consequence

This pass produces a useful Byzantine capability taxonomy:

```text
                 BYZANTINE CAPABILITY SURFACE

ANTI-INFANTRY
    ├── Cataphract / Elite Cataphract
    ├── ranged candidates
    └── siege candidates

ANTI-MOUNTED
    ├── Spearman family
    └── Camel Rider family

ANTI-RANGED
    ├── Skirmisher family
    └── cavalry / siege alternatives
```

The Cataphract therefore occupies a different strategic niche from the Camel Rider even though both are mechanically cavalry.

This is exactly why a future strategic evaluator needs **role tags independent of unit IDs**.

No Layer-2 implementation is authorized by this observation.

---

# 11. Current evidence grades

| Finding | Grade |
|---|---|
| Cataphract is mechanically cavalry | DIRECT |
| Cataphract is trained at Castle | DIRECT |
| Cataphract has infantry attack bonus | DIRECT |
| Cataphract has anti-cavalry bonus resistance | DIRECT |
| Cataphract is strategically anti-infantry | DIRECT/COMPOSED |
| Cataphract's role can differ from mechanical family | COMPOSED |
| Cataphract is automatically an anti-cavalry counter | DISPROVEN as a role inference |
| Cataphract is always the best anti-infantry option | NOT ESTABLISHED |
| Cataphract is economically superior to cheaper Byzantine lines | NOT ESTABLISHED |
| Elite/Logistica is always worth its transition cost | NOT ESTABLISHED |

---

# 12. Hostile QC

### Failure mode A — ontology leakage
**Test:** Did mechanical cavalry classification overwrite strategic role?  
**Result:** NO.

### Failure mode B — role inflation
**Test:** Did anti-infantry classification imply universal superiority?  
**Result:** NO.

### Failure mode C — nominal-counter error
**Test:** Did anti-cavalry resistance get converted into anti-cavalry strategic role?  
**Result:** NO.

### Failure mode D — economy overclaim
**Test:** Was Cataphract incorrectly given the Byzantine -25% food discount?  
**Result:** NO.

### Failure mode E — technology collapse
**Test:** Was Logistica treated as inherent to every Cataphract?  
**Result:** NO.

### Failure mode F — local-data overclaim
**Test:** Were external reference values falsely represented as verified installed `.dat` values?  
**Result:** NO. Local extraction remains explicitly pending because the remote workstation was unavailable during this pass.

---

# 13. Six-month re-entry test

A future engineer returning six months from now should be able to answer immediately:

1. **What is a Cataphract mechanically?** Cavalry / unique mounted unit.
2. **What is its strategic role?** Anti-infantry.
3. **Why?** Infantry-specific attack bonus plus combat/mass-combat properties.
4. **Does that make it an anti-cavalry unit?** No.
5. **Why is it unusually resilient to anti-cavalry units?** Special anti-cavalry bonus-defense property.
6. **Does Byzantine's -25% food discount apply to it?** No.
7. **What remains to be measured locally?** Exact installed `.dat` values, armor interactions, technology states, effective damage, time-to-kill, mass-combat effect, and transition economics.

If these answers are not recoverable from this artifact, the pass has failed its re-entry requirement.

---

# 14. Next research frontier

The next high-value pass should not revisit the Cataphract ontology. That question is resolved.

The next task is the **full measured Byzantine combat graph**:

```text
UNIT
→ TARGET
→ ARMOR CLASS
→ BONUS INTERACTION
→ FINAL DAMAGE
→ ATTACK INTERVAL
→ TIME TO KILL
→ COST
→ TRAIN TIME
→ TECHNOLOGY BURDEN
→ INFRASTRUCTURE BURDEN
→ STRATEGIC ROLE
```

Priority targets:

1. Cataphract → infantry matrix
2. Camel Rider → cavalry matrix
3. Spearman/Halberdier → cavalry matrix
4. Skirmisher → ranged matrix
5. Siege → mass-unit matrix
6. Monks → control/sustain matrix
7. Naval capabilities under the 2026 naval system

The resulting graph should support strategic comparison without confusing game ontology with strategic purpose.

---

# 15. Boundary declaration

**Layer 2 remains research-only.**

This pass contains:
- no `.per` implementation;
- no production rules;
- no controller;
- no runtime candidate;
- no deployment;
- no modification of stock AI.

It is an evidence artifact establishing the correct research ontology for Byzantine Cataphract analysis.

---

## Verdict

**PASS — STRATEGIC ROLE CONFIRMED.**

The central correction is now explicit and durable:

> **Cataphract is cavalry by mechanical identity and anti-infantry by strategic function.**

AEGIS must preserve both truths simultaneously.
