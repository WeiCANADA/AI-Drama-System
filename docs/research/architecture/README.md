# Architecture Standards Research (Layer 4)

## Purpose

This folder contains Layer 4 standards research records requested by the Shot
specification in [docs/domain/shot.md](../../domain/shot.md), Section 28.

Status policy:
- Research artifacts only.
- No architecture decision is accepted here.
- No standard or technology is adopted here.
- All requirements and ADR items remain candidates.

## Records

- [camera-spatial-interchange.md](./camera-spatial-interchange.md)
  - ID: RL-ARCH-CAMERA-001
  - Focus: provider-neutral camera/spatial intent and interchange boundaries.
- [provenance-interchange.md](./provenance-interchange.md)
  - ID: RL-ARCH-PROV-001
  - Focus: minimal provider-neutral provenance concepts across generation chain.
- [temporal-editorial-interchange.md](./temporal-editorial-interchange.md)
  - ID: RL-ARCH-TIME-001
  - Focus: neutral temporal/editorial concepts and interoperability boundaries.

## Boundary Rule

External standards should map as:

AI Drama Domain
-> Internal Contract
-> Adapter / Interchange
-> External Standard

Core domain concepts are not replaced by external standard entities.

## Source Policy

- Prefer primary and official sources.
- Include official URL, organization, version where available, and access date.
- If a source is inaccessible, state limits explicitly.

## Related Synthesis

- [../synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md](../synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md)
