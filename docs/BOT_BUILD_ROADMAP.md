# AEGIS Bot Build Roadmap

**Purpose:** Single path from current repo state to a workable civilian-first bot.  
**Authority:** Final Audit + `docs/progress/` + residual-risk rules.

---

## Phase 0 — Knowledge base (largely done)

- [x] Authority order + agent session contract
- [x] Final Reconstruction Audit open gates
- [x] Supersession register
- [x] Branch policy
- [x] Progress layer (load, ownership, ABI policy, probes, civilian contract)
- [x] Policy CI (GitHub Actions)

---

## Phase 1 — Live lifecycle evidence (current bottleneck)

1. Run fixed **CL-1** and **CL-3** probes on target build
2. Commit evidence under `docs/progress/evidence/`
3. Update residual-risk doc with results

**Exit:** Goal visibility confirmed; train path shows issued → pending and/or census change (or clean, documented failure modes).

---

## Phase 2 — Freeze civilian channels

1. Collision-check experimental blocks (403–554 region, timers 42–43) against typed census as far as static evidence allows
2. Freeze the channel set for the civilian slice in ownership inventory
3. Still **no** blanket production clearance — freeze means “these are the only numbers this slice may use”

---

## Phase 3 — Candidate integration root

1. One integration `.per` that loads only the civilian candidate modules needed for the slice
2. Remains marked NOT LOADED by production root until residual risk accepted
3. Chat/telemetry for stage visibility

---

## Phase 4 — Controlled playtest

1. Single-player controlled games
2. Record failures (no food, no TC, pop cap, pending without completion)
3. Fix only against observed failures — no architecture rewrites

---

## Phase 5 — Limited production promotion

Only when:

- Lifecycle evidence for actions used is recorded
- Ownership freeze documented
- Residual-risk acceptance written

Then promote a **narrow** production root for the civilian loop — not a full strategic bot.

---

## Explicitly later

- Cavalry threat containment slice
- Full economy optimization
- Military TSA closure
- Strategic-effect claims (W4)

---

## Non-goals until gates say otherwise

- XS
- Copying stock HD AI as AEGIS
- Resurrecting ADprom / byzwarcouncil
- Claiming completion from command issue alone
