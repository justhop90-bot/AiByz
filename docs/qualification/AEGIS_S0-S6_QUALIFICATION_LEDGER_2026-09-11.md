# AEGIS S0–S6 Qualification Ledger — 2026-09-11

## Normative maturity states

- **S0 — Absent:** no substantive artifact.
- **S1 — Research / Concept:** evidence, hypothesis, or design intent exists.
- **S2 — Specified:** formal contract, schema, invariants, or state model exists.
- **S3 — Statically Implemented:** actual `.per` implementation or validation machinery exists.
- **S4 — Static-Qualified:** S3 survives deterministic static/policy/contract validation with no known blocking static contradiction.
- **S5 — Runtime-Qualified:** the exact target AoE2DE build loads the tested source and demonstrates the required lifecycle with preserved evidence.
- **S6 — Strategically Qualified:** repeated target-runtime evidence establishes the intended operational/strategic effect with causal attribution and no unresolved alternative explanation.

### Absolute promotion rule

**S3/S4 never imply S5. S5 never implies S6.** Source comments, schemas, validators, GitHub Actions, replay commands, pending objects, or world deltas cannot independently establish target-engine causal success.

## Definitive AegisProm result

All **49/49** current files in `main/AegisProm` have been individually assigned a state and audited against the 16 adversarial invariants in:

`docs/qualification/AEGISPROM_MODULE_S0-S6_AUDIT_2026-09-11.md`

The audit is the detailed module ledger. This file is the normative state vocabulary and promotion boundary.

## Current aggregate disposition

| Qualification state | Current AegisProm interpretation |
|---|---|
| S0 | No current AegisProm source capability is classified S0 solely because it is undocumented; S0 is reserved for absent artifacts/capabilities. |
| S1 | Research/probe intent exists in parts of the tree. |
| S2 | Contracts and state models exist broadly, but the current source modules are generally beyond S2 because implementation exists. |
| S3 | **Dominant state:** implemented source whose target-engine behavior remains unproven. |
| S4 | Limited: modules with strong static/policy qualification, including bounded cavalry/production and candidate integration artifacts where applicable. S4 does not authorize runtime promotion. |
| S5 | **0 modules.** No target-build runtime evidence currently establishes the complete required lifecycle. |
| S6 | **0 modules.** No strategic-effect claim is authorized. |

## 16 adversarial invariants

1. **OWN** — state ownership explicit.
2. **WRITE** — authorized writer explicit.
3. **INIT** — initialization established.
4. **GEN** — generation fencing exists.
5. **VALID** — validity established/fail-closed.
6. **REQ** — physical request boundary explicit.
7. **ACCEPT** — engine acceptance/pending distinguished.
8. **WORLD** — world transition evidence explicit.
9. **CAUSAL** — causal attribution explicit and not inferred.
10. **RELEASE** — authority/lifecycle release exists.
11. **STALE** — stale-generation behavior fail-closed.
12. **IDEMP** — duplicate execution/re-entry controlled.
13. **LOSS** — evidence disappearance/failure handled.
14. **RACE** — competing producers/writers controlled.
15. **FALSE+** — false-positive advancement prevented.
16. **ABI** — external symbols/numeric channels safe for claimed role.

Audit notation: **P** = statically defensible; **△** = partial/external dependency/incomplete; **U** = runtime-unproven; **X** = identified defect/contradiction; **—** = not applicable.

## Non-negotiable findings from the individual audit

### P0 — Military selector initialization
`AEGIS-military-production-v0.per` declares and compares `aegis-mp-unit` without establishing its initialization locally. Selector initialization remains a blocker.

### P0 — Production reservation CR binding
The cavalry-response reservation grant must explicitly bind the authorization/request to the spearman resource/unit before the reservation is granted. Downstream dispatch predicates do not retroactively validate an invalid grant.

### P0 — Numeric ABI
Timer 42 and other experimental numeric blocks remain unqualified. Numeric vacancy is not allocation permission.

### P1 — Worker demand starvation
`AEGIS-worker-role-vector-v0.per` currently defines V0 desired role targets as zero unless another writer changes them. The worker execution chain can therefore be structurally present while normal demand is zero.

### P1 — Control-plane Execute is not physical execution
`Aegis-execution-final.per` propagates execution state; it does not itself issue the physical command. Physical execution lives in bounded adapters.

### P1 — Micro cross-file authority
Micro control, targeting, governor, bridge, and physical adapter form a cross-file mutable state machine. Transition/write ownership must be explicitly qualified before S5.

### P1 — Stock finaling provenance
`AEGIS-stock-finalingConstants.per` is not a clean canonical ABI namespace because of duplicate/conflicting definitions and conditional provenance. It is substrate/evidence, not production authority.

## Runtime promotion gate

A module can move S4→S5 only after the exact target build **101.103.48987.0 / BuildID 24094652 / Update #180059** demonstrates, as applicable:

`LOAD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE/DEMAND → FEASIBILITY → AUTHORIZATION → REQUEST → ACCEPT/PENDING → WORLD TRANSITION → ATTRIBUTION → CAUSAL CONFIRMATION → REASSESS`

with negative-path, idempotency, stale-generation, reproducibility, and evidence-integrity coverage.

## Strategic promotion gate

S5→S6 additionally requires repeated controlled evidence showing the intended operational/strategic effect. A successful command, unit-count delta, completed construction, or lifecycle confirmation alone is not strategic success.

## Governance

This ledger supersedes percentage-complete language for qualification decisions. The historical reconstruction audit remains authoritative for historical evidence; the module audit is authoritative for individual AegisProm maturity labeling; target-build evidence is authoritative for S5; repeated strategic evidence is authoritative for S6.

Production AEGIS remains **not qualified** until the required gates close.
