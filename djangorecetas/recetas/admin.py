from django.contrib import admin
from .models import Ingrediente, Plato, MenuSemanal

admin.site.register(Ingrediente)
admin.site.register(Plato)
admin.site.register(MenuSemanal)