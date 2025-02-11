from quart import Blueprint


class BaseRoute:
    def __init__(self, bp: Blueprint, controller, singular_prefix: str, plural_prefix: str):
        self.bp = bp
        self.controller = controller
        self.singular_prefix = singular_prefix
        self.plural_prefix = plural_prefix
        self.init_routes()

    def init_routes(self):
        # crate
        self.bp.add_url_rule(
            "/",
            view_func=getattr(self.controller, f"create_{self.singular_prefix}"),
            methods=["POST"],
        )
        # get_by_id
        self.bp.add_url_rule(
            '/<int:id>',
            view_func=getattr(self.controller, f'get_{self.singular_prefix}'),
            methods=["GET"]
        )
        # get_all
        self.bp.add_url_rule(
            '/',
            view_func=getattr(self.controller, f'get_all_{self.plural_prefix}'),
            methods=["GET"]
        )
        # update
        self.bp.add_url_rule(
            '/<int:id>',
            view_func=getattr(self.controller, f'update_{self.singular_prefix}'),
            methods=["POST"]
        )
        # delete
        self.bp.add_url_rule(
            '/<int:id>',
            view_func=getattr(self.controller, f'delete_{self.singular_prefix}'),
            methods=["DELETE"]
        )
