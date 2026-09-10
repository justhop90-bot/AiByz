# AiByz Branch Policy

**Effective:** 2026-09-10  
**Authority parent:** `CANONICAL_AUTHORITY.md`

## Canonical rule

1. **`main` is the only canonical branch.**
2. Historical `aegis/*` branches are **provenance only**. Never develop new work on them and never treat their names or documents as live status.
3. The apparent 201-branch population substantially overstates the number of distinct states: multiple branch-name clusters point to identical commits.
4. Branch names containing `canonical`, `final`, `master`, `signoff`, `completion`, `promote`, or `build-readiness` confer **no authority**.

## Confirmed duplicate clusters

The following branch families contain multiple refs to the same commit and are cleanup candidates after provenance is preserved: `aegis/handoff*` → `77404a996a0b0e517992565f9f163b4aa5d2b98a`; `aegis/pass5-cross-validation-*` → the same commit; `aegis/harness*` and `aegis/pass6-operationalization` → `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`; `aegis/pass16-*` → `8d031fd4d7e9ea9f5172bef6e5a77b2fcab591e1`; `aegis/pass75-*` and `tmp-pass75*` → `d9e07d3bfe4a4b875f666b65dd8105e1e29a629c`; `aegis/pass91-layer3-integration-2026-09-04-v2..v11` → `56cafb661201a0c96517508bc6793cb55e05b24f`; `aegis/replay-lifecycle-qc-v2..v4` and related replay-QC refs → `eaa8681a028e4d0d0e7efca4cd7130c0af32bbd1`.

## High-risk historical names

Treat these as stale historical evidence unless `main` explicitly supersedes them: `aegis/final-build-readiness-2026-09-08`, `aegis/r2-r4-semantic-mutation-2026-09-09`, `aegis/project-head-signoff-2026-09-05`, `aegis/promote-completed-systems-2026-09-05`, `aegis/canonical-handoff-2026-09-05`, all `aegis/handoff-canonical*`, all `aegis/handoff-final*`, `aegis/handoff-master`, and `aegis/l3-architecture-prototype-final-2026-09-05`.

**Known semantic conflict:** `aegis/final-build-readiness-2026-09-08` names Cavalry Threat Containment as the first executable slice, while current `main` establishes Civilian Production Loop as primary. Therefore the older branch must not be used to choose current implementation priority.

## Working branches

Use short-lived branches only when needed:
- `feature/<name>` — candidate implementation
- `probe/<name>` — runtime/evidence work
- `experiment/<name>` — speculative work; never authority

Delete feature/probe branches after merge. Do not create `handoff-final`, `final2`, `canonical-final`, or similar authority-sounding refs.

## Cleanup rule

Do **not** delete historical evidence merely because it is obsolete as authority. First preserve provenance in `main`; then delete only redundant refs, especially exact duplicate refs and `tmp-*` branches. Branch cleanup must never rewrite or delete `main` history.

## Protection

`main` should be protected against force-push/deletion and should require appropriate review/status gates before production-oriented `.per` changes are merged.