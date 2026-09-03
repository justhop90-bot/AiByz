# AEGIS Layer 1 — Native Scheduler Recovery Pass

Date: 2026-09-03
Status: investigation / no causal promotion
Build: 101.103.48987.0
Executable SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4

## Question
Can the native AI rule-list execution boundary be recovered without the Scenario Editor test path?

## Work performed
1. Shelved automated Scenario Editor testing as a primary Layer 1 route.
2. Re-ran static archaeology against the exact controlled executable.
3. Verified .text/.rdata/.data/.pdata section geometry with PE parsing.
4. Re-tested the historical AIExpert RunList signature from FLWL/aoe2-ai-module.
5. The historical signature produced 0 matches in the current executable.
6. Re-tested direct RIP-relative references to current AIExpertEngine diagnostic strings; 0 direct code references.
7. Built a .pdata-derived function interval index from the current executable.
8. Corrected the earlier whole-.text Capstone approach: mixed/data regions cause disassembly to stop early; function ranges must be disassembled individually.
## New external comparative evidence
FLWL/aoe2-ai-module is historical (last source push 2021) and is not current-runtime proof. Its DE branch nevertheless exposes a useful architecture lead:
- AIExpert::RunList is represented as (AIExpert*, int listId, void* statsOutput).
- The project resolves a DE RunList function dynamically by byte signature.
- Its detoured RunList calls the original FuncRunList and then processes its own command queue.
- Its DE AIExpert structure contains maxStrings/numStrings/string, maxFacts/numFacts/fact/factNames, maxActions/numActions/action/actionNames.
- Its AIFact structure contains type, touched, lastResult, argc, factFn and argument-type fields.
- Its fact loader maps each DE fact name to the native fact function pointer and argc.

## Current-build findings
The 2021 RunList signature has 0 matches in the exact current executable, so it cannot be reused as a current address claim.
The current binary contains the AIExpertEngine/loadRules and persistent-fact diagnostic strings, but a corrected .text RIP-relative scan finds 0 direct references to those string addresses/ranges.
Raw pattern mapping found many generic RCX-field accesses; apparent matches at offsets 0x18/0x20/0x38/0x40 were inspected and are not proven AIExpert objects because the same functions also access unrelated offsets such as 0x50/0x68/0x70.
Therefore no function has been promoted as current RunList, loadRules, or scheduler code.

## Interpretation
The strongest next static route is not string-xref chasing. It is current-build structural recovery: use .pdata function boundaries, instruction-level object-field signatures, call graphs, and data/function-pointer relationships to identify the native AIExpert/AIExpertEngine object and its rule-list execution routine.

## Promotion decision
No causal promotion. Historical RunList/fact structure is comparative evidence only.

## Next discriminating test
Recover candidate functions by combining: (1) AIExpert field-layout signatures where independently supported, (2) caller/callee structure, (3) native AIExpert construction/loadRules context, and (4) current-build execution/log evidence if available. Reject candidates that cannot be tied to AIExpert state.
