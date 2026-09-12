# AEGIS AI Capability Audit — AIBuilder × AI(HD) × Promisory

**Date:** 2026-09-12  
**Status:** Deep static audit pass — research authority, no production code changes  
**Scope:** AIBuilder substrate, current AIByzBuild fork, installed stock AI (HD version).per, installed Promisory corpus, AI Scripting Encyclopedia/UserPatch documentation, and relevant public AI-engineering sources.

## 1. Executive verdict

This pass establishes that the current AEGIS runtime fork is in a much healthier state than the recent 20-mechanic experiment. The installed/repository AIBuilder execution modules are byte-identical across the nine core modules. The current AIByzBuild fork differs from the AIBuilder root primarily by path rebinding plus the existing Vertical Slice 1 rule; the execution modules themselves have not been replaced.

The major strategic finding is that **Promisory is not merely a larger version of AIBuilder**. It contains substantially deeper stateful behavior in scouting, gatherer retasking, threat telemetry, boar lifecycle, search/geometry, pending-object handling, defensive reaction, production arbitration, and attack/retreat control. The AI Scripting Encyclopedia confirms that many of these are native/high-value `.per` primitives rather than requiring an external language.

The correct AEGIS objective is therefore not to copy Promisory wholesale. It is to identify the functional contracts that make those systems competent, then reproduce only the contracts that are compatible with the preserved AIBuilder execution substrate.

## 2. Corpus inventory

The current local source audit measured the following byte/line boundaries:

| Corpus | Files | Bytes | Lines | SHA / note |
|---|---:|---:|---:|---|
| `AiBuilder.per` root | 1 | 55,542 | 1,426 | `12917E0F...DD4BAE` |
| `AiBuilder/` modules | 10 | 183,716 | 5,119 | current repository corpus |
| `AIByzBuild/` | 11 | 238,224 | 6,518 | current fork |
| Stock `AI (HD version).per` | 1 | 1,240,320 | 38,217 | `D7D10C33...C457199` |
| Installed `Promisory/` | 42 total files; 36 `.per` | 5,398,578 | 164,661 | current installed corpus |

`PromiDE.per2` is a separate composition root. Its current load sequence is:

```text
Promisory/defaultConstants
Promisory/finalingConstants
Promisory/customConstants
Promisory/init
Promisory/threats
Promisory/escrow
Promisory/dawn
Promisory/gatherers
Promisory/scoutcontrol
Promisory/tsa
Promisory/watercontrol
Promisory/general
Promisory/orb
Promisory/boarhunting
Promisory/researches
Promisory/interaction
Promisory/buildings
Promisory/units
Promisory/trade
Promisory/resign
Promisory/event
```

The historical Promisory composition also includes `Geometry.xs`. That is **historical evidence only**; AEGIS remains pure `.per` and must not adopt XS as an implementation dependency.

## 3. Current AEGIS/AIBuilder integrity finding

The following nine execution modules are byte-identical between repository `AiBuilder/` and `AIByzBuild/`:

- `constantsUP.per`
- `construction.per`
- `economy.per`
- `general.per`
- `market.per`
- `militaryBehavior.per`
- `militaryUnits.per`
- `phaseUpdate.per`
- `technologies.per`

Their SHA-256 values match exactly in each pair.

The current `AIByzBuild.per` root is the AIBuilder root with its load paths rebound to `AIByzBuild\\...` and the existing AEGIS Vertical Slice 1 appended. That is the correct architecture at this stage: **preserve the execution substrate; add policy incrementally.**

## 4. Ten high-value competence patterns

### 1. Phase-driven policy projection

**AIBuilder:** strong. `phaseUpdate.per` projects phase state into desired civilian, building, military, technology, exploration, and attack policy. The recent house/scouting regression demonstrated that removing this layer damages downstream systems even when the downstream construction/scouting code still exists.

**Promisory/HD:** also strong, but with substantially more specialized state and exception handling.

**AEGIS status:** **PRESERVE / DO NOT REPLACE.** The AIBuilder phase control plane is currently foundational.

---

### 2. Continuous economic control through actual worker state

