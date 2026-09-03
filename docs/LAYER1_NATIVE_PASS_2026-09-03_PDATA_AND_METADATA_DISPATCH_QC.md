# Layer 1 — Native Pass — `.pdata` Function Geometry and Metadata Dispatch QC — 2026-09-03

## Status

ACTIVE / NOT COMPLETE

Working completion estimate: 89%.

This pass changes the native-archaeology method more than the machine model. The important result is a reproducible way to recover verified native function boundaries from PE exception/unwind metadata without depending on a completed Ghidra auto-analysis run.

## Controlled executable

Build: AoE2DE version `101.103.48987.0`

SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

Image base: `0x140000000`

The public record intentionally omits the local installation path.

## 1. PE section geometry is now independently reproducible

The controlled executable reports:

- `.text`: RVA `0x1000`, raw `0x400`, raw size `0x313A000`;
- `.rdata`: RVA `0x313C000`, raw `0x313AC00`, raw size `0xBF6A00`;
- `.data`: RVA `0x3D33000`, raw `0x3D31600`, raw size `0x4AB600`;
- `.pdata`: RVA `0x4C30000`, raw `0x41DCC00`, raw size `0x1E8800`.

The section mapping rule remains mandatory:

`raw = section.raw_pointer + (RVA - section.virtual_address)`

A raw file offset must never be treated as a universal RVA.

## 2. `.pdata` provides a large native function-boundary index

Parsing the PE `.pdata` records as 12-byte runtime-function entries produced **166,730 valid function ranges** for the controlled build.

Each recovered range supplies a start RVA and end RVA, yielding an independently reproducible native function-boundary set.

This is a major methodological improvement because it gives us a verified candidate function geometry layer even when broad Ghidra auto-analysis is incomplete or times out.

Evidence class: NATIVE-IMPLEMENTATION / executable-format-derived structure.

It does not prove semantic names or callers. It proves that the executable's unwind metadata supplies these function ranges.

## 3. Metadata-region pointer experiment

The native API metadata region contains the string `xsGetUnitObjectId` at VA `0x1432AF648` (raw `0x32AE248`).

A scan of a nearby correctly mapped `.rdata` region found one 8-byte value at:

`0x1432B0A48 -> 0x1417FF3E0`

The target `0x1417FF3E0` is a `.pdata`-recognized function start.

Therefore we have now demonstrated the complete mechanical chain:

`PE raw bytes -> section mapping -> 64-bit pointer -> `.pdata` function-start membership -> verified native function range`

This is stronger than the earlier proximity-only association.

## 4. The pointer target is NOT an XS API implementation

The verified function at `0x1417FF3E0` was disassembled directly from the executable.

Its observed behavior includes:

- saving registers and receiving an object pointer in `RCX`;
- installing a vtable-related pointer at `[RCX]`;
- reading a count at `[RCX+0x20]`;
- iterating an 8-byte pointer array at `[RCX+0x18]`;
- invoking cleanup/release-like calls for each non-null element;
- zeroing array entries;
- releasing additional owned pointers;
- clearing object fields;
- conditionally freeing the containing object when a flag is set;
- returning the original object pointer.

The function therefore has strong cleanup/destructor-like characteristics.

The pointer's proximity to the XS API string region does **not** make it an XS API implementation.

This association is explicitly rejected.

## 5. Why this negative result matters

The experiment establishes a useful anti-false-positive rule:

`metadata-region pointer -> valid function start`

is necessary evidence for a possible dispatch relationship, but it is not sufficient evidence that the function implements the adjacent API symbol.

We must additionally establish at least one of:

- table-record geometry connecting the symbol and pointer;
- initialization code that constructs the record;
- lookup code that selects the pointer from an identifier;
- a calling convention/argument pattern consistent with the API;
- runtime or source-contract corroboration.

Without that bridge, the function remains unrelated native infrastructure.

## 6. New archaeology capability: function-boundary-first analysis

