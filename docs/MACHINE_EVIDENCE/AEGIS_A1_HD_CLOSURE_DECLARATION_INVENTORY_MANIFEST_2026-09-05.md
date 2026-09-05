# AEGIS A1 — HD Closure Declaration Inventory Manifest

**Date:** 2026-09-05  
**Evidence class:** A1 — exact installed target package/build  
**Target executable:** `AoE2DE_s.exe`  
**Target SHA-256:** `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`  
**Steam BuildID:** `24094652`

## Inventory artifact

A deterministic declaration inventory was generated directly from the four-file normal HD AI closure:

1. `AI (HD version).per`
2. `Promisory/defaultConstants.per`
3. `Promisory/finalingConstants.per`
4. `Promisory/finaling.per`

The inventory contains **5,259 declaration rows**, **1,480 unique symbols**, and **4,892 numeric declarations**.

Local authoritative evidence artifact:

`C:\Users\justh\AEGIS_A1_HD_CLOSURE_DECLARATION_INVENTORY_2026-09-05.jsonl`

Artifact size: **853,198 bytes**  
SHA-256: `7f775f636dd4872f01701c88830bdba2327d56b8cbf0610970a510798eb7376f`

## Record schema

Each row preserves:

`symbol | value | file | line | source_sha256`

The inventory is a direct-source declaration inventory, not a semantic ABI decision. Numeric values are not treated as universally interchangeable across channels.

## Allocation finding

No numeric declaration in the exact HD closure occupies the candidate scalar-goal range `10000–15999`.

This supports the existing Layer-2 namespace decision and is strong static collision evidence, but final numeric ABI clearance still requires validator/build-operation qualification and the broader package collision audit defined by Pass 94.

## Provenance rule

The local JSONL is the raw deterministic inventory output for this acquisition. The GitHub repository stores this manifest and its cryptographic identity rather than silently replacing the raw evidence with a summarized approximation.
