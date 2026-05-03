from django.db import models


class Receta(models.Model):
    """
    Clase abstracta que representa una receta genérica.

    Parameters
    ----------
    nome : str
        Nombre de la receta.
    tipo : str
        Tipo de receta (ej: primer plato, postre).
    data : datetime.date
        Fecha de creación o publicación.
    tempada : str
        Temporada recomendada para la receta.
    preparacion : str
        Texto con la preparación de la receta.
    foto : ImageField, optional
        Imagen asociada a la receta.

    Notes
    -----
    Esta clase es abstracta y sirve como base para otros modelos.

    Returns
    -------
    str
        Nombre de la receta.
    """

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    tempada = models.CharField(max_length=50)
    preparacion = models.TextField()
    foto = models.ImageField(upload_to='recetas/', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        """
        Devuelve una representación en texto de la receta.

        Returns
        -------
        str
            Nombre de la receta.
        """
        return self.nome


class Ingrediente(models.Model):
    """
    Modelo que representa un ingrediente.

    Parameters
    ----------
    nombre : str
        Nombre del ingrediente.
    cantidad : str
        Cantidad del ingrediente (ej: 200g, 1 litro).

    Returns
    -------
    str
        Representación del ingrediente.
    """

    nome = models.CharField(max_length=100)
    cantidade = models.CharField(max_length=50)

    def __str__(self):
        """
        Representación en texto del ingrediente.

        Returns
        -------
        str
            Nombre y cantidad del ingrediente.
        """
        return f"{self.nome} ({self.cantidade})"

    def __eq__(self, other):
        """
        Compara dos ingredientes por el nombre.

        Parameters
        ----------
        other : Ingrediente
            Otro ingrediente a comparar.

        Returns
        -------
        bool
            True si tienen el mismo nombre, False en caso contrario.
        """
        return self.nome == other.nome


class Plato(Receta):
    """
    Modelo que representa un plato.

    Parameters
    ----------
    ingredientes : ManyToManyField
        Lista de ingredientes asociados al plato.

    Returns
    -------
    str
        Nombre del plato.
    """

    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        """
        Representación en texto del plato.

        Returns
        -------
        str
            Nombre del plato.
        """
        return self.nome


class MenuSemanal(models.Model):
    """
    Modelo que representa un menú semanal.

    Parameters
    ----------
    semana : int
        Número de la semana.
    ano : int
        Año correspondiente.
    platos : ManyToManyField
        Platos incluidos en el menú.

    Returns
    -------
    str
        Representación del menú semanal.
    """

    semana = models.IntegerField()
    ano = models.IntegerField()
    platos = models.ManyToManyField(Plato)

    def __str__(self):
        """
        Representación en texto del menú.

        Returns
        -------
        str
            Texto con la semana y el año.
        """
        return f"Semana {self.semana} - {self.ano}"