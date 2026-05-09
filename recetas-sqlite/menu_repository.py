from database import get_connection



def crear_menu(menu):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO menu_semanal (semana, ano)
        VALUES (%s, %s)
        """,
        (menu.semana, menu.ano)
    )

    menu_id = cursor.lastrowid

    for plato in menu.getPlatos():

        cursor.execute(
            "SELECT id FROM plato WHERE nome = %s",
            (plato.nome,)
        )

        plato_id = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO menu_plato (menu_id, plato_id)
            VALUES (%s, %s)
            """,
            (menu_id, plato_id)
        )

    conn.commit()
    conn.close()