# ABI State Registry

Every AEGIS state field must carry:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

| Field | Type | Owner | Writer | Readers | Lifecycle | Evidence | Status |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | UNREGISTERED |

## State discipline

- **VALID** says whether the payload is usable.
- **OWNER** identifies the sole authoritative writer/controller.
- **GENERATION** prevents stale observations from masquerading as current state.
- **STAGE** identifies the lifecycle position.
- **PAYLOAD** is typed data, not an untyped scratch number.
- **EVIDENCE_LEVEL** records how the state was established.

A field is not complete until its writer/readers and lifecycle are explicit.
