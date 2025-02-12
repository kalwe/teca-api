from pydantic import Field

from app.api.schemas.base_schema import (
    BaseSchema,
    DeletedSchema,
    InputSchema,
    OutputSchema,
)


class VacancySchema(BaseSchema):
    """
    Schema for serializing and deserializing the Vacancy model using Pydantic.
    """

    quantity: int = Field(description="Quantity of vacancies")
    position: str = Field(max_length=32, description="Position of vacancy")
    description: str = Field(max_length=32, description="Description of vacancy")
    requirements: str = Field(max_length=255, description="Requirements of vacancy")
    benefits: str = Field(max_length=255, description="Benefits of vacancy")
    salary: int = Field(description="Salary of vacancy")


class VacancyInputSchema(VacancySchema, InputSchema):
    pass


class VacancyOutputSchema(VacancySchema, OutputSchema):
    pass


class VacancyDeletedSchema(DeletedSchema):
    pass
