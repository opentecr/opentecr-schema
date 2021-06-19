from typing import Optional

from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import Base
from .literature_reference import LiteratureReference
from .mixin import ModelMixin
from .representative_reaction import RepresentativeReaction
from .user import User


class CuratedMeasurement(ModelMixin, Base):

    __tablename__ = "curated_measurements"

    reference_id: int = Column(
        Integer, ForeignKey("literature_references.id"), nullable=False
    )
    reference: LiteratureReference = relationship("LiteratureReference")
    submitter_id: Optional[int] = Column(Integer, ForeignKey("users.id"), nullable=True)
    submitter: Optional[User] = relationship("User", foreign_keys=[submitter_id])
    curator_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    curator: User = relationship("User", foreign_keys=[curator_id])
    representative_reaction_id: int = Column(
        Integer, ForeignKey("representative_reactions.id"), nullable=False
    )
    representative_reaction: RepresentativeReaction = relationship(
        "RepresentativeReaction"
    )
    equilibrium_constant: float = Column(Float)
    hydrogen_potential: float = Column(Float)
    magnesium_potential: Optional[float] = Column(Float, nullable=True)
    temperature: float = Column(Float)
    ionic_strength: float = Column(Float)
