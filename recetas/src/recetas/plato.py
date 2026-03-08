from .receta_base import Receta
from .ingrediente import Ingrediente


class Plato(Receta): #herencia

    def __init__(self, nome, tipo, data, tempada, preparacion, foto):
        super().__init__(nome, tipo, data, tempada, preparacion, foto)
        self.__ingredientes = []

    def engadirIngrediente(self, ingrediente: Ingrediente):
        self.__ingredientes.append(ingrediente)

    def eliminarIngrediente(self, nome: str):
        self.__ingredientes = [
            i for i in self.__ingredientes if i.nome != nome
        ]

    def getIngredientes(self):
        return self.__ingredientes

    def mostrar(self):
        texto = f"Plato: {self.nome}\n"
        texto += "Ingredientes:\n"

        for i in self.__ingredientes:
            texto += f" - {i}\n"

        return texto

    def __len__(self):
        return len(self.__ingredientes)

    def __repr__(self):
        return f"Plato({self.nome})"