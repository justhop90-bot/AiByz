# AEGIS Project Status — Final Layer 1 Investigation Position

**Last substantive update:** 2026-09-03  
**Current layer:** Layer 1 — Machine Understanding  
**Investigation status:** CLOSED / HANDOFF  
**Working completion estimate:** **89%**  
**Completion certification:** NOT SATISFIED

## Executive status

Layer 1 investigation is closed at 89%. This is a deliberate stopping point, not a declaration of machine omniscience and not a claim that the remaining work is unimportant. The remaining 11% is concentrated in implementation-level causal closure: verified native state mutations, rule-to-action bridging, scheduler behavior, failure propagation, and at least one predictive end-to-end causal path.

The repository now contains a final investigation handoff, the `.pdata`/CodeView/PDB findings, native negative-evidence boundaries, the AIExpert/UnitAI model, the predictive standard, and the explicit unresolved frontier. A future engineer should be able to resume from this point without reconstructing the investigation from conversational history.

## Scope clarification

ByzBot is a pure `.per` implementation. XS is machine archaeology only and is neither an implementation dependency nor a Layer 1 completion gate. The completion checklist must not require XS qualification merely because XS is present in the executable.

## Authoritative controlled build

- Executable: `AoE2DE_s.exe`
- Version: `101.103.48987.0`
- Size: `71,648,568` bytes
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Image base: `0x140000000`
- Architecture: PE32+, x86:LE:64 Windows

All native claims are build-scoped. The local installation path remains intentionally redacted from public documentation.

## Final native archaeology findings

### `.pdata` function geometry

The controlled executable contains 166,741 physical 12-byte `.pdata` slots. 166,730 are non-zero runtime-function records and 11 are trailing zero padding. Valid starts are unique and monotonically ordered; no overlaps were found among valid runtime-function intervals. Function interval statistics: minimum 1 byte, median 91 bytes, mean 275.17 bytes, maximum 106,696 bytes. Aggregate interval coverage is 45,879,189 bytes, approximately 88.88% of `.text` raw size.

This is a structural coordinate system, not a semantic function inventory. It allows bounded native instruction/data-flow work without depending on guessed function boundaries.

### CodeView / PDB lead

The PE debug directory contains CodeView `RSDS` data with GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`, age `1`, and an embedded build-system path ending in `AoE2DE_s.pdb`. No matching PDB was found in the user's home directory; a full `C:\` search encountered access-denied locations and did not establish a match. A matching PDB is therefore a future authorized lead, not current evidence.

### AI anchor reference tests

A corrected section-aware mapping was used to test seven exact AI diagnostic/source anchors, including `UnitAIModule.cpp`, `TribeUnitAIModule.cpp`, `CurrentAction`, `currentTargetID`, `currentTargetType`, `processNotify`, and `ai::search`. Full `.text` Capstone scanning found zero RIP-relative references to those exact `.rdata` addresses. An executable-wide exact 64-bit-pointer scan also found zero occurrences.

This is bounded negative evidence for the tested direct representations. It does not prove the AI code or diagnostics are absent; indirect, indexed, encoded, or metadata-mediated representations remain possible.

### Metadata-pointer false positive

A correctly mapped metadata-area field pointed to `0x1417FF3E0`, a valid `.pdata` function start. Direct disassembly showed cleanup/destructor-like behavior, so the candidate was rejected as an XS API implementation association. The permanent rule is: metadata proximity + valid pointer + valid function boundary does not establish semantic ownership.

## Ghidra disposition

Historical Pass33 remains preserved. It contains genuine analysis activity but also substantial function-body repair noise. The controlled headless run successfully imported/saved the exact executable, but broad analysis timed out at 1800 seconds during `Disassemble Entry Points` with a `CreateThunkFunctionCmd` / `body must contain the entry point` error. Therefore import/save is established, but clean complete auto-analysis is not. Targeted `.pdata`-bounded native work is the preferred method.

## Current machine model

The working `.per` causal model is:

`.per source -> lexical/preprocessor handling -> rule construction -> rule storage -> scheduling/evaluation -> facts/goals/strategic numbers -> action/handler -> native AI control -> UnitAI -> simulation -> observable feedback`

Native vocabulary establishes explicit AI-fact initialization, persistent-fact evaluation, rule definitions, sorted rules, rule groups, UnitAI order/action/target/notification/search/recovery concepts, feasibility validation, and broad game-state semantics. Exact implementation ownership of the critical bridges remains open.

## Predictive architecture

The most defensible future ByzBot authority model is:

`OBSERVATION -> BELIEF / MACHINE FACTS -> STRATEGIC INTENT -> TACTICAL REQUEST -> NATIVE VALIDATION / ACCEPTANCE -> EXECUTION -> OBSERVED RESULT -> RECONCILIATION -> RETAIN / RETRY / RETARGET / REPLACE / ABANDON`

This is an engineering architecture derived from convergent evidence, not a claim that the shipped engine literally uses these exact classes.

## Final Layer 1 gaps

1. Verified rule-loader/parser boundary.
2. Verified rule-representation ownership and mutation.
3. Verified persistent-fact result mutation, cache/storage lifetime, and freshness boundary.
4. Verified scheduler comparator, interval semantics, and transition path.
5. Verified rule/handler-to-native-action bridge.
6. Verified `CurrentOrder -> CurrentAction` mutation chain.
7. Verified action failure/invalidation/completion propagation.
8. At least one runtime-predictive `.per` causal path.
9. Complete native object identity lifecycle closure where required by implementation.

## Why 89% remains correct

No implementation-level AI causal edge was promoted solely from strings, source names, metadata proximity, decompiler guesses, or plausible architecture. The remaining work is therefore small in scope but high in evidentiary difficulty. Raising the percentage without closing a critical causal edge would weaken the project's epistemic standard.

## Repository disposition

The current public tree is suitable for practical development and preserves the research record. Historical source-derived material remains controlled exposure rather than certified-clean history. Malformed/unverified disassembly remains non-evidentiary. Every substantive finding is expected to survive in dated documentation or atomic knowledge records.

## Final handoff

Read `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md` first when resuming after the investigation closure. Then follow `RESEARCH_INDEX.md`, the predictive standard, the evidence matrix, the native archaeology/QC documents, and the open-question register.

**Final Layer 1 position: 89%, investigation closed, completion gate unsatisfied, remaining work precisely bounded.**
