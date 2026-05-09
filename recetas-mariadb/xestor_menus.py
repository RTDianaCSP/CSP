class XestorMenus:

    def __init__(self):
        self.__menus = []

    def engadirMenu(self, menu):
        self.__menus.append(menu)

    def buscarPorSemana(self, semana, ano):
        for menu in self.__menus:
            if menu.semana == semana and menu.ano == ano:
                return menu

        return None

    def buscarPorNome(self, nome):
        resultado = []

        for menu in self.__menus:
            for plato in menu.getPlatos():
                if plato.nome == nome:
                    resultado.append(plato)

        return resultado

    def __len__(self):
        return len(self.__menus)

    def __repr__(self):
        return f"XestorMenus({len(self.__menus)} menus)"