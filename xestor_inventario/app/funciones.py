from __future__ import annotations

import json
from datetime import date
from collections import Counter
from typing import Dict, List, Optional, Any


RUTA_DATOS: str = "data/datos.json"


# ======================================================
#                     JSON
# ======================================================

def cargar() -> Dict[str, Any]:
    """
    Carga os datos do ficheiro JSON principal.

    Returns:
        Dict[str, Any]: Estrutura cos campos:
            - categorias
            - pedidos

        Se o ficheiro non existe ou está corrupto,
        devólvese unha estrutura baleira válida.
    """
    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"categorias": [], "pedidos": []}


def gardar(datos: Dict[str, Any]) -> None:
    """
    Garda os datos no ficheiro JSON.

    Args:
        datos (Dict[str, Any]): Datos completos.
    """
    with open(RUTA_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


# ======================================================
#                 FUNCIÓNS AUXILIARES
# ======================================================

def buscar_modelo(nome_modelo: str) -> Optional[Dict[str, Any]]:
    """
    Busca un modelo de zapatillas polo seu nome, sen distinguir entre
    maiúsculas e minúsculas, dentro de todas as categorías dispoñibles.

    Args:
        nome_modelo (str): Nome do modelo a buscar.

    Returns:
        Optional[Dict[str, Any]]:
            - Diccionario co modelo atopado se existe.
            - None se non se atopa ningún modelo con ese nome.
    """
    datos = cargar()

    for categoria in datos["categorias"]:
        for modelo in categoria["modelos"]:
            if modelo["modelo"].lower() == nome_modelo.lower():
                return modelo

    return None


def buscar_modelo_con_categoria(nome_modelo: str) -> Optional[tuple[Dict[str, Any], Dict[str, Any]]]:
    """
    Busca un modelo polo seu nome (sen distinguir maiúsculas/minúsculas)
    e devolve tanto o modelo como a categoría á que pertence.

    Args:
        nome_modelo (str): Nome do modelo a buscar.

    Returns:
        Optional[Tuple[Dict[str, Any], Dict[str, Any]]]:
            - (categoria, modelo) se o modelo existe.
            - None se non se atopa ningún modelo con ese nome.
    """
    datos = cargar()

    for categoria in datos["categorias"]:
        for modelo in categoria["modelos"]:
            if modelo["modelo"].lower() == nome_modelo.lower():
                return categoria, modelo

    return None


def buscar_cor(modelo: Dict[str, Any], cor: str) -> Optional[Dict[str, Any]]:
    """
    Busca unha cor dentro dun modelo.

    Args:
        modelo (dict): Modelo onde buscar.
        cor (str): Nome da cor.

    Returns:
        Optional[dict]: Cor atopada ou None.
    """
    for c in modelo.get("cores", []):
        if c["cor"].lower() == cor.lower():
            return c
    return None


# ======================================================
#                   VALIDACIÓNS
# ======================================================

def validar_talla(talla: int) -> bool:
    """Verifica se a talla está entre 33 e 50."""
    return 33 <= talla <= 50


def validar_cantidade(cantidade: int) -> bool:
    """Verifica se a cantidade está entre 1 e 100."""
    return 1 <= cantidade <= 100


def obter_data_hoxe() -> str:
    """Devolve a data actual en formato DD-MM-YYYY."""
    return date.today().strftime("%d-%m-%Y")


# ======================================================
#                   INVENTARIO
# ======================================================

def obter_todos_modelos() -> List[Dict[str, Any]]:
    """
    Obtén todos os modelos do sistema nunha lista,
    engadindo o deporte correspondente no diccionario de cada modelo.
    """
    datos = cargar()
    resultado: List[Dict[str, Any]] = []

    for categoria in datos["categorias"]:
        for modelo in categoria["modelos"]:
            copia = modelo.copy()
            copia["deporte"] = categoria["deporte"]
            resultado.append(copia)

    return resultado


def ver_dado_alta(nome_modelo: str) -> bool:
    """Comproba se un modelo xa existe."""
    return buscar_modelo(nome_modelo) is not None


def obter_deportes() -> List[str]:
    """Devolve a lista de deportes rexistrados."""
    return [c["deporte"] for c in cargar()["categorias"]]


def obter_caracteristicas_inserir(deporte: str) -> List[str]:
    """
    Obtén a lista das características que debe ter un modelo
    dun deporte determinado.
    """
    for categoria in cargar()["categorias"]:
        if categoria["deporte"].lower() == deporte.lower():
            if categoria["modelos"]:
                return list(categoria["modelos"][0]["caracteristicas"].keys())
    return []


def introducir_modelo(
    modelo: str,
    marca: str,
    deporte: str,
    caracteristicas: List[str],
    valores_caracteristicas: List[str],
    cores: List[str]
) -> None:
    """
    Engade un novo modelo ao inventario.

    Args:
        modelo (str): Nome do modelo.
        marca (str): Marca do modelo.
        deporte (str): Deporte ao que pertence (Running, Fútbol, etc.).
        caracteristicas (List[str]): Lista cos nomes das características.
        valores_caracteristicas (List[str]): Lista cos valores correspondentes ás características.
        cores (List[str]): Lista de cores dispoñibles para o modelo.
    """
    datos = cargar()

    novo_modelo = {
        "marca": marca,
        "modelo": modelo,
        "ventas": 0,
        "caracteristicas": dict(zip(caracteristicas, valores_caracteristicas)),
        "cores": [{"cor": c, "tallas": []} for c in cores]
    }

    for categoria in datos["categorias"]:
        if categoria["deporte"] == deporte:
            categoria["modelos"].append(novo_modelo)
            gardar(datos)
            return


def obter_modelo(nome_modelo: str) -> Optional[Dict[str, Any]]:
    """Obtén un modelo polo seu nome.
     Returns:
        Optional[Dict[str, Any]]:
            - Diccionario co modelo atopado se existe.
            - None se non se atopa ningún modelo con ese nome.
    """
    return buscar_modelo(nome_modelo)


def modelo_ten_stock(modelo: Dict[str, Any]) -> bool:
    """
    Indica se un modelo ten algunha talla dispoñible.

    Args:
        modelo (Dict[str, Any]): Dicionario que representa un modelo.
    """
    return any(c["tallas"] for c in modelo["cores"])


def dar_baixa_modelo(nome_modelo: str) -> bool:
    """
    Elimina un modelo do inventario se:
        - non ten stock
        - non é o único da categoría
    Returns:
        -True se se consegue dar de baixa
        -False se non se consegue
    """
    datos = cargar()

    for categoria in datos["categorias"]:
        modelos = categoria["modelos"]

        for modelo in modelos:
            if modelo["modelo"].lower() == nome_modelo.lower():
                if modelo_ten_stock(modelo) or len(modelos) <= 1:
                    return False

                modelos.remove(modelo)
                gardar(datos)
                return True

    return False


# ======================================================
#                  CORES / TALLAS
# ======================================================

def cor_existe_en_modelo(modelo_nome: str, cor: str) -> List[bool]:
    """
    Comproba se un modelo existe e se unha cor existe nel.

    Returns:
        [modelo_existe, cor_existe]
    """
    modelo = buscar_modelo(modelo_nome)
    if not modelo:
        return [False, False]

    existe = any(c["cor"].lower() == cor.lower() for c in modelo["cores"])
    return [True, existe]


def engadir_cor_a_modelo(modelo_nome: str, cor: str) -> None:
    """Engade unha nova cor a un modelo."""
    datos = cargar()

    for categoria in datos["categorias"]:
        for modelo in categoria["modelos"]:
            if modelo["modelo"].lower() == modelo_nome.lower():
                modelo["cores"].append({"cor": cor, "tallas": []})
                gardar(datos)
                return


def listar_cores_modelo_stock(nome_modelo: str) -> Optional[List[Dict[str, bool]]]:
    """
    Lista as cores dun modelo indicando se teñen stock.

    Returns:
        Optional[List[Dict[str, bool]]]:
            Lista de dicionarios co formato:
                {
                    "cor": str,
                    "ten_stock": bool
                }
            ou None se o modelo non existe.
    """
    modelo = buscar_modelo(nome_modelo)
    if not modelo:
        return None

    return [
        {"cor": c["cor"], "ten_stock": bool(c["tallas"])}
        for c in modelo["cores"]
    ]


def dar_baixa_cor(modelo_nome: str, cor: str) -> bool:
    """Elimina unha cor sen stock."""
    datos = cargar()

    for categoria in datos["categorias"]:
        for modelo in categoria["modelos"]:
            if modelo["modelo"].lower() == modelo_nome.lower():
                cor_obj = buscar_cor(modelo, cor)
                if not cor_obj or cor_obj["tallas"]:
                    return False

                modelo["cores"].remove(cor_obj)
                gardar(datos)
                return True

    return False


def vender_talla(modelo_nome: str, cor: str, talla: int) -> bool:
    """
    Rexistra unha venda dunha talla concreta.
    """
    datos = cargar()

    for categoria in datos["categorias"]:
        for modelo in categoria["modelos"]:
            if modelo["modelo"].lower() == modelo_nome.lower():
                cor_obj = buscar_cor(modelo, cor)

                if not cor_obj or talla not in cor_obj["tallas"]:
                    return False

                cor_obj["tallas"].remove(talla)
                modelo["ventas"] += 1
                gardar(datos)
                return True

    return False


# ======================================================
#                     PEDIDOS
# ======================================================

def obter_pedidos_pendentes() -> List[Dict[str, Any]]:
    """
    Obtén os pedidos aínda non entregados.
    Args:
        Lista con diccionarios que representa o contido do json
    
    """
    return [p for p in cargar()["pedidos"] if p["dia_entrega"] == ""]


def obter_seguinte_id_pedido() -> int:
    """Calcula e devolve o seguinte ID dispoñible para un pedido."""
    datos = cargar()
    return max((p["id"] for p in datos["pedidos"]), default=0) + 1


def crear_pedido(
    id_: int,
    marca: str,
    modelo: str,
    cor: str,
    talla: int,
    cant: int
) -> Dict[str, Any]:
    """
    Crea un novo pedido para o inventario.

    Args:
        id_ (int): ID único do pedido.
        marca (str): Marca do modelo solicitado.
        modelo (str): Nome do modelo solicitado.
        cor (str): Cor do modelo.
        talla (int): Talla da zapatilla.
        cant (int): Cantidade de unidades solicitadas.

    Returns:
        Dict[str, Any]: Dicionario representando o pedido, co formato:
            {
                "id": int,
                "marca": str,
                "modelo": str,
                "cor": str,
                "talla": int,
                "cantidad": int,
                "dia": str,       
                "dia_entrega": str   
            }
    """
    return {
        "id": id_,
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "talla": talla,
        "cantidad": cant,
        "dia": obter_data_hoxe(),
        "dia_entrega": ""
    }



def engadir_pedido(pedido: Dict[str, Any]) -> None:
    """
    Engade un pedido ao sistema.

    Args:
         Dict[str, Any]: Dicionario representando o pedido, co formato:
            {
                "id": int,
                "marca": str,
                "modelo": str,
                "cor": str,
                "talla": int,
                "cantidad": int,
                "dia": str,       
                "dia_entrega": str   
            }
    
    """
    datos = cargar()
    datos["pedidos"].append(pedido)
    gardar(datos)


def marcar_pedido_entregado(pedido_id: int) -> bool:
    """
    Marca un pedido como entregado e actualiza stock.
    """
    datos = cargar()

    for pedido in datos["pedidos"]:
        if pedido["id"] == pedido_id and pedido["dia_entrega"] == "":
            pedido["dia_entrega"] = obter_data_hoxe()

            for categoria in datos["categorias"]:
                for modelo in categoria["modelos"]:
                    if (
                        modelo["marca"].lower() == pedido["marca"].lower()
                        and modelo["modelo"].lower() == pedido["modelo"].lower()
                    ):
                        cor_obj = buscar_cor(modelo, pedido["cor"])
                        if cor_obj:
                            cor_obj["tallas"].extend(
                                [pedido["talla"]] * pedido["cantidad"]
                            )

            gardar(datos)
            return True

    return False


def cancelar_pedido(pedido_id: int) -> bool:
    """Cancela un pedido pendente."""
    datos = cargar()

    for pedido in datos["pedidos"]:
        if pedido["id"] == pedido_id and pedido["dia_entrega"] == "":
            datos["pedidos"].remove(pedido)
            gardar(datos)
            return True

    return False


# ======================================================
#                     CONSULTAS
# ======================================================

def obter_modelos_mais_vendidos() -> List[Dict[str, Any]]:
    """
    Devolve os modelos ordenados por número de vendas.

    Returns:
        Lista cos diccionarios que representan un modelo cada un deles.
    
    """
    return sorted(
        obter_todos_modelos(),
        key=lambda m: m.get("ventas", 0),
        reverse=True
    )


def obter_dispoñibilidade_modelo(
    marca: str,
    modelo_nome: str
) -> Dict[str, Dict[int, int]]:
    """
    Obtén a dispoñibilidade de tallas por cor.

    Returns:
        Dict[str, Dict[int, int]]: Dicionario onde cada clave é unha cor
        do modelo, e o valor é outro dicionario que indica a cantidade
        dispoñible por talla. Exemplo:

        {
            "Negro": {38: 2, 39: 1, 40: 3},
            "Branco": {36: 1, 37: 2}
        }

        Se non se atopa o modelo ou a marca devolve un diccionario baleiro

    """
    for modelo in obter_todos_modelos():
        if (
            modelo["marca"].lower() == marca.lower()
            and modelo["modelo"].lower() == modelo_nome.lower()
        ):
            return {
                c["cor"]: dict(Counter(c["tallas"]))
                for c in modelo["cores"]
            }

    return {}
