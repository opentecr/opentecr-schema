import json
import sys
from pathlib import Path

from pydantic.schema import schema


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from opentecr.data import CuratedMeasurement


def main():
    result_path = project_root / "output" / "openTECR.json"
    result = json.dumps(
        schema([CuratedMeasurement], title="openTECR Data Model"), indent=2
    )
    print(result)
    with result_path.open("w") as handle:
        handle.write(result)


if __name__ == "__main__":
    main()
