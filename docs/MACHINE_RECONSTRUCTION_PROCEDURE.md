# Machine Reconstruction Procedure

## Purpose

This procedure defines how a future engineer returns to Layer 1 without depending on memory. It is deliberately procedural: each conclusion must be recoverable from evidence.

## A. Establish build identity

1. Locate the installed executable.
2. Record absolute path, size, timestamps, version metadata, PE architecture, and SHA-256.
3. Bind every native artifact to that identity.
4. Reject evidence whose build provenance is unknown.

## B. Establish script identity

1. Locate the active AI resource root.
2. Identify `.ai` entry files and `.per` source files.
3. Resolve root `load` relationships.
4. Record load order and missing targets.
5. Hash the controlled source tree.
6. Separate stock, canonical control, strategy fossil, experimental, and runtime-candidate material.

## C. Establish lexical machine surface

Search the executable and qualified source artifacts for:

- AI/script vocabulary;
- rule/rule-group vocabulary;
- goals and strategic numbers;
- facts and UP calls;
- timers;
- XS interfaces;
- action/order/target vocabulary;
- validation/error strings;
- loader/file-resolution vocabulary.

Classify every hit before interpreting it.

## D. Recover scheduler semantics

Start with `mCurrentRuleID`, `mRules`, `mSortedRules`, `mNextSortedRuleIndex`, `mPriority`, `mMinInterval`, `mMaxInterval`, `numberRules`, `numberSortedRules`, and `numberRuleGroups`.

Then locate:

1. rule creation;
2. rule registration;
3. rule-group creation;
4. sorting;
5. next-rule selection;
6. activation/deactivation;
7. interval mutation;
8. priority mutation;
9. execution;
10. execution failure.

Do not infer comparator direction until the implementation or controlled behavior demonstrates it.

## E. Recover interpreter semantics

Trace the chain:

`file acquisition -> data buffer -> parser/interpreter -> rule construction -> trigger/handler interpretation -> registration -> scheduler`.

Where source definitions are absent, use Ghidra and runtime evidence. Never substitute similarly named editor/library classes as proof of shipped-runtime behavior.

## F. Recover state semantics

For each goal/SN/timer/fact interface, record:

- identifier;
- producer;
- consumers;
- legal range;
- semantic type;
- persistence/lifetime;
- initialization;
- reset behavior;
- update mechanism;
- downstream consequences;
- evidence class.

This turns the state substrate into a typed ledger instead of an undocumented integer namespace.

## G. Recover UP semantics

Build an API ledger for every used UP primitive. Each entry must distinguish:

`name | category | arguments | argument domains | outputs | side effects | failure modes | reset requirements | evidence`.

Special attention is required for search/filter APIs, unit-line identifiers, player indexes, goals used as output registers, and functions whose valid ranges differ by context.

## H. Recover action semantics

For each consequential action identify:

`intent -> order -> action -> target -> execution -> result -> completion/failure/invalidation -> world-state effect`.

Do not collapse these states.

## I. Recover failure semantics

Map errors into layers:

- lexical;
- interpretation;
- registration;
- scheduling;
- authorization/feasibility;
- execution;
- verification;
- stale belief;
- authority collision.

Every error that can affect AEGIS architecture gets a durable record.

## J. Cross-validate

A high-confidence machine claim should preferably converge across at least two independent evidence classes, and critical claims across three when feasible.

Example:

`XS signature -> script usage -> native implementation`

is materially stronger than:

`string -> interpretation`.

## K. Preserve negative results

Failed searches, missing source definitions, unavailable debugging symbols, and invalid experimental approaches are evidence. They constrain future search strategy and prevent circular rediscovery.

## L. Ghidra discipline

Broad automated analysis is an index-building operation, not semantic proof. Function-repair noise, overlapping functions, thunks, external stubs, and decompiler artifacts must be recorded.

Targeted validation should prioritize:

1. scheduler functions;
2. rule construction;
3. interpreter/trigger/handler dispatch;
4. XS registration;
5. UP dispatch;
6. AI file loading;
7. action execution bridges.

## M. Runtime experiment discipline

A runtime experiment must have:

- hypothesis;
- controlled input;
- exact build;
- exact AI source hash;
- expected observation;
- actual observation;
- interpretation;
- confidence delta;
- rollback/cleanup status.

A successful experiment proves only the behavior tested.

## N. Architecture reconstruction

After machine facts are assembled, derive the machine-compatible architecture. The canonical AEGIS control loop is:

`OBSERVE -> NORMALIZE -> BELIEF -> INTENT -> AUTHORITY -> FEASIBILITY -> EXECUTE -> VERIFY -> MEMORY -> REPLAN`.

Every arrow must correspond to an explicit interface or documented abstraction boundary.

## O. Re-entry test

A future engineer passes Layer-1 re-entry only if they can explain, without conversational context:

1. which executable is authoritative;
2. what the AI script substrate is;
3. how rules are represented and scheduled;
4. how rules are dynamically controlled;
5. how state is represented;
6. how UP observes and acts;
7. how actions report failure/completion;
8. how loader/interpreter uncertainty is bounded;
9. what the validator/runtime distinction means;
10. what is known versus hypothesized;
11. what evidence remains outstanding;
12. why the AEGIS architecture follows from those constraints.

Failure of any of these questions is a documentation deficiency, not permission to guess.
