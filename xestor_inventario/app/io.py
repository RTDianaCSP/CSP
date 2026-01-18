from typing import List, Tuple
from colorama import Fore, Style, init

from app.funciones import (
    # Inventario
    obter_todos_modelos,
    obter_modelos_mais_vendidos,
    obter_dispoñibilidade_modelo,
    obter_deportes,
    obter_caracteristicas_inserir,
    introducir_modelo,
    vender_talla,
    ver_dado_alta,
    obter_modelo,
    dar_baixa_modelo,
    # Cores / tallas
    cor_existe_en_modelo,
    engadir_cor_a_modelo,
    dar_baixa_cor,
    listar_cores_modelo_stock,
    # Pedidos
    obter_pedidos_pendentes,
    obter_seguinte_id_pedido,
    crear_pedido,
    engadir_pedido,
    marcar_pedido_entregado,
    cancelar_pedido,
    # Validacións
    validar_talla,
    validar_cantidade,
)

init(autoreset=True)


# ======================================================
#                 FUNCIÓNS AUXILIARES
# ======================================================

def seleccionar_opcion_numerica(max_opcion: int, mensaxe: str) -> int:
    """
    Solicita ao usuario unha opción numérica segura.

    Args:
        max_opcion (int): Número máximo permitido.
        mensaxe (str): Mensaxe a mostrar.

    Returns:
        int: Opción válida escollida (1..max_opcion).
    """
    while True:
        try:
            opcion = int(input(mensaxe))
            if 1 <= opcion <= max_opcion:
                return opcion
            print(Fore.RED + "❌ Número fóra de rango")
        except ValueError:
            print(Fore.RED + "❌ Entrada incorrecta. Introduce un número válido.")


def mostrar_lista_modelos(modelos: List[Tuple[str, str]]) -> None:
    """
    Mostra unha lista numerada de modelos.

    Args:
        modelos nunha lista (marca, modelo).
    """
    for i, (marca, modelo) in enumerate(modelos, start=1):
        print(f"{i}. {marca} - {modelo}")


# ======================================================
#                        MENÚS
# ======================================================

def mostrar_menu() -> None:
    """Amosa o menú principal."""
    print(Style.BRIGHT + Fore.CYAN + "\n*** XESTOR DE INVENTARIO - TENDA DE ZAPATILLAS ***")
    print("1. Ver inventario")
    print("2. Dar de alta/baixa modelo")
    print("3. Dar de alta/baixa cor")
    print("4. Vender talla")
    print("5. Pedidos")
    print("6. Saír")


def mostrar_menu_inventario() -> None:
    """Amosa o submenú de inventario."""
    print("1. Ver todas as zapatillas")
    print("2. Ver máis vendidas")
    print("3. Ver dispoñibilidade dun modelo")
    print("4. Atrás")


def mostrar_menu_modelo() -> None:
    """Amosa o submenú de modelos."""
    print("1. Dar alta modelo")
    print("2. Dar baixa modelo")
    print("3. Atrás")


def mostrar_menu_cor() -> None:
    """Amosa o submenú de cores."""
    print("1. Dar alta nova cor")
    print("2. Dar baixa cor")
    print("3. Atrás")


def mostrar_menu_pedidos() -> None:
    """Amosa o submenú de pedidos."""
    print("1. Ver pedidos pendentes")
    print("2. Facer pedido")
    print("3. Marcar pedido como recibido")
    print("4. Cancelar pedido")
    print("5. Atrás")


# ======================================================
#                     INVENTARIO
# ======================================================

def mostrar_produtos_inventario() -> None:
    """
    Mostra todo o inventario agrupado por deporte.
    """
    modelos = obter_todos_modelos()

    if not modelos:
        print(Fore.YELLOW + "Non hai produtos no inventario")
        return

    categorias = {}
    for m in modelos:
        categorias.setdefault(m["deporte"], []).append(m)

    for deporte, lista in categorias.items():
        print(Style.BRIGHT + Fore.CYAN + f"\n{deporte.upper()}")

        for m in lista:
            dispo = any(c["tallas"] for c in m["cores"])
            cor = Fore.GREEN if dispo else Fore.RED
            icon = "✔" if dispo else "✖"

            print(
                cor +
                f"  {icon} {m['marca']} - {m['modelo']} (Vendas: {m.get('ventas', 0)})"
            )


