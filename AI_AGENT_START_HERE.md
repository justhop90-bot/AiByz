# AEGIS / AiByz — AI Agent Start Here

**Canonical purpose:** This file is the first orientation document for any AI or engineer entering the repository. Read it before interpreting individual archaeology files, experiments, architecture drafts, or implementation candidates.

**Canonical branch:** `main`
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`
**Scope:** pure `.per`; XS is out of scope.

## 0. The single most important rule

**Do not infer the current project state from filenames, directory names, old handoffs, or isolated source vocabulary.**

The repository contains historical research, failed experiments, superseded architectures, runtime candidates, forensic evidence, and current authority documents side-by-side because preserving negative evidence is intentional.

The current project is not asking: “What might AoE2 AI do?”

It is asking: **“What does the target stock machine demonstrably do, what remains unproven, and how do we reconstruct AEGIS without silently inventing semantics?”**

## 1. Read in this order

1. `README.md`
2. `CANONICAL_AUTHORITY.md`
3. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
4. `docs/CANONICAL_QC_2026-09-05.md`
5. `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` — current unresolved-proof register
6. `docs/architecture/AEGIS_STOCK_SUBSYSTEM_RECONSTRUCTION_MAP_2026-09-08.md` — stock subsystem/load/ownership reconstruction
7. `docs/forensics/P0_TOTAL_SUBSTRATE_DECONSTRUCTION_PASS_2026-09-08.md`
8. `RESEARCH_INDEX.md`
9. Only then enter historical Pass 9–13 and earlier archaeology as needed.

If an older document conflicts with a newer canonical audit, **the newer canonical audit wins unless it explicitly preserves the older item as unresolved evidence.**

## 2. Project status in one page

### Closed or substantially closed

- Broad Layer-1 machine archaeology: frozen at 89%.
- Broad Layer-2 historical strategy archaeology: closed; targeted evidence only.
- Layer-3A AEGIS architecture: closed for implementation design.
- Historical control-chain reconstruction: extensive and substantially closed.
- Stock subsystem reconstruction map: present.
- Stock runtime import closure: substantially mapped.
- Fact/class/foundation/object-data ABI inventory: substantially mapped.
- Construction OS forensic/ABI work: substantially investigated.
- Replay evidence/indexing pipeline: real code exists and has been calibrated on real target-build replay data.

### Still open

The project is now in **machine-truth reconciliation and qualification**, not broad archaeology.

The remaining work is to prove or explicitly leave unresolved:

1. exact effective conditional compilation/load semantics;
2. complete mutable-state ownership and channel semantics;
3. numeric ABI allocation for AEGIS-owned state/operations;
4. runtime lifecycle transitions from issued command to accepted/queued/created/available/effective;
5. selected world-state observations and their semantic units;
6. strategic-effect qualification where claims exceed control evidence;
7. complete disposition of undercovered stock services such as research, TSA, scouting, trade, water, boar, interaction, general/init/orb/resign;
8. consistency of all old research against the current canonical model.

## 3. What the stock AI evidence actually means

The stock system has three evidence/provenance layers:

1. `AI (HD version).per` — flattened behavioral controller and primary historical behavior body.
2. `Promisory` source corpus — decomposed source material useful for reconstruction, but not automatically runtime-loaded.
3. Active runtime substrate — the target stock load closure, chiefly `defaultConstants`, `finalingConstants`, and conditional `finaling`, with only proven nested imports on directly loaded Promisory modules.

**Do not equate source-corpus presence with runtime dependency.**

The reconstruction map documents this distinction explicitly.

## 4. Evidence discipline

Use these distinctions in every conclusion:

- DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN
- CONFIRMED / PROBABLE / PLAUSIBLE / DISPROVEN / OBSOLETE
- A1 exact target package/build
- A2 verified package snapshot
- A3 byte/content-equivalent repository snapshot
- A4 historical/source material
- A5 inference

Runtime evidence levels:

`W0 command only → W1 accepted/pending execution evidence → W2 world-state observation → W3 operational capability → W4 strategic effect`

Do not promote W0 to W2/W3/W4 by intuition.

## 5. Semantic traps that repeatedly caused mistakes

- `GOAL`, `SN`, `FLAG`, and `TIMER` are different channels.
- Numeric equality is not semantic identity.
- Declaration is not runtime state.
- Validator acceptance is not engine semantics.
- Command issued is not command accepted.
- Queue/dequeue is not object creation.
- Build command is not construction completion.
- Research command is not technology completion.
- Aggregate object counts are not individual object lineage.
- Historical behavior is not target-build runtime proof.
- A source comment is not an active load dependency.
- An unused-looking numeric value is not automatically safe for AEGIS allocation.
- A native/test-harness symbol embedded in the executable is not proof of retail invocability.
- Architecture closure does not clear ABI semantics.

## 6. Architecture model

AEGIS is a stateful strategic controller:

`WORLD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT → CANDIDATES → RESOURCE/TIMING EVALUATION → COMMIT → AUTHORIZE → EXECUTE → VERIFY → RESULT CLASSIFICATION → RECOVER/RE-ARBITRATE → REASSESS`

Mandatory state envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Controller time and world time are distinct.

## 7. First implementation target

**Cavalry Threat Containment** is the first executable vertical slice.

Historical evidence already closes much of its control path:

`enemy composition observation → threat aggregate → camel requirement → traincamel authorization → stable search → can-train → train command`

What remains before implementation is proving the required machine/runtime semantics and postconditions. Do not treat the historical chain as automatic target-runtime proof.

## 8. What NOT to do

Do not:

- restart broad Layer-1 archaeology;
- rebuild the project from stock AI by copying `AI (HD version).per` into AEGIS;
- resurrect `ADprom` or `byzwarcouncil` as production architecture;
- restart retired scenario-loader automation unless explicitly reopened;
- introduce XS;
- promote an experimental branch merely because it exists;
- treat CaptureAge as core semantic authority;
- use hidden native test-harness facilities without independent qualification;
- silently make AoE2Control/invasive instrumentation a core dependency;
- claim completion from a command stream alone;
- fill unknowns with plausible engine semantics.

## 9. How to work from here

When investigating a question:

1. Find the current canonical status first.
2. Search the recent P0/reconstruction documents before older archaeology.
3. Identify the exact source/build evidence.
4. Separate runtime dependency from historical source provenance.
5. Trace declaration → writer → reader → guard → side effect → reset/reassessment.
6. Assign evidence level and confidence.
7. Record the unresolved boundary explicitly if world/runtime proof is missing.
8. Update the canonical audit rather than creating another competing handoff.

## 10. The current question

The project has enough research to stop asking “what else can we discover?” in the broad sense.

The current question is:

> **Which exact claims/cells remain unproven in the machine model, and what minimum evidence would close each one?**

That register is maintained in:

`docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`

That document is the authoritative starting point for the next engineering phase.
