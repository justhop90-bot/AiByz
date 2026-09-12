# AiBuilder Customization Contract v0.1

**Status:** STATICALLY QUALIFIED — architecture decision baseline
**Date:** 2026-09-12
**Scope:** `AiBuilder.per`, `AiBuilder/`, current `ByzBot.per`, and upstream AIBuilder source/README

## 1. Executive finding

The AiBuilder corpus contains an explicit, first-class customization surface. The intended model is **not** to replace the Builder executor and is not to require a parallel Byzantine execution architecture.

The canonical pattern visible in the root is:

```text
AiBuilder configuration constants
        ↓
phaseUpdate policy projection
        ↓
AiBuilder execution libraries
        ↓
CUSTOMIZATION section
        ↓
Byzantine-specific policy rules
        ↓
existing Goals / Strategic Numbers / native executor
        ↓
engine
```

The strongest direct evidence is the root's explicit `- CUSTOMIZATION -` section, which appears **after the library loads** and states that additional lines may be added there to customize the AI. The root also provides commented customization examples using ordinary `.per` rules and Strategic Number writes.

**Architectural consequence:** AEGIS should feed the existing AiBuilder control channels wherever possible. It should not duplicate `militaryUnits.per`, `construction.per`, `economy.per`, or the other execution libraries merely to obtain Byzantine behavior.

## 2. Direct source evidence

### 2.1 Root configuration is intentionally editable

The root begins with:

```text
; AIBuilder v2.0 - CONSTANTS
; Feel free to adjust these values --->
```

It then defines large families of phase-specific constants for:

- explorer counts
- gatherer policy
- villager caps
- age caps and age-up requirements
- building caps
- upgrade policy
- military unit caps
- naval unit caps
- attack timing and requirements
- difficulty scaling
- cheating parameters
- resource/search distances
- military training scaling

These constants are subsequently projected into mutable Goals/SNs by `phaseUpdate.per`.

**Evidence class:** DIRECT.

### 2.2 The phase constants are the primary data-driven customization layer

`phaseUpdate.per` maps phase constants into runtime policy Goals. Examples include:

```text
phase1-spearman-cap-*    → desired-number-spearmen
phase1-skirmisher-cap-*  → desired-number-skirmishers
phase1-archer-cap-*      → desired-number-archers
phase1-camelrider-cap-*  → desired-number-camelriders
phase1-uniqueunit-cap-*  → desired-number-uniqueunits
phase1-monk-cap-*        → desired-number-monks
phase1-bombardcannon-cap-* → desired-number-bombardcannons
phase1-fireship-cap-*    → desired-number-fireships
```

The same pattern exists across phases and difficulty branches.

**Evidence class:** DIRECT.

### 2.3 The root explicitly defines the Goal interface used by executors

The root allocates the production Goals, including:

```text
desired-number-spearmen       49
desired-number-camelriders     54
desired-number-archers         56
desired-number-skirmishers     57
desired-number-uniqueunits     61
desired-number-monks            62
desired-number-bombardcannons   69
desired-number-fireships        73
```

`militaryUnits.per` consumes these Goals to make training requests.

**Evidence class:** DIRECT.

### 2.4 The root has an explicit post-load customization hook

The current root loads:

```text
AiBuilder\\phaseUpdate
AiBuilder\\general
AiBuilder\\market
AiBuilder\\economy
AiBuilder\\technologies
AiBuilder\\construction
AiBuilder\\ByzBot
AiBuilder\\militaryUnits
AiBuilder\\militaryBehavior
```

and then immediately declares:

```text
; - CUSTOMIZATION -
; You can add more lines to customize your AI here --->
```

The section contains commented examples of custom rules that modify Strategic Numbers and use ordinary `.per` predicates/actions.

**Evidence class:** DIRECT.

This is the most important finding in this document.

## 3. What the Builder author appears to customize

The source exposes several distinct customization classes.

### A. Phase policy constants

Use when the desired behavior can be represented as a phase-specific baseline.

Examples:

