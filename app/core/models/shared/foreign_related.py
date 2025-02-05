from tortoise.fields import ForeignKeyField


class ForeignRelated:
    """
        Create relation between Parent() and Child()
    """
    # @classmethod
    # def foreign_relation(cls, parent_model: MODEL):
    #     """
    #         Define Parent class model in Child
    #     """
    #     return ForeignKeyRelation[parent_model]

    @classmethod
    def foreign_key(cls, parent_model: str, related_name: str):
        """
            Link Child in Parent
        """
        return ForeignKeyField(
            f"models.{parent_model}",
            related_name=related_name
        )
