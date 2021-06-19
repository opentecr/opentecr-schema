from sqlalchemy import create_engine

from opentecr.orm import Base


def main():
    engine = create_engine("sqlite:///openTECR.sqlite")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
