from abc import ABC, abstractmethod


class Receta(ABC):

    def __init__(self, nome: str, tipo: str, data, tempada: str, preparacion: str, foto: str):
        self.nome = nome #atributo publico
        self.tipo = tipo
        self.data = data
        self.tempada = tempada
        self.preparacion = preparacion
        self.foto = foto

    @abstractmethod #metodo abstracto
    def mostrar(self):
        pass

    def __str__(self): #dunder method
        return f"{self.nome} ({self.tipo})"