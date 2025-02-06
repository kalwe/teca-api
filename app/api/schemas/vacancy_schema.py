from pydantic import Field
from app.api.schemas.base_schema import BaseSchema, InputBaseSchema, OutputBaseSchema


class VacancyBaseSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Vacancy model using Pydantic.
    """
    street: str = Field(
        max_length=255,
        description="Name of street"
    )
    number: str = Field(
        max_length=8,
        description="Number of street"
    )
    neighborhood: str = Field(
        max_length=120,
        description="Name of neighborhood"
    )
    city: str = Field(
        max_length=255,
        description="Name of the city"
    )
    zip_code: str = Field(
        max_length=12,
        description="CEP of street"
    )
    state: str = Field(
        max_length=60,
        description="Name of state"
    )

class VacancyInputSchema(VacancyBaseSchema, InputBaseSchema):
   pass

class VacancyOutputSchema(VacancyBaseSchema, OutputBaseSchema):
   pass
