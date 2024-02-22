#!/usr/bin/env python
import os
import sys

import django

init_flag = True

if init_flag:
    sys.dont_write_bytecode = True

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
    django.setup()

    init_flag = False


def migrate(model):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "makemigrations", model])
    execute_from_command_line(["manage.py", "migrate", model])


if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    # from django.core.management import execute_from_command_line
    #
    # execute_from_command_line(["manage.py", "makemigrations", "models"])
    # execute_from_command_line(["manage.py", "migrate", "models"])
    migrate('db')
    pass
