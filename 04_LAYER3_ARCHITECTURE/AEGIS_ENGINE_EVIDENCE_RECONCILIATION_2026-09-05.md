# AEGIS — Engine Evidence Reconciliation

**Date:** 2026-09-05  
**Status:** ACTIVE EVIDENCE REGISTER

## Key conclusions

1. AoE2DE scripting behavior is demonstrably mutable across updates.
2. Search semantics have historically required fixes, including stacked search behavior and pending-object visibility.
3. Focus/target facts have historically required correctness fixes.
4. Object-data fields have historically required correctness fixes.
5. Some scripting commands have changed accepted argument behavior or edge cases.
6. Therefore AEGIS must qualify semantics on the installed build rather than treat historical documentation as a permanent ABI.

## Evidence-to-gate mapping

| Official evidence | AEGIS consequence |
|---|---|
| Update 39284 search stacking fixes | Q-07 search isolation |
| Update 39284 focus/target fact fixes | Q-02 typed fact semantics |
| Update 39284 pending-object search behavior | Q-09 lifecycle |
| Update 37650 unavailable-unit object-type-data support | Q-02/Q-06 object/fact semantics |
| Update 47820 training edge-case and search behavior fixes | Q-02/Q-07/Q-09 |
| Update 177723 players-unit-type-count/object-data/exploration fixes | Q-02/Q-07/Q-09/Q-12 |
| Update Preview 125283 goals 512→16000 | Q-02 goal namespace |

## Engineering disposition

These sources are strong evidence that the selected gates are not theoretical bureaucracy: they correspond to real engine behavior that has changed or required correction historically.

They still do not establish the exact semantics of the current installed build for every gate. Those require target-build evidence.
