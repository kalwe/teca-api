
from app.api.common.fetch.fetch_response_strategy import FetchResponseStrategy
from app.api.common.fetch.fetch_strategy import FetchAllItemsStrategy, FetchItemStrategy

class FetchHandler:
    @staticmethod
    async def fetch_item(service, item_id):
        fetch_strategy = FetchItemStrategy()
        fetch_response_strategy = FetchResponseStrategy(fetch_strategy)
        return await fetch_response_strategy.create_response(service, item_id)

    @staticmethod
    async def fetch_all_items(service):
        fetch_strategy = FetchAllItemsStrategy()
        fetch_response_strategy = FetchResponseStrategy(fetch_strategy)
        return await fetch_response_strategy.create_response(service)
