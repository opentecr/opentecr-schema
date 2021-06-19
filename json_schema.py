import json
from pathlib import Path

from pydantic.schema import schema

from opentecr.data import CuratedMeasurement


def main():
    result = json.dumps(
        schema([CuratedMeasurement], title="openTECR Data Model"), indent=2
    )
    print(result)
    with Path("openTECR.json").open("w") as handle:
        handle.write(result)


if __name__ == "__main__":
    main()
