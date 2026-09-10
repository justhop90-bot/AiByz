# AEGIS / AiByz — Agent Session Contract

**Purpose:** Pasteable hard rules for any AI session on this repository.  
**Authority parent:** `CANONICAL_AUTHORITY.md` + `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`  
**Effective:** 2026-09-10

---

## 1. Authority order (strict)

1. `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` — open-proof register
2. `docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07_REV2.md` — design manual
3. `docs/progress/` — current working material
4. `docs/BOT_BUILD_ROADMAP.md` — build sequence
5. `docs/MACHINE_EVIDENCE/` — machine captures
6. `AI_AGENT_START_HERE.md` + `CANONICAL_AUTHORITY.md` + this contract
7. `AI_OPERATING_PROTOCOL.md` + `docs/AI_TASK_TRIAGE.md` + `docs/SUPERSESSION_REGISTER_2026-09-09.md` + `docs/BRANCH_POLICY.md` + `docs/BRANCH_DISPOSITION.md`
8. Everything else is historical or supporting unless explicitly promoted

**Conflict rule:** A branch name, commit message, document title, or repeated historical claim cannot outrank the authority order above.

---

## 2. Hard bans

- Do not invent engine semantics.
- Do not treat numeric vacancy as allocation permission.
- Do not equate: command issued = accepted = pending = created = available = effective.
- Do not treat Promisory file presence as runtime load.
- Do not restart broad Layer-1 or Layer-2 archaeology.
- Do not resurrect ADprom, byzwarcouncil, XS, or scenario-loader automation as production paths.
- Do not promote candidate `.per` to production without closed gates / explicit residual-risk acceptance.
- Do not create parallel “final” handoffs or authority-sounding branches.
- Do not use Husky; shared automation is GitHub Actions only.
- Do not infer current status from historical branches, even when their names contain `final`, `canonical`, `master`, `signoff`, or `completion`.

---

## 3. Primary vertical slice

**Primary:** Civilian Production Loop — `docs/progress/07_CIVILIAN_VERTICAL_SLICE_CONTRACT_V0_2026-09-09.md`  
**Secondary:** Cavalry Threat Containment — deferred.

---

## 4. Evidence discipline

```text
CLAIM:
EVIDENCE CLASS: A1 | A2 | A3 | A4 | A5
WORLD LEVEL: W0 | W1 | W2 | W3 | W4
STATUS: CONFIRMED | PROBABLE | PLAUSIBLE | UNCERTAIN | OBSOLETE | DISPROVEN
SOURCE:
FALSIFIER:
```

Never promote W0 → W2/W3/W4 by intuition. A4/A5 cannot clear numeric ABI allocation.

---

## 5. State envelope

```text
VALID + OWNER + GENERATION + STAGE + PAYLOAD + (optional) EVIDENCE_LEVEL / ATTEMPTS / OBSERVED-AT
```

Candidate modules in `implementation/` must say **NOT LOADED by production root**.

---

## 6. Production coding gate

Blocked until minimum ownership/ABI freeze for used channels **and** command-lifecycle evidence for relied-upon actions (especially R5), **or** explicit residual-risk acceptance.

Live evidence goes in `docs/progress/evidence/`.

---

## 7. Task triage

Before starting substantive work, classify it as proof, architecture, implementation, qualification, documentation, or repository hygiene. Use `docs/AI_TASK_TRIAGE.md` to avoid reopening closed work and to select the minimum next action.

---

## 8. Version control

- `main` is the only canonical branch.
- Commit knowledge work to `main` when safe.
- Use `feature/`, `probe/`, or `experiment/` for isolated work when needed.
- Never treat historical `aegis/*` branches as live authority.
- Do not delete historical evidence merely because it is obsolete as authority.

---

## 9. Session re-anchor

At the beginning and end of a substantial session, identify:

1. Authority documents in force
2. Primary vertical slice
3. What remains blocked for production coding
4. What this session changed
5. What evidence is still missing
6. Which canonical artifact records the result

---

**End of contract.**
