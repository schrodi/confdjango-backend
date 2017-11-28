"""
WSGI config for confdjango_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

from django.conf import settings
sys.path.append(os.path.join(settings.BASE_DIR, "apps"))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "confdjango_backend.settings")

application = get_wsgi_application()
