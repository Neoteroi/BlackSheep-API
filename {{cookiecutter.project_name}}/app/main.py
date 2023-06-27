"""
This module configures the BlackSheep application before it starts.
"""
from blacksheep import Application
from config.common import Configuration
from rodi import Container

from app.auth import configure_authentication
from app.config import load_configuration
{%- if cookiecutter.use_openapi == "True" %}
from app.docs import configure_docs
{%- endif %}
from app.errors import configure_error_handlers
from app.services import configure_services


def configure_application(
    services: Container,
    config: Configuration,
) -> Application:
    app = Application(
        services=services, show_error_details=config.app.show_error_details
    )

    configure_error_handlers(app)
    configure_authentication(app, config)
{%- if cookiecutter.use_openapi == "True" %}
    configure_docs(app, config)
{%- endif %}
    return app


app = configure_application(*configure_services(load_configuration()))
