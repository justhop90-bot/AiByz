# Object Lifecycle Reconstruction — QC Pass 1
Date: 2026-09-02
Status: research / calibration only

## Purpose
Reconstruct object existence without equating disappearance with death. The atomic unit is an object-state episode bounded by temporal evidence.

## State model
UNKNOWN -> OBSERVED -> CREATED/INFERRED -> ACTIVE
ACTIVE may transition to MOVING, GATHERING, COMBAT, PRODUCING, GARRISONED, TRANSFORMING, DAMAGED, or IDLE.
Terminal candidates: DESTROYED, DELETED, TRANSFORMED, GARRISONED, OWNERSHIP_CHANGED, HIDDEN, OUT_OF_OBSERVATION, PARSER_MISSING, UNKNOWN.

## Evidence hierarchy
1. Explicit replay command or parser-decoded object reference.
2. Repeated object observation in rich synchronization/state payload.
3. Later reappearance with stable identity.
4. Production/build lineage.
5. Combat/repair/transform/garrison command neighborhood.
6. Absence alone — never terminal proof.

## Identity contract
Each object record should contain object_id, owner, unit/building type if known, first_seen, last_seen, evidence class, confidence, source locator, and identity continuity score. Type or ownership changes must be represented as state transitions, not silently overwritten.

## Disappearance taxonomy
A missing object creates a TERMINATION_CANDIDATE, not a death event. Candidate causes must be adjudicated from surrounding commands, later observations, and visibility. If evidence is insufficient, preserve UNKNOWN.

## Temporal contract
Use temporal clusters rather than JSONL position as causal order. Events sharing the same sequence are potentially simultaneous. Sequence provides ordering and probable temporal placement; it does not prove causal precedence.

## Production lineage
For produced units, retain parent production object/building, queue admission, cancellation, completion candidate, first battlefield observation, and subsequent lifecycle. Queue admission is not completion; completion is not battlefield availability.

## Transformation lineage
DE_TRANSFORM and related SPECIAL events should create a lineage edge from pre-state object to post-state representation when identity evidence supports continuity. Do not create two unrelated deaths/births when a transformation is plausible.

## Garrison lineage
UNGARRISON, garrison-related orders, building destruction, and later reappearance can explain apparent disappearance. Garrison state should be explicit and duration-bounded where evidence permits.

## Ownership
Ownership should be modeled as a time-indexed state. Do not assume an object_id uniquely implies one owner across its entire life without evidence.

## Visibility
A player's information set is distinct from omniscient replay evidence. A hidden object may exist while being strategically unknown. Preserve observer/perspective when reconstructing decision events.

## QC verdict
The lifecycle subsystem should be implemented as a typed state machine with evidence-backed transitions and uncertainty. The next pass must quantify identity continuity, disappearance classes, production lineage, transformation/garrison cases, and false-terminal rates on the calibration corpus.
