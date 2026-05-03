# Django – Aplicación de Menús Semanais

Aplicación web desenvolvida con Django para a xestión de receitas, ingredientes, pratos e planificación de menús semanais.

## Funcionalidades

- CRUD completo de:
  - Ingredientes
  - Pratos
  - Menús semanais

- Relacións:
  - Pratos ↔ Ingredientes (ManyToMany)
  - Menús ↔ Pratos (ManyToMany)

- Uso de herdanza de templates
- Panel de administración habilitado
- Uso de Django Forms
- Uso de tags e filters personalizados
- Subida de imaxes para os pratos

## Tecnoloxías

- Python 3
- Django
- SQLite

## Instalación

Clonar o repositorio:

```bash
git clone <URL_DO_REPO>
cd djangorecetas
```

Crear entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Base de datos

Aplicar migracións:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Crear superusuario

```bash
python manage.py createsuperuser
```

No meu caso: dianart

## Executar a aplicación

```bash
python manage.py runserver
```

Abrir no navegador:

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
