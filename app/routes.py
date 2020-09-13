from datetime import datetime

from guardpost import User
from roconfiguration import Configuration

from blacksheep.server import Application
from blacksheep.messages import Response
from blacksheep.server.responses import json, text


def configure_routes(app: Application) -> None:

    # Root route
    # Note: routes can be organized in submodules as desired, and registered inside
    # functions that receive the application as input parameter.
    @app.route("/")
    async def home() -> Response:
        return text(
            f"Hello, World! {datetime.utcnow().isoformat()}. "
            "See `/me` and `/conf` endpoints!"
        )

    # Example showing dependency injection of user object
    # (read from request.identity property, populated by auth code)
    @app.route("/me")
    async def user_info(user: User) -> Response:
        return json(user.claims)

    # Example showing dependency injection of services
    @app.route("/conf")
    async def dependency_injection_example(conf: Configuration) -> Response:
        # Note how `Configuration` service is registered in `app.services.py`;
        # Refer to BlackSheep, and rodi documentation for more information
        return json({"app_name": conf.app_name, "github_url": conf.github_url})
