# AEGIS Engineering Safety & Authorization Standard — 2026-09-02

## Status

**Mandatory project control.** This standard governs native archaeology, reverse engineering, replay research, runtime experimentation, analysis tooling, and repository publication.

It supplements — and does not replace — `PUBLICATION_AND_RIGHTS_CONTROL_STANDARD_2026-09-02.md`.

## Purpose

The project must be useful **without becoming careless**. Technical capability does not establish authorization. An analysis result does not automatically establish a publication right.

The governing rule is:

> **Do not perform, retain, publish, or operationalize an action unless its technical purpose, authorization basis, and safety/publication boundary are understood. When uncertain, stop the risky path and preserve only the minimum safe research record.**

## 1. Four separate gates

Every nontrivial operation is evaluated against four distinct questions:

1. **Technical:** Can the operation be performed reliably and safely?
2. **Authorization:** Are we authorized to perform it in this environment and for this purpose?
3. **Evidence:** Does the resulting evidence actually support the claim being made?
4. **Publication/use:** Is this particular representation appropriate and authorized for the intended use?

A pass at one gate never implies a pass at another.

In particular:

- possession is not ownership;
- access is not redistribution permission;
- tool output is not implementation proof;
- technical usefulness is not publication justification.

## 2. Authorization boundary

The project assumes only authority actually established by available facts.

Possession or local access to an executable is not treated as blanket permission to redistribute it, publish extracted proprietary code, disclose private material, circumvent access controls, or interact with systems outside the authorized environment.

Analysis must remain within the user's authorized environment and applicable platform, license, contractual, and legal boundaries. If authorization becomes uncertain, the operation is paused rather than rationalized.

No project document may state or imply that reverse engineering, copying, publication, redistribution, or circumvention is legally permitted merely because a tool can technically perform it.

## 3. Ghidra safety and provenance rule

Ghidra is an analysis instrument, not a source of automatically publishable material.

Every material native-analysis output receives two independent labels before durable use:

### Evidence level

- **E0 — controlled input:** original local artifact; restricted by default.
- **E1 — tool observation:** directly produced by an analysis tool; not automatically semantic proof.
- **E2 — reproduced observation:** independently reproduced by a second controlled method/configuration.
- **E3 — verified native mechanism:** implementation-level evidence sufficient to support the stated proposition.
- **E4 — runtime corroboration:** controlled runtime behavior independently supports the proposition.

These labels supplement, rather than replace, the Layer 1 evidence ladder.

### Publication/handling class

Use the existing P0–P6 publication classes defined by the publication standard. This document does **not** redefine those classes.

As an operational shortcut:

- **Public derived** → normally P0/P1 after the publication checks pass.
- **Restricted** → normally P2/P3/P4/P5/P6 as applicable.
- **Unresolved** → remains P2 or the stricter applicable class until rights/sensitivity are established.

When classifications conflict, the **more restrictive handling rule wins** and the underlying publication standard controls.

The preferred public representation of proprietary native archaeology is:

`LOCAL EXECUTABLE -> CONTROLLED ANALYSIS -> ORIGINAL OBSERVATION -> ORIGINAL TECHNICAL DESCRIPTION`

not:

`LOCAL EXECUTABLE -> BULK EXTRACTION -> PUBLIC REDISTRIBUTION`

## 4. Prohibited default publication

Without an established publication basis, do not publish:

- copies of the game executable or DLLs;
- bulk binary or memory dumps;
- substantial decompiled/disassembled proprietary code;
- private/proprietary symbols or recovered source;
- extracted game assets;
- credentials, tokens, keys, account information, or private identifiers;
- private correspondence or unrelated personal information;
- raw replay collections whose ownership/privacy/publication status is unclear.

Even a technically small native artifact can remain restricted when its context, sensitivity, contractual status, or publication basis is unclear.

If the research conclusion can be preserved using an original description, measurement, hash, provenance record, or appropriately scoped reference, that representation is preferred.

## 5. Least-sensitive-representation principle

Before publishing executable-derived material, ask:

> **Can the engineering objective be achieved with a less sensitive representation?**

Prefer, where sufficient:

`hash + provenance + address/range + measurement + original explanation`

over

`binary dump + copied disassembly + proprietary implementation text`.

The objective is not to suppress useful research. It is to preserve the research value while minimizing unnecessary redistribution of third-party material.

## 6. Evidence discipline

The following distinctions are mandatory:

- native vocabulary is not implementation proof;
- a decompiler rendering is not verified source;
- a string reference is not a call graph;
- a recovered address is not automatically a public identifier;
- a parser field is not automatically native state;
- a failed search is not proof of absence;
- tool capability is not authorization;
- local access is not redistribution permission;
- command issuance is not execution success;
- execution success is not strategic postcondition success.

Critical conclusions require evidence appropriate to the proposition. When an analysis result is weaker than the claim it is being used to support, the **claim is demoted** rather than the evidence being rhetorically upgraded.

## 7. Tool-operation safety

Before a new invasive or destructive operation, establish:

1. exact target;
2. technical purpose;
3. authorization basis;
4. expected side effects;
5. preservation/rollback method;
6. evidence classification;
7. publication/handling classification;
8. independent verification method.

Never overwrite the only copy of an authoritative source artifact or historical analysis project. Preserve cryptographic hashes and provenance before transformation. Prefer disposable analysis projects for experiments.

Destructive repository operations require a verified recovery/provenance record and independent post-operation verification.

## 8. Repository publication gate

Before any new public artifact is committed, the engineer must answer the publication questions established by the publication standard:

