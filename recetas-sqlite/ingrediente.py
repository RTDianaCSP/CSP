class Ingrediente:

    def __init__(self, nome, cantidade):
        self.nome = nome
        self.cantidade = cantidade

    def __str__(self):
        return f"{self.nome} ({self.cantidade})"

    def __eq__(self, other):
        return self.nome == other.nome