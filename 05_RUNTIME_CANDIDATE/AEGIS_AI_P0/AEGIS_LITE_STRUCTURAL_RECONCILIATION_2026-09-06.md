# AEGIS-Lite Structural Reconciliation — 2026-09-06

**Status:** P0 structural reconciliation completed; runtime generation qualification remains open  
**Target:** AoE2DE `101.103.48987.0`, Steam BuildID `24094652`  
**Repository:** `justhop90-bot/AiByz`  
**Branch:** `aegis/external-harness-v1-2026-09-05`  
**Reconciled HEAD:** `447b086bbbe9915988c6f13f3428126053625d0b`

## Executive result

The AEGIS-Lite source package has been structurally reconciled without adding native Execution.

The prior candidate had two copies of the World Model and two Carpenter source artifacts. The reconciliation establishes:

- **Architect / `AEGIS-BYZ.per`** owns World Model meaning, state, qualification, evidence state, and generation semantics.
- **Engine Carpenter / `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`** is the sole loaded native sensor adapter. It acquires native facts and writes into Architect-owned World Model goals.
- The superseded unloaded `AegisProm/Aegis-carpenter.per` artifact was removed after its source hash was recorded. Its Git history remains the preservation record.
- The generation probe remains separate instrumentation and is not part of the production eight-file load closure.

The exact pre-reconciliation machine-tested P2 artifact was preserved in Git history before modification. Its previously recorded SHA-256 was:

`667F7C6F36A7537606DD087E52DAC7147DE34F7B927852E49D6F2CF0088629A`

The reconciled P2 source is a new artifact and must not be described as the exact pre-reconciliation file.

## Final eight-file load closure

```text
AEGIS-BYZ.per
├── AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per
├── AegisProm/Aegis-belief.per
├── AegisProm/Aegis-situation.per
├── AegisProm/Aegis-objectives.per
├── AegisProm/Aegis-planning.per
├── AegisProm/Aegis-decision.per
└── AegisProm/Aegis-commitment.per
```

The generation probe is intentionally not loaded.

## Final recursive audit

A fresh target-machine run of `tools/aegis_abi_audit_v2.py` against reconciled HEAD `447b086bbbe9915988c6f13f3428126053625d0b` returned:

| Metric | Result |
|---|---:|
| Closure files | 8 |
| Declaration rows | 129 |
| Numeric declarations | 129 |
| Unique symbols | 129 |
| Resolved goal operands | 237 |
| Resolved high-goal operands | 0 |
| Duplicate declarations | **0** |

The equality of declaration rows and unique symbols is the direct audit indication that the prior 27 duplicate declarations have been removed from the loaded closure.

## Ownership decision

### World Model

**Authoritative owner: `AEGIS-BYZ.per`.**

The Architect retains:

- World Model goal declarations 300–318;
- timer identity and cadence ownership;
- bootstrap state envelope;
- qualification transition;
- evidence-level transition;
- cavalry-age observation retention;
- enemy-presence interpretation;
- downstream semantic boundary.

The Architect no longer performs native sensor acquisition itself. This prevents two independent observation implementations from mutating the same state envelope.

### Engine Carpenter

**Authoritative loaded owner: `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`.**

The Carpenter retains:

- native sensor expression;
- native fact acquisition into Architect-owned goals;
- Carpenter heartbeat/runtime markers;
- bounded diagnostics.

The Carpenter does not declare World Model state, qualify World Model evidence, select objectives, reserve resources, or issue commands.

### Superseded standalone Carpenter

`AegisProm/Aegis-carpenter.per` was an unloaded duplicate/alternate Carpenter implementation. It was removed from the active branch during reconciliation rather than left as an ambiguous second implementation.

Recorded source SHA-256 before removal:

`27A97A7C3C2195E1F83E6142DFF67F7977140D3D0881662D91A470B263F5A2BD`

The removal is reversible through Git history; it is not an unrecorded destruction of evidence.

## Why this ownership model is correct

The architecture separates **meaning** from **native expression**:

```text
Architect
  owns WHAT the World Model means
          ↓
Carpenter
  owns HOW native engine primitives populate it
          ↓
World Model state
  is consumed by downstream semantic layers
```

This is materially cleaner than either of the two rejected arrangements:

1. two World Model owners mutating the same goals; or
2. Carpenter owning the semantic World Model itself.

The Carpenter's native adapter is therefore an implementation mechanism, not the semantic authority for the resulting state.

## Remaining semantic limitations

The reconciliation does **not** upgrade sensor semantics to PROVEN.

Current observation remains:

- `aegis-knight = 38`: concrete Knight-unit probe, not a qualified `knight-line` observation;
- `up-get-fact-max any-enemy unit-type-count aegis-knight`: current cavalry signal is not established as a total across all enemies;
- `aegis-wm-observed-at = 1`: observation marker, not a timestamp;
- `aegis-wm-time`: sampled game-time channel, whose exact semantic units remain separately qualified;
- `aegis-wm-valid = 1`: architectural qualification transition, not independent corroboration of sensor truth.

The public AoE2 AI scripting reference confirms `up-get-fact`, `up-get-fact-max`, and the native AI scripting model, but documentation does not by itself prove the target-build semantics of these specific AEGIS probes. citeturn0search1turn0search2

The scripting data-limit reference also confirms the relevant broad limits: 10,000 rules, 32 elements per rule in DE, goals 1–16,000, timers 1–50, and nested loads up to 10 files. These are background constraints, not proof of AEGIS runtime behavior. citeturn0search3

## Provenance binding

The reconciled eight-file source closure has deterministic per-file hashes and the closure manifest hash:

`6F9533CFD5DF3B3BD9C0AE95AA16A6DEBA153AABDDA0814E8AED00C3076EA4EC`

Target executable SHA-256:

`6378CA6F1BFD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

The full source/hash record is stored in:

`AEGIS_LITE_RECONCILED_SOURCE_HASH_2026-09-06.md`

## Runtime state after reconciliation

No reconciled package has yet been promoted to PROVEN runtime semantics.

The target machine currently has no active `AEGIS-P0-Entry` local mod package; the previous disposable package was removed. This reconciliation therefore has not silently overwritten the user's machine package.

The next runtime operation is deliberately controlled package installation and launch using the reconciled eight-file closure, followed by generation propagation qualification.

## Required generation experiment

The next gate is:

```text
reconciled source
    ↓
reconciled eight-file closure
    ↓
closure hash
    ↓
exact AoE2 executable hash
    ↓
engine load
    ↓
generation N
    ↓
generation N+1
    ↓
World Model → Belief → Situation → Objectives → Planning → Decision → Commitment
    ↓
stale-generation rejection
    ↓
verdict
```

The UNKNOWN/zero/absence experiment remains separate. A missing or zero sensor value must not be confused with stale-generation rejection.

## Gate disposition

- **P0-STRUCT-001 — CLOSED:** duplicate World Model implementation removed from active closure.
- **P0-STRUCT-002 — CLOSED:** one loaded Carpenter owner established; superseded unloaded alternate removed.
- **P0-AUDIT-001 — CLOSED:** recursive eight-file load closure verified on target machine.
- **P0-AUDIT-002 — CLOSED:** stale one-file audit snapshot superseded by reconciled closure record.
- **P0-RUNTIME-GEN-001 — OPEN:** generation N → N+1 propagation remains unqualified.
- **P0-RUNTIME-STALE-001 — OPEN:** stale-generation rejection remains unqualified.
- **P0-RUNTIME-SENSOR-001 — OPEN:** sensor semantic qualification remains separate.

**Gate:** native Execution adapters remain blocked until generation propagation and stale-generation qualification are complete.
