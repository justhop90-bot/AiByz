# P0 Construction Operating System Forensics — 2026-09-08

Status: STATIC FORENSICALLY QUALIFIED / RUNTIME UNQUALIFIED
Target: AoE2DE build 101.103.48987.0 / BuildID 24094652

## Executive finding

Construction is not one primitive called `build`.
The stock system is a distributed construction operating system spanning:

1. strategic demand / `increase-ts`
2. affordability and authorization
3. placement policy
4. placement search and spatial constraints
5. native build issuance
6. builder assignment
7. pending-placement observation
8. failed-placement recovery
9. foundation/progress inspection
10. completion accounting
11. queue cancellation/reset
12. specialized building families
13. military/defensive forward construction
14. farm and dropsite logistics
15. migration / town-center relocation
16. conditional extreme placement algorithms

The major architectural correction is that AEGIS must own this lifecycle while still using the engine's native construction ABI. Copying `buildings.per` into AegisProm would preserve behavior but would not create AEGIS ownership.

## Corpus inspected

Authoritative machine files inspected:

- `Promisory/buildings.per` — 13,117 lines
- `Promisory/extremebuildings2.per` — 1,010 lines
- `AiBuilder/construction.per` — 399 lines
- `AI (HD version).per` — 36,141 lines
- current `AegisProm/AEGIS-operations-final.per`
- stock constants previously established in `defaultConstants.per` / `finalingConstants.per`

Existing GitHub forensic corpus was treated as prior evidence rather than discarded.

## 1. `buildings.per` is the primary construction OS

Measured on the untouched machine:

- 1,063 `defrule` blocks
- 122 occurrences of `up-build`
- 77 occurrences of `up-can-build`
- 24 occurrences of `up-assign-builders`
- 28 occurrences of `up-pending-placement`
- 178 occurrences of `up-pending-objects`
- 38 occurrences of `up-set-placement-data`
- 54 occurrences of `up-build-line`
- 50 assignments of `sn-placement-zone-size`
- 8 `up-reset-placement` uses
- 218 `set-goal increase-ts` uses

This density proves construction is a stateful subsystem rather than a small set of build commands.

## 2. Strategic demand and execution are deliberately separated

The central construction state is `increase-ts`.
Rules select values such as:

- town-center
- house
- castle
- market
- blacksmith
- monastery / fortified-church
- barracks
- archery-range
- stable
- university
- siege-workshop
- feitoria
- other specialized structures

The execution layer then interprets that state using either:

- `build <building>`
- `up-build ...`
- `up-build-line ...`

This confirms a two-level model:

`construction demand -> placement/execution policy -> engine command`

AEGIS should preserve that separation and make it explicit through its service contract.

## 3. Placement is a first-class subsystem

Stock construction repeatedly programs placement state before issuing a build command.
Observed mechanisms include:

- `up-set-placement-data`
- `sn-placement-zone-size`
- `sn-placement-to-center`
- `sn-placement-fail-delta`
- `sn-town-center-placement`
- `sn-allow-adjacent-dropsites`
- `sn-dropsite-separation-distance`
- `up-set-target-point`
- `up-build place-control`
- `up-build place-point`
- `up-build-line`
- point interpolation and bounding operations
- distance constraints against existing structures/resources/enemy objects

Therefore "where to build" cannot be hidden inside a generic `build()` wrapper.
It is an observable policy decision that must be represented in the AEGIS construction service.

## 4. Builder assignment is a separate lifecycle stage

Stock frequently performs:

`placement/issuance -> up-assign-builders`

and sometimes assigns builders immediately after `up-build-line`.

A particularly strong example is defensive tower construction: the stock system creates a target point, checks whether the line can be built there, issues the build, and assigns five builders; if the tower is nearly complete or military pressure exists, it may assign up to ten.

Therefore builder count is not merely an implementation detail. It is part of construction policy and can be influenced by urgency/threat.

## 5. Pending placement is an explicit state

Stock checks `up-pending-placement` for houses, town centers, farms, military structures, castles, and other structures.

This is distinct from completed building counts and from generic `up-pending-objects`.

The construction state machine must therefore distinguish at least:

