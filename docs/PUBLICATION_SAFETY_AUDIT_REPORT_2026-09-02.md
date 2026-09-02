# PUBLICATION SAFETY AUDIT REPORT — 2026-09-02

## Executive decision

**STATUS: NOT CERTIFIED COMPLIANT.**

The current public trees were materially cleaned, but the repository's historical Git object graph still contains previously published source-derived material. The audit therefore does not certify the repository as fully compliant with the project's publication standard until historical remediation is completed and independently verified.

This report is deliberately conservative. A failed inspection, inaccessible object, or historical persistence condition is not converted into a claim of absence.

## 1. Audit scope

The audit covered the public `AiByz` repository, its enumerated branches and pull-request refs, current trees, reachable Git objects, historical path/object evidence, and repository metadata.

A local mirror was created solely for authorized audit analysis. The mirror was not used to execute repository artifacts.

Initial repository snapshot contained 73 Git refs, including branch heads and pull-request refs. The object database contained 736 reachable object names and 183 unique reachable blobs totaling approximately 6.06 MB at the initial audit point.

## 2. Current-tree result

The current `main` tree contains 81 files.

Current-tree checks found:

- no current `ADPromisory/` path;
- no current `AiBuilder/` path;
- no current `ByzantineWarCouncil.per`;
- no current `ByzantineWarCouncil.ai`;
- no current `.exe`, `.dll`, `.winmd`, `.aoe2record`, `.zip`, `.7z`, or `.bin` path detected by the filename audit;
- no current email-address matches in the automated scan;
- no current credential-assignment patterns tested by the scanner;
- no current Windows installation paths after the public-path remediation pass.

The current tree is therefore substantially cleaner than the historical repository state.

## 3. Historical exposure finding

The audit discovered that historical public refs had exposed a source-derived tree containing 67 files, including 57 restricted-path candidates:

- complete `ADPromisory/` source tree;
- complete `AiBuilder/` source tree;
- `ByzantineWarCouncil.per`;
- `ByzantineWarCouncil.ai`;
- `ADPromisory/Microsoft.Services.Store.winmd`;
- `ADPromisory/PowerShell Installer.exe`.

The two binary artifacts were byte-classified locally as binary objects. Their presence is inconsistent with the project's conservative P3/P6 publication controls absent an independently established redistribution basis.

The historical source tree was associated with commit `46bd0076b790bd141f07343b8a39e4284d26cfcb`; the pull-request merge ref also exposed the same source tree before remediation.

## 4. Branch exposure remediation

Nine branch heads that pointed directly to the exposed source-tree commit were force-moved to the current safe engineering baseline `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`:

- `aegis/harness`
- `aegis/harness2`
- `aegis/harness3`
- `aegis/harness4`
- `aegis/research-harness`
- `aegis/research-harness-final`
- `aegis/research-harness-v2`
- `aegis/research-harness-v3`
- `aegis/sprint-0-foundation`

Pull request #2 was closed after its exposed head was moved to the safe baseline. The stale `refs/pull/2/merge` ref disappeared on the subsequent remote fetch. This is branch/ref remediation, not historical object erasure.

## 5. Historical Git-object finding

Historical source-derived blobs remain reachable through repository history even though no current public ref points directly to the old source-tree commit.

The audit identified historical path families including:

- `ADPromisory/`;
- `AiBuilder/`;
- `ByzantineWarCouncil.*`;
- the associated binary artifacts.

At the initial complete-object scan, 183 unique reachable blobs were present. After branch-tip remediation, the old source objects remain represented in reachable historical ancestry from other public histories.

The audit also identified 47 unique historical commits touching `ADPromisory`, 10 touching `AiBuilder`, and 3 touching the War Council paths.

Therefore, **current-tree cleanup is not sufficient**.

## 6. Direct historical accessibility

After branch remediation, GitHub still resolved the historical commit:

`46bd0076b790bd141f07343b8a39e4284d26cfcb`

This demonstrates that historical object availability cannot be inferred solely from current branch tips.

The repository is consequently **not yet certified clean of historical exposure**.

## 7. Local-path/privacy finding

The current public tree previously exposed the exact local installation path of the controlled game executable. This was unnecessary disclosure of local environment information.

The affected public Layer 1 records were remediated to use `[LOCAL_AOE2DE_INSTALL]\AoE2DE_s.exe` while retaining version, size, and SHA-256 as the build identity.

A subsequent current-tree scan found no remaining Windows-path matches.

## 8. Automated byte/content scan

