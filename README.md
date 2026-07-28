# AI Drama System

AI Drama System is a production-oriented foundation for building AI-assisted drama pipelines around reusable assets, configurable workflows, and shot-based execution.

## Purpose

This repository is the starting point for a platform that will eventually support:

- story and episode planning
- scene and shot production
- reusable asset management
- prompt construction
- image, video, and audio generation
- quality control
- timeline assembly and export

The current milestone intentionally delivers only the initial Django foundation and the core Project → Story → Episode → Scene → Shot hierarchy.

## Architecture Principles

- **Model-agnostic:** domain logic must not depend on any single AI model or provider.
- **Workflow-driven:** generation pipelines will be configurable and versioned.
- **Asset-centric:** reusable production elements will live as persistent assets.
- **Shot-based:** shot is the primary production unit.
- **Reproducible:** future generated artifacts will retain full provenance.

## Current Implementation Status

This first implementation includes:

- Django project bootstrap under `backend/`
- environment-aware settings for local and future production use
- SQLite-by-default development setup with PostgreSQL-compatible configuration
- foundational UUID/timestamp abstract model support
- initial `Project`, `Story`, `Episode`, `Scene`, and `Shot` models
- Django admin registration
- Django REST Framework CRUD APIs for the initial hierarchy
- focused model and API tests
- initial architecture and ADR documentation in `docs/`

No external AI providers, workflow engines, vector databases, or media pipelines are implemented yet.

## Project Structure

```text
backend/
├── apps/
│   ├── production/
│   ├── projects/
│   └── stories/
├── common/
├── config/
├── providers/
├── services/
└── tests/
docs/
├── adr/
├── architecture/
├── development/
└── domain/
```

## Development Setup

1. Create a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables as needed:

   ```bash
   cp .env.example .env
   set -a
   source .env
   set +a
   ```

4. Run migrations:

   ```bash
   python backend/manage.py migrate
   ```

5. Start the development server:

   ```bash
   python backend/manage.py runserver
   ```

6. Run tests:

   ```bash
   python backend/manage.py test
   ```

## Roadmap

Planned future phases include:

- assets and asset versioning
- workflow definitions and versioning
- prompt instances and generation tasks
- provider adapters for LLM, image, video, and audio systems
- artifact tracking and provenance
- continuity, QC, and export domains
- knowledge retrieval and rule management

See `docs/architecture/initial-foundation.md` and the ADRs for the foundation decisions.
