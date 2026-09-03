# Layer 1 Native Pass — Persistent Fact QC

## Scope
This pass continues the `.per`-first Layer 1 investigation. XS remains machine-archaeology context only and is not a ByzBot dependency.

## New evidence inspected
The controlled AIExpert native corpus contains a contiguous semantic boundary including `Starting a new game`, application of game settings, `Finished applying game settings to new game start`, `Init AI Facts`, comparison operators, player-scope fact families, game-mode/age/civ vocabulary, and `UP-PROCESS-60FPS`.

This strengthens the conclusion that AI fact definitions are initialized as part of a native AI/game-state initialization phase. It does not prove the exact function boundaries, object ownership, or scheduler frequency.

## Important causal distinction
The native diagnostics also expose explicit validation failures for rule variable context, goals, unit/building types, attributes, resources, players, timers, search sources, target objects, technologies, and related state. This demonstrates that many AI-facing operations cross a native semantic validation boundary before producing a result.

Working model:

`.per semantic request → native resolution/validation → result or controlled failure`

This is stronger than treating every AI command/fact as an unchecked primitive. Exact dispatch and return-state representation remain open.

## Persistent-fact target
The native corpus still provides the strongest current causal anchor:

`Evaluating Persistent Facts`
→ per-fact evaluation/reporting
→ `Finished Evaluating Persistent Facts`

The current evidence establishes a named phase and per-fact reporting, but not its storage layout or cadence.

## New experimental design
The next runtime probe should distinguish four hypotheses:

1. persistent facts are recomputed directly whenever queried;
2. persistent facts are refreshed on a fixed AI evaluation boundary;
3. persistent facts are cached until invalidated;
4. different fact classes use different freshness mechanisms.

Minimum experiment:

`T0 controlled state → evaluate fact → mutate only underlying state → observe next evaluation`

Repeat with a direct-state fact and a derived/feasibility fact. Record game time, rule-pass observations, fact result, and the first subsequent transition. A result that changes before a normal rule boundary would falsify a simple per-pass cache model; a result that remains stale across a controlled boundary would support caching/invalidation behavior.

## `UP-PROCESS-60FPS` caution
`UP-PROCESS-60FPS` is confirmed native AI-visible vocabulary. It must not be interpreted as proof that rule evaluation runs at 60 Hz. The only valid promotion path is a controlled timing experiment correlating the setting with observable AI evaluation behavior.

## Scheduler implication
Because the native corpus contains rule priority, interval, sorted-rule state, and next-rule indexing, the next scheduler experiment should use two otherwise equivalent rules and vary exactly one arbitration parameter at a time. The objective is deterministic prediction of rule selection, not merely confirmation that both rules can fire.

## Programmer-intent interpretation
The separation between initialization, semantic fact vocabulary, validation diagnostics, and persistent-fact evaluation is evidence of deliberate subsystem boundaries, but programmer intent remains graded as inference until implementation-level ownership and call flow are recovered.

## Security / provenance
No executable, replay, local installation path, credential, personal identifier, or other restricted machine artifact is copied into this public research record. Native addresses remain version-qualified evidence and are not presented as universal offsets.

## Status
No implementation-level causal edge was proven in this pass. Layer 1 remains 89%.

## Next pass
Prioritize one verified persistent-fact read/write chain or one verified `CurrentOrder → CurrentAction` mutation chain. Prefer evidence that closes a causal path over additional vocabulary collection.
