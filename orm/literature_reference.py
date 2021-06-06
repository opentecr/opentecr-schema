from sqlalchemy import Column, String

from .base import Base
from .mixin import ModelMixin


class LiteratureReference(ModelMixin, Base):

    __tablename__ = "literature_references"

    pubmed_id: str = Column(String, nullable=True, index=True, unique=True)
    doi: str = Column(String, nullable=True, index=True, unique=True)
    url: str = Column(String, nullable=False, index=True, unique=True)
    title: str = Column(String, nullable=True)
    authors: str = Column(String, nullable=True)
