import pytest
from datetime import date
from recetas.models import Ingrediente, Plato, MenuSemanal


@pytest.mark.django_db
def test_crear_ingrediente():
    ingrediente = Ingrediente.objects.create(nome="Sal")
    assert ingrediente.nome == "Sal"
    assert Ingrediente.objects.count() == 1


@pytest.mark.django_db
def test_crear_plato():
    ingrediente = Ingrediente.objects.create(nome="Tomate")

    plato = Plato.objects.create(
        nome="Ensalada",
        data=date.today()   
    )

    plato.ingredientes.add(ingrediente)

    assert plato.nome == "Ensalada"
    assert ingrediente in plato.ingredientes.all()


@pytest.mark.django_db
def test_crear_menu_semanal():
    from datetime import date

    plato1 = Plato.objects.create(nome="Pasta", data=date.today())
    plato2 = Plato.objects.create(nome="Sopa", data=date.today())

    menu = MenuSemanal.objects.create(
        ano=2026,
        semana=18
    )

    menu.platos.add(plato1, plato2)

    assert menu.ano == 2026
    assert menu.semana == 18
    assert menu.platos.count() == 2
    assert plato1 in menu.platos.all()
    assert plato2 in menu.platos.all()