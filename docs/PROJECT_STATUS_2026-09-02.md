# AEGIS Project Status — 2026-09-02

## Executive status

**Current layer: Layer 1 — Machine Understanding**  
**State: active, not declared complete**  
**Working completion estimate: 88%**

The project has accumulated a substantial operational and research record, but the completion standard is deliberately stricter than familiarity with AI scripting vocabulary. The remaining work is to turn important machine-facing observations into causal, implementation-level, and experimentally predictive understanding.

## Newest QC result

The latest deep QC pass materially expanded the native XS model. The binary contains a coherent native-vocabulary family for source files, symbol tables, function entries, rule entries/modules, syscall entries/modules, runtime state, activation records, variables, and data.

Especially important structures now visible in the corpus include `mSymbolID`, `mCodeOffset`, `mReturnType`, `mNumberParameters`, `mHashTableSize`, `mNumberSymbols`, `mSymbolsByID`, `mContext`, `mCallerContext`, `mParameters`, `mSyscalls`, `mAddSymbols`, `mStoreHelp`, and activation-record fields including `mFunctionID`, `mPC`, `mStack`, and `mHeap`.

This changes the working XS research model from a simple API-string registry toward a structured runtime/interpreter with symbol identity, registration, dispatch, execution, and debugging state. The model remains an architectural inference until one native registration-to-dispatch chain is recovered.

## Project objective

Build a high-quality Byzantine AI for AoE2DE by establishing the machine contract first, reconstructing general strategic intelligence second, specializing that intelligence for the Byzantine civilization third, and implementing the validated architecture last.

## Current native completion gaps

1. Recover one real XS syscall registration-to-dispatch chain.
2. Recover one symbol-table lookup consumer.
3. Recover one function-entry/code-offset execution path.
4. Recover one activation-record PC transition.
5. Recover one UnitAI state mutation chain.
6. Recover the AIExpert rule-evaluation-to-action/order bridge.

These are now higher priority than additional broad string collection.

## Key methodological rule

All native raw offsets must be converted through the PE section containing the byte. The `.rdata` section has RVA `0x313c000` and raw pointer `0x313ac00`, producing the relevant `0x1400` displacement. Results produced by treating raw offsets as universal RVAs are not admissible evidence.

## XS model

The current strongest model is:

script symbol/name
 -> symbol representation
 -> symbol ID / metadata
 -> function entry or syscall entry
 -> code representation or syscall ID/call array
 -> runtime/interpreter execution
 -> simulation-visible state

This is deliberately split into competing function-entry and syscall-entry branches. The native corpus gives `BXSFunctionEntry` vocabulary for symbol/code/parameter metadata and `BXSSyscallEntry` vocabulary for context/parameter state. `BXSSyscallModule` diagnostics explicitly mention syscall IDs, symbols, entries, and a call array.

No claim is made that every XS function uses one universal dispatch mechanism.

## AIExpert / rule-engine model

The rule-engine evidence remains at the native-vocabulary/architecture level: rule loading, fact/action definition, indexed rule elements, debug metadata, persistent-fact evaluation, sorted rules, groups, and rule timing are established. The implementation bridge from rule evaluation to action/order issuance remains open.

## UnitAI model

Native vocabulary continues to support separate order, action, target, notification, search, retry, and recovery concepts. The next promotion target remains a concrete state mutation chain showing a native read/branch/write followed by a subsequent consumer.

## Repository position

The public tree remains suitable for practical development, while historical source-derived material remains controlled exposure rather than certified-clean history. Native archaeology artifacts that contain malformed or unverified disassembly remain quarantined.

## Immediate next sequence

1. Identify a concrete `BXSSyscallModule` registration site.
2. Follow symbol insertion and syscall-ID assignment.
3. Recover the call-array relationship and final callable target.
4. Independently recover a `BXSSymbolTable` lookup.
5. Recover a `BXSFunctionEntry` `mCodeOffset` consumer.
6. Recover activation-record PC mutation.
7. Recover UnitAI `CurrentAction` or `CurrentOrder` mutation.
8. Recover AIExpert rule execution into an action/order request.
9. Run a runtime experiment against one recovered path.
10. Update atomic facts and predictive tests from demonstrated results.

## Status rule

The 88% estimate is a working progress estimate, not a completion claim. Layer 1 reaches completion only when the predictive machine-understanding gate is satisfied and material critical paths no longer depend on unacknowledged black boxes.
