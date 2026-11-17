"""Unit tests for art manifest structure and failure-safe production gate."""
import copy
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from validate_concept3_assets import validate  # noqa: E402

ROOT = HERE.parents[1] / "design/puppy-01"
MANIFEST = ROOT / "concept3-rig-manifest.json"


class AssetContractTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_structure_contract_is_valid_but_not_art(self):
        self.assertEqual([], validate(self.data, ROOT, "structure"))

    def test_production_rejects_unfinished_source_and_layers(self):
        failures = validate(self.data, ROOT, "production")
        self.assertTrue(failures)
        self.assertTrue(any("reference file missing" in s.lower() for s in failures))
        self.assertTrue(any("exported PNG missing" in s for s in failures))

    def test_required_parts_are_not_silently_skipped(self):
        data = copy.deepcopy(self.data)
        data["layers"] = data["layers"][:-1]
        self.assertTrue(any("Missing required layers" in s for s in validate(data, ROOT, "structure")))

    def test_rejects_relative_escape(self):
        data = copy.deepcopy(self.data)
        data["layers"][0]["file"] = "../outside.png"
        self.assertTrue(any("path must stay within" in s for s in validate(data, ROOT, "structure")))

    def test_rejects_duplicate_asset_reference(self):
        data = copy.deepcopy(self.data)
        data["layers"][0]["file"] = "same.png"
        data["layers"][1]["file"] = "same.png"
        self.assertTrue(any("may not reference" in s for s in validate(data, ROOT, "structure")))


if __name__ == "__main__":
    unittest.main()
