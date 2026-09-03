# AEGIS Layer 1 — Native `.pdata` / Member-Recovery Deep Dive

Date: 2026-09-03
Build: 101.103.48987.0 / game #180059 / Steam Build ID 24094652
SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4
Layer 1 status: 89%

## Purpose
Reassess the latest `.pdata` member-recovery result and test whether RTTI, vtables,
function-pointer tables, or PDB retrieval can turn AI-related metadata into real
native executable functions.

## Prior evidence
The preceding pass established 166,730 valid x64 RUNTIME_FUNCTION records and
70,952 64-bit data pointers landing on exact runtime-function starts. The AI-related
strings include `loadRules`, `mAiRulesFileData`, `mAiScriptBaseName`, persistent-fact
messages, and BaseScenario AI filename metadata. Earlier RIP-relative scanning found
no direct executable references to the selected literals.

## Method
1. Parse the PE exception directory and construct exact executable function ranges.
2. Scan `.rdata` and `.data` for pointers whose targets are exact `.pdata` function starts.
3. Search for canonical MSVC x64 Complete Object Locator structures and candidate vtables.
4. Enumerate long contiguous function-pointer runs as potential vtables/dispatch tables.
5. Test the exact CodeView PDB identity against the public Microsoft symbol endpoint.
6. Do not infer semantics from address proximity, metadata proximity, or pointer density.

## Result A — `.pdata` remains strong structural evidence
The exact executable contains 166,730 valid runtime-function records. These are legitimate
function intervals supplied by the PE exception/unwind metadata. They provide a reliable
universe of executable function starts for later attribution. Microsoft documents that
x64 unwind metadata is associated with function prologs/epilogs and exception handling.

This does not identify C++ class membership or semantic purpose. A runtime-function record
is a boundary, not a name.

## Result B — 70,952 function-pointer hits are real but heterogeneous
A scan found 70,952 64-bit pointers in `.rdata`/`.data` that resolve exactly to a valid
`.pdata` function start. This materially improves the recovery substrate: we now have
real executable targets rather than merely string or type metadata.

However, the hits are necessarily heterogeneous. They can include vtables, callback
arrays, registration tables, dispatch tables, jump/handler tables, object-model tables,
and other function-pointer structures. Therefore `70,952` is not a count of C++ virtual
functions and is not an AIExpert function count.

## Result C — canonical MSVC x64 COL scan returned zero candidates
A structural scan for six-DWORD MSVC Complete Object Locator records using plausible
image-relative descriptor RVAs and the self-RVA invariant produced:

`COL candidates = 0`

This is important. The earlier plan to recover AIExpert/BaseScenario primarily through
named MSVC RTTI/vftable metadata is now downgraded. The executable may omit standard RTTI,
use a different object/type mechanism, have metadata unavailable in this image, or have
optimization/linking characteristics that defeat this simple signature test.

The negative result does NOT prove that no virtual tables exist. It only rejects this
specific canonical COL-based recovery route for the present binary.

## Result D — long function-pointer runs exist
There are 4,379 contiguous runs containing at least four pointers to valid `.pdata`
function starts. The largest observed run contains 135 entries. Other large runs contain
117, 103, 100, 92, 88, 60, and 58 entries.

These runs are excellent candidate dispatch structures, but their semantics are not yet
known. A long run alone cannot distinguish a vtable from a generated callback/registration
array or another table. The next attribution step must inspect table context and target
function bodies, not just run length.

## Result E — PDB retrieval is not available from the tested public Microsoft endpoint
The executable's CodeView identity is:
GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`, age 1, PDB `AoE2DE_s.pdb`.
A direct public Microsoft symbol-server request using the exact PDB identity returned HTTP
404. This is consistent with the game's PDB not being published there. No private symbol
source was assumed and no untrusted symbol package was accepted as authoritative.

## Correction to the previous direction
The previous pass concluded that “RTTI signature + vtable candidate recovery” was the next
primary route. The COL scan now shows that this should be narrowed:

`canonical COL/RTTI recovery -> downgraded / conditional`
`function-pointer structure recovery -> promoted`
`member/data access -> primary`
`.pdata containing-function attribution -> primary`

The strongest path is now to classify the large function-pointer structures and connect
their targets to executable code that manipulates AI-specific data or calls known AI
subsystems.

## Deeper inference
The combination of zero direct RIP-relative references to selected diagnostic strings,
zero canonical COL candidates, and many genuine function-pointer tables suggests that
compiler/linker metadata is a poor primary navigation surface in this retail image.
The investigation should therefore pivot from “find the name” to “find the behavior”: identify
executable instructions that read/write AI-specific state, then use `.pdata` to delimit the
containing function and pointer tables/call sites to expand the graph.

A useful future target is the native AI scenario handoff:

`scenario/player AI state -> AI rules data/path -> AIExpert construction -> rule load -> persistent facts`

The `mAiRulesFileData` and `mAiScriptBaseName` strings remain useful semantic anchors,
but they are not executable addresses.

## Competing hypotheses
H1: AIExpert/BaseScenario use conventional C++ virtual dispatch but standard COL RTTI is
not present in this retail image.
H2: the relevant classes use virtual dispatch but RTTI metadata is optimized/stripped or
otherwise not recoverable by the canonical COL scan.
H3: relevant dispatch is largely non-virtual/static/generated tables, making function-pointer
cluster classification more productive than RTTI recovery.
H4: AI-specific member access can be recovered from executable instructions without needing
class RTTI at all.

Current ranking: H3/H4 are now the most productive working hypotheses; H1/H2 remain possible
but are no longer the primary route.

## Next discriminating tests
1. Classify the largest function-pointer clusters by target-function locality and table shape.
2. Identify whether cluster targets share common prologue/calling patterns or nearby data tables.
3. Trace executable instructions that load/store pointers into the AI-related object/data
   regions, rather than searching for member-name strings.
4. Use exact `.pdata` intervals to delimit every recovered candidate function.
5. Score candidate functions by convergence on AIExpert-specific behavior: rule loading,
   persistent-fact evaluation, scenario AI data, and filename resolution.
6. Reassess vtable hypotheses only where table structure supplies independent evidence.

## Security and epistemic controls
No executable modification, DLL injection, hooks, debugger attachment, memory modification,
or installed AI-corpus modification was performed. The PDB request was read-only.
No function address is promoted from a string address, pointer-table proximity, or metadata
proximity alone. A successful structural candidate is not a causal Layer 1 finding until
its executable behavior is independently established.

## Promotion decision
Promote: `.pdata` as the authoritative local executable-function boundary; 70,952 pointer
hits as a candidate structure-recovery substrate; zero COL candidates as a reproducible
negative result for canonical MSVC RTTI recovery.

Do not promote: any specific pointer cluster as AIExpert/BaseScenario; any string address as
a function; any function-pointer run as a vtable; any PDB absence as proof of no symbols.

## Repository artifact
This report records the correction and deeper interpretation. The next pass should add a
machine-readable table-classification artifact rather than another broad string census.
