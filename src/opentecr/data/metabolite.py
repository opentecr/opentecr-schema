"""Provides dataclass Metabolite."""


from pydantic import Field

from .annotation import Annotation
from .base import Base


class Metabolite(Base):
    """Define a metabolite ORM model.

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

    inchi: str | None = Field(
        None,
        title="InChI",
        description="IUPAC international chemical identifier.",
    )
    inchi_key: str | None = Field(
        None,
        alias="inchiKey",
        title="InChIKey",
        description="IUPAC international chemical identifier hashed key.",
    )
    smiles: str | None = Field(
        None,
        title="SMILES",
        description="Simplified molecular-input line-entry system (SMILES).",
    )
    molecular_formula: str | None = Field(
        None,
        alias="molecularFormula",
        title="Molecular Formula",
        description="The number of atoms in the metabolite.",
    )
    # FIXME: how do we define charge exactly? valence electrons + protons?
    charge: float | None = Field(None)
    # FIXME: molecular weight, atomic mass, or monoisotopic mass?
    mass: float | None = Field(None)
    names: list[str] = Field(
        [],
        title="Common Names",
        description="Common names or synonyms for this metabolite mostly to further "
        "human understanding.",
    )
    annotation: list[Annotation] = Field(
        [],
        description="Cross-references for the metabolite.",
    )
