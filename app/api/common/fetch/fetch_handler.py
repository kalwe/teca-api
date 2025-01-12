
from app.api.common.fetch.fetch_data_strategy import FetchDataStrategy
from app.api.common.fetch.fetch_strategy import (
    FetchAllItemsStrategy, FetchItemStrategy)


class FetchHandler:
    @staticmethod
    async def fetch_item(service, item_id):
        fetch_strategy = FetchItemStrategy()
        fetch_data = FetchDataStrategy(fetch_strategy, schema)
        return await fetch_data.create_response(service)

    @staticmethod
    async def fetch_all(service):
        fetch_strategy = FetchAllItemsStrategy()
        fetch_response = FetchDataStrategy(fetch_strategy)
        return await fetch_response.create_response(service)
