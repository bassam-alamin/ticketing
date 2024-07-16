#!/usr/bin/env python
import os
import sys
from decouple import config

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config('SETTINGS'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHON PATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
