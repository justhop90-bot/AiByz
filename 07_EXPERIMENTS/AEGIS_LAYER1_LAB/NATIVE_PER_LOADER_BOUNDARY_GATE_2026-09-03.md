# AEGIS Layer 1 — Native .per Loader Boundary Gate — 2026-09-03

## Question
Can the exact retail executable provide evidence that pure `.per` / `.per2` files are parsed by a native AI loader, and can we safely connect that loader to the runtime AI without guessing?

## Build
- AoE2DE_s.exe 101.103.48987.0 / #180059 / Steam build 24094652.
- SHA-256 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.

## Method
Immutable static extraction of exact-build ASCII strings. No executable modification, injection, hooks, debugger attachment, memory modification, arbitrary network traffic, or XS. No unverified script execution.

## Findings
The executable contains repeated native parser diagnostics beginning with `Parsing script %s`, a native `Failed to setup script %s` diagnostic, `loadRules for listId=%d, file=%s`, and `AI file must have at least one rule`. The same binary contains `.per` and `.per2` literals.

Observed offsets:
- `loadRules for listId=%d, file=%s`: 52207960
- `AI file must have at least one rule`: 52208003
- `.per2`: 52208060
- `.per`: 52208052
- first `Failed to setup script`: 52943407
- repeated `Parsing script %s` diagnostics begin at 52940807.

These strings are materially stronger than generic `.per` vocabulary because they form a coherent native parser/error surface: a script is parsed, rule loading is attempted, empty-rule validation exists, and setup can fail. The evidence is still structural; offsets alone do not identify the containing function or prove that a specific user-supplied file reached the loader.

## Disposition
CONFIRMED: exact executable contains a native `.per/.per2` script-parser diagnostic surface.
CONFIRMED: native rule-loading diagnostic exists.
CONFIRMED: native empty-rule validation exists.
NOT ESTABLISHED: exact containing function address/control flow.
NOT ESTABLISHED: filesystem path selected for the active AI.
NOT ESTABLISHED: a controlled user `.per` reached this parser.
NOT ESTABLISHED: parser success causes a known rule to execute.
NO Layer 1 causal promotion.

## Security
No unsafe instrumentation was used. We deliberately stopped at immutable evidence rather than attempting to inject or attach to the process. Pure `.per` architecture remains unchanged; XS remains excluded.

## Next discriminating gate
Resolve the containing native function(s) for `loadRules`, `Parsing script`, and `Failed to setup script` using a PE-aware disassembler database. Then establish the legitimate AI-file selection path and design the smallest possible harmless `.per` sentinel that can be loaded without modifying installed game files.
