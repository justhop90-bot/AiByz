# Layer 1 Deep QC Pass — XS Metadata, Symbol Table, and Syscall Architecture

Date: 2026-09-02
Status: active investigation; Layer 1 remains incomplete

## Executive assessment

This QC pass re-examined the previous metadata-addressing result at byte level and then widened the inspection around the same native corpus rather than starting another broad executable-wide search.

The most important new finding is that the apparent API metadata region sits inside a much richer native XS subsystem vocabulary than the previous pass recorded.

The binary contains source/debug vocabulary for a coherent family of XS implementation units:

- xsactivationrecord.cpp
- xsdata.cpp
- xsfileentry.cpp
- xsfunctionentry.cpp
- xsruleentry.cpp
- xsrulemodule.cpp
- xsruntime.cpp
- xssource.cpp
- xssymboltable.cpp
- xssyscallentry.cpp
- xssyscallmodule.cpp
- xsuserclassentry.cpp
- xsvariableentry.cpp

This materially strengthens the architectural model of XS as a runtime with explicit source, symbol, function, rule, syscall, variable, data, and activation-record structures.

The evidence does not yet recover the exact native call graph. The correct promotion is therefore architectural/native-vocabulary evidence, not implementation closure.

## 1. Major correction: the metadata problem is larger than an API string table

The previous pass correctly rejected the simplistic model:

API name -> direct RIP reference -> handler

The new corpus provides a much stronger alternative research model:

XS source/signature vocabulary
  -> symbol representation
  -> symbol table
  -> function/syscall entry
  -> syscall module / call array
  -> runtime execution

This is still a hypothesis about the exact data flow. What is now directly established is that the shipped binary contains explicit native vocabulary for each of the intermediate conceptual layers.

## 2. New native source-unit evidence

The inspected source-path corpus contains hundreds of embedded PhoenixBuilders source paths. There were 565 observed occurrences of the PhoenixBuilders-11 path prefix in the current binary scan.

Within the relevant XS region, adjacent source/debug records identify a particularly informative sequence:

xsactivationrecord.cpp
xsdata.cpp
xsfileentry.cpp
xsfunctionentry.cpp
xsruleentry.cpp
xsrulemodule.cpp
xsruntime.cpp
xssource.cpp
xssymboltable.cpp
xssyscallentry.cpp
xssyscallmodule.cpp
xsuserclassentry.cpp
xsvariableentry.cpp

The ordering itself is not proof of compilation-unit dependency or runtime call order. It is nevertheless valuable because it establishes that these concepts coexist in one native XS implementation corpus.

## 3. Function-entry structure discovered

The native vocabulary surrounding xsfunctionentry.cpp exposes:

- mSymbolID
- mReturnType
- mCodeOffset
- mNumberParameters
- mMutable
- mVariables

The presence of mCodeOffset is particularly important.

It creates a competing explanation for apparent code-address values in nearby metadata: an executable relationship may be represented through a function-entry structure and code offset rather than through a direct pointer embedded beside every API name.

Therefore the previous candidate value 0x1417ff3e0 must remain quarantined. Its location inside .text is not enough to establish handler identity.

A future test should determine whether mCodeOffset is stored as an offset, VA, RVA, index, or another representation in actual function-entry instances.

## 4. Symbol-table structure discovered

The xssymboltable.cpp corpus exposes:

- symbolLength
- mSymbol
- mHashTableSize
- mNumberSymbols
- mInvalidValue
- mInvalidType
- entryCount
- mSymbolsByID

This is the strongest new clue in the pass.

The existence of both a hash-table size and symbols-by-ID vocabulary makes an indexed and/or hashed symbol-resolution mechanism substantially more plausible than a linear scan of API strings.

Still unproven:

- hash function
- bucket representation
- symbol-entry structure
- ID assignment policy
- collision handling
- lookup function
- whether syscall names use the same table as user functions
- whether IDs are stable across saved runtime state

## 5. Syscall-entry structure discovered

The xssyscallentry.cpp corpus exposes:

- mContext
- mCallerContext
- mParameters
- mParameters.getNumber()

This establishes a native syscall-entry abstraction with explicit execution context and parameter storage vocabulary.

This is highly relevant to XS API execution because the inspected API corpus consists of script-visible syscall-like functions such as xsGetGoal, xsSetGoal, xsGetStrategicNumber, xsSetStrategicNumber, xsGetMapSeed, and xsGetTechAttribute.

