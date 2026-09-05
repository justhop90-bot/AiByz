# AEGIS World Model — Scientist Pass 2

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** SCIENTIST  
**Status:** ENGINE-SEMANTICS QUALIFICATION — NOT IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Mission

This pass tests the Carpenter + Adversary World Model against actual AoE2DE AI-scripting evidence.

The previous adversarial pass found that the simplified architecture needs a semantic distinction between current observation, last-known information, unknown state, and unresolved/contradicted information. That conclusion is useful architecturally, but it cannot be accepted merely because it sounds correct.

The Scientist's job is narrower:

1. establish what the engine/documentation actually exposes;
2. separate direct engine semantics from derived semantics;
3. identify what can safely be represented architecturally now;
4. identify what still requires runtime qualification;
5. prevent the architecture from silently assuming an engine feature that does not exist.

**No `.per` implementation, runtime experiment, or ABI allocation is authorized by this pass.**

---

# 1. Evidence standard

Claims are classified as:

- **DIRECT** — explicitly documented engine/script behavior.
- **OBSERVED** — established from the captured stock AI corpus or committed machine evidence.
- **COMPOSED** — follows directly by combining multiple documented/direct primitives without adding an engine assumption.
- **INFERRED** — technically plausible but not directly established.
- **PROPOSED** — architecture choice, not an engine fact.
- **OPEN** — requires runtime/build-specific qualification.
- **REJECTED** — architecture must not assume it.

This pass deliberately does not convert `INFERRED` or `PROPOSED` into `PROVEN`.

---

# 2. What the engine actually exposes

## 2.1 Search is a real computational surface

The AI scripting command surface explicitly provides local and remote searches, status-filtered searches, resource searches, filters, search reset operations, and search-state retrieval.

The current Scripting Encyclopedia describes:

- `up-find-local` — finds objects owned by the local player for direct targeting;
- `up-find-remote` — finds objects owned by the focus player for direct targeting;
- `up-find-status-local` / `up-find-status-remote` — status-filtered searches;
- `up-filter-status` — establishes the object status filter for status searches/resource searches;
- `up-full-reset-search` — resets search/filter state;
- `up-get-search-state` — exposes search result state.

**Classification: DIRECT.**

This validates the architectural concept of an **Observation Workbench** as a real engine-facing computation stage rather than an invented abstraction.

Source: AoE2 AI Scripting Encyclopedia command index and legacy scripting guide. The Encyclopedia also labels the relevant search/filter operations as high-cost operations, which makes scheduling a separate architectural concern. citeturn2search11turn2search4

---

# 3. Search results do NOT establish universal absence

This is the most important scientific qualification in this pass.

A remote search is constrained by ownership, visibility/sightability, search filters, and object status. Historical UserPatch documentation explicitly states that non-ally remote objects are discoverable under visibility/sighting conditions; later DE fixes also changed how pending objects, gates, status searches, and object visibility behaved.

Therefore:

```text
SEARCH RESULT = 0
```

cannot, by itself, be promoted to:

```text
WORLD FACT = OBJECT DOES NOT EXIST
```

**Classification: DIRECT for the visibility/search limitation; COMPOSED for the architectural consequence.**

This directly supports the Adversary's correction. A missing search result is an **observation about the search surface**, not automatically a destruction event.

The 2013 UserPatch guide states that non-allied objects could be found only under specific sighting conditions, including recently seen units and sighted buildings. This is historical evidence rather than a complete current-build specification, but it establishes the fundamental distinction that searchability and existence are not identical concepts. citeturn2search12

The later DE patch history also contains fixes where `up-find-remote` behavior changed for pending objects and gates, demonstrating that search semantics are engine behavior and can change by build. citeturn2search1turn2search0

**Architectural rule:** AEGIS must never implement `not found` as `destroyed` without an independently qualified completeness condition.

---

# 4. Object data is richer than existence

The current parameter index identifies `ObjectData` as a distinct UP parameter type, and the stock/engine evidence surface includes object-data fields for substantially more than identity.

Relevant documented/current-build examples include:

- action/order state;
- movement position;
- target/target ID;
- patrolling;
- ownership;
- hero flags;
- attack-related state;
- precise position;
- progress/lifecycle-related information in the stock corpus;
- newer attack-delay information.

The official DE patch history confirms that object-data semantics have been actively expanded and corrected over time. Update 37650 added `object-data-ownership` and capture-object data; Update 50292 added return behavior for object-data target/movement fields and corrected several object-data functions; Update 153015 added `object-data-attack-delay`; Update 177723 corrected `Object-data-next-attack` behavior. citeturn2search0turn2search4turn0search5turn0search6

