from django import forms
from .models import Ingrediente, Plato, MenuSemanal

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'


class MenuSemanalForm(forms.ModelForm):
    class Meta:
        model = MenuSemanal
        fields = '__all__'