def mostrar_mais_vendidos() -> None:
    """
    Mostra os modelos máis vendidos.
    """
    modelos = obter_modelos_mais_vendidos()

    print(Fore.CYAN + "\n📈 MODELOS MÁIS VENDIDOS\n")

    for i, m in enumerate(modelos, start=1):
        dispo = any(c["tallas"] for c in m["cores"])
        cor = Fore.GREEN if dispo else Fore.RED

        print(
            cor +
            f"{i}. {m['marca']} - {m['modelo']} | {m['deporte']} | Vendas: {m.get('ventas', 0)}"
        )


def mostrar_disponible_modelo() -> None:
    """
    Mostra a dispoñibilidade de tallas dun modelo.
    """
    modelos = obter_todos_modelos()
    lista = [(m["marca"], m["modelo"]) for m in modelos]

    mostrar_lista_modelos(lista)

    op = seleccionar_opcion_numerica(len(lista), "\nEscolla o modelo: ")
    marca_sel, modelo_sel = lista[op - 1]

    dispo = obter_dispoñibilidade_modelo(marca_sel, modelo_sel)

    if not dispo:
        print(Fore.RED + "❌ Modelo non atopado")
        return

    print(Style.BRIGHT + Fore.CYAN + f"\n{marca_sel} {modelo_sel}")

    for cor, tallas in dispo.items():
        print(Fore.YELLOW + f"- {cor}")
        if not tallas:
            print("   Sen stock")
        else:
            for t, c in tallas.items():
                print(f"   Talla {t}: {c}")


# ======================================================
#                        MODELOS
# ======================================================

def dar_alta_modelo_io() -> None:
    """
    Interface para dar de alta un novo modelo.
    """
    while True:
        modelo = input("Modelo: ").strip()
        if 2 <= len(modelo) <= 100:
            break
        print(Fore.RED + "❌ O nome do modelo debe ter entre 2 e 100 caracteres")

    if ver_dado_alta(modelo):
        print(Fore.RED + "❌ O modelo xa existe")
        return

    while True:
        marca = input("Marca: ").strip()
        if 2 <= len(marca) <= 100:
            break
        print(Fore.RED + "❌ O nome da marca debe ter entre 2 e 100 caracteres")

    deportes = obter_deportes()
    for i, d in enumerate(deportes, start=1):
        print(f"{i}. {d}")

    op = seleccionar_opcion_numerica(len(deportes), "Categoría: ")
    deporte = deportes[op - 1]

    caracs = obter_caracteristicas_inserir(deporte)
    valores: List[str] = []

    for c in caracs:
        while True:
            valor = input(f"{c}: ").strip()
            if c.lower() == "peso":
                try:
                    float(valor)
                    valores.append(valor)
                    break
                except ValueError:
                    print(Fore.RED + "❌ O peso debe ser numérico")
            else:
                if 2 <= len(valor) <= 100:
                    valores.append(valor)
                    break
                print(Fore.RED + "❌ Valor incorrecto")

    try:
        n = int(input("Número de cores (1-5): "))
        n = max(1, min(5, n))
    except ValueError:
        n = 1

    cores = [input(f"Cor {i + 1}: ") for i in range(n)]

    introducir_modelo(modelo, marca, deporte, caracs, valores, cores)
    print(Fore.GREEN + "✅ Modelo dado de alta")


def dar_baixa_modelo_io() -> None:
    """
    Interface para dar de baixa un modelo.
    """
    modelos = obter_todos_modelos()
    lista = [(m["marca"], m["modelo"]) for m in modelos]

    mostrar_lista_modelos(lista)

    op = seleccionar_opcion_numerica(len(lista), "\nModelo a eliminar: ")
    marca_sel, modelo_sel = lista[op - 1]

    pedidos = obter_pedidos_pendentes()
    for p in pedidos:
        if p["marca"].lower() == marca_sel.lower() and p["modelo"].lower() == modelo_sel.lower():
            print(Fore.RED + "❌ Non se pode eliminar: ten pedidos pendentes")
            return

    if dar_baixa_modelo(modelo_sel):
        print(Fore.GREEN + f"✅ Modelo '{modelo_sel}' eliminado")
    else:
        print(Fore.RED + "❌ Non se pode eliminar o modelo")


