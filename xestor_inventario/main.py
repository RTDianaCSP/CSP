from app.io import (
    cancelar_pedido_io,
    dar_baixa_cor_io,
    entregar_pedido_io,
    facer_pedido_io,
    mostrar_disponible_modelo,
    mostrar_menu,
    mostrar_produtos_inventario,
    mostrar_menu_inventario,
    mostrar_menu_pedidos,
    mostrar_mais_vendidos,
    dar_alta_modelo_io,
    mostrar_menu_modelo,
    dar_baixa_modelo_io,
    dar_alta_cor_io,
    mostrar_menu_cor,
    vender_talla_io,
    mostrar_pedidos_pendentes,
)


def menu_inventario() -> None:
    """
    Submenú de inventario.

    Permite al usuario:
    1. Ver todos os produtos dispoñibles no inventario.
    2. Consultar os modelos más vendidos.
    3. Consultar a dispoñibilidade dun modelo específico.
    4. Saír ao menú principal.
    """
    while True:
        mostrar_menu_inventario()
        opcion = input("Selecciona unha opción: ")

        match opcion:
            case "1":
                mostrar_produtos_inventario()
            case "2":
                mostrar_mais_vendidos()
            case "3":
                mostrar_disponible_modelo()
            case "4":
                break
            case _:
                print("Opción non válida. Inténtao de novo.")


def menu_modelos() -> None:
    """
    Submenú de modelos.

    Permite al usuario:
    1. Dar de alta un novo modelo no inventario.
    2. Dar de baixa un modelo existente do inventario
    3. Saír ao menú principal.
    """
    while True:
        mostrar_menu_modelo()
        opcion = input("Selecciona unha opción: ")

        match opcion:
            case "1":
                dar_alta_modelo_io()
            case "2":
                dar_baixa_modelo_io()
            case "3":
                break
            case _:
                print("Opción non válida. Inténtao de novo.")


def menu_cores() -> None:
    """
    Submenú de cores dos modelos

    Permite al usuario:
    1. Dar de alta unha nova cor nun modelo existente.
    2. Dar de baixa unhaa cor dun modelo.
    3. Saír ao menú principal.
    """
    while True:
        mostrar_menu_cor()
        opcion = input("Selecciona unha opción: ")

        match opcion:
            case "1":
                dar_alta_cor_io()
            case "2":
                dar_baixa_cor_io()
            case "3":
                break
            case _:
                print("Opción non válida. Inténtao de novo.")


def menu_pedidos() -> None:
    """
    Submenú de pedidos.

    Permite ao usuario:
    1. Mostrar os pedidos pendentes.
    2. Crear un novo pedido.
    3. Marcar un pedido como entregado.
    4. Cancelar un pedido pendente.
    5. Saír ao menú principal.
    """
    while True:
        mostrar_menu_pedidos()
        opcion = input("Selecciona unha opción: ")

        match opcion:
            case "1":
                mostrar_pedidos_pendentes()
            case "2":
                facer_pedido_io()
            case "3":
                entregar_pedido_io()
            case "4":
                cancelar_pedido_io()
            case "5":
                break
            case _:
                print("Opción non válida. Inténtao de novo.")


def main() -> None:
    """
    Menú principal da aplicación.

    Permite al usuario:
    1. Acceder ao submenú de inventario.
    2. Acceder ao submenú de modelos.
    3. Acceder ao submenú de cores
    4. Vender unha talla dunha zapatilla
    5. Acceder al submenú de pedidos.
    6. Saír do programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Selecciona unha opción: ")

        match opcion:
            case "1":
                menu_inventario()
            case "2":
                menu_modelos()
            case "3":
                menu_cores()
            case "4":
                vender_talla_io()
            case "5":
                menu_pedidos()
            case "6":
                print("Saíndo do programa. Ata logo!")
                break
            case _:
                print("Opción non válida. Inténtao de novo.")


if __name__ == "__main__":
    main()
