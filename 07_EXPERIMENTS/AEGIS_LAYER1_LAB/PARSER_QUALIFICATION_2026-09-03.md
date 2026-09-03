# AoE2ScenarioParser Qualification — 2026-09-03

## Decision

**QUALIFIED FOR LAB FIXTURE CONSTRUCTION — NOT PART OF BYZBOT RUNTIME.**

The supplied AoE2ScenarioParser source was extracted under the controlled AoE2DE
installation and executed from an isolated Python 3.13 virtual environment.
The capability is approved only for deterministic scenario-fixture construction.

## Source identity

- extracted root: `AoE2ScenarioParser-master`
- source files: 295 (excluding generated `__pycache__` / `.pyc`)
- deterministic source-tree SHA-256:
  `1F3B47E916C296EFF4A18E809B5B2D392D8382B4FD2680B04784BD1E57ED0652`
- uploaded archive SHA-256:
  `3B3F81A92E6B68544A28D357245BC21ABD261F8D64A4AEB02AA579273246CC4D`
- package version field: `<VERSION_HERE>`
- scenario format exercised: DE 1.58

The package version placeholder means this source snapshot is **not promoted as
a numbered upstream release**. Requalification is required if the source tree changes.

## Dependency isolation

The parser was executed from a dedicated virtual environment outside the game
AI directory. Installed dependencies were `deprecation==2.1.0`,
`typing_extensions==4.16.0`, `ordered-set==4.1.0`, and `packaging==26.3`.
The project itself was loaded from the extracted source tree; it was not installed
into the game's Python or AI directories.

## Tests

The parser's bundled unit suite completed **106/106 PASS** under Python 3.13.
The first import exposed a Windows `cp1252` console encoding defect when the
parser emitted a Unicode progress glyph. The lab wrapper now forces UTF-8 stdout
before parser import; no parser source was modified to mask the failure.

A supplied DE 1.58 default scenario was parsed successfully, reconstructed, written,
and parsed again. The original was 645 bytes; the reconstructed file was 657 bytes.
Semantic checks preserved DE 1.58, an 80x80 map, and two active players.

## Pure-.per fixture qualification

A calibration scenario was generated from the parser's bundled DE 1.58 default
fixture. It contains one initial P1 male villager and one non-looping five-second
scenario trigger that creates exactly one additional P1 male villager.

The fixture was reloaded and verified to contain exactly one trigger, one initial
P1 unit, and **zero script-call conditions/effects**. No XS script was added.
The parser's XsManager was not used to construct the fixture; inspection deliberately
avoids its lazy XS-trigger accessor.

This establishes the parser as a fixture-generation instrument while preserving
the project's pure-.per runtime boundary.

## Security boundaries

1. The parser is never trusted merely because it is available on disk.
2. The source-tree digest is checked before import by the AEGIS wrapper.
3. The parser is not allowed to modify the installed game executable or AI corpus.
4. XS-related parser facilities and the bundled `xs-check` executable are outside
   the qualified capability surface.
5. Generated scenarios are written into isolated experiment directories.
6. A generated scenario is not considered game-valid until AoE2DE itself loads it.
7. Parser success is format evidence only; it is not native engine causal evidence.
8. No Layer 1 claim is promoted from parser output.

## Next gate

The next experiment is **P0A-CAL-001**: load the generated scenario in the controlled
AoE2DE build, run a pure-.per probe, and establish the S0/R0 -> mutation -> S1/R1
observation channel. Only after that calibration succeeds will the persistent-fact
freshness arms be executed.

## Evidence status

- parser source qualification: PASS
- parser bundled tests: PASS (106/106)
- parser round-trip: PASS
- pure-.per scenario structure: PASS
- native AoE2DE load: **NOT YET TESTED**
- native observation channel: **NOT YET TESTED**
- P0-A causal result: **NOT TESTED**
- Layer 1 status: **89% unchanged**
