# AEGIS / AiByz — AI Operating Protocol

**Purpose:** Prevent predictable AI failure modes when researching, modifying, or reviewing this repository.
**Authority:** `main` only. This file supplements `AGENT_SESSION_CONTRACT.md`; it does not override the Final Audit.
**Effective:** 2026-09-10

## 1. Before doing work

1. Read `AGENT_SESSION_CONTRACT.md`.
2. Read `AI_AGENT_START_HERE.md`.
3. Read the current Final Audit named by those documents.
4. Read current `docs/progress/` material relevant to the task.
5. Identify the exact claim, subsystem, file, and gate being worked.
6. Check whether the question is already resolved, superseded, or explicitly blocked.

**Never begin by browsing branches or searching the whole repository indiscriminately.**

## 2. Authority firewall

Only `main` is current authority.

Historical branches, old handoffs, filenames containing `final`/`canonical`/`master`, and plausible-looking source code have no authority by themselves.

When sources disagree:

`Final Audit / current progress` > `current design manual` > `machine evidence` > `historical archaeology` > `inference`.

If the disagreement cannot be resolved, record it as unresolved. Do not choose the prettier or newer-looking answer.

## 3. Evidence firewall

Every nontrivial claim must be mentally tagged:

`CLAIM | SOURCE | EVIDENCE CLASS | WORLD LEVEL | STATUS | FALSIFIER`

Never upgrade evidence merely because multiple documents repeat the same statement. Ten copies of an unsupported claim remain unsupported.

Required distinction:

`declared → loaded → read → written → guarded → commanded → accepted → pending → created → available → effective`

These are separate states unless evidence proves equivalence.

## 4. AI-specific anti-error rules

### A. Do not pattern-complete missing semantics

If code looks like a familiar AoE2 pattern, do not assume it has familiar semantics. State the unknown and identify the minimum evidence needed.

### B. Do not confuse names with identity

`knight`, `knight-line`, IDs, goals, flags, SNs, timers, facts, and object types are not interchangeable because their names or values look related.

### C. Do not confuse repetition with confirmation

Repeated historical text is provenance, not independent evidence.

### D. Do not confuse successful parsing with successful execution

A script that loads or validates is not thereby semantically correct.

### E. Do not confuse command traces with world state

A replay command, queue event, or parser event cannot by itself prove completion or strategic effect.

### F. Do not optimize before correctness gates close

Do not add abstraction, cleverness, caching, generalization, or speculative architecture to compensate for an unproven engine boundary.

### G. Do not resurrect rejected work

`ADprom`, `byzwarcouncil`, XS, scenario-loader automation, and other explicitly rejected paths remain historical evidence unless the current authority explicitly reopens them.

### H. Do not widen scope silently

A task about one subsystem must not become a repository-wide rewrite. Record adjacent findings separately unless they are required to complete the requested gate.

## 5. Work-unit discipline

Every work unit should have exactly one primary objective:

`QUESTION → CURRENT ANSWER → GAP → TEST/EVIDENCE → DECISION → ARTIFACT`

Before editing code, answer:

- What exact behavior am I changing?
- What proves the required inputs and outputs?
- Who owns every state/channel touched?
- What resets it?
- What happens on failure?
- What evidence would falsify this design?

## 6. Stop conditions

Stop and report instead of guessing when:

- authority documents conflict;
- a required ABI allocation is unproven;
- ownership is ambiguous;
- runtime load is conditional and unresolved;
- command lifecycle is inferred rather than observed;
- a change would alter stock-runtime assumptions;
- a historical branch is the only support for a current architectural claim;
- the proposed fix requires semantics not established by evidence.

## 7. Change discipline

Prefer the smallest reversible change that closes a named gap.

For production-oriented `.per`:

`evidence → ownership/ABI gate → lifecycle gate → candidate implementation → qualification → promotion`

Candidate modules under `implementation/` are not production roots unless current authority explicitly says otherwise.

## 8. Handoff discipline

Do not create another handoff document merely to summarize the current chat.

Update the authoritative register or the relevant `docs/progress/` artifact. If a new durable rule is discovered, add it to the appropriate canonical document so the next AI does not need conversational memory.

## 9. Completion language

Use precise language:

- **Proven:** evidence directly establishes the claim.
- **Qualified:** proven sufficiently for the stated gate/use.
- **Candidate:** designed but not yet proven.
- **Inferred:** reasoned from evidence but not directly established.
- **Blocked:** required evidence or authority is missing.
- **Rejected:** explicitly ruled out by current authority.
- **Superseded:** once valid, replaced by newer canonical material.

Never say “done,” “works,” “safe,” or “canonical” without stating what was actually verified.

## 10. Default AI behavior

When uncertain, the correct behavior is:

`preserve uncertainty → locate authority → isolate claim → seek evidence → update canonical record → proceed only when the gate permits.`

That is preferable to producing a plausible but unverified AoE2DE interpretation.
