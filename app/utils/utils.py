from marshmallow import ValidationError
from http import HTTPStatus
from app.utils.response import error_response

async def fetch_all_with_or_error(service, error_message="No records found"):
    try:
        items = await service.get_all()
        if not items:
            return None, error_response({"message": error_message}, HTTPStatus.NOT_FOUND)

        return items, None

    except Exception as e:
        return None, error_response(f"An error occurred: {str(e)}", HTTPStatus.INTERNAL_SERVER_ERROR)