**Classification: DIRECT.**

**Architectural consequence:** World State can legitimately represent observed object state richer than `exists / does not exist`, but each field must retain its own semantic meaning.

---

# 5. Identity: engine evidence is sufficient for object identification, not universal continuity

The parameter model distinguishes `ObjectId` from `ObjectData`, and the stock AI uses selected search objects as targets for object-data reads. This gives AEGIS a legitimate engine-facing concept of a selected object.

However, the available evidence does **not** establish that AEGIS can safely maintain a universal historical identity graph across all observations, deaths, replacements, visibility gaps, and respawns.

Therefore:

```text
OBJECT ID AVAILABLE
        ≠
UNIVERSAL HISTORICAL IDENTITY GUARANTEE
```

**Classification:**

- selected/current object identity: **DIRECT/OBSERVED**;
- universal continuity across time: **OPEN**;
- continuity inference from type/location similarity: **REJECTED**.

This preserves the Adversary rule:

> Identity is evidence, not a guess.

The architecture may use identity continuity where engine evidence or a later qualified mechanism makes it safe. It must not silently manufacture continuity.

---

# 6. Ownership is directly representable, but record ownership is architectural

`object-data-ownership` is explicitly documented as an engine object-data capability. Official Update 37650 identifies it as object-data ID 83. citeturn2search0

This establishes:

```text
OBJECT OWNER
```

as a legitimate world fact.

It does **not** establish:

```text
WORLD-STATE RECORD OWNER
```

or:

```text
MESSAGE WRITER OWNER
```

Those remain AEGIS architecture concepts.

**Classification:**

- object ownership: **DIRECT**;
- state-record ownership: **PROPOSED**;
- writer authority: **PROPOSED / OPEN for representation**.

This distinction prevents the previous ABI review mistake of treating engine object ownership as equivalent to state-channel ownership.

---

# 7. Lifecycle is observable, but readiness and capability remain separate

The engine exposes object state and progress-related data, and the stock corpus uses pending/ready/status distinctions in searches and production logic. Official patch history also confirms that pending objects and queue state have materially different behavior: `up-find-remote` was explicitly changed to find building foundations, while other updates distinguish pending objects and queued units. citeturn2search5turn2search1

This supports the following conceptual chain:

```text
OBJECT OBSERVED
      ↓
OBJECT STATUS / PROGRESS
      ↓
READINESS
      ↓
CAPABILITY
```

But the last two transitions are not the same engine primitive.

For example:

```text
stable foundation exists
```

is not equivalent to:

```text
stable can currently produce cavalry
```

The first is world state. The second requires readiness plus civilization/technology/queue/cost/production conditions and therefore belongs to Capability/Production reasoning.

**Classification:**

- object/status distinction: **DIRECT/OBSERVED**;
- lifecycle → readiness composition: **COMPOSED**;
- readiness → capability: **COMPOSED/ARCHITECTURAL**, depending on the capability question;
- capability effectiveness: **OPEN/strategic**.

---

# 8. `up-get-object-type-data` proves type-level observation, not object existence

Official Update 37650 explicitly states that `up-get-object-type-data` was changed to function for units which are not available. citeturn2search0

This is a useful warning for architecture:

```text
TYPE DATA
```

and:

```text
LIVE OBJECT STATE
```

are different surfaces.

Type data can describe what a unit/object type is capable of even when that unit is not presently available as a live world object.

**Classification: DIRECT.**

**Architectural rule:** Type-level capability information must not be inserted into World State as if it were a live-object observation.

This is another high-leverage boundary: one engine primitive can support planning without pretending to be world observation.

---

# 9. Search status is not the same thing as temporal freshness

The engine exposes object statuses for search/filter purposes. Historical documentation describes status categories such as pending, ready, resource, down, and gatherable states, but these are object-state classifications, not universal timestamps.

Therefore:

```text
OBJECT STATUS
```

must not be conflated with:

```text
OBSERVATION AGE
```

**Classification: DIRECT.**

No source examined in this pass establishes a general-purpose AI scripting primitive equivalent to:

```text
observation_timestamp(object, field)
```

for the World Model.

**Classification of universal observation timestamps: OPEN.**

The architecture therefore retains `CURRENT / LAST-KNOWN / UNKNOWN / CONTRADICTED` as semantic categories without claiming that the engine directly supplies a timestamp field.

---

# 10. Can supersession be represented safely?

