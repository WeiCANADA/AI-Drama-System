# Standards Architecture Synthesis v1

## 1. Scope

This synthesis consolidates Layer 4 standards research records:
- [../architecture/camera-spatial-interchange.md](../architecture/camera-spatial-interchange.md)
- [../architecture/provenance-interchange.md](../architecture/provenance-interchange.md)
- [../architecture/temporal-editorial-interchange.md](../architecture/temporal-editorial-interchange.md)

Status policy:
- Research synthesis only.
- No architecture decision is accepted here.
- No standard or technology is adopted here.
- All requirements and ADR items remain candidates.

## 2. Cross-standard Findings

- External standards are complementary but layer-specific.
- No single standard is sufficient as AI Drama core domain ontology.
- A stable mapping boundary is repeatedly supported:
  AI Drama Domain -> Internal Contract -> Adapter/Interchange -> External Standard.
- Interoperability value is high when identity, provenance, and temporal contracts
  remain internal-first and traceable.

## 3. Camera/Spatial Findings

- glTF 2.0 provides strong interoperable spatial/camera representation primitives.
- OTIO provides editorial composition/timing constructs, not 3D spatial ontology.
- SMPTE provides standards ecosystem and related media/timing/camera metadata
  families, but this batch remains partial for camera-spatial clause-depth review.
- Implication: define provider-neutral internal camera/spatial intent and map via
  adapters to external interchange targets.

## 4. Provenance Findings

- W3C PROV provides neutral provenance graph semantics suitable for internal
  production causality modeling.
- C2PA provides signed authenticity packaging suitable for external verification
  workflows.
- Internal production provenance != external authenticity provenance.
- Implication: maintain separate-but-linkable provenance layers.

## 5. Temporal/Editorial Findings

- SMPTE ST 12 family is a formal time and control code reference family.
- OTIO provides editorial timeline/clip/time-range interchange semantics.
- Shot identity must remain independent of timeline placement and clip constructs.
- Implication: keep identity, timing references, editorial placement, and media
  segment artifacts as distinct but linkable layers.

## 6. Domain vs Interchange Boundary

Recommended conceptual separation:

- Domain:
  - Shot identity, intent, continuity context, provenance anchors.
- Internal contract:
  - Neutral camera/spatial/provenance/temporal schemas.
- Adapter/interchange:
  - OTIO payloads, glTF payloads, optional C2PA manifests, SMPTE-aligned labels.
- External standard:
  - Standard-specific representations and constraints.

Guardrail:
- Do not replace core domain entities with external schema entities
  (for example OTIO Clip, glTF Node/Camera).

## 7. Stable Architecture Principles

- Principle 1: Internal domain semantics remain primary.
- Principle 2: External standards are integration targets, not ontology sources.
- Principle 3: Provenance and temporal traceability must remain end-to-end.
- Principle 4: Provider neutrality is preserved by contract-first design.
- Principle 5: Candidate standards remain replaceable until formal decision.

## 8. Consolidated Candidate Requirements

- CANDIDATE CR-ARCH-001: Define a versioned internal camera/spatial intent
  contract with mandatory/optional fields.
- CANDIDATE CR-ARCH-002: Define a minimal internal provenance graph contract for
  Shot -> PromptInstance -> GenerationTask -> GenerationAttempt ->
  GenerationResult -> Artifact.
- CANDIDATE CR-ARCH-003: Define separate internal structures for temporal identity,
  timeline placement, and media segment timing.
- CANDIDATE CR-ARCH-004: Define adapter mappings to selected interchange targets
  (OTIO/glTF/C2PA/SMPTE-aligned labels) by profile.
- CANDIDATE CR-ARCH-005: Require reversible traceability links between internal
  contract fields and exported interchange fields.

## 9. Standards/Technology Candidate Registry

- Candidate: W3C PROV
  - Role: internal provenance semantics reference
  - Status: Technology Candidate
- Candidate: C2PA 2.2
  - Role: external authenticity packaging reference
  - Status: Technology Candidate
- Candidate: OpenTimelineIO
  - Role: editorial interchange reference
  - Status: Technology Candidate
- Candidate: glTF 2.0
  - Role: camera/spatial interchange reference
  - Status: Technology Candidate
- Candidate: SMPTE standards families (including ST 12 suite)
  - Role: timing/media interoperability reference
  - Status: Standards Candidate Set

