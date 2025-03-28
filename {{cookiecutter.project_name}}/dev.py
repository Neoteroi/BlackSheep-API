"""
Runs the application for local development. This file should not be used to start the
application for production.

Refer to https://www.uvicorn.org/deployment/ for production deployments.
"""
import os

import uvicorn
from blacksheep.server.env import get_global_route_prefix
from rich.console import Console

try:
    import uvloop
except ModuleNotFoundError:
    pass
else:
    uvloop.install()

if __name__ == "__main__":
    os.environ["APP_ENV"] = "dev"
    os.environ["APP_SHOW_ERROR_DETAILS"] = "1"
    port = int(os.environ.get("APP_PORT", 44777))

    prefix = get_global_route_prefix()
    if prefix:
        prefix = prefix.strip("/") + "/"
    console = Console()
    console.rule("[bold yellow]Running for local development", align="left")
{%- if cookiecutter.use_openapi %}
    console.print(f"[bold yellow]Visit http://localhost:{port}/{prefix}docs/\n")
{%- endif %}

    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=port,
        lifespan="on",
        log_level="info",
        reload=True,
    )
