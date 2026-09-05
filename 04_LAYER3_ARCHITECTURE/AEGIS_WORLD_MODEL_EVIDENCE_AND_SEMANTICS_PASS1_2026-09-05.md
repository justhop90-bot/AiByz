# AEGIS World Model — Evidence & Semantics Pass 1

**Date:** 2026-09-05  
**Layer:** 3A — Architecture / evidence-led subsystem design  
**Mode:** SCIENTIST  
**Status:** EVIDENCE BASELINE / ARCHITECTURE NOT YET LOCKED  
**Target build:** AoE2DE `101.103.48987.0`  
**Repository:** `justhop90-bot/AiByz`  

---

## 0. Mission

This pass establishes the evidence boundary for the first AEGIS subsystem: the **World Model**.

The mission is deliberately narrower than designing the final World Model:

> Determine what the AoE2DE AI can observe, what those observations actually mean, what lifecycle information they expose, and where the evidence stops.

No AEGIS runtime representation, goal allocation, strategic-number allocation, or production `.per` implementation is authorized by this document.

The governing principle is:

`REAL WORLD → ENGINE OBSERVATION → INTERPRETATION → WORLD MODEL`

The first arrow is machine capability. The second is semantics. The third is architecture. They must not be silently collapsed.

---

# 1. Existing evidence entering this pass

The repository already contains unusually strong source-level evidence for the historical observation surface.

### 1.1 Observation-semantics archaeology

Pass 18 established that verified Promisory source uses a broad object-data vocabulary spanning:

- identity/type: `object-data-id`, `object-data-type`, `object-data-class`, `object-data-player`, `object-data-ownership`;
- geometry: distance, full/precise distance, point and precise coordinates, movement coordinates;
- lifecycle/progress: `object-data-progress-value`, `object-data-progress-type`, `object-data-researching`, `object-data-train-count`, `object-data-train-time`;
- tactical state: under-attack, hitpoints, target, target-id, action, order, attack stance, attacker count;
- grouping/placement: group flag, object index, map zone;
- economic/resource state: resource, carry, gather type, dropsite.

The same pass documented a recurring source pipeline:

`SEARCH → FILTER → SELECT → READ → DERIVE → STORE → DECIDE`.

It also established that the historical AI persists `object-data-id` for continuity and distinguishes lifecycle conditions such as pending construction, research progress, producer readiness, and endangered production sites. fileciteturn300file0L2-L2

### 1.2 Vertical world-state archaeology

Pass 13 established a second important distinction:

`CONTROL ≠ WORLD ≠ STRATEGIC`.

A source-level command path can be closed while the resulting world-state transition remains unproven. The pass formalized W0–W4 evidence levels from command-only through strategic effect, and distinguished **conversion** from **realization**. fileciteturn299file0L2-L2

### 1.3 Replay information boundary

Pass 19 established four forensic layers:

`L0 raw recording → L1 parser decoding → L2 normalized representation → L3 state reconstruction`.

The tested normalized replay surface does not expose sufficient dynamic object-state lineage for arbitrary W2 claims, and the inspected parser does not itself provide a continuously reconstructed dynamic world-state database. Raw lifecycle archaeology remains open. fileciteturn298file0L2-L2

This means replay-derived evidence must not be used as a substitute for live AI observation semantics.

---

# 2. First major conclusion

The historical AI's observation system is substantially richer than a collection of counters.

The strongest source-derived model is:

`WORLD OBJECTS`
`↓`
`SEARCH SET`
`↓`
`FILTER / ORDER / SELECT`
`↓`
`OBJECT OBSERVATION`
`↓`
`DERIVED MEASUREMENT`
`↓`
`PERSISTED CONTROL STATE`
`↓`
`DECISION`

This is important for AEGIS because the World Model should not be designed as a giant table of facts populated by independent sensors.

The historical evidence instead suggests a **selective observation pipeline**: the controller constructs a temporary computational workspace, reduces it to the objects relevant to a question, extracts only the needed properties, and then promotes selected results into persistent control state. fileciteturn300file0L2-L2