It does not yet prove that every xs-prefixed function is represented by BXSSyscallEntry. That mapping requires a registration trace.

## 6. Syscall-module structure discovered

The xssyscallmodule.cpp corpus exposes:

- mSyscalls
- mAddSymbols
- mStoreHelp
- number of syscalls
- save/load of syscall entries

More importantly, diagnostics state that the native subsystem can:

- create a syscall entry
- add a symbol for a syscall
- find an expected syscall symbol
- add an entry to the call array
- set a syscall ID for a symbol
- reject a syscall with an invalid type ID
- reject an unavailable/nonexistent syscall
- preserve compatibility information across save/load

These diagnostics are unusually valuable because they describe relationships between symbols, syscall IDs, entries, and a call array.

They still do not reveal the exact implementation function boundaries.

## 7. New practical dispatch model

The best current model is now:

script symbol/name
    |
    v
symbol table
    |
    +--> symbol ID / metadata
    |
    v
syscall or function entry
    |
    +--> parameter/type/context metadata
    |
    +--> function code representation where applicable
    |
    v
call-array / dispatch representation
    |
    v
XS runtime

This is an architectural model with mixed evidence levels. The existence of the named structures is native-vocabulary evidence; the arrows require implementation tracing.

## 8. Important distinction: function entry versus syscall entry

The corpus now provides enough evidence to keep two mechanisms separate in the research model:

A. Function-entry path

symbol ID -> return type -> code offset -> parameters/variables -> execution

B. Syscall-entry path

symbol -> syscall ID -> syscall entry -> context/parameters -> call array -> runtime

These may share symbol infrastructure while having different execution mechanisms.

Do not collapse them into one universal function-pointer table without proof.

## 9. Runtime structure discovered

The xsruntime.cpp corpus exposes:

- mSyscalls
- mSource
- mDatas
- mInstanceLimit
- mCaseSensitive
- mWarningsOn
- mInfoMessagesOn
- mRunMessagesOn
- mListInterpreter
- mListFunctionEntry
- mGenerateListing
- mDebugTokenizer
- mDebugCode
- temporary IDs
- source and syscall save/load

This provides a much richer native runtime boundary than previously documented.

A particularly useful future question is whether mListInterpreter, mListFunctionEntry, and mSyscalls are runtime registries, debug/listing structures, or both.

## 10. Source subsystem structure

The xssource.cpp corpus exposes:

- mFiles
- mCodeSize
- mCode
- numberFiles

The xssource representation therefore appears to distinguish source files from compiled/interpreted code storage.

This creates a new investigation path:

source file entry
  -> source ID/file ID
  -> code representation
  -> function entry code offset
  -> runtime execution

The exact relationship remains open.

## 11. XS file-entry and source-line evidence

The xsfileentry.cpp corpus exposes:

- mFilenameLength
- mFilename
- mSourceLength
- mSource
- mSourceLines

This means source-level debugging information is represented as explicit runtime/native data rather than merely being an external development artifact.

Practical implication: source-line and function metadata may provide an alternative route for identifying function boundaries when ordinary string xrefs fail.

## 12. Rule subsystem gets an additional structural anchor

The same XS corpus exposes:

xsruleentry.cpp:
- mPriority
- mMinInterval
- mMaxInterval
- mLastExecuteTime
- mActive
- mRunImmediately
- mGroups

xsrulemodule.cpp:
- mRules
- mSortedRules
- mRuleGroups
- mNextSortedRuleIndex

This is substantially stronger than generic rule vocabulary. It shows that rule state, sorted-rule state, group membership, and execution timing are represented as explicit native data members in the binary's source/debug vocabulary.

The exact scheduler algorithm remains unproven.

## 13. Activation-record evidence

xsactivationrecord.cpp exposes:

- mFunctionID
- mStack
- mHeap
- mPC
- mLineNumber
- mBreakpoint
- mStepOverBreakpoint

This is one of the most consequential findings of the pass.

It indicates a native execution/debugging model with an explicit program counter, stack, heap, function ID, and source line state.

Therefore the XS interpreter should no longer be conceptualized merely as a collection of callback functions. A VM/interpreter-style execution state is now strongly supported at the vocabulary level.

