from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, Tuple, Union

from pydantic_core import ErrorDetails

from app.common.responses.response_schema import (
    BodyErrorSchema, BodySuccessSchema)

if TYPE_CHECKING:
    from app.common.responses.response_schema import (
        BodyErrorSchema, BodySuccessSchema)

# Define a type for data body(JSON)
DictType = Dict[str, Any]

# Define a type alias for the response body schema
BodySchemaType = Union[BodySuccessSchema, BodyErrorSchema]

# Define a type alias for ErrorDetailsType
ErrorDetailsType = Union[list[ErrorDetails], Exception]

# Define a type alias for Result extraction
ResultType = Union[Any, Tuple[Any, int]]
# Less flexible
ResultReturnType = Tuple[DictType, HTTPStatus]
