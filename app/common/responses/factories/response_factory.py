from http import HTTPStatus

from app.common.responses.enums import ResponseMessages, ResponseStatus
from app.common.responses.response_schema import BodySuccessSchema
from app.common.responses.response_types import DataBodyType


class ResponseFactory:
    """
    Factory class for creating different types of response bodies.
    """

    @staticmethod
    def create_success_body(
            data: DataBodyType,
            http_code: HTTPStatus) -> BodySuccessSchema:
        """
        Creates a success body schema.

        Args:
            data (Dict[str, Any]): The data payload for the response.
            http_code (HTTPStatus): The HTTP status code for the response.

        Returns:
            BodySuccessSchema: A standardized success body schema.
        """
        return BodySuccessSchema(
            status=ResponseStatus.SUCCESS,
            message=ResponseMessages.get_message_for_status(http_code),
            data=data)
