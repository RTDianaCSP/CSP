from ingrediente import Ingrediente
from plato import Plato
from menu_semanal import MenuSemanal

from plato_repository import crear_plato, obter_platos
from xestor_repository import XestorRepository


def crear_novo_plato():

    print("--- CREAR NOVO PLATO ---")

    nome = input("Nome do prato: ")
    tipo = input("Tipo: ")
    data = input("Data: ")
    tempada = input("Tempada: ")
    preparacion = input("Preparación: ")
    foto = input("Foto: ")

    plato = Plato(
        nome,
        tipo,
        data,
        tempada,
        preparacion,
        foto
    )

    while True:

        engadir = input("Engadir ingrediente? (s/n): ").lower()

        if engadir != "s":
            break

        nome_ing = input("Nome ingrediente: ")
        cantidade = input("Cantidade: ")

        ingrediente = Ingrediente(nome_ing, cantidade)
        plato.engadirIngrediente(ingrediente)

    try:
        crear_plato(plato)
        print("Plato gardado correctamente")

    except Exception as e:
        print(f"ERRO: {e}")


def mostrar_platos():

    print("--- PLATOS ---")

    platos = obter_platos()

    if not platos:
        print("Non hai platos gardados")
        return

    for plato in platos:
        print(plato.nome)


def crear_novo_menu():

    print("--- CREAR MENU SEMANAL ---")

    menu = MenuSemanal.crear_menu_actual()

    platos = obter_platos()

    if not platos:
        print("Non existen platos na base de datos")
        return

    print("Platos dispoñibles:")

    for plato in platos:
        print(f"- {plato.nome}")

    while True:

        nome_plato = input("Nome do plato para engadir (0 para terminar): ")

        if nome_plato == "0":
            break

        atopado = None

        for p in platos:
            if p.nome == nome_plato:
                atopado = p
                break

        if atopado:

            plato_obj = Plato(
                atopado.nome,
                atopado.tipo,
                atopado.data,
                atopado.tempada,
                atopado.preparacion,
                atopado.foto
            )

            menu.engadirPlato(plato_obj)
            print("Plato engadido")

        else:
            print("Plato non encontrado")

    xestor = XestorRepository()
    xestor.gardar_menu(menu)

    print("Menu creado correctamente")


def mostrar_menus():

    print("--- MENUS ---")

    xestor = XestorRepository()
    menus = xestor.listar_menus()

    if not menus:
        print("Non hai menus")
        return

    for menu in menus:
        print(f"Semana: {menu.semana} - Ano: {menu.ano}")


def menu_principal():

    while True:

        print("""
============================
    XESTOR DE RECEITAS
============================

1. Crear plato
2. Ver platos
3. Crear menú semanal
4. Ver menús
0. Saír
""")

        opcion = input("Selecciona unha opción: ")

        match opcion:

            case "1":
                crear_novo_plato()

            case "2":
                mostrar_platos()

            case "3":
                crear_novo_menu()

            case "4":
                mostrar_menus()

            case "0":
                print("Saíndo da aplicación...")
                break

            case _:
                print("Opción non válida")


if __name__ == "__main__":
    menu_principal()