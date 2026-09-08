# AI Syntax Rules — Compiler-Facing Constitution

**Status:** registry specification; not a claim that every entry is target-build qualified.

Every command entry must eventually contain:

| Field | Requirement |
|---|---|
| Command | Exact command token |
| Canonical syntax | Exact parser-facing form |
| Argument count | Exact arity |
| Argument types | Goal/SN/fact/object/unit/line/class/etc. |
| Accepted symbolic forms | Proven aliases/lines/constants |
| Known invalid forms | Proven rejects or unsafe substitutions |
| Side effects | State mutation / engine action |
| State affected | Exact channel/object/action state |
| Evidence level | A1–A5 |
| Target-build qualification | UNKNOWN / STATIC / RUNTIME / STRESS |

## Rules

1. Never infer syntax from English descriptions.
2. Never infer argument type from numeric coincidence.
3. Unit ID, unit-line ID, unit class, goal, SN, timer, fact ID, and object-data field are distinct types unless evidence proves compatibility.
4. A validator error records validator behavior; it does not prove engine rejection.
5. A command that parses is not thereby semantically safe.
6. Target-build runtime evidence outranks historical documentation.
7. Public documentation is a high-value vocabulary source but cannot clear an ABI channel by itself.

## Initial known boundary cases

- `up-get-focus-fact` is an engine primitive whose exact target-build argument domains must be tracked per fact.
- `unit-type-count` is a fact identifier; its unit operand must be typed separately from class IDs.
- `knight-line` is semantically a unit-line concept, not the same type as concrete unit `knight`.
- `temporary-goal` has context-sensitive numeric legality; storage/set usage must not be conflated with narrower comparison contexts.

This file is intentionally a constitution and schema, not a fabricated exhaustive command table. Detailed command entries should be generated from public reference material plus local stock evidence and then promoted through the evidence ledger.