## 10. Candidate ADR Review Queue

- CANDIDATE ADR-Q-001: Should one canonical internal camera/spatial contract be
  required across all provider profiles?
- CANDIDATE ADR-Q-002: Should internal provenance be modeled as graph-native,
  relational-event-native, or hybrid?
- CANDIDATE ADR-Q-003: When is external authenticity packaging required in product
  profiles (if ever)?
- CANDIDATE ADR-Q-004: Should OTIO import/export be baseline or optional module?
- CANDIDATE ADR-Q-005: What canonical time-base policy is required for mixed-rate
  editorial pipelines?

## 11. Answers to Shot Layer 4 Research Requests

### 11.1 RL-ARCH-CAMERA-001 (Camera / Spatial)

- Evidence:
  - glTF 2.0 normative spatial/camera primitives.
  - OTIO official editorial/time composition model.
  - SMPTE standards portal + open library index evidence.
- What is now known:
  - A neutral internal camera/spatial intent contract can map outward to external
    standards through adapters.
  - External schemas are complementary but incomplete for Shot-domain semantics.
- What remains unknown:
  - Final minimal camera/spatial field set and mandatory profile policy.
  - Full clause-level SMPTE camera-spatial implications.
- Recommended architectural direction:
  - Keep Shot-domain intent internal-first; export/import via adapter mappings.
- ADR required?:
  - Likely yes, for canonical internal contract commitment.
- Blocking?:
  - Non-blocking for conceptual Shot v1; potentially blocking for strict
    interoperability implementation milestone.

### 11.2 RL-ARCH-PROV-001 (Provenance)

- Evidence:
  - W3C PROV-DM/PROV-O/overview semantics.
  - C2PA 2.2 authenticity manifest and validation model.
- What is now known:
  - Internal provenance and external authenticity are distinct and should be
    separate layers.
  - Minimal internal chain provenance abstraction is feasible and standards-aligned.
- What remains unknown:
  - Canonical ID profile, retention policy, and redaction policy details.
- Recommended architectural direction:
  - Implement internal provider-neutral provenance contract first; expose optional
    authenticity manifests through adapters.
- ADR required?:
  - Likely yes, for internal provenance data model and optional C2PA policy.
- Blocking?:
  - Non-blocking for conceptual Shot/domain drafts; may become blocking for
    external publishing/compliance workflows.

### 11.3 RL-ARCH-TIME-001 (Temporal / Editorial)

- Evidence:
  - SMPTE ST 12 suite discoverability and official timecode explanation.
  - OTIO timeline and timing interchange model.
- What is now known:
  - Shot identity must remain separate from timeline placement, media duration,
    generated segment, and editorial clip.
  - A layered temporal model is feasible and consistent with architecture rules.
- What remains unknown:
  - Canonical normalization strategy across mixed frame rates and drop-frame rules.
  - Minimum mandatory temporal metadata before timeline assembly/export.
- Recommended architectural direction:
  - Define internal temporal contract layers, then map to OTIO/SMPTE-aligned
    representations via adapters.
- ADR required?:
  - Likely yes, for canonical time-base policy and mandatory temporal fields.
- Blocking?:
  - Non-blocking for current conceptual Shot scope; potentially blocking for
    editorial round-trip interoperability implementation.

## 12. Remaining Open Questions

- Which exact SMPTE document subsets are mandatory for deeper clause-level camera
  and temporal interoperability definition?
- Which minimal internal contract fields are globally mandatory vs profile-based?
- How should provenance/privacy redaction be standardized without losing
  reproducibility value?
- What compatibility guarantees (lossless/lossy/round-trip) should adapters meet?

## 13. Recommended Next Research

- Next R1: Targeted SMPTE deep-dive record with clause-level extraction for ST 12
  and related timing/camera metadata references from open library documents.
- Next R2: Internal contract draft record for camera/spatial fields with mapping
  matrix to glTF and OTIO.
- Next R3: Internal provenance contract draft record with PROV alignment profile
  and optional C2PA binding profile.
- Next R4: Temporal normalization profile research for mixed frame-rate projects,
  including drop-frame handling and round-trip editorial constraints.

## Official Source Note

All standards and technologies in this synthesis remain candidates.
No adoption decision is made in this document.
