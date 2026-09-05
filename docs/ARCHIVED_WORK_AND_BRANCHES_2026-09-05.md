# AiByz / AEGIS — Historical Work and Branch Disposition

**Effective:** 2026-09-05

This record prevents historical work from being mistaken for current authority while preserving the project's development history.

## Current authority

`main` is the only canonical starting branch.

Current canonical documents:

- `CANONICAL_AUTHORITY.md`
- `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
- `docs/CANONICAL_QC_2026-09-05.md`
- `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
- `docs/REPOSITORY_OPERATING_STANDARD_2026-09-05.md`

## Superseded handoff/QC records

These remain valuable historical records but are not current authority:

- `docs/PROJECT_HANDOFF_2026-09-04.md`
- `docs/QC_FULL_REPOSITORY_2026-09-04.md`
- earlier dated handoffs, completion records, and QC passes.

Their Git history is retained. A future engineer should consult them only when tracing how a conclusion changed or when the canonical record explicitly references them.

## Superseded/open PRs

The repository accumulated several PRs from intermediate architecture and laboratory branches. Once their useful contents have been incorporated or explicitly preserved, the PR itself should be closed rather than left as a competing workflow.

Current known intermediate PRs:

| PR | Disposition | Reason |
|---:|---|---|
| #11 | Historical / close | Layer-1 harness bootstrap; superseded by later architecture and current package-first gate |
| #12 | Historical / close | AoE2DE adapter branch depended on #11 and is not the current runtime path |
| #13 | Historical / close | Earlier QC/front-door pass superseded by canonical 2026-09-05 state |
| #14 | Historical / close after preserving research | Comparative optimization research; useful as methodology, not current machine authority |
| #15 | Merged | Layer-2 practical archaeology retained in canonical history |
| #16 | Merged | Canonical handoff/QC promotion; current main head |

PR closure does not delete the commits or the underlying research branches. Git history remains the forensic record.

## Branch naming problem

The repository contains many branches named with `final`, `final2`, `final3`, `master`, `canonical`, `active`, `work`, and similar adjectives. These names are historical and must not be interpreted as authority.

The project will not create additional authority-looking branches. New work should use a precise workstream name and date, then merge into `main` when accepted.

## Historical experimental families

The repository history also contains:

- Layer-1 harness/adapter experiments;
- scheduler and native-runtime investigations;
- replay/CADE experiments;
- old cross-validation passes;
- early Layer-3 architecture passes;
- superseded handoff attempts.

These are not junk. They document negative results, corrections, and decision boundaries. Preserve them unless they contain sensitive material or violate the publication policy.

## Cleanup rule

The objective is not a pretty branch list. The objective is an unambiguous authority graph:

`main → current authority`

`historical branches/commits → provenance`

`open PRs → active proposed changes only`

No branch or PR should remain open merely because it once represented a possible future direction.
