"""Provides dataclass CuratedMeasurement."""


from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from .base import Base

if TYPE_CHECKING:
    from .contributor import Contributor
    from .literature_reference import LiteratureReference
    from .representative_reaction import RepresentativeReaction


class CuratedMeasurement(Base):
    """Define a curated measurement of thermodynamic information and context."""

    reference: LiteratureReference = Field(
        ...,
        title="Literature Reference",
        description="The official source from which these measurements were curated. "
        "Ideally identified by a DOI.",
    )
    curator: Contributor | None = Field(
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
    equilibrium_constant: float | None = Field(
        None,
        alias="equilibriumConstant",
        title="Equilibrium Constant",
        description="The equilibrium constant ($K$) of this reaction.",
    )
    hydrogen_potential: float | None = Field(
        None,
        alias="hydrogenPotential",
        title="Potential of Hydrogen",
        description="The potential of hydrogen (pH) at which the measurements were "
        "performed.",
    )
    magnesium_potential: float | None = Field(
        None,
        alias="magnesiumPotential",
        title="Potential of Magnesium",
        description="The potential of magnesium (pMg) at which the measurements were "
        "performed.",
    )
    temperature: float | None = Field(
        None,
        title="Temperature",
        description="The temperature in Kelvin (K) at which the measurements were "
        "performed.",
    )
    ionic_strength: float | None = Field(
        None,
        alias="ionicStrength",
        title="Ionic Strength",
        description="The molar ionic strength ($I$) of the solution in which the "
        "reaction occurred.",
    )
