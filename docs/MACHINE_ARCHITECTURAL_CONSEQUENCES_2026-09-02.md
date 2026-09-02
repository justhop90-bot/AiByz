# AEGIS Machine-Derived Architectural Consequences

## Thesis

The purpose of Layer 1 was not to memorize engine vocabulary. It was to determine which architectural forms are compatible with the machine. This document converts machine evidence into engineering constraints.

## 1. Source order is not authority

Because the runtime exposes priorities and sorted-rule structures, lexical source order cannot be treated as the sole authority over execution order. Architecture must reason in terms of scheduler-visible lifecycle and priority.

**Requirement:** every critical subsystem documents its intended cadence, priority, activation state, and ownership.

## 2. A rule is not a decision

A rule is a scheduler unit. A strategic decision is a semantic commitment. Conflating the two creates architectures in which whichever rule happens to fire becomes the de facto strategist.

**Requirement:** strategic state must exist above individual executable rules.

## 3. Observation must be side-effect constrained

The UP surface is rich enough to query facts, objects, resources, terrain, paths, timers, targets, and feasibility. Observation therefore has substantial power without needing to issue side effects.

**Requirement:** observation modules should default to read-only behavior. Any exception must be explicitly authorized.

## 4. Feasibility belongs before authorization

The machine exposes `up-can-build`, `up-can-research`, and `up-can-train`. These are direct evidence that engine feasibility can be queried.

**Requirement:** an intent must not become an authorized command until current engine feasibility has been checked or an explicit reason for bypass exists.

## 5. Execution is not success

Native action diagnostics distinguish action execution, completion, failure, invalidation, and search-required states.

**Requirement:** the execution layer must emit a result and the verification layer must establish whether the strategic postcondition occurred.

## 6. Postconditions must be world-based

A command can be issued successfully while the intended world-state transition fails later. Therefore verification must inspect state after execution rather than treating command issuance as proof.

**Requirement:** consequential actions receive explicit postconditions wherever observable.

## 7. Search is stateful until disproven otherwise

The existence of reset-search/reset-filter operations strongly suggests query context can be configured and cleared. It is unsafe to assume every query begins from a blank state.

**Requirement:** search procedures explicitly establish their filter/search preconditions.

## 8. Dynamic rule lifecycle is an architectural primitive

Enable/disable/group APIs mean subsystem lifecycle can be controlled dynamically. This is valuable for staged architectures, but dangerous if ownership is ambiguous.

**Requirement:** each dynamic lifecycle operation has one owner and a documented reason.

## 9. Timers are not cosmetic delays

The historical AI uses timers extensively, while the native surface exposes timer APIs and precise-time vocabulary. Timers therefore represent state/hysteresis mechanisms as much as performance controls.

**Requirement:** timer names should encode semantic purpose; every nontrivial timer should document the transition it protects.

## 10. Hysteresis is strategic memory

A system that reacts immediately to every threshold crossing oscillates. Timers, minimum/maximum intervals, persistent goals, and state transitions allow a controller to remember a commitment long enough to evaluate its consequences.

**Requirement:** major strategic transitions should have entry conditions, persistence conditions, exit conditions, and cooldown/recovery semantics.

## 11. One writer per consequential state

V3's major architectural weakness is multi-writer competition: several rules can directly produce production/research/state effects. The machine permits this, but does not make it safe.

**Requirement:** consequential goals and action domains should have a declared authority owner. Other modules submit proposals or observations.

## 12. Capability beats unit identity

The engine can count unit types and unit lines, while the strategic layer needs to reason about combat capabilities, production capacity, mobility, range, durability, siege pressure, anti-armor, anti-archer, raiding, map control, and so on.

**Requirement:** unit identity remains a mechanical fact; capability is a strategic abstraction derived from it.

## 13. Unit-line abstraction must be explicit

A unit line is not the same entity as a concrete unit ID or a broad class ID. The validator incident around `knight-line` demonstrates why this distinction must be represented explicitly.

**Requirement:** knowledge records specify the semantic level of every identifier used by an API.

## 14. Resource economics must be state-dependent

The engine exposes actual resource amounts, percentages, costs, escrow, and market/tribute primitives. Fixed worker ratios therefore represent policies, not fundamental economic truth.

**Requirement:** the future economy director should compute deficits against current obligations, production capacity, technology commitments, and strategic reserves.

## 15. Production is a capability pipeline

Production cannot be reduced to `train unit X`. The meaningful causal chain is objective -> capability -> composition -> infrastructure -> technology -> resource demand -> feasibility -> queue -> completion -> reinforcement.

