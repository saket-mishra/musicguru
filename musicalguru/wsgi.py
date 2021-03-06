"""
WSGI config for musicalguru project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicalguru.settings")

application = get_wsgi_application()

try:
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)	
    from dj_static import Cling
    application = Cling(MediaCling(get_wsgi_application()))
except:
		pass