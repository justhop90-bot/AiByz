# Layer 2 Pass 20 — Deep QC / Correction

**Date:** 2026-09-04  
**Status:** ACCEPT WITH CORRECTIONS — corrected working canon  
**Scope:** replay/parser/state-reconstruction boundary  

## QC verdict

Pass 20 was directionally correct but overstated what had been established about the `.aoe2record` format itself. The evidence securely establishes a parser/normalized-output boundary; it does **not** exhaust the raw recording format.

## Required corrections

### 1. Separate four layers

Use the following forensic model:

`L0 RAW RECORDING → L1 PARSER DECODING → L2 NORMALIZED EVIDENCE → L3 STATEFUL RECONSTRUCTION`

The tested evidence establishes that `L2 != L3`. It does not prove that `L0` is exhausted.

### 2. Narrow the W2 conclusion

Correct claim:

> The tested parser implementations do not expose a sufficiently rich dynamic object-state representation to close individual W2 lineage.

Do **not** claim:

> The `.aoe2record` format contains no richer lifecycle information.

That remains OPEN.

### 3. Correct CREATE interpretation

`CREATE` being present in the parser enum proves parser capability only. Its absence from the reference recording means it cannot be used as an object-birth bridge for this specimen. Its semantic identity remains unresolved.

### 4. Correct unknown-opcode interpretation

Unknown DE enum entries are reverse-engineering targets, not evidence that lifecycle data exists. The reference ACTION stream must be tested for their actual occurrence before assigning semantics.

### 5. Correct H1 evidence language

The proposition that mgz-fast normalization alone explains the W2 gap is **rejected as a sufficient explanation**, not logically disproven in every respect.

### 6. Preserve parser/executor distinction

A replay parser is an evidence decoder. A stateful replay interpreter is a separate system that applies validated transition semantics over time. A full AoE2 simulator is not yet justified.

## Canonical W2 model

`W0 = command/event evidence`  
`W1 = authoritative accepted/pending state`  
`W2 = authoritative world-state realization`  
`W3 = operational capability`  
`W4 = strategic effect`

Each level must additionally carry an epistemic status such as `OBSERVED`, `INFERRED`, or `UNKNOWN`.

## Escalation rule

Before building any bespoke simulator:

1. inspect raw replay opcode coverage;
2. inspect existing playback/state-reconstruction implementations;
3. test whether they expose object-level observations equivalent to historical `.per` object-data channels;
4. only then consider a minimal deterministic state interpreter.

The scenario-loader remains retired and is not reopened by this correction.

## Disposition

**Pass 20: ACCEPT WITH CORRECTIONS.** The pass remains valuable as the parser-boundary foundation, but the raw-format conclusion is explicitly left open pending direct binary/lifecycle archaeology.