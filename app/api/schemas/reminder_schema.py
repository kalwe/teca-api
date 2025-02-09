from pydantic import Field

from app.api.schemas.base_schema import (
    BaseSchema,
    DeletedSchema,
    InputSchema,
    OutputSchema,
)


class ReminderSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Reminder model using Pydantic.
    """

    date_time: str = Field(max_length=32, description="Name of street")
    title: str = Field(max_length=255, description="Number of street")
    description: str = None

class ReminderInputSchema(ReminderSchema, InputSchema):
   pass


class ReminderOutputSchema(ReminderSchema, OutputSchema):
   pass


class ReminderDeletedSchema(DeletedSchema):
    pass
