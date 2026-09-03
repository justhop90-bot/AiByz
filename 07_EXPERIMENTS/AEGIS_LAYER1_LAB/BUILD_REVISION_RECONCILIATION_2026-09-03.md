# AEGIS Layer 1 — Build Revision Reconciliation — 2026-09-03

## Question
Was the controlled executable 101.103.48987.0 an obsolete build, or does it correspond to the current public Steam build?

## Evidence
- Local executable: `AoE2DE_s.exe`.
- Local file version/product version: `101.103.48987.0`.
- Local SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`.
- Local Steam AppID 813780 manifest reports build ID `24094652`.
- SteamDB public branch reports build ID `24094652`, built July 7 2026.
- Current Steam/community reports identify build `101.103.48987.0 (#180059)` with Steam build `24094652`.

## Official revision check
World's Edge identifies Update 177723 as the June 2 2026 PC release and states the title screen should show Build 177723. Its page subsequently lists minor updates 178524, 179158, and 180059. The final listed 180059 fixes include a shutdown crash, player-profile-stats crash, and a dataset-mod loading issue.

Therefore the previous `BUILD_REVISION_BOUNDARY_2026-09-03.md` interpretation that treated `101.103.48987.0` as merely an older pre-current-build artifact was incorrect.

## Reconciled identity
The controlled executable is the current public Steam PC build lineage represented by Steam build ID `24094652` and game build `#180059`, while its executable file version remains `101.103.48987.0`.

These identifiers are different namespaces and must not be conflated:
- game/update build: `180059`
- executable file version: `101.103.48987.0`
- Steam build ID: `24094652`
- executable SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

## Epistemic disposition
CONFIRMED: the controlled executable is not an obsolete pre-177723 build.
CONFIRMED: local Steam manifest and public Steam build ID agree at `24094652`.
CONFIRMED: the executable file version maps to the current `#180059` public PC build in contemporary public reporting.
SUPERSEDES: the earlier inference that a future current-build replacement was required.
RETAINED: exact SHA-256 remains the primary experimental executable identity.

## Architecture impact
The existing Layer 1 corpus remains validly tied to the current public PC build. No migration or re-baselining is required solely because of the version-number mismatch.

Future reports must record all four identifiers where available. A future executable update requires a new hash and explicit revision-delta qualification.

## Security / methodology
No game files were modified. No injection, hooks, debugger attachment, memory modification, arbitrary UDP, or XS was used. This reconciliation is evidence hygiene, not runtime causal evidence.

## Status
No Layer 1 promotion.
Layer 1 remains 89%.