# ======================================================
#                         CORES
# ======================================================

def dar_alta_cor_io() -> None:
    """
    Interface para engadir unha nova cor a un modelo.
    """
    modelos = obter_todos_modelos()
    lista = [(m["marca"], m["modelo"]) for m in modelos]

    mostrar_lista_modelos(lista)

    op = seleccionar_opcion_numerica(len(lista), "\nModelo: ")
    _, modelo_sel = lista[op - 1]

    cor = input("Nova cor: ").strip()

    modelo_ok, cor_ok = cor_existe_en_modelo(modelo_sel, cor)

    if not modelo_ok:
        print(Fore.RED + "❌ O modelo non existe")
        return

    if cor_ok:
        print(Fore.RED + "❌ Esa cor xa existe")
        return

    engadir_cor_a_modelo(modelo_sel, cor)
    print(Fore.GREEN + "✅ Cor engadida")


def dar_baixa_cor_io() -> None:
    """
    Interface para eliminar unha cor dun modelo.

    Non se permite eliminar unha cor se:
        - ten stock
        - é a única cor do modelo
        - existen pedidos pendentes desa cor
    """
    modelos = obter_todos_modelos()
    lista = [(m["marca"], m["modelo"]) for m in modelos]

    mostrar_lista_modelos(lista)
    op = seleccionar_opcion_numerica(len(lista), "\nModelo: ")
    marca_sel, modelo_sel = lista[op - 1]

    cores_stock = listar_cores_modelo_stock(modelo_sel)
    if not cores_stock:
        print(Fore.RED + "❌ Modelo non válido")
        return

    if len(cores_stock) == 1:
        print(Fore.RED + "❌ O modelo debe ter máis dunha cor")
        return

    print("\nCores dispoñibles:")
    for i, c in enumerate(cores_stock, start=1):
        estado = "✔" if c["ten_stock"] else "Sen"
        print(f"{i}. {c['cor']} ({estado})")

    op_cor = seleccionar_opcion_numerica(len(cores_stock), "Cor a eliminar: ")
    cor_sel = cores_stock[op_cor - 1]["cor"]

    if cores_stock[op_cor - 1]["ten_stock"]:
        print(Fore.RED + "❌ A cor ten stock")
        return

    pedidos = obter_pedidos_pendentes()
    for p in pedidos:
        if (
            p["modelo"].lower() == modelo_sel.lower()
            and p["cor"].lower() == cor_sel.lower()
        ):
            print(
                Fore.RED +
                f"❌ Non se pode eliminar a cor '{cor_sel}': existen pedidos pendentes"
            )
            return

    if dar_baixa_cor(modelo_sel, cor_sel):
        print(Fore.GREEN + f"✅ Cor '{cor_sel}' eliminada")
    else:
        print(Fore.RED + "❌ Non se puido eliminar a cor")



# ======================================================
#                       VENDAS
# ======================================================

def vender_talla_io() -> None:
    """
    Interface para vender unha talla.
    """
    modelos = obter_todos_modelos()
    lista = [(m["marca"], m["modelo"]) for m in modelos]

    mostrar_lista_modelos(lista)
    op = seleccionar_opcion_numerica(len(lista), "\nModelo: ")
    _, modelo_sel = lista[op - 1]

    modelo = obter_modelo(modelo_sel)
    if not modelo:
        print(Fore.RED + "❌ Modelo non atopado")
        return

    cores = modelo["cores"]
    print("\nCores:")
    for i, c in enumerate(cores, start=1):
        estado = "✔" if c["tallas"] else "Sen"
        print(f"{i}. {c['cor']} ({estado})")

    op_cor = seleccionar_opcion_numerica(len(cores), "Cor: ")
    cor_sel = cores[op_cor - 1]

    if not cor_sel["tallas"]:
        print(Fore.RED + "❌ Esa cor non ten stock")
        return

    tallas_dispo = sorted(set(cor_sel["tallas"]))
    print("\nTallas dispoñibles:", tallas_dispo)

    try:
        talla = int(input("Talla a vender: "))
    except ValueError:
        print(Fore.RED + "❌ Talla incorrecta")
        return

    if vender_talla(modelo_sel, cor_sel["cor"], talla):
        print(Fore.GREEN + "✅ Venda rexistrada")
    else:
        print(Fore.RED + "❌ Non hai stock desa talla")


