import typing

from flask import Flask

from configman import ConfigMan

from ..internal.example.service import UserService

from toolbelt.logging import get_logger
from toolbelt.cli import Command, Argument

from toolbelt.gunicorn import Application
from toolbelt.flask import Path, register_rest_api
from toolbelt.sqlalchemy.process_safe_session import ProcessSafeSessionFactory

if typing.TYPE_CHECKING:
    from .config import Config


class ServerConfig(ConfigMan):
    binding_address: str = "0.0.0.0"
    binding_port: int = 7654

    number_of_workers: int = 10


class Server(object):
    def __init__(self, config: 'Config'):
        self._host = config.server.binding_address
        self._port = config.server.binding_port

        self._flask_app = Flask("{{cookiecutter.project_name}}")

        process_safe_session_factory = ProcessSafeSessionFactory(db_path=config.database)

        logger = get_logger(__name__)

        register_rest_api(
            self._flask_app,
            UserService,
            Path("user_api", "/users/", "user_id"),
            process_safe_session_factory,
            logger
        )

        self._server = Application(self._flask_app, self._host, self._port, config.server.number_of_workers)

    def run(self) -> None:
        self._server.run()


server_command = Command(
    command_class=Server,
    args=[
        Argument("server.number_of_workers", ["--workers"], "Number of gunicorn workers"),
        Argument("server.binding_port", ["--port", "-p"], "Listening port"),
        Argument("server.binding_address", ["--interface", "-i"], "Binding interface")
    ])
