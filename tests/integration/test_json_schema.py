"""Test json schema generation."""

import json
from pathlib import Path

from opentecr.data import CuratedMeasurement

PROJECT_ROOT = Path(__file__).parent.parent.parent


def test_json_schema() -> None:
    """Check that json schema generation works as expected."""
    result_path = PROJECT_ROOT / "output" / "openTECR.json"
    with result_path.open("r") as f:
        expected = json.load(f)
    actual = CuratedMeasurement.model_json_schema()
    assert expected == actual
