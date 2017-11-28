#!/usr/bin/env python
import os
import sys




if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "confdjango_backend.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    
    
from django.conf import settings
sys.path.append(os.path.join(settings.BASE_DIR, "apps"))