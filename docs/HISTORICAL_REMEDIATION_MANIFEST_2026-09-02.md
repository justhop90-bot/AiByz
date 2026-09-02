# HISTORICAL REMEDIATION MANIFEST — 2026-09-02

## Status

**CONTROLLED / NOT A CERTIFICATION**

This manifest defines the historical Git material that must be removed from the public repository history if the project elects to perform complete historical remediation. It deliberately records metadata, path families, object identities, and verification requirements rather than reproducing restricted source material.

## 1. Objective

The objective is historical eradication of repository content classified as restricted under the project's publication and rights controls, while preserving a non-reconstructive forensic record sufficient to verify what was removed.

Current-tree cleanup is not the objective of this document. Current-tree cleanup has already been separately audited.

## 2. Known historical anchor

The primary historically exposed commit established by live GitHub inspection is:

`46bd0076b790bd141f07343b8a39e4284d26cfcb`

Its tree is:

`e8a038ba152cc1a163101c9e3f9da2e20bf70e8c`

The historical tree is demonstrably accessible by Git object identity even though current branch remediation moved the known legacy branch heads away from it.

## 3. Restricted path families

The remediation scope includes, at minimum:

- `ADPromisory/**`
- `AiBuilder/**`
- `ByzantineWarCouncil.per`
- `ByzantineWarCouncil.ai`
- `ADPromisory/Microsoft.Services.Store.winmd`
- `ADPromisory/PowerShell Installer.exe`

The `ADPromisory` tree is a source-derived artifact family. The historical tree also contains a broad historical HD/AI source corpus adjacent to that family; individual files must be classified during the rewrite preparation rather than assuming that every historical file has identical rights or publication status.

## 4. Known binary object identities

The following binary objects were directly identified in the exposed historical tree:

| Historical path | Git blob | Size | Disposition |
|---|---|---:|---|
| `Microsoft.Services.Store.winmd` | `e9b62b481aecb4cd7ffbd70dbf679114d9695ddb` | 5,120 bytes | REMOVE |
| `PowerShell Installer.exe` | `773eb9a3b257bc997aac6f9c215ad585781b5942` | 815,136 bytes | REMOVE |

These are recorded by identity only. Their contents are intentionally not reproduced in the public research record.

## 5. Known source-object identities

Representative source blobs directly observed in the exposed `ADPromisory` subtree include:

- `ADByzantineAfterActionMemoryDirector.per` — `4c2e0748a29c9332f923e25ea8f50fe595d0abf6` — 14,599 bytes
- `ADByzantineBattlefieldCommander.per` — `46bec54d27c7980cad873d6709fa7f046f8a7f47` — 29,242 bytes
- `ADByzantineCivilArchitectDirector.per` — `0738244db05d8e06a9ebb2c2d3b8fc216c40c245` — 14,944 bytes
- `ADByzantineCommandNetwork.per` — `e9c05bd9ab07b9bf7ad9d77c376ca2c52ecda2a3` — 10,924 bytes
- `ADByzantineCompatibility.per` — `2c929ddcaa9c29d8fe124257257dda9ec11e740a` — 993 bytes
- `ADByzantineCompositionOptimizer.per` — `094f370aba824b925b9c758aeac1779b4e43387e` — 21,519 bytes
- `ADByzantineConstants.per` — `5a9d70a5f2b976adfede83e132caef642b2cefe9` — 12,128 bytes
- `ADByzantineEconomicWarDirector.per` — `19953f8a2caaa485b393b761c2816c959518e8ab` — 14,163 bytes
- `ADByzantineExecutionBridge.per` — `3a645202207bec494fb010ba6a5a42791e572baf` — 28,143 bytes
- `ADByzantineForcePlanner.per` — `5ba9b7865b3f1098e269259961261dd928fe555a` — 20,217 bytes
- `ADByzantineIntelligence.per` — `d11f10c970689264fa8a88552a55f3528130c0d5` — 19,243 bytes
- `ADByzantineMarketWarfareOfficer.per` — `c0fc52b083ded7fa88fbe34d581e6fdd31ca10c5` — 14,491 bytes
- `ADByzantineMemory.per` — `e2f857f8a2aefeacff2f14509c2bd09311359acf` — 11,651 bytes
- `ADByzantineMicroTacticalDirector.per` — `60865ed841095337ce6fde656604d8d4f42dc0a9` — 19,556 bytes
- `ADByzantineNavalWarDirector.per` — `b21f6b2270e6cb4bdea03358feec79566a7079ac` — 18,769 bytes
- `ADByzantineProductionDirector.per` — `bf6f85fccf393703f89814beabd4d9ab6dbd08aa` — 29,367 bytes
- `ADByzantineReasoning.per` — `4fef10820f05bd2259f02e61d1cae13d8aed1b60` — 13,206 bytes
- `ADByzantineSiegeConversionDirector.per` — `56990110c19ede3bb3dc238b011fc06d68a295cc` — 20,495 bytes
- `ADByzantineSovereign.per` — `0e6b22515a26930efa35f12eff91a85ad5bd3f15` — 9,249 bytes
- `ADByzantineTechImperialDirector.per` — `5c6547c4dc2b6595d84a143c5fe129b94d755f4c` — 16,082 bytes
- `ADbuildings.per` — `00552518e90dbc464934c91428aa462565353440` — 427,371 bytes
- `ADgatherers.per` — `167942015a0af2a66d5c05f2228d6bad62eef7eb` — 198,654 bytes
- `ImprovementBucketsConst.per` — `b97bf22a44a427172c7fdd1aad95683def9ebcf5` — 134,558 bytes
- `ImprovementBucketsTestConst.per` — `ce986b9db8634afa2d7f1ae9590ad9264f380e8d` — 29,193 bytes

