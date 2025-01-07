from typing import TYPE_CHECKING, Any, Dict, Union

from app.common.responses.response_schema import (
    BodyErrorSchema, BodySuccessSchema
)

if TYPE_CHECKING:
    from app.common.responses.response_schema import (
        BodyErrorSchema, BodySuccessSchema
    )

# Define a type for JSON
JSONType = Union[Dict[str, Any]]

# Define a type alias for the response body schema
BodySchemaType = Union[BodySuccessSchema, BodyErrorSchema]
