from http import HTTPStatus
from typing import Any, Type
from app.api.common.fetch.fetch_strategy import FetchStrategy
from app.api.schemas.base_schema import BaseSchema
from app.core.services.interfaces.get_service_interface import BaseService


class FetchDataStrategy(ResponseStrategy):
    """
    Strategy for handling fetch responses.
    """

    DEFAULT_STATUSES = {
        ResponseStatus.SUCCESS: HTTPStatus.OK,
        ResponseStatus.NOT_FOUND: HTTPStatus.NOT_FOUND,
        ResponseStatus.ERROR: HTTPStatus.INTERNAL_SERVER_ERROR,
    }

    def __init__(self, fetch_strategy: FetchStrategy, schema: Type[BaseSchema], custom_statuses=None):
        """
        Initialize the response handler with the desired schema for serialization.

        :param schema: The schema to use for serializing the fetched data.
        :param custom_statuses: Optional custom HTTP status mappings.
        """
        self.fetch_strategy = fetch_strategy
        self.schema = schema
        self.statuses = {**self.DEFAULT_STATUSES, **(custom_statuses or {})}

    def get_status(self, status_key: ResponseStatus):
        """
        Retrieve the HTTP status code for a given ResponseStatus key.

        Args:
            status_key (ResponseStatus): The status type.

        Returns:
            HTTPStatus: Corresponding HTTP status code.
        """
        return self.statuses.get(status_key, HTTPStatus.INTERNAL_SERVER_ERROR)

    def get_success_message(self, data):
        """
        Determine the success message based on the fetched data type.

        Args:
            data: The fetched data.

        Returns:
            str: The appropriate success message.
        """
        if isinstance(data, list):
            return ResponseMessages.FETCHED_ALL_SUCCESS.value
        return ResponseMessages.FETCHED_SINGLE_SUCCESS.value

    async def create_response(self, service: BaseService, fetch_strategy: callable, *args, **kwargs):
        """
        Handles the fetch flow and formats the response.
        """
        try:
            data = await self.fetch_strategy.fetch(service, *args, **kwargs)
            success_status = self.get_status(ResponseStatus.SUCCESS)
            success_message = self.get_success_message(data)

            schema_instance = self.schema()
            serialized_data = schema_instance.dump(data)

            return self.format_response(
                status=ResponseStatus.SUCCESS,  # TODO:
                data=serialized_data,
                message=success_message,
                http_code=success_status
            ), success_status
        except ValueError as not_found_error:
            not_found_status = self.get_status(ResponseStatus.NOT_FOUND)
            return self.format_response(
                status=ResponseStatus.FAILURE,  # TODO:
                data=None,
                message=f"{ResponseMessages.get_message_for_status(not_found_status)}: {
                    str(not_found_error)}",
                http_code=not_found_status
            ), not_found_status

        except Exception as unexpected_error:
            error_status = self.get_status(ResponseStatus.ERROR)
            return self.format_response(
                data=None,
                message=f"{ResponseMessages.get_message_for_status(error_status)}: {
                    str(unexpected_error)}",
                http_code=error_status
            ), error_status

    def format_response(self, status, data: Any, message: str, http_code: HTTPStatus):
        """
        Formats the response data into the expected structure.
        """
        return {
            "status": status,  # TODO:
            "http_code": http_code.value,
            "message": message,
            "data": data
        }
