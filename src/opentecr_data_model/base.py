from pydantic import BaseModel


class Base(BaseModel):
    """Define a customized base model."""

    class Config:
        """Define default configuration options for all models."""

        anystr_strip_whitespace = True
        allow_population_by_field_name = True
        orm_mode = True
