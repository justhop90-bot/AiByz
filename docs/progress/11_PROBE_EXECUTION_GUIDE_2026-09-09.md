# AEGIS Probe Execution Guide — 2026-09-09

**Purpose:** Practical instructions so a human can run the minimum lifecycle probes on the real game and produce evidence that can be committed back to the repository.

**Target game version:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## Why this matters

Static research is largely complete. The remaining critical unknown is how the engine actually behaves for:

- Goal / SN visibility across rules
- Train command → pending → confirmed (or failed)
- (Later) Build foundation lifecycle

These probes exist to answer those questions with real observations.

## Safety rules

- Probes are disposable. They must **never** be loaded by a production AEGIS root.
- Use a private / single-player test game.
- Prefer the simplest possible map (e.g. one Town Center, open resources).
- Record the exact game version and any AI debug settings you enable.

## Recommended order

1. **CL-1** (Goal mutation visibility) — safest, no world interaction.
2. **CL-3** (Train villager lifecycle) — the most important for the civilian vertical slice.
3. CL-2, CL-4, CL-5 as time allows.

## How to run a probe (high level)

1. Copy the chosen skeleton from `docs/progress/probes/` into a temporary AI folder that the game can load (or use the game’s AI script loading method you already use for testing).
2. Give the probe a unique AI name so it cannot be confused with stock or AEGIS production files.
3. Start a controlled single-player game on the target version.
4. Enable AI logging / debugging if available (`AIDEBUGGING`, `LogSystems=AIScript`, etc.).
5. Observe:
   - Chat messages (if the probe uses `chat-to-all`)
   - Any log files the game writes
   - Manual confirmation of villager count / pending production where relevant
6. Write an evidence record (see template below) and commit it under `docs/progress/evidence/` or similar.

## Evidence record template (copy for every run)

```markdown
# Probe Evidence — <PROBE-ID> — <YYYY-MM-DD>

- Target build: 101.103.48987.0 / BuildID 24094652
- Script file + SHA-256:
- Probe ID: CL-?
- Map / starting conditions:
- Debug settings used:

## Expected behavior
...

## Observed behavior
...

## Logs / screenshots / notes
...

## Interpretation + confidence
...

## Falsification / residual uncertainty
...

## Architectural consequence
...
```

## What success looks like for CL-3 (most important)

You can clearly show at least one clean path of:

`authorized → issued (train command) → pending objects visible → villager census increased`

**or** a clean failure path where pending disappears without a census increase and the probe marks failure.

Three successful (or cleanly failed) controlled runs are enough to start treating the civilian vertical slice as having basic lifecycle observability.

## After you have evidence

Commit the evidence files and tell the AI agent. The residual-risk document and vertical-slice contract can then be updated, and limited production-oriented coding can begin under the rules already written.
