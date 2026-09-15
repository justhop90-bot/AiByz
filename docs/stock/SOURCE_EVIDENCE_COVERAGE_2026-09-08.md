# Source / Evidence Coverage Matrix — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

This matrix separates what the project can establish from public/historical material, what is directly established from the restored target-build package, and what remains an unresolved machine question. It is a deconstruction instrument, not an implementation authorization.

## Evidence classes

| Class | Meaning | Engineering use |
|---|---|---|
| PUBLICLY PROVEN | Current or stable public documentation directly specifies the vocabulary, syntax, parameterization, or documented behavior. | Syntax/reference; never sufficient alone for target numeric ABI allocation. |
| HISTORICALLY CORROBORATED | Historical source, package manifests, diffs, or independent repositories corroborate topology or design intent. | Reconstruction of prior architecture and behavior. |
| LOCALLY PROVEN | Exact target-build installed package or machine capture establishes the artifact, content, hashes, or observed static topology. | Primary basis for current stock reconstruction and ABI occupancy. |
| TARGET-BUILD UNKNOWN | The available evidence does not establish the proposition for build `101.103.48987.0`. | Must remain explicitly unresolved. |
| FUTURE RUNTIME QUALIFICATION | A controlled target-build experiment is required to distinguish competing semantic explanations. | Deferred until the relevant subsystem has been fully deconstructed and the qualification contract is explicit. |

## Coverage

| Domain | Best current evidence | Coverage | What is established | What is not established |
|---|---|---|---|---|
| AI command vocabulary | AoE2 AI Scripting Encyclopedia | PUBLICLY PROVEN | Command names, documented forms, parameter references, broad scripting vocabulary. | Exact undocumented target-build side effects. |
| Facts / object-data | Encyclopedia + official DE patch notes | PUBLICLY PROVEN | Documented fact/object-data surfaces and several documented fixes. | Complete implementation semantics and mutation timing. |
| Strategic numbers | Encyclopedia + target package census | PUBLICLY PROVEN + LOCALLY PROVEN | Public SN vocabulary plus exact target package declarations/writes. | Safe AEGIS allocation without ownership/lifecycle analysis. |
| Goals | Target package census + stock source | LOCALLY PROVEN | Referenced channels, writes/reads, declaration sites and occupancy. | Universal semantic meaning from numeric value alone. |
| Timers | Target package census | LOCALLY PROVEN | Referenced timer channels and operations. | Scheduler timing/visibility guarantees. |
| Load-if | Encyclopedia load-if table | PUBLICLY PROVEN | System-defined load-if vocabulary and initial-pass concept. | Exact target-build interaction with every historical package variant. |
| Normal-HD runtime closure | A1 load-closure capture | LOCALLY PROVEN | `AI (HD version).per` loads `defaultConstants`, `finalingConstants`, and `finaling`; those four files have no further loads. | Whether historical Promisory source modules are independently loaded by a different runtime path. |
| Full Promisory source substrate | Restored package + historical source manifests | LOCALLY PROVEN + HISTORICALLY CORROBORATED | Large subsystem corpus exists and contains dedicated modules such as buildings, gatherers, researches, tsa, threats, units, etc. | Treating the entire corpus as the current normal-HD runtime closure. |
| Stock construction OS | `buildings.per` source archaeology | HISTORICALLY CORROBORATED + LOCALLY PROVEN | Placement, build-line, builder assignment, pending-object and recovery mechanisms exist in the source substrate. | Exact target-build temporal side effects of every construction primitive. |
| Stock economy/worker OS | `gatherers.per`, `dawn.per`, `init.per` | HISTORICALLY CORROBORATED + LOCALLY PROVEN | Allocation, worker tasking, dropsite/service-distance, search/filter, and reconciliation patterns. | Universal per-tick scheduling guarantees. |
| Stock research OS | `researches.per` | HISTORICALLY CORROBORATED + LOCALLY PROVEN | Age/research policy, affordability, pending/research command patterns. | Exact command completion and transition timing. |
| Stock military OS | `tsa.per`, `units.per`, `scoutcontrol.per`, `threats.per` | HISTORICALLY CORROBORATED + LOCALLY PROVEN | Tactical production, scouting, threat signals, military state and recovery patterns. | Complete causal timing from sensor observation to physical outcome. |
| Escrow | `escrow.per` + public command documentation | HISTORICALLY CORROBORATED + LOCALLY PROVEN | Escrow is an actual AI/engine substrate with reservation/control operations. | Exact race behavior under simultaneous competing spends. |
| Replay observability | Target-build replay corpus + parsers | LOCALLY PROVEN | Observable replay/header/body surfaces can corroborate external outcomes and command/lifecycle traces. | Hidden native state that never reaches the replay surface. |
| Rule-pass visibility | Existing machine archaeology | TARGET-BUILD UNKNOWN | Some state relationships are statically visible. | General same-pass mutation/read visibility and scheduling guarantees. |
| Pending-object lifecycle | Source + official patch notes | PARTIALLY PROVEN | Pending objects and several related behaviors are real and documented. | Complete transition/failure lifecycle for all object classes. |
| Command issuance vs completion | Source + machine evidence | TARGET-BUILD UNKNOWN | Commands are distinguishable from later observed state. | Universal completion latency or success semantics. |
| Native scheduler mutation | Layer-1 evidence | TARGET-BUILD UNKNOWN | Scheduler architecture has been partially reconstructed. | Full predictive scheduler state transition model. |
| AEGIS numeric ABI allocation | State collision evidence | NOT AUTHORIZED | Collision/occupancy evidence exists. | No channel is cleared solely because its number appears available. |

## Current machine facts

The dated A1 capture identifies the target executable as:

`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

The restored stock AI package contains 516 files. The normal-HD runtime closure captured on 2026-09-05 is only:

```text
AI (HD version).per
├── Promisory/defaultConstants.per
├── Promisory/finalingConstants.per
└── Promisory/finaling.per
```

The wider Promisory corpus is therefore treated as **historical/source substrate for reconstruction**, not as proof that every source file is independently loaded in the current normal-HD closure.

The A1 typed-state census records approximately:

- 87 referenced goal channels / 3,193 operations
- 143 referenced strategic-number channels / 1,836 operations
- 29 referenced timers / 83 operations
- no detected flag operations

The normalized runtime topology records:

- 74 unique goal writers / 2,177 write occurrences
- 58 unique goal readers / 1,016 read occurrences
- 143 unique strategic-number writers / 1,836 occurrences
- 7 fact/query forms / 1,867 occurrences
- 5 command families / 1,806 occurrences

These figures describe **observed source/runtime topology**, not semantic ownership.

## Immediate deconstruction consequence

The next work is a join across four evidence layers:

```text
exact A1 package
      ↓
load closure + symbol census
      ↓
stock source subsystem reconstruction
      ↓
reader / writer / resetter / lifecycle matrix
      ↓
AEGIS ownership decisions
```

The critical distinction is now explicit:

> **Current runtime closure and historical Promisory source topology are different evidence objects.**

The project must reconstruct the latter without falsely promoting it into the former.

## Deferred qualification queue

1. Persistent-fact mutation and freshness.
2. Scheduler state mutation and rule-pass visibility.
3. Rule-to-action bridging.
4. UnitAI order/action mutation.
5. Failure propagation and pending-object transitions.
6. Required identity lifecycle edges.
7. One predictive end-to-end causal path.

These remain Layer-1/runtime qualification work and are intentionally not being reopened during this total-system deconstruction pass.
