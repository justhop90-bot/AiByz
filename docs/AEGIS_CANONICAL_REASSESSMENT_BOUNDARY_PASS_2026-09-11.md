# AEGIS Canonical Reassessment Boundary Pass — 2026-09-11

## Verdict

**IMPLEMENTED / LOCALIZED / NO MONOLITHIC CONTROLLER**

The seven registered verticals now publish a canonical reassessment event from their registry-defined `REASSESS` owner. The event is keyed to the terminal lifecycle generation and is emitted once per generation.

This pass does not promote any vertical to qualified status and does not manufacture causal evidence.

## Boundary semantics

The canonical boundary is:

```text
terminal lifecycle outcome
        ↓
REASSESS token = lifecycle generation
        ↓
next owner may reconsider
        ↓
new observation / classification / demand generation
```

The reassessment publisher does **not**:

- choose the next strategy;
- issue a physical command;
- create a replacement authorization;
- claim strategic success;
- convert UNKNOWN into success;
- convert world-state observation into causal proof;
- coordinate all seven verticals through a central controller.

## Seven registered implementations

| Vertical | Reassessment owner | Goal slots | Trigger |
|---|---|---:|---|
| `worker_economy` | `worker_economy.verification` | 760–761 | worker verification confirmed/failed |
| `villager_production` | `villager_production.lifecycle` | 762–763 | lifecycle reconciler confirmed/failed |
| `housing` | `housing.verification` | 764–765 | housing lifecycle confirmed/failed |
| `age_transition` | `age_transition.reassessment` | 766–767 | age transition confirmed/failed |
| `anti_cavalry` | `anti_cavalry.reassessment` | 768–769 | anti-cavalry lifecycle confirmed/failed |
| `tactical_micro` | `tactical_micro.verification` | 770–771 | micro verification reaches reassess |
| `military_production` | `military_production.reassessment` | 772–773 | candidate lifecycle confirmed/failed |

Each publisher uses its own semantic owner and lifecycle generation. No shared strategy-state goal was introduced.

## Idempotency

Each publisher compares:

```text
reassess-generation != lifecycle-generation
```

before publishing. Once the token has been published for that lifecycle generation, the same terminal state cannot generate an unbounded stream of duplicate reassessment events.

## Failure behavior

Both terminal success/evidence states and terminal failure states publish reassessment. This is intentional:

```text
SUCCESSFUL OBSERVED OUTCOME -> REASSESS
FAILED/EXPIRED OUTCOME      -> REASSESS
```

The consumer therefore receives an opportunity to re-evaluate either continuation or recovery.

## Registry/validator enforcement

The vertical registry already defines `REASSESS` as the required terminal stage. The validator now additionally requires the final event to contain:

- `reassessment_published = true`;
- `reassessment_generation == trace.generation`;
- no `reassessment_strategy` selected by the publisher.

New validation errors:

- `VSL-029` — reassessment token not published;
- `VSL-030` — reassessment generation mismatch;
- `VSL-031` — reassessment publisher selected strategy.

Tests were added for all three conditions.

## Namespace integrity discovery during this pass

The broader source inspection exposed two omissions in the previous namespace ledger. They were repaired without changing semantic ownership:

1. Worker Task Verification:
   - request identity `546 → 560`
   - authorization identity `547 → 561`
2. Worker Loop Qualification:
   - generation/valid/stage/progress/cycle `555–559 → 562–566`

The reason for the second repair is significant: Worker Recovery had already been correctly repaired into `555–556`, while the older qualification artifact still occupied those same slots.

The authoritative namespace map has been updated accordingly.

## What remains intentionally unresolved

### Causal verification

The reassessment boundary does not manufacture causal evidence. Housing, villager production, and anti-cavalry still require independently proven attribution before their observed world-state changes can receive causal completion credit.

### Military Production

Military Production remains `CANDIDATE_BLOCKED` because `aegis-mp-unit` remains a selector-initialization blocker. Publishing a reassessment event does not promote the candidate.

### Tactical Micro

The micro boundary is now explicit, but command-to-tactical-world-effect remains a separate qualification problem.

### Downstream consumption

The publisher now exists. The next architectural pass must prove that the owning demand/decision path consumes the token to create a **new generation**, rather than merely observing the token. That is intentionally separate from publication so that the boundary remains local and non-monolithic.

## Evidence discipline

No target-build runtime claim is made by this document. These changes are source-architecture and validator changes only.

The implementation therefore remains:

```text
SOURCE-IMPLEMENTED
≠
ENGINE-QUALIFIED
```
