import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inte_edc.settings.uganda.namulonge")

application = get_wsgi_application()
