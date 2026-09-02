# Programmer ↔ Machine Bridge — HD/2013 Pass 1

## Thesis

The historical AI demonstrates the exact point where a programmer's conceptual model of an RTS becomes machine-executable: the designer selects a low-dimensional state representation, maps observable engine predicates into that state, and lets later rules operate on the compressed conclusion.

The research target is therefore not an individual rule. It is the translation boundary between **human concept** and **engine primitive**.

## Bridge table

| Human concept | Program representation | Machine-facing mechanism | Evidence |
|---|---|---|---|
| Strategic mode | `strategy-goal` | goal register + rule predicates | CONFIRMED |
| Military capability | `unit-goal` | goal register + train selection | CONFIRMED |
| Position role | `position-goal` | goal state + position predicates | CONFIRMED |
| Enemy plan | `enemy-goal` | classified goal state | CONFIRMED |
| Resource reservation | `sn-resource-control` / escrow goals | strategic number + escrow API | CONFIRMED |
| Threat memory | threat goals/data | goal state + threat queries | CONFIRMED |
| Attack lifecycle | `attack-goal`, `attack-status-goal` | goals + timers | CONFIRMED |
| Retreat policy | `retreat-now-goal` | goal + attack reset | CONFIRMED |
| Temporal hysteresis | timer bank | timer predicates/actions | CONFIRMED |
| Construction feasibility | `can-build` + pending objects | engine query + build | CONFIRMED |
| Research feasibility | `can-research` + research status | engine query + research | CONFIRMED |
| Map class | map/position state | engine predicates + state | CONFIRMED |

## 1. Compression is the bridge

A programmer observes a high-dimensional world but the historical rule substrate does not offer a clean general-purpose strategic model. The solution is **compression into reusable state**.

Example:

`enemy age + enemy military + enemy buildings + game time`
→ `enemy-goal = classified strategy`
→ many downstream rules consume that classification.

This is a machine-efficient representation of a human strategic conclusion.

## 2. Goals are software state

The goal bank behaves as primitive state memory. A goal can function as a mode, classification, permission, reservation purpose, target identity, lifecycle state, scratch register, or reset latch.

Therefore goal counts alone cannot establish semantics. The semantic type must be recovered from writer-reader transitions and consequences.

## 3. Strategic numbers are policy state

Strategic numbers in the recovered controller include resource control, gatherer percentages, military threat scalars, current age, exploration capacity, attack-group sizing, map classification, drop-distance policy, and military level.

The same machine primitive can therefore carry different semantic types. AEGIS must classify the semantic role instead of inheriting the historical numeric namespace blindly.

## 4. Timers are control memory

The timer subsystem supplies hysteresis and rate limiting:

`event -> timer armed -> repeated event suppressed -> recovery window -> reevaluation`

This is a historical machine-level solution to oscillation and command spam.

## 5. Feasibility is an execution boundary

`can-build`, `can-research`, pending-object counts, and research status separate **intent** from **completed world state**.

The historical program does not generally assume that issuing a command means that the corresponding state transition has already completed.

## 6. Resource reservation is a protocol

The recurring pattern is:

`need -> reserve -> protect escrow -> wait for feasibility -> execute -> release`

This is closer to a transaction/resource-lock protocol than to a static “resources >= cost” test.

## 7. Attack/retreat is a lifecycle

The controller connects strategic intent to tactical interruption:

`attack permission -> threat/target evaluation -> retreat/regroup -> timer -> reset/restart -> reassessment`

The historical design therefore models an operational lifecycle around offensive action.

## 8. The AEGIS separation rule

AEGIS should preserve these conceptual boundaries:

1. observation is not classification;
2. classification is not intent;
3. intent is not command;
4. command is not execution;
5. execution is not completion;
6. completion is not strategic success.

The historical source often compresses several boundaries into goals, timers, and rule chains. AEGIS should recover and separate them.

## 9. What not to inherit

Historical implementation details must not be promoted merely because they exist:

- fragmented multi-writer authority;
- arbitrary numeric conventions;
- duplicated production writers;
- undocumented scratch registers;
- obsolete/commented mechanisms;
- historical workarounds without evidence;
- thresholds detached from state context.

These are implementation artifacts until independently justified.

## 10. Research conclusion

The programmer-machine connection becomes visible when a human concept becomes a stable state representation with a downstream causal role.

The strongest Pass 1 bridges are:

- position -> strategy/unit state;
- enemy observations -> enemy classification;
- resource need -> reservation state;
- threat -> attack lifecycle transition;
- map class -> infrastructure/exploration policy;
- feasibility/pending state -> command boundary;
- timer -> temporal hysteresis.

Pass 2 now asks **why these abstractions were selected**, what competitive principle each encodes, and which principles survive outside the historical engine.
