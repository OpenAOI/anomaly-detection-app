from flask import Flask
from typing import Any


def create_app() -> Any:
    app = Flask(__name__, instance_relative_config=True)
    from pcb_anodet_server.api import api_blueprint

    app.register_blueprint(api_blueprint)
    app.secret_key = "AOI"
    app.config["SESSION_TYPE"] = "filesystem"

    return app
