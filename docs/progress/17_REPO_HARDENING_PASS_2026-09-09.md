# Repo Hardening Pass — 2026-09-09

**No Husky.** Shared automation via GitHub Actions only.

## Added

| Path | Role |
|------|------|
| `docs/BRANCH_POLICY.md` | main-only authority; feature/probe naming |
| `.github/workflows/policy.yml` | CI: candidate markers, no XS, authority files present |
| `implementation/README.md` | Candidate rules for bot modules |
| `docs/progress/evidence/README.md` | Where live probe evidence goes |
| `docs/BOT_BUILD_ROADMAP.md` | Path to a workable civilian-first bot |
| `.gitignore` | Scratch, secrets, binaries |
| PR template refresh | Gate-aware checklist |

## Unchanged

- Production coding still blocked pending lifecycle evidence
- No numeric allocations cleared
- Civilian remains primary vertical slice
