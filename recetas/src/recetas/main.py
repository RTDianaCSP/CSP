from recetas.plato import Plato
from recetas.ingrediente import Ingrediente
from recetas.menu_semanal import MenuSemanal
from recetas.xestor_menus import XestorMenus

#PROBAS DE FUNCIONAMENTO DA APLICACIÓN
def main(): 

    i1 = Ingrediente("Ovos", "2")
    i2 = Ingrediente("Patacas", "5")
    i3 = Ingrediente("Sal", "1")

    tortilla = Plato(
        "Tortilla",
        "cena",
        "2025-03-01",
        "todo o ano",
        "Bater ovos e fritir",
        "tortilla.jpg"
    )

    tortilla.engadirIngrediente(i1)
    tortilla.engadirIngrediente(i2)
    tortilla.engadirIngrediente(i3)

    menu = MenuSemanal.crear_menu_actual()
    menu.engadirPlato(tortilla)


    xestor = XestorMenus()
    xestor.engadirMenu(menu)

    resultado = xestor.buscarPorPlato("Tortilla")

    for p in resultado:
        print(p.mostrar())


if __name__ == "__main__":
    main()