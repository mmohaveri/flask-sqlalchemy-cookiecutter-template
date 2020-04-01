import typing

from alembic.config import Config as AlembicConfig
from alembic.command import revision

from configman import ConfigMan

from toolbelt.cli import Command, Argument

if typing.TYPE_CHECKING:
    from .config import Config


class MigrationCreatorConfig(ConfigMan):
    migration_message: str = ""
    auto_generate: bool = False


class MigrationCreator(object):
    def __init__(self, config: 'Config'):
        self._alembic_config = AlembicConfig()
        self._alembic_config.set_main_option("script_location", "{{cookiecutter.project_name}}/internal/alembic")
        self._alembic_config.set_main_option("sqlalchemy.url", config.database)

        self._migration_message = config.migration_creator.migration_message
        self._auto_generate = config.migration_creator.auto_generate

    def run(self):
        revision(self._alembic_config, self._migration_message, autogenerate=self._auto_generate)


migration_creator_command = Command(
    command_class=MigrationCreator,
    args=[
        Argument("migration_creator.migration_message", ["migration_message"], "new migration's message"),
        Argument("migration_creator.auto_generate", ["--auto-generate"],
                 "try to auto-generate migration", action="store_true")
    ]
)
