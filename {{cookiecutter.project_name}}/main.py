"""This module is where the application is configured.

To run with uvicorn cli, with hot reload:
    $ uvicorn server:app --port 44777 --reload --log-level info
"""
try:
    import uvloop
except ModuleNotFoundError:
    print("[*] Running without `uvloop`")
    uvloop = ...

from app.config import load_configuration
from app.program import configure_application
from app.services import configure_services

if uvloop is not ...:
    uvloop.install()

app = configure_application(*configure_services(load_configuration()))


if __name__ == "__main__":
    """
    `python main.py` can be used to debug; use this only for local development!
    """
    import os
    import uvicorn
    os.environ["APP_ENV"] = "dev"

    uvicorn.run(app, host="localhost", lifespan="on", log_level="info")
