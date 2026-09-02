# AEGIS Engineering Safety & Authorization Standard — 2026-09-02

## Purpose

This standard is a mandatory project-control layer for AEGIS native archaeology, reverse engineering, replay research, runtime experimentation, and repository publication.

The project must be useful **without becoming careless**. Technical capability does not establish authorization. An analysis result does not automatically establish a publication right.

The governing rule is:

> **Do not perform, retain, publish, or operationalize an action unless its technical purpose, authorization basis, and safety/publication boundary are understood. When uncertain, stop the risky path and preserve only the minimum safe research record.**

## 1. Scope

This standard applies to Ghidra and other native-analysis work, locally obtained game executables and supporting binaries, disassembly/decompilation, strings and metadata, replay extraction, runtime experiments, analysis scripts, GitHub operations, derived documentation/data, and future tools or connectors.

## 2. Authorization boundary

The project assumes only authority actually established by available facts.

Possession or local access to an executable is not treated as blanket permission to redistribute it, publish extracted proprietary code, disclose private material, circumvent access controls, or interact with systems outside the authorized environment.

Analysis must remain within the user's authorized environment and applicable platform, license, contractual, and legal boundaries. If authorization becomes uncertain, the operation is paused rather than rationalized.

No project document may state or imply that reverse engineering, copying, publication, redistribution, or circumvention is legally permitted merely because a tool can technically perform it.

## 3. Ghidra safety and provenance rule

Ghidra is an analysis instrument, not a source of automatically publishable material.

Every material native-analysis output receives both an **evidence classification** and a **publication classification** before it becomes durable project evidence.

### Evidence classifications

- **E0 — raw controlled input:** original local artifact; restricted by default.
- **E1 — tool observation:** directly produced by an analysis tool; not automatically semantic proof.
- **E2 — reproduced observation:** independently reproduced by a second controlled method/configuration.
- **E3 — verified native mechanism:** implementation-level evidence sufficient to support the stated proposition.
- **E4 — runtime corroboration:** controlled runtime behavior independently supports the proposition.

These evidence labels supplement, rather than replace, the Layer 1 evidence ladder.

### Publication classifications

1. **P0 / safe derived observation** — original description, measurement, hash, address/range, or methodology that does not reproduce substantial proprietary material.
2. **P2 / restricted** — useful evidence retained locally because publication rights or sensitivity do not permit public release.
3. **P2 / unresolved** — rights, privacy, contractual status, or sensitivity cannot presently be established; publication is blocked.

The preferred public representation is:

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

If the research conclusion can be preserved using an original description, measurement, hash, provenance record, or appropriately scoped reference, that representation is preferred.

## 5. Evidence gate and rights gate

Every public artifact requires two independent gates.

**Evidence gate:** Is the technical claim actually demonstrated at the stated evidence level?

**Rights gate:** Is the proposed representation authorized and responsible to publish?

Passing one gate never substitutes for passing the other.

A technically certain result can remain private. A publishable artifact can remain scientifically weak.

## 6. Native-analysis evidence discipline

The following distinctions are mandatory:

- native vocabulary is not implementation proof;
- a decompiler rendering is not verified source;
- a string reference is not a call graph;
- a recovered address is not automatically a public identifier;
- a parser field is not automatically native state;
- a failed search is not proof of absence;
- tool capability is not authorization;
- local access is not redistribution permission.

Critical conclusions require the evidence ladder defined by Layer 1 controls. When an analysis result is weaker than the claim it is being used to support, the claim is demoted rather than the evidence being rhetorically upgraded.

## 7. Tool-operation safety

Before a new invasive or destructive operation, establish:

1. exact target;
2. technical purpose;
3. authorization basis;
4. expected side effects;
5. preservation/rollback method;
6. evidence classification;
7. publication classification;
8. independent verification method.

Never overwrite the only copy of an authoritative artifact or historical analysis project. Preserve hashes and provenance before transformation. Prefer disposable analysis projects for experiments.

