# recetas-sqlite

Versión do proxecto de receitas utilizando sqlite.

## Instalación

Clonamos o repositorio:

```bash
git clone <url>
cd recetas-sqlite

```

## Configuración

Creamos a contorna virtual, no meu caso coa terminal de Git Bash en Windows:

```bash
python -m venv venv
source venv/Scripts/activate

```

Non teremos que instalar nada.

Creamos a base de datos e as táboas:

```bash
python crear_tablas.py

```

Executamos o proxecto:

```bash
python main.py

```