The engine gives AEGIS goals, strategic numbers, timers, search state, and object data as separate primitive surfaces. The current data-limits documentation also distinguishes scalar goals from multi-goal operations and emphasizes that parameter types matter. citeturn0search16turn0search2

What the evidence does **not** establish is a native generic record primitive such as:

```text
compare observation generation
atomically replace world record
```

Therefore universal engine-level supersession is **OPEN**.

However, the architecture can still require the semantic rule:

```text
A newer, better-qualified observation should supersede an older one.
```

That is a **PROPOSED architectural invariant**, not a claim that the engine already provides the mechanism.

The eventual representation must be qualified empirically before implementation.

---

# 11. Contradiction is an architectural state, not a proven engine primitive

The evidence supports situations in which multiple observations can fail to establish one definitive world truth:

- an enemy object may become unsearchable;
- an object may be pending rather than ready;
- different searches can have different visibility/filter constraints;
- object data has changed historically across patches.

But no direct engine primitive was found in the sources examined that says:

```text
CONTRADICTED
```

as a native World Model status.

Therefore the status:

```text
CONTRADICTED
```

is **PROPOSED**, not DIRECT.

That does not make it a bad architecture. It means implementation must determine how contradiction is represented using qualified goals/SNs/search state or another permitted primitive.

---

# 12. Current / Last-Known / Unknown: what is actually justified?

The adversarial model proposed:

```text
CURRENT
LAST-KNOWN
UNKNOWN
CONTRADICTED
```

Scientist verdict:

| Semantic state | Evidence status | Keep? |
|---|---|---|
| CURRENT | COMPOSED from qualified current observation | **YES** |
| LAST-KNOWN | COMPOSED from preserved prior observation | **YES** |
| UNKNOWN | COMPOSED absence of sufficient evidence | **YES** |
| CONTRADICTED | PROPOSED unresolved semantic state | **YES, but explicitly architectural** |
| universal timestamp | OPEN | **NO assumption** |
| universal confidence score | OPEN / unnecessary | **NO assumption** |
| destruction from search=0 | REJECTED | **NO** |
| total count from partial search | REJECTED | **NO** |

This is the correct level of commitment for Layer 3A.

---

# 13. Execution is a legitimate evidence source, but not World Model ownership

AoE2 AI scripting distinguishes actions/commands from fact/object-data queries. The Encyclopedia's command index explicitly categorizes `up-get-object-data` as an action that reads selected object information, while commands such as `train`, `build`, and `research` cause AI-directed actions. The stock corpus also demonstrates extensive use of these surfaces. citeturn2search11turn2search4

The architecture therefore retains:

```text
EXECUTION INTENT
      ↓
ENGINE ACTION
      ↓
WORLD TRANSITION
      ↓
OBSERVATION / VERIFICATION
```

The important scientific qualification is that issuing an action is not automatically proof that the desired world transition occurred.

Historical patch notes demonstrate exactly why: multiple AI commands and object-data behaviors have required fixes for cases where commands failed, targeted incorrectly, or returned incorrect state. citeturn2search0turn2search1turn0search6

**Classification:**

- command issuance: **DIRECT**;
- intended transition: **DIRECT/architectural interpretation**;
- successful world transition: **OPEN until observed/qualified**;
- verification requirement: **PROPOSED but strongly justified**.

This supports the AEGIS evidence ladder rather than weakening it.

---

# 14. Search state is a workbench, not persistent truth

The documented search system allows objects to be accumulated, filtered, reset, and counted/read. Historical documentation specifically describes search result sets and `up-get-search-state`. citeturn2search4turn2search12

Therefore the Carpenter's distinction is scientifically sound:

```text
OBSERVATION WORKBENCH
```

should be treated as temporary computational state.

It should not automatically become:

```text
WORLD DATABASE
```

A search result is a measurement/workset. Persistence is an architectural decision made only when continuity, recomputation cost, or strategic amnesia justify it.

**Classification: COMPOSED + PROPOSED.**

---

# 15. Observation cost is not theoretical

The current command index classifies search/filter operations such as `up-find-local`, `up-find-remote`, `up-filter-distance`, and `up-filter-status` as **Very High** cost. citeturn2search11

The Encyclopedia's data-limits guidance also warns about script execution time and expensive search operations. citeturn0search16

Therefore:

```text
SCHEDULER / ATTENTION
```

is not architectural decoration.

It is required to keep the Observation Workbench from becoming an uncontrolled polling loop.

**Classification: DIRECT for operation cost categories; PROPOSED for AEGIS scheduling architecture.**

---

# 16. Partial observation is a first-class semantic hazard

