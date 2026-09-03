# AEGIS Layer 1 — Build Revision Boundary — 2026-09-03

## Question
Is the controlled executable still the current public AoE2DE build, and what does that mean for Layer 1 evidence?

## Method
- Re-checked current official Age of Empires II: Definitive Edition release information.
- Compared it against the exact executable fingerprint used by the AEGIS laboratory.
- No executable replacement was made.

## Controlled build
- Executable: `AoE2DE_s.exe`
- Internal version: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- This fingerprint remains the laboratory's controlled historical build.

## Current public revision
Official Update 177723, dated June 2, 2026, instructs Steam/Microsoft Store users to update to Build 177723. The update includes AI-engine fixes, including exploration-command targeting and players-unit-type-count reporting corrections.

Therefore the laboratory executable is not the current public build as of this review date.

## Scientific consequence
The distinction is now explicit:

`101.103.48987.0 / SHA256 ...A321A4`
= controlled historical executable and evidence source.

`177723`
= current public revision and a future revision-comparison target.

Evidence obtained from the controlled executable remains valid for that exact build unless independently shown otherwise. It must not be silently generalized to Build 177723.

## Disposition
CONFIRMED: controlled executable identity remains exact and reproducible.
CONFIRMED: current public build is newer.
NEW REQUIREMENT: every future runtime claim must carry the executable build/hash provenance.
NO existing Layer 1 finding is invalidated solely by this revision boundary.
NO automatic promotion or downgrade of Layer 1 percentage.
Layer 1 remains 89%.

## Next discriminating work
1. Finish causal closure on the controlled build rather than mixing revisions.
2. When a current-build executable is intentionally supplied, create a separate build fingerprint and run a revision-delta campaign.
3. Prioritize AI-engine changes that can alter fact semantics or command behavior before comparing cross-build results.
