# recetas-mariadb

Versión do proxecto de receitas utilizando MariaDB.

## Instalación

Clonamos o repositorio:

```bash
git clone <url>
cd recetas-mariadb

```

## Configuración

Creamos a contorna virtual, no meu caso coa terminal de Git Bash en Windows:

```bash
python -m venv venv
source venv/Scripts/activate

```

Instalamos a dependencia de mariadb:

```bash
pip install -r requirements.txt

```

Ademais habería que crear a base de datos coa consola de MariaDB(instalamola antes):

```sql
CREATE DATABASE recetas;

```

Creamos as táboas:

```bash
python crear_tablas.py

```

Executamos o proxecto:

```bash
python main.py

```
