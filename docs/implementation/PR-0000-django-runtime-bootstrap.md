# PR-0000 Django Runtime Bootstrap

## Status

- Status: Draft implementation plan
- Readiness: READY FOR PR-0000 IMPLEMENTATION
- Scope Type: Runtime/bootstrap engineering slice
- Scope Discipline:
  - no code in this document
  - no dependency installation in this document
  - no domain models in this document

## Purpose

Define the minimum runtime foundation required before PR-0001A so the
repository can support:

- a runnable Django project,
- dependency management,
- settings structure,
- database configuration,
- environment-variable handling,
- migration baseline,
- test baseline,
- repeatable development commands.

This bootstrap exists to establish engineering runtime prerequisites only.
It must not silently introduce planning-domain models, workflow/runtime
architecture, or provider integrations.

## Source Specifications

Primary repository evidence used for this plan:

- AGENTS.md
- README.md
- docs/DEVELOPMENT_SPEC.md
- docs/reviews/CORE_DOMAIN_READINESS_REVIEW_v1.md
- docs/reviews/CORE_DOMAIN_READINESS_DELTA_REVIEW_v1.md
- repository root contents
- .gitignore

Repository state relevant to bootstrap:

- current repository contains documentation only,
- no `manage.py` exists,
- no Django settings module exists,
- no Python dependency manifest exists,
- no Django apps/models/migrations/tests exist,
- `docs/development/` is not present,
- `.gitignore` already ignores `.env`, virtual environments, Django logs, and
  `db.sqlite3` as generic defaults.

## Scope

Included in PR-0000:

- Python runtime decision
- Django runtime version decision
- dependency-management decision
- minimal Django project skeleton decision
- settings and environment-variable contract
- database direction for local development and tests
- migration baseline plan
- minimum test baseline plan
- development command baseline
- git-secret handling baseline

## Explicitly Out of Scope

Explicitly excluded from PR-0000:

- Scene/Shot/Storyboard/StoryboardPanel models
- provider integrations
- Celery
- Redis
- DRF APIs
- frontend
- object storage
- AI providers
- Workflow/Generation/QC/Continuity models
- business/domain services
- domain migrations beyond Django bootstrap defaults

## Current Repository Assessment

Current repository root is documentation-first and contains no executable Django
runtime.

Bootstrap implication:

- PR-0001A cannot be implemented safely until a Django runtime baseline exists.
- PR-0000 should create only the engineering skeleton required to let later
  domain PRs add models and migrations without also inventing project
  conventions implicitly.

## Python Version

Repository-specified Python version:

- none found

Engineering decision status:

- explicit decision required in PR-0000

Recommendation:

- Python 3.13

Rationale:

- current repository has no contrary Python constraint,
- Python 3.13 remains a supported maintained Python release,
- Python 3.12 is now in security-fixes-only lifecycle and no longer receives
  regular bugfix binary releases,
- Django 5.2 LTS officially supports Python 3.13,
- Python 3.13 is a conservative compatibility baseline for the initial
  Django/PostgreSQL runtime,
- it is well aligned with current Django support expectations,
- it avoids anchoring bootstrap to an older compatibility target without
  repository evidence.

Implementation note:

- record the chosen version explicitly in project bootstrap files once PR-0000
  is implemented.
- do not guess a lower version silently.

## Django Version

Repository-specified Django version:

- none found

Recommendation:

- Django 5.2 LTS

Rationale:

- DEVELOPMENT_SPEC explicitly names Django as the backend framework,
- an LTS release minimizes near-term framework churn,
- this is the strongest stable baseline for a new repository with no existing
  compatibility constraints,
- it keeps runtime bootstrap simple without prematurely bringing in optional
  framework layers.

Not included in PR-0000:

- Django REST Framework

Reason:

- DEVELOPMENT_SPEC lists DRF in proposed stack, but PR-0000 only needs the
  minimum runtime to support model/migration/test work.
- DRF can be added later when API work begins.

## Dependency Management

Options evaluated:

### Option A: pyproject.toml + pip

Pros:

- modern Python-standard project metadata location,
- easy to extend later,
- no extra package manager required,
- works with vanilla `pip` and `venv`.

Cons:

- slightly more setup than a single requirements file.

### Option B: requirements.txt

Pros:

- extremely simple,
- familiar for minimal Django bootstrap,
- no additional packaging decisions.

Cons:

- weaker long-term project metadata story,
- dependency groups and tooling metadata get awkward as the repo grows.

