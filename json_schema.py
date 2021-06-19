from pathlib import Path

from opentecr.data import CuratedMeasurement


def main():
    schema = CuratedMeasurement.schema_json(indent=2)
    print(schema)
    with Path("dummy.json").open("w") as handle:
        handle.write(schema)


if __name__ == "__main__":
    main()
