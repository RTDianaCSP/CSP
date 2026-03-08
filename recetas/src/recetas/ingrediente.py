class Ingrediente:

    def __init__(self, nome: str, cantidade: str):
        self.nome = nome
        self.cantidade = cantidade

    def __str__(self):
        return f"{self.nome} - {self.cantidade}"

    def __eq__(self, other):
        if isinstance(other, Ingrediente):
            return self.nome == other.nome
        return False