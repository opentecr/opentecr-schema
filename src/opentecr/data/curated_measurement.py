from typing import Optional

from pydantic import Field

from .base import Base
from .contributor import Contributor
from .literature_reference import LiteratureReference


class CuratedMeasurement(Base):

    reference: LiteratureReference = Field(
        ...,
        title="Literature Reference",
        description="The official source from which these measurements were curated. "
        "Ideally identified by a DOI.",
    )
    curator: Optional[Contributor] = Field(
        None,
        title="Contributor",
        description="The person who contributed these measurements.",
    )
    representative_reaction: RepresentativeReaction = Field(
        ...,
        title="Representative Reaction",
        description="The representative biochemical reaction to which the measurements "
        "apply.",
    )
    # FIXME: add fields for units? (also explicitly dimensionless)
    # FIXME: free energy?
    # FIXME: apparent equilibrium constant?
    equilibrium_constant: Optional[float] = Field(
        None,
        alias="equilibriumConstant",
        title="Equilibrium Constant",
        description="The equilibrium constant ($K$) of this reaction.",
    )
    hydrogen_potential: Optional[float] = Field(
        None,
        alias="hydrogenPotential",
        title="Potential of Hydrogen",
        description="The potential of hydrogen (pH) at which the measurements were "
        "performed.",
    )
    magnesium_potential: Optional[float] = Field(
        None,
        alias="magnesiumPotential",
        title="Potential of Magnesium",
        description="The potential of magnesium (pMg) at which the measurements were "
        "performed.",
    )
    temperature: Optional[float] = Field(
        None,
        title="Temperature",
        description="The temperature in Kelvin (K) at which the measurements were "
        "performed.",
    )
    ionic_strength: Optional[float] = Field(
        None,
        alias="ionicStrength",
        title="Ionic Strength",
        description="The molar ionic strength ($I$) of the solution in which the "
        "reaction occurred.",
    )
