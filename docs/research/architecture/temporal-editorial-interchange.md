# RL-ARCH-TIME-001 - Temporal / Editorial Interchange

## 1. Research Metadata

- Research ID: RL-ARCH-TIME-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Requested by: [docs/domain/shot.md](../../domain/shot.md) Section 28
- Scope: neutral temporal/editorial concepts for interoperability
- Constraint: keep Shot identity separate from timeline and media constructs

## 2. Research Question

What neutral temporal/editorial concepts may be needed for future Shot,
continuity, storyboard, video, and editing interoperability?

Required distinctions:
- Shot identity != timeline placement
- Shot identity != media duration
- Shot identity != generated video segment
- Shot identity != editorial clip

## 3. Standards Investigated

- SMPTE timecode ecosystem
  - ST 12 family discoverability via official document library
  - official SMPTE explanatory material for time code concepts
- ASWF / OpenTimelineIO (OTIO)

## 4. Findings

- [STANDARD-DEFINED] SMPTE official materials identify a Time and Control Code
  family (ST 12-1, ST 12-2, ST 12-3) for frame/field labeling and transport
  semantics across production/post workflows.
- [STANDARD-DEFINED] SMPTE timecode concept includes frame-address style labeling
  and supports multiple frame-rate families and drop-frame modes (per official
  SMPTE explanatory material).
- [OFFICIAL-PROJECT-DEFINED] OTIO defines editorial composition and timing
  constructs (Timeline/Track/Clip, RationalTime/TimeRange), suitable for timeline
  placement and edit decision interchange.
- [STANDARD-SPECIFIC] OTIO timing constructs define editorial placement semantics,
  not Shot domain identity or continuity semantics by themselves.
- [CROSS-STANDARD SUPPORT] SMPTE time labeling and OTIO timeline composition are
  complementary for editorial interoperability when connected by stable internal IDs.
- [INTERPRETATION] AI Drama should retain Shot as canonical identity and map to
  one or more temporal representations for interchange/editorial needs.
- [OPEN QUESTION] Minimal mandatory temporal fields for v1 interoperability remain
  unresolved.

## 5. Cross-standard Comparison

- SMPTE contributes formalized timing/timecode ecosystem concepts.
- OTIO contributes editorial timeline structure and interchange abstraction.
- Neither standard directly defines AI Drama Shot ontology.
- Combined usage can support robust timeline and edit interoperability if internal
  identity and provenance contracts remain primary.

## 6. Stable Findings

- Stable finding A: Shot identity must remain independent from timeline-specific
  placement records.
- Stable finding B: Timecode-like labels and editorial time ranges should be
  modeled as related-but-separate temporal references.
- Stable finding C: Generated media segment boundaries and editorial clip
  boundaries are context-dependent and should not redefine Shot identity.

## 7. Gaps

- Gap 1: Internal canonical temporal contract linking Shot, continuity checkpoints,
  generated segment boundaries, and editorial clips.
- Gap 2: Policy for frame-rate normalization and drop-frame handling across mixed
  pipelines.
- Gap 3: Crosswalk from OTIO timing objects to AI Drama continuity review and
  generation provenance records.

## 8. AI Drama System Implications

- Define temporal layers explicitly:
  - Identity layer: Shot ID and ordering.
  - Timing-reference layer: optional timecode/clock/frame-rate references.
  - Editorial layer: OTIO-like timeline placement entities.
  - Media-result layer: generated segment durations and artifact offsets.
- Preserve boundary:
  AI Drama Domain -> Internal Contract -> Adapter/Interchange -> External Standard.
- Keep editorial clip constructs in interchange/adapters, not as replacements for
  Shot domain identity.

## 9. Candidate Requirements

- CANDIDATE CR-ARCH-TIME-001: Define minimal temporal identity contract with
  explicit separation of Shot ID, Shot order, and optional timeline placement IDs.
- CANDIDATE CR-ARCH-TIME-002: Define frame-rate and time-base metadata policy
  fields for generated video and editorial interchange.
- CANDIDATE CR-ARCH-TIME-003: Define adapter mappings between internal temporal
  contract and OTIO timing constructs.
- CANDIDATE CR-ARCH-TIME-004: Define optional timecode reference fields compatible
  with SMPTE timecode concepts where needed.

## 10. Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-TIME-001: Should a canonical internal time-base model be
  enforced globally or profile-specific?
- CANDIDATE ADR-Q-ARCH-TIME-002: Which temporal fields are required before
  timeline assembly/export is allowed?
- CANDIDATE ADR-Q-ARCH-TIME-003: Should OTIO export/import be baseline capability
  or optional module?

## 11. Open Questions

- What minimal continuity checkpoint representation is needed between adjacent
  shots for editorial handoff?
- How should mixed-rate projects (23.98/24/25/29.97/30/50/59.94/60) be normalized
  without data loss?
- What is the required granularity for temporal provenance links from generation
  attempts to final editorial placements?

## 12. Official Sources

- SMPTE Standards portal
  - Organization: SMPTE
  - URL: https://www.smpte.org/standards
  - Version: N/A (web portal)
  - Accessed: 2026-07-28
- SMPTE Document Library index
  - Organization: SMPTE
  - URL: https://pub.smpte.org/doc/
  - Version: live index
  - Accessed: 2026-07-28
  - Note: ST 12-1, ST 12-2, ST 12-3 entries are visible in index.
- SMPTE official explainer: Understanding Standards: Time Code
  - Organization: SMPTE
  - URL: https://www.smpte.org/blog/understanding-standards-time-code
  - Version: article dated 2025-02-26
  - Accessed: 2026-07-28
  - Note: explanatory source; not a substitute for normative clause text.
- OpenTimelineIO documentation
  - Organization: Academy Software Foundation (ASWF)
  - URL: https://opentimelineio.readthedocs.io/en/latest/
  - Version: latest (as published)
  - Accessed: 2026-07-28
- OpenTimelineIO repository
  - Organization: ASWF
  - URL: https://github.com/AcademySoftwareFoundation/OpenTimelineIO
  - Version: repository main branch (as accessed)
  - Accessed: 2026-07-28

Source-limit disclosure:
- This record does not claim a complete clause-level review of all SMPTE temporal
  standards beyond what was accessible and indexed in this batch.
