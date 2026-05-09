from database import db
from models import PlatoModel, IngredienteModel, MenuSemanalModel, MenuPlato

def crear_tablas():

    db.connect()

    db.create_tables([
        PlatoModel,
        IngredienteModel,
        MenuSemanalModel,
        MenuPlato
    ])

    db.close()


if __name__ == "__main__":
    crear_tablas()