# ADR-0002: AI providers are isolated behind provider interfaces

## Status

Accepted

## Decision

All future AI providers will be integrated behind provider interfaces and adapter layers.

## Rationale

This keeps Django models, services, and workflows independent from specific vendors, APIs, or model families. It allows the platform to evolve across image, video, audio, and language providers without restructuring the domain model.
