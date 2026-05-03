import os
import django
import pydoc

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangorecetas.settings")
django.setup()

pydoc.help("recetas.models")