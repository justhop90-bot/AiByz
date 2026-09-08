# AEGIS A1 Physical Tree Contamination QC — 2026-09-05

**Status:** IMPORTANT CORRECTION — runtime closure remains usable; physical root is not a pristine stock-only tree

## Finding

A direct recursive inspection of the installed `resources\_common\ai` tree found a project-specific artifact:

`testharness\scripts\AEGIS_FTS_CAL_001.fts`

The same physical tree also contains non-entrypoint directories such as `AoE2ScenarioParser-master`, `AiBuilder`, and `testharness`.

Therefore the 516-file physical directory must **not** be described as a pristine Steam-only package solely from the owner's restoration statement.

## Runtime consequence

This does **not** invalidate the current ABI closure audit.

The selected entrypoint `AI (HD version).per` resolves to only four imported files:

- `AI (HD version).per`
- `Promisory/defaultConstants.per`
- `Promisory/finaling.per`
- `Promisory/finalingConstants.per`

The project-specific `testharness` artifact is outside that import closure.

## Revised authority model

Use:

`A1 executable + A1 physical manifest + exact entrypoint import closure`

rather than treating every file physically present under `ai` as runtime authority.

For runtime ABI allocation, imported closure is the decisive boundary unless a separate engine mechanism proves otherwise.

For historical/physical archaeology, the 516-file tree is a mixed provenance corpus and must remain classified as such.

## Required follow-up

Do not delete or modify the extra files as part of this pass.
Preserve the current machine state and record the contamination explicitly.

The next qualification experiments should use disposable AI packages derived from the four-file runtime closure, not the entire mixed-provenance directory.
