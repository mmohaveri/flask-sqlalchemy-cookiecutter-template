import typing

from alembic.config import Config as AlembicConfig
from alembic.command import upgrade

from configman import ConfigMan

from toolbelt.cli import Command, Argument

if typing.TYPE_CHECKING:
    from .config import Config


class MigratorConfig(ConfigMan):
    revision: str = "head"
    sql_only: bool = False


class Migrator(object):
    def __init__(self, config: 'Config'):
        self._alembic_config = AlembicConfig()
        self._alembic_config.set_main_option("script_location", "{{cookiecutter.project_name}}/internal/alembic")
        self._alembic_config.set_main_option("sqlalchemy.url", config.database)

        self._revision = config.migrator.revision
        self._sql_only = config.migrator.sql_only

    def run(self):
        upgrade(self._alembic_config, self._revision, self._sql_only)


migrator_command = Command(command_class=Migrator, args=[
    Argument("migrator.revision", ["revision"], "revision to upgrade to"),
    Argument("migrator.sql_only", ["--sql"],
             "instead of applying migration, spit out SQL commands.", action="store_true")
])