Exact instruction format, bytecode representation, PC semantics, stack-frame ownership, and interpreter dispatch remain open.

## 14. Variable and user-class structures

xsuserclassentry.cpp exposes variable storage and serialization.

xsvariableentry.cpp exposes:

- mModifiers
- dataLength
- raw data storage

This supports a broader model in which script variables, user classes, functions, rules, and runtime activation records are separate native structures.

Do not yet infer a specific C++ inheritance hierarchy from these names.

## 15. Strong new causal hypothesis

The accumulated evidence now supports testing the following causal architecture:

LOAD
  -> tokenize/parse
  -> source/file registration
  -> symbol registration
  -> function/rule/syscall registration
  -> ID assignment
  -> code/rule representation construction
  -> runtime installation
  -> evaluation/interpreter dispatch
  -> state mutation / syscall execution

This is not yet a recovered call graph.

It is the highest-value experimental architecture to test next because multiple independent native structures line up with its stages.

## 16. Reinterpretation of the candidate code address

The previous candidate 0x1417ff3e0 remains quarantined.

New evidence actually makes premature promotion less appropriate, not more appropriate.

Why:

- function entries have explicit mCodeOffset vocabulary;
- syscall entries have a separate syscall ID/call-array vocabulary;
- symbol tables have ID-oriented storage;
- runtime owns syscall state;
- the candidate appears only once in the tested raw binary;
- bytes at the candidate address do not establish a conventional callable function boundary.

The correct question is no longer “is this the handler?”

It is:

“What native record, if any, contains the executable representation corresponding to xsGetTechAttribute, and how is that representation consumed?”

## 17. New metadata research strategy

The next metadata pass should not search only for API names.

It should search for structural signatures around:

- mSymbolID
- mCodeOffset
- mReturnType
- mNumberParameters
- mHashTableSize
- mNumberSymbols
- mSymbolsByID
- mContext
- mCallerContext
- mParameters
- mSyscalls
- mAddSymbols
- mStoreHelp
- call array
- syscall ID

The objective is to find a native function that reads or writes one of these fields.

## 18. Highest-value experiment: syscall registration

Find one registration operation for a known API such as xsGetGoal or xsGetMapSeed.

Required evidence chain:

symbol string
 -> symbol-table entry
 -> syscall ID
 -> syscall entry
 -> call-array slot
 -> native callable target

A single complete chain would dramatically reduce uncertainty across the entire XS capability surface.

## 19. Highest-value experiment: function-entry registration

Find one script-defined function rather than a built-in syscall.

Required chain:

function symbol
 -> BXSFunctionEntry
 -> mSymbolID
 -> mCodeOffset
 -> activation record / PC
 -> interpreter execution

This would independently test the function-entry branch and establish whether it shares symbol infrastructure with syscalls.

## 20. Practical AEGIS implication

The correct future capability registry should not be modeled as:

name -> guessed native address

The machine evidence now points toward a more robust abstraction:

capability name
 -> build-qualified symbol identity
 -> capability class (syscall/function/rule/etc.)
 -> registration identity
 -> validated parameter contract
 -> dispatch representation
 -> verified handler

This is directly useful to the eventual ByzBot implementation because it allows capability qualification to remain build-specific and evidence-backed.

## 21. UnitAI implication

The XS findings reinforce a broader methodological point: script-visible APIs, AIExpert rules, and UnitAI execution should not be assumed to share one dispatch layer merely because they eventually affect the simulation.

Research should explicitly distinguish:

script VM state
AIExpert rule state
UnitAI execution state
simulation state

and then recover the bridges between them.

## 22. Corrections to previous pass

Correction 1:
The previous pass described the inspected binary fields as metadata adjacent to the API corpus. That remains correct, but the new evidence shows that the surrounding native subsystem includes explicit symbol-table and syscall-module concepts. The term “metadata” should therefore not imply a passive table.

Correction 2:
The previous pass treated the candidate .text-range value as a possible handler field. It remains a candidate field, but mCodeOffset and syscall-ID/call-array evidence now provide competing representations. It must stay quarantined.

Correction 3:
The direct-reference negative result is useful only as a representation constraint. It must not be interpreted as evidence that the APIs lack native consumers.

Correction 4:
The XS subsystem should now be modeled as a potential interpreter/runtime architecture, not merely an API registry, until disproven.

## 23. What can be extrapolated safely

