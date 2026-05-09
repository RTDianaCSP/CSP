from database import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS plato (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) UNIQUE,
    tipo VARCHAR(50),
    data VARCHAR(50),
    tempada VARCHAR(50),
    preparacion TEXT,
    foto VARCHAR(255)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingrediente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cantidade VARCHAR(100),
    plato_id INT,
    FOREIGN KEY (plato_id) REFERENCES plato(id)
    ON DELETE CASCADE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_semanal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    semana INT,
    ano INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_plato (
    menu_id INT,
    plato_id INT,
    PRIMARY KEY(menu_id, plato_id),
    FOREIGN KEY (menu_id) REFERENCES menu_semanal(id)
    ON DELETE CASCADE,
    FOREIGN KEY (plato_id) REFERENCES plato(id)
    ON DELETE CASCADE
)
""")

conn.commit()
conn.close()

print("Táboas creadas correctamente")