Promisory's `gatherers.per` is much more stateful than AIBuilder's percentage projection. The Promisory corpus repeatedly uses gatherer identity, task state, cargo, source relationships, dropsite distance, object data, search state, and explicit retasking mechanisms.

Promisory contains multiple uses of:

```text
up-retask-gatherers
up-drop-resources
up-idle-unit-count
object-data-carry
object-data-hitpoints
up-path-distance
```

The UserPatch documentation explicitly describes `up-retask-gatherers` as a mechanism for forcing gatherers toward preferred resources after dropping resources, including resource-specific hunting/foraging/fishing classes.

**AEGIS status:** **MAJOR GAP.** AIBuilder has resource percentages and drop-distance controls, but not the same demonstrated gatherer continuity/retasking machinery.

---

### 3. Scouting as information acquisition with routing and recovery

Promisory `general.per` contains extensive use of `up-send-scout`, including enemy, corner, center, and other scouting modes. Promisory also has dedicated `scoutcontrol.per` and interacts with exploration strategic numbers and search state.

The Encyclopedia documents `up-send-scout`, `up-reset-scouts`, `up-point-explored`, `up-path-distance`, and related search/geometry operations. `up-reset-scouts` is explicitly documented as halting/disbanding soldier explore groups, meaning explorer policy and reset policy must be coordinated.

**AEGIS status:** **MAJOR GAP / HIGH PRIORITY.** The current AIBuilder substrate provides explorer goals and native group handling; the candidate AEGIS ScoutControl should remain disabled until it preserves those owners and does not fight `general.per`.

---

### 4. Threat telemetry and threat-aware reaction

Promisory `init.per` calls:

```text
up-get-threat-data gl-threat-time gl-threat-player gl-threat-source gl-threat-target
```

The Encyclopedia describes `up-get-threat-data` as returning elapsed time plus player, source, and target information for the latest threat.

Stock HD also contains the threat primitive.

**AEGIS status:** **HIGH-VALUE GAP.** This directly supports the AEGIS `THREAT → CAPABILITY` research line. The implementation should first model threat telemetry as observation/state, not immediately as counter-unit authorization.

---

### 5. Boar lifecycle and support-hunter management

Promisory's `boarhunting.per` is a large dedicated subsystem. It uses:

- `sn-enable-boar-hunting`
- `sn-minimum-boar-lure-group-size`
- `sn-minimum-boar-hunt-group-size`
- `sn-minimum-number-hunters`
- boar distance and food-source checks
- search state
- point distance
- villager/hunter census
- boar reset/recovery state

The UserPatch documentation is explicit: `sn-minimum-boar-lure-group-size` controls whether a new lure may start, while `sn-minimum-boar-hunt-group-size` controls the total active hunters desired during an existing lure; `up-request-hunters` can request support for an active lure.

**AEGIS status:** **KNOWN GAP; DO NOT RECREATE FROM MEMORY.** The previous AEGIS mistake of permitting a one-person early lure was precisely the kind of failure this subsystem's historical contract prevents.

---

### 6. Resource reservation / escrow-aware production

Promisory's `escrow.per` contains repeated uses of:

```text
can-research-with-escrow
can-train-with-escrow
```

The Encyclopedia confirms that these facts test whether research/training can start when escrowed resources are included. The command index also documents escrow-aware building feasibility.

**AEGIS status:** **HIGH-VALUE GAP / HISTORICAL CONTRACT AVAILABLE.** Escrow should be treated as engine-level resource reservation, distinct from any future AEGIS logical reservation layer.

---

### 7. Pending-state and placement-aware construction

Promisory `buildings.per` contains extensive `up-pending-objects` use and placement/search state. The Encyclopedia documents `up-pending-objects` as a comparison against the pending count of an object and separately documents `up-pending-placement`.

This establishes an important behavioral contract:

```text
request ≠ pending ≠ completed
```

The current AIBuilder construction system already uses pending objects in key rules, including housing. That behavior must be preserved.

**AEGIS status:** **SUBSTRATE PRESENT; CONTRACT SHOULD BE FORMALIZED.** This is a good candidate for an early vertical-slice verification boundary.

---

### 8. Geometry/search as a tactical decision layer

Promisory makes heavy use of:

