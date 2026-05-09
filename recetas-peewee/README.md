# recetas-peewee

Versión do proxecto de receitas utilizando peewee.

## Instalación

Clonamos o repositorio:

```bash
git clone <url>
cd recetas-peewee

```

## Configuración

Creamos a contorna virtual, no meu caso coa terminal de Git Bash en Windows:

```bash
python -m venv venv
source venv/Scripts/activate

```

Instalamos a dependencia de peewee:

```bash
pip install -r requirements.txt

```

Creamos a base de datos e as táboas:

```bash
python crear_tablas.py

```

Executamos o proxecto:

```bash
python main.py

```
