from django import forms
from .models import Ingrediente, Plato, MenuSemanal


class IngredienteForm(forms.ModelForm):
    """
    Formulario para crear o editar ingredientes.

    Este formulario permite la creación y modificación de objetos
    del modelo Ingrediente.

    :returns: Formulario de ingrediente validado
    :rtype: IngredienteForm
    """

    class Meta:
        """
        Configuración del formulario.

        :ivar model: Modelo asociado al formulario
        :vartype model: Ingrediente

        :ivar fields: Campos incluidos en el formulario
        :vartype fields: list
        """
        model = Ingrediente
        fields = '__all__'


class PlatoForm(forms.ModelForm):
    """
    Formulario para crear o editar platos.

    Este formulario permite gestionar los platos y sus ingredientes.

    :returns: Formulario de plato validado
    :rtype: PlatoForm
    """

    class Meta:
        """
        Configuración del formulario.

        :ivar model: Modelo asociado al formulario
        :vartype model: Plato

        :ivar fields: Campos incluidos en el formulario
        :vartype fields: list
        """
        model = Plato
        fields = '__all__'


class MenuSemanalForm(forms.ModelForm):
    """
    Formulario para crear o editar menús semanales.

    Permite asignar platos a una semana y año concretos.

    :returns: Formulario de menú validado
    :rtype: MenuSemanalForm
    """

    class Meta:
        """
        Configuración del formulario.

        :ivar model: Modelo asociado al formulario
        :vartype model: MenuSemanal

        :ivar fields: Campos incluidos en el formulario
        :vartype fields: list
        """
        model = MenuSemanal
        fields = '__all__'