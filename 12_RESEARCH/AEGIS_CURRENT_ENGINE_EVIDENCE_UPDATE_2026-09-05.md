# AEGIS — Current AoE2DE Engine Evidence Update

**Date:** 2026-09-05  
**Purpose:** Refresh machine-qualification evidence before runtime implementation.

## 1. Installed target

The authorized workstation currently reports:

- `AoE2DE_s.exe`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam AppID: `813780`
- Steam BuildID: `24094652`
- Steam TargetBuildID: `24094652`

This is the build identity for current AEGIS qualification.

## 2. Official engine-change evidence

Official Update 177723 documents AI-engine changes including fixes to `up-send-scout`, `players-unit-type-count`, Treaty-expiry object classification, `Object-data-next-attack`, and other AI behavior. The same release page records subsequent minor updates through 180059.

Engineering consequence: historical command semantics are useful evidence but cannot substitute for target-build behavior when a gate is load-bearing.

## 3. Goal capacity

Official Update Preview 125283 states that available goals increased from 512 to 16,000.

The current specialist Data Limits reference likewise lists goals `1–16,000` and strategic numbers `0–511` for DE/UP scripting.

Engineering consequence: legacy 512-goal assumptions must not be used as a universal current limit. The AEGIS Layer-2 namespace decision remains separately authoritative for reserved AEGIS allocation.

## 4. Specialist reference

The AoE2 AI Scripting Encyclopedia provides current command, parameter, fact, object-data, unit-line, strategic-number, and data-limit references. It is a specialist semantic reference, not a substitute for target-build runtime evidence.

## 5. Evidence hierarchy for Layer 3B

`TARGET EXECUTABLE > TARGET VALIDATOR > STOCK AI > OFFICIAL PATCH NOTES > SPECIALIST REFERENCE > PROJECT INFERENCE > HISTORICAL EXPERIMENT`

A lower level may suggest a test; it may not silently promote a hypothesis to implementation truth.

## 6. Immediate implications

The highest-value qualification targets remain:

1. typed ABI identity;
2. state-channel ownership;
3. identity/generation propagation;
4. unknown/zero/absence semantics;
5. search isolation and multiplicity;
6. publication coherence;
7. command acceptance/pending/created lifecycle;
8. cancellation/supersession;
9. concurrent resource/commitment races;
10. runtime cost and controller-to-world latency.

## 7. Source references

- World's Edge — Update 177723: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/
- World's Edge — Update Preview 125283: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-preview-125283/
- AoE2 AI Scripting Encyclopedia: https://airef.github.io/
- AoE2 AI Scripting Encyclopedia — Data Limits: https://airef.github.io/resources/articles/data-limits.html

## 8. Status

This artifact refreshes evidence only. It does not authorize production `.per` implementation and does not reopen the Layer-3A architecture.
