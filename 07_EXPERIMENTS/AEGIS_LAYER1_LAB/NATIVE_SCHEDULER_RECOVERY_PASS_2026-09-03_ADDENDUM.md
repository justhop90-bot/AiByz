# AEGIS Layer 1 — Native Scheduler Recovery Pass Addendum

Date: 2026-09-03
Layer 1 status: 89% (unchanged)
Build: AoE2DE #180059 / executable 101.103.48987.0 / Steam Build 24094652
Executable SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

## Question
Can the AIExpert region's function-pointer metadata be used to recover the scheduler, or does it represent unrelated compiler-generated/type-erasure machinery?

## Prior evidence
The controlled executable has 166,730 valid `.pdata` runtime-function records. AIExpertEngine diagnostic/source vocabulary is concentrated around the `.rdata` region containing `loadRules`, persistent-fact markers, and the embedded source path. Direct references to the exact diagnostic string bytes remain absent.

## New discriminating test
A strict PE-aware scan was added that:
1. parses the exception directory from the exact executable;
2. treats only BeginRVA values in valid `{BeginRVA,EndRVA,UnwindRVA}` records as function starts;
3. scans the AIExpert-adjacent `.rdata` region for 8-byte pointers to those verified starts;
4. inspects the strongest local pointer families with bounded disassembly and MSVC RTTI reconstruction.

The strict `.pdata` reconstruction independently reports 166,730 valid starts, matching the existing machine coordinate system.

## Key finding: local vtable-like structure is real, but its type is not AIExpertEngine
At `0x1431CC698` the bytes form:

- `0x1431CC698 -> 0x14366D628`
- subsequent entries include `0x140BCEB00`, `0x140BCEB10`, `0x140BCEB20`, `0x140BCEBA0`, `0x140BCEBC0`, `0x140BCEBB0`.

The first pointer is consistent with an MSVC Complete Object Locator. Decoding it gives:

- COL: `0x14366D628`
- TypeDescriptor: `0x144105A80`
- ClassHierarchyDescriptor: `0x14366D650`

The TypeDescriptor contains:

`.?AV?$_Func_impl_no_alloc@V<lambda_1>@@XHPEAH@std@@`

Therefore this structure is a `std::_Func_impl_no_alloc<lambda_1>` type-erasure/vtable object, not evidence of an `AIExpertEngine` vtable.

This is an important rejection: **physical adjacency to `Fact[%d] evaluated persistently to %s` does not establish ownership by the persistent-fact subsystem.**

## Function-body observation
`0x140BCEB20` is a verified `.pdata` function start with a 115-byte body. Its code:

- reads an integer from `[rdx]`;
- obtains a pointer from `[r8]`;
- calls `0x1415E34F0`;
- conditionally calls `0x1415E7790`;
- tests byte offset `0x89` of the returned object;
- increments the caller-supplied integer at `[rdi]` when the predicate succeeds;
- otherwise jumps to `0x140B39B60` with a formatted-data pointer.

The surrounding small functions at `0x140BCEB00`, `0x140BCEB10`, `0x140BCEBA0`, `0x140BCEBB0`, and `0x140BCEBC0` are not `.pdata` function starts in the strict table. Bounded disassembly shows they are short compiler-generated helpers/fragments around the verified function.

No direct caller to `0x140BCEB20` was recovered by a bounded `.text` CALL-rel32 scan. This further prevents promotion to a scheduler edge.

## Why this matters for P0-B
The result does not close scheduler recovery, but it changes the search strategy. The AIExpert-adjacent metadata contains genuine C++ type-erasure structures. The correct next move is therefore:

`AIExpert source-path / diagnostic neighborhood`
→ `RTTI COL`
→ `TypeDescriptor`
→ `class hierarchy`
→ `vtable(s)`
→ `verified virtual method starts`
→ `callers / object construction`
→ `AIExpertEngine state ownership`

The rejected shortcut is:

`nearby diagnostic string`
→ `nearby function pointer`
→ `scheduler`

## Competing hypotheses and disposition

### H1 — AIExpert scheduler vtable
**Rejected for this structure.** RTTI identifies `std::_Func_impl_no_alloc<lambda_1>`, not `AIExpertEngine`.

### H2 — Persistent-fact loop callback represented by a lambda
**Open but unproven.** The lambda type could still be instantiated from AIExpert code; type identity alone does not establish its source call site. The body currently lacks a causal edge to persistent-fact state.

### H3 — Unrelated nearby standard-library object
**Plausible.** The structure's type-erasure machinery is generic C++ infrastructure and may be adjacent to AI diagnostics only because of linker/translation-unit layout.

### H4 — AIExpert scheduler code exists elsewhere in the same source/data neighborhood
**Still open and currently strongest.** The next test should recover all RTTI objects whose TypeDescriptors contain `AIExpertEngine` or relevant nested class names, then enumerate their vtable slots and constructor/destructor references.

## Corrected methodological note
The earlier broad function-pointer cluster output must not be treated as semantic evidence until each target is independently revalidated against the exact `.pdata` table. A reproducible reconciliation probe now confirms that raw-file and memory-mapped `.pdata` parsing produce the same 166,730 starts.

## Security boundary
No binary modification, DLL injection, hooks, debugger attachment, memory modification, protection bypass, arbitrary internal protocol use, or scenario-editor automation was performed.

## Promotion decision
**No Layer 1 proposition promoted.**

The pass produced a stronger negative result and a new positive structural route: **MSVC RTTI/vtable recovery is viable, but the first recovered local vtable is a `std::function` lambda object rather than the scheduler.**

## Next test
Build a strict RTTI inventory over the AIExpert-adjacent `.rdata` region. For every COL, recover TypeDescriptor and ClassHierarchyDescriptor, then retain only classes whose decoded names are AIExpert/AI-related or whose vtable methods have independently established AI state references. Trace constructor → vtable installation → virtual call sites before considering scheduler promotion.
