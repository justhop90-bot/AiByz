# AEGIS P0 — Native Entry Point Qualification

Date: 2026-09-05
Target: AoE2DE 101.103.48987.0 / Build 24094652 / update #180059
Status: **CODE COMPLETE / RUNTIME QUALIFICATION BLOCKED BY RETAIL STARTUP CRASH**

## Candidate

`AEGIS-BYZ.per` is a self-contained AEGIS-owned entry point.

Dependencies: **none**.

It does not load `AI (HD version).per`, Promisory, or any stock AI module.

The file contains the AEGIS architectural sections and one native bootstrap rule. No unqualified numeric state ABI was allocated.

SHA-256: `c4124247207522e7d8f99282b2ad1fd10c3e3ad0a993d60748d66bc6df26c28a`
Lines: 178
Parentheses: 5 open / 5 close
Load directives: 0

## Static audit

`aegis_abi_audit_v2.py` returned exit code 0.

Closure: 1 file.
Declarations: 1.
Unique symbols: 1.
Numeric declarations: 1.
Resolved goal operands: 0.
High goal operands: 0.

## Disposable package

Local mod candidate:
`mods/local/AEGIS-P0-Entry/resources/_common/ai/AEGIS-BYZ.per`

Required empty descriptor:
`AEGIS-BYZ.ai`

The `.ai` file is a selector/descriptor, not an AEGIS logic module.

## Runtime result

The first mod-status experiment manually inserted the local mod and caused duplicate mod activation; that configuration was restored immediately.

A subsequent clean launch with the original `mod-status.json` restored also crashed at the retail main-menu session before an AI-running match could be established. The latest crash report has `ActiveMods` empty and therefore does **not** attribute that crash to AEGIS.

The latest retail startup log reaches `Running Game` and then terminates with `UnhandledExceptionResponse_BugSplat`. Repeated `curl_easy_setop` errors and obstruction warnings are present before the crash.

Therefore P0 runtime verdict is:

**UNKNOWN — AEGIS entry point has not yet been selected/executed by an AI-running match. The retail launch surface itself is currently unstable, including with no active mods.**

No claim of `.per` runtime success or failure is made from this run.
