# AEGIS C1 Package Integration / Authority Audit — Pass 42

**Date:** 2026-09-04  
**Layer:** 2 — strategy / implementation bridge  
**Predecessor:** Pass 41 C1 vertical slice  
**Status:** PASS — integration boundary mapped; implementation deliberately not yet promoted

## Executive result

Pass 41 is a valid isolated controller candidate, but it is **not yet a drop-in runtime module** for the canonical PORPHYRA V2.2.2 package.

The decisive finding is that V2.2.2 has **no downstream consumer for `traincamel`**. The Pass-41 controller can establish the AEGIS authority state and set `traincamel yes`, but the current V2.2.2 production package does not consume that state. Historical Promisory had a separate `traincamel` production pipeline; V2.2.2 does not.

Therefore the correct integration boundary is:

`C1 OBSERVE → REQUIRE → DEFICIT → COMMIT → AUTHORITY → C1 EXECUTION ADAPTER → TRAIN → VERIFY`

rather than pretending the historical `traincamel` contract already exists in the new runtime.

## Runtime baseline audit

The canonical local control candidate is **PORPHYRA V2.2.2**.

Its deployment contract is a flat set of files in:

`AoE2DE\resources\_common\ai`

with entry file `PORPHYRA_V2_2_2.ai` loading:

1. `PORPHYRA_V2_2_2_CONSTANTS`
2. `PORPHYRA_V2_2_2_BOOTSTRAP`
3. `PORPHYRA_V2_2_2_ECONOMY`
4. `PORPHYRA_V2_2_2_SCOUTING`
5. `PORPHYRA_V2_2_2_BOAR`
6. `PORPHYRA_V2_2_2_ECO_UPGRADES`
7. `PORPHYRA_V2_2_2_MILITARY_UPGRADES`
8. `PORPHYRA_V2_2_2_WALLS`
9. `PORPHYRA_V2_2_2_CONTROL`

The live game AI root was inspected separately. It currently contains the stock/Promisory-era root and **does not contain the PORPHYRA V2.2.2 package**. No runtime deployment was performed during this pass.

This prevents an accidental conflation of engineering baseline and live installation.

## Authority arbitration finding

V2.2.2 currently has one direct camel production rule in `PORPHYRA_V2_2_2_CONTROL.per`:

`castle-age + camel count < 8 + gold >= 100 + can-train camel → train camel`

It is a baseline capability rule, not a threat-deficit controller.

The same control module directly trains skirmishers and spears from enemy composition thresholds. No `traincamel` goal writer/reader pair exists in the V2.2.2 package.

Consequently, inserting Pass 41 unchanged would create **silent authority loss**: C1 would believe it had authorized production while no downstream rule necessarily acts on that authorization.

## Correct integration design

The next executable integration should make authority explicit.

### 1. Preserve C1 state namespace

Pass 41 goals `3830–3839` remain isolated from the V2.2.2 namespace `3950–3999`.

No renumbering is required.

### 2. Add a C1 execution adapter

The adapter should consume the AEGIS authority state directly and issue the native action only through a final feasibility gate:

`aegis-c1-authority = active`
`+ deficit > 0`
`+ can-train camel-line`
`→ train camel-line`

The adapter, not the controller, is the action boundary.

### 3. Arbitrate the existing baseline camel rule

The existing V2.2.2 camel-core rule must not remain an uncontrolled competing writer while C1 owns camel-response authority.

The preferred first integration is to gate baseline camel production when C1 has an active commitment, rather than deleting the baseline rule. This preserves a fallback path when C1 is inactive.

### 4. Keep verification world-facing

`set-goal traincamel yes` or `train camel-line` is **not** completion evidence.

C1 must continue to verify by observing the friendly camel capability count on later cycles.

### 5. Keep recovery explicit

If authority remains active while verified capability fails to increase for the configured persistence window, C1 should enter the existing stalled/recovery path rather than repeatedly issuing the same command without feedback.

## Load-order consequence

The C1 module must be loaded after its constants are defined and before/alongside the production-control boundary where its authority is consumed. The final action adapter must execute in a deterministic position relative to the existing camel rule.

The package should therefore be treated as a **single authority graph**, not a bag of independently valid `.per` files.

## Non-goals of this pass

- No live deployment.
- No scenario-loader testing.
- No resurrection of automated scenario testing.
- No claim that historical `traincamel` semantics transfer automatically to V2.2.2.
- No claim that the historical pressure/target ladder is optimal for Byzantines.

## Evidence grading

| Finding | Evidence |
|---|---|
| V2.2.2 is the canonical control package | DIRECT / project baseline |
| V2.2.2 flat load contract | DIRECT |
| V2.2.2 current camel rule is direct production | DIRECT |
| V2.2.2 has no `traincamel` consumer | DIRECT static audit |
| Pass 41 `traincamel yes` is inert without an adapter | COMPOSED |
| Baseline camel rule can compete with C1 | COMPOSED |
| C1 needs explicit authority arbitration | AEGIS-GENERALIZATION |
| Historical Promisory production architecture should be copied literally | DISPROVEN / rejected |

## Disposition

**PASS 42 closes the package-integration question far enough to implement safely.**

The important correction is architectural: AEGIS cannot inherit a historical state name and assume the historical downstream machine exists. The new runtime must explicitly construct the authority-to-action edge.

## Next target

**Pass 43 — C1 controlled package integration candidate:** add the smallest possible execution adapter, arbitrate the existing camel-core rule, run static package validation, and perform a code-level hostile review before any live installation.
