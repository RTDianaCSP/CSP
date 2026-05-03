from django.test import TestCase
from unittest.mock import patch
from datetime import date

from ..models import Ingrediente, Plato, MenuSemanal


class PlatoTest(TestCase):

    def setUp(self):
        self.ingrediente = Ingrediente.objects.create(
            nome="Patata",
            cantidade="2"
        )

        self.plato = Plato.objects.create(
            nome="Tortilla",
            tipo="Primer plato",
            data=date.today(),
            tempada="Todo el año",
            preparacion="Freír patatas y mezclar con huevo"
        )
        self.plato.ingredientes.add(self.ingrediente)

        self.menu = MenuSemanal.objects.create(
            semana=1,
            ano=2026
        )
        self.menu.platos.add(self.plato)


    # TEST 1

    def test_creacion_plato(self):
        """Comprueba que el plato se crea correctamente"""
        self.assertEqual(self.plato.nome, "Tortilla")
        self.assertEqual(self.plato.tipo, "Primer plato")


    # TEST 2 (MOCK)

    @patch("recetas.models.Plato.save")
    def test_mock_save_plato(self, mock_save):
        """
        Test usando Mock para evitar guardar en BD real.
        """
        plato = Plato(
            nome="Arroz",
            tipo="Segundo plato",
            data=date.today(),
            tempada="Verano",
            preparacion="Cocer arroz"
        )

        plato.save()

        mock_save.assert_called_once()


class MenuTest(TestCase):

    def setUp(self):
        self.menu = MenuSemanal.objects.create(
            semana=10,
            ano=2026
        )


    def test_menu_creado(self):
        """Comprueba creación de menú"""
        self.assertEqual(self.menu.semana, 10)
        self.assertEqual(self.menu.ano, 2026)