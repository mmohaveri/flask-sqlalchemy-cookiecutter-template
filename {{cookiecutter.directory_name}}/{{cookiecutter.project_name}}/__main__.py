#!/usr/bin/env python

import argparse

from typing import Mapping

from .cmd.config import Config

from .cmd.serve import server_command
from .cmd.migrate import migrator_command
from .cmd.create_migrations import migration_creator_command

from toolbelt.cli import Command, Argument


def main():
    command_table: Mapping[str, Command] = {
        "serve": server_command,
        "migrate": migrator_command,
        "create_migrations": migration_creator_command,
    }

    config = Config()
    parser = argparse.ArgumentParser(description="{{cookiecutter.cli_short_description}}")

    parser.add_argument("--config", "-c", type=str, help="config file path")

    sub_parser = parser.add_subparsers(title="mode", description="running modes", required=True, dest="mode")

    for command_name, command_data in command_table.items():
        serve_parser = sub_parser.add_parser(command_name)

        for arg in command_data.args:
            config.set_arg(arg.config_name, *arg.name_or_flags, parser=serve_parser,
                           action=arg.action, required=arg.required, help_str=arg.help_str)

    args = parser.parse_args()

    if args.config is not None:
        config.set_config_file(args.config)

    config.load(args)

    command_table[args.mode].command_class(config).run()


if __name__ == "__main__":
    main()
