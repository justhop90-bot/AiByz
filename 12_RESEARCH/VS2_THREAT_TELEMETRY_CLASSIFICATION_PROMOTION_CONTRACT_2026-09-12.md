# AEGIS Vertical Slice 2 — Threat Telemetry → Threat Classification

Date: 2026-09-12
Status: IMPLEMENTED LOCALLY / PROMOTION-READY CONTRACT / EXECUTION NOT PROMOTED

## 1. Scope

This slice realizes the observation and classification half of the canonical AEGIS threat lifecycle:

`ENGINE THREAT OBSERVATION → RAW AEGIS TELEMETRY → TEMPORAL VALIDITY → THREAT CLASSIFICATION`

It deliberately stops before response selection, production authorization, resource allocation, or military execution.

The implementation preserves AIBuilder executors. No `desired-*` goal, strategic number, training command, build command, research command, attack command, scout command, or military executor is modified by this slice.

The engine primitive `up-get-threat-data` provides elapsed time, player, source class, and target class for the latest threat record. This is consistent with the AI Scripting Encyclopedia/UserPatch command definition. citeturn0search0turn0search2

## 2. Installed insertion points

### Constants

`AIByzBuild/constantsUP.per`

Private AEGIS state IDs:

| Goal | ID | Role | Writer |
|---|---:|---|---|
| `aegis-focus-player-state` | 600 | reserved focus-state channel | future slice |
| `aegis-enemy-military-state` | 601 | recent hostile military classification | VS2 |
| `aegis-enemy-age-state` | 602 | reserved enemy-age channel | future slice |
| `aegis-threat-time-state` | 603 | raw elapsed threat age | VS2 engine write |
| `aegis-threat-player-state` | 604 | raw threat player | VS2 engine write |
| `aegis-threat-source-state` | 605 | raw attacker class | VS2 engine write |
| `aegis-threat-target-state` | 606 | raw target class | VS2 engine write |
| `aegis-under-attack-state` | 607 | recent military threat against villager/building | VS2 |
| `aegis-cavalry-threat-state` | 608 | source class = cavalry | VS2 |
| `aegis-archer-threat-state` | 609 | source class = archery | VS2 |
| `aegis-infantry-threat-state` | 610 | source class = infantry | VS2 |
| `aegis-forward-threat-state` | 611 | reserved; requires geometry | future slice |

The IDs were previously collision-audited against the installed AI corpus. No executor consumes these goals in VS2.

### Runtime module

`AIByzBuild/aegisThreatClassification.per`

### Root load

`AIByzBuild.per`

The module is loaded immediately after `AIByzBuild/constantsUP` and before the existing AIBuilder modules. This guarantees that AEGIS state definitions are available while leaving executor ownership unchanged.

## 3. Rule ledger

### R1 — Capture latest engine threat

**Input:** engine's latest threat record.

**Action:**

`up-get-threat-data aegis-threat-time-state aegis-threat-player-state aegis-threat-source-state aegis-threat-target-state`

**Postcondition:** all four raw telemetry goals contain the current engine-reported threat tuple.

**Failure/uncertainty:** the primitive reports the latest threat record, not a complete enemy-world model. No inference about unseen forces is permitted.

**Expiry:** derived state expires at 16000 ms. Raw telemetry remains available for inspection.

### R2 — Reset derived classification

Every evaluation pass clears the six derived classification channels before current telemetry is classified.

This makes classification idempotent with respect to the current threat tuple and prevents a previous cavalry/archer/infantry state from surviving after a different threat becomes the latest record.

### R3 — Fresh military threat

Preconditions:

- threat age `< 16000`
- threat player `>= 1`
- source class is cavalry, archery, infantry, or warship

Postcondition:

`aegis-enemy-military-state = 1`

No production or military goal changes occur.

### R4 — Cavalry classification

Preconditions:

- fresh threat
- hostile player
- source class = `cavalry-class`

Postcondition:

`aegis-cavalry-threat-state = 1`

### R5 — Archer classification

Preconditions:

- fresh threat
- hostile player
- source class = `archery-class`

Postcondition:

`aegis-archer-threat-state = 1`

### R6 — Infantry classification

Preconditions:

- fresh threat
- hostile player
- source class = `infantry-class`

Postcondition:

`aegis-infantry-threat-state = 1`

### R7 — Local attack classification

Preconditions:

- fresh hostile military threat
- target class = `villager-class` OR `building-class`

Postcondition:

