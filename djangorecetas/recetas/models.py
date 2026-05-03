from django.db import models


class Receta(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    data = models.DateField()
    tempada = models.CharField(max_length=50)
    preparacion = models.TextField()
    foto = models.ImageField(upload_to='recetas/', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    cantidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.cantidade})"

    def __eq__(self, other):
        return self.nome == other.nome
    

class Plato(Receta):
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nome
    

class MenuSemanal(models.Model):
    semana = models.IntegerField()
    ano = models.IntegerField()
    platos = models.ManyToManyField(Plato)

    def __str__(self):
        return f"Semana {self.semana} - {self.ano}"