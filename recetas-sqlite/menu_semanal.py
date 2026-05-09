from datetime import datetime


class MenuSemanal:

    def __init__(self, semana, ano):
        self.semana = semana
        self.ano = ano
        self.__platos = []

    def engadirPlato(self, plato):
        self.__platos.append(plato)

    def eliminarPlato(self, nome):
        self.__platos = [
            p for p in self.__platos
            if p.nome != nome
        ]

    def getPlatos(self):
        return self.__platos

    def __str__(self):
        return f"Menu semana {self.semana}/{self.ano}"

    def __len__(self):
        return len(self.__platos)

    @classmethod
    def crear_menu_actual(cls):
        actual = datetime.now()
        semana = actual.isocalendar()[1]
        ano = actual.year

        return cls(semana, ano)