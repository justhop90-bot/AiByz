import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools' / 'vertical_slice_validator'))
from vertical_slice_validator import validate_vertical_slice

SLICES = {
    'worker_economy': ['OBSERVE','CLASSIFY','DEMAND','FEASIBILITY','AUTHORIZATION','PHYSICAL_REQUEST','ENGINE_ACCEPTED_PENDING','WORLD_STATE_VERIFIED','REASSESS'],
    'villager_production': ['OBSERVE','DEMAND','FEASIBILITY','AUTHORIZATION','PHYSICAL_REQUEST','ENGINE_ACCEPTED_PENDING','WORLD_STATE_VERIFIED','REASSESS'],
    'housing': ['OBSERVE','DEMAND','FEASIBILITY','AUTHORIZATION','PHYSICAL_REQUEST','ENGINE_ACCEPTED_PENDING','WORLD_STATE_VERIFIED','REASSESS'],
    'age_transition': ['OBSERVE','DEMAND','FEASIBILITY','AUTHORIZATION','PHYSICAL_REQUEST','WORLD_STATE_VERIFIED','REASSESS'],
    'anti_cavalry': ['OBSERVE','CLASSIFY','DEMAND','FEASIBILITY','AUTHORIZATION','PHYSICAL_REQUEST','ENGINE_ACCEPTED_PENDING','WORLD_STATE_VERIFIED','REASSESS'],
    'tactical_micro': ['OBSERVE','CLASSIFY','DEMAND','FEASIBILITY','AUTHORIZATION','PHYSICAL_REQUEST','WORLD_STATE_VERIFIED','REASSESS'],
}


def valid_trace(stages, generation=1):
    events = []
    for i, stage in enumerate(stages):
        event = {'stage': stage, 'generation': generation}
        if stage == 'PHYSICAL_REQUEST':
            event.update(authorized=True, request_id=f'req-{i}')
        if stage == 'ENGINE_ACCEPTED_PENDING':
            event['request_id'] = next(e['request_id'] for e in reversed(events) if e.get('stage') == 'PHYSICAL_REQUEST')
        if stage == 'WORLD_STATE_VERIFIED':
            event['world_state_evidence'] = True
        events.append(event)
    return {'generation': generation, 'expected_stages': list(stages), 'events': events}


class TestEveryVerticalSlice(unittest.TestCase):
    def test_all_slices_accept_complete_lifecycle(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                result = validate_vertical_slice(valid_trace(stages))
                self.assertTrue(result['qualified'], result['errors'])

    def test_no_slice_can_skip_authorization(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                broken = valid_trace(stages)
                for event in broken['events']:
                    if event['stage'] == 'PHYSICAL_REQUEST':
                        event['authorized'] = False
                result = validate_vertical_slice(broken)
                self.assertFalse(result['qualified'])
                self.assertIn('VSL-003', {e['error_code'] for e in result['errors']})

    def test_no_slice_can_promote_pending_to_success_without_verification(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                broken = valid_trace(stages)
                for event in broken['events']:
                    if event['stage'] == 'ENGINE_ACCEPTED_PENDING':
                        event['strategic_success'] = True
                result = validate_vertical_slice(broken)
                self.assertFalse(result['qualified'])
                self.assertIn('VSL-006', {e['error_code'] for e in result['errors']})

    def test_unknown_outcome_never_receives_credit(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                broken = valid_trace(stages)
                broken['events'][-1].update(outcome='UNKNOWN', credited=True)
                result = validate_vertical_slice(broken)
                self.assertFalse(result['qualified'])
                self.assertIn('VSL-007', {e['error_code'] for e in result['errors']})

    def test_failed_outcome_never_receives_credit(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                broken = valid_trace(stages)
                broken['events'][-1].update(outcome='FAILED', credited=True)
                result = validate_vertical_slice(broken)
                self.assertFalse(result['qualified'])
                self.assertIn('VSL-010', {e['error_code'] for e in result['errors']})

    def test_stale_generation_is_fail_closed(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                broken = valid_trace(stages, generation=9)
                broken['events'][0]['generation'] = 8
                result = validate_vertical_slice(broken)
                self.assertFalse(result['qualified'])
                self.assertIn('VSL-008', {e['error_code'] for e in result['errors']})

    def test_duplicate_physical_request_is_rejected(self):
        for name, stages in SLICES.items():
            with self.subTest(slice=name):
                broken = valid_trace(stages)
                request = next(e for e in broken['events'] if e['stage'] == 'PHYSICAL_REQUEST')
                duplicate = dict(request)
                broken['events'].insert(broken['events'].index(request) + 1, duplicate)
                result = validate_vertical_slice(broken)
                self.assertFalse(result['qualified'])
                self.assertIn('VSL-009', {e['error_code'] for e in result['errors']})


if __name__ == '__main__':
    unittest.main(verbosity=2)
