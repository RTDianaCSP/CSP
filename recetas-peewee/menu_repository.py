from models import MenuSemanalModel, MenuPlato, PlatoModel


def crear_menu(menu):

    m = MenuSemanalModel.create(
        semana=menu.semana,
        ano=menu.ano
    )

    for plato in menu.getPlatos():

        p = PlatoModel.get_or_none(PlatoModel.nome == plato.nome)

        if p:
            MenuPlato.create(
                menu=m,
                plato=p
            )


def listar_menus():

    return MenuSemanalModel.select()