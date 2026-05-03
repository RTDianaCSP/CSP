from django import forms
from .models import Ingrediente, Plato, MenuSemanal


class IngredienteForm(forms.ModelForm):
    """
    Formulario para crear ou editar ingredientes.

    Permite a creación e modificación de obxectos do modelo Ingrediente.
    """

    class Meta:
        """
        Configuración do formulario.

        Attributes:
            model: Modelo asociado ao formulario (Ingrediente)
            fields: Campos incluídos no formulario
        """
        model = Ingrediente
        fields = '__all__'


class PlatoForm(forms.ModelForm):
    """
    Formulario para crear ou editar pratos.

    Permite xestionar pratos e os seus ingredientes.
    """

    class Meta:
        """
        Configuración do formulario.

        Attributes:
            model: Modelo asociado ao formulario (Plato)
            fields: Campos incluídos no formulario
        """
        model = Plato
        fields = '__all__'


class MenuSemanalForm(forms.ModelForm):
    """
    Formulario para crear ou editar menús semanais.

    Permite asignar pratos a unha semana e ano concretos.
    """

    class Meta:
        """
        Configuración do formulario.

        Attributes:
            model: Modelo asociado ao formulario (MenuSemanal)
            fields: Campos incluídos no formulario
        """
        model = MenuSemanal
        fields = '__all__'