# AEGIS — Target-Build Qualification Baseline

**Date:** 2026-09-05  
**Layer:** 3A → Machine Qualification  
**Status:** BASELINE ESTABLISHED — QUALIFICATION ACTIVE  
**Target:** Age of Empires II: Definitive Edition on the authorized Windows workstation

## 1. Purpose

This artifact freezes the machine identity against which all AEGIS qualification evidence is interpreted. It is deliberately separate from subsystem architecture closures and from runtime implementation.

## 2. Current executable identity

| Field | Observed value |
|---|---|
| Executable | `AoE2DE_s.exe` |
| Install path | `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe` |
| File size | 71,648,568 bytes |
| File last-write | 2026-09-03 10:51:37 local workstation time |
| SHA-256 | `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4` |
| Steam AppID | `813780` |
| Steam BuildID | `24094652` |
| Steam TargetBuildID | `24094652` |
| Steam LastUpdated | `1786762653` |

The executable hash and Steam manifest were re-observed during this engineering phase. The hash matches the previously established AEGIS baseline.

## 3. External release correlation

Official Update 177723 identifies build 177723 and documents multiple AI-engine fixes, including fixes to `up-send-scout`, `players-unit-type-count`, Treaty-expiry object classification, object-data-next-attack, and other AI behavior. The official page also records later minor updates through 180059. Therefore historical patch notes are evidence of evolving engine semantics, not a substitute for target-build qualification.

The installed executable is newer than the June 2026 Update 177723 release baseline. This strengthens the requirement that all load-bearing machine behavior be tested against the installed executable rather than inferred from older documentation.

## 4. Goal-capacity baseline

Official Update Preview 125283 states that available goals increased from 512 to 16,000. The current AEGIS Layer-2 static ABI closure independently established a reserved candidate AEGIS scalar-goal namespace of `10000–15999`, with `16000` treated as the boundary sentinel. This document does not supersede that ABI decision.

The current community Data Limits reference also lists goals `1–16,000`, strategic numbers `0–511`, and DE rules/elements limits. These values remain secondary evidence and must not override direct target-build tests.

## 5. Evidence hierarchy

1. Direct behavior of the installed target executable.
2. Target-build validator/compiler behavior.
3. Stock AI behavior from the untouched installed `/ai` tree.
4. Official World's Edge release/update documentation.
5. AoE2 AI Scripting Encyclopedia and other specialist references.
6. Project inference.
7. Historical experiments and failed prototypes.

Lower-level evidence cannot silently override higher-level evidence.

## 6. Immediate qualification consequence

The machine qualification program should prioritize behaviors that are both:

- shared by multiple AEGIS subsystems; and
- capable of corrupting authority, identity, evidence, lifecycle, or execution if misunderstood.

Therefore the first qualification wave is:

`Q-01 → Q-02 → Q-03 → Q-04 → Q-05 → Q-06 → Q-07 → Q-08 → Q-09 → Q-10 → Q-11 → Q-12`

No production AEGIS `.per` implementation is considered machine-qualified merely because it parses or validates.

## 7. Current status

**Build identity:** QUALIFIED FOR TESTING  
**Architecture:** Layer 3A closed  
**Shared qualification register:** ACTIVE  
**Runtime implementation:** NOT YET CLAIMED QUALIFIED  
**Execution architecture:** remains closed while its empirical gates are re-tested under the current qualification program.