```text
up-get-search-state
up-get-point-distance
up-path-distance
up-point-explored
up-find-player
up-get-fact
```

The Encyclopedia classifies several of these as high/very-high value operations. Promisory uses them to perform bounded searches, filter candidate objects, reason about distances, and select tactical targets.

**AEGIS status:** **MAJOR GAP IN APPLICATION, NOT PRIMITIVE AVAILABILITY.** The engine already exposes much of the required machinery; AEGIS currently does not apply it broadly enough.

---

### 9. Dynamic army control: attack, defense, retreat, and scaling

Promisory has extensive military behavior and strategic-number control. Its corpus includes strong use of attack-group sizing, exploration groups, targeting, defense, and retreat-related mechanisms. The Encyclopedia documents `up-retreat-now`, attack-group controls, targeting reset operations, projectile detection/target information, and multiple military search primitives.

The historical HD corpus additionally exposes the attack-state constants:

```text
retreat-now-goal = 20
attack-status-goal = 24
restart-attack-goal = 27
```

These are useful historical evidence of explicit attack lifecycle state, but their exact semantics should remain tied to the source in which they occur.

**AEGIS status:** **PARTIAL.** AIBuilder has attack grouping/timing/percentage controls, but Promisory demonstrates a much richer tactical lifecycle.

---

### 10. Defense and infrastructure as proactive state

Promisory contains extensive building, fortification, targeting, placement, and emergency infrastructure behavior. The UserPatch documentation also exposes strategic controls for tower targeting and related defensive behavior.

This includes the general pattern:

```text
threat / map state
    ↓
defensive requirement
    ↓
placement / production / targeting policy
    ↓
execution
    ↓
verification / recovery
```

**AEGIS status:** **PARTIAL.** AIBuilder has the construction substrate and phase-driven building goals; AEGIS still lacks a mature evidence-backed defensive policy layer.

## 5. Cross-corpus signal counts

A targeted lexical scan of the current installed corpora produced the following useful comparison. Counts are occurrences, not quality scores:

| Mechanism | Promisory | AIBuilder | Interpretation |
|---|---:|---:|---|
| `can-train-with-escrow` | 5 | 0 | Promisory-specific escrow production path |
| `can-research-with-escrow` | 72 | 104 | Both use escrow-aware research; AIBuilder has substantial research/escrow logic |
| `up-get-threat-data` | 1 | 0 | Promisory/HD threat telemetry is absent from AIBuilder |
| `up-send-scout` | 17 | 0 | Promisory has explicit scout dispatch; AIBuilder delegates exploration through native explorer machinery |
| `up-find-player` | 47 | 1 | Promisory performs far more explicit player/search work |
| `up-pending-objects` | 353 | 11 | Promisory has much deeper pending-state handling |
| `up-retask-gatherers` | 7 | 0 | Major economic control-plane gap |
| `up-drop-resources` | 11 | 0 | Major worker-cargo/resource continuity gap |
| `up-idle-unit-count` | 11 | 0 | Promisory explicitly reasons about idle units |
| `up-path-distance` | 25 | 0 | Major tactical geometry gap |
| `up-projectile-detected` | 124 | 0 | Promisory has extensive projectile/threat response |
| `up-projectile-target` | 57 | 0 | Promisory classifies projectile targets |
| `up-reset-unit` | 37 | 0 | Promisory actively resets unit activity in many recovery cases |
| `up-retreat-now` | 11 | 0 | Promisory has explicit emergency retreat use |
| `up-reset-scouts` | 20 | 0 | Promisory explicitly controls explorer lifecycle |
| `sn-home-exploration-time` | 40 | 1 | Scouting timing is much richer in Promisory |
| `sn-minimum-attack-group-size` | 34 | 0 | Promisory exposes explicit attack-group sizing |
| `sn-maximum-attack-group-size` | 24 | 0 | Promisory exposes explicit maximum attack-group sizing |
| `sn-scaling-frequency` | 1 | 0 | Promisory has an explicit scaling cadence |

These counts are diagnostic only. They do not mean that more occurrences are automatically better.

## 6. What this means for the ten common bot-improvement practices

The audit now supports the following classification:

