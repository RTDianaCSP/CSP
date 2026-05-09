from abc import ABC, abstractmethod


class Receta(ABC):

    def __init__(self, nome, tipo, data, tempada, preparacion, foto):
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.tempada = tempada
        self.preparacion = preparacion
        self.foto = foto

    @abstractmethod
    def mostrar(self):
        pass

    def __str__(self):
        return f"{self.nome} - {self.tipo}"