`REQUESTED -> ADMITTED -> PLACEMENT_PENDING -> ISSUED -> FOUNDATION/PENDING -> COMPLETE`

with failure/cancellation branches.

## 6. Placement failure is explicitly recoverable

Stock contains `sn-placement-fail-delta` and reset-placement logic.
It also repeatedly clears or retries placement when pending placement remains unresolved.

Observed recovery examples include:

- `up-reset-placement`
- changing placement zone size
- changing placement policy
- clearing a queued structure
- relaxing dropsite adjacency rules
- changing town-size/camp-distance constraints
- retrying at a different point
- abandoning a construction request in favor of another demand

This validates the previously established AEGIS failure taxonomy: a placement failure must not be collapsed into a generic command failure.

Recommended construction-specific dispositions:

- `PLACEMENT_UNAVAILABLE`
- `PLACEMENT_CONFLICT`
- `PLACEMENT_OUT_OF_RANGE`
- `PLACEMENT_POLICY_REJECTED`
- `PLACEMENT_RETRY_REQUIRED`
- `BUILDER_UNAVAILABLE`
- `BUILD_AUTHORIZATION_FAILED`
- `COMMAND_NOT_OBSERVED`
- `FOUNDATION_STALLED`
- `CONSTRUCTION_CANCELLED`

## 7. Town-center construction is materially different

The stock TC path contains a dedicated preparation state and dynamically modifies:

- maximum town size
- camp maximum distance
- town-center placement policy
- resource-relative placement preference

The stock also detects an unresolved TC pending placement and resets it after a timed condition.

TC construction therefore combines:

`economic demand + spatial logistics + settlement policy + placement retry + builder execution`.

AEGIS must not implement TC construction as merely `build town-center`.

## 8. Resource infrastructure is construction coupled to economic state

Lumber camps, mining camps, mills and settlements are selected based on:

- resource discovery
- dropsite distance
- desired number of camps
- worker percentages
- existing infrastructure
- pending placement
- resource availability
- map size

This directly connects our previous resource/dropsite forensic work to construction.

The construction OS therefore consumes economic/information state and publishes new spatial infrastructure that changes economic serviceability.

That creates a feedback loop:

`economic demand -> infrastructure request -> placement -> completion -> serviceability -> worker allocation`

## 9. Farms are a specialized construction scheduler

`AiBuilder/construction.per` exposes a separate algorithm for dependent farm placement.
It searches existing TC/mill structures, derives candidate points using offsets and distance tests, calls `up-can-build-line`, and finally uses `up-build-line`.

This is not equivalent to ordinary structure placement.

It establishes that farm placement is an algorithmic spatial service with:

- candidate generation
- collision/legality testing
- distance optimization
- iterative search
- fallback to ordinary `build farm`

## 10. AiBuilder requires a boundary correction

`AiBuilder/construction.per` is a real construction-related subsystem, but a direct `(load "AiBuilder...` dependency was not established in the AI(HD) entry file during this pass.

Therefore it must currently be classified:

**CONSTRUCTION-RELATED STOCK CORPUS / RUNTIME DEPENDENCY UNQUALIFIED**

It must be preserved as evidence and investigated separately rather than silently promoted to a live dependency.

This is important because the project requirement is to incorporate the entire AI system, while still distinguishing actual runtime dependencies from parallel source/tooling subsystems.

## 11. Extreme placement is conditional, not universal

`buildings.per` conditionally loads `Promisory/extremebuildings2` under the extreme-difficulty configuration and selected map guards.

`extremebuildings2.per` has 76 rules and 20 `up-build` operations.
It uses repeated `up-can-build-line` / `up-build-line` operations to construct patterned walls and related structures.

Therefore extreme placement must be modeled as an optional policy provider under AEGIS, not fused into the generic placement primitive.

## 12. Forward construction is a strategic operation

The stock corpus contains `build-forward` and construction rules tied to defensive and military pressure.
The tower-rush example is particularly clear: enemy tower detection establishes a target location, the system attempts a legal tower placement, assigns builders, adjusts the point if invalid, and escalates builder count when enemy military pressure or construction progress warrants it.

This is a genuine cognition-to-construction interface:

