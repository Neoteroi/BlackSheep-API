from rodi import Container
from guardpost import User
from datetime import datetime
from roconfiguration import Configuration
from blacksheep.server import Application
from blacksheep.server.responses import text, json
from core.events import ServicesRegistrationContext
from .auth import configure_authentication
from .errors import configure_error_handlers


def configure_application(services: Container,
                          context: ServicesRegistrationContext,
                          configuration: Configuration):
    app = Application(services=services,
                      show_error_details=configuration.show_error_details)

    # Root route
    # Note: routes can be organized in submodules as desired, and registered inside functions that receive the
    # application as input parameter.
    @app.route('/')
    async def home():
        return text(f'Hello, World! {datetime.utcnow().isoformat()}. See `/me` and `/conf` endpoints!')

    # Example showing dependency injection of user object (read from request.identity property, populated by auth code)
    @app.route('/me')
    async def user_info(user: User):
        return json(user.claims)

    # Example showing dependency injection of services
    @app.route('/conf')
    async def dependency_injection_example(conf: Configuration):
        # Note how `Configuration` service is registered in `app.services.py`;
        # Refer to BlackSheep, and rodi documentation for more information
        return json({
            'app_name': conf.app_name,
            'github_url': conf.github_url
        })

    app.on_start += context.initialize
    app.on_stop += context.dispose

    configure_error_handlers(app)
    configure_authentication(app)

    return app