- origin;
- ownership/publication basis;
- license or permission where applicable;
- third-party content;
- personal/private information;
- secrets/security material;
- derivation from restricted material;
- necessity of publication;
- provenance reproducibility.

If a material-rights or sensitivity question remains unresolved, publication stops at the applicable restrictive class.

The repository's public visibility does not change this requirement.

## 9. Pre-commit safety review

Before committing material derived from native archaeology, replay data, runtime logs, or third-party sources, perform a lightweight review appropriate to the artifact:

### Content scan

Check for:

- executable/binary material;
- large decompiler/disassembly excerpts;
- copied third-party source;
- embedded assets;
- secrets/credentials/tokens/keys;
- personal identifiers;
- private paths or machine identifiers;
- raw replay/chat content;
- unrelated third-party documents.

### Provenance check

Record:

- source artifact/build;
- relevant hash;
- tool/version/configuration;
- transformation performed;
- evidence level;
- publication class;
- reason the representation is necessary and appropriate.

### Independent sanity check

Confirm that the final committed artifact is actually the sanitized/derived artifact intended for publication, not the raw analysis output or an accidental copy.

Automated scanning may assist this review, but automated scanning is **not** itself proof of legal permission or absence of sensitive content.

## 10. Native archaeology handling paths

**PUBLIC DERIVED:** original methodology, measurements, hashes, provenance, structural descriptions, carefully scoped factual observations, and original summaries that pass the publication gate.

**LOCAL RESTRICTED:** binary dumps, detailed decompiler output, bulk string/signature extraction, proprietary implementation material, or other evidence not established as publishable.

**WITHHOLD:** secrets, private information, unclear-rights material, unauthorized material, or content whose disclosure cannot be justified as necessary and responsible.

Restricted material may be retained in the controlled local investigation environment when needed for authorized reproducible analysis. It should not enter the public repository merely for convenience.

## 11. Runtime experiments

Runtime experimentation must remain within the authorized local environment and avoid unnecessary interaction with third-party services, accounts, or systems.

Experiments must identify build identity, purpose, controlled inputs, expected side effects, observed outputs, safety constraints, and evidence classification.

No experiment is justified solely because it might reveal an interesting mechanism.

## 12. Personal and third-party data

Replay files, logs, screenshots, diagnostics, and generated reports are potentially sensitive until inspected.

Before publication, check for player/account identifiers, chat, local paths, machine identifiers, unnecessary timestamps, private metadata, third-party recordings, and embedded sensitive information.

Sanitize or withhold material when the research objective does not require disclosure.

## 13. Professional stop conditions

The engineer must stop and reassess when:

- authorization is unclear;
- publication rights are unclear;
- the operation could expose secrets or personal information;
- the only useful evidence would require publishing restricted material;
- an analysis method risks modifying the authoritative source artifact;
- a destructive Git operation lacks a verified recovery path;
- a conclusion depends on an unsupported semantic assumption;
- tool output is being mistaken for proof;
- a requested action crosses from authorized local analysis into an unauthorized external system;
- the provenance of a proposed public artifact cannot be reconstructed sufficiently to justify publication.

Stopping is a successful engineering control, not a project failure.

## 14. Incident response

If restricted material is accidentally committed or otherwise exposed:

1. stop further distribution;
2. preserve the relevant commit/ref/provenance information for the audit record;
3. determine exactly what was exposed and where;
4. rotate/revoke credentials immediately if secrets are involved;
5. remove or quarantine the material using an appropriate repository-history procedure when required;
6. assess whether cached, forked, downloaded, or otherwise copied versions require additional response;
7. document the incident and corrective action;
8. re-run the publication audit before resuming normal publication.

A history rewrite does not by itself guarantee that every previously copied or cached representation has disappeared. Sensitive exposure must therefore be treated as an incident, not merely as a file-deletion task.

## 15. Documentation requirement

Every significant native investigation record must state, where safely recordable:

- artifact identity and provenance;
- build/version/hash;
- analysis tool/version/configuration;
- what was observed;
- what was independently reproduced;
- what was inferred;
- what remains unknown;
- evidence classification;
- publication/handling classification;
- why the public representation is appropriate.

Corrections amend the record rather than concealing prior uncertainty or failed experiments.

## 16. Change control and retrospective review

Changes to this standard or publication-sensitive repository policy must be auditable. Preserve the prior policy version, record the reason for the change, and identify whether previously published artifacts require re-review.

A policy improvement does not retroactively establish rights for historical material. Historical exposure remains a separate audit problem.

When the project discovers that an older artifact was classified too permissively, the new standard applies prospectively to handling **and triggers retrospective review** of the affected artifact class.

## 17. Legal-review boundary

This document is an engineering control, not legal advice and not a determination of legal rights.

Copyright, license terms, contracts, reverse-engineering exceptions, interoperability, privacy, jurisdiction, and redistribution questions may require qualified legal review.

Where such a question is material and unresolved, the conservative engineering action is to withhold the disputed material and preserve only a safe provenance/technical record.

## 18. Final engineering principle

The project's standard is deliberately higher than "technically possible."

For every nontrivial action, the engineer must ask:

1. **Can we do it?**
2. **Are we authorized to do it?**
3. **Does the evidence justify what we are saying?**
4. **Is it responsible and authorized to retain, use, or publish the result in this form?**
5. **Can we achieve the same engineering objective with a less sensitive representation?**
6. **Can we reconstruct the provenance if this decision is challenged six months from now?**

Only when the applicable answers support the action should it proceed.

> **Capability is not permission. Evidence is not ownership. Usefulness is not justification. When in doubt, preserve the research value and withhold the risky artifact.**