### Option C: uv or poetry

Assessment:

- repository evidence does not support adopting extra dependency-management
  tooling yet.
- `.gitignore` contains generic ignore patterns for these tools, but that is not
  architecture evidence.

Recommendation:

- use `pyproject.toml` + `pip`

Reason:

- simplest maintainable modern baseline,
- adds no extra toolchain dependency,
- gives the repository a standard home for Python version and dependency
  metadata,
- better long-term fit than `requirements.txt` alone while staying lightweight.

Practical note:

- a generated lock or exported requirements file may be added later if needed,
  but it is not required for PR-0000.

## Django Project Layout

Recommended layout:

```text
manage.py
config/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```

Recommendation rationale:

- conventional and familiar,
- sufficient for bootstrap without unnecessary settings fragmentation,
- easy to evolve later into split settings only if real complexity appears,
- minimizes PR-0000 surface area.

Explicit recommendation:

- use one `config/settings.py` file in PR-0000
- do not create multi-file settings packages yet

## Database

Repository direction from DEVELOPMENT_SPEC:

- initial recommended backend stack includes PostgreSQL
- local development SHOULD support PostgreSQL

Decision:

- PostgreSQL is the intended development and production baseline
- do not silently choose SQLite as the authoritative project database

Local development expectation:

- developer runs a local PostgreSQL instance by any preferred method
- bootstrap should not require Docker in PR-0000
- Docker Compose may be introduced later if the repository chooses to standardize
  service startup

Environment-variable contract recommendation:

- prefer explicit Django/PostgreSQL environment variables over `DATABASE_URL`
  in PR-0000

Recommended variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

Reason:

- avoids adding a database-URL parsing dependency in the bootstrap PR,
- keeps configuration obvious and framework-native,
- can be mapped to `DATABASE_URL` later if repository conventions evolve.

Test strategy:

- use Django's standard test database creation on PostgreSQL
- test runtime should derive from the same PostgreSQL environment contract
- do not introduce a separate database backend just for tests in PR-0000

## Environment Variables

PR-0000 should define a minimal environment contract.

Planned files/conventions:

- `.env.example`
- real `.env` excluded from git
- no real secrets committed

Minimum bootstrap variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

Optional future variables, not required in PR-0000:

- allowed hosts
- CSRF/trusted origins
- logging level
- provider credentials

Secrets policy:

- `.env` remains ignored by git
- `.env.example` documents keys only, never values beyond safe placeholders

## Testing

Minimum testing baseline for PR-0000:

- `python manage.py check`
- ability to run Django test runner successfully
- one bootstrap smoke test or empty test package proving test discovery works
- database-backed test viability on PostgreSQL

Recommendation:

- include one minimal smoke test rather than relying on an empty test suite

Reason:

- proves Django settings, app registry, and test database wiring actually work,
- gives PR-0001A a concrete baseline to extend.

## Project Conventions

Only conventions needed before PR-0001A should be fixed now.

UUID identities:

- recommend UUID primary keys as baseline convention
- aligns with DEVELOPMENT_SPEC identity guidance and downstream domain specs

Timestamps:

- recommend a small reusable baseline convention for `created_at` and
  `updated_at` only if implemented consistently from bootstrap onward
- no broader audit/history mixins in PR-0000

App organization:

- do not create many apps in PR-0000
- create only the minimal project/runtime app structure needed to boot Django
- let PR-0001A apply the already-approved planning-slice app-boundary decision

Tests layout:

- use repository-local app/package test modules consistent with Django default
  discovery
- prefer plain Django `TestCase` baseline before introducing pytest-specific
  tooling

## Candidate Django App Boundary

Bootstrap choices evaluated:

### Option A: Create only project-level runtime skeleton in PR-0000

Includes:

- config package
- manage.py
- optional tiny core/runtime app only if Django requires a local app anchor

Pros:

- minimal runtime surface,
- avoids pre-committing domain app boundaries too early,
- clean handoff to PR-0001A.

Cons:

- very little application code exists after bootstrap.

### Option B: Create runtime skeleton plus planning app in PR-0000

Pros:

- slightly fewer files in PR-0001A.

Cons:

- leaks domain-slice implementation into bootstrap,
- violates bootstrap-only discipline,
- risks mixing engineering and domain review scope.

Recommendation:

- choose Option A

Reason:

- PR-0000 should establish runtime only
- PR-0001A should remain the first domain-model PR

