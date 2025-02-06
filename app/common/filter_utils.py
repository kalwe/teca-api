from tortoise.expressions import Q
from http import HTTPStatus
from app.responses.response_handler import unified_response


def build_filters(**kwargs):
    filters = {}
    for key, value in kwargs.items():
        if value.lower() == 'true':
            filters[key] = True
        elif value.lower() == 'false':
            filters[key] = False
        else:
            filters[key] = value
    return filters


async def apply_filters(query, filters: dict, operator: str = "AND"):
    if filters:
        expressions = [Q(**{key: value}) for key, value in filters.items()]
        if operator.upper() == "OR":
            query = query.filter(Q(*expressions, join_type="OR"))
        else:
            query = query.filter(*expressions)
    return await query


async def get_filtered_items(repository, filters: dict, operator: str = "AND"):
    if not filters:
        return await repository.get_all()

    items = await repository.get_filtered(filters, operator)
    if not items:
        error_messages = []
        for key, value in filters.items():
            single_filter = {key: value}
            single_item = await repository.get_filtered(single_filter, operator)
            if not single_item:
                error_messages.append(f'No item found with "{key}" = {value}')
        return None, error_messages

    return items, None

# TODO: monkey check


async def get_all_items(get_service, repository, request_args, output_schema):
    args = request_args.to_dict()
    operator = args.pop("operator", "AND")
    filters = build_filters(**args)
    error_messages = []

    if not filters:
        items = await get_service.get_all()
    else:
        items, error_messages = await get_filtered_items(repository, filters, operator)

    if not items:
        if error_messages:
            return unified_response(message=" | ".join(error_messages), http_code=HTTPStatus.NOT_FOUND)
        return unified_response(message="No item found", http_code=HTTPStatus.NOT_FOUND)

    items_result = output_schema(many=True).dump(items)
    return unified_response(data=items_result, message="Item Obtained Sucessfully", http_code=HTTPStatus.OK)
