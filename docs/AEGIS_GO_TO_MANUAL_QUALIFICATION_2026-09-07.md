# AEGIS Go-To Engineering Manual — Qualification Report
## 2026-09-07 Hard Qualification

**Project:** AEGIS-BYZ
**Manual qualified:** `docs/AEGIS_GO_TO_ENGINEERING_MANUAL_2026-09-07.md`
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Repository:** `justhop90-bot/AiByz`
**Verdict:** CANONICAL / ENGINEERING-QUALIFIED WITH EXPLICIT RUNTIME BOUNDARIES

---

# 1. Purpose

This report is the final hard-QC record for the go-to AEGIS engineering manual. The manual was checked against the accumulated target-build stock forensics, recent economic/civilian/production/control-flow reports, the external ABI cross-reference, and authoritative external documentation.

The question was not whether the manual is complete in an absolute sense. No engineering manual can be complete while target-build runtime questions remain unqualified. The question was whether it is safe to use as the project's controlling engineering doctrine without causing known evidence, architecture, ownership, or qualification errors.

Answer: **yes, with the explicit boundaries recorded below.**

---

# 2. Evidence cross-check

## 2.1 Target-build stock

The manual's central civilization-substrate conclusions agree with the forensic record:

- worker allocation is a feedback process rather than a static percentage table;
- resource selection includes object status, task load, spatial/service constraints, and resource-specific filters;
- dropsite topology participates in resource acquisition;
- construction has pending/foundation/builder/placement/recovery state;
- production contains goal arbitration, suppression, escrow/authorization, endpoint selection, and command stages;
- threat behavior is distributed rather than a proven universal civilian evacuation manager;
- `object-data-tasks-count` is controller-specific workload evidence, not universal capacity;
- command issuance is distinct from engine-state confirmation;
- recovery is distributed across subsystems;
- rule ordering and `up-jump-rule` are executable control-flow mechanisms.

These are therefore safe as architectural foundations.

## 2.2 External scripting documentation

The AoE2 AI Scripting Encyclopedia explicitly covers Definitive Edition scripting and provides command, parameter, strategic-number, fact, object-data, resource, technology and unit-line references. It also identifies `up-jump-rule`, `up-log-data`, `up-modify-goal`, `up-modify-sn`, `set-goal`, and `set-strategic-number` as scripting primitives. This is strong semantic cross-reference but is not treated as target-build behavioral proof.

Official World's Edge Update 61321 independently confirms that DE exposes `AIDEBUGGING`, `fe-break-point`, script-position/state diagnostics, infinite jump-loop detection, `AISCRIPTDEBUGGING`, and `LogSystems=AIScript`. This validates the manual's decision to make interpreter instrumentation part of the qualification system.

## 2.3 Version discipline

The manual correctly treats later official updates as evidence that the engine continues to evolve, not as proof that later behavior existed unchanged in the target build. Target-build stock and target-build runtime evidence remain controlling.

---

# 3. Architecture qualification

### PASS — cognition preserved, substrate rebuilt

The manual correctly rejects a full restart. Belief → Situation → Objectives → Planning → Decision → Commitment remains useful strategic cognition, while Economy, Worker Allocation, Resource/Logistics, Construction, Production, Information, Military, Civilization State, Verification and Recovery become the principal reconstruction targets.

### PASS — feedback architecture

The manual correctly replaces the misleading linear-stack interpretation with a closed-loop control architecture:

```text
INTENT
 → DEMAND / ARBITRATION
 → SERVICE
 → ENGINE
 → OBSERVATION / RECONCILIATION
 → VERIFICATION / RECOVERY
 → COGNITION
```

The former L0→L12 model remains useful only as a dependency map and is explicitly no longer treated as execution order.

### PASS — authority boundary

The engine/game is authoritative. Civilization State is a reconciled AEGIS representation. This distinction is mandatory and correctly stated.

### PASS — ownership

The manual assigns ownership to cognition, arbitration, reservation/escrow, Civilization State, operating services, ABI, verification, recovery and telemetry without allowing one service to silently become another service's state owner.

---

# 4. ABI qualification

### PASS — syntax/reference boundary

External references are correctly treated as semantic accelerators rather than target-build proof.

### PASS — jump semantics

The manual correctly treats `up-jump-rule` as executable control flow. The external reference states that it jumps forward or backward within the current rule set. Official DE documentation independently confirms dedicated tooling for jump/control-flow problems.

### PASS — mutation boundary

The manual does not overclaim universal same-pass visibility. Goal/SN mutation primitives are documented, but exact target-build visibility across every evaluation context remains a runtime question.

### PASS — command/confirmation distinction

The manual consistently distinguishes command issuance from engine-state observation and productivity/verification.

### PASS — ABI instrumentation

The manual correctly makes target-build probes and logging mandatory for unresolved interpreter semantics.

