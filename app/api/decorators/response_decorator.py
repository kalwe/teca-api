from functools import wraps
from typing import Callable

from pydantic import ValidationError

from app.common.responses.response_error_handler import ResponseErrorHandler
from app.common.responses.response_handler import ResponseHandler


class ResponseDecorator:
    """
    Decorator to handle responses and apply consistent formatting for Quart routes.

    Methods:
        handle_response: A decorator to wrap route functions and format their responses.
    """

    @staticmethod
    def build_response(func: Callable) -> Callable:
        """
        Decorator to handle responses for Quart route functions. Ensures consistent
        formatting of the response and handles validation and generic exceptions.

        Args:
            func (Callable): The Quart route function being decorated.

        Returns:
            Callable: A wrapped function with response handling.
        """

        @wraps(func)
        async def decorated_function(*args, **kwargs):
            """
            Wrapper function to process the result of the decorated route and handle errors.

            Args:
                *args: Positional arguments for the original route function.
                **kwargs: Keyword arguments for the original route function.

            Returns:
                Response: A formatted response object with a standardized schema.
            """
            try:
                # Execute the original route function
                result = await func(*args, **kwargs)

                # Extract result and HTTP status
                data, http_code = ResponseHandler.extract_result(result)

                # Create a success response
                response_schema = ResponseHandler.create_success_response(
                    data=data,
                    http_code=http_code)
                return await ResponseHandler.convert_to_response(
                    response_schema)

            except ValidationError as e:
                # Handle validation errors
                response_schema = (ResponseErrorHandler.
                                   create_validation_error_response(e))
                return await ResponseHandler.convert_to_response(
                    response_schema)

            except Exception as e:
                # Handle generic exceptions
                response_schema = (ResponseErrorHandler.
                                   create_generic_error_response(e))
                return await ResponseHandler.convert_to_response(
                    response_schema)

        return decorated_function
