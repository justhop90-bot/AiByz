# AEGIS / AiByz — AI Agent Start Here

**Canonical purpose:** First orientation document for any AI or engineer entering the repository.  
**Canonical branch:** `main`  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Scope:** pure `.per` only; XS is out of scope.  
**Updated:** 2026-09-09 (knowledge-resource pass)

Also read: `AGENT_SESSION_CONTRACT.md` (pasteable hard rules).

---

## 0. The single most important rule

**Do not infer the current project state from filenames, directory names, old handoffs, or isolated source vocabulary.**

The repository intentionally preserves historical research, failed experiments, superseded architectures, and negative evidence.

The current question is not “What might AoE2 AI do?”  
It is: **What does the target stock machine demonstrably do, what remains unproven, and how do we reconstruct AEGIS without inventing semantics?**

---

## 1. Read in this order

1. `AGENT_SESSION_CONTRACT.md` — hard rules
2. `CANONICAL_AUTHORITY.md`
3. `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` — **current unresolved-proof register**
4. `docs/AEGIS_FORWARD_ENGINEERING_MANUAL_2026-09-07_REV2.md` — design manual
5. `docs/progress/` — **current working material** (ownership, ABI policy, probes, residual risk, civilian slice)
6. `README.md`
7. Stock subsystem reconstruction map and machine evidence as needed
8. Only then enter historical Layer 2 / Layer 3 passes as supporting evidence

If an older document conflicts with the Final Audit or `docs/progress/`, the newer canonical material wins unless it explicitly preserves the older item as unresolved evidence.

---

## 2. Project status (2026-09-09)

### Closed or substantially closed

- Broad Layer-1 machine archaeology (frozen ~89%)
- Broad Layer-2 historical strategy archaeology (targeted evidence only going forward)
- Layer-3A architecture design
- Stock subsystem / load reconstruction (static high-confidence closure recorded in progress/)
- Fact/class/foundation/object-data ABI inventory (allocation still gated)
- Replay indexer boundary (commands ≠ completion)

### Open (qualification frontier)

Tracked in the Final Audit R1–R19 register. Highest priority for implementation:

1. R1 effective load / conditional closure (static advanced; full conditional graph still open)
2. R2 complete mutable-state ownership (practical civilian inventory exists; full matrix open)
3. R3 numeric/typed ABI allocation (**nothing cleared**)
4. R5 command lifecycle (probes designed; live evidence required)
5. World realization for the first vertical slice

### Production `.per`

**Blocked** until required gates close or residual risk is explicitly accepted.

---

## 3. Primary vertical slice

**Primary (current):** Civilian Production Loop  
See `docs/progress/07_CIVILIAN_VERTICAL_SLICE_CONTRACT_V0_2026-09-09.md`

**Secondary (deferred):** Cavalry Threat Containment  
Historical control path is strong; target-build world/strategic realization remains open.

---

## 4. Stock evidence layers

1. `AI (HD version).per` — flattened behavioral controller
2. Promisory corpus — reconstruction/provenance; **not** automatic runtime load
3. Active runtime substrate — primarily `defaultConstants`, `finalingConstants`, conditional `finaling` (see progress load-closure doc)

Do not equate source-corpus presence with runtime dependency.

---

## 5. Evidence discipline

- Classes: A1 (exact target) > A2 > A3 > A4 (historical) > A5 (inference)
- World levels: W0 command only → W1 pending/accepted → W2 world observation → W3 capability → W4 strategic effect
- Statuses: CONFIRMED / PROBABLE / PLAUSIBLE / UNCERTAIN / OBSOLETE / DISPROVEN

Never promote lower evidence by intuition. A4/A5 cannot clear numeric allocation.

---

## 6. Semantic traps (repeated failure modes)

- GOAL / SN / FLAG / TIMER are different channels
- Numeric equality ≠ semantic identity
- Declaration ≠ runtime state
- Validator acceptance ≠ engine semantics
- Command issued ≠ accepted ≠ pending ≠ created ≠ available ≠ effective
- Build/research/train command ≠ completion
- Aggregate counts ≠ object lineage
- Historical behavior ≠ target-build proof
- Unused-looking number ≠ safe allocation
- Architecture closure ≠ ABI clearance

---

## 7. Architecture model

```text
WORLD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT
  → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE
  → VERIFY → RESULT → RECOVER/RE-ARBITRATE → REASSESS
```

Mandatory envelope: `VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

---

## 8. What NOT to do

- Restart broad Layer-1/2 archaeology
- Copy stock flattened AI into AEGIS as the reconstruction method
- Resurrect ADprom / byzwarcouncil / XS / scenario-loader automation
- Treat experimental branches as production authority
- Claim completion from command streams alone
- Fill unknowns with plausible engine semantics
- Hijack high-traffic stock channels without evidence-backed takeover design

---

## 9. How to work

1. Find current canonical status first (Final Audit + progress/)
2. Identify exact evidence class and world level
3. Separate runtime dependency from historical provenance
4. Trace declaration → writer → reader → guard → effect → reset
5. Record unresolved boundaries explicitly
6. Update Final Audit / progress docs rather than creating competing handoffs

---

## 10. The current question

> Which exact claims remain unproven in the machine model, and what minimum evidence would close each one?

Authoritative register: `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`  
Current working layer: `docs/progress/`
