# AEGIS / AiByz — Agent Session Contract

**Purpose:** Pasteable hard rules for any AI session on this repository.  
**Authority parent:** `CANONICAL_AUTHORITY.md` + `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`  
**Effective:** 2026-09-09

---

## 1. Authority order (strict)

1. `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` — open-proof register
2. `docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07_REV2.md` — design manual
3. `docs/progress/` — current working material (ownership, ABI policy, probes, residual risk)
4. `docs/MACHINE_EVIDENCE/` — machine captures
5. `AI_AGENT_START_HERE.md` + `CANONICAL_AUTHORITY.md` + this contract
6. Everything else is historical or supporting unless explicitly promoted

If documents conflict, the higher item wins unless it explicitly preserves the lower item as unresolved evidence.

---

## 2. Hard bans

- Do not invent engine semantics.
- Do not treat numeric vacancy as allocation permission.
- Do not equate: command issued = accepted = pending = created = available = effective.
- Do not treat Promisory file presence as runtime load.
- Do not restart broad Layer-1 or Layer-2 archaeology.
- Do not resurrect ADprom, byzwarcouncil, XS, or scenario-loader automation as production paths.
- Do not promote candidate `.per` to production without closed gates / explicit residual-risk acceptance.
- Do not create parallel “final” handoffs that compete with the Final Audit or `docs/progress/`.

---

## 3. Primary vertical slice

**Primary (current):** Civilian Production Loop — see `docs/progress/07_CIVILIAN_VERTICAL_SLICE_CONTRACT_V0_2026-09-09.md`

**Secondary (deferred):** Cavalry Threat Containment — historical control strong; world realization still open.

---

## 4. Evidence discipline (mandatory)

Every non-trivial claim should be taggable as:

```text
CLAIM:
EVIDENCE CLASS: A1 | A2 | A3 | A4 | A5
WORLD LEVEL: W0 | W1 | W2 | W3 | W4
STATUS: CONFIRMED | PROBABLE | PLAUSIBLE | UNCERTAIN | OBSOLETE | DISPROVEN
SOURCE:
FALSIFIER:
```

Never promote W0 → W2/W3/W4 by intuition.  
A4/A5 can never clear numeric ABI allocation.

---

## 5. State envelope for AEGIS-owned channels

```text
VALID + OWNER + GENERATION + STAGE + PAYLOAD + (optional) EVIDENCE_LEVEL / ATTEMPTS / OBSERVED-AT
```

---

## 6. Production coding gate

Production `.per` remains **blocked** until:

- minimum ownership/ABI freeze for the channels used, and
- command-lifecycle evidence for the actions relied upon (especially R5), or
- an explicit, written residual-risk acceptance.

Candidate / experimental modules must remain marked as not loaded by any production root.

---

## 7. Session re-anchor (use after substantial work)

State in ≤5 lines:

1. Authority documents in force
2. Primary vertical slice
3. What remains blocked for production coding
4. What this turn changed
5. What evidence is still missing

---

## 8. Preferred work style

- Prefer labeling, supersession, and progress updates over rewriting history.
- Prefer minimum evidence to close an open R-gate over broad rediscovery.
- Prefer chatty, observable probes over silent assumptions.
- Preserve failures and negative evidence.

---

**End of contract.**
