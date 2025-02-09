from typing import Optional
from app.api.schemas.roles_schema import RolesInputSchema, RolesOutputSchema
from app.core.repositories.roles.roles_create_repository import RolesCreateRepository
from app.core.services.shared.create_service import CreateService


class RolesCreateService(CreateService):
    """
    Service for managing roles-related business logic.
    Handles creation of new roless with role assignment and password hashing.
    """

    def __init__(self, repository: RolesCreateRepository):
        """
        Initialize the service with a repository for roles operations.

        Args:
            repository (RolesCreateRepository): An instance of
                RolesCreateRepository
                to handle data persistence for the Roles model.
        """
        super().__init__(repository)
        # self._get_service = RolesGetService(RolesGetRepository(Roles()))

    async def create(
        self,
        roles_data: RolesInputSchema,
    ) -> Optional[RolesOutputSchema]:
        (
            """
        Create a new roles with additional business logic.

        Args:
            name (str): The name of the roles.
            email (str): The email of the roles.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the roles.

        Returns:
            RolesOutputSchema: Serialized data of the created roles.

        Raises:
            RolesAlreadyExistsException: If a roles with the given email
            already exists.
        """
            """
        Create a new roles with additional business logic.

        Args:
            name (str): The name of the roles.
            email (str): The email of the roles.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the roles.

        Returns:
            RolesOutputSchema: Serialized data of the created roles.

        Raises:
            RolesAlreadyExistsException: If a roles with the given email
            already exists.
        """
        )
        created_roles = await self.create_record(roles_data)
        return RolesOutputSchema().validate(created_roles)
