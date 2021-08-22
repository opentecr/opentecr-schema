from typing import Dict, List, Optional

from pydantic import Field

from .annotation import Annotation
from .base import Base
from .metabolite import Metabolite


class RepresentativeReaction(Base):
    """"""

    rinchi: Optional[str] = Field(
        None,
        title="RInChI",
        description="Reaction IUPAC international chemical identifier.",
    )
    rinchi_key: Optional[str] = Field(
        None,
        alias="rinchiKey",
        title="RInChIKey",
        description="Hashed version of the reaction IUPAC international chemical "
        "identifier.",
    )
    names: List[str] = Field(
        (),
        title="Common Names",
        description="Common names or synonyms for this reaction mostly to further "
        "human understanding.",
    )
    annotation: List[Annotation] = Field(
        (), description="Cross-references for the reaction."
    )
    stoichiometry: Dict[Metabolite, float] = Field(
        ...,
        description="A dictionary of the stoichiometric coefficients and metabolites"
        "that define this reaction. Includes both reactants (negative coefficients) "
        "and products (positive coefficients).",
    )

    @property
    def reactants(self) -> List[Metabolite]:
        return [met for met, coef in self.stoichiometry if coef < 0]

    @property
    def products(self) -> List[Metabolite]:
        return [met for met, coef in self.stoichiometry if coef > 0]
