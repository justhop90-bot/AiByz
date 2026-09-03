import tempfile
import unittest
from pathlib import Path

from aegis_lab.adapter.scenario_provider import (
    QUALIFIED_TREE_SHA256,
    build_p0a_calibration_fixture,
    load_qualified_parser,
    validate_p0a_fixture,
)


PARSER_ROOT = Path(
    r"C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\AoE2ScenarioParser-master"
)
TEMPLATE = PARSER_ROOT / "AoE2ScenarioParser" / "versions" / "DE" / "v1.58" / "default.aoe2scenario"
FIXTURE = Path(__file__).parents[1] / "fixtures" / "P0A_CAL_001_BASE.aoe2scenario"


class ScenarioProviderTests(unittest.TestCase):
    def test_qualified_source_loads(self):
        module = load_qualified_parser(str(PARSER_ROOT))
        self.assertEqual(Path(module.__file__).resolve(), (PARSER_ROOT / "AoE2ScenarioParser" / "__init__.py").resolve())
        self.assertEqual(len(QUALIFIED_TREE_SHA256), 64)

    def test_committed_fixture_is_pure_per(self):
        result = validate_p0a_fixture(str(PARSER_ROOT), str(FIXTURE))
        self.assertTrue(result["pure_per_fixture"])
        self.assertEqual(result["initial_p1_unit_count"], 1)
        self.assertEqual(result["xs_script_calls"], 0)

    def test_fixture_generation_round_trips(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "generated.aoe2scenario"
            result = build_p0a_calibration_fixture(
                str(PARSER_ROOT), str(TEMPLATE), str(output)
            )
            self.assertTrue(output.is_file())
            self.assertEqual(result["scenario_version"], "1.58")
            self.assertEqual(result["trigger_count"], 1)


if __name__ == "__main__":
    unittest.main()
