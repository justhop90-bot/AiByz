# AEGIS / AiByz — Agent Instructions

## Mandatory first read

Before changing this repository, read:

1. `AGENT_SESSION_CONTRACT.md`
2. `AI_OPERATING_PROTOCOL.md`
3. `AI_AGENT_START_HERE.md`
4. `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`
5. the relevant current file under `docs/progress/`

## Authority

- `main` is the only canonical branch.
- Historical `aegis/*`, `lab/*`, `qc/*`, and `research/*` refs are not current authority.
- Never infer authority from a branch name, commit message, filename, or apparent completeness.

## Engineering constraints

- Target is AoE2DE `101.103.48987.0` / BuildID `24094652` / Update `#180059`.
- Scope is pure `.per`; XS is out of scope.
- Do not modify the untouched stock `resources\\_common\\ai` baseline during acquisition or qualification.
- Production `.per` remains gated until the current authority says the required proof gates are closed or residual risk is explicitly accepted.
- Candidate files under `implementation/` are not production roots unless explicitly promoted by current authority.

## Evidence discipline

Do not convert plausibility into fact. Separate command issued, accepted, pending, created, available, and effective. Separate source declaration from runtime load. Record evidence class, world level, status, source, and falsifier for substantive claims.

## Scope discipline

Do not restart broad Layer-1/Layer-2 archaeology. Do not resurrect ADprom, byzwarcouncil, XS, or scenario-loader automation. Search historical material only when it is needed to answer a specific current proof question.

## Change discipline

Prefer the smallest reversible change that closes a named gap. Update existing canonical documentation rather than creating parallel handoffs. If authority conflicts or a required engine semantic is unproven, stop and document the blocker rather than guessing.

## Current priority

The primary vertical slice is **Civilian Production Loop**. Cavalry Threat Containment is secondary/deferred. Current qualification gates are tracked in the Final Audit and `docs/progress/`.
