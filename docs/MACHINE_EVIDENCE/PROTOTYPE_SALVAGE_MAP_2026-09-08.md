# AEGIS / ByzBot — Prototype Salvage Map

**Date:** 2026-09-08
**Machine source:** `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\AegisProm`
**Evidence class:** target-machine static evidence
**Runtime:** not performed
**GitHub comparison base:** `c3bd849f0cfaf9a18103d5a0064fdab47fda3d4f`

## Executive finding

The directory is a real, substantial AEGIS prototype corpus, but it is **not a coherent final package**. It contains at least three distinct generations/layers: final-named architectural modules, v0 experimental services, and a 36,141-line stock-derived civilization substrate. The machine corpus is also materially divergent from the current GitHub `implementation/` tree.

The correct treatment is salvage, not promotion. No machine file is authoritative merely because it has `final` in its filename or lives under the AoE2DE AI directory.

## Machine inventory

The directory contains **58 files totaling 2,510,440 bytes**.

There are **33 active-looking `.per` files at the directory root** plus 24 research/backup documents under `RESEARCH-QUALIFICATIONS` (the remaining root population is accounted for by the complete recursive inventory taken during this pass).

Key files include:

- `AEGIS-foundation.per` — 208 lines; 155 `defconst` declarations; one rule.
- `Aegis-belief-final.per` — 55 lines; 5 rules.
- `Aegis-situation-final.per` — 75 lines; 6 rules.
- `Aegis-objectives-final.per` — 73 lines; 6 rules.
- `Aegis-planning-final.per` — 79 lines; 7 rules.
- `Aegis-decision-final.per` — 31 lines; 3 rules.
- `Aegis-commitment-final.per` — 38 lines; 4 rules.
- `Aegis-economy-final.per` — 66 lines; 5 rules.
- `Aegis-military-final.per` — 59 lines; 5 rules.
- `Aegis-execution-final.per` — 104 lines; 8 rules.
- `Aegis-verification-final.per` — 89 lines; 7 rules.
- `Aegis-recovery-final.per` — 67 lines; 4 rules.
- `AEGIS-operations-final.per` — 119 lines; 9 rules.
- `AEGIS-Carpenter-final.per` — 31 lines; 1 rule.

The v0 service layer includes civilian lifecycle, economic demand/arbitration, source/dropsite serviceability, villager production, and multiple worker-role/task/recovery/qualification modules.

## Major substrate files

`AEGIS-BYZ-FINAL-CIVOS.per` and `AEGIS-civilization-os.per` are both 36,141 lines and approximately 1.17 MB.

They are **not byte-identical**. SHA-256:

- `AEGIS-BYZ-FINAL-CIVOS.per`: `A593B33717D4E862E496FD1EF98694E5F862C974A3FEE368BBD1A3B66BBE2596`
- `AEGIS-civilization-os.per`: `1A86862B8C4FFFB8AA98CD387552F7E109B0847D893D079AC5F856693A8FE4A9`

A line comparison found only **10 difference records**, corresponding to five effective source-line changes: identity comments and load-path/load-target changes. This strongly indicates a rehosted/retargeted copy rather than two independently developed 36k-line implementations. It must nevertheless be preserved as two distinct artifacts until provenance is formally resolved.

## Load-closure defects found on the machine

The machine's `AEGIS-BYZ-FINAL-CIVOS.per` contains loads for:

- `AegisProm\\AEGIS-stock-defaultConstants` — present.
- `AegisProm\\AEGIS-stock-finalingConstants` — **missing**.
- `AegisProm\\AEGIS-stock-finaling` — **missing**.

`AEGIS-civilization-os.per` contains:

- `AegisProm\\AEGIS-stock-defaultConstants` — present.
- `AegisProm\\AEGIS-stock-finalingConstants` — **missing**.
- `Promisory\\finaling` — present.

The `Stock Aegis\AEGIS-BYZ.per` root is also stale relative to the present `AegisProm` directory. Its seven AEGIS module loads resolve to **missing files**, including `AEGIS-BYZ-Engine-Carpenter-P2`, `Aegis-belief`, `Aegis-situation`, `Aegis-objectives`, `Aegis-planning`, `Aegis-decision`, and `Aegis-commitment`. The current machine directory instead contains renamed `-final` variants and `AEGIS-Carpenter-final.per`.

Therefore the machine currently contains **prototype package drift**: roots and module names from different generations do not form one mechanically closed package.

## GitHub divergence

The current local clone at `C:\Temp\AiByz-main-current` is at `c3bd849f0cfaf9a18103d5a0064fdab47fda3d4f`.

Every overlapping v0 implementation file checked is byte-different from its machine counterpart. The repository also contains `AEGIS-integration-candidate-v0.per`, which is **absent from the machine AegisProm directory**.

Conversely, the machine contains the final-named architecture files listed above, which are **not present under the repository's current `implementation/` tree**. For example, `implementation/Aegis-execution-final.per` does not exist on the current GitHub branch.

This means the machine and GitHub are currently **different development states**, not two copies of one build.

## Initial salvage classification

### KEEP / EVIDENCE

- Both 36,141-line civilization substrate copies, pending provenance resolution.
- All `RESEARCH-QUALIFICATIONS` artifacts; they document design/qualification history.
- Final-named architecture modules as implementation candidates, not verified code.

### EXTRACT / REWRITE

- `AEGIS-foundation.per`: useful state-envelope and protocol design, but its numeric allocations require the final typed collision audit before promotion.
- Belief → Situation → Objective → Planning → Decision → Commitment chain: strong architectural skeleton; implementation must be reconciled with the final ABI and rule-order/temporal contracts.
- Execution/Verification/Recovery: useful transaction-state model, but evidence transitions and retry semantics remain implementation candidates.
- v0 civilian/economic/worker modules: salvage contracts and algorithms, rewrite against current ABI and parser findings.

### RETIRE FROM FINAL PACKAGE

- Broken/stale roots whose load closures do not resolve.
- Duplicate 36k-line copies as competing sources of truth; preserve both as evidence, select one provenance path only after comparison.
- Any backup file used as executable source.

## Important ABI warning

`AEGIS-foundation.per` currently allocates many AEGIS state channels in the 300–400 range and includes `aegis-wm-timer 40`. These values are **prototype allocations**, not cleared final ABI. The final package must regenerate its numeric map from the complete typed inventory and collision record rather than copying these constants.

## Next operation

The next static operation is a **contract/ABI reconciliation pass over the final-named machine modules**. For each module we will extract state reads/writes, command/fact surface, dependencies, upstream/downstream generation contracts, numeric allocations, and unsupported primitives. We will then compare that graph against the current GitHub contracts and the target-build stock ABI.

No runtime qualification is implied by this map.
