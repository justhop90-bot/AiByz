# AiByz — AEGIS Byzantine AI Engineering Repository

> Professional research, reverse-engineering, architecture, and implementation repository for a next-generation Byzantine AI for Age of Empires II: Definitive Edition.

## AI ENTRY POINT — READ THIS FIRST

**If you are an AI taking over this project, do not search the entire repository at random.**

Start with:

1. **`AGENT_SESSION_CONTRACT.md`** — hard rules (pasteable)
2. **`AI_OPERATING_PROTOCOL.md`** — anti-error workflow for AI reasoning and changes
3. **`AI_AGENT_START_HERE.md`** — orientation, traps, what is already solved
4. **`docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`** — definitive unresolved-proof register
5. **`docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07_REV2.md`** — design manual
6. **`docs/progress/`** — current working material (ownership, ABI, probes, residual risk, civilian slice)
7. `CANONICAL_AUTHORITY.md`
8. `docs/BRANCH_POLICY.md` + `docs/BRANCH_DISPOSITION.md`
9. Machine evidence and stock reconstruction maps as needed

**Do not treat older handoffs, experiments, or historical passes as competing current authorities.** They remain for evidence and provenance.

## Canonical status — 2026-09-10

**GitHub `main` is the authoritative starting point.**

The project has moved beyond broad archaeology. The current frontier is **machine-truth reconciliation and targeted runtime qualification**.

| Area | Status |
|------|--------|
| Layer 1 — Machine/runtime broad archaeology | ~89% — frozen; broad discovery closed |
| Layer 2 — Historical strategy archaeology | Major reconstruction closed; targeted evidence only |
| Layer 3A — AEGIS architecture | Closed for design; qualification active |
| Stock load reconstruction | High-confidence static closure in `docs/progress/` |
| Ownership / ABI allocation | Practical inventory exists; **nothing cleared** |
| Command lifecycle (R5) | Probes exist; live evidence required |
| Production `.per` | **Blocked** until gates close or residual risk accepted |

## Current frontier

Open-proof register: `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`

Highest gates before implementation:

`R1 load/conditional` → `R2 ownership` → `R3 numeric ABI` → `R5 command lifecycle` → first vertical qualification

## Primary vertical slice

**Civilian Production Loop** (current primary)  
Contract: `docs/progress/07_CIVILIAN_VERTICAL_SLICE_CONTRACT_V0_2026-09-09.md`

**Cavalry Threat Containment** remains secondary/deferred (strong historical control; world realization still open).

## Permanent boundaries

- Scenario-loader automation retired unless explicitly reopened
- XS outside scope
- HD/Promisory = historical evidence, not automatic target-runtime authority
- Commands are not completion proof
- Apparently unused numeric channels are not automatically safe
- `ADprom` / `byzwarcouncil` are not production architecture
- Architecture closure does not clear ABI semantics

## Target runtime

AoE2DE `101.103.48987.0` / BuildID `24094652` / Update `#180059`

Untouched installed `resources\_common\ai` is the stock-runtime baseline. Do not modify it during acquisition or qualification.

## Stock-system model

1. **`AI (HD version).per`** — flattened behavioral controller
2. **Promisory corpus** — provenance/reconstruction; existence ≠ runtime load
3. **Active runtime substrate** — chiefly `defaultConstants`, `finalingConstants`, conditional `finaling`

## Architecture

```text
WORLD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT
  → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE
  → VERIFY → RESULT → RECOVER/RE-ARBITRATE → REASSESS
```

Envelope: `VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Evidence: `W0 command → W1 pending/accepted → W2 world → W3 capability → W4 strategic effect`

## Repository organization

```text
AGENT_SESSION_CONTRACT.md   Hard rules for AI sessions
AI_OPERATING_PROTOCOL.md    AI anti-error workflow / stop conditions
AI_AGENT_START_HERE.md      Orientation contract
03_HD_ARCHAEOLOGY/          Historical strategy (see LAYER2_INDEX.md)
04_LAYER3_ARCHITECTURE/     Architecture (see LAYER3_CURRENT.md)
implementation/              Candidate .per modules (not production roots)
docs/                        Governance, Final Audit, machine evidence, progress/
docs/progress/               Current working engineering layer
```

## Immediate next gate

Do **not** begin production `.per` implementation yet.

Preferred sequence:

`AUTHORITY CONSISTENCY` → `OWNERSHIP / ABI FREEZE` → `LIVE LIFECYCLE PROBES` → `CIVILIAN SLICE QUALIFICATION` → `LIMITED PRODUCTION .PER`

The repository is organized so an AI can identify what is authoritative, what is historical, what is obsolete, what is already solved, and what still must be proven — without relying on conversational memory.
