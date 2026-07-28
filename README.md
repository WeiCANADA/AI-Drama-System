# AI-Drama-System
An AI-native drama production platform for story development, asset management, storyboard generation, image/video/audio workflows, continuity control, quality assurance, and final episode production.

## Development Bootstrap

Runtime baseline:

- Python 3.13
- Django 5.2 LTS
- PostgreSQL

Bootstrap steps:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Required environment variables are documented in `.env.example`:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

PostgreSQL must be available before running Django commands.

Baseline commands:

```bash
python manage.py check
python manage.py migrate
python manage.py test
python manage.py runserver
```