Destructive repository operations require a verified recovery/provenance record and independent post-operation verification.

## 8. Repository publication gate

The existing `PUBLICATION_AND_RIGHTS_CONTROL_STANDARD_2026-09-02.md` remains the governing publication policy for P0–P6 material.

This standard adds an operational rule: **uncertainty is a blocking condition for sensitive publication**.

When rights are unclear, publish only a safe original research conclusion if it can be communicated without redistributing the restricted underlying material. Otherwise withhold it.

## 9. Native archaeology output policy

Native-analysis artifacts fall into three handling paths:

**PUBLIC DERIVED:** hashes, methodology, measurements, original structural descriptions, carefully scoped factual identifiers, and original pseudocode-level summaries where appropriate.

**LOCAL RESTRICTED:** binary dumps, detailed decompiler output, bulk string/signature extraction, proprietary implementation material, and other evidence whose publication basis is not established.

**WITHHOLD:** material containing secrets, private information, unclear third-party rights, or content whose publication cannot be justified as necessary and authorized.

Restricted material may be retained in the controlled local investigation environment when needed for authorized reproducible analysis. It should not enter the public repository merely for convenience.

## 10. Runtime experiments

Runtime experimentation must remain within the authorized local environment and avoid unnecessary interaction with third-party services, accounts, or systems.

Experiments must identify build identity, purpose, controlled inputs, expected side effects, observed outputs, safety constraints, and evidence classification.

No experiment is justified solely because it might reveal an interesting mechanism.

## 11. Personal and third-party data

Replay files, logs, screenshots, diagnostics, and generated reports are potentially sensitive until inspected.

Before publication, check for player/account identifiers, chat, local paths, machine identifiers, unnecessary timestamps, private metadata, third-party recordings, and embedded sensitive information.

Sanitize or withhold material when the research objective does not require disclosure.

## 12. Professional stop conditions

The engineer must stop and reassess when:

- authorization is unclear;
- publication rights are unclear;
- the operation could expose secrets or personal information;
- the only useful evidence would require publishing restricted material;
- an analysis method risks modifying the authoritative source artifact;
- a destructive Git operation lacks a verified recovery path;
- a conclusion depends on an unsupported semantic assumption;
- tool output is being mistaken for proof;
- a requested action crosses from local analysis into an unauthorized external system.

Stopping is a successful engineering control, not a project failure.

## 13. Documentation requirement

Every significant native investigation record must state, where safely recordable:

- artifact identity and provenance;
- build/version/hash;
- analysis tool/version/configuration;
- what was observed;
- what was independently reproduced;
- what was inferred;
- what remains unknown;
- evidence classification;
- publication classification;
- why the public representation is appropriate.

Corrections amend the record rather than concealing prior uncertainty or failed experiments.

## 14. Change-control requirement

Changes to this standard or to publication-sensitive repository policy must be auditable. The project should preserve the prior policy version, record the reason for the change, and identify whether any previously published artifact requires re-review.

A policy improvement does not retroactively establish rights for historical material. Historical exposure remains a separate audit problem.

## 15. Legal-review boundary

This document is an engineering control, not legal advice and not a determination of legal rights.

Copyright, license terms, contracts, reverse-engineering exceptions, interoperability, privacy, jurisdiction, and redistribution questions may require qualified legal review.

Where such a question is material and unresolved, the conservative engineering action is to withhold the disputed material and preserve only a safe provenance/technical record.

## 16. Final engineering principle

The project's standard is deliberately higher than "technically possible."

For every nontrivial action, the engineer must ask:

1. **Can we do it?**
2. **Are we authorized to do it?**
3. **Is it responsible to retain, use, or publish the result in this form?**
4. **Can we achieve the engineering objective with a less sensitive representation?**

Only when the applicable answers support the action should it proceed.

> **Capability is not permission. Evidence is not ownership. Usefulness is not justification. When in doubt, preserve the research value and withhold the risky artifact.**