`threat intelligence -> construction objective -> spatial solution -> urgent builder allocation`.

AEGIS should expose this as a typed urgent construction request rather than burying it in generic building rules.

## 13. Construction cancellation is part of arbitration

Stock periodically clears building queues when conditions change.
Examples include:

- house emergency
- excess wood becoming available
- military building requirements changing
- castle timing changing
- resource/strategic conditions changing

Observed operations include `up-reset-placement` and resetting `increase-ts` to zero.

Therefore construction requests are revocable commitments.
This matches the previously established AEGIS contention/preemption work.

Construction cannot own final economic arbitration; it receives an admitted request and must report status/failure back to arbitration.

## 14. Current AEGIS construction position is insufficient

`AEGIS-operations-final.per` currently issues direct native construction commands for:

- house
- lumber camp
- mining camp
- mill
- barracks

It also directly changes stock gatherer percentages.

This is useful as a bootstrap liveness mechanism but is **not** the final Construction OS.
It bypasses the construction request/reservation/placement/builder/verification architecture now established by forensics.

It should eventually become either:

- a bootstrap-only service disabled once full AEGIS construction is active, or
- a thin service client submitting typed construction requests.

It must not remain a competing construction authority.

## 15. Required AEGIS construction contract

Recommended lifecycle:

`REQUESTED
 -> ADMITTED
 -> RESERVED
 -> PLACEMENT_SEARCH
 -> PLACEMENT_SELECTED
 -> AUTHORIZED
 -> COMMAND_ISSUED
 -> PLACEMENT_PENDING
 -> FOUNDATION_OBSERVED
 -> BUILDING_PROGRESS
 -> COMPLETE`

Failure branches:

`PLACEMENT_FAILED
BUILDER_FAILED
AUTHORIZATION_FAILED
COMMAND_NOT_OBSERVED
FOUNDATION_STALLED
CANCELLED
SUPERSEDED`

Every request should carry at minimum:

- generation
- building type
- urgency
- strategic owner
- reservation reference
- placement policy
- target point/policy
- builder requirement
- retry budget
- evidence timestamp
- current state
- failure disposition

## Three-angle review

### Archaeologist / ABI

Confirmed:

- native `build`, `up-build`, `up-build-line`, `up-can-build-line`, placement-data, pending-placement and builder-assignment primitives are deeply integrated.
- exact interpreter pass ordering and command side effects remain runtime-unqualified.
- placement distance terminology must remain precise; stock uses multiple different spatial mechanisms.

### Byzantine Architect

Construction must support Byzantine-specific priorities including:

- early defensive continuity
- monastery/castle timing
- fortified defensive structures where civilization rules allow them
- counter-pressure construction
- water/coastal infrastructure
- late-game infrastructure density
- strategic settlement placement

The service must be civ-policy-neutral at the substrate level but expose enough control for Byzantine cognition to shape priorities.

### AI(HD) / Behavioral Regression

The dangerous regression is to replace the distributed stock construction scheduler with a simplistic FIFO.
That would lose:

- emergency houses
- dropsite logic
- TC placement policy
- placement retries
- military/defensive urgency
- specialized farm placement
- queue cancellation
- builder escalation
- map/difficulty conditional behavior

The final AEGIS Construction OS must reproduce these behavioral contracts while moving strategic authority upward into AEGIS.

## Evidence boundary

This pass reaches the natural static boundary.

We now have enough evidence to define the Construction OS architecture, but not enough to claim runtime equivalence.
The next construction-specific evidence required is controlled runtime qualification of:

1. `build` vs `up-build` vs `up-build-line`
2. placement-data semantics
3. pending-placement transition timing
4. builder assignment side effects
5. placement reset behavior
6. same-pass visibility of construction state
7. command observation after issuance
8. failure/retry timing

No final construction implementation should be declared runtime-qualified until those are tested on the target build.

## Final disposition

**CONSTRUCTION OS FORENSICS: STATIC QUALIFIED.**

**AEGIS implementation: NOT YET QUALIFIED.**

**Promisory runtime dependency: MUST NOT be retained in the final architecture.**

The construction subsystem is now ready for architecture/design implementation, subject to the runtime ABI experiments listed above.
