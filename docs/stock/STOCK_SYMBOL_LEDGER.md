# Stock Symbol Ledger

Machine-readable source of truth remains the dated A1 inventories under `docs/MACHINE_EVIDENCE/`.

This living ledger records the required dimensions for each symbol:

| Symbol | Kind | Numeric value | Defining source | Readers | Writers | Context/type | Evidence | Status |
|---|---|---:|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | UNREGISTERED |

## Rule

Do not copy a numeric symbol into an AEGIS implementation until its channel type, context, owner, lifecycle, and collision status are explicit.

The large A1 declaration and collision inventories remain the raw evidence layer; this file is the curated engineering interface to those inventories.
