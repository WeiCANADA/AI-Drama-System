# ADR-0003: AI Drama System is model-agnostic and workflow-driven

## Status

Accepted

## Decision

The platform will remain model-agnostic and represent generation pipelines through configurable workflows.

## Rationale

Drama production requires repeatable, auditable, and replaceable generation steps. Workflow-driven orchestration makes those steps versionable, while model-agnostic design prevents business logic from depending on a single provider or prompt pattern.
