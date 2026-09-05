# AiByz / AEGIS — Repository Operating Standard

**Effective:** 2026-09-05
**Authority:** `main`
**Purpose:** define how this repository is organized, what is authoritative, how history is preserved, and how future engineering work enters the project.

## 1. Repository role

`justhop90-bot/AiByz` is the authoritative project record for AEGIS.

GitHub is the durable source for:

- current project state;
- architecture and contracts;
- machine evidence and its provenance;
- historical archaeology;
- research conclusions and negative results;
- implementation source once implementation begins;
- validation records;
- decisions and their rationale.

Local workstation state is evidence, not authority, until it is captured, hashed, dated, and committed with provenance.

## 2. Authority hierarchy

When sources disagree, resolve them in this order:

1. **Current authoritative repository state** on `main`.
2. **Dated current evidence artifacts** explicitly superseding older records.
3. **Layer-specific authoritative artifacts** named by `CANONICAL_AUTHORITY.md`.
4. **Historical repository records** preserved for provenance.
5. External documentation and comparative research.
6. Engineering inference/hypothesis.

A newer document does not automatically erase an older one. It must explicitly supersede or correct it.

## 3. Main branch policy

`main` is the canonical starting point.

Future implementation or evidence changes should normally follow:

`feature/research branch → review → merge → main`

Direct mutation of `main` should be reserved for emergency corrections or repository administration. Important changes should have a reviewable commit/PR trail.

GitHub's repository guidance recommends protected important branches, pull-request review, status checks, and code ownership where stability matters. AEGIS adopts those principles.

## 4. Branch taxonomy

Use short-lived branches for active work:

- `aegis/<workstream>-<date>` — architecture/research/engineering work;
- `fix/<topic>-<date>` — corrections;
- `experiment/<topic>-<date>` — bounded experiments that are not yet authoritative.

Historical branches are retained only as provenance when they contain information not represented elsewhere. They are not alternate sources of truth.

Do not create branches named `final`, `final2`, `final3`, `master`, `canonical`, `active`, etc. to indicate authority. Authority is assigned by the repository's canonical documents, not by adjectives in branch names.

## 5. Artifact classes

Every important artifact belongs conceptually to one of these classes:

### A. Canonical current state

Current authority records, active architecture, current ABI, current runtime source, and current status.

### B. Evidence

Hashes, manifests, machine observations, validator output, runtime observations, replay evidence, and controlled experiment results.

### C. Architecture

AEGIS contracts, state models, transition specifications, interfaces, invariants, and implementation plans.

### D. Historical archaeology

HD/Promisory reconstruction, source archaeology, strategic fossils, and historical engineering analysis.

### E. Research

External comparative work, literature, tools, and supporting investigations.

### F. Historical / superseded records

Older handoffs, QC passes, abandoned approaches, and corrected records. These remain valuable because they show how conclusions changed.

## 6. Directory responsibilities

```text
03_HD_ARCHAEOLOGY/       Historical AI / strategy archaeology
04_LAYER3_ARCHITECTURE/  Current AEGIS architecture and ABI work
05_RUNTIME_CANDIDATE/    Runtime candidates and bounded interpreters
07_EXPERIMENTS/          Experimental infrastructure only when intentionally promoted
12_RESEARCH/             External research and source provenance
knowledge/               Durable atomic institutional memory / ledgers

docs/                    Governance, handoffs, QC, machine evidence, and repository documentation
```

The numbered research directories are historical project strata. Do not renumber them merely for aesthetic reasons; path stability is part of provenance.

## 7. Naming standard

Use:

`<SUBJECT>_<PURPOSE>_<PASS/REVISION>_<YYYY-MM-DD>.<ext>`

for dated forensic artifacts.

Use stable descriptive names without dates for living documents such as:

- `CANONICAL_AUTHORITY.md`
- `RESEARCH_INDEX.md`
- `README.md`
- schemas and registries that represent the current contract.

Do not create duplicate files merely because a handoff was revised. Prefer one canonical living document plus explicitly named historical records.

## 8. Handoff standard

There is exactly one current canonical handoff.

At present:

`docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`

Older handoffs remain historical records and must not be presented as current starting points.

Every future canonical handoff should state:

- effective date;
- canonical commit/branch;
- current build target and qualification;
- current layer boundaries;
- current architecture;
- evidence authority;
- known contradictions/corrections;
- blocked gates;
- exact next action;
- canonical reading order.

## 9. QC standard

There is exactly one current canonical QC record:

`docs/CANONICAL_QC_2026-09-05.md`

Historical QC passes remain under their original names. They are evidence of process and should not be silently rewritten into current status.

## 10. Research promotion

A research result enters canonical engineering status only when:

1. its source is identified;
2. its evidence class is explicit;
3. competing interpretations are considered where material;
4. reproducibility is recorded where possible;
5. contradictions are preserved;
6. the affected architecture/implementation decision is identified;
7. the result is committed to GitHub.

## 11. Runtime safety

No `.per` numeric state allocation is authoritative until the target package/build has been inventoried and the ABI gate has been cleared.

Never infer safety from an apparently unused number.

Keep independent:

`engine semantics | validator acceptance | AEGIS design intent`

Never treat:

`command issued = action completed`

or:

`world transition = strategic success`.

## 12. Historical-source policy

Historical/vendor-derived source is research material, not automatically current project source. Public repository presence does not confer implementation authority.

The project preserves knowledge, provenance, hashes, and analysis while respecting the repository's publication/provenance rules.

Failed experiments are retained when they explain a decision, but they must be clearly marked as failed, superseded, quarantined, or non-authoritative.

## 13. Pull-request standard

Every substantive PR should answer:

- What changed?
- Why?
- What evidence supports it?
- What did not change?
- What remains uncertain?
- How was it validated?
- Does it alter an authority boundary?
- Does it alter the ABI?
- What historical artifacts are superseded?

The project uses CODEOWNERS and a pull-request template to enforce the minimum review context.

## 14. Cleanup philosophy

Cleanup means **making authority obvious**, not deleting history.

Preferred actions are:

- consolidate current front-door documents;
- explicitly mark superseded records;
- close stale PRs while retaining their commits/branches as history;
- stop creating duplicate `final`/`handoff` branches;
- use a branch/PR for meaningful repository reorganization;
- retain historical evidence needed to reproduce decisions.

Do not rewrite Git history merely to make the graph look pretty.

## 15. Definition of a clean starting place

A new engineer/model should be able to start at:

`README.md`
→ `CANONICAL_AUTHORITY.md`
→ `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
→ `docs/CANONICAL_QC_2026-09-05.md`
→ `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
→ `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`
→ targeted archaeology/evidence.

If a reader must inspect a dozen similarly named handoffs or guess which branch is current, the repository is not clean enough.
