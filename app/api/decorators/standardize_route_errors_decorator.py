from functools import wraps
from http import HTTPStatus
from app.common.responses_old.response_handler import ResponseHandler
from app.common.responses_old.response_messages import ResponseMessages


# DEPRECATED
def standardize_route_errors(f):
    """
    Capture and handle generic errors in routes using standardized response formatting.
    """
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except Exception as e:
            # Use standardized error response with default message
            http_code = HTTPStatus.INTERNAL_SERVER_ERROR
            message = f"{ResponseMessages.get_message_for_status(http_code)}: {
                str(e)}"
            return ResponseHandler.create_response(
                data=None,
                message=message,
                http_code=http_code
            )

    return decorated_function
