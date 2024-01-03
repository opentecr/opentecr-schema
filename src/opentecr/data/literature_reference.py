"""Provides dataclass LiteratureReference."""

from pydantic import Field

from .base import Base


class LiteratureReference(Base):
    """Information about a literature reference."""

    pubmed_id: str | None = Field(None, alias="pubmedId", title="PubMed Identifier")
    doi: str | None = Field(None, title="Digital Object Identifier (DOI)")
    url: str | None = Field(None, title="Universal Resource Locator (URL)")
    title: str = Field(..., title="Title")
    authors: str = Field(..., title="Authors")
    year: int = Field(..., title="Year")
