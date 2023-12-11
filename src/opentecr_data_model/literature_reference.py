from typing import Optional

from pydantic import Field

from .base import Base


class LiteratureReference(Base):

    pubmed_id: Optional[str] = Field(None, alias="pubmedId", title="PubMed Identifier")
    doi: Optional[str] = Field(None, title="Digital Object Identifier (DOI)")
    url: Optional[str] = Field(None, title="Universal Resource Locator (URL)")
    title: str = Field(..., title="Title")
    authors: str = Field(..., title="Authors")
    year: int = Field(..., title="Year")