`aegis-under-attack-state = 1`

This is intentionally narrower than claiming that the entire town is under attack.

### R8 — Forward-threat non-inference

`aegis-forward-threat-state` is not derived from `up-get-threat-data` alone. The primitive provides source and target classes but not the spatial relationship required to prove a forward threat.

Therefore VS2 leaves this state at zero. A future geometry-qualified slice may own it.

## 4. State ownership

| State class | Owner | Consumers in VS2 |
|---|---|---|
| Raw threat tuple | AEGIS telemetry module | AEGIS only |
| Threat freshness | AEGIS classification module | AEGIS only |
| Military threat | AEGIS classification module | none yet |
| Cavalry/archer/infantry threat | AEGIS classification module | none yet |
| Local attack | AEGIS classification module | none yet |
| Forward threat | no owner in VS2 | none |
| AIBuilder desired-* goals | existing AIBuilder modules | unchanged |
| AIBuilder strategic numbers | existing AIBuilder modules | unchanged |
| Military execution | existing military modules | unchanged |

## 5. Explicit forbidden transitions

VS2 MUST NOT:

- change `sn-target-player-number`
- change `sn-focus-player-number`
- change `desired-number-spearmen`
- change `desired-number-skirmishers`
- change `desired-number-archers`
- change `desired-number-camelriders`
- change `desired-number-watchtowers`
- change attack-group state
- call `up-send-scout`
- call `up-retreat-now`
- issue `train`, `build`, `research`, or attack commands
- modify escrow
- modify gatherer allocation
- infer unseen enemy composition
- equate threat telemetry with combat success

## 6. Temporal contract

Freshness threshold: **16000 ms**.

Rationale: Promisory repeatedly treats threat telemetry as temporal state and uses thresholds in the same order of magnitude, including 16000 ms windows. This is a source-derived timing boundary, not a claim that 16000 ms is an engine-defined semantic constant. The AI Scripting Encyclopedia confirms that threat data exposes elapsed time. citeturn0search2

When stale:

- raw telemetry is preserved;
- all VS2 derived threat classifications are cleared;
- no downstream response is authorized.

## 7. Evidence contract

`up-get-threat-data` result = **DIRECT engine observation**.

Source-family classification = **COMPOSED** from direct source-class output plus an explicit class predicate.

`enemy-military-state` = **COMPOSED**, not proof of enemy army size or strategic intent.

`under-attack-state` = **COMPOSED**, limited to a recent hostile military threat whose target class is villager/building.

`forward-threat-state` = **UNCERTAIN / NOT PROMOTED** until geometry evidence exists.

No state in VS2 claims strategic success.

## 8. AIBuilder preservation gate

AIBuilder is retained as the execution substrate. Its public project describes generated AI as having basic build/attack instructions and relying on library files for common behavior. VS2 therefore adds an observational control layer without replacing those executors. citeturn0search3turn0search4

The critical invariant is:

`AEGIS observes/classifies → AIBuilder remains executor`

not:

`AEGIS observes/classifies → AEGIS commandeers executor`

## 9. Static qualification

Local qualification performed after installation:

- AEGIS goal-definition duplicate scan: **0 duplicates**
- `.xs` references in `AIByzBuild/*.per`: **0**
- parenthesis imbalance in `AIByzBuild/*.per`: **0**
- root load insertion verified after `constantsUP`
- AoE2DE launched with `-autogame -AIdebug`
- installed build observed: `101.103.48987.0`
- game process successfully initialized and ran during the qualification window

This proves loadability/syntax at the installed runtime boundary. It does **not** prove that a real combat event populated every classification branch; that distinction is intentional.

## 10. Promotion criteria

VS2 is promotion-ready when all of the following remain true:

1. raw telemetry remains AEGIS-owned;
2. derived classifications are private AEGIS state;
3. 16000 ms expiry is enforced;
4. classification is idempotent per current telemetry;
5. no AIBuilder executor is modified;
6. no strategic-number ownership is changed;
7. no production authorization is inferred from classification;
8. forward threat remains unclassified without geometry;
9. runtime load remains clean;
10. a later slice may consume these states only through an explicit reader contract.

## 11. Next vertical slice

The correct next promotion is **Threat Classification → Contextual Response Authorization**, not direct unit production.

That slice should add a separate response-state owner which consumes VS2 classifications and determines whether a response is authorized, expired, feasible, and reassessed. Only after that authorization contract is proven should existing AIBuilder production goals be conditionally influenced.
