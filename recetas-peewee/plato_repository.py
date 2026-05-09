from models import PlatoModel, IngredienteModel
from erros import PlatoDuplicadoError


def crear_plato(plato):

    try:

        p = PlatoModel.create(
            nome=plato.nome,
            tipo=plato.tipo,
            data=plato.data,
            tempada=plato.tempada,
            preparacion=plato.preparacion,
            foto=plato.foto
        )

        for ing in plato.getIngredientes():

            IngredienteModel.create(
                nome=ing.nome,
                cantidade=ing.cantidade,
                plato=p
            )

    except Exception:

        raise PlatoDuplicadoError("O plato xa existe")


def obter_platos():

    return PlatoModel.select()