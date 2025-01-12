from dynaconf import settings
from quart import Blueprint


api_settings = Blueprint("api_settings", __name__)


@api_settings.route("/settings")
async def api_settings() -> str:
    return (
        "<h3>Settings</h3>"
        + f"<p>Dynaconf Environment: {settings.ENV_FOR_DYNACONF}</p><br>"
        + f"<p>DB_HOST: {settings.DB_HOST}</p>"  # type: ignore
    )