**Requirement:** the production director owns this chain; tactical modules do not independently create competing production plans.

## 16. Research is an investment

A technology consumes resources and production opportunity while changing capability. Its value is state-dependent.

**Requirement:** research proposals carry strategic rationale and expected capability delta, not only availability predicates.

## 17. Map state is part of economy

Path distance, terrain, elevation, zone, object position, and pathability are exposed engine concepts. A resource or production plan is therefore not economically neutral if it requires unsafe or inefficient map access.

**Requirement:** strategic evaluation incorporates position and logistics into resource valuation.

## 18. Information has value

The engine exposes player, target, object, search, threat, and projectile information. Information can change which strategic branch is optimal.

**Requirement:** scouting and observation should be evaluated partly by the decisions they enable, not only by the number of facts collected.

## 19. Opponent modeling is state estimation

Enemy strategy is not a fact unless directly observed. The strategic layer should maintain beliefs with confidence and alternatives.

**Requirement:** represent opponent hypotheses separately from observations; attach evidence and confidence.

## 20. Transition reasoning is first-class

HD's adaptive strategy code repeatedly reacts to enemy composition, age, infrastructure, map conditions, and military state. This indicates strategic plans are transitions between states rather than permanent labels.

**Requirement:** the future strategy engine models entry conditions, required commitments, transition signatures, likely counters, and fallback states.

## 21. Attack is a commitment, not a Boolean

The inherited system uses goals, timers, military thresholds, technology state, and enemy state around attack/retreat. Native action state also shows target persistence and invalidation.

**Requirement:** attack intent should specify purpose, force requirement, target class, expected conversion, abort condition, and recovery.

## 22. Retreat is preservation logic

Retreat should not be modeled merely as `enemy > threshold`. It is a response to changing force ratio, target viability, pathability, reinforcement, objective completion, and preservation value.

**Requirement:** retreat decisions evaluate whether continuing increases or destroys future capability.

## 23. Initiative is a state variable

Native and historical evidence supports priority, timing, action persistence, and strategic commitment. These interact to create initiative: the ability to force the opponent to answer before they can execute their preferred transition.

**Requirement:** strategic evaluation includes tempo/initiative and not only resource or military totals.

## 24. Conversion efficiency is central

A successful commitment is valuable when the capability invested produces greater enemy economic, military, positional, or strategic damage than it costs to create and replace.

**Requirement:** evaluate actions by conversion value, not raw kill count.

## 25. Resource tax is a strategic mechanism

If an action forces the opponent to spend resources on defense, replacement, siege, counter-units, walls, idle time, or technology, it creates a conversion tax. The Byzantines can later specialize this principle.

**Requirement:** record induced enemy obligations as part of strategic outcome.

## 26. Failure must be modeled before implementation

The native machine has invalidation/failure states. The strategic layer must similarly define failure signatures before issuing complex commitments.

**Requirement:** every major strategic plan records expected result, failure signature, abort condition, and recovery path.

## 27. Memory should preserve causal episodes

A final world state is insufficient. The bot needs to know what it believed, what it attempted, what happened, and whether the result matched expectation.

**Requirement:** strategic memory stores `observation -> belief -> intent -> authorization -> execution -> verification -> outcome -> lesson`.

## 28. Architecture must be evidence-compatible

Every future subsystem must map its assumptions to Layer-1 evidence. If it requires an engine capability not established by the machine contract, that dependency becomes an explicit investigation item.

## 29. Architecture must remain replaceable

Layer 2 strategy should not become entangled with undocumented engine behavior. The boundary should be explicit enough that a later Ghidra finding can amend an execution adapter without rewriting strategic theory.

## 30. Design target

The intended AEGIS architecture is therefore:

`WORLD
 -> OBSERVATION
 -> NORMALIZATION
 -> BELIEF / STATE
 -> STRATEGIC EVALUATION
 -> CANDIDATE INTENTS
 -> COMMITMENT
 -> AUTHORITY
 -> ENGINE FEASIBILITY
 -> EXECUTION
 -> POSTCONDITION
 -> VERIFICATION
 -> MEMORY
 -> REPLANNING`

The native rule scheduler is the clockwork beneath this architecture; it is not the architecture itself.

## 31. Layer-2 implementation gate

No major implementation is considered mature merely because it runs. It must demonstrate:

- a clear strategic purpose;
- an explicit state representation;
- unique authority ownership;
- machine-compatible primitives;
- feasibility gating;
- postcondition verification;
- failure/recovery behavior;
- evidence-backed assumptions;
- reproducible validation;
- a durable knowledge record.

That is the minimum acceptable engineering bar for AEGIS.
