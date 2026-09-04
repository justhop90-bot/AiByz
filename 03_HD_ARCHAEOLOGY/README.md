# 03 — HD AI Forensic Archaeology

## Mission

This directory preserves the recovered **AI (HD version).per** as an archaeological artifact and reconstructs the design knowledge embedded in it. The objective is not to produce a cleaner clone. The objective is to make the artifact returnable: a future engineer should be able to recover what the code does, why its authors likely structured it this way, what constraints they were compensating for, what assumptions they made about the game, and which conclusions are proven, inferred, historical, or unresolved.

## Research unit

The basic unit of analysis is not the line or even the `defrule`. It is the **control event**:

> observation → classification → state write → authority effect → action / resource consequence → temporal guard → reassessment

Rules are evidence for these events. Multiple rules may instantiate one principle; one rule may participate in several control loops.

## Required forensic questions

Every major subsystem should answer:

- **Who:** Which author/module/rule family owns the decision? Which other modules read, modify, override, or depend upon it?
- **What:** What state is observed, represented, transformed, and acted upon?
- **When:** What age, game-time, timer, interval, event, or transition permits it?
- **Where:** In which source section/module/goal/SN/timer/action domain does it live?
- **Why:** What strategic, economic, tactical, or engine-level rationale best explains the implementation?
- **How:** What exact predicates and actions implement the mechanism?
- **Failure:** What happens when the assumptions fail? Is there a reset, timeout, fallback, competing writer, or silent degradation?
- **Feedback:** What observable world state proves success, failure, or changed conditions?
- **Evidence:** What supports the interpretation and what would falsify it?

### Strategy-game extension

The questions above must be answered at the **AoE2 game level**, not only at the code level. For every major decision ask:

`WHO matters -> WHAT capability/relationship changes -> WHEN is the window valuable -> WHERE does it apply -> WHY does the action improve the strategic position -> WHAT IF the opponent changes -> WHAT DOES FAILURE TEACH US?`

The programmer was writing code to play a strategy game proficiently. The reconstruction must therefore recover the game model implicit in the code.

## Epistemic discipline

Use explicit labels:

- `CONFIRMED` — directly established by source syntax/comments or independently verified engine evidence.
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

## Pass structure

### Pass 1 — Explicit knowledge

What does the program explicitly represent and do?

Primary artifact: `HD_EXPLICIT_RECONSTRUCTION_PASS1.md`.

### Pass 2 — Implicit strategic principles

What competitive principles are plausibly encoded by repeated patterns?

Primary artifact: `HD_IMPLICIT_STRATEGIC_PRINCIPLES_PASS2.md`.

### Pass 3 — Meta-knowledge / programmer reconstruction

Why would an experienced AoE2 programmer choose these abstractions, timers, reservations, search loops, fallbacks, and distributed control channels? What game problems are being solved, and which mechanisms are strategy versus engine compensation?

Primary artifact: `HD_META_KNOWLEDGE_PASS3_2026-09-04.md`.

### Pass 4 — State-channel / writer-reader reconstruction

Which strategic state channels exist, who appears to write them, who reads them, what game decision they mediate, and where conflicting writers can destabilize the controller?

Primary artifact: `HD_STATE_CHANNEL_GRAPH_PASS4_2026-09-04.md`.

This pass converts the programmer-mind reconstruction into an explicit logical architecture and identifies the highest-value end-to-end causal chains for the next investigation.

### Practical coding catalogue

The archaeology is now paired with `AOE2DE_PRACTICAL_CODING_KNOWLEDGE_BASE.md`, which starts from common AoE2 game problems and records what the historical HD/Promisory code needed to solve them, the coding patterns used, and the AEGIS generalization.

`AOE2DE_STRATEGIC_PROBLEM_MATRIX.md` provides the compact problem-first lookup table.

## Practical reconstruction standard

A future engineer should be able to answer, for any important behavior:

> What activates it? What state does it consume? What state does it create? What resources does it protect or spend? What capability does it create? What timing window makes it valuable? What action follows? What timer or reset controls it? What other rules compete with it? What happens when it fails? What strategic problem was it solving? What did the programmer have to approximate because of the rule-machine substrate? What evidence supports the rationale? And what remains unknown?

If the repository cannot answer those questions, the archaeology is incomplete.

## AEGIS boundary

The historical source is a strategic knowledge fossil and engineering case study. AEGIS should preserve the underlying strategic principles while rejecting accidental architecture: distributed state ownership, magic-number semantics, oversized predicates, hidden search state, and assumptions that command issuance equals success.

The target architecture is:

`WORLD -> OBSERVATION -> BELIEF/CLASSIFICATION -> REQUIREMENT -> CAPABILITY CANDIDATES -> RESOURCE/TIMING EVALUATION -> COMMITMENT -> AUTHORIZED ACTION -> POSTCONDITION -> RECOVERY/REASSESSMENT`.
