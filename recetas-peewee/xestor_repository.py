from menu_repository import crear_menu, listar_menus


class XestorRepository:

    def gardar_menu(self, menu):
        crear_menu(menu)

    def listar_menus(self):
        return listar_menus()