## Candidate Model Mapping

PR-0000 creates no business/domain models.

Potential bootstrap-only model policy:

- none required

If Django bootstrap requires an installed local app:

- prefer an empty runtime/core app with no business models
- do not create placeholder domain tables

## Database Constraints

PR-0000 should not introduce business-domain constraints.

Only bootstrap-level database expectations:

- Django can connect to PostgreSQL
- migrations framework initializes successfully
- test database can be created/destroyed successfully

No domain uniqueness or ordering constraints belong in this PR.

## Validation Rules

PR-0000 validation scope:

- Django settings load successfully
- required environment variables are validated early and fail clearly
- database configuration is structurally valid for Django startup

Deferred validation:

- domain-model validation
- business invariants
- cross-model validation

## Test Plan

PR-0000 test plan should cover:

- Django system check passes
- Django test runner executes successfully
- bootstrap smoke test passes
- migration graph initializes
- database test creation works against PostgreSQL configuration

Do not add:

- domain model tests
- API tests
- provider integration tests

## Migration Plan

PR-0000 migration scope:

- initialize Django project
- initialize migration framework
- create only bootstrap/runtime migrations if Django requires them
- do not add business/domain tables

Migration discipline:

- no unrelated migration noise
- no planning-domain models yet

## Development Commands

Baseline commands to support after PR-0000 implementation:

- create virtual environment
- install dependencies
- run `python manage.py check`
- run `python manage.py migrate`
- run `python manage.py test`
- run `python manage.py runserver`

Optional later commands, not required in PR-0000:

- worker processes
- provider daemons
- storage services

## Implementation Sequence

1. Add dependency manifest.
2. Add Django project skeleton.
3. Add settings and environment-variable loading.
4. Add PostgreSQL configuration wiring.
5. Add minimal test baseline.
6. Initialize migration baseline.
7. Document developer bootstrap commands.

## Definition of Done

PR-0000 is done when:

- Python environment is installable
- Django imports successfully
- `python --version` runs successfully and reports the configured Python
  baseline
- `python -m django --version` runs successfully
- `python manage.py check` passes
- `python manage.py migrate` runs successfully against the configured
  PostgreSQL environment
- `python manage.py test` runs successfully against the configured PostgreSQL
  environment
- migration system initializes
- tests can run
- no business/domain models exist yet
- no secrets are committed
- PostgreSQL configuration is wired through environment variables
- runtime foundation is sufficient for PR-0001A to add models without inventing
  project conventions implicitly

Environment-blockage rule:

- PR-0000 is not complete merely because bootstrap files exist.
- If PostgreSQL is unavailable, PR-0000 completion is environment-blocked and
  must be reported as such.
- The implementation must not silently fall back to SQLite.

## Open Questions

Non-blocking follow-up questions:

- should the repository later adopt split settings modules by environment?
- should Docker Compose become standard for local PostgreSQL bootstrapping?
- should DRF enter the runtime baseline before the first API PR?

Current blocking engineering decisions:

- none, if PR-0000 adopts the explicit recommendations in this plan

## ADR Check

Assessment:

- PR-0000 does not require a new ADR

Reason:

- it implements runtime bootstrap only,
- it does not change accepted domain architecture,
- it does not force provider, workflow, or generation policy decisions.

## Risks

- Risk: choosing Python 3.13 is an explicit engineering decision because no
  repository version is currently specified.
- Risk: choosing Django 5.2 LTS sets a framework baseline that later PRs must
  follow unless deliberately revised.
- Risk: PostgreSQL-first local development introduces a real service dependency
  before any domain models exist.
- Risk: using explicit DB environment variables instead of `DATABASE_URL` may
  need later adaptation if hosting conventions differ.

Risk level overall:

- low to moderate

## Review Checklist

- runtime bootstrap only
- no domain/business models
- no dependency installation in this plan document
- Django project layout recommended
- Python version decision explicit
- Django version decision explicit
- dependency-management decision explicit
- PostgreSQL direction explicit
- environment-variable contract explicit
- testing baseline explicit
- migration baseline explicit
- no secrets committed
- no new ADR required

## Final Readiness

Final determination:

- READY FOR PR-0000 IMPLEMENTATION

Reason:

- the repository has enough documentation to choose a conservative Django
  runtime baseline,
- no unresolved engineering decision remains that would force implementers to
  guess during bootstrap,
- domain implementation remains deferred to later PRs as intended.
