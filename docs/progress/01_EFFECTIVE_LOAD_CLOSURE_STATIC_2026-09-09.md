# AEGIS Effective Load Closure — Static Statement (2026-09-09)

**Status:** High-confidence static closure based on committed machine evidence  
**Parent:** FINAL_RECONSTRUCTION_AUDIT R1  
**Evidence source:** `docs/MACHINE_EVIDENCE/AEGIS_A1_LOAD_CLOSURE_2026-09-05.json` + Stock Subsystem Reconstruction Map

## Verified active runtime substrate (target build)

Entrypoint:
- `AI (HD version).per`  
  SHA-256: `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`  
  Size: 1,167,238 bytes

Direct loads recorded in the closure capture:
1. `Promisory\\defaultConstants.per`  
   SHA-256: `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad`
2. `Promisory\\finalingConstants.per`  
   SHA-256: `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455`
3. `Promisory\\finaling.per` (conditional in source structure)  
   SHA-256: `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52`

No further loads were discovered from the three Promisory files in the 2026-09-05 capture.

## Provenance rules (binding)

1. A file under `Promisory\\` is **not** a runtime dependency merely because it exists.
2. Commented historical loaders are provenance only.
3. Nested imports that appear only inside non-loaded modules are not active unless an active path is proven.
4. The flattened `AI (HD version).per` is the primary behavioral body; Promisory modules are reconstruction material except for the three files above.

## Known nested relationships (reconstruction, not automatic runtime)

- `buildings.per` → `extremebuildings2.per` (source relationship)
- `gatherers.per` → `ugp.per` (source relationship)

These are not automatically part of the active load graph of the flattened controller.

## Residual open item for R1

Full expansion of every preprocessor conditional branch and the exact effective rule/symbol set after all conditionals are resolved still requires a deterministic parser run against the exact package.  
The static four-file closure above is the current high-confidence baseline and is sufficient for ownership and ABI policy work.

## Engineering consequence

AEGIS must treat the four-file substrate + the flattened controller as the stock reference.  
Any AEGIS load graph must be explicit and must not silently depend on the broader Promisory corpus.
