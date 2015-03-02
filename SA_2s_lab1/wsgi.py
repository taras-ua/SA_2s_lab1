"""
WSGI config for SA_2s_lab1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SA_2s_lab1.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
