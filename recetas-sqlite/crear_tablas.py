from database import get_connection

def crear_tablas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plato(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE,
        tipo TEXT,
        data TEXT,
        tempada TEXT,
        preparacion TEXT,
        foto TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingrediente(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cantidade TEXT,
        plato_id INTEGER,
        FOREIGN KEY(plato_id) REFERENCES plato(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu_semanal(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        semana INTEGER,
        ano INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu_platos(
        menu_id INTEGER,
        plato_id INTEGER,
        FOREIGN KEY(menu_id) REFERENCES menu_semanal(id),
        FOREIGN KEY(plato_id) REFERENCES plato(id)
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    crear_tablas()