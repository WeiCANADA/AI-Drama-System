# Development Setup

## Requirements

- Python 3.12+
- pip
- PostgreSQL optional for local development

## Quick Start

```bash
pip install -r requirements.txt
python backend/manage.py migrate
python backend/manage.py runserver
```

## Configuration

The default settings module is `config.settings.local`.

- SQLite is used by default for local development.
- You can load `.env.example` values into your shell with `set -a && source .env && set +a`.
- PostgreSQL can be enabled with `DATABASE_URL` or the `POSTGRES_*` variables in `.env.example`.
- Future production deployments should use `config.settings.production`.

## Test Command

```bash
python backend/manage.py test
```
