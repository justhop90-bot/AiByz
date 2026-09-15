# AoE2Control 1.0.0 — AEGIS Adapter Qualification Record

Status: **CANDIDATE / STATICALLY COMPATIBLE / RUNTIME-UNQUALIFIED BY AEGIS**

## Source artifact

Project: `aoe2control/AoE2Control`
Release: `1.0.0`
Release publication: `2026-08-13`
Release ZIP: `AoE2Control_1.0.0.zip`
Observed ZIP SHA-256: `D428FA1E25D5E6F26A126E1C104BB7CD1CA73F42D6E23C28D84ECD0C684DA224`

## Upstream release evidence

The release manifest identifies:

- configuration: `ReleasePacked|x64`;
- source commit: `3810f3b8e87ad22ea188b6a07fcdf7d793abac4b`;
- clean source tree at packaging time;
- launcher status protocol version 1;
- module package writer version 2;
- module package readers versions 1 and 2.

The release manifest explicitly records game build ID `24094652` and game file version `101.103.48987.0` in its runtime metrics. This exactly matches the AEGIS target build.

The manifest also reports an upstream bounded single-player Lua compatibility probe and native test result `212/212`. Those are **upstream evidence**, not AEGIS runtime qualification.

## Security / architecture boundary

AoE2Control communicates directly with the game through DLL injection and runtime hooks. Its own release manifest states that mapped executable state is legitimately modified by manual mapping and runtime hooks.

Therefore AEGIS treats AoE2Control as an **optional instrumentation adapter**, never as a trusted architectural subsystem and never as an unconditional dependency.

Default AEGIS harness policy remains:

- no executable patching;
- no memory writes;
- no debugger attachment;
- no hidden native test-harness activation;
- single-player experiments only unless separately qualified.

An AoE2Control-backed experiment must explicitly opt into a separate adapter security profile and record the exact adapter artifact hash.

## What this evidence changes

Before this record, AoE2Control was only a version-compatibility candidate. The release manifest now gives direct upstream evidence that version 1.0.0 was built and tested against the exact AEGIS retail build.

This removes one major compatibility uncertainty, but does **not** establish that AEGIS can consume its observations correctly, that its offsets remain valid on this machine, or that its observation timestamps satisfy AEGIS temporal semantics.

## Required AEGIS adapter tests

1. Launch/attach against the exact retail build.
2. Verify adapter artifact hash before execution.
3. Verify assigned player identity.
4. Verify game clock observation.
5. Verify unit/object identity continuity.
6. Verify fog/visibility semantics.
7. Verify cavalry unit-line observation.
8. Verify command observation versus world transition.
9. Verify teardown leaves the retail installation unchanged.
10. Cross-correlate at least one live observation stream with the resulting `.aoe2record`.

No adapter result may upgrade an AEGIS machine-semantic claim without the required cross-evidence.