The engine's remote search model is visibility/search constrained, and the search API returns sets of objects matching the search conditions. Nothing in the examined evidence establishes that an arbitrary enemy-unit search is a complete census of all enemy units in the game.

Therefore:

```text
observed cavalry = 2
```

must not automatically become:

```text
enemy cavalry total = 2
```

**Classification: COMPOSED → architectural invariant.**

The World Model should therefore label aggregate measurements by semantic scope:

- observed subset;
- confirmed total only where completeness is independently established;
- derived estimate in Belief Model;
- last-known measurement.

This is a small semantic rule with enormous downstream leverage.

---

# 17. Current-build variability is itself evidence

AoE2DE's official patch history repeatedly documents changes to AI scripting semantics:

- object-data fields added or corrected;
- search behavior corrected;
- pending-object handling changed;
- unit queue counting changed;
- object-data movement and attack fields corrected;
- strategic-number capacity expanded;
- AI debugging facilities added.

Examples include Updates 39284, 50292, 61321, 153015, and 177723. citeturn2search1turn2search4turn2search8turn0search5turn0search6

**Scientific conclusion:** documentation and historical behavior are necessary evidence, but target-build empirical qualification remains mandatory for any semantics on which AEGIS correctness critically depends.

This is especially important for:

- search visibility edge cases;
- identity continuity;
- object-data return values;
- status semantics;
- multi-goal output behavior;
- supersession representation;
- freshness/generation encoding.

---

# 18. What the Scientist closes

The following architectural statements are now sufficiently grounded for Layer 3A:

### CLOSED — 1. Observation Workbench is legitimate
The engine has real search/filter/select/read primitives and search state. **DIRECT.**

### CLOSED — 2. Search result is not universal world truth
Visibility, focus player, status, and search constraints matter. **DIRECT + COMPOSED.**

### CLOSED — 3. World State may represent observed object facts
Object-data exposes identity/type/ownership/position/action and other state surfaces. **DIRECT.**

### CLOSED — 4. Object existence, status, readiness, and capability are distinct concepts
Pending/search status and production/availability behavior establish the distinction. **DIRECT + COMPOSED.**

### CLOSED — 5. Object ownership is world data, not state-channel ownership
`object-data-ownership` is directly supported; AEGIS record ownership remains architectural. **DIRECT + PROPOSED.**

### CLOSED — 6. Type data is not live object state
`up-get-object-type-data` functioning on unavailable units proves the distinction. **DIRECT.**

### CLOSED — 7. Observation Workbench must be scheduled
Search/filter operations are high/very-high cost. **DIRECT + PROPOSED.**

### CLOSED — 8. World State must not infer destruction from search absence
Searchability is not equivalent to existence. **DIRECT + COMPOSED.**

### CLOSED — 9. Aggregate scope must be explicit
Partial observations cannot be treated as complete enemy totals without an independent completeness guarantee. **COMPOSED.**

### CLOSED — 10. Execution is not proof of world transition
Historical engine corrections make verification necessary. **DIRECT + PROPOSED.**

---

# 19. What remains OPEN

The following are deliberately not closed by this pass:

1. exact current-build freshness/timestamp representation;
2. whether a target-build object ID can be safely used as a long-lived continuity key across all relevant lifecycle events;
3. exact semantics of every object-data field in build `101.103.48987.0`;
4. exact completeness conditions under which a search can justify an absence claim;
5. safe representation of local supersession/generation;
6. safe representation of `CONTRADICTED` state;
7. atomicity of multi-field publication using goals/SNs;
8. exact runtime cost of proposed observation schedules;
9. exact behavior of high-goal scalar storage for the eventual World State representation;
10. any claim that depends on runtime behavior rather than static documentation/corpus evidence.

These belong to later Layer 3 validation gates.

---

# 20. Scientist correction to the architecture

The previous architecture used:

```text
OBSERVATION WORKBENCH
        ↓
QUALIFY / PUBLISH
        ↓
WORLD STATE
```

The Scientist now gives that boundary a more exact meaning:

```text
                         REAL WORLD
                             │
                             ▼
                 OBSERVATION WORKBENCH
                 search / filter / select
                       read / measure
                             │
                             ▼
                    QUALIFY OBSERVATION
                    ├── scope
                    ├── object/type
                    ├── status
                    ├── ownership
                    ├── evidence quality
                    └── completeness where proven
                             │
                             ▼
                        WORLD STATE
                  ┌──────────┼──────────┐
                  ▼          ▼          ▼
               CURRENT   LAST-KNOWN  UNRESOLVED
                  │          │          │
                  └──────────┼──────────┘
                             ▼
                    BELIEF / SITUATION
                       / CAPABILITY
```