| Practice | Current AEGIS/AIBuilder condition | Priority |
|---|---|---:|
| Preserve phase/build-order control | Strong | P0 — protect |
| Continuous economic state/retasking | Partial | P1 |
| Information-rich scouting | Partial | P1 |
| Threat → response | Missing as a mature layer | P1 |
| Adaptive army composition | Partial | P1 |
| Timing/temporal guards | Present in substrate | P2 |
| Proactive infrastructure | Present in substrate | P2 |
| Escrow/feasibility | Strong substrate; underused strategically | P1 |
| Defense ↔ offense coupling | Partial | P1 |
| Failure/recovery/reassessment | Strong pieces; not yet unified | P0/P1 |

## 7. Most important architectural conclusion

The evidence argues against another broad “20 mechanics” port.

The next improvements should be **vertical slices** that reuse the existing AIBuilder execution channels while importing one functional contract at a time from HD/Promisory.

The preferred migration form is:

```text
HISTORICAL MECHANISM
        ↓
FUNCTIONAL CONTRACT
        ↓
OBSERVATION
        ↓
STATE / BELIEF
        ↓
AUTHORIZATION
        ↓
EXISTING AIBuilder EXECUTION CHANNEL
        ↓
PENDING / WORLD TRANSITION
        ↓
VERIFICATION
        ↓
REASSESSMENT
```

Do not copy the Promisory implementation topology merely because it is larger.

## 8. Highest-value candidate slices

### Slice A — threat telemetry → skirmisher authorization

Already partially represented by current Vertical Slice 1. The next improvement should add observation/state separation and feasibility/reassessment without replacing `militaryUnits.per`.

### Slice B — boar safety/support

Use the historical boar contract to prevent underpowered lures and preserve recovery. This should remain isolated from the general economy until qualified.

### Slice C — gatherer continuity

Add one resource-transition contract using existing worker/resource facts and the native retasking machinery where its target-build semantics are established.

### Slice D — scout information lifecycle

Preserve AIBuilder explorer ownership while adding a narrowly scoped observation/targeting layer. No competing explorer-goal owner.

### Slice E — pending construction lifecycle

Formalize one building lifecycle: desired count → candidate placement → build request → pending object → completed object → reassessment.

## 9. Explicit prohibitions retained

- No XS.
- No replacement of the AIBuilder phase control plane.
- No wholesale Promisory import.
- No new Goal/timer allocation until the ABI extension question is closed.
- No inference that a command means completion.
- No inference that enemy infrastructure equals enemy army composition.
- No runtime claim from lexical/source evidence alone.
- No reactivation of the disabled AEGIS ScoutControl/BoarHunting modules until their ownership and lifecycle contracts are qualified.

## 10. Audit status

### Closed in this pass

- Current AIBuilder/AIByzBuild execution-module integrity.
- Current AIByzBuild root divergence from AIBuilder.
- PromiDE composition/load order.
- Promisory corpus inventory and size.
- Direct presence/absence of major tactical/economic primitives across the corpora.
- Ten high-value competence patterns and their AEGIS relevance.
- Initial historical-contract mapping for scouting, threats, boar, escrow, construction/pending state, gatherers, geometry, and military recovery.

### Still open

- Full symbol-level dependency graph across all Promisory modules.
- Full writer/reader graph for Promisory goals/SNs.
- Complete cross-generation comparison of every primitive used by HD and Promisory.
- Exact semantic reconstruction of the most important Promisory subsystems.
- Runtime authority/causality for new AEGIS writers.
- Promotion of any new mechanic into production.

## 11. Next research pass

The next pass should not begin by writing code. It should produce a **mechanic-by-mechanic contract table** for the ten priority capabilities:

```text
mechanic
→ historical source file(s)
→ source rule(s)
→ primitive(s)
→ state variables
→ writers
→ readers
→ preconditions
→ feasibility
→ action
→ pending evidence
→ completion evidence
→ failure paths
→ expiry
→ reassessment
→ AIBuilder equivalent
→ AEGIS insertion point
→ evidence class
→ promotion status
```

That is the point at which a historical mechanism becomes an AEGIS engineering candidate rather than another speculative feature port.
