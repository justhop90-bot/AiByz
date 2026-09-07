# AEGIS Runtime Corrections

This file archives important corrections applied to the live AEGIS runtime. The live runtime must remain free of backup/copy artifacts; Git history is the preservation mechanism.

## 2026-09-07 — Operations scout ABI correction

**File:** `AegisProm/AEGIS-operations-final.per`  
**Line:** 115  
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652

### Defect

The scout route used the wrong operand class for `up-lerp-tiles`:

```per
(up-lerp-tiles aegis-ops-scout-point position-self-x c: aegis-ops-scout-radius)
```

### Correction

The live runtime was corrected to:

```per
(up-lerp-tiles aegis-ops-scout-point position-self-x g: aegis-ops-scout-radius)
```

This matches the verified stock form:

```per
(up-lerp-tiles scout-waypoint-x position-self-x g: scout-radius)
```

### Machine evidence

The corrected live line was re-read from the target installation after the edit and is physically present as:

```text
115  (up-lerp-tiles aegis-ops-scout-point position-self-x g: aegis-ops-scout-radius)
```

Current SHA-256 of the live Operations module at archival time:

`49170A45720DB2C1628DB777DFFA8D51BA593083F84F2770517EDA189B8BEC01`

### Qualification status

**ABI correction confirmed. Full Operations runtime qualification: NOT YET COMPLETE.**

This correction fixes the identified operand-class defect only. It does not prove the surrounding scout pipeline, timer behavior, search isolation, target selection, or action execution under the live interpreter.

### Preservation rule

No machine backup file was retained. This document and Git commit history are the canonical correction record.
