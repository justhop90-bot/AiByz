# AiByz — Branch Disposition Register

**Effective:** 2026-09-10
**Canonical branch:** `main`
**Purpose:** Prevent branch-name ambiguity from corrupting reconstruction work.

## Authority

`main` is the only canonical branch. No historical branch can override current documents merely because its name contains `canonical`, `final`, `master`, `signoff`, `completion`, `promote`, or `build-readiness`.

## Disposition classes

| Class | Meaning | AI treatment |
|---|---|---|
| CANONICAL | Current project authority | Use for decisions |
| WORKING | Short-lived active work | Inspect only for the task |
| EXPERIMENTAL | Speculative/test work | Evidence only; never authority |
| PROVENANCE | Historical reconstruction | Evidence only |
| OBSOLETE | Superseded as authority | Do not use for current decisions |
| DUPLICATE | Ref points to an already represented commit/state | Cleanup candidate |
| TEMPORARY | Scratch branch | Delete after provenance is preserved |
| HIGH-RISK-NAME | Name can falsely imply authority | Treat as historical unless `main` explicitly promotes content |

## Current disposition

### CANONICAL

- `main`

### WORKING / FUTURE NAMING

Use only when necessary:

- `feature/<name>` — candidate implementation
- `probe/<name>` — evidence/runtime work
- `experiment/<name>` — speculative work

Delete short-lived feature/probe branches after merge.

### PROVENANCE / HISTORICAL

- All `aegis/*` branches are historical unless current authority explicitly says otherwise.
- `lab/*`, `qc/*`, and `research/*` are historical/experimental by default.

### TEMPORARY CLEANUP CANDIDATES

- `tmp-pass75`
- `tmp-pass75b`
- `tmp-pass75c`
- `tmp-pass75d`
- `tmp-pass75e`
- `tmp-pass75f`

These were verified as members of the same pass-75 commit cluster and should be removed only after provenance is represented elsewhere.

## Confirmed duplicate-state families

Multiple refs point to identical commits. The branch names therefore do not represent independent project states.

- `aegis/handoff*` → `77404a996a0b0e517992565f9f163b4aa5d2b98a`
- `aegis/pass5-cross-validation-*` → `77404a996a0b0e517992565f9f163b4aa5d2b98a`
- `aegis/harness*` and `aegis/pass6-operationalization` → `51305c01b2a58260e7dee4eea8a3b5a3ab52abcb`
- `aegis/pass16-*` → `8d031fd4d7e9ea9f5172bef6e5a77b2fcab591e1`
- `aegis/pass75-*` and `tmp-pass75*` → `d9e07d3bfe4a4b875f666b65dd8105e1e29a629c`
- `aegis/pass91-layer3-integration-2026-09-04-v2..v11` → `56cafb661201a0c96517508bc6793cb55e05b24f`
- replay lifecycle/QC families → `eaa8681a028e4d0d0e7efca4cd7130c0af32bbd1`

## High-risk names

The following must never be interpreted as current authority by name alone:

- `aegis/final-build-readiness-2026-09-08`
- `aegis/r2-r4-semantic-mutation-2026-09-09`
- `aegis/project-head-signoff-2026-09-05`
- `aegis/promote-completed-systems-2026-09-05`
- `aegis/canonical-handoff-2026-09-05`
- all `aegis/handoff-canonical*`
- all `aegis/handoff-final*`
- `aegis/handoff-master`
- `aegis/l3-architecture-prototype-final-2026-09-05`

## Known semantic conflict

`aegis/final-build-readiness-2026-09-08` identifies Cavalry Threat Containment as its first executable slice. Current `main` identifies Civilian Production Loop as primary and Cavalry as deferred. The older branch therefore cannot determine current implementation priority.

## Cleanup safety rule

Do not delete historical evidence solely because it is obsolete as authority. First preserve the relevant provenance in canonical documentation. Then remove redundant refs, starting with exact duplicate and `tmp-*` refs. Never rewrite or delete `main` history as part of branch cleanup.

## AI rule

If a branch is not `main`, assume it is non-authoritative until a current canonical document explicitly states otherwise. Branch age, branch name, commit message, or apparent completeness are not authority signals.
