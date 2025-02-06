from pydantic import Field
from app.api.schemas.base_schema import BaseSchema, InputBaseSchema, OutputBaseSchema


class FunctionSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Function model using Pydantic.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=120,
        description="Name of function",
    )


class FunctionInputSchema(FunctionSchema, InputBaseSchema):
   pass

class FunctionOutputSchema(FunctionSchema, OutputBaseSchema):
   pass
