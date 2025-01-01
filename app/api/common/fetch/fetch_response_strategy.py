from http import HTTPStatus
from app.api.common.fetch.fetch_strategy import FetchStrategy
from app.common.responses.response_strategy import ApiResponseStrategy
from app.core.services.interfaces.base_service import BaseService

class FetchResponseStrategy(ApiResponseStrategy):
    """
    Strategy for handling fetch responses.
    """

    def __init__(self, fetch_strategy: FetchStrategy):
        self.fetch_strategy = fetch_strategy

    async def create_response(self, service: BaseService, *args, **kwargs):
        """
        Handles the fetch flow and formats the response.
        """
        try:
            data = await self.fetch_strategy.fetch(service, *args, **kwargs)
            return self.format_response(
                data=data,
                message="Operation successful",
                status_code=HTTPStatus.OK
            ), HTTPStatus.OK

        except ValueError as not_found_error:
            return self.format_response(
                data=None,
                message=str(not_found_error),
                status_code=HTTPStatus.NOT_FOUND
            ), HTTPStatus.NOT_FOUND

        except Exception as unexpected_error:
            return self.format_response(
                data=None,
                message=f"Internal error: {str(unexpected_error)}",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR
            ), HTTPStatus.INTERNAL_SERVER_ERROR


# from app.api.common.fetch_helpers import FetchItemStrategy, FetchAllItemsStrategy
# from app.decorators.response_decorator import ApiResponseDecorator

# @ApiResponseDecorator.standardize_response
# async def get_item_handler(service: BaseService, item_id: int):
#     fetch_strategy = FetchItemStrategy()
#     fetch_response_strategy = FetchResponseStrategy(fetch_strategy)
#     return await fetch_response_strategy.create_response(service, item_id)

# @ApiResponseDecorator.standardize_response
# async def get_all_items_handler(service: BaseService):
#     fetch_strategy = FetchAllItemsStrategy()
#     fetch_response_strategy = FetchResponseStrategy(fetch_strategy)
#     return await fetch_response_strategy.create_response(service)
