# Copyright (c) 2019, Moritz E. Beber.
# Copyright (c) 2019, Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
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


"""Provide a metabolite annotation ORM model."""


from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from .base import Base
from .mixin import AnnotationMixin, ModelMixin


class MetaboliteAnnotation(AnnotationMixin, ModelMixin, Base):
    """
    Define a metabolite annotation ORM model.

    Attributes
    ----------
    metabolite_id : int
        The metabolite being annotated.

    """

    __tablename__ = "metabolite_annotations"

    metabolite_id: int = Column(Integer, ForeignKey("metabolites.id"), nullable=False)

    __table_args__ = (UniqueConstraint("metabolite_id", "namespace_id", "identifier"),)

    def __repr__(self):
        """Return a string representation of the object."""
        return (
            f"{type(self).__name__}(metabolite={self.metabolite_id}, "
            f"identifier={self.identifier}, "
            f"namespace={self.namespace_id})"
        )