This table is a verified subset of the historical tree, not a claim that these are the only affected objects. The complete rewrite preparation must enumerate the entire target tree recursively and deduplicate by blob identity.

## 6. Historical volume findings

The earlier repository-wide audit established:

- initial snapshot: 73 Git refs;
- initial reachable object names: 736;
- unique reachable blobs: 183;
- initial reachable blob data: approximately 6.06 MB;
- exposed historical source-tree snapshot: 67 files;
- restricted-path candidates in that snapshot: 57;
- historical commits touching `ADPromisory`: 47 unique commits;
- historical commits touching `AiBuilder`: 10 unique commits;
- historical commits touching War Council paths: 3 unique commits.

These numbers are audit observations for the prior snapshot. They are not assumed to be unchanged after subsequent repository mutations. A fresh authenticated mirror is mandatory before the actual rewrite.

## 7. Ref remediation already completed

The known legacy branch heads were moved to safe baseline `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`:

- `aegis/harness`
- `aegis/harness2`
- `aegis/harness3`
- `aegis/harness4`
- `aegis/research-harness`
- `aegis/research-harness-final`
- `aegis/research-harness-v2`
- `aegis/research-harness-v3`
- `aegis/sprint-0-foundation`

PR #2 was closed after its exposed head was remediated. This is containment, not object erasure.

## 8. Why a fresh mirror is mandatory

The repository has continued to change after the initial audit. Therefore the old 73-ref/183-blob inventory cannot be treated as the final rewrite input.

The authenticated rewrite operator must capture:

1. every branch ref;
2. every tag ref;
3. every pull-request ref that is exposed to the authenticated operator;
4. relevant release references;
5. complete commit ancestry;
6. complete tree/path inventory;
7. blob identities and sizes;
8. rename/move relationships;
9. merge topology;
10. current repository metadata.

The resulting manifest becomes the authoritative rewrite input for that operation.

## 9. Rewrite rule

The rewrite must remove the target path families from every rewritten tree, not merely delete them from current tips.

The rewrite operator must not perform broad content substitution that could silently alter unrelated research material. Path-targeted removal is preferred, followed by object-graph verification.

If an affected file has been renamed outside the known path family, the rename must be included in scope based on historical blob identity and provenance rather than filename alone.

## 10. Verification rule

After rewriting, perform a fresh clone/mirror and verify all of the following:

- no prohibited target path exists in any rewritten tree;
- no prohibited target blob identity remains reachable;
- no rewritten commit retains the exposed historical tree;
- old anchor commit `46bd0076b790bd141f07343b8a39e4284d26cfcb` is not reachable through the intended public refs;
- affected pull-request refs have been assessed;
- releases/tags have been assessed;
- current-tree publication scans pass;
- path, byte-pattern, secret-pattern, local-path, and binary filename scans pass;
- repository documentation matches the actual post-rewrite state.

A second independent mirror audit should be performed before certification.

## 11. Non-goals

This manifest does not:

- reproduce restricted source;
- reproduce executable or WinMD contents;
- establish legal ownership by itself;
- assert that every historically published object is impermissible without classification;
- claim that GitHub's server-side caches, forks, clones, or external mirrors have been erased;
- authorize a destructive history rewrite.

## 12. Authorization boundary

The actual history rewrite is a destructive repository operation. It must be performed only through an authenticated GitHub/Git transport under the repository owner's authorization.

The current available connector can inspect public Git data and manipulate ordinary refs/files, but it is not treated as a substitute for an authenticated full-history rewrite environment.

No credentials will be guessed, solicited unnecessarily, or bypassed. No access-control boundary will be circumvented.

## 13. Decision

**REMEDIATION MANIFEST: ESTABLISHED.**

**HISTORICAL EXPOSURE: CONFIRMED.**

**CURRENT-TREE CONTAINMENT: CONFIRMED WITHIN AUDITED CLASSES.**

**HISTORICAL ERADICATION: NOT PERFORMED.**

**PUBLICATION CERTIFICATION: WITHHELD.**

The next authorized operation is an authenticated fresh mirror followed by complete rewrite preparation and post-rewrite verification. Until that occurs, the old historical object identities remain forensic evidence and must not be re-published as source content.
