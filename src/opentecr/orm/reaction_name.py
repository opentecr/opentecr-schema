# Copyright (c) 2019, Moritz E. Beber.
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


"""Provide a reaction name ORM model."""


from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from .base import Base
from .mixin import ModelMixin, NameMixin


class ReactionName(NameMixin, ModelMixin, Base):
    """
    Define a reaction name ORM model.

    Attributes
    ----------
    reaction_id : int
        The SBML reaction being annotated.

    """

    __tablename__ = "reaction_names"

    reaction_id: int = Column(
        Integer, ForeignKey("representative_reactions.id"), nullable=False
    )

    __table_args__ = (UniqueConstraint("reaction_id", "namespace_id", "name"),)

    def __repr__(self):
        """Return a string representation of the object."""
        return (
            f"{type(self).__name__}(reaction={self.reaction_id}, "
            f"name={self.name}, "
            f"namespace={self.namespace_id})"
        )