The audit read every blob reachable through the enumerated local Git refs as raw bytes and computed cryptographic identities during analysis. It screened the complete blob contents for selected classes of sensitive or restricted material, including:

- historical source-path identifiers;
- executable/DLL/WinMD/replay/archive filename indicators;
- common credential/secret markers;
- private-key markers;
- GitHub token patterns;
- AWS-style access-key markers;
- local Windows paths;
- email addresses;
- IPv4 address patterns.

The scan found no tested secret-token patterns in the current public tree. Historical source blobs and local/private-path indicators were found in historical material as documented above.

This scan is a screening control, not proof that no undiscovered sensitive material exists. GitHub's own secret-scanning documentation describes pattern-based detection and its limitations; the project therefore retains human review and publication classification as independent gates.

## 9. Repository metadata finding

The repository is public and currently reports no repository-level license. GitHub's documentation states that absence of a license does not grant broad redistribution rights; default copyright applies to the repository's own source absent a license, and content not created or owned by the poster requires an appropriate basis for posting.

The repository also permits forking. Public exposure must therefore be treated as potentially replicable.

## 10. Evidence versus publication

The audit found no basis for treating the mere presence of technically accurate native findings as automatic publication permission.

In particular, the following remain governed material classes:

- executable-derived strings and signatures;
- disassembly/decompiler output;
- addresses and native structural details;
- replay-derived data;
- historical source excerpts;
- third-party reference material.

Each requires independent evidence and publication review.

## 11. Required historical remediation

The repository requires a controlled history-rewrite operation if the engineering objective is to remove the identified source-derived artifacts from the repository's historical object graph.

The appropriate operation is a fresh authenticated clone/mirror, followed by a carefully reviewed `git-filter-repo` rewrite over the complete relevant ref set, removal of the identified restricted paths, exhaustive post-rewrite verification, and coordinated update of public refs.

GitHub documents that history rewriting has significant side effects and that force-pushing rewritten history does not by itself guarantee removal from forks, clones, cached views, or pull-request references. For sensitive data, GitHub provides additional support/remediation procedures.

This audit did **not** perform that destructive history rewrite because the available local environment has no authenticated GitHub CLI session and the available connector does not expose the required complete history-rewrite operation. Guessing at credentials or circumventing that boundary would violate this project's authorization standard.

## 12. Required post-rewrite verification

After an authenticated history rewrite, the project must verify from a fresh clone/mirror:

1. all intended public branch/tag refs point to rewritten history;
2. prohibited paths no longer exist in any rewritten tree;
3. prohibited blobs are absent from the rewritten reachable object graph;
4. the identified old commits are no longer reachable through public refs;
5. pull-request refs and releases have been assessed;
6. current-tree and byte/content scans pass again;
7. no new sensitive material was introduced during remediation;
8. repository documentation accurately describes the resulting history state.

Do not certify success from the force-push operation alone.

## 13. Security hardening recommendation

GitHub documents secret scanning and push protection as controls for preventing future credential exposure. The project should enable and verify the applicable repository security controls before future publication work, particularly push protection and secret scanning, subject to the repository/account features actually available.

These controls are supplementary. They do not replace provenance, rights, evidence, or minimum-disclosure review.

## 14. Certification vocabulary

The following terms are now controlled:

- **CURRENT-TREE CLEAN:** no identified prohibited artifacts in the inspected current tree.
- **HISTORICALLY EXPOSED:** prohibited/restricted material existed in prior public repository state.
- **HISTORY REMEDIATED:** rewritten history has passed fresh-object verification.
- **PUBLICATION COMPLIANT:** evidence, authorization, rights, safety, minimum disclosure, and auditability gates all pass for the inspected scope.
- **FULLY AUDITED:** only permitted when the claimed scope and all material inspection boundaries have actually been covered.

The present repository status is:

**CURRENT-TREE CLEAN: YES, within the tested classes.**  
**HISTORICALLY EXPOSED: YES.**  
**HISTORY REMEDIATED: NO.**  
**PUBLICATION COMPLIANT: NO — historical remediation remains outstanding.**  
**FULLY AUDITED: NO — historical/server-side replication boundaries remain.**

## 15. Final engineering decision

The audit did exactly what the standard requires: it found a problem rather than hiding it.

The correct response is not to weaken the standard. It is to preserve the evidence, remediate the exposure through an authorized history-rewrite workflow, verify the result independently, and only then certify the repository.

> **Do not declare the repository clean while the historical object graph still contains material we have decided should not be public.**
