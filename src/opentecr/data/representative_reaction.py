"""Provides dataclass RepresentativeReaction."""


from pydantic import Field, computed_field

from .annotation import Annotation
from .base import Base
from .metabolite import Metabolite


class RepresentativeReaction(Base):
    """Information about a reaction."""

    rinchi: str | None = Field(
        None,
        title="RInChI",
        description="Reaction IUPAC international chemical identifier.",
    )
    rinchi_key: str | None = Field(
        None,
        alias="rinchiKey",
        title="RInChIKey",
        description="Hashed version of the reaction IUPAC international chemical "
        "identifier.",
    )
    names: list[str] = Field(
        [],
        title="Common Names",
        description="Common names or synonyms for this reaction mostly to further "
        "human understanding.",
    )
    annotation: list[Annotation] = Field(
        [],
        description="Cross-references for the reaction.",
    )
    stoichiometry: dict[Metabolite, float] = Field(
        ...,
        description="A dictionary of the stoichiometric coefficients and metabolites"
        "that define this reaction. Includes both reactants (negative coefficients) "
        "and products (positive coefficients).",
    )

    @property
    def reactants(self: "RepresentativeReaction") -> list[Metabolite]:
        """Add the reactants attribute."""
        return [met for met, coef in self.stoichiometry.items() if coef < 0]

    @property
    def products(self: "RepresentativeReaction") -> list[Metabolite]:
        """Add the products attribute."""
        return [met for met, coef in self.stoichiometry.items() if coef > 0]
