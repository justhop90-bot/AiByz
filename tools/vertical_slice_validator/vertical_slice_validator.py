from typing import Any

def validate_vertical_slice(trace: dict[str, Any]) -> dict[str, Any]:
    expected = trace.get('expected_stages', [])
    stages = [e.get('stage') for e in trace.get('events', [])]
    errors = []
    for stage in expected:
        if stage not in stages:
            errors.append({'error_code':'VSL-001','message':f'Required stage {stage!r} is missing.'})
    positions = {s: stages.index(s) for s in set(stages) if s is not None}
    for left, right in zip(expected, expected[1:]):
        if left in positions and right in positions and positions[left] > positions[right]:
            errors.append({'error_code':'VSL-002','message':f'Stage {right!r} occurs before {left!r}.'})
    generation = trace.get('generation')
    request_ids = set()
    for e in trace.get('events', []):
        if generation is not None and e.get('generation') != generation:
            errors.append({'error_code':'VSL-008','message':'Event generation does not match trace generation.'})
        rid = e.get('request_id')
        if e.get('stage') == 'PHYSICAL_REQUEST':
            if not e.get('authorized'):
                errors.append({'error_code':'VSL-003','message':'Physical request lacks authorization.'})
            if rid and rid in request_ids:
                errors.append({'error_code':'VSL-009','message':f'Duplicate request {rid!r}.'})
            if rid: request_ids.add(rid)
        if e.get('stage') == 'ENGINE_ACCEPTED_PENDING' and not rid:
            errors.append({'error_code':'VSL-004','message':'Pending state lacks request identity.'})
        if e.get('stage') == 'WORLD_STATE_VERIFIED' and not e.get('world_state_evidence'):
            errors.append({'error_code':'VSL-005','message':'Verification lacks world-state evidence.'})
        if e.get('strategic_success') and e.get('stage') != 'WORLD_STATE_VERIFIED':
            errors.append({'error_code':'VSL-006','message':'Success was claimed before verification.'})
        if e.get('outcome') == 'UNKNOWN' and e.get('credited'):
            errors.append({'error_code':'VSL-007','message':'Unknown outcome received credit.'})
        if e.get('outcome') == 'FAILED' and e.get('credited'):
            errors.append({'error_code':'VSL-010','message':'Failed outcome received credit.'})
    return {'qualified': not errors, 'errors': errors}
