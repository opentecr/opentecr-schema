# Copyright (c) 2021, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import List, Optional

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base
from .mixin import ModelMixin
from .participant import Participant
from .reaction_annotation import ReactionAnnotation
from .reaction_name import ReactionName


class RepresentativeReaction(ModelMixin, Base):
    """"""

    __tablename__ = "representative_reactions"

    rinchi: Optional[str] = Column(String, nullable=True, index=True, unique=True)
    notes: Optional[str] = Column(String, nullable=True)
    names: List[ReactionName] = relationship(
        "ReactionName", cascade="all, delete-orphan"
    )
    annotation: List[ReactionAnnotation] = relationship(
        "ReactionAnnotation", cascade="all, delete-orphan"
    )
    reactants: List[Participant] = relationship(
        "Participant",
        primaryjoin="and_(RepresentativeReaction.id == Participants.reaction_id, "
        "Participants.is_product.is_(False))",
        cascade="all, delete-orphan",
    )
    products: List[Participant] = relationship(
        "Participant",
        primaryjoin="and_(RepresentativeReaction.id == Participants.reaction_id, "
        "Participants.is_product.is_(True))",
        cascade="all, delete-orphan",
    )
