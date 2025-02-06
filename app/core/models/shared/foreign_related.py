from tortoise import fields
# from tortoise.fields.base import Field
# from tortoise.fields.relational import MODEL, ForeignKeyRelation


class ForeignRelated:
    """
        Create relation between Parent() and Child()
    """

    # def __init__(self, parent_model: MODEL):
    #     self._parent_model = parent_model

    # @staticmethod
    # def foreign_parent[MODEL]():
    #     """
    #         Define Parent class model in Child
    #     """
    #     return fields.ForeignKeyRelation[MODEL]

    @staticmethod
    def foreign_related(parent_model: str, related_name: str):
        """
            Link Child in Parent
        """
        return fields.ForeignKeyField(
            f"models.{parent_model}",
            related_name=related_name
        )

# class ForeignParent(Field[MODEL])
