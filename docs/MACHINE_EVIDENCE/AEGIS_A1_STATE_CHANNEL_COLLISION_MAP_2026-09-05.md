 # AEGIS A1 State-Channel Collision Map — 2026-09-05

## Purpose

This is an evidence-only join of the complete A1 typed state census. It maps numeric defconst declarations to symbolic names, inferred state-channel kind where the census has an operation record, source file/line, and observed state-operation occurrence count.

**No AEGIS goal/SN/timer/flag allocation is authorized by this document.** Numeric equality is not treated as semantic ownership.

## Summary

- **capture_utc:** 2026-09-05T06:59:11.409275+00:00
- **source:** docs/MACHINE_EVIDENCE/AEGIS_A1_TYPED_STATE_CENSUS_2026-09-05.json
- **numeric_declaration_rows:** 4893
- **unique_symbols:** 1456
- **unique_numeric_values:** 756
- **values_with_multiple_symbols:** 257
- **state_value_domain_0_511:** 322
- **note:** Evidence-only collision map. No AEGIS numeric channel is allocated or authorized by this artifact.

## Method

1. Start from every numeric declaration in the committed A1 typed state census.
2. Preserve symbol, numeric value, file, and source line.
3. Join symbols against the census operation maps for goal/SN/timer to show observed runtime-state usage frequency where available.
4. Group by numeric value to expose multiplexing/collision pressure.
5. Treat values 0–511 as a state-domain collision surface, not as free space.

## Engineering conclusion

The correct next ABI question is not “which number is unused?” It is “which symbol/value/context has compatible ownership, lifetime, type, and write/read behavior for the intended AEGIS field?”

The complete machine-readable join is in `AEGIS_A1_STATE_CHANNEL_COLLISION_MAP_2026-09-05.json`.
