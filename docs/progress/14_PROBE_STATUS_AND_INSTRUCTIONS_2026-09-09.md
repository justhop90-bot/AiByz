# Probe Status & Simple Instructions — 2026-09-09

## What changed

The earlier probe files were only skeletons. They loaded without errors but did almost nothing visible.

CL-1 and CL-3 have now been rewritten into **complete, chatty, runnable tests**.

## How to test (simple version)

1. Download / use the new versions of:
   - `docs/progress/probes/CL1_goal_mutation_visibility.per`
   - `docs/progress/probes/CL3_train_villager_lifecycle.per`

2. Load **one probe at a time** as a test AI in a normal single-player game.

3. Watch the **game chat**. The probes will talk to you.

### What you should see

**CL-1 (easy test)**  
You should see messages similar to:
- `CL1: Probe starting...`
- `CL1: Wrote value 42`
- `CL1: SUCCESS - Value 42 is visible`
- `CL1: Probe finished - Goal mutation works`

**CL-3 (villager test)**  
You should see messages similar to:
- `CL3: Probe starting - Villager train test`
- `CL3: Baseline villager count captured`
- `CL3: Train command ISSUED`
- then either:
  - `CL3: PENDING villager detected in queue` → `CL3: SUCCESS - New villager appeared`
  - or a failure message if something blocked training (not enough food, etc.)

## Important notes for CL-3

- You need at least 1 Town Center.
- You need enough food (50+) and population space.
- If the probe says it cannot train, that is still useful information — just make sure you have food and a TC, then try again.

## What to tell me after you run them

Just reply with what the chat said. For example:

- “CL1 showed the success messages”
- “CL3 said Train command ISSUED then SUCCESS”
- or copy any failure messages you saw

That is enough for me to update the project and continue.
