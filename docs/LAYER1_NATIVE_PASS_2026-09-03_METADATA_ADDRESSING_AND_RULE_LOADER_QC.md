# Layer 1 Native Pass — Metadata Addressing and Rule-Loader QC — 2026-09-03

## Executive result

This pass materially improves the native archaeology method by resolving a previously dangerous address-space ambiguity and by identifying a concrete binary structure adjacent to the XS API name/signature corpus.

Two conclusions are promoted:

1. The earlier apparent `+0x1400` correction is confirmed by the PE section table, not by inference. The `.rdata` section has RVA `0x313c000` and raw pointer `0x313ac00`; therefore a raw file offset in `.rdata` maps through the section formula rather than `imagebase + raw_offset`.
2. The contiguous XS API name/signature corpus is followed, for at least the inspected tail entry, by non-text binary fields before the recovered source-path string. One inspected 8-byte field has the value `0x1417ff3e0`, which lies inside `.text`. This is a candidate code-address field, but its semantics are **not promoted** because the bytes at that address currently decode to `ret 0xcd04`, which is not sufficient evidence that the value is a callable XS handler. It may be a data-bearing coincidence, stub, thunk, or another representation.

## PE mapping proof

The target executable's PE headers were read directly. The section table reports:

| Section | RVA | Virtual Size | Raw Pointer |
|---|---:|---:|---:|
| `.text` | `0x1000` | `0x313a000` | `0x400` |
| `.rodata` | `0x313b000` | `0x800` | `0x313a400` |
| `.rdata` | `0x313c000` | `0xbf6a00` | `0x313ac00` |
| `.data` | `0x3d33000` | `0x4ab600` | `0x3d31600` |

Thus `.rdata` file offsets and virtual addresses differ by `0x1400` over the relevant range.

This explains why a raw scan at `0x32ae248` must not be treated as virtual address `imagebase + 0x32ae248`. The correct virtual address is obtained from the `.rdata` section mapping.

## XS metadata corpus

The binary contains a dense sequence of API names and signatures including:

- `xsGetUnitObjectId`
- `xsGetUnitCopyId`
- `xsGetObjectCopyId`
- `xsGetUnitClass`
- `xsGetObjectClass`
- `xsGetUnitType`
- `xsGetObjectType`
- `xsIsObjectValid`
- `xsIsObjectAvailable`
- `xsGetGarrisonedInUnitId`
- `xsGetGarrisonedUnitIds`
- `xsGetMapSeed`
- `xsGetTechAttribute`

For the inspected tail around `xsGetMapSeed` / `xsGetTechAttribute`, the raw bytes are organized as:

`name → signature → padding/binary fields → source-path string → source/debug vocabulary`

Immediately before the source path, the inspected binary fields include:

- an 8-byte zero field;
- an 8-byte value `0x1436a0a38`, which lies in the image's data/readonly-data address space;
- an 8-byte value `0x1417ff3e0`, which lies in `.text`.

The existence of these fields is direct byte-level evidence. Their semantic labels are not yet known.

## Why the previous direct-reference result must be reinterpreted

The earlier zero-reference scans targeted the correct *virtual* API-string addresses only after section mapping was corrected, but the native evidence path remains incomplete because the API name strings themselves may be consumed indirectly through metadata rather than by direct RIP-relative references.

The key methodological change is therefore:

`API string → metadata record/parallel table → identifier/index → dispatch consumer → callable target`

rather than:

`API string → direct code xref → handler`

The direct-RIP-negative result remains valid for the tested representation; it does not demonstrate absence of an API registry.

## Candidate function-address field: quarantine status

The value `0x1417ff3e0` is a candidate address because it lies inside `.text`. However, bytes at that address currently decode as `ret 0xcd04` under raw-file mapping.

Therefore:

- **Observed:** a `.text`-range value occurs in the binary field immediately preceding the source path.
- **Not proven:** the value is an XS function pointer.
- **Not proven:** the value is the implementation of `xsGetTechAttribute`.
- **Not proven:** the decoded instruction at the address is a complete native function boundary.

The field remains a high-value target for corroborating searches, not a recovered dispatch edge.

## New research tree

The next metadata investigation should use the following falsification-first sequence:

1. Recover the exact boundaries of the inspected metadata record.
2. Compare several adjacent API entries rather than one tail entry.
3. Determine whether the binary fields repeat at a fixed stride.
4. Determine whether one field varies monotonically with API order.
5. Determine whether one field points into `.rdata`, `.data`, `.text`, or another registry region.
6. Search for reads of the candidate data region using correct section-aware VA mapping.
7. Locate initialization code that iterates across the region.
8. Recover one identifier-to-record lookup.
9. Recover one record-to-handler resolution.
10. Only then promote a function address to an XS dispatch target.

## Rule-loader implications

The AIExpert corpus independently contains:

- `loadRules for listId=%d, file=%s`
- `Defining Constant`
- `Defining Fact`
- `Defining Action`
- `ruleElementsPtr`
- indexed `rule[j].element`
- `ruleDebugInfo[j]`
- `Evaluating Persistent Facts`
- `Finished Evaluating Persistent Facts`
- `Next Rule`
- `ResolveBreakPoint`

This is strong evidence for a structured rule-loading/evaluation subsystem. The metadata-addressing result now suggests a parallel engineering principle: names/signatures are likely vocabulary at a registry boundary, while execution requires an additional lookup/dispatch structure.

No claim is made that the XS registry and AIExpert rule registry share implementation.

## Native-analysis health

The controlled headless full-analysis attempt remains incomplete. The run reached the `Disassemble Entry Points` analyzer, consumed the 1800-second timeout, and emitted a `CreateThunkFunctionCmd` exception involving an invalid function body. It saved/imported the executable before timeout.

A separate `-noanalysis` invocation attempted to process the project but failed because the expected project path did not exist. These failures are tooling/analysis-state facts, not evidence about the game's native architecture.

The historical Pass33 analysis remains preserved and is not modified.

## Practical engineering consequence

Do not build an XS bridge by hard-coding guessed function addresses. The correct development abstraction remains:

`capability name → build-qualified registry identity → qualified handler → validated call contract`

For AEGIS, this is especially important because capability-level qualification is required; a convenient symbol match is insufficient evidence of callable compatibility.

## Promotion / quarantine ledger

| Finding | Status | Reason |
|---|---|---|
| `.rdata` raw/VA mapping differs by `0x1400` | PROMOTED | PE section-header proof |
| XS name/signature corpus is contiguous | PROMOTED | direct byte observation |
| Binary fields occur between signature corpus and source/debug strings | PROMOTED | direct byte observation |
| One field equals a `.text`-range address | PROMOTED AS OBSERVATION | direct numeric/address-range test |
| `.text`-range field is XS handler | QUARANTINED | no dispatch consumer/call corroboration |
| Direct RIP xref absence proves no API registry | REJECTED | indirect metadata remains plausible |
| AIExpert rule vocabulary represents structured loader/evaluator | PROMOTED AS NATIVE-VOCABULARY MODEL | coherent repeated native corpus |

## Next pass target

The next pass should recover **one real consumer of the metadata region** and **one real UnitAI state mutation chain**, using section-aware address mapping and independently validated instruction boundaries. The objective is not more string collection; it is the first native implementation-level causal edge.
