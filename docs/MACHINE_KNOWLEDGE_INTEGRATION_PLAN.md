# Machine Knowledge Integration Plan

The preservation packet is now large enough that the principal remaining risk is fragmentation. The next engineering task is to connect the artifacts into a traversable evidence graph.

## Integration sequence

1. Populate the complete UP primitive ledger from preserved source/runtime evidence.
2. Link every important machine claim to one or more evidence records.
3. Link evidence records to ontology entities.
4. Link ontology entities to architectural consequences.
5. Link consequential actions to command/postcondition records.
6. Link failure classes to recovery behaviors.
7. Link experiments to claims they confirm or weaken.
8. Link replay observations to machine snapshots where applicable.
9. Execute the independent re-entry examination.
10. Convert stable invariants into automated tests.

## Desired graph

`artifact → observation → evidence record → ontology entity → claim → invariant → architecture requirement → implementation contract → experiment → runtime result`

## Integration quality gate

No major architectural requirement should remain without a backward evidence path. No major machine claim should remain without an identified architectural consumer or an explicit reason that it is currently informational only.

## Strategic bridge

Once the machine graph is sufficiently integrated, Layer 2 can treat Layer 1 as a typed execution substrate. Strategy should express desired state transitions and capabilities; the implementation layer should compile those intentions through the machine contracts rather than bypass them.
