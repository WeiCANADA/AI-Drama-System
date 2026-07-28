# Initial Architecture Foundation

## System Purpose

AI Drama System is being built as a production platform for AI-assisted drama creation, not as a single-prompt media generator. The platform will manage planning, production, generation, review, and export around a durable domain model.

## Architectural Principles

- Model-agnostic business logic
- Workflow-driven production pipelines
- Asset-centric reusable production elements
- Shot-based production management
- Reproducible generation provenance

## Domain Hierarchy

The initial implementation establishes:

`Project → Story → Episode → Scene → Shot`

Shot is the core production unit, but its schema is intentionally minimal for this milestone.

## Application Boundaries

- `apps.projects`: project-level planning container
- `apps.stories`: story and episode hierarchy
- `apps.production`: scene and shot production units
- `common`: shared abstract models and reusable enums
- `providers`: future provider adapters
- `services`: future orchestration and application services

## Provider Abstraction Strategy

External AI integrations will be isolated behind provider interfaces and adapters. Domain models do not contain provider-specific logic, and this milestone intentionally avoids coupling to ComfyUI, LLM vendors, or media-generation APIs.

## Future Workflow Architecture

Future workflow modules will define versioned generation pipelines that transform production entities such as shots into prompt instances, tasks, attempts, artifacts, and review records. This milestone only prepares the domain foundation those workflows will attach to later.