- unit caps
- building caps
- villager caps
- age caps
- upgrade enablement
- attack timing
- attack requirements
- resource/search distances
- difficulty scaling

**Recommended Byzantine use:** establish the Byzantine baseline here first.

### B. Post-load policy rules

Use when behavior depends on observations or conditions that cannot be represented by a fixed phase constant.

Examples from the root's own customization examples:

```text
(defrule
    <condition>
=>
    <set strategic number / goal / native action>)
```

**Recommended Byzantine use:** threat-conditioned composition changes, temporary responses, civ-specific tactical policy, and other reactive behavior.

### C. Existing Goal channels

The production executor already consumes `desired-number-*` Goals.

Therefore a Byzantine rule can customize production by changing the value consumed by the executor rather than issuing a second `train` command.

**Classification:** DIRECT architecture pattern; exact runtime precedence between multiple writers remains a separate qualification question.

### D. Existing Strategic Number channels

The root's own customization examples modify Strategic Numbers directly. These are legitimate Builder control channels and should be preferred over inventing parallel scratch state when an existing SN expresses the needed behavior.

### E. Native engine-facing commands

The customization surface technically permits ordinary `.per` actions, but that does **not** imply that a custom layer should duplicate an existing executor.

The preferred rule is:

> If AiBuilder already owns the action executor, customize its inputs before creating a second executor.

## 4. What should remain library infrastructure

The following should remain owned by AiBuilder unless a concrete deficiency is proven:

| Subsystem | Default owner | Byzantine role |
|---|---|---|
| `militaryUnits.per` | AiBuilder | Feed production Goals |
| `construction.per` | AiBuilder | Feed building Goals |
| `economy.per` | AiBuilder | Feed economy Goals/SNs |
| `technologies.per` | AiBuilder | Feed upgrade/age policy |
| `militaryBehavior.per` | AiBuilder | Feed military policy/SNs |
| `general.per` | AiBuilder | Feed explorer/search policy |
| `market.per` | AiBuilder | Avoid replacement unless deficient |
| `constantsUP.per` | Engine/Builder vocabulary | Do not casually modify |
| Goal allocation | Root | Use existing allocated channels |
| Timer allocation | Root | Do not invent IDs |

## 5. Byzantine architecture implied by the customization contract

The preferred architecture is now:

```text
                 AiBuilder
                     │
        ┌────────────┴────────────┐
        │                         │
 phase constants             native state
        │                         │
        ▼                         ▼
   phaseUpdate              observations
        │                         │
        └──────────┬──────────────┘
                   ▼
          Byzantine policy
                   │
          ┌────────┴────────┐
          │                 │
       Goal writes       SN writes
          │                 │
          └────────┬────────┘
                   ▼
          AiBuilder executor
                   │
                   ▼
              engine request
                   │
                   ▼
              world state
                   │
                   └────→ reassessment
```

This preserves the user's stated principle of going **with** the AiBuilder execution model rather than against it.

## 6. Reinterpretation of the current `ByzBot.per`

Current `AiBuilder/ByzBot.per` is a small policy module containing:

```text
players-building-type-count any-enemy archery-range > 0
    → desired-number-skirmishers 12

players-building-type-count any-enemy stable > 0
    → desired-number-spearmen 10
```

It deliberately does not train units directly, allocate new Goals, use scratch state, or issue attacks.

This is conceptually aligned with the customization contract.

However, its current **placement in the load list is not yet established as the intended customization location**. The root already provides a dedicated post-load `CUSTOMIZATION` section, and `ByzBot.per` is loaded before `militaryUnits.per` and `militaryBehavior.per`.

Therefore:

- `ByzBot.per` is a valid policy experiment.
- Its two rules are not yet runtime-qualified.
- Its current placement should not be treated as canonical architecture.
- The next safe design step is to determine whether Byzantine policy should be represented in the explicit post-load customization section, in a dedicated loaded policy file immediately before that section, or through edited phase constants plus a small post-load policy block.

**Evidence class:** COMPOSED from direct source evidence.

