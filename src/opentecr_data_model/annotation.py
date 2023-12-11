from pydantic import Field

from .base import Base


class Annotation(Base):

    namespace: str = Field(
        ...,
        description="The MIRIAM compliant prefix of the identifier namespace. MUST be "
        "registered at https://identifiers.org/.",
    )
    identifier: str = Field(
        ..., description="The actual identifier within the namespace."
    )
    # FIXME: add a qualifier field?
