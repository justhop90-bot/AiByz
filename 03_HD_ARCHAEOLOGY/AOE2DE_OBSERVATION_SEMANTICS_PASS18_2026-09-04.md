# AoE2DE Observation Semantics Archaeology — Pass 18
Date: 2026-09-04
Layer: 2 — HD / Promisory strategic-code archaeology
Status: WORKING CANON — OBSERVATION SEMANTICS CLOSURE
Primary source: verified Promisory archive (`Promisory.zip`), exact `.per` source

## 1. Mission
Pass 18 reconstructs how the historical programmer turns engine-visible object state into usable strategic observations. The target is not merely the names of `object-data-*` fields. It is the semantic pipeline:

`WORLD OBJECTS → SEARCH SET → FILTER / SELECT → OBJECT OBSERVATION → DERIVED STATE → DECISION`

The replay W2 problem is deliberately not used as a premise. This pass asks what the AI itself was able to observe and how that observation was operationalized.

## 2. Direct observation surface
The verified Promisory source uses a broad object-data vocabulary. Confirmed fields include:

- identity/type: `object-data-id`, `object-data-type`, `object-data-class`, `object-data-player`, `object-data-ownership`
- geometry: `object-data-distance`, `object-data-full-distance`, `object-data-precise-distance`, `object-data-point-x/y/z`, `object-data-precise-x/y/z`, `object-data-move-x/y`
- lifecycle/progress: `object-data-progress-value`, `object-data-progress-type`, `object-data-researching`, `object-data-train-count`, `object-data-train-time`
- tactical state: `object-data-under-attack`, `object-data-hitpoints`, `object-data-target`, `object-data-target-id`, `object-data-action`, `object-data-order`, `object-data-attack-stance`, `object-data-attacker-count`
- placement/grouping: `object-data-group-flag`, `object-data-index`, `object-data-map-zone-id`
- economic/resource state: `object-data-resource`, `object-data-carry`, `object-data-gather-type`, `object-data-dropsite`

The source also defines numeric constants for several fields: `status-pending = 0`, `status-ready = 2`, `status-resource = 3`; `object-data-train-count = 31`, `object-data-researching = 41`, `object-data-train-time = 57`, and `object-data-progress-value = 61`.

These definitions establish that object data is not a decorative metadata layer. It is an active observation interface used by the rule system.

## 3. Observation is a pipeline, not a predicate
The recurring source pattern is:

`up-full-reset-search → establish target/filter geometry → find local/remote objects → remove objects by object-data → select object → read object-data → write goal/SN → act`

The programmer therefore treats the search structure as an intermediate state representation. A strategic decision is often produced only after several transformations of that search set.

## 4. Lifecycle semantics are explicitly operationalized
### 4.1 Construction / pending state
`buildings.per` uses:
`up-filter-status c: status-pending c: list-active`
and separately tests `object-data-progress-value` and `object-data-under-attack`.
A concrete rule deletes a foundation when it is under attack and has very low hitpoints, then issues `action-delete`.

This proves a historical distinction between an object existing in a pending/building state and a completed strategic structure. The programmer did not treat object existence as equivalent to completed capability.

### 4.2 Research progress
`buildings.per` filters town centers to objects with `object-data-researching == 1`, then checks `object-data-progress-value < 90` before continuing a control path for Feudal research.
This is direct evidence that research progress is represented at object level and used to distinguish active research from a merely existing building.

### 4.3 Production readiness / pending producer state
`units.per` repeatedly removes candidate production buildings with `object-data-progress-value >= 1` before selecting a production site. The same production paths remove buildings with `object-data-under-attack >= 1`, sort by distance, and require a valid surviving search candidate before issuing training.
This is a direct operational pattern:
`candidate producer → reject unfinished producer → reject endangered producer → rank/select → issue production command`.

### 4.4 Production command versus production-state observation
The source uses both command operations and object-state observations. Example: villager training reads town-center `object-data-progress-value`, while later production routines filter candidate producers by progress and attack state before issuing commands.
Therefore the historical architecture already separates at least partially:
`can/command eligibility` from `observed object lifecycle state`.

This is a stronger historical basis for AEGIS's pending/available distinction than replay ACTION telemetry alone.

## 5. Identity continuity is available inside the AI
The source explicitly reads and stores `object-data-id` into goals in several systems.
Examples include research/building and gatherer logic. Gatherer control stores livestock/object IDs, compares current and next livestock IDs against the current search object, and uses those IDs to maintain continuity across repeated rule evaluation.

This is critical: while our normalized replay corpus does not currently expose a complete production lineage, the AI itself has an object-identity channel and uses it as persistent control state.

Historical pattern:
`SEARCH OBJECT → object-data-id → persistent goal → later search object → ID comparison → continuity decision`.

## 6. The search set is programmable state
The source repeatedly composes:
- object discovery (`up-find-local`, `up-find-remote`, `up-find-status-local`, `up-find-status-remote`);
- geometric constraints (`up-filter-distance`, point targeting);
- semantic filters (`object-data-*` removal);
- ordering (`up-clean-search ... search-order-asc/desc`);
- selection (`up-set-target-object`);
- extraction (`up-get-object-data`, `up-get-point`);
- aggregate measurement (`up-get-search-state local-total`).

