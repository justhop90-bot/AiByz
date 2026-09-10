# AEGIS Supersession Register — 2026-09-09

**Purpose:** Single list of documents that are historical or secondary, and what to use instead.  
**Rule:** Prefer this register + live authority docs over any older “final” or “current status” claim.

---

## Live authority (use these)

| Role | Path |
|------|------|
| Agent hard rules | `AGENT_SESSION_CONTRACT.md` |
| Orientation | `AI_AGENT_START_HERE.md` |
| Authority rules | `CANONICAL_AUTHORITY.md` |
| Open-proof register | `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` |
| Design manual | `docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07_REV2.md` |
| Working material | `docs/progress/` |
| Machine evidence | `docs/MACHINE_EVIDENCE/` |
| Layer 2 navigation | `03_HD_ARCHAEOLOGY/LAYER2_INDEX.md` |
| Layer 3 living status | `04_LAYER3_ARCHITECTURE/LAYER3_CURRENT.md` |

---

## Engineering manuals — SUPERSEDED as primary design authority

| Document | Use instead |
|----------|-------------|
| `docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07.md` (original) | **Rev2** manual |
| `docs/AEGIS_GO_TO_ENGINEERING_MANUAL_2026-09-07.md` | Rev2 + Final Audit |
| `docs/AEGIS_GO_TO_MANUAL_QUALIFICATION_2026-09-07.md` | Final Audit + `docs/progress/` |
| `docs/AEGIS_MASTER_ENGINEERING_GUIDE.md` | Rev2 + Final Audit + progress/ |
| `docs/AEGIS_CIVILIZATION_SUBSTRATE_GUIDE.md` | Civilian slice contract + progress ownership/ABI docs; Rev2 for architecture |
| `docs/AEGIS_PERSONALITY_KNOWLEDGE_PACK_2026-09-07.md` | Supporting only; not implementation authority |

These files remain valuable as history. They are **not** the live rulebook.

---

## Project handoffs — SUPERSEDED as current status

| Document | Use instead |
|----------|-------------|
| `PROJECT_HANDOFF_CURRENT_2026-09-05.md` | Final Audit + `docs/progress/` + Start Here |
| `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md` | Same |
| `docs/CANONICAL_QC_2026-09-05.md` | Final Audit + progress residual-risk docs |

Note: handoffs still contain useful evidence summaries; do not treat their “current next step” sections as live if they conflict with the Final Audit or progress/.

---

## Layer 3 Phase 3B status cluster — SUPERSEDED for navigation

Use: `04_LAYER3_ARCHITECTURE/LAYER3_CURRENT.md`

Superseded as living status (keep as historical snapshots):

- `AEGIS_PHASE_3B_CURRENT_STATUS_2026-09-05.md`
- `AEGIS_PHASE_3B_ENGINEERING_STATUS_2026-09-05.md`
- `AEGIS_PHASE_3B_AUTONOMY_SUMMARY_2026-09-05.md`
- `AEGIS_PHASE_3B_COMPLETENESS_CHECKLIST_2026-09-05.md`
- `AEGIS_LAYER3B_PHASE_EXIT_CRITERIA_2026-09-05.md`
- `AEGIS_IMPLEMENTATION_READINESS_DECISION_2026-09-05.md`

---

## Cavalry vertical-slice pack — SECONDARY / DEFERRED

Primary slice is **Civilian Production Loop** (`docs/progress/07_...`).

| Document | Role now |
|----------|----------|
| `AEGIS_CAVALRY_VERTICAL_SLICE_QUALIFICATION_CONTRACT_2026-09-05.md` | Keep as secondary contract |
| Plan / sensor ABI / symbolic-numeric map (same folder) | Supporting; not primary implementation focus |

---

## Layer 2 — `03_HD_ARCHAEOLOGY`

| Class | Rule |
|-------|------|
| All `*_QC_PASS*` files | Supporting critique only — not primary authority |
| Sequential Pass 8–22 family | Historical evidence; broad discovery closed |
| Practical coding knowledge base | Reference for language discipline; not live project status |

Navigation: `03_HD_ARCHAEOLOGY/LAYER2_INDEX.md`

---

## Rejected / non-production (never revive as architecture)

Per Final Audit §5:

- ADprom as production architecture
- byzwarcouncil as production architecture
- V2/V3/V4 experimental architecture as grandfathered final design
- XS-based implementation
- Broad scenario-loader automation as primary test strategy
- Copying stock flattened AI into AEGIS as reconstruction method
- Treating entire Promisory tree as runtime load graph
- Treating numeric vacancy as permission to allocate

---

## How agents should apply this register

1. If a document is listed here as superseded → read it only as history/evidence.
2. For decisions → Final Audit, Rev2, `docs/progress/`, Session Contract.
3. Do not create a new “final handoff” that competes with those.
4. When updating status → update Final Audit open gates and/or `docs/progress/`, not old Phase 3B snapshots.
