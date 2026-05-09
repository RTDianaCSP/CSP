from database import get_connection


def crear_ingrediente(ingrediente, plato_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO ingrediente (nome, cantidade, plato_id)
        VALUES (%s, %s, %s)
        """,
        (
            ingrediente.nome,
            ingrediente.cantidade,
            plato_id
        )
    )

    conn.commit()
    conn.close()