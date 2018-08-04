"""
WSGI config for python_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append("/home/user/python_django")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_django.settings")


application = get_wsgi_application()
