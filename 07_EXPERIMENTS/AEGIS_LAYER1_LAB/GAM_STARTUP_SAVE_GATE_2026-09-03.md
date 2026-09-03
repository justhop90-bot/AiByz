# AEGIS GAM Startup-Save Gate — 2026-09-03

## Layer 1 status
**89% — unchanged. No causal proposition promoted.**

## Question
Can the native AoE2DE build enter a saved game automatically through the `GAM`
startup-save launch option when launched under the AEGIS runtime boundary?

## Prior evidence
Public launch-option references classify `GAM` as a startup save-game file.
This is not authoritative proof of the exact argument grammar on build
101.103.48987.0. The controlled executable hash is
`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`.

## Test GAM-001
Input save: the user's existing `-AUTOSAVE-.aoe2spgame`.
Arguments included `SKIPINTRO WINDOW NOMODS GAM=<absolute save path> EXIT=15`.
The exact executable hash was verified before launch. Native PID 31236 was
created and remained alive. A new AoE2DE log directory was created, but only
`Main.txt` appeared and it contained startup/menu initialization through player
profile loading; no native `MainLog.txt` was produced for this session.

## Test GAM-002
Arguments included `SKIPINTRO WINDOW NOMODS -autogame GAM=<absolute save path>
EXIT=15`. Native PID 36128 was created and remained alive. The resulting log
again contained only `Main.txt` with the startup sequence and did not establish
saved-game entry. The process command line independently confirmed both
`-autogame` and the `GAM=` argument.

## Test GAM-003 — Steam-mediated probe
A Steam `-applaunch 813780` invocation was issued with the same arguments. It did
not create a new AoE2DE process because PID 36128 was already alive. Therefore
this test is not evidence for or against Steam-mediated GAM behavior.

## Interpretation
Direct executable launch plus `GAM=<absolute path>` does **not yet establish**
a deterministic saved-game entry path. The experiment also does not establish
that absolute paths are the accepted grammar; `GAM` may expect a save filename
resolved through the native save-game search path. The current result is a
negative infrastructure result, not proof that GAM is unsupported.

## Next discriminating test
After the existing test process is safely cleared, repeat with a uniquely named
copy of `-AUTOSAVE-.aoe2spgame` placed in the normal user save-game directory,
and pass only the filename to `GAM`. Compare native logs and lifecycle behavior.
Do not infer scenario loading from process survival alone.

## Security
No DLL injection, hooks, debugger attachment, memory patching, or process
modification was used. The executable hash was verified. Game installation
remained an input source; experiment artifacts remained under the AEGIS run root.

## Promotion
**No Layer 1 percentage change. No causal claim promoted.**
