from .excepcions import PlatoDuplicadoError


class MenuSemanal:

    def __init__(self, semana: int, ano: int):
        self.semana = semana
        self.ano = ano
        self.__platos = []#atributo privado

    def engadirPlato(self, plato):

        if plato in self.__platos:
            raise PlatoDuplicadoError()

        self.__platos.append(plato)

    def eliminarPlato(self, nome: str):

        self.__platos = [
            p for p in self.__platos if p.nome != nome
        ]

    def getPlatos(self):
        return self.__platos

    def __str__(self):
        return f"Menu semana {self.semana}/{self.ano}"

    def __len__(self):
        return len(self.__platos)

    @classmethod
    def crear_menu_actual(cls):

        import datetime

        hoy = datetime.date.today()

        semana = hoy.isocalendar()[1]
        ano = hoy.year

        return cls(semana, ano)