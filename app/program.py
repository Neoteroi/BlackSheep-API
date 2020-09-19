from rodi import Container

from roconfiguration import Configuration
from blacksheep.server import Application

from core.events import ServicesRegistrationContext
from .auth import configure_authentication
from .errors import configure_error_handlers
from .routes import configure_routes


def configure_application(
    services: Container,
    context: ServicesRegistrationContext,
    configuration: Configuration,
) -> Application:
    app = Application(
        services=services, show_error_details=configuration.show_error_details
    )

    configure_routes(app)

    app.on_start += context.initialize
    app.on_stop += context.dispose

    configure_error_handlers(app)
    configure_authentication(app)

    return app
