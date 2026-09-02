# FINAL PUBLICATION SAFETY QC GATE — 2026-09-02

## Status

**Binding engineering gate for public repository publication and executable-derived research artifacts.**

This document supplements the authoritative `PUBLICATION_AND_RIGHTS_CONTROL_STANDARD_2026-09-02.md`. It does not replace or weaken the P0–P6 publication classes.

## 1. Highest-level rule

> **No technical usefulness, scientific value, convenience, prior publication, tool capability, or user request is sufficient by itself to authorize an operation or publication.**

Every sensitive operation must separately satisfy:

`AUTHORIZATION -> SAFETY -> EVIDENCE -> MINIMUM DISCLOSURE -> PUBLICATION RIGHTS -> AUDITABILITY`

Failure or material uncertainty at any gate means:

`STOP / WITHHOLD / INVESTIGATE`

## 2. Separation of permissions

The project must never collapse these questions into one:

1. **May we access/analyze it?**
2. **May we transform it?**
3. **May we retain the resulting artifact?**
4. **May we publish the resulting artifact?**
5. **May others receive, reproduce, or redistribute it?**

Permission at one level does not automatically establish permission at another.

## 3. Native-analysis safety boundary

For proprietary game executables and related native material:

- preserve the original input unchanged;
- record identity/hash and acquisition provenance;
- use controlled or disposable analysis environments where practical;
- do not execute unknown extracted artifacts merely to inspect them;
- do not bypass DRM, authentication, anti-cheat, access controls, or license enforcement without a separate lawful authorization basis;
- do not publish the executable, DLLs, assets, bulk binary dumps, private symbols, or substantial copied/decompiled implementation absent an established publication right;
- treat addresses, symbols, strings, signatures, calling conventions, and structural findings as potentially sensitive rather than automatically safe;
- prefer original descriptions, measurements, hashes, and reproducible procedures.

A Ghidra-generated artifact is not presumed project-owned, publication-safe, or legally redistributable merely because the project generated it.

## 4. Evidence discipline

The Layer 1 evidence ladder remains authoritative for epistemic status. The E0–E4 handling labels supplement it.

Never promote:

- a string to an implementation;
- a declaration to an implementation contract;
- a decompiler rendering to verified source;
- a parser observation to complete native state;
- a command issuance to execution success;
- execution success to strategic success;
- absence to destruction;
- a failed search to proof of absence;
- a numeric match to namespace identity;
- a tool result to truth without corroboration.

Every material conclusion must identify observation, inference, uncertainty, and unresolved alternatives where applicable.

## 5. Least-sensitive representation test

Before publication, attempt the following substitutions in order:

`UNDERLYING ARTIFACT`

-> `SANITIZED DERIVATIVE`

-> `MEASUREMENT`

-> `ORIGINAL STRUCTURAL DESCRIPTION`

-> `HASH + PROVENANCE`

-> `PUBLIC REFERENCE`

Use the least sensitive representation that still satisfies the engineering objective.

If publication of the underlying artifact provides no necessary additional reproducibility value, do not publish it.

## 6. Rights provenance

A rights-dependent publication decision must be reconstructable later. Record, as applicable:

- source and origin;
- creator/rightsholder;
- license/permission/basis;
- scope of permission;
- attribution requirements;
- verification date;
- reviewer;
- limitations or expiration;
- exact artifact/version reviewed;
- resulting P0–P6 classification.

When rights cannot be established confidently, the artifact remains restricted.

## 7. Public-repository threat model

Assume that anything placed on a public Git ref may be:

- indexed;
- cloned;
- forked;
- cached;
- mirrored;
- archived;
- quoted;
- incorporated into another project.

Therefore, a public commit is treated as an intentional disclosure event, not as temporary storage.

Deletion or history rewriting is remediation, not proof that every prior copy has vanished.

## 8. Automated screening plus human review

Before publication of sensitive or executable-derived material:

- run appropriate automated secret/sensitive-data scans;
- inspect prohibited file types and suspicious generated artifacts;
- inspect local paths and identifiers;
- review binary/decompiler/string extraction outputs for accidental over-disclosure;
- perform human publication review.

Automated scanners are not legal review, authorization evidence, or proof of absence.

## 9. Change-control and re-review

Re-review is mandatory when:

- new evidence changes the interpretation;
- ownership or license information changes;
- a restricted artifact is transformed into a new representation;
- a branch becomes public;
- a release/tag is created;
- repository ownership or hosting changes;
- a previously published artifact is discovered to contain additional sensitive material;
- a policy is strengthened in a way that reveals an earlier decision was under-controlled.

Policy improvement never retroactively grants a missing right.

## 10. Incident response

If inappropriate material is published:

`STOP -> IDENTIFY -> CONTAIN -> ASSESS -> REMEDIATE -> VERIFY -> DOCUMENT -> PREVENT`

Secrets receive immediate revocation/rotation where applicable. Personal/security-sensitive exposure receives priority containment. History remediation must be considered separately from current-tree cleanup.

No engineer may claim complete eradication without evidence supporting that claim.

## 11. Engineering integrity rule

When evidence, authorization, rights, or safety are uncertain, the engineer must be conservative even when that delays the research.

A slower legitimate result is preferable to a faster result obtained through unauthorized access, unsafe execution, unjustified inference, or inappropriate disclosure.

## 12. Final decision matrix

| Question | Pass condition | Failure action |
|---|---|---|
| Authorization | Specific basis understood | Stop |
| Safety | Operation is controlled and non-destructive | Stop/minimize |
| Evidence | Claim is supported and classified | Downgrade/investigate |
| Privacy/security | No unjustified exposure | Withhold/redact |
| Rights | Publication basis established | Restrict |
| Necessity | Disclosure is justified | Use less-sensitive form |
| Provenance | Source and transformation traceable | Do not publish |
| Reproducibility | Result can be independently reconstructed without restricted material where practical | Improve method |
| Review | Required human QC completed | Do not publish |

## 13. Final professional standard

> **We do not ask only whether we can obtain an answer. We ask whether we are authorized to obtain it, whether obtaining it is safe, whether the evidence actually supports it, whether we can preserve the result with less disclosure, whether publication is authorized, and whether another engineer can audit the decision later.**

The correct default under unresolved material uncertainty is not optimism. It is controlled restraint.

## Scope limitation

This is an engineering governance standard, not legal advice. Questions involving copyright, contract, license interpretation, reverse engineering, interoperability, privacy, security, platform rules, or jurisdiction-specific law may require qualified legal review. The project must not treat this document as creating rights that do not otherwise exist.
