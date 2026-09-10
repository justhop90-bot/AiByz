# AEGIS / AiByz — Canonical Authority

**Effective:** 2026-09-09 (knowledge-resource + hardening refresh)  
**Canonical branch:** `main` only — see `docs/BRANCH_POLICY.md`

GitHub `main` is the authoritative project starting point and durable project record.

---

## Canonical documents (live order)

1. `AGENT_SESSION_CONTRACT.md` — pasteable hard rules for AI sessions
2. `AI_AGENT_START_HERE.md` — orientation contract
3. `CANONICAL_AUTHORITY.md` — this file
4. `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` — **unresolved-proof register**
5. `docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07_REV2.md` — **design manual**
6. `docs/progress/` — **current working material**
7. `docs/BOT_BUILD_ROADMAP.md` — path to a workable civilian-first bot
8. `docs/SUPERSESSION_REGISTER_2026-09-09.md` — historical vs live docs
9. `docs/BRANCH_POLICY.md` — version-control rules
10. `docs/MACHINE_EVIDENCE/` — machine captures
11. `README.md` — public front door

Older handoffs, QC files, and Layer 2/3 passes remain for provenance. They are not competing live authorities.

---

## Authority rules

1. `main` is the sole canonical starting branch.
2. Prefer the newest committed evidence-backed artifact when documents conflict; verify explicit supersession.
3. Preserve superseded artifacts; do not erase research history to hide contradictions.
4. Machine facts require machine evidence at the appropriate authority class (A1–A5).
5. Numeric ABI allocation requires A1/A2/A3 evidence; A4/A5 can never clear it.
6. No `.per` implementation is authorized merely because an identifier appears unused.
7. Engine semantics, validator acceptance, and AEGIS design status are independent dimensions.
8. XS is outside project scope.
9. Scenario-loader automation is retired.
10. Every durable research/engineering result must be committed and independently verifiable in GitHub.
11. Historical branches (`aegis/*` handoffs/passes) are provenance, not alternate authority.
12. Primary vertical slice is the **Civilian Production Loop**; Cavalry is secondary/deferred.
13. Shared automation is **GitHub Actions** (`.github/workflows/policy.yml`), not Husky.

---

## Current engineering gate

```text
STOCK SNAPSHOT → IMPORT/LOAD CLOSURE → OWNERSHIP MATRIX → ABI / NUMERIC FREEZE
  → COMMAND LIFECYCLE PROBES (R5) → CIVILIAN VERTICAL QUALIFICATION
  → LIMITED PRODUCTION .PER
```

Numeric ABI remains **BLOCKED** (nothing cleared).  
Production coding remains **BLOCKED** until lifecycle/ownership gates close or residual risk is explicitly accepted.

See `docs/BOT_BUILD_ROADMAP.md` for the phased path.

---

## Target runtime

AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`

Untouched installed `resources\_common\ai` is the designated stock-runtime baseline.
