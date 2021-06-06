from sqlalchemy import Column, String, Unicode

from .base import Base
from .mixin import ModelMixin


class User(ModelMixin, Base):

    __tablename__ = "users"

    orcid: str = Column(String, nullable=False, unique=True, index=True)
    name: str = Column(Unicode)
