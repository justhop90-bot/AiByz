# AEGIS A1 Stock Baseline Reconciliation — 2026-09-06

**Status:** FORENSIC DISCREPANCY IDENTIFIED / STOCK CLOSURE INTACT
**Target executable:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652
**AI root:** C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai

## Finding

The repository's 2026-09-05 A1 snapshot records a 516-file installed AI tree. A fresh workstation enumeration on 2026-09-06 finds 525 files in the same directory. The additional nine files are AEGIS development artifacts:

- AEGIS-BYZ-Architect-P1.ai
- AEGIS-BYZ-Architect-P1.per
- AegisProm/Aegis-belief.per
- AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per
- AegisProm/Aegis-commitment.per
- AegisProm/Aegis-decision.per
- AegisProm/Aegis-objectives.per
- AegisProm/Aegis-planning.per
- AegisProm/Aegis-situation.per

The existing 	estharness/scripts/AEGIS_FTS_CAL_001.fts was already present in the 2026-09-05 516-file snapshot, so it is not part of the nine-file delta.

## Closure result

Running the repository ABI audit against the installed AI (HD version).per entrypoint produced an exact four-file import closure:

1. AI (HD version).per — SHA-256 8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c
2. Promisory/defaultConstants.per — SHA-256 187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad
3. Promisory/finaling.per — SHA-256 95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52
4. Promisory/finalingConstants.per — SHA-256 ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455

The four closure hashes exactly match the 2026-09-05 repository A1 stock manifest. The audit reports 5,259 declaration rows, 1,480 unique symbols, 5,490 resolved goal operands, and zero resolved high-goal operands in the exact four-file closure.

## Contamination boundary

A recursive textual search across the installed AI tree found no AEGIS/AegisProm references in .per, .ai, .json, or .txt files. Therefore the nine newly identified AEGIS artifacts are not established as imported by the stock AI (HD version).per closure.

This is a **tree-level provenance failure**, not a demonstrated stock-closure mutation.

The distinction matters:

- **Installed tree:** NOT currently pristine; contains nine post-snapshot AEGIS artifacts.
- **Stock AI closure:** byte-identical to the 2026-09-05 recorded four-file closure.
- **Stock closure semantics:** not changed by this finding.
- **A1 whole-tree snapshot:** must be reacquired after establishing a truly clean package boundary.

## Evidence hashes of identified AEGIS artifacts

| Path | SHA-256 |
|---|---|
| AEGIS-BYZ-Architect-P1.ai | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| AEGIS-BYZ-Architect-P1.per | 44f324bf25b9231036126a0f72efbb7aeb6eac6b36f69c8a8e27df7571beb2f4 |
| AegisProm/Aegis-belief.per | 27920bd9e9435cfd498d26d7511784fae1c06b14219eadcc570b617d801df5b3 |
| AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per | 1c206c99c92a457e5027aadea6177572c99bae1ee50aaa67195d4ea8757676a0 |
| AegisProm/Aegis-commitment.per | ea0adee699fd61e01c56a98ffc2f97cd465b91bc4882184b6dff9c6810ef2fdd |
| AegisProm/Aegis-decision.per | 2a1e5e5fc4d6f976442a70a07a1cc45791b561000661f295704bcee6819ba43c |
| AegisProm/Aegis-objectives.per | edcba6074ce6a829ba4de04ac2b64127af515f4f5bd12b89d092ef0f7ce3bb4 |
| AegisProm/Aegis-planning.per | 65bc3bd0bf96a99949f683bda5e669e6fd5dd744c7685aed6622dba83de339c |
| AegisProm/Aegis-situation.per | 74cee91c0c8801d4399369ea51e29efea4355d0f78c29528f162edabe0d1f8b7 |

## Engineering disposition

Do not delete these artifacts yet. Preserve them as evidence of the machine/repository divergence. Do not call the installed directory a pristine stock baseline until the extra files are removed or the clean Steam package is independently reacquired and snapshotted.

The correct next operation is to obtain a clean stock package boundary without modifying the evidence currently being used for runtime experiments, then regenerate the A1 manifest and compare the four-file runtime closure plus the full tree.