---

# 5. Civilization-substrate qualification

### PASS — Civilization State

Correctly defined as reconciled state with freshness/generation rather than strategy or authority.

### PASS — Economy

Correctly separates:

1. strategic commitment;
2. economic demand;
3. logical reservation;
4. engine escrow;
5. execution authorization;
6. queue endpoint;
7. confirmation.

This matches the stock forensic distinction and prevents the common architectural error of collapsing all economic state into one Boolean or one reservation ledger.

### PASS — Worker allocation

Correctly modeled as desired-role target → actual-role census → deficit → eligible workers → source/dropsite qualification → command → observation → productivity.

### PASS — Resource/logistics

Correctly avoids a universal resource-good/resource-bad state and preserves resource-specific task-load thresholds and serviceability constraints.

### PASS — Construction

Correctly represented as a persistent lifecycle rather than a one-shot build command.

### PASS — Production

Correctly rejects a universal FIFO assumption and separates demand, arbitration, reservation/escrow, endpoint selection, authorization, command, observation and confirmation.

### PASS — Information

Correctly treats scouting as information acquisition with freshness, not merely movement.

### PASS — Threat

Correctly separates threat-blocked from generic task failure and does not invent a universal evacuation manager.

### PASS — Verification/recovery

Correctly requires typed failure causes, bounded retries, reselect/replan behavior and evidence-based state transitions.

---

# 6. Qualification gates

The manual's six-gate model is accepted:

```text
G0 Source Integrity
G1 Static
G2 ABI
G3 Dynamic
G4 Stress
G5 Integration
G6 Long-Horizon
```

Important interpretation: the **manual itself** passes the engineering-documentation gate. The AEGIS runtime does not thereby become G3/G4/G5/G6 qualified.

Current project truth remains:

```text
DOCUMENTATION          → QUALIFIED
ARCHITECTURE           → QUALIFIED FOR IMPLEMENTATION
STATIC MODULES         → PARTIALLY QUALIFIED
TARGET ABI             → PARTIALLY QUALIFIED
CIVILIZATION SUBSTRATE → INCOMPLETE
DYNAMIC SYSTEM         → NOT QUALIFIED
STRESS                 → NOT QUALIFIED
LONG HORIZON           → NOT QUALIFIED
```

---

# 7. Mandatory remaining runtime questions

These remain intentionally open:

- exact rule-pass boundary;
- universal same-pass goal visibility;
- universal same-pass strategic-number visibility;
- command side-effect visibility within the same evaluation context;
- exact backward-jump scheduling;
- exact instruction/rule budget;
- exact re-entry/quiescence behavior;
- object-state refresh timing after commands;
- census/state refresh latency;
- timer/jump/rule-traversal interaction.

No critical AEGIS invariant may depend on these until target-build probes qualify them.

---

# 8. First vertical slice qualification target

The manual's first vertical slice is accepted as the correct implementation target:

```text
VILLAGER DEMAND
 → HOUSING
 → CIVILIZATION CENSUS
 → WORKER TARGETS
 → FOOD / WOOD DEMAND
 → SOURCE + DROPSITE SERVICEABILITY
 → WORKER SELECTION
 → TASK COMMAND
 → ENGINE OBSERVATION
 → PRODUCTIVITY MEASUREMENT
 → FAILURE / RECOVERY
```

This slice exercises the critical substrate contracts without prematurely requiring a complete military system.

---

# 9. Hard prohibitions accepted as binding

The following are now project doctrine:

- Promisory never becomes an AEGIS runtime dependency.
- External documentation never outranks target-build evidence.
- A building count never proves operational capability.
- Command issuance never proves success.
- `object-data-tasks-count` is never treated as universal capacity.
- Worker role is never treated as immutable identity.
- Food is never modeled as one homogeneous source.
- Threat is never silently collapsed into task failure.
- Logical reservation is never called engine escrow without proof.
- Unqualified same-pass visibility is never used as a critical invariant.
- Static qualification is never called runtime qualification.
- Negative findings are preserved.
- Runtime backups are not substituted for project/Git history.

---

# 10. Final verdict

**QUALIFIED AS THE GO-TO ENGINEERING MANUAL.**

The manual is sufficiently evidence-disciplined, architecturally coherent, and explicit about remaining uncertainty to control forward implementation.

It is not a claim that AEGIS itself is runtime-qualified. It is the controlling specification for getting AEGIS there.

The next engineering action is therefore implementation/qualification, not another broad research phase:

1. run the target-build ABI probes;
2. build Civilization State;
3. implement villager production + housing lifecycle;
4. implement worker allocation;
5. implement source/dropsite serviceability;
6. implement food/wood tasking;
7. implement verification/recovery;
8. adversarially qualify the civilian vertical slice.

**Qualification status:** GO.
