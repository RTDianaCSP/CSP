from database import get_connection
from erros import PlatoDuplicadoError
from ingrediente_repository import crear_ingrediente


def crear_plato(plato):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM plato WHERE nome = %s",
        (plato.nome,)
    )

    existe = cursor.fetchone()

    if existe:
        conn.close()
        raise PlatoDuplicadoError("O prato xa existe")

    cursor.execute(
        """
        INSERT INTO plato
        (nome, tipo, data, tempada, preparacion, foto)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            plato.nome,
            plato.tipo,
            plato.data,
            plato.tempada,
            plato.preparacion,
            plato.foto
        )
    )

    plato_id = cursor.lastrowid

    conn.commit()
    conn.close()

    for ingrediente in plato.getIngredientes():
        crear_ingrediente(ingrediente, plato_id)



def obter_platos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM plato")

    datos = cursor.fetchall()

    conn.close()

    return datos