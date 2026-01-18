import unittest
from unittest.mock import patch

from app.funciones import (
    validar_talla,
    validar_cantidade,
    crear_pedido,
    modelo_ten_stock,
    buscar_cor,
    buscar_modelo,
    ver_dado_alta,
    obter_seguinte_id_pedido,
)

#Fanse probas daquelas funcións máis lóxicas

class TestValidacions(unittest.TestCase):
    """Probas das funcións de validación."""

    def test_talla_valida(self):
        self.assertTrue(validar_talla(40))

    def test_talla_invalida_menor(self):
        self.assertFalse(validar_talla(30))

    def test_talla_invalida_maior(self):
        self.assertFalse(validar_talla(60))

    def test_cantidade_valida(self):
        self.assertTrue(validar_cantidade(1))
        self.assertTrue(validar_cantidade(50))

    def test_cantidade_invalida(self):
        self.assertFalse(validar_cantidade(0))
        self.assertFalse(validar_cantidade(200))


class TestPedidos(unittest.TestCase):
    """Probas relacionadas cos pedidos."""

    def test_crear_pedido(self):
        pedido = crear_pedido(
            10,
            "Nike",
            "Air Zoom",
            "Negro",
            42,
            3
        )

        self.assertEqual(pedido["id"], 10)
        self.assertEqual(pedido["marca"], "Nike")
        self.assertEqual(pedido["modelo"], "Air Zoom")
        self.assertEqual(pedido["cor"], "Negro")
        self.assertEqual(pedido["talla"], 42)
        self.assertEqual(pedido["cantidad"], 3)
        self.assertEqual(pedido["dia_entrega"], "")

    @patch("app.funciones.cargar")
    def test_obter_seguinte_id_con_pedidos(self, mock_cargar):
        mock_cargar.return_value = {
            "categorias": [],
            "pedidos": [{"id": 1}, {"id": 4}, {"id": 7}]
        }

        self.assertEqual(obter_seguinte_id_pedido(), 8)

    @patch("app.funciones.cargar")
    def test_obter_seguinte_id_sen_pedidos(self, mock_cargar):
        mock_cargar.return_value = {
            "categorias": [],
            "pedidos": []
        }

        self.assertEqual(obter_seguinte_id_pedido(), 1)


class TestInventario(unittest.TestCase):
    """Probas da lóxica de inventario."""

    def test_modelo_ten_stock_true(self):
        modelo = {
            "cores": [
                {"cor": "Negro", "tallas": [40]},
                {"cor": "Branco", "tallas": []},
            ]
        }
        self.assertTrue(modelo_ten_stock(modelo))

    def test_modelo_ten_stock_false(self):
        modelo = {
            "cores": [
                {"cor": "Negro", "tallas": []},
                {"cor": "Branco", "tallas": []},
            ]
        }
        self.assertFalse(modelo_ten_stock(modelo))

    def test_buscar_cor_existe(self):
        modelo = {
            "cores": [
                {"cor": "Negro", "tallas": []},
                {"cor": "Azul", "tallas": []},
            ]
        }

        cor = buscar_cor(modelo, "Azul")
        self.assertIsNotNone(cor)
        self.assertEqual(cor["cor"], "Azul")

    def test_buscar_cor_non_existe(self):
        modelo = {"cores": [{"cor": "Negro", "tallas": []}]}
        self.assertIsNone(buscar_cor(modelo, "Vermello"))


class TestBusquedaModelos(unittest.TestCase):
    """Probas de búsqueda de modelos."""

    @patch("app.funciones.cargar")
    def test_buscar_modelo_existe(self, mock_cargar):
        mock_cargar.return_value = {
            "categorias": [
                {
                    "modelos": [
                        {"modelo": "Air Zoom"},
                        {"modelo": "Pegasus"},
                    ]
                }
            ]
        }

        modelo = buscar_modelo("Pegasus")
        self.assertIsNotNone(modelo)

    @patch("app.funciones.cargar")
    def test_buscar_modelo_non_existe(self, mock_cargar):
        mock_cargar.return_value = {"categorias": []}
        self.assertIsNone(buscar_modelo("Inexistente"))

    @patch("app.funciones.cargar")
    def test_ver_dado_alta(self, mock_cargar):
        mock_cargar.return_value = {
            "categorias": [
                {"modelos": [{"modelo": "Air Zoom"}]}
            ]
        }

        self.assertTrue(ver_dado_alta("Air Zoom"))
        self.assertFalse(ver_dado_alta("Outro"))
