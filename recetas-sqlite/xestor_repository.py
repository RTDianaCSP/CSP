from database import get_connection



def listar_menus():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT semana, ano FROM menu_semanal"
    )

    datos = cursor.fetchall()

    conn.close()

    return datos