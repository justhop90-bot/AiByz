# Replay Forensic Record — Player 1 Villager Production Timeline

**Replay:** `rec.aoe2record`
**Player under test:** Player 1 — `AIByzBuild`
**Replay end:** 45:57.868
**Purpose:** Preserve the complete extracted Player 1 villager MAKE-command timeline for AEGIS economic-throughput qualification.

## Evidence boundary

This artifact records replay command-stream evidence. A villager `MAKE` command is a production command event, not proof of completed simultaneous unit count. Historical population and resource snapshots are not reconstructed here because the native `.aoe2record` command stream does not directly expose those values without engine replay.

Unit ID reconciliation used by the parser: `83 = Villager`.

## Timeline

| # | Timestamp | Pop | Interval | Class |
|---:|---:|:---:|---:|---|
| 1 | 0:00.028 | — | — | — |
| 2 | 0:50.630 | — | 50.602s | >40 |
| 3 | 1:15.964 | — | 25.334s | OK |
| 4 | 1:41.290 | — | 25.326s | OK |
| 5 | 2:57.966 | — | 76.676s | >40 |
| 6 | 3:57.940 | — | 59.974s | >40 |
| 7 | 4:48.620 | — | 50.680s | >40 |
| 8 | 5:49.966 | — | 61.346s | >40 |
| 9 | 6:39.272 | — | 49.306s | >40 |
| 10 | 7:31.942 | — | 52.670s | >40 |
| 11 | 8:21.276 | — | 49.334s | >40 |
| 12 | 9:04.622 | — | 43.346s | >40 |
| 13 | 9:34.618 | — | 29.996s | OK |
| 14 | 10:37.704 | — | 63.086s | >40 |
| 15 | 11:07.702 | — | 29.998s | OK |
| 16 | 11:40.386 | — | 32.684s | OK |
| 17 | 12:33.048 | — | 52.662s | >40 |
| 18 | 12:58.394 | — | 25.346s | OK |
| 19 | 13:26.380 | — | 27.986s | OK |
| 20 | 21:44.822 | — | 498.442s | TARGET / transition |
| 21 | 23:18.158 | — | 93.336s | INVESTIGATE |
| 22 | 24:03.504 | — | 45.346s | >40 |
| 23 | 24:29.170 | — | 25.666s | OK |
| 24 | 25:39.184 | — | 70.014s | >40 |
| 25 | 26:41.850 | — | 62.666s | >40 |
| 26 | 27:07.192 | — | 25.342s | OK |
| 27 | 27:32.682 | — | 25.490s | OK |
| 28 | 27:58.006 | — | 25.324s | OK |
| 29 | 28:23.368 | — | 25.362s | OK |
| 30 | 28:48.690 | — | 25.322s | OK |
| 31 | 29:35.362 | — | 46.672s | >40 |
| 32 | 30:01.002 | — | 25.640s | OK |
| 33 | 30:26.156 | — | 25.154s | OK |
| 34 | 30:51.480 | — | 25.324s | OK |
| 35 | 31:16.800 | — | 25.320s | OK |
| 36 | 31:42.142 | — | 25.342s | OK |
| 37 | 32:07.476 | — | 25.334s | OK |
| 38 | 32:32.808 | — | 25.332s | OK |
| 39 | 32:58.152 | — | 25.344s | OK |
| 40 | 33:23.492 | — | 25.340s | OK |
| 41 | 33:48.802 | — | 25.310s | OK |
| 42 | 34:14.118 | — | 25.316s | OK |
| 43 | 34:39.486 | — | 25.368s | OK |
| 44 | 35:04.806 | — | 25.320s | OK |
| 45 | 35:30.150 | — | 25.344s | OK |
| 46 | 35:55.482 | — | 25.332s | OK |
| 47 | 36:20.944 | — | 25.462s | OK |
| 48 | 36:46.278 | — | 25.334s | OK |
| 49 | 39:52.286 | — | 186.008s | >90 |
| 50 | 40:17.604 | — | 25.318s | OK |
| 51 | 40:42.944 | — | 25.340s | OK |
| 52 | 41:08.286 | — | 25.342s | OK |
| 53 | 41:33.604 | — | 25.318s | OK |
| 54 | 41:58.950 | — | 25.346s | OK |
| 55 | 42:29.628 | — | 30.678s | OK |
| 56 | 42:54.960 | — | 25.332s | OK |
| 57 | 43:19.626 | — | 24.666s | OK |
| 58 | 43:20.298 | — | 0.672s | OK |
| 59 | 43:44.960 | — | 24.662s | OK |
| 60 | 43:45.628 | — | 0.668s | OK |
| 61 | 44:10.286 | — | 24.658s | OK |
| 62 | 44:22.296 | — | 12.010s | OK |
| 63 | 44:35.610 | — | 13.314s | OK |
| 64 | 44:58.280 | — | 22.670s | OK |
| 65 | 45:08.284 | — | 10.004s | OK |
| 66 | 45:09.616 | — | 1.332s | OK |

## Qualification observations

- There are 66 Player 1 villager MAKE commands in the parsed command stream.
- The 13:26.380 → 21:44.822 interval is 498.442s. The bot's Dark Age policy target was 22 villagers; this interval overlaps the transition to Feudal at approximately 20:28.16 and is therefore treated as a target/age-transition interaction rather than a production-resource failure.
- The first substantial post-transition gap is 21:44.822 → 23:18.158 = 93.336s.
- The replay command stream does not prove the exact food bank at that time. RESOURCE is therefore a probable hypothesis, not a confirmed classification.
- A later 186.008s gap occurs at 39:52.286 and is not the first post-transition substantial gap.
- No source modification, commit, or deployment was performed as part of this forensic extraction.

## Related runtime facts

- Villager executor: `AIByzBuild/economy.per` uses `unit-type-count-total villager < desired-number-villagers`, gated by `can-train villager`, then `(train villager)`.
- Housing executor exists in `AIByzBuild/construction.per` and uses `population-headroom`, with `population-headroom = 2` in `constantsUP.per`.
- The current age-up escrow correction is commit `124c3d7` (`Fix escrow gate in age-up rules`).

## Status

**FORENSIC DATASET — READ-ONLY EVIDENCE**

This file is intentionally not a diagnosis or a code change. The next engineering decision must be based on the first classified post-transition interruption, with RESOURCE / HOUSING / TARGET / EXECUTOR / UNKNOWN evidence kept distinct.
