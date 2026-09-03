# Adapter QC Amendment — 2026-09-03

## Scope

This amendment records the next qualification pass after PR #12's adapter
foundation. It supersedes stale test-count wording without rewriting historical
records.

## Corrections

PR #12 originally reported 3/3 adapter tests. The actual committed adapter suite
contains four tests, and the new scenario-provider suite contains three more.
The current local combined result is therefore **7/7 PASS**.

The previously unimplemented scenario-provider gap is now addressed by a
qualified external AoE2ScenarioParser capability and a committed deterministic
fixture. This does not constitute native game-load or causal validation.

## Parser qualification result

The supplied parser source was executed read-only from the installed AI directory
using an isolated Python 3.13 environment. Its deterministic source tree contains
295 non-generated files and has SHA-256
`1F3B47E916C296EFF4A18E809B5B2D392D8382B4FD2680B04784BD1E57ED0652`.
The source declares `<VERSION_HERE>`, so it is treated as an unnumbered snapshot,
not an upstream release.

The bundled parser suite passed **106/106**. A DE 1.58 default scenario was parsed,
reconstructed, written, and parsed again successfully. The generated calibration
fixture was independently reloaded and verified to contain one P1 unit, one
five-second creation trigger, and zero XS script-call conditions/effects.

## Security boundary

The parser is laboratory tooling only. It is not installed into the game runtime,
not shipped with ByzBot, and does not execute its bundled `xs-check` facility.
The AEGIS wrapper fail-closes on an unexpected parser source-tree digest. Generated
fixtures are rejected if XS script-call conditions/effects appear.

The pure-.per project boundary remains unchanged: **no XS runtime dependency**.

## Scientific status

The fixture now provides a deterministic candidate for P0A-CAL-001:

`S0 known state -> R0 -> one scenario-trigger mutation at t=5s -> S1 -> R1`

The parser establishes fixture provenance and format integrity only. It does not
prove that AoE2DE loads the fixture, that the AI observes the expected native state,
or that any fact is persistent, cached, live, scheduled, or explicitly refreshed.
Those propositions remain untested.

**Layer 1 remains 89%. No causal proposition is promoted.**

## Security-hardening pass

The two gates were raised from functional qualification to explicit fail-closed
security controls. Native runs now require an isolated lab run root and a
sanitized child environment. The runtime continues to use the verified
executable, explicit argv, shell=False, mandatory timeout, and process reap.

The parser environment is now reproduced in a dedicated Python 3.13 virtual
environment with exact dependency versions recorded in
`PARSER_ENVIRONMENT_LOCK_2026-09-03.txt`. No dependency is installed into the
game installation or global interpreter as part of qualification.

A deliberately incomplete system-Python test initially failed because the
parser dependency `typing_extensions` was absent. This was treated as a gate
failure, not worked around by weakening the qualification. The isolated
environment was then provisioned from the parser's own requirements and the
full adapter suite passed.

Final local adapter/scenario-provider suite: **9/9 PASS**. Compileall: PASS.
Parser source remains SHA-256 pinned. No native game launch was performed.

The security gate still does not certify the game executable's internal safety,
nor does it permit DLL injection, hooks, debugger attachment, memory patching,
or XS execution. Those remain explicitly outside the laboratory contract.

## Native startup calibration â€” follow-up

The exact verified executable was launched through the hardened runtime with `SKIPINTRO` and a 20-second timeout. The process did not terminate naturally within the window. The runtime killed and reaped PID 3876; return code after enforced termination was `1`. stdout and stderr were empty, and a post-reap task check found no matching PID. This is infrastructure/lifecycle evidence only and does not prove successful initialization, scenario loading, AI loading, or any game-state observation.

The local combined adapter + scenario-provider suite is **7/7 PASS** (four adapter tests plus three scenario-provider tests). Parser bundled tests remain **106/106 PASS**.

Layer 1 remains 89%; no causal proposition is promoted.