The critical word is **QUALIFY**.

World State is not simply a bucket into which observations are dumped.

It is the first semantic publication boundary.

---

# 21. Minimal World State contract after Scientist pass

The architecture should now require only the following conceptual information when material:

```text
WORLD FACT
├── VALUE
├── KIND / SEMANTIC SCOPE
├── STATUS
└── PROVENANCE WHEN NEEDED
```

Where:

```text
STATUS ∈ {
    CURRENT,
    LAST-KNOWN,
    UNKNOWN,
    UNRESOLVED / CONTRADICTED
}
```

And where semantic scope answers questions such as:

```text
OBSERVED SUBSET
CONFIRMED TOTAL
OBJECT-SPECIFIC
TYPE-LEVEL
LIFECYCLE STATE
POSITION
OWNERSHIP
OPERATIONAL STATE
```

This is intentionally not a universal database schema.

It is the minimum semantic contract that prevents the most dangerous category errors.

---

# 22. Falsifiers for the next validation gate

The next empirical Scientist work should attempt to falsify the following:

### F1 — Search absence
Can a zero remote search result be made to coexist with a known surviving enemy object outside current visibility?

### F2 — Identity continuity
Does the same engine object retain a stable identifier through movement, selection, visibility loss, and re-observation?

### F3 — Replacement
Can a destroyed object and a replacement object produce distinguishable identity evidence?

### F4 — Lifecycle
Can foundation, construction progress, and completed object state be distinguished reliably through object-data/search semantics?

### F5 — Publication ordering
Can two observations of the same semantic field be safely ordered using only permitted AI primitives?

### F6 — Multi-field coherence
Can a state publication update multiple related fields without consumers observing a dangerous half-updated state?

### F7 — Completeness
Under what exact conditions, if any, can a search legitimately support a claim of zero total objects?

### F8 — Execution transition
After a command that should create/change an object, what engine-visible evidence proves the transition actually occurred?

### F9 — Cost
What is the practical cost of repeated observation patterns on the target build?

### F10 — High-goal representation
Which object-state fields can safely inhabit the Layer 2-qualified scalar goal namespace without violating command-specific constraints?

These are empirical questions. They are not to be answered by architectural optimism.

---

# 23. Scientist verdict

## PASS — with explicit boundaries

The Carpenter's simplification survives.

The Adversary's correction survives.

The Scientist confirms that the correction is compatible with the actual AoE2DE scripting model **provided AEGIS treats the semantic statuses as architectural contracts rather than pretending they are native engine fields.**

The strongest scientifically grounded design is therefore:

```text
REAL WORLD
    ↓
OBSERVATION WORKBENCH
    ↓
QUALIFIED OBSERVATION
    ↓
WORLD STATE
    ↓
BELIEF / SITUATION / CAPABILITY
```

with these hard rules:

1. **No observation without a reason.**
2. **No search result is automatically complete.**
3. **No missing observation is automatically destruction.**
4. **No partial count is automatically a total.**
5. **No object similarity is automatically identity continuity.**
6. **No object existence is automatically readiness.**
7. **No readiness is automatically strategic capability.**
8. **No command issuance is automatically world-transition proof.**
9. **No type-level data is automatically live-world state.**
10. **No engine primitive is assumed to provide timestamps or generations until experimentally proven.**
11. **No strategic interpretation belongs inside World State.**
12. **No persistent field exists merely because the engine can expose it.**

The World Model is now scientifically bounded enough to continue architecture work without pretending that the engine has capabilities we have not proven.

---

# 24. Handoff to Architect

The next mode should be:

**🧠 ARCHITECT**

The Architect should now revise the World Model contract using only the Scientist-closed facts.

The next pass should answer:

1. What is the smallest publishable World State concept that preserves these semantics?
2. Which fields are truly worth persistence?
3. How should `CURRENT / LAST-KNOWN / UNKNOWN / UNRESOLVED` exist conceptually without becoming four databases?
4. Which world facts are object-specific versus aggregate?
5. Where does scope (`observed subset` vs `confirmed total`) live?
6. What information belongs in World State versus Belief/Situation/Capability?
7. How should execution-derived evidence enter the publication pipeline?
8. What is the smallest mailbox contract needed between World State and its consumers?
9. What can be deferred completely until runtime qualification?
10. Can the resulting design be expressed clearly enough that a later AoE2 engineer can map every concept to an actual primitive without inventing engine semantics?

**Do not implement yet.**

The architecture is ready for another design pass, not for furniture installation.
