# The MIT License (MIT)
#
# Copyright (c) 2019, Moritz E. Beber.
# Copyright (c) 2018 Institute for Molecular Systems Biology, ETH Zurich.
# Copyright (c) 2018 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""Provide a metabolite ORM model."""


from typing import List, Optional

from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship

from .base import Base
from .metabolite_annotation import MetaboliteAnnotation
from .metabolite_name import MetaboliteName
from .mixin import ModelMixin


class Metabolite(ModelMixin, Base):
    """
    Define a metabolite ORM model.

    Attributes
    ----------
    inchi : str, optional
    inchi_key : str, optional
    smiles : str, optional
    chemical_formula : str, optional
    charge : float, optional
    mass : float, optional
    notes : str, optional
    names : list, optional
    annotation : list, optional

    """

    __tablename__ = "metabolites"

    inchi: Optional[str] = Column(String, nullable=True, index=True, unique=True)
    inchi_key: Optional[str] = Column(
        String(27), nullable=True, index=True, unique=True
    )
    smiles: Optional[str] = Column(String, nullable=True, index=True)
    chemical_formula: Optional[str] = Column(String, nullable=True, index=True)
    charge: Optional[float] = Column(Float, nullable=True)
    mass: Optional[float] = Column(Float, nullable=True)
    notes: Optional[str] = Column(String, nullable=True)
    names: List[MetaboliteName] = relationship(
        "MetaboliteAnnotation", cascade="all, delete-orphan"
    )
    annotation: List[MetaboliteAnnotation] = relationship(
        "MetaboliteAnnotation", cascade="all, delete-orphan"
    )

    def __repr__(self):
        """Return a string representation of the object."""
        return f"{type(self).__name__}(id={self.id}, inchi_key={self.inchi_key})"