Thus a search is not merely a query. It is a temporary computational workspace.

## 7. Scout micro demonstrates multi-stage perception
`scoutcontrol.per` first discovers scouts, groups them, then computes a group centroid by repeatedly selecting the next object, reading its coordinates, accumulating X/Y, removing the processed object, incrementing a counter, and jumping back.

The same module then defines a safety-analysis path: it creates a bounded interpolation point toward the enemy, filters a local radius, counts nearby archers, then searches for spears, town centers, and castles. Later it computes enemy strength using weighted local counts.

The programmer therefore constructs higher-order observations from primitive object data:

`objects → geometry → local neighborhood → counts → weighted strength → tactical classification`.

This is direct mechanism plus composed strategic interpretation.

## 8. Object-data semantics reveal the programmer's mental model
The code repeatedly treats an AoE2 object as a stateful entity with:

`identity + type + ownership + position + progress + task/action + target + threat + capability context`.

This is substantially richer than a static unit count. It resembles an entity-state model built within the constraints of `.per`.

Strategic interpretation: the programmer was trying to answer not only "what exists?" but "what is this object doing, where is it, what state is it in, and can it currently be used?"

Evidence grade: COMPOSED / PROBABLE for the broad mental model; individual field usage is DIRECT.

## 9. Major discovery: capability is filtered through object state
A recurring pattern is:

`candidate exists → candidate is in valid lifecycle/status → candidate is safe/usable → candidate is selected → command issued`.

Examples:
- unfinished production/building objects are excluded;
- researching objects are excluded from some construction-selection searches;
- pending/ready/resource statuses are deliberately separated;
- endangered objects can be excluded or deleted;
- exact object IDs are persisted where continuity matters.

This means the historical controller is not simply `IF resource then action`. It is closer to a capability gate over a dynamically maintained object set.

## 10. Relation to replay W2
Passes 15–17 established that normalized replay ACTION data is strong for command chronology but weak for object lifecycle lineage.
Pass 18 shows that the historical AI source itself possesses richer object-level lifecycle observations than the normalized replay ACTION stream currently exposes.

Therefore the correct next question is no longer:
"Can replay ACTION records prove production completion?"

It is:
"Can we reconstruct or instrument the same object-level observation semantics the AI had at runtime?"

That is a fundamentally better experimental target.

## 11. AEGIS inheritance map
### Inherit
- object identity as persistent state where continuity matters;
- lifecycle-aware capability gates;
- search as a computational workspace;
- semantic filtering before commitment;
- explicit geometry and proximity calculations;
- aggregation only after primitive observations are established;
- separation of observation from strategic interpretation.

### Improve
- explicit typed observation records;
- provenance for every derived state;
- confidence and freshness on observations;
- stable identity lineage across production/research/build events;
- explicit pending/completed/available states;
- postcondition verification after commands.

### Reject
- treating a command as proof of world-state mutation;
- treating a raw object count as strategic commitment;
- treating temporary goals as semantically self-describing;
- relying on temporal proximity where identity continuity is required.

## 12. Evidence ledger
| Finding | Evidence | Grade |
|---|---|---|
| Object-data is a broad runtime observation interface | exact field definitions + repeated uses | DIRECT |
| Search sets are computational workspaces | repeated find/filter/select/read chains | COMPOSED |
| Lifecycle state is operationally relevant | progress/researching/status filters | DIRECT |
| Object identity is persisted for continuity | object-data-id → goals → later comparisons | DIRECT |
| Capability gates depend on lifecycle/safety | producer/foundation filters | COMPOSED |
| Scout system derives higher-order state from primitive observations | centroid + threat aggregation chains | COMPOSED |
| Programmer modeled objects as stateful entities | cross-module field usage | INFERRED / PROBABLE |
| Historical source can provide richer lifecycle semantics than normalized replay ACTION | source fields absent from normalized ACTION payload | DIRECT comparison |
| Exact production queue → created-object lineage is solved | not established | UNCERTAIN / OPEN |

## 13. Closure decision
**Pass 18 closes the observation-semantics question at the source level, but not the replay W2 lineage question.**

We now have a strong source-derived model of the historical observation stack:

`OBJECT SET → FILTER → SELECT → READ → DERIVE → STORE → DECIDE`.

The remaining runtime problem is instrumentation/access to those object-state channels, not conceptual uncertainty about what the historical AI was designed to observe.

## 14. Pass 19 target
Investigate the exact object-state observation vocabulary and runtime access path in the current engine/tooling, with priority on:
1. `object-data-id/type/progress/status/researching/train-count/train-time`;
2. pending-object and status queries;
3. object identity continuity;
4. whether mgz/mgz-fast source contains lower-level structures that preserve these fields;
5. whether the AI debug/chat/logging surface can expose them without scenario-loader automation.

Scenario-loader remains retired.
