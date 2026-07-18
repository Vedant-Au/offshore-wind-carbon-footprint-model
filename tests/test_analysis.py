from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analysis import add_stage_shares, estimate_cradle_to_gate


class WindCarbonModelTests(unittest.TestCase):
    def test_reported_scenario_bounds(self) -> None:
        self.assertEqual(estimate_cradle_to_gate(528, 15, 0.70), 5544)
        self.assertEqual(estimate_cradle_to_gate(528, 15, 0.80), 6336)

    def test_invalid_share_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            estimate_cradle_to_gate(528, 15, 1.1)

    def test_impact_table_reconciles(self) -> None:
        frame = pd.read_csv(ROOT / "data/reference/impact_by_stage.csv")
        result = add_stage_shares(frame)
        self.assertTrue(result["manufacturing_share"].between(0, 1).all())
        gwp = result.loc[result["impact_category"].eq("Global warming potential")].iloc[0]
        self.assertAlmostEqual(gwp["manufacturing_share"], 7.1 / 7.5)

    def test_non_reconciling_total_is_rejected(self) -> None:
        frame = pd.DataFrame({"impact_category":["x"],"unit":["u"],"manufacturing":[1],"plant_setup":[1],"total":[3]})
        with self.assertRaisesRegex(ValueError, "reconcile"):
            add_stage_shares(frame)


if __name__ == "__main__":
    unittest.main()
