from flask import Flask, Blueprint
from typing import Any
from importlib import import_module


def register_blueprint(app):
    """Load the routes"""
    for module_name in ("views", "project_routes"):
        module = import_module("pcb_anodet_server.{}.routes".format(module_name))
        app.register_blueprint(module.api_blueprint)


def create_app() -> Any:
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "AOI"
    app.config["SESSION_TYPE"] = "filesystem"
    register_blueprint(app)

    return app