High-confidence extrapolations:

1. XS has explicit internal state for source, symbols, functions, rules, syscalls, variables, and runtime execution.
2. Symbol identity is likely important to multiple XS subsystems because symbol IDs and symbol tables are explicit native concepts.
3. Built-in syscall dispatch likely has more structure than a direct string-to-pointer lookup because syscall IDs, entries, parameters, and a call array are explicitly represented in diagnostics.
4. Script-defined function execution likely has a different representation from built-in syscall execution because BXSFunctionEntry exposes code-offset state while BXSSyscallEntry exposes context/parameter state.
5. Debugging facilities are deeply integrated with execution state through activation records, PC, stack, heap, source line, and breakpoint state.

Low-confidence hypotheses requiring tests:

1. One global symbol table serves functions and syscalls.
2. Syscall IDs index a fixed call array.
3. mCodeOffset is an offset into mCode.
4. Function IDs map directly to activation records.
5. API names are registered once at runtime initialization.
6. Rule IDs and syscall IDs share an ID allocator.

None of these low-confidence hypotheses should enter implementation as machine fact.

## 24. New falsification matrix

| Hypothesis | Falsifier | Required evidence |
|---|---|---|
| Symbols use a hash table | registration performs only linear scan | native lookup routine |
| Syscall IDs index call array | ID is not used as array/index key | registration/dispatch trace |
| mCodeOffset addresses mCode | offset resolves outside code storage | concrete function entry |
| Syscalls share symbol table | separate unrelated symbol registry | registration trace |
| Function entries use interpreter PC | function execution bypasses activation records | runtime/native trace |
| Rule state lives in BXSRuleEntry | rule scheduler uses unrelated transient state | scheduler mutation chain |
| Runtime owns syscall dispatch | another subsystem performs final dispatch | call graph |

## 25. Evidence promotion status

PROMOTED:

- native XS source-unit family includes symbol, function, syscall, rule, source, runtime, activation-record, variable, and data components;
- BXSFunctionEntry vocabulary includes symbol ID and code offset;
- BXSSymbolTable vocabulary includes hash-table and symbols-by-ID state;
- BXSSyscallEntry vocabulary includes context and parameter state;
- BXSSyscallModule vocabulary includes syscall storage and call-array registration diagnostics;
- BXSRuntime vocabulary includes syscall/source/data registries and interpreter/debug state;
- BXSActivationRecord vocabulary includes PC, stack, heap, function ID, and source line;
- rule-entry/module structures explicitly expose scheduler-relevant state.

QUARANTINED:

- candidate 0x1417ff3e0 as a specific handler;
- exact data-structure layout;
- exact ownership relationships;
- exact hash/ID algorithms;
- exact syscall call-array layout;
- exact interpreter dispatch loop;
- exact runtime initialization order;
- exact rule-to-UnitAI bridge.

REJECTED:

- API-string direct-xref search as a sufficient dispatch-recovery method;
- raw offset plus image base as a valid universal address conversion;
- treating source-path adjacency as proof of runtime call order.

## 26. Updated Layer 1 priority

The highest-value native investigation is now:

1. recover one BXSSyscallModule registration path;
2. recover one BXSSymbolTable lookup path;
3. recover one syscall-ID to call-array relationship;
4. recover one BXSSyscallEntry execution path;
5. separately recover one BXSFunctionEntry code-offset path;
6. recover one activation-record PC transition;
7. return to UnitAI state mutation;
8. connect AIExpert rule execution to an action/order request.

This ordering is preferable to another broad string scan because it seeks implementation edges with maximum architectural leverage.

## Final QC verdict

The previous pass was directionally correct but materially underestimated how much structure was encoded around the XS API corpus.

The newly recovered source/debug vocabulary exposes an entire native subsystem family: source management, symbol resolution, function entries, syscall entries/modules, rule entries/modules, runtime state, activation records, variables, and data.

The most important practical conclusion is that the XS boundary is probably not a simple name-to-function-pointer table. It is a structured runtime with identity, registration, dispatch, execution, and debugging state.

That is a major increase in Layer 1 understanding, but it is not yet implementation closure.

The next decisive artifact should be a **single recovered registration-to-dispatch chain**, preferably for `xsGetGoal` or `xsGetMapSeed`, followed by a separate UnitAI state mutation chain.
