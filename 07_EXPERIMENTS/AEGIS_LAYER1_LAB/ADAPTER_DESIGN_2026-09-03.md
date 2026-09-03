# AEGIS AoE2DE Native Experiment Adapter — 2026-09-03

## Status

**ADAPTER FOUNDATION IMPLEMENTED — NATIVE CALIBRATION NOT YET EXECUTED**

This branch extends the Layer 1 laboratory with an AoE2DE-specific process and
provenance boundary. It does **not** claim that a native game experiment can yet
be constructed, mutated, observed, or causally adjudicated end-to-end.

## Governing causal pipeline

```text
experiment definition
    -> controlled scenario contract
    -> verified executable
    -> isolated runtime
    -> native state / mutation
    -> observation artifact
    -> adjudication
    -> evidence ledger
    -> promotion decision
```

A process exit is never substituted for a game-state observation.
A replay is an observation artifact, not direct native state.
A validator result is not runtime evidence.

## Implemented modules

- `aegis_lab/adapter/build_guard.py`
  - fail-closed SHA-256 verification of the controlled executable.
- `aegis_lab/adapter/runtime_controller.py`
  - explicit argv process launch, no shell interpolation, isolated run directory,
    stdout/stderr capture, timeout handling.
- `aegis_lab/adapter/scenario_contract.py`
  - explicit machine-readable scenario/probe/mutation/timing contract.
  - refuses missing scenario artifacts and invalid player/timing fields.
- `aegis_lab/adapter/observer.py`
  - strict ingestion boundary for observations.
  - rejects missing fields, malformed measurements, and experiment-ID mismatch.
- `aegis_lab/adapter/artifacts.py`
  - copies raw artifacts and records byte size and SHA-256 provenance.
- `aegis_lab/adapter/calibration.py`
  - preflight gate separating instrumentation readiness from causal promotion.
- `tests/test_adapter.py`
  - fail-closed identity, observation provenance, and artifact integrity tests.

## Controlled build

The project-controlled executable is build `101.103.48987.0` with SHA-256:

`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

The local machine inventory found the Steam installation at the expected AoE2DE
installation root and independently verified this executable hash. The adapter
requires the hash match before launch.

## What remains intentionally unimplemented

### 1. Scenario provider

The machine does not currently have a committed native `.aoe2scenario` fixture
for this campaign. No scenario generator is invented here. A provider must be
introduced only after its format, version compatibility, and generated state are
independently validated.

### 2. State mutator

The adapter contract records a mutation specification, but does not pretend a
JSON field changes native game state. A real mutator must enact exactly one
controlled state transition and emit evidence of that transition.

### 3. Native observation provider

The observation reader defines the boundary but does not fabricate measurements.
The first implementation should establish a known S0, obtain R0, perform one
controlled mutation, obtain R1, and demonstrate that the observation channel
tracks the known change.

### 4. Full game lifecycle automation

External research indicates that AoE2DE exposes AI/debug launch options such as
`AIDEBUGGING`, `AISCRIPTDEBUGGING`, and logging-related options. These are treated
as candidate instrumentation surfaces, not as proven causal interfaces. They
must be tested against the controlled build before entering the evidence chain.

## Security / integrity rules

1. Never launch an unverified executable.
2. Never use shell command strings for native execution; pass argv as a list.
3. Never inject DLLs, hooks, or unsupported process modifications as the default
   experiment mechanism.
4. Never use external automation to silently alter experiment state.
5. Every run gets an isolated directory and explicit experiment ID.
6. Raw observations remain immutable inputs to adjudication.
7. Timeouts and crashes are infrastructure/runtime outcomes, not causal results.
8. No Layer 1 proposition is promoted from this adapter until competing
   hypotheses are discriminated.

## Calibration gate

The first native test is deliberately microscopic:

```text
S0: known object/unit count
R0: observe count
S1: exactly one controlled create/destroy mutation
R1: observe count
```

Success means only that the instrumentation path is calibrated. It does not
establish persistent-fact freshness.

The next causal test then implements the P0-A design:

```text
S0 -> evaluate F -> R0
     mutate to S1
     DO NOT intentionally reevaluate F
     consume/query F -> R1
```

A matched reevaluation arm follows:

```text
S0 -> evaluate F -> R0
     mutate to S1
     reevaluate F
     consume/query F -> R1
```

The adapter must preserve timing and raw evidence sufficiently to distinguish
live, scheduled, cached, explicit-refresh, and fact-class-specific hypotheses.

## Evidence / external cross-checks

The current official AoE2DE update found during this adapter build is Update
177723 (June 2, 2026). It includes AI fixes and an XS custom-lobby transfer fix;
it does not establish the native causal contracts targeted by this laboratory.

Public launch-option documentation independently lists `AIDEBUGGING` and
`AISCRIPTDEBUGGING` among AoE2DE launch options. These are candidate runtime
controls only until verified on the controlled build.

## Promotion decision

**No Layer 1 percentage change. No causal claim promoted.**

This branch is an engineering-enablement milestone. The Layer 1 status remains
89% pending the P0-A/P0-B/P0-C/P0-D/P0-E causal closures defined by the project
methodology.

## Reproduction

1. Checkout this branch.
2. Run the adapter unit tests with Python's standard `unittest` runner.
3. Supply a real, independently validated scenario fixture to
   `ScenarioContract`.
4. Run `calibration.preflight` before any native launch.
5. Only after preflight passes, execute the microscopic calibration experiment.
6. Preserve every raw artifact and adjudication result under the experiment ID.