That is a potentially high-leverage primitive pattern and should be preserved unless later evidence demonstrates a better approach.

---

# 3. Observation surface — evidence inventory

## 3.1 Object identity

**Observed capability:** object identity is available through `object-data-id`.

**Historical use:** IDs are read from selected objects and stored in goals so later searches can compare the current object with previously observed objects.

**Evidence grade:** DIRECT.

**Architectural implication:** identity continuity is a legitimate design primitive. It is materially stronger than attempting to identify an entity solely by type, location, or temporal proximity.

**Do not infer:** that every object type has a stable lifecycle lineage available through every replay/parser surface. Pass 19 explicitly leaves replay lineage open. fileciteturn300file0L2-L2 fileciteturn298file0L2-L2

## 3.2 Type and classification

**Observed capability:** type, class, player/ownership-related object fields are part of the source observation vocabulary.

**Evidence grade:** DIRECT.

**Architectural implication:** World Model entities can potentially be classified at multiple levels rather than reducing everything to one concrete unit ID.

**Constraint:** concrete type, unit line, class, ownership, and strategic category are different semantic layers. They must remain typed rather than treated as interchangeable labels.

## 3.3 Geometry

**Observed capability:** distance variants and point/precise-coordinate fields are actively consumed by the source.

**Evidence grade:** DIRECT.

**Architectural implication:** spatial reasoning can be derived from primitive object observations rather than requiring a separate omniscient map abstraction.

The stock scout system demonstrates this leverage: object coordinates are accumulated into centroids, local neighborhoods are filtered, and local counts are converted into weighted tactical strength. fileciteturn300file0L2-L2

## 3.4 Lifecycle and progress

**Observed capability:** progress value, progress type, researching state, train count, train time, and pending/ready/resource status are represented and operationally consumed.

**Evidence grade:** DIRECT.

**Important conclusion:** object existence is not equivalent to capability availability.

Historical examples include:

`foundation exists` ≠ `building is usable`

`producer exists` ≠ `producer is valid for training`

`research exists on a building` ≠ `research is complete`

`command issued` ≠ `capability realized`.

This is one of the strongest foundations for the AEGIS state envelope and should become a core World Model principle. fileciteturn300file0L2-L2

## 3.5 Tactical state

**Observed capability:** under-attack, hitpoints, target, target ID, action/order, stance, and attacker count are present in the historical observation vocabulary.

**Evidence grade:** DIRECT for the field usage.

**Architectural implication:** the World Model should be able to distinguish an entity's existence from its current operational condition.

Example conceptual distinction:

`KNIGHT EXISTS` is weaker than:

`KNIGHT EXISTS + OWNER + LOCATION + HP/THREAT STATE + CURRENT ACTION`.

No conclusion is made here about which of these fields should become persistent AEGIS state. That is the Architect pass's job.

## 3.6 Economic/resource object state

**Observed capability:** resource, carried resource, gather type, and dropsite information are present in the historical source.

**Evidence grade:** DIRECT.

**Architectural implication:** resource intelligence can potentially be grounded in actual economic objects and their state rather than only global resource totals.

This matters because:

`600 wood`

and

`600 wood + 10 active woodcutters + functioning dropsite + safe access`

are strategically different situations even if the global stock number is identical.

That broader interpretation is architectural reasoning, not a claim that the historical AI explicitly represented the equation this way.

---

# 4. Search is a primitive computational workspace

This pass adopts the following source-derived principle:

> A search set is not merely a query result. It is a temporary workspace on which the controller performs computation.

The historical pattern repeatedly performs:

`reset search`
→ `find local/remote`
→ `filter by geometry`
→ `remove by semantic object-data conditions`
→ `order`
→ `select`
→ `read object data`
→ `aggregate`
→ `store result`.

This is particularly valuable because it explains how a constrained rule language obtains surprisingly sophisticated behavior from simple primitives.

