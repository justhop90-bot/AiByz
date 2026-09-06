# AEGIS Repository Baseline — 2026-09-06

## Authoritative source

Branch: `aegis/architecture-completion-2026-09-06`

Baseline HEAD: `ac508f0` (`docs: final AEGIS-Lite engineering handoff to next lead`)

Upstream at baseline: `origin/aegis/external-harness-v1-2026-09-05`

The working tree was normalized from the detached experimental checkout onto the
latest upstream reconciliation before further architecture work.

## Production P0 closure

The authoritative eight-file closure is the `AEGIS-BYZ.per` entrypoint plus the
seven loaded AegisProm modules documented by the P0 build-status record.

The channel-aware audit reports 8 closure files, 129 declaration rows, 129 unique
symbols, 237 resolved goal operands, and zero resolved high-goal operands.

## Experimental material

Runtime parses, replay extracts, and local audit scratch material are kept outside
the Git working tree under `C:\Users\justh\AEGIS-EVIDENCE-ARCHIVE-2026-09-06`.

Experimental probes remain separate from the production closure and must not be
loaded implicitly by `AEGIS-BYZ.per`.

## Live /ai discrepancy

The live target previously contained `AEGIS-BYZ-Architect-P1.per` rather than the
canonical `AEGIS-BYZ.per`. Its normalized text matched the canonical entrypoint,
but its filename and line-ending representation differed. The live tree was
snapshotted before any corrective deployment.

Live AEGIS module hashes also differed from the canonical source hashes because of
representation differences; source-to-target deployment must use an explicit
manifest rather than filename assumptions.

## Engineering gate

No Execution, Verification, or Recovery implementation is promoted until the
World Model publication/generation contract and sensor UNKNOWN/zero/absence
semantics have been runtime-qualified on the target build.
