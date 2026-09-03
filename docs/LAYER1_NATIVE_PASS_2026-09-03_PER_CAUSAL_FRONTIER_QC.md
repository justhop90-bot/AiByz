# LAYER 1 — NATIVE PASS: `.PER` CAUSAL FRONTIER QC

Date: 2026-09-03
Status: ACTIVE / NOT COMPLETE
Working progress estimate: 89%

## Executive finding

This pass materially changes the confidence model for the prior XS/metadata finding. The controlled executable's PE section mapping must be used for every raw-file-to-VA conversion. A previous pointer observation at the apparent XS API string address was an artifact of treating `VA - image base` as a raw-file offset.

The corrected mapping places `xsGetUnitObjectId` at VA `0x1432AF648`, raw offset `0x32AE248`, where the bytes are the expected ASCII string. The earlier apparent pointer at that address is therefore rejected.

A real function pointer to `0x1417FF3E0` exists at VA `0x1432B0A48`, in the same broader `.rdata` region, but it is not associated with `xsGetUnitObjectId` by current evidence. The target `0x1417FF3E0` is a valid `.pdata` function start and disassembles coherently, but its behavior is cleanup/destruction-like: it installs a vtable, iterates a pointer array, invokes cleanup/release operations, clears fields, releases storage, and conditionally frees the object. It is therefore quarantined as an XS handler candidate.

## PE mapping baseline

Image base: `0x140000000`.

Relevant sections:

- `.text`: RVA `0x1000`, raw `0x400`, raw size `0x313A000`.
- `.rdata`: RVA `0x313C000`, raw `0x313AC00`, raw size `0xBF6A00`.
- `.pdata`: RVA `0x4C30000`, raw `0x41DCC00`, raw size `0x1E8800`.

For `.rdata`: `raw = 0x313AC00 + (VA - 0x14313C000)`.

For `.text`: `raw = 0x400 + (VA - 0x140001000)`.

This mapping is now mandatory for archaeology scripts.

## Corrected API-region observation

The API metadata region contains adjacent API name/signature strings such as:

`xsGetUnitObjectId`, `xsGetUnitCopyId`, `xsGetObjectCopyId`, `xsGetUnitClass`, `xsGetObjectClass`, `xsGetUnitType`, `xsGetObjectType`, `xsIsObjectValid`, `xsIsObjectAvailable`, `xsGetGarrisonedInUnitId`, and `xsGetGarrisonedUnitIds`.

Corrected raw addresses confirm these are ordinary data strings in `.rdata`.

A corrected scan found one valid 8-byte value in the broader API-region neighborhood that equals a `.pdata` function start: VA `0x1432B0A48` contains `0x1417FF3E0`. The pointer is near `xsGetTechAttribute`/`BXSSource` source/debug strings, not at the API string itself.

## Function-boundary verification

The `.pdata` directory contains approximately 166,730 unwind entries. `0x1417FF3E0` is a valid function start with end `0x1417FF4C6`.

Independent disassembly is coherent from `0x1417FF3E0` through the return at `0x1417FF4C5`. The function:

1. saves registers and establishes stack state;
2. stores an incoming object pointer;
3. writes a vtable pointer;
4. reads a count from object offset `+0x20`;
5. walks an array at object offset `+0x18`;
6. invokes cleanup on non-null elements;
7. clears array elements;
8. releases the array/storage;
9. releases another owned pointer;
10. destroys a secondary member;
11. releases the main array storage;
12. conditionally frees the containing object.

This is strong implementation-level evidence for a cleanup/destruction function. It is not evidence that the function implements any XS API.

## Critical correction

The prior statement that the API string itself contained a pointer to `0x1417FF3E0` is withdrawn.

The stronger and more accurate statement is:

`A real native function pointer exists elsewhere in the surrounding metadata/debug region; its semantic ownership is unresolved.`

This distinction prevents a false dispatch edge from entering the evidence matrix.

## `.per` project scope

ByzBot is a pure `.per` project. XS is retained only as native-machine archaeology. No XS subsystem is a ByzBot implementation dependency under the current design.

The implementation-facing machine path is therefore prioritized as:

`.per source → lexical/preprocessor handling → rule construction → scheduling/evaluation → facts/goals/strategic numbers → action/handler → native UnitAI → simulation → observable feedback`.

## Native `.per` evidence currently strongest

The native AIExpert corpus contains source/debug vocabulary for:

- `loadRules`
- `Defining Constant`
- `Defining Fact`
- `Defining Action`
- `ruleElementsPtr`
- `rule[j].element`
- `ruleDebugInfo[j]`
- `Evaluating Persistent Facts`
- `Finished Evaluating Persistent Facts`
- `Next Rule`
- `AIExpertEngine::ResolveBreakPoint`
- `AIDebugger`

The parser/error corpus distinguishes lexical, directive/preprocessor, syntax, file I/O, capacity, and rule-presence failures. This provides a native semantic boundary map but does not yet establish the complete call graph.

## High-value `.per` inference

The machine exposes many derived predicates and control surfaces rather than only raw values. Relevant examples include feasibility (`can-build`, `can-research`, `can-train`), population/resource state, research state, player state, timers, and strategic numbers governing attack/defense groups, target evaluation, gathering, retasking, exploration, defense distance, and cooperation.

Practical implication: ByzBot should eventually distinguish between mechanisms it must implement itself and mechanisms it should steer through native AI control surfaces.

## Current causal frontier

### A. Rule loading

Need verified native function boundaries for:

`.per file → loadRules → parser/preprocessor → semantic construction`.

### B. Rule representation

Need to establish ownership and mutation of:

`rule[]`, `ruleElements`, `ruleDebugInfo`, sorted rule structures, and rule scheduling state.

### C. Persistent fact evaluation

Need one verified path from world-state query to persistent fact result and then to a rule decision.

### D. Rule → native action bridge

Need one verified path from a satisfied rule handler to an action/order request.

### E. UnitAI mutation

Need one verified native path showing a mutation of `CurrentOrder` or `CurrentAction`, followed by its downstream consumer.

### F. Feedback

Need one verified path from native execution result/failure/completion back into state observable by the rule engine.

## Evidence policy

The following remain explicitly quarantined:

- malformed prior targeted disassembly artifacts;
- raw-offset-as-RVA address interpretations;
- `0x1417FF3E0` as an XS handler;
- source/debug string adjacency as execution order;
- unverified function-pointer ownership;
- rule-engine architecture inferred solely from names.

The following are promoted:

- PE section mapping;
- `.pdata` function-boundary membership for `0x1417FF3E0`;
- coherent disassembly of that function;
- native AIExpert parser/rule vocabulary;
- native UnitAI state vocabulary;
- the requirement to treat `.per` causal closure as the implementation frontier.

## Next pass

Do not perform another broad XS scan.

Primary target: recover a verified native `.per` rule-engine function boundary and follow it into either rule construction or persistent-fact evaluation. In parallel, recover one UnitAI state mutation chain. The preferred result is one end-to-end causal edge rather than a larger vocabulary inventory.