The stock scout implementation is a strong example: it turns primitive coordinates and local object counts into centroids and weighted local strength. That is **behavioral leverage**, not primitive proliferation. fileciteturn300file0L2-L2

### AEGIS inheritance decision

**INHERIT:** search-as-workspace.

**MODERNIZE:** add explicit provenance and lifecycle semantics to the resulting derived state.

**REJECT:** building a separate abstract database merely to rename search operations.

---

# 5. Observation ≠ belief ≠ situation

This pass establishes the following separation as a required architectural boundary.

### Observation

What the machine directly obtained from an observation operation.

Example:

`selected object → object-data-id = X`.

### World Model

The current structured representation of relevant observed world entities/states.

Example conceptually:

`object X → enemy cavalry → location Y → observed state Z`.

### Belief Model

What AEGIS thinks may be true despite incomplete/currently unavailable observation.

Example:

`enemy probably retains cavalry outside current observation area`.

### Situation Model

What the combination of world facts and beliefs means strategically right now.

Example:

`cavalry pressure is currently the dominant military constraint`.

These four levels must not be collapsed.

In particular:

`INFERENCE MUST NOT MASQUERADE AS OBSERVATION.`

---

# 6. Freshness is unresolved at the primitive level

The architecture requires freshness, but the present evidence does not authorize us to pretend that every observation primitive automatically carries a usable timestamp or freshness guarantee.

Therefore the following are **architectural requirements, not yet qualified engine semantics**:

- observation time;
- age of information;
- invalidation conditions;
- stale-state handling;
- contradiction handling.

The historical source clearly performs repeated observation and uses state across rule evaluation, but that does not by itself prove a universal engine-level timestamp model.

**Status:** OPEN / requires qualification.

This is precisely the type of question that must not be filled in by architectural intuition.

---

# 7. Ownership is not yet an AEGIS allocation

The stock source demonstrates that goals/SNs can carry observations or derived state, and that object IDs can persist across evaluations.

It does **not** follow that a stock channel is safe for AEGIS ownership.

Layer 2 already rejected reuse of heavily multiplexed stock control channels as core AEGIS envelope fields.

Therefore this pass makes the following rule permanent:

> **Observation semantics may be inherited from stock; stock state-channel ownership may not be inherited merely because the channel looks convenient.**

The World Model may eventually consume observations and publish AEGIS-owned derived fields into the reserved namespace established by Layer 2, but no specific field allocation is made here.

---

# 8. The World Model should not become an encyclopedia

A critical architectural danger has emerged.

If we take the rich object-data surface literally, we could attempt to represent everything:

- every unit;
- every building;
- every resource object;
- every coordinate;
- every order;
- every target;
- every hitpoint;
- every production state;
- every research state.

That would reproduce the game state rather than build an AI abstraction.

The historical source provides a better clue:

> **Observe selectively according to the question being asked.**

Therefore the AEGIS World Model should eventually represent **decision-relevant world state**, not necessarily a complete replica of the engine's internal world.

This is a hypothesis for the Architect pass, not a finalized design.

---

# 9. Candidate World Model categories — NOT YET FINAL

The evidence supports investigating these categories:

1. **Actors / entities** — units, buildings, resource objects, relevant neutral objects.
2. **Ownership** — self, ally, enemy, neutral where directly supported.
3. **Identity** — persistent object ID where continuity is required.
4. **Spatial state** — position, distance, neighborhood, map zone where available.
5. **Lifecycle state** — pending, active, progressing, complete/ready where directly observable.
6. **Operational state** — action/order/target/under-attack/health where supported.
7. **Economic state** — resource/carry/gather/dropsite where supported.
8. **Aggregate state** — counts and weighted measurements derived from selected object sets.
9. **Capability state** — whether the observed object set appears to provide a usable capability, with the realization boundary kept explicit.
10. **Provenance** — how the observation was obtained.

These are **candidate categories**, not an approved schema.

---

