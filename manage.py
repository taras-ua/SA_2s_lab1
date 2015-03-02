#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SA_2s_lab1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
