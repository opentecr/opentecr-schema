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


"""Provide an association between a reaction and its participating metabolites."""


from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer

from .base import Base


class Participant(Base):
    """
    Define an association between a reaction and a participating metabolite.

    Attributes
    ----------
    stoichiometry : str

    """

    __tablename__ = "participants"

    reaction_id: int = Column(
        Integer, ForeignKey("representative_reactions.id"), primary_key=True
    )
    metabolite_id: int = Column(Integer, ForeignKey("metabolites.id"), primary_key=True)
    stoichiometry: int = Column(Float, nullable=False)
    is_product: bool = Column(Boolean, nullable=False)

    def __repr__(self):
        """Return a string representation of the object."""
        return (
            f"{type(self).__name__}(reaction={self.reaction_id}, "
            f"metabolite={self.metabolite_id}, stoichiometry="
            f"{self.stoichiometry if self.is_product else f'-{self.stoichiometry}'})"
        )