# 10. Evidence grades for World Model work

Use this vocabulary in all subsequent passes:

### DIRECT
The exact primitive/field/use is present in verified source or independently measured machine evidence.

### COMPOSED
Multiple direct observations support a higher-order relationship.

### INFERRED / PROBABLE
The interpretation is strongly suggested but not explicitly established.

### ARCHITECTURAL PROPOSAL
AEGIS design choice, not historical fact.

### OPEN
Evidence is insufficient.

### REJECTED
A hypothesis has been tested or contradicted strongly enough that it should not guide architecture.

This is deliberately stricter than simply calling something “known.”

---

# 11. What this pass has actually closed

### CLOSED

- The historical AI has a broad object-level observation interface.
- Object identity is actively used for continuity.
- Search/filter/select/read is a real computational pattern in the source.
- Lifecycle/progress state is operationally relevant.
- Capability availability cannot safely be equated with mere object existence.
- Object-level observations can be transformed into higher-order measurements.
- Observation, command, world transition, and strategic effect must remain distinct.
- Replay normalized data is not currently sufficient to stand in for arbitrary live object-state lineage.

### NOT CLOSED

- Exact current-build runtime freshness semantics.
- Universal timestamp/age semantics for every observation.
- Exact dynamic object lineage through replay.
- Complete current-build exposure of every historical `object-data-*` field.
- Which observations deserve persistent AEGIS World Model state.
- Which observations should remain temporary search computations.
- Exact AEGIS storage representation.
- Goal/SN allocation.
- Runtime performance cost of the eventual observation architecture.

---

# 12. Scientific falsifiers

The following findings would force architectural revision:

**F1 — missing observation:** a supposedly available field is unavailable under the target build/runtime conditions.

**F2 — wrong semantics:** a field's actual meaning differs materially from the source-derived interpretation.

**F3 — non-persistence:** an identity or state assumed to survive repeated evaluation does not provide reliable continuity.

**F4 — freshness failure:** the engine does not provide enough information to distinguish current observation from stale observation for a proposed use.

**F5 — performance failure:** the observation pipeline requires search/filter work at a frequency that is operationally unacceptable.

**F6 — ownership collision:** the chosen representation cannot be isolated from stock/game writers.

**F7 — realization gap:** an observation/command chain appears complete but fails to produce the expected world-state postcondition.

---

# 13. Scientist's verdict

The first architectural temptation would be to design a sophisticated “World Database.”

**I reject that as the starting point.**

The evidence instead supports a more disciplined hypothesis:

> AEGIS should build a **decision-oriented World Model from selective, typed, lifecycle-aware observations**, using search as a temporary computational workspace and promoting only valuable results into persistent state.

That is not yet the final architecture. It is the strongest evidence-grounded starting hypothesis.

The stock AI's greatest lesson appears again here: it obtains substantial behavioral power by making primitive observation mechanisms do multiple jobs. AEGIS should inherit that leverage rather than burying it beneath an oversized data model.

---

# 14. Handoff to Architect

The Scientist phase is complete enough to hand the problem to the next mode.

The Architect's question is now:

> **Given only the evidence established here, what is the smallest World Model that can support the strategic spine without pretending to know information the engine cannot reliably provide?**

The Architect must not invent new engine capabilities.

It may invent **relationships and abstractions over proven capabilities**, provided every such abstraction is explicitly labeled as an AEGIS architectural proposal.

The next pass must produce:

1. a candidate World Model shape;
2. its minimum state envelope;
3. observation vs persistence rules;
4. proposed leverage paths;
5. producer/consumer ownership boundaries;
6. lifecycle/freshness handling as an explicit design problem;
7. a list of deliberate omissions;
8. a list of claims requiring later empirical qualification.

---

## Mode transition

**CURRENT:** 🔬 SCIENTIST — Evidence & Semantics  
**NEXT:** 🧠 ARCHITECT — World Model Abstraction  

No implementation. No runtime. No ABI allocation.
