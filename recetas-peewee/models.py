from peewee import *
from database import db

class BaseModel(Model):
    class Meta:
        database = db


class PlatoModel(BaseModel):

    nome = CharField(unique=True)
    tipo = CharField()
    data = CharField()
    tempada = CharField()
    preparacion = TextField()
    foto = CharField()


class IngredienteModel(BaseModel):

    nome = CharField()
    cantidade = CharField()
    plato = ForeignKeyField(PlatoModel, backref="ingredientes")


class MenuSemanalModel(BaseModel):

    semana = IntegerField()
    ano = IntegerField()


class MenuPlato(BaseModel):

    menu = ForeignKeyField(MenuSemanalModel)
    plato = ForeignKeyField(PlatoModel)