The investigation should now reverse the previous search direction.

Old method:

`interesting string -> search for direct code reference -> infer function`

New preferred method:

`verified function ranges -> characterize function bodies -> identify data references -> classify subsystem`

This is more robust because strings may be referenced indirectly, optimized away from obvious forms, retained as debug material, or embedded in metadata.

For the AIExpert/UnitAI frontier, this means the next useful pass should enumerate verified `.pdata` function ranges in carefully bounded regions and inspect their actual instruction structure rather than scanning the entire executable for string references.

## 7. Immediate target: AIExpert semantic boundary

Known native AI string addresses include:

- `loadRules` — `0x1431CB558`;
- `Defining Fact` — `0x1431CB4F8`;
- `Defining Action` — `0x1431CB528`;
- `Evaluating Persistent Facts` — `0x1431CBF48`;
- `Finished Evaluating Persistent Facts` — `0x1431CBF68`;
- `Next Rule:` — `0x1431CC0D1`.

Direct RIP-relative scans of these exact strings were negative.

The next search should therefore use verified function geometry plus bounded data/reference analysis to identify candidate AI functions without assuming direct string references.

## 8. Immediate target: UnitAI mutation boundary

Known native UnitAI vocabulary includes:

- `CurrentAction`;
- `CurrentOrder`;
- `CurrentTarget`;
- `CurrentTargetType`;
- `processNotify`;
- `processIdle`;
- `ai::search`;
- action completion/failure diagnostics.

The next promotion target is not the diagnostic string itself. It is a verified function containing a defensible state mutation such as:

`read CurrentOrder -> branch -> write CurrentAction`

or

`action failure -> invalidate state -> search/recovery transition`.

## 9. Ghidra status correction

The controlled Ghidra project **does exist** under the investigation directory and contains a repository/project structure plus imported program data.

A long-running Java/Ghidra process was still active during this pass. Its presence means the workspace should not be treated as a clean completed analysis until the process terminates and the resulting project is validated.

The earlier interpretation that the controlled project was simply missing was incorrect and is withdrawn.

The actual problem is narrower: the completed analysis artifact has not yet been demonstrated as a clean, terminal, reproducible analysis result.

## 10. Current evidence promotion

### Promoted

1. PE `.pdata` can be parsed into 166,730 valid function ranges for the controlled build.
2. A correctly mapped `.rdata` metadata-region pointer can be proven to target a `.pdata` function start.
3. The resulting function can be independently disassembled from the executable.
4. The tested pointer target is cleanup/destructor-like and is not proven to implement the adjacent XS API.
5. Function-boundary-first native archaeology is now the preferred method for the AIExpert/UnitAI frontier.

### Not promoted

- XS API dispatch implementation.
- AIExpert rule-loader call graph.
- persistent-fact evaluator function.
- UnitAI state mutation function.
- rule-to-UnitAI bridge.

## 11. Predictive machine implication

We are getting closer to the required causal level because function geometry can now be established independently of semantic labels.

The target chain remains:

`input/state -> verified function -> condition -> state mutation -> downstream call -> observable result`

A native function boundary is the next prerequisite, not the final answer.

## 12. Next pass

1. Use `.pdata` function geometry to partition the AI-related executable regions into verified functions.
2. Within those functions, recover data-reference and call targets using bounded scans.
3. Find the first function with a defensible AIExpert state mutation.
4. In parallel, find the first UnitAI function with a defensible `CurrentOrder`/`CurrentAction` mutation.
5. Prefer whichever produces a complete implementation-level edge first.
6. Record the edge in the atomic machine ledger and use it to construct the first predictive test.

## Six-month recovery note

A future engineer should understand from this record that the project did not fail to find native functions; rather, it lacked a sufficiently reliable bridge from native vocabulary to function bodies. `.pdata` now supplies a reproducible function-boundary layer, while the failed metadata association demonstrates why pointer proximity cannot be promoted to semantics.
