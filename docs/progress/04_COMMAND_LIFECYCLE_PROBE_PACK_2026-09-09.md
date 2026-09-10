# AEGIS Command Lifecycle Probe Pack — 2026-09-09

**Status:** Design + skeleton scripts ready for target-build execution  
**Parent:** FINAL_RECONSTRUCTION_AUDIT R5 + ABI_PROBE_PLAN_2026-09-08  
**Goal:** Produce the minimum observable evidence that distinguishes  
`ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE`

## Design principles

- One proposition per probe.
- Disposable, retail-safe scripts.
- Explicit generation and validity.
- Never equate command issuance with success.
- Capture both controller state and independent world observation where possible.
- Use official DE debugging facilities when available (AIDEBUGGING, LogSystems=AIScript, etc.).

## Probe set (minimum viable)

### Probe CL-1 — Goal mutation visibility
Question: After rule A writes a goal, when can rule B observe the new value?  
Variants: adjacent rule, timer-separated, jump-separated, next full pass.

### Probe CL-2 — Strategic-number mutation visibility
Same question for a dedicated probe SN.

### Probe CL-3 — Train villager lifecycle
Issue a single `train` / `up-train` under controlled conditions.  
Observe:
- command issued (controller)
- pending production signal (if available)
- civilian / villager census change
- failure case (pending disappears without census increase)

### Probe CL-4 — Build foundation lifecycle
Issue a single simple build.  
Observe foundation appearance, progress if available, completion or failure.

### Probe CL-5 — Timer and jump interaction
Minimal finite-state machine using enable-timer and up-jump-rule to establish re-entry and visibility boundaries.

## Required evidence record for every run

- Target build identity and executable hash
- Script SHA-256
- Probe ID
- Expected vs observed behavior
- Log / debug excerpts
- Interpretation + confidence
- Falsification condition
- Architectural consequence

## Skeleton scripts

See `docs/progress/probes/` directory:
- `CL1_goal_mutation_visibility.per`
- `CL3_train_villager_lifecycle.per`

These are skeletons only. They must be completed with safe constants and instrumentation before use, and must never be loaded by production roots.

## Success criteria for closing R5 for first vertical slice

At least CL-3 (and preferably CL-4) must produce repeatable, documented distinction between issued, pending, and confirmed creation on the target build.  
Until then, any production code that assumes later lifecycle stages remains under residual risk.
