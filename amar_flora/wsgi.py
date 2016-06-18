"""
WSGI config for amar_flora project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
#import sys

#sys.path.append('/usr/local/lib/python3.4/dist-packages/')


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "amar_flora.settings")

application = get_wsgi_application()
