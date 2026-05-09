from receta import Receta


class Plato(Receta):

    def __init__(self, nome, tipo, data, tempada, preparacion, foto):
        super().__init__(nome, tipo, data, tempada, preparacion, foto)
        self.__ingredientes = []

    def engadirIngrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)

    def eliminarIngrediente(self, nome):
        self.__ingredientes = [
            i for i in self.__ingredientes
            if i.nome != nome
        ]

    def getIngredientes(self):
        return self.__ingredientes

    def mostrar(self):
        print(f"Prato: {self.nome}")

        for ingrediente in self.__ingredientes:
            print(f" - {ingrediente}")

    def __str__(self):
        return f"Plato: {self.nome}"

    def __len__(self):
        return len(self.__ingredientes)

    def __repr__(self):
        return self.__str__()