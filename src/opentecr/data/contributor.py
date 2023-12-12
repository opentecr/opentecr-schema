"""Provides data class Contributor."""


from pydantic import Field

from .base import Base


class Contributor(Base):
    """Data about a person who contributes to OpenTECR."""

    orcid: str = Field(
        ...,
        title="ORCID",
        description="The ORCID is a nonproprietary alphanumeric code to uniquely"
        " identify authors and contributors of scholarly communication.",
    )
    name: str = Field(..., title="Name", description="The contributor's full name.")
