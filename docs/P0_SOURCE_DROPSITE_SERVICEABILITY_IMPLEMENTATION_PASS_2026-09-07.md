# P0 Source/Dropsite Serviceability — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate implemented and statically reviewed; NOT runtime-qualified; NOT loaded by production root.

## Evidence recovered

The untouched stock gatherer corpus uses `up-find-resource` to build remote resource searches and then filters candidate resource objects using `object-data-tasks-count`. A representative wood path rejects resource objects with `object-data-tasks-count >= 2`. This establishes task-load filtering as a real stock selection signal, but not as a universal capacity rule.

Stock also uses `dropsite-min-distance` as a resource-to-dropsite serviceability predicate. Observed thresholds include resource-specific strategic numbers such as maximum gold and stone drop distances. The stock initialization corpus sets baseline values of food 8, wood 20, gold 10, stone 10, and hunt 12 before later adaptation. These values are stock policy, not AEGIS universal constants.

## Implemented contract

ARBITRATED DEMAND → RESOURCE SOURCE SEARCH → RESOURCE TASK-LOAD FILTER → DROPSITE SERVICEABILITY PREDICATE → SERVICEABILITY RESULT.

The candidate records generation, requested resource, source-candidate count, serviceability state, failure state, observation timestamp, and cycle. It issues no worker task command.

## Important correction during this pass

The first GitHub draft incorrectly used the gold resource search for both gold and stone. That was caught by review before the candidate was accepted. The file was surgically corrected so stone uses its own `up-find-resource c: stone c: 8` path and its own `dropsite-min-distance stone` predicate. The corrected GitHub commit is `1892870506894bab078df72a0d544884debb5772`.

This correction is retained as an engineering lesson: resource identity must never be inferred from neighboring resource logic merely because the control structure is similar.

## Food boundary

Food is explicitly deferred. Stock evidence shows food acquisition is a portfolio spanning different source mechanisms, including herdables, forage, hunting, farms, and fishing. V0 therefore does not invent one universal food-resource object class. A dedicated food-source adapter is required.

## Qualification states

OBSERVED: stock resource search, object-data task-load filtering, dropsite-min-distance predicate, and resource-specific maximum drop-distance strategic numbers.
CORRELATED: source candidates plus delivery-distance qualification form a valid serviceability boundary for downstream task assignment.
IMPLEMENTED: AEGIS source search and conservative serviceability adapter for wood, gold, and stone.
STATIC-QUALIFIED: balanced syntax, isolated goal range 499–507, production root unchanged, no Promisory runtime dependency.
UNQUALIFIED: exact target-build search mutation visibility, precise meaning of `remote-total` after filtering, exact path/delivery-distance semantics, same-pass strategic-number visibility, and the runtime relationship between selected source and dropsite.

## Deliberate non-claims

`object-data-tasks-count` is not treated as universal worker capacity. `dropsite-min-distance` is not described as exact path distance. Building count is not treated as proof of operational serviceability. A source existing is not treated as proof that a worker can currently use it.

## Next engineering target

Build the actual task-command adapter. It must combine candidate worker, qualified source, dropsite/serviceability, threat/eligibility, and generation fencing before issuing the engine command. Command issuance remains distinct from productivity confirmation and recovery.