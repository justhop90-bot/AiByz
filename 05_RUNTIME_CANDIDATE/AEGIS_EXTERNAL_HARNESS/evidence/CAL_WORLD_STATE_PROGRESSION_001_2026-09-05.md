# CAL_WORLD_STATE_PROGRESSION_001 — Target-Build World-Time Progression

**Date:** 2026-09-05  
**Classification:** PROVEN runtime observation / semantic qualification still open  
**Build:** AoE2DE `101.103.48987.0`, Steam BuildID `24094652`, exe SHA-256 `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`  
**CaptureAge:** 1.25.0  
**Replay:** `MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`  
**Replay SHA-256:** `41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

## Objective

Close the immediate runtime gate after frame-stream discovery: demonstrate that the target-build CA:DE/UnCage runtime does not merely publish render frames, but exposes a progressing **world-time signal** while the canonical replay is actually running.

## Acquisition path

The replay was loaded through CaptureAge's normal replay path. The CaptureAge worker log records:

- `19:49:48.841` — `gameIntegration/loadReplay` from CA:DE
- `19:49:49.861` — worker launched `AoE2DE_s.exe`
- `19:49:49.919` — game PID `23788` invoked
- `19:50:37.271` — worker told the game to load the canonical replay
- `19:50:51.888` — replay speed temporarily `Paused`
- `19:50:52.463` — `gameStart`
- `19:51:06.412` — replay speed `Fast`
- `19:51:07.402` — replay speed `Paused`
- `19:51:07.958` — `apiMetrics` reported `worldTime=8502`
- `19:51:11.391` — replay speed `Slow`
- `19:51:12.226` — replay speed `Normal`
- `19:52:07.950` — `apiMetrics` reported `worldTime=107653`
- `19:53:07.954` — `apiMetrics` reported `worldTime=209053`
- `19:53:21.256` — publisher subscriber ended
- `19:53:21.256+` — repeated `UNAVAILABLE: read ECONNRESET` observations

This establishes that world time changed substantially during one target-build replay session: `8502 → 107653 → 209053`.

## Quantitative progression

| Observation | Wall-clock log time | worldTime | Delta from prior |
|---|---:|---:|---:|
| A | 19:51:07.958 | 8,502 | — |
| B | 19:52:07.950 | 107,653 | +99,151 |
| C | 19:53:07.954 | 209,053 | +101,400 |

The two one-minute wall-clock intervals therefore produced large, monotonic world-time advances. This is not render-frame cadence: it is a distinct game/runtime time signal emitted by CA:DE's runtime metrics path.

## Replay-timeline cross-check

The canonical replay body was parsed with mgz-fast. Its ACTION records contain a `sequence` field that matches the cumulative SYNC increment stream used by the AEGIS replay index. Around the CA:DE observations:

### worldTime = 8,502
Nearest replay ACTION sequence values:

- `8,216` — `DE_QUEUE`, player 2, unit 83
- `8,632` — `MOVE`, player 1
- `8,632` — `DE_QUEUE`, player 2, unit 83

### worldTime = 107,653
Nearest replay ACTION sequence values:

- `104,910` — `DE_QUEUE`, player 2, unit 83
- `110,591` — `MOVE`, player 2
- `112,021` — `MOVE`, player 2

### worldTime = 209,053
Nearest replay ACTION sequence values:

- `206,674` — `ORDER`, player 2
- `208,910` — `MOVE`, player 1
- `209,118` — `MOVE`, player 1
- `210,535` — `ORDER`, player 1

Most importantly, the `209,053` CA:DE world-time observation falls directly between replay ACTION sequence values `208,910` and `209,118`, only 65 raw sequence units from the latter.

## What this proves

**PROMOTE:**

1. The target retail build exposes a runtime `worldTime` signal through the CA:DE runtime integration.
2. `worldTime` advances over an actively loaded replay session; it is not merely a static frame/render counter.
3. The advancing world-time observations occupy the same numeric timeline neighborhood as the replay's parsed ACTION/SYNC sequence values.
4. World-time progression is therefore now a viable bridge variable for the next qualification step: correlating runtime state with replay commands.

## What this does NOT yet prove

1. Do **not** rename the field to `world_time_ms` yet. The observations are strongly consistent with milliseconds, but this experiment did not independently establish the unit contract from an authoritative protocol/type definition.
2. `worldTime` is not yet proven to be the same semantic clock as the replay parser's raw SYNC units. The numerical alignment is strong corroboration, not a formal identity proof.
3. `applyPatchId`, `gameStateId`, and individual entity state were not captured in this particular progression artifact.
4. `DE_QUEUE → CREATED` is still unqualified. A command occurring near a world-time observation is not completion evidence.
5. `BUILD → REALIZED` is still unqualified.

## Failure / termination note

The session eventually terminated its publisher stream at approximately `19:53:21`, with repeated `14 UNAVAILABLE: read ECONNRESET` errors. This is a runtime-session failure/teardown observation, not evidence that the world-time mechanism itself is invalid. The CA:DE log also recorded a renderer-side reactive-map error (`Expected to find a reactive map entry for key 3384`) shortly before termination.

## Next gate

Run a fresh controlled progression capture with the runtime publisher observed continuously and explicitly collect:

`worldTime + lookaheadWorldTime + applyPatchId + lookaheadApplyPatchId + gameStateId + frame handle + loopCount`

Then select a short interval containing a known `DE_QUEUE` and attempt the first **non-adjacency** lifecycle correlation against actual entity/state publication. Completion stages remain UNKNOWN until creation/realization is directly evidenced.

## Source

Primary source: `C:\Users\justh\AppData\Roaming\CaptureAge\logs\main.log` from the target-machine run described above. Replay source is the canonical calibration replay named above.
