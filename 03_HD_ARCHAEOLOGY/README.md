# 03 — HD AI Forensic Archaeology

## Mission

This directory preserves the recovered **AI (HD version).per** as an archaeological
artifact and reconstructs the design knowledge embedded in it. The objective is
not to produce a cleaner clone. The objective is to make the artifact returnable:
a future engineer should be able to recover not only what the code does, but why
its authors likely structured it this way, what constraints they were compensating
for, what assumptions they made about the game, and which conclusions are proven,
inferred, historical, or unresolved.

## Research unit

The basic unit of analysis is not the line or even the `defrule`. It is the
**control event**:

> observation → classification → state write → authority effect → action /
> resource consequence → temporal guard → reassessment

Rules are evidence for these events. Multiple rules may instantiate one principle;
one rule may participate in several control loops.

## Required forensic questions

Every major subsystem should answer:

- **Who:** Which author/module/rule family owns the decision? Which other modules
  read, modify, override, or depend upon it?
- **What:** What state is observed, represented, transformed, and acted upon?
- **When:** What age, game-time, timer, interval, event, or transition permits it?
- **Where:** In which source section/module/goal/SN/timer/action domain does it live?
- **Why:** What strategic, economic, tactical, or engine-level rationale best
  explains the implementation?
- **How:** What exact predicates and actions implement the mechanism?
- **Failure:** What happens when the assumptions fail? Is there a reset, timeout,
  fallback, competing writer, or silent degradation?
- **Evidence:** What supports the interpretation and what would falsify it?

## Epistemic discipline

Use explicit labels:

- `CONFIRMED` — directly established by source syntax/comments or independently
  verified engine evidence.
- `PROBABLE` — repeated executable structure with strong semantic consistency.
- `PLAUSIBLE` — useful causal interpretation not yet independently validated.
- `UNCERTAIN` — evidence insufficient.
- `OBSOLETE` — source itself marks behavior as obsolete/unused.
- `ENGINE-SPECIFIC` — conclusion depends on AoE2/UP implementation details.
- `HISTORICAL` — explains development lineage rather than current semantics.
- `DISPROVEN` — contradicted by stronger evidence.

Never silently promote an inference to fact.

## Source hierarchy

1. Exact recovered source text.
2. Source comments and named semantic constants.
3. Repeated executable patterns.
4. Independent V3/PORPHYRA evidence.
5. Replay observations.
6. Native-engine evidence.
7. General AoE2 knowledge.

When sources disagree, preserve the disagreement and record the adjudication.

## Deliverable standard

A completed subsystem should permit reconstruction from the repository without
requiring the original analyst's memory. Preserve source excerpts by reference,
line ranges, hashes, state diagrams, writer/reader graphs, causal explanations,
known exceptions, historical artifacts, and implementation consequences.
