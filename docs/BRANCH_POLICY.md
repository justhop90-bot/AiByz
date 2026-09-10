# AiByz Branch Policy

**Effective:** 2026-09-09  
**Authority parent:** `CANONICAL_AUTHORITY.md`

## Rules

1. **`main` is the only canonical branch.**
2. Historical `aegis/*` branches are **provenance only** — never develop new work on them and never treat them as live status.
3. Prefer small knowledge/progress commits directly on `main`.
4. Use short-lived branches for risky code:
   - `feature/<name>` — candidate modules / slice work
   - `probe/<name>` — probe fixes and evidence packages
   - `experiment/<name>` — speculative; never authority
5. Delete feature/probe branches after merge.
6. Do not create `handoff-final`, `final2`, or similar authority-sounding branches.
7. Production-oriented `.per` changes should land via PR when possible, with residual-risk notes updated.

## Naming examples

```text
feature/civilian-lifecycle-v1
probe/cl3-evidence-2026-09-10
experiment/food-portfolio
```
