# Layer 1 Pass — `.pdata` / CodeView / RIP QC — 2026-09-03

## Controlled executable
- Executable: `AoE2DE_s.exe`
- File size: 71,648,568 bytes
- Image base: `0x140000000`
- `.text`: RVA `0x1000`, raw size `0x313ae72`
- `.rdata`: RVA `0x313c000`, raw pointer `0x313ac00`
- `.pdata`: RVA `0x4c28000`, raw pointer `0x41d4000`, raw size `0x1e8a00`

## `.pdata` geometry
- 166,741 physical 12-byte slots were inspected.
- 166,730 slots contain non-zero runtime-function records.
- 11 trailing slots are zero padding.
- Valid function starts are unique and monotonically ordered.
- No overlaps were found among valid runtime-function intervals.
- Function-size minimum: 1 byte; median: 91 bytes; mean: 275.17 bytes; maximum: 106,696 bytes.
- Sum of valid runtime-function interval sizes: 45,879,189 bytes, about 88.88% of `.text` raw size.

## CodeView discovery
- PE debug directory contains CodeView type 2 data.
- Signature: `RSDS`.
- PDB GUID: `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`.
- PDB age: `1`.
- Embedded PDB path: `F:\Agents\PhoenixBuilders-11\p4\release_12_0_0_build_machine\Build\Steam\Game\Retail\Output\AoE2DE_s.pdb`.
- No matching `AoE2DE_s.pdb` was found under `C:\Users\justh`; a full `C:\` search encountered access-denied locations and did not produce a match.

## AI anchor RIP-reference test
The corrected raw/VA mapping was used. The entire `.text` section was Capstone-decoded and tested for RIP-relative memory operands targeting seven exact `.rdata` AI diagnostic/source anchor addresses.

Selected anchors included `UnitAIModule.cpp`, `TribeUnitAIModule.cpp`, `CurrentAction`, `currentTargetID`, `currentTargetType`, `processNotify`, and `ai::search`.

Result: zero RIP-relative references to the seven exact anchor addresses.

## Absolute-pointer test
The entire executable byte image was searched for the exact 64-bit little-endian virtual addresses of those seven anchors. All seven returned zero exact pointer occurrences.

## Interpretation
The diagnostic/source strings are not recoverable through the tested direct RIP-relative or exact 64-bit-pointer representations. This strengthens the case that these strings are debug/source/metadata corpus rather than straightforward code-reference anchors, or that references are mediated through another representation.

This does NOT establish that the corresponding AI code is absent. It establishes only that these two direct reference representations were absent in the controlled image.

## New high-value lead
The executable itself identifies the exact PDB identity. If the matching PDB can be obtained through an authorized build/symbol source, it could radically improve source/function/line attribution without weakening the native evidence standard. Until the PDB is authenticated against this GUID+age, it is an external lead, not evidence.

## Next native target
Use `.pdata` as the function coordinate system and pursue stateful functions through instruction/data-flow rather than string ownership. Priority remains: persistent-fact result mutation, then `CurrentOrder -> CurrentAction`, then action invalidation/recovery.
