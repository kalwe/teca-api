from quart_schema import QuartSchema, Info, Contact

class QuartSchemaConfig:
    """Configuration for Quart Schema."""
    CONVERSION_PREFERENCE = 'pydantic'
    TITLE = "Teca API"
    VERSION = "0.1.0"
    DESCRIPTION = (
        "The `teca-api` is developed in Python using the Quart framework. "
        "It is designed to manage information related to different fields, offering routes for creating, retrieving, updating, and deleting data. "
    )
    CONTACT_NAME = "Kalwe Caramalac"
    CONTACT_URL = "https://github.com/kalwe"
    SUMMARY = "A comprehensive API built with the Quart framework."
    TAGS = [
        {"name": "Address", "description": "Management of addresses, including creation, retrieval, updating, and deletion of addresses."},
        {"name": "Bank Account", "description": "Management of bank accounts, including creation, retrieval, updating, and deletion of bank accounts."},
        {"name": "Clothing", "description": "Management of clothing items, including creation, retrieval, updating, and deletion of clothing items."},
        {"name": "Contact", "description": "Management of contacts, including creation, retrieval, updating, and deletion of contacts."},
        {"name": "Employee", "description": "Management of employees, including creation, retrieval, updating, and deletion of employees."},
        {"name": "Function", "description": "Management of functions, including creation, retrieval, updating, and deletion of functions."},
        {"name": "Reminder", "description": "Management of reminders, including creation, retrieval, updating, and deletion of reminders."},
        {"name": "Roles", "description": "Management of roles, including creation, retrieval, updating, and deletion of roles."},
        {"name": "User", "description": "Management of users, including creation, retrieval, updating, and deletion of users."},
        {"name": "Vacancy", "description": "Management of vacancies, including creation, retrieval, updating, and deletion of vacancies."}
    ]

    @staticmethod
    def configure_schema(app):
        """Configure the Quart Schema for the application."""
        QuartSchema(app, info=Info(
            title=QuartSchemaConfig.TITLE,
            version=QuartSchemaConfig.VERSION,
            description=QuartSchemaConfig.DESCRIPTION,
            contact=Contact(
                name=QuartSchemaConfig.CONTACT_NAME,
                url=QuartSchemaConfig.CONTACT_URL
            ),
            summary=QuartSchemaConfig.SUMMARY,
        ), tags=QuartSchemaConfig.TAGS, conversion_preference=QuartSchemaConfig.CONVERSION_PREFERENCE)
