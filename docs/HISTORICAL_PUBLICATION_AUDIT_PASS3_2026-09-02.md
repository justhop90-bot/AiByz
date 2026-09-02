# Historical Publication Audit — Pass 3

Date: 2026-09-02
Repository: justhop90-bot/AiByz
Audit status: NOT CERTIFIED

## Purpose

Pass 3 extends the historical-publication audit from object/path exposure into the live repository's ref, pull-request, issue, and release surfaces. The objective is containment verification and identification of any currently reachable secondary exposure surface. This document intentionally records metadata and findings without reproducing restricted historical source material.

## Live ref topology

The live Git refs endpoint returned fewer than 100 refs; the second page was empty. The observed branch inventory contains a large number of AEGIS-named branches, many intentionally converged on sanitized baseline commits. The known legacy harness branches remain redirected to the sanitized baseline `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`.

A notable topology finding is that many handoff/pass-final branches converge on `77404a996a0b0e517992565f9f163b4aa5d2b98a`. This is not itself evidence of restricted content; it is a ref-management complexity and increases the importance of exhaustive ref enumeration during any future history rewrite.

The active `aegis/pass6-operationalization` branch is currently at `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`, confirming that the formerly active research branch is no longer pointing at the historical source-bearing head.

## Pull-request surface

PR #7 is closed and merged. Its purpose explicitly included removal of former ADPromisory, AiBuilder, and ByzantineWarCouncil material from the current tree. Its former head was a research branch that has subsequently been remediated.

PR #6 is open and draft. Its head is `aegis/six-month-handoff`, commit `157d35694d20befbf38529a57e1b539641639c04`, and it is substantially diverged from current main. A direct contents probe for a known former restricted path on that branch returned Not Found, and comparison against current main reports only nine added HANDOFF files. Therefore no current-tree restricted path was demonstrated on the PR head in this pass.

However, PR #6 has a long ancestry and is a public historical surface. It must remain in the history-rewrite verification set even if its current tree is clean. A future rewrite must verify the PR's head, base, commits, merge-base, patch views, and any regenerated GitHub references after rewriting.

## Issues and release surface

The repository currently exposes two open issues. Issue #6 is a draft-style institutional handoff record and does not, from the retrieved metadata, contain the restricted source itself. Issue #1 is an empty `Byzmaster` issue. These surfaces should nevertheless be included in final keyword/path-link review.

The releases endpoint currently returns an empty list. No release asset surface was identified in this pass.

## Privacy / metadata finding

Public Git metadata exposes an author/committer email address in repository commit records. The audit treats this as personal-data exposure under the project's P5 classification. The address is not reproduced here. Before final publication certification, future commit configuration should use an appropriate non-personal GitHub identity where possible, and any decision to rewrite historical author/committer metadata must be handled as an explicit remediation item rather than assumed away.

## Current conclusion

1. No active branch examined in this pass was demonstrated to contain a known restricted path in its current tree.
2. The historical source-bearing commit remains directly addressable and therefore historical eradication is still not established.
3. The repository has no releases according to the live releases endpoint.
4. Open PR #6 is a secondary historical surface that must be included in final rewrite verification even though its current tree probe is clean.
5. The large number of converged AEGIS branches makes ref-complete rewrite verification mandatory.
6. Public commit metadata contains personal author/committer information and remains a separate publication-hygiene item.

## Required next operation

Do not perform a destructive rewrite through the currently available connector. The correct next operation remains an authenticated fresh mirror under the repository owner's control, followed by complete ref enumeration, full-history path/blob classification, controlled rewrite in an isolated mirror, ref recreation, PR/release verification, fresh-clone validation, and a second independent audit.

## Certification state

CURRENT TREE: CONTAINED WITHIN TESTED CLASSES
HISTORICAL OBJECT GRAPH: NOT CLEAN
SECONDARY PUBLICATION SURFACES: AUDIT CONTINUES
HISTORY REWRITE: NOT PERFORMED
PUBLICATION CERTIFICATION: WITHHELD
