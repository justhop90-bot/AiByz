# AEGIS — Stock AI Runtime Baseline

**Date:** 2026-09-05  
**Status:** VERIFIED STOCK BASELINE  
**Target executable SHA-256:** `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`  
**Steam BuildID:** `24094652`

## Purpose

Freeze the untouched stock HD AI entrypoint closure used as the reference boundary for AEGIS machine qualification.

## Authoritative stock closure

The normal HD entrypoint is:

`AI (HD version).per`

Its direct load closure is:

1. `AI (HD version).per`
2. `Promisory\defaultConstants.per`
3. `Promisory\finalingConstants.per`
4. `Promisory\finaling.per`

No production AEGIS implementation is permitted to silently modify this stock baseline.

## Current workstation hashes

| File | SHA-256 |
|---|---|
| `AI (HD version).per` | `8A554A90A18F7983A949F7BEF3B767E09732BCE87DCA3B9546FE782F098DE51C` |
| `Promisory\defaultConstants.per` | `187980FD34F5A5626955B20DD97114DC2212C9E7E86356014A7976DD1AE310AD` |
| `Promisory\finalingConstants.per` | `CE7A804A9855742CF4329C0FA44E603A5D19655951BF8E6BC5CF689264E07455` |
| `Promisory\finaling.per` | `95E18EB8B765A7F87EA499C25ED944D0E04C9ABF932B70D8821EF1154D872E52` |

## Engineering rule

This baseline is evidence, not implementation. Historical stock modules outside the normal HD closure remain useful for semantic archaeology, but their presence does not mean they are part of the normal HD runtime closure.

Any qualification result that depends on a modified stock file must be labeled as a modified-build experiment and must not be promoted into the untouched stock baseline.

## Relationship to shared qualification

This artifact directly supports Q-01 (Build Identity & Semantic Scope), Q-02 (Typed ABI Identity), and Q-03 (State-Channel Ownership & Collision).
