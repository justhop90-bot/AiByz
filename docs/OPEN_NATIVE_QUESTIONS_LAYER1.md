# Open Native Questions — Layer 1 — Final Investigation Frontier

**Investigation phase:** CLOSED / HANDOFF  
**Working completion position:** **89%**  
**Completion certification:** NOT SATISFIED

These are not defects in the operational contract. They are the bounded unresolved native questions remaining after the Layer 1 investigation. They are preserved so future work resumes from the actual evidentiary frontier rather than repeating completed vocabulary searches.

## Highest-priority implementation-closure questions

1. Which verified native function produces and stores persistent-fact results?
2. What is the persistent-fact cache/freshness boundary and snapshot cadence?
3. Which verified native function reads, transitions, and writes rule scheduler state?
4. What is the exact scheduler comparator, tie-breaker, interval unit, and rebuild trigger?
5. Which verified native path turns a rule/handler result into an action/order request?
6. Which verified native function mutates UnitAI `CurrentAction` or `CurrentOrder` after acceptance?
7. Which native path carries completion, failure, invalidation, or search-required state back through UnitAI and/or the rule system?
8. Which native boundary connects search candidate selection to target-state mutation?
9. Which native object owns the relevant UnitAI order/action/target/notification state?
10. What runtime experiment can falsify the current fact-refresh and scheduler-cadence hypotheses?

## `.per` implementation frontier

11. Exact minimum/maximum interval units and boundary behavior.
12. Fairness/starvation behavior among eligible rules.
13. Exact group/rule synchronization timing.
14. Trigger versus handler execution boundaries.
15. Intra-handler state visibility and action atomicity.
16. Resource reservation timing relative to feasibility and command issuance.
17. Pending-object lifecycle and cancellation semantics.
18. Target-handle lifetime and invalidation behavior.
19. Search result ordering and stability.
20. AI evaluation tick boundary relative to simulation updates.
21. Hidden scheduler/interpreter state not exposed to scripts.
22. Exact validator/runtime semantic divergences.
23. Loader call graph from AI selection to rule registration.
24. Parser/interpreter boundary for `.per` constructs.
25. Environment-dependent behavior of the AI runtime.
26. Whether machine behavior is deterministic under identical world-state inputs.
27. Fact/action registration timing.
28. Rule navigation state and interaction with sorted scheduling.
29. Action conflict resolution when multiple handlers issue competing requests.
30. Runtime feedback: what state becomes script-visible after native action completion, failure, or invalidation.
31. Required object-identity lifecycle edges: creation, lookup, transformation, garrison, ownership change, removal, reuse, and replay correlation.

## Native structural questions opened by the final pass

32. Which `.pdata`-bounded functions in AIExpert regions access persistent-fact result storage?
33. Which `.pdata`-bounded functions in UnitAI regions access the state fields represented by `CurrentOrder` and `CurrentAction` diagnostics?
34. Can data-flow relationships be recovered even where direct references to diagnostic strings are absent?
35. Which of the 166,730 non-zero runtime-function ranges belong to AIExpert, UnitAI, search, action, or shared infrastructure?
36. Which executable bytes outside the 88.88% aggregate `.pdata` interval coverage represent code, padding, tables, or other structures?
37. Can an authorized PDB matching GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d` and age `1` be obtained and authenticated against the controlled executable?

## Research priority

Prioritize questions by architectural leverage. The first useful result is not the largest recovered subsystem; it is the smallest verified causal edge that closes a dependency:

`read -> condition -> write -> consumer -> observable consequence`

Persistent-fact mutation and `CurrentOrder -> CurrentAction` remain the two highest-value state-transition targets. The rule-to-action bridge and failure/completion propagation follow immediately because they close the strategic-to-tactical feedback loop.

## XS scope

XS and XS qualification are explicitly excluded from the ByzBot implementation and from the Layer 1 completion gate. XS may be investigated as machine archaeology, but it is not a required dependency. Prior XS questions remain preserved as historical archaeology and must not inflate the remaining implementation frontier.

## Methodological boundary

The corrected PE mapping is authoritative for native file-offset conversion. `.rdata` uses RVA `0x313c000` and raw pointer `0x313ac00`; `.pdata` uses RVA `0x4c28000` and raw pointer `0x41d4000`. Treating `VA - imagebase` as a universal raw offset is prohibited.

The latest direct AI-reference tests found zero RIP-relative references to seven selected diagnostic/source anchors and zero exact absolute 64-bit pointer occurrences. This eliminates only those tested representations. It does not prove absence of the underlying subsystem or its indirect/table-mediated references.

The latest metadata-pointer experiment likewise demonstrates that a valid pointer to a `.pdata` function start does not establish semantic API ownership. Direct disassembly of the candidate showed cleanup/destructor-like behavior, so the association was rejected.

## Re-entry rule

Do not restart broad string inventories. Begin with `.pdata` function geometry, identify bounded candidate functions, validate instruction decoding independently, recover state reads/writes, establish callers/callees, and then perform runtime falsification where practical.

A resumed investigation should first read `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md` and `docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md`. The final investigation position remains 89% until a new demonstrated causal edge changes it.
