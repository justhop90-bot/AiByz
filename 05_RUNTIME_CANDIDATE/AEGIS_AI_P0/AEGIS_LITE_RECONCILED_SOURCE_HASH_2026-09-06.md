# AEGIS-Lite Reconciled Source Hash Record — 2026-09-06

## Binding

- Target AoE2DE: `101.103.48987.0`
- Steam BuildID: `24094652`
- Executable: `AoE2DE_s.exe`
- Executable SHA-256: `6378CA6F1BFD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Branch: `aegis/external-harness-v1-2026-09-05`
- Reconciled source HEAD before this record: `447b086bbbe9915988c6f13f3428126053625d0b`

## Authoritative production closure

The package hash is computed from the UTF-8 text manifest formed by sorting these eight paths lexicographically and concatenating `path|bytes|sha256` with LF separators.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `AEGIS-BYZ.per` | 6630 | `4371F968BD122DC59B7AD1352545A6F3D106455044D7F40F76C45A7CCC73E7FB` |
| `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per` | 4896 | `CC674A7D51CB45F218A5609D7291754FDB334F6D47274FA063DE50DD00F34F44` |
| `AegisProm/Aegis-belief.per` | 3206 | `6F27506AA23F5FDADEF724D794A52D72DD0EBDE6D8BA416470EBC7B44BEC4900` |
| `AegisProm/Aegis-commitment.per` | 3355 | `280C1E3F99F7E53FCE1055806F3C9CB5DDF1C6FB1C78DEE3C6A3C2F3D5ACF025` |
| `AegisProm/Aegis-decision.per` | 3978 | `642DBC991893325574E9EE2757B268D39757079673A4E6B4C5F231C7447CE6A4` |
| `AegisProm/Aegis-objectives.per` | 3881 | `38E0DFDCE16BA3B7A0E0172559FD1568E5B7C09E5E05C0778F56D0FCBA506B48` |
| `AegisProm/Aegis-planning.per` | 3619 | `E6113EA519AA47F318DB872F596BF9A20AECC9F4C0D0C75DE386C1662013BC6C` |
| `AegisProm/Aegis-situation.per` | 3439 | `7A2BB09AC17850CB5526EA746AD6C6D3EDA5437AE934C3436589E4D0703F71C6` |

## Closure manifest hash

`6F9533CFD5DF3B3BD9C0AE95AA16A6DEBA153AABDDA0814E8AED00C3076EA4EC`

## Non-closure instrumentation

`AegisProm/Aegis-generation-probe.per` is deliberately not part of the production closure. It remains experimental instrumentation for generation propagation qualification.

Current probe SHA-256:

`3378C025C43512D5168DCE3DE1F95D0414BC2CCA9FF17F7B57756B7D9DC87790`

It must not be included in the production package hash unless explicitly promoted by a later qualification record.

## Preserved pre-reconciliation artifacts

### Machine-tested P2 before reconciliation

Path:
`AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`

Pre-reconciliation SHA-256:

`667F7C6F36A7537606DD087E52DAC7147DE34F7B927852E49D6F2CF0088629A`

Disposition: preserved in Git history; replaced only after structural ownership reconciliation.

### Superseded unloaded Carpenter

Path:
`AegisProm/Aegis-carpenter.per`

SHA-256 before removal:

`27A97A7C3C2195E1F83E6142DFF67F7977140D3D0881662D91A470B263F5A2BD`

Disposition: removed from active branch because it was not loaded and created an ambiguous second Carpenter implementation. Recoverable through Git history.

## Evidence classification

- Source hashes: **PROVEN** for the recorded GitHub tree and target-machine audit worktree.
- Recursive closure: **PROVEN** by target-machine audit run.
- Zero duplicate declarations: **PROVEN** by target-machine audit result.
- Executable hash: **PROVEN** on target machine.
- Engine load of this reconciled package: **UNKNOWN** until controlled runtime installation/launch.
- Sensor semantic correctness: **UNKNOWN** pending qualification.
- End-to-end generation propagation: **UNKNOWN** pending experiment.
- Stale-generation rejection: **UNKNOWN** pending experiment.

This record is provenance, not a runtime qualification claim.
