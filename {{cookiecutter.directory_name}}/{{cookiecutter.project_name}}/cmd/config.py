from configman import ConfigMan

from .serve import ServerConfig
from .migrate import MigratorConfig
from .create_migrations import MigrationCreatorConfig


class Config(ConfigMan):
    server: ServerConfig = ServerConfig()
    migrator: MigratorConfig = MigratorConfig()
    migration_creator: MigrationCreatorConfig = MigrationCreatorConfig()

    database: str = "sqlite:///test.sqlite3"
