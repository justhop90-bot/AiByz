# Rule-Site Extraction Schema — 2026-09-08

This schema is the next static deconstruction unit. It prevents the project from stopping at file-level or symbol-level summaries.

## Record schema

| Field | Required | Meaning |
|---|---|---|
| `RULE_ID` | yes | Stable identifier derived from source file + rule sequence. |
| `SOURCE_FILE` | yes | Exact source artifact. |
| `SOURCE_LINE_START` | yes | First source line. |
| `SOURCE_LINE_END` | yes | Last source line. |
| `ACTIVATION_PREDICATE` | yes | Effective lexical `load-if`/conditional context known statically. |
| `READ_GOALS` | yes | Goals read or compared. |
| `WRITE_GOALS` | yes | Goals mutated/set. |
| `RESET_GOALS` | yes | Goals explicitly reset/reconciled. |
| `READ_SN` | yes | Strategic numbers read. |
| `WRITE_SN` | yes | Strategic numbers mutated/set. |
| `RESET_SN` | yes | Strategic numbers explicitly reset/reconciled. |
| `TIMERS` | yes | Timer channels touched. |
| `FACTS` | yes | Facts/query primitives used. |
| `OBJECT_DATA` | yes | Object-data fields used. |
| `SEARCH_STATE` | yes | Search/object state created or consumed. |
| `ENGINE_ACTION` | yes | Engine-facing action family, if any. |
| `DOWNSTREAM_CONSUMERS` | yes | Known static consumers of the resulting state. |
| `FAILURE_RECOVERY` | yes | Failure, retry, reset, or fallback relationship. |
| `MODULE_ROLE` | yes | Reconstructed subsystem responsibility. |
| `EVIDENCE_STATUS` | yes | OBSERVED / CORRELATED / INFERRED / etc. |
| `TARGET_RUNTIME_STATUS` | yes | RUNTIME-QUALIFIED or UNKNOWN where applicable. |

## Extraction rules

1. Preserve exact source line numbers.
2. Never infer a state owner from a single write.
3. Record both positive and negative conditional activation.
4. Keep engine action distinct from strategic intent.
5. Treat reset/reconciliation as first-class mutations.
6. Preserve unresolved timing semantics explicitly.
7. Link every extracted state mutation to its downstream consumers where statically discoverable.
8. Do not rewrite source while extracting it.

## Rule identity

Recommended stable form:

```text
<FILE_BASENAME>:R<ORDINAL>
```

Example:

```text
buildings:R00421
```

Line numbers remain separate because edits to a reconstruction copy must not silently change identity.

## Activation representation

Represent lexical conditions as an ordered stack, for example:

```text
BYZANTINE-CIV
AND NOT DEATH-MATCH
AND DIFFICULTY-HARD
```

Do not collapse this into a Boolean “active” flag. The purpose is to preserve the conditions under which the historical rule exists.

## Consumer linkage

Consumer linkage should use stable rule IDs when possible:

```text
units:R00217
  → goal:unit-goal
  → buildings:R00421
  → tsa:R00803
```

If the consumer cannot be established statically, record `UNKNOWN` rather than guessing.

## Runtime boundary

This schema intentionally has two separate statuses:

- `EVIDENCE_STATUS` describes what the source/evidence establishes.
- `TARGET_RUNTIME_STATUS` describes whether target-build interpreter behavior has been qualified.

Static source archaeology must never upgrade a rule to runtime-qualified merely because its syntax is valid.
