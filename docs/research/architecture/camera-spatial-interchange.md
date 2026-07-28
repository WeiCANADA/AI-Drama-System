# RL-ARCH-CAMERA-001 - Camera / Spatial Interchange

## 1. Research Metadata

- Research ID: RL-ARCH-CAMERA-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Requested by: [docs/domain/shot.md](../../domain/shot.md) Section 28
- Scope: standards-aligned concepts for provider-neutral camera/spatial intent
- Constraint: do not make OTIO Clip or glTF Node/Camera core domain concepts

## 2. Research Question

What standards-aligned concepts could support provider-neutral camera and spatial
intent for Shot without reshaping the core domain around an external standard?

## 3. Standards Investigated

- SMPTE
  - SMPTE standards portal and library index (official)
  - Time and control family visibility (ST 12 suite discoverable)
  - Camera-position-related document discoverability (for example ST 315 title)
- ASWF / OpenTimelineIO (OTIO)
- Khronos / glTF 2.0

## 4. Findings

- [STANDARD-DEFINED] glTF 2.0 defines portable 3D scene representation concepts,
  including scene graphs, node transforms, and camera projection types
  (perspective/orthographic) for exchange/runtime interoperability.
- [STANDARD-SPECIFIC] glTF concepts are asset/scene-graph oriented; they do not
  define narrative Shot identity, dramatic intent, or production review states.
- [OFFICIAL-PROJECT-DEFINED] OTIO defines editorial interchange concepts such as
  Timeline, Track, Clip, composition hierarchy, and time range/rational time.
- [STANDARD-SPECIFIC] OTIO does not define a canonical 3D spatial schema for
  camera blocking or actor spatial geometry semantics.
- [CROSS-STANDARD SUPPORT] SMPTE and OTIO both reinforce interoperability and
  exchange intent, but at different layers (broadcast/media engineering and
  editorial interchange respectively).
- [STANDARD-DEFINED] SMPTE official catalog confirms a formal standards ecosystem
  where time/control and media metadata families are standardized and published.
- [OPEN QUESTION] Direct clause-level review of specific SMPTE camera/spatial
  standards remains partial in this batch; index visibility exists, but a full
  normative walkthrough for all relevant camera-spatial clauses was not completed.
- [INTERPRETATION] The strongest neutral path is to model camera/spatial intent as
  internal contract primitives and translate them to glTF/OTIO/SMPTE-compatible
  interchange outputs via adapters.

## 5. Cross-standard Comparison

- glTF is strongest for spatial geometry and camera transform/projection carriage.
- OTIO is strongest for editorial structure and temporal composition context.
- SMPTE is strongest as standards governance and broad media interoperability
  framework, with discoverable time/control and metadata families.
- None of these, alone, is a complete Shot-domain ontology.

## 6. Stable Findings

- Stable finding A: Provider-neutral Shot intent should not be isomorphic to any
  single external schema.
- Stable finding B: A layered mapping is feasible and consistent with project
  architecture constraints:
  AI Drama Domain -> Internal Contract -> Adapter/Interchange -> External Standard.
- Stable finding C: glTF and OTIO are complementary interchange candidates,
  not domain replacements.

## 7. Gaps

- Gap 1: Neutral vocabulary for cinematography intent beyond raw transforms
  (framing purpose, narrative composition intent, emphasis).
- Gap 2: Neutral representation for relative subject blocking semantics that is
  portable across image/video generation providers.
- Gap 3: Normative SMPTE clause-level camera/spatial analysis beyond index-level
  discoverability in this batch.

## 8. AI Drama System Implications

- Keep Shot as canonical production unit.
- Keep camera/spatial data in provider-neutral internal contracts.
- Map contract subsets to:
  - glTF-compatible transforms/camera payloads where 3D interchange is needed.
  - OTIO-compatible editorial references where timeline context is needed.
  - SMPTE-compatible metadata/time labels where downstream broadcast/edit workflows
    require that interoperability.
- Do not encode glTF Node/Camera or OTIO Clip as core Shot entities.

## 9. Candidate Requirements

- CANDIDATE CR-ARCH-CAM-001: Define a minimal internal camera intent schema
  (shot size, framing intent, angle intent, movement intent, optional numeric
  fields) independent from external schema names.
- CANDIDATE CR-ARCH-CAM-002: Define a minimal internal spatial intent schema
  (relative placement, orientation, depth layering, proximity semantics).
- CANDIDATE CR-ARCH-CAM-003: Require adapter mappings from internal camera/spatial
  contract to at least one external interchange target per integration profile.
- CANDIDATE CR-ARCH-CAM-004: Preserve round-trip traceability between Shot intent
  fields and exported interchange fields.

## 10. Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-CAM-001: Should one canonical internal camera/spatial
  contract version be mandated across all providers?
- CANDIDATE ADR-Q-ARCH-CAM-002: Which fields are mandatory vs optional for
  generation readiness across production profiles?
- CANDIDATE ADR-Q-ARCH-CAM-003: Should glTF export be baseline-capable or profile-
  dependent?

## 11. Open Questions

- Which SMPTE documents, beyond ST 12 family and index-discoverable metadata/camera
  titles, should be mandatory for full camera-spatial normative review?
- What precision and coordinate normalization are required for reproducibility
  without over-constraining creative workflows?
- What is the minimum contract that supports both still-image and video providers?

## 12. Official Sources

- SMPTE Standards portal
  - Organization: SMPTE
  - URL: https://www.smpte.org/standards
  - Version: N/A (web portal)
  - Accessed: 2026-07-28
- SMPTE Open-Access Standards Library announcement
  - Organization: SMPTE
  - URL: https://www.smpte.org/setting-the-standards-free
  - Version: N/A (web page)
  - Accessed: 2026-07-28
- SMPTE Document Library index
  - Organization: SMPTE
  - URL: https://pub.smpte.org/doc/
  - Version: live index
  - Accessed: 2026-07-28
  - Note: ST 12-1, ST 12-2, ST 12-3 entries are discoverable from this index.
- OpenTimelineIO documentation
  - Organization: Academy Software Foundation (ASWF)
  - URL: https://opentimelineio.readthedocs.io/en/latest/
  - Version: latest (as published)
  - Accessed: 2026-07-28
- OpenTimelineIO project repository
  - Organization: Academy Software Foundation (ASWF)
  - URL: https://github.com/AcademySoftwareFoundation/OpenTimelineIO
  - Version: repository main branch (as accessed)
  - Accessed: 2026-07-28
- glTF 2.0 specification
  - Organization: Khronos Group
  - URL: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
  - Version: 2.0
  - Accessed: 2026-07-28
- Khronos glTF overview
  - Organization: Khronos Group
  - URL: https://www.khronos.org/gltf/
  - Version: N/A (overview page)
  - Accessed: 2026-07-28

Source-limit disclosure:
- This record does not claim full clause-by-clause review of all potentially
  relevant SMPTE camera/spatial standards in this batch.
