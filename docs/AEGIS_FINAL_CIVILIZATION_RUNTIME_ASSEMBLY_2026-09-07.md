# AEGIS-BYZ Final Civilization Runtime Assembly

## Decision

The project has reached the point where a functioning civilization substrate is more important than maintaining a tiny bespoke runtime. The final machine build therefore uses a self-contained, stock-derived civilization operating substrate under the AEGIS-BYZ namespace, rather than loading the Promisory directory at runtime.

## Machine artifact

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\AegisProm\AEGIS-BYZ-FINAL-CIVOS.per`

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.

Observed artifact size: 36,141 lines / 1,167,233 bytes.
SHA-256 at assembly: `A593B33717D4E862E496FD1EF98694E5F862C974A3FEE368BBD1A3B66BBE2596`.

The artifact contains the full flattened HD civilization behavior corpus and the Byzantine-specific conditional path. Its runtime constant dependencies have been rehosted under `AegisProm\AEGIS-stock-*` rather than loaded from `Promisory`.

## Why this architecture

Forensic research established that the stock AI is a civilization operating system, not merely a strategy script. AEGIS must therefore preserve the operational depth required for worker management, construction, production, research, scouting, threat response, and late-game continuity while progressively replacing strategic policy with Byzantine cognition.

A tiny entry-point loader is not itself evidence of a tiny AI, but the previous 94 KB AEGIS-only runtime was also materially incomplete compared with the 36,141-line flattened civilization substrate. This assembly corrects that gap at the operational layer.

## Runtime safety

The untouched stock reference remains preserved in its original installation location. The AEGIS artifact is a separate derived file. No Promisory runtime load remains in the final civilization artifact after rehosting its three stock load dependencies.

## Qualification status

This assembly is a functional runtime build, not yet runtime-qualified. Static assembly evidence is recorded above. Actual game execution remains the authority for runtime approval.

The final qualification requirement is three independent reviews after live execution:

1. ABI/compiler/reverse-engineering review.
2. Byzantine strategy/civilization review.
3. Behavioral regression/adversarial AI review.

Runtime approval requires observed game behavior, not static file size or syntax alone.