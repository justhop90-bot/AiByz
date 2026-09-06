# CAL_RUNTIME_LAUNCH_SURFACE_001 — Retail AI Execution Surface

## Result

**No qualified autonomous AI-match launch path established.**

## Experiments

1. `SCRIPT + SCRIPTREPORT + RUNNING_AUTOTEST` with the discovered FTS script: the retail process launched and remained alive, but no report was emitted and no test-harness listener was observed.
2. Adding `AIDEBUGGING` and `AISCRIPTDEBUGGING` did not produce a report; the process reached startup but did not advance to a match automatically.
3. `RANDOMGAME` / `RANDOMMAP` seeds were accepted as launch arguments but did not autonomously enter a match during the observation window.
4. `GAM` against a copied `-AUTOSAVE-.aoe2spgame`, both by absolute path and filename, caused the process to exit during early startup rather than establish a loaded game.

## Interpretation

The target build exposes a broad command-line surface, and independent documentation lists `AIDEBUGGING`, `AISCRIPTDEBUGGING`, `RANDOMGAME`, `RANDOMMAP`, `GAM`, `SCRIPT`, and `SCRIPTREPORT` as launch options. That documentation is useful discovery evidence, not proof that each option is semantically operational in this exact build/profile. The controlled workstation results above are the authoritative runtime observations for this project.

The remaining P0 blocker is therefore not the scalar goal itself. It is **reliable entry into a controlled AI-running match with the disposable package**.

## Next engineering target

Find or construct the smallest deterministic match-start path that:

- loads the disposable AI package;
- starts an actual simulation;
- lets the AI execute at least one rule;
- emits a replay or other independent evidence artifact;
- leaves the retail stock installation unchanged.

No runtime ABI claim should be promoted until that path exists.
