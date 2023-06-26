"""
This module configures the BlackSheep application before it starts.
"""
from blacksheep import Application
from config.common import Configuration
from rodi import Container

from .auth import configure_authentication
{%- if cookiecutter.use_openapi | int %}
from .docs import configure_docs
{%- endif %}
from .errors import configure_error_handlers


def configure_application(
    services: Container,
    config: Configuration,
) -> Application:
    app = Application(
        services=services, show_error_details=config.app.show_error_details
    )

    configure_error_handlers(app)
    configure_authentication(app, config)
{%- if cookiecutter.use_openapi | int %}
    configure_docs(app, config)
{%- endif %}
    return app