# ======================================================
#                       PEDIDOS
# ======================================================

def mostrar_pedidos_pendentes() -> None:
    """Mostra todos os pedidos pendentes."""
    pedidos = obter_pedidos_pendentes()

    if not pedidos:
        print(Fore.GREEN + "✅ Non hai pedidos pendentes")
        return

    for p in pedidos:
        print(
            f"ID {p['id']} | {p['marca']} {p['modelo']} | "
            f"{p['cor']} | Talla {p['talla']} | Cantidade {p['cantidad']}"
        )


def facer_pedido_io() -> None:
    """
    Interface para crear un novo pedido.
    """
    modelos = obter_todos_modelos()
    lista = [(m["marca"], m["modelo"]) for m in modelos]

    mostrar_lista_modelos(lista)
    op = seleccionar_opcion_numerica(len(lista), "\nModelo: ")
    marca_sel, modelo_sel = lista[op - 1]

    modelo = obter_modelo(modelo_sel)
    if not modelo:
        print(Fore.RED + "❌ Modelo non atopado")
        return

    print("\nCores dispoñibles:")
    for i, c in enumerate(modelo["cores"], start=1):
        print(f"{i}. {c['cor']}")

    op_cor = seleccionar_opcion_numerica(len(modelo["cores"]), "Cor: ")
    cor_sel = modelo["cores"][op_cor - 1]["cor"]

    try:
        talla = int(input("Talla (33-50): "))
        cant = int(input("Cantidade (1-100): "))
    except ValueError:
        print(Fore.RED + "❌ Datos incorrectos")
        return

    if not validar_talla(talla) or not validar_cantidade(cant):
        print(Fore.RED + "❌ Valores fóra de rango")
        return

    pid = obter_seguinte_id_pedido()
    pedido = crear_pedido(pid, marca_sel, modelo_sel, cor_sel, talla, cant)
    engadir_pedido(pedido)

    print(Fore.GREEN + f"✅ Pedido {pid} creado")


def entregar_pedido_io() -> None:
    """
    Interface para marcar un pedido como entregado.
    """
    pedidos = obter_pedidos_pendentes()

    if not pedidos:
        print(Fore.YELLOW + "Non hai pedidos pendentes")
        return

    ids = [p["id"] for p in pedidos]
    for p in pedidos:
        print(f"ID {p['id']} | {p['marca']} {p['modelo']} | {p['cor']}")

    while True:
        try:
            pid = int(input("ID do pedido: "))
            if pid in ids:
                break
            print(Fore.RED + "❌ ID non válido")
        except ValueError:
            print(Fore.RED + "❌ Entrada incorrecta")

    if marcar_pedido_entregado(pid):
        print(Fore.GREEN + "✅ Pedido entregado")
    else:
        print(Fore.RED + "❌ Non se puido marcar como entregado")


def cancelar_pedido_io() -> None:
    """
    Interface para cancelar un pedido pendente.
    """
    pedidos = obter_pedidos_pendentes()

    if not pedidos:
        print(Fore.YELLOW + "Non hai pedidos pendentes")
        return

    ids = [p["id"] for p in pedidos]
    for p in pedidos:
        print(f"ID {p['id']} | {p['marca']} {p['modelo']}")

    while True:
        try:
            pid = int(input("ID do pedido a cancelar: "))
            if pid in ids:
                break
            print(Fore.RED + "❌ ID non válido")
        except ValueError:
            print(Fore.RED + "❌ Entrada incorrecta")

    if cancelar_pedido(pid):
        print(Fore.GREEN + "✅ Pedido cancelado")
    else:
        print(Fore.RED + "❌ Non se puido cancelar")
