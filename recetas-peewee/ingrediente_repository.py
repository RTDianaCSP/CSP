from models import IngredienteModel

class IngredienteRepository:

    def gardar(self, ingrediente, plato_id):

        IngredienteModel.create(
            nome=ingrediente.nome,
            cantidade=ingrediente.cantidade,
            plato=plato_id
        )