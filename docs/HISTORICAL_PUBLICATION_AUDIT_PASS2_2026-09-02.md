# Historical Publication Audit — Pass 2 — 2026-09-02

## Status

**IN PROGRESS — NOT CERTIFIED CLEAN**

This pass extends the repository-wide publication audit by re-querying GitHub's live public repository state after the branch-remediation work. It is an evidence update, not a history purge.

## Scope

Target repository: `justhop90-bot/AiByz`

Audit target:

- current default branch reference;
- known historically exposed commit;
- known restricted path families;
- branch remediation state;
- pull-request state;
- distinction between current-tree cleanliness and historical object accessibility.

This pass deliberately does not republish the contents of restricted historical files.

## 1. Current repository identity

GitHub currently reports:

- repository: `justhop90-bot/AiByz`
- visibility: public
- default branch: `main`
- current `main` ref observed during this pass: `65c27133a15ebbf37619885a2781ce025d330b89`

The repository remains publicly visible. Public visibility does not itself establish redistribution rights for third-party material.

## 2. Historical commit remains addressable

The previously identified historical commit remains directly resolvable by SHA:

`46bd0076b790bd141f07343b8a39e4284d26cfcb`

GitHub resolves that commit and reports its tree as:

`e8a038ba152cc1a163101c9e3f9da2e20bf70e8c`

The historical tree still contains the former `ADPromisory` path family. The returned tree evidence includes multiple `.per` source files and other source-derived material. The historical tree also contains a `Microsoft.Services.Store.winmd` binary and other restricted-path candidates.

**Conclusion:** current deletion/removal from active trees has not constituted historical eradication.

## 3. Pull-request state

PR #2 is now closed and unmerged. Its current head is the sanitized baseline commit `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`.

PR #7 is closed and merged. Its purpose explicitly included carrying the public-tree cleanup of former `ADPromisory`, `AiBuilder`, and `ByzantineWarCouncil` material into `main`.

The present PR state therefore does not provide evidence that the old source tree is still exposed through the active head of PR #2 or through the merged PR #7 head. It does **not** prove that GitHub's historical object/cache/PR infrastructure has expunged all old objects.

## 4. Branch-remediation observation

The known legacy harness branches previously identified as pointing at the old material were moved to the sanitized baseline. A current branch enumeration confirms that the named harness branches resolve to the sanitized baseline rather than the historical source-tree commit.

However, the branch list alone cannot prove that no historical object remains reachable through every possible server-side reference, fork, cache, or other GitHub-managed storage boundary.

## 5. Evidence interpretation

This pass establishes three distinct states:

### A. CURRENT-TREE STATE

**Substantially remediated within the previously audited classes.**

The problematic source trees are not being treated as current project files.

### B. ACTIVE-REF STATE

**Known legacy branches remediated.**

The previously identified harness branches were moved away from the tainted historical head.

### C. HISTORICAL OBJECT STATE

**NOT CLEAN.**

The old commit and its historical tree remain directly addressable by SHA. Therefore the repository cannot yet be certified as historically eradicated.

## 6. Why this distinction matters

A Git history rewrite is different from deleting files in a later commit. GitHub documents that removing a file from the working tree does not remove it from Git history. GitHub further documents that historical material can remain accessible through commits, forks, clones, pull requests, and cached views until the applicable references/storage are dealt with.

Accordingly, the correct engineering state is:

`CURRENT TREE CLEANER -> KNOWN ACTIVE REFS REMEDIATED -> HISTORICAL OBJECTS STILL OBSERVABLE -> CERTIFICATION WITHHELD`

## 7. Safety disposition

No destructive history operation was performed in this pass.

No historical source file was reintroduced into the current repository.

No executable or binary historical artifact was copied into this report.

Only commit/tree identifiers, path-family descriptions, state classifications, and minimum necessary audit facts are retained here.

## 8. Remaining remediation requirement

To achieve historical eradication rather than merely current-tree remediation, the project still requires an authenticated full-history workflow capable of:

1. obtaining a fresh mirror of all relevant refs;
2. rewriting all affected history with a controlled path/blob policy;
3. preserving a pre-rewrite forensic manifest outside the rewritten public history;
4. verifying the rewritten repository locally before publication;
5. force-updating the appropriate writable refs;
6. verifying branches, tags, PR references, and other GitHub-managed references;
7. obtaining GitHub-side assistance where necessary for cached views or server-side references that cannot be removed through normal repository operations;
8. checking forks/repository-network exposure to the extent visible and authorized;
9. performing a fresh-clone post-remediation audit;
10. issuing certification only if the evidence supports it.

## 9. Certification rule

This document does **not** certify the repository as historically clean, legally cleared, or completely purged.

The correct status remains:

**CURRENT TREE: REMEDIATED WITHIN AUDITED CLASSES**

**KNOWN ACTIVE LEGACY BRANCHES: REMEDIATED**

**HISTORICAL SHA ACCESS: CONFIRMED**

**HISTORICAL ERADICATION: NOT COMPLETE**

**PUBLICATION CERTIFICATION: WITHHELD**

## 10. Re-entry point

The next engineering action is not another blind deletion pass. It is construction of the complete historical remediation manifest and an authenticated disposable mirror suitable for `git-filter-repo` or an equivalent controlled rewrite.

The rewrite must be treated as a destructive publication operation with rollback, provenance, pre/post object inventories, and independent verification.
