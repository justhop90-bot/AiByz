# AiByz / AEGIS — Canonical Repository QC

**Effective:** 2026-09-05
**Canonical branch:** `main`
**Disposition:** PASS — repository authority and current baseline clarified; implementation gates remain closed

## 1. Scope

This QC establishes whether GitHub is a safe, unambiguous starting point for the next engineering phase.

It covers:

- branch/authority topology;
- current front-door documents;
- handoff consistency;
- historical-artifact disposition;
- current target-build identity;
- stock AI package provenance;
- architecture/ABI gates;
- implementation readiness.

## 2. Authority result

`main` is the sole canonical starting branch.

The previous canonical handoff branch `aegis/canonical-handoff-2026-09-05` was merged into `main` at commit `8bdeb43594235980f0ab0d3d90fbace7ad00653a`.

The repository contains many historical branches, including numerous `final`, `canonical`, `handoff`, and `work` variants. These are provenance only. Branch names do not confer authority.

## 3. Front-door result

The canonical front door is now:

`README.md`
→ `CANONICAL_AUTHORITY.md`
→ `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
→ `docs/CANONICAL_QC_2026-09-05.md`
→ `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
→ `docs/REPOSITORY_OPERATING_STANDARD_2026-09-05.md`
→ `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`

Older handoffs/QC records are historical and remain recoverable.

## 4. Current machine/build identity

Authorized workstation evidence establishes:

- target executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam BuildID: `24094652`
- Update: `#180059`

This is the current A1 executable identity.

## 5. Stock AI package disposition

The project owner has restored:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\\_common\\ai`

from Steam and states that it has not been modified after restoration.

**QC disposition: CURRENT STOCK-RUNTIME BASELINE.**

This corrects older repository language that treated the installed tree as necessarily contaminated or unavailable. Names found in the restored tree are not evidence of project modification.

The remaining package gate is documentary/forensic capture: immutable manifest, per-file hashes, entrypoint, recursive import closure, and typed symbol/reference inventory.

## 6. Layer disposition

### Layer 1

89%; frozen for handoff. Broad archaeology is closed. Re-enter only for a specific implementation requirement tied to a recorded closure target.

### Layer 2

Major historical strategy/programmer reconstruction is closed. Targeted evidence work remains permissible when it can alter implementation architecture.

### Layer 3

Active. Symbolic architecture and ABI procedure are defined. Numeric allocation is blocked.

### Layer 4

Blocked until package/build/ABI gates are cleared.

### XS

Outside project scope.

### Scenario loader

Automation/testing route retired.

### CADE

Secondary validation candidate, not primary authority.

## 7. Strategic architecture result

First vertical slice:

`CAVALRY THREAT → CAMEL REQUIREMENT → CAPABILITY/RESOURCE CHECK → PRODUCER SELECTION → COMMIT → EXECUTE → VERIFY → RECOVER/RE-ARBITRATE → REASSESS`

State envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

The architecture correctly keeps strategic intent, runtime control, world postconditions, and strategic success distinct.

## 8. ABI result

**BLOCKED — correctly.**

No numeric goal/SN/flag/timer allocation is authoritative yet.

Required sequence:

`IMMUTABLE STOCK SNAPSHOT → IMPORT CLOSURE → SYMBOL INVENTORY → REFERENCE INVENTORY → CHANNEL OCCUPANCY → WRITER/READER MATRIX → ENGINE/VALIDATOR JOIN → ABI DECISIONS → FREEZE`

Safety rules remain binding:

- parser failure is not absence;
- numeric equality is not identity;
- declaration is not import closure;
- validator behavior is not engine semantics;
- historical source is not current-build proof;
- A5 inference cannot clear an ABI channel;
- no audit step may mutate the stock baseline.

## 9. Historical evidence result

The repository preserves substantial HD/Promisory archaeology and the evidence-edge methodology developed through the latest passes. The historical AI is treated as a capable strategic controller materially below a decent human player, not as a toy ruleset. Claims about individual match outcomes remain separately bounded.

## 10. Cleanup result

The correct cleanup strategy is consolidation, not history destruction.

Keep:

- dated archaeology passes;
- failed investigations that explain decisions;
- superseded handoffs/QC as historical records;
- old commits and branches required for provenance.

Remove from the active workflow:

- stale open PRs that compete with current authority;
- duplicate authority-looking branch names for new work;
- obsolete front-door instructions that contradict the current handoff.

## 11. Current repository standard

Substantive work enters through a work branch and reviewable PR, then merges to `main`. CODEOWNERS and the PR template establish minimum review context.

GitHub's repository guidance recommends protected important branches, pull-request review, code ownership, and security controls for repositories where stability matters. This repository adopts those principles as operating standards.

## 12. Final verdict

**PASS.**

The repository now has a single canonical starting branch, a single current handoff, a single current QC record, an explicit historical disposition model, and a corrected current stock-runtime baseline.

The next engineering action is no longer repository archaeology. It is:

`STOCK AI SNAPSHOT → IMPORT CLOSURE → ABI INVENTORY → ABI CLEARANCE → FIRST .per VERTICAL SLICE`