## 7. Production-specific consequence

The previous Production Authority Matrix remains useful as an audit of current writers, but it should **not** be treated as a requirement to build a new arbitration executor.

The more natural Builder-native sequence is:

```text
Byzantine requirement
        ↓
customization rule
        ↓
existing desired-number-* Goal
        ↓
existing militaryUnits.per
        ↓
can-train
        ↓
train
        ↓
queue/pending/world observation
        ↓
reassessment
```

The unresolved problem is therefore not:

> How do we build another production executor?

It is:

> How should Byzantine policy write or modify the existing production Goals without being unintentionally overwritten by phase policy or another active writer?

That is a much smaller and more Builder-compatible problem.

## 8. Authority/precedence question that remains open

There are currently multiple writers of some `desired-number-*` Goals, especially in `phaseUpdate.per` and `byzPolicy.per`.

Static evidence establishes that the writers exist. It does **not** yet establish a universal same-pass precedence rule for competing writes.

Therefore the correct next investigation is:

```text
phase constant
 → phaseUpdate writer
 → Byzantine customization writer
 → militaryUnits reader
```

with explicit analysis of:

- rule eligibility
- rule order
- `disable-self`
- Goal mutation timing
- same-pass visibility
- repeated firing
- subsequent-pass persistence
- expiry/reversion

No new arbitration primitive is justified until this is resolved.

## 9. AEGIS placement

AEGIS should be understood as a **policy/cognition layer feeding Builder control channels**, not as a replacement for Builder execution.

The appropriate conceptual relationship is:

```text
AEGIS observation/classification
          ↓
AEGIS belief / threat state
          ↓
AEGIS objective / requirement
          ↓
Builder-compatible customization rule
          ↓
existing Goal/SN
          ↓
existing Builder executor
```

AEGIS lifecycle concepts such as authorization, expiry, verification, and reassessment may still be valuable, but they must be implemented only where the Builder ABI provides an appropriate control channel.

## 10. Evidence classification

### CONFIRMED / DIRECT

1. `AiBuilder.per` contains a large editable configuration-constant section.
2. `phaseUpdate.per` projects those constants into Goals/SNs.
3. `AiBuilder.per` explicitly contains a post-load `CUSTOMIZATION` section.
4. That section explicitly instructs the author that additional customization lines may be added.
5. The section provides concrete `.per` customization examples.
6. Production Goals are allocated in the root and consumed by `militaryUnits.per`.
7. Upstream AIBuilder is explicitly a generator for `.ai`/`.per` files and uses additional library `.per` files for common behavior.

### COMPOSED

1. The most Builder-native Byzantine architecture is policy customization feeding existing executors.
2. The production problem should be reframed from executor replacement to Goal-writer ownership/precedence.

### INFERRED

1. The post-load customization section is the preferred place for reactive Byzantine policy.
2. Phase constants are the preferred place for static Byzantine baseline policy.
3. A dedicated Byzantine policy file may be useful for organization, but its placement should preserve the Builder customization semantics.

### UNQUALIFIED

1. Exact same-pass precedence between competing Goal writers.
2. Exact runtime semantics of the `any-enemy` building predicate in the current target runtime.
3. Whether moving the existing `ByzBot` rules changes runtime behavior materially.
4. Whether every possible AEGIS state can be represented cleanly using existing Builder Goals/SNs.

## 11. Decision

**Do not build a new production arbitration executor at this stage.**

The repository now has enough direct evidence to treat the Builder's customization interface as the primary architectural constraint.

The next implementation target should be a **Builder-native Byzantine production customization slice**:

```text
one baseline target
+
one reactive target
+
one phase transition
+
one existing militaryUnits executor
+
one explicit precedence/expiry analysis
```

The best first target remains **spearmen**, because it has:

- an existing Builder production Goal;
- an existing executor path;
- an existing Byzantine baseline;
- an existing threat-response policy;
- a simple unit line;
- a clear relationship to enemy cavalry;
- and existing AEGIS threat state available for later integration.

No new production executor should be created for this slice.
