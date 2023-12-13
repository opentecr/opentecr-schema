"""Write the CuratedMeasurement schema to a json file."""

import json
import logging
import sys
from pathlib import Path

from opentecr.data import CuratedMeasurement

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))


def main() -> None:
    """Run the script."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    result_path = project_root / "output" / "openTECR.json"
    result = json.dumps(CuratedMeasurement.model_json_schema(), indent=2)
    logging.info(result)
    with result_path.open("w") as handle:
        handle.write(result)


if __name__ == "__main__":
    main()
