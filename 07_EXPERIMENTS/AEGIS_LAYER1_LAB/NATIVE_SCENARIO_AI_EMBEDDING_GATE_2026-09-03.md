# AEGIS Layer 1 — Scenario AI Embedding / Loader-Boundary Pass

Date: 2026-09-03
Build: 101.103.48987.0 / game build #180059 / Steam Build ID 24094652
Executable SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4
Status: structural/tooling evidence; no causal promotion

## Question
Can the qualified DE 1.58 scenario representation carry a native AI file payload,
and does that sharpen the native scenario-to-AIExpert loading boundary?

## Method
Inspected the qualified AoE2ScenarioParser 1.58 structure definition and runtime
object model. Created a disposable scenario fixture outside the game installation
containing one embedded `.per` payload. Reparsed the written file and verified the
filename/content survived serialization. No XS script-call condition/effect was used.

## Finding: Files section has native AI-file containers
The DE 1.58 structure defines `Files.ai_files` as repeated `struct:AI2Struct`.
`AI2Struct` contains two `str32` fields: `ai_file_name` and `ai_file`.
The parser therefore models an explicit scenario Files-section AI payload rather
than treating AI as only an external loose file.

## Finding: PlayerDataTwo also carries AI structures
The DE 1.58 structure defines `PlayerDataTwo.ai_files` as repeated `AIStruct`.
`AIStruct` contains `ai_per_file_text` plus an 8-byte unknown field. The same section
also has `ai_names`. This is distinct from the Files-section `AI2Struct` and should
not be collapsed into one representation without native code tracing.

## Controlled fixture
Fixture: `fixtures/P0A_CAL_002_EMBEDDED_PER_PROBE.aoe2scenario`
SHA-256: DD250A5EDD2B5632E2A3D0FC6F26A857BCFDCDD00E165296241CB7FAA1F5C079
Size: 915 bytes
Embedded name: `AEGIS_EMBEDDED_SENTINEL.per`
Embedded content: one minimal `defrule` setting a strategic number.
Parser round-trip: PASS; one AI2Struct survived with exact filename/content.

## Native-binary correlation
The exact executable independently exposes `mAiRulesFileData`, `aiRulesFileSize`,
`aiRulesFileDataSize`, and diagnostics for embedded AI data versus loose AI files.
It also exposes `BaseScenario::getOrExtractPlayerAiRulesFileName(...)`.
This is strong cross-layer correlation: the scenario parser's explicit AI payload
model corresponds to native executable concepts for embedded/loose AI rule data.
It remains correlation until a native call edge is recovered.

## Competing hypotheses
H1 Files-section AI2Struct is consumed by native scenario AI resolution and feeds the
AIExpert rule loader.
H2 PlayerDataTwo AIStruct is the primary scenario/player AI representation and the
Files section is an auxiliary transport/serialization layer.
H3 Both representations are normalized by BaseScenario before AIExpert construction.
H4 They serve different game modes and only one reaches the runtime AIExpert path.

## Discriminating next step
Resolve the native read path for `Files.ai_files` / `mAiRulesFileData` and the native
`BaseScenario::getOrExtractPlayerAiRulesFileName` implementation. Determine whether
it reads the embedded payload, loose path, or both, and identify the exact handoff
into `AIExpertEngine::loadRules(listId,file)`.

## Runtime attempt disposition
A direct GAM launch of the scenario was not accepted by the execution security gate
in this pass. Therefore no runtime claim is made about scenario startup or AI loading.
The failed execution request is infrastructure/tooling evidence only.

## Security
Fixture remained in the lab repository. No installed AI corpus was modified.
No XS execution, DLL injection, hooks, debugger attachment, memory modification,
arbitrary UDP, binary patching, or guessed regression protocol was used.

## Promotion
Promote: existence of explicit scenario AI payload structures as parser-level evidence;
corroborated by native embedded/loose AI-rule vocabulary.
Do not promote: runtime scenario->AIExpert call edge, file-root semantics, or successful
embedded `.per` execution.
Layer 1 remains 89%.
