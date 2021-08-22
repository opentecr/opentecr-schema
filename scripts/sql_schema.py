import sys
from pathlib import Path

from sqlalchemy import create_engine


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from opentecr.orm import Base


def main():
    db_path = project_root / "output" / "openTECR.sqlite"
    Base.metadata.create_all(create_engine(f"sqlite:///{db_path}"))


if __name__ == "__main__":
    main()
