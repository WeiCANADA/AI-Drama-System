# Cinematography

## Research Metadata

- Research ID: RL-PROD-CINE-001
- Discipline: Cinematography and Camera Grammar
- Source Type: Official software manuals and educational production references
- Status: Draft Archived
- Primary AI Drama Modules Affected: Shot, Storyboard, Prompt, QC, Generation
- Last Reviewed: 2026-07-28

## 1. Purpose

This record captures practical cinematography controls relevant to shot intent modeling and reproducible generation planning.

## 2. Professional Terminology

- Focal length (lens): influences field of view and perspective characteristics. Source: https://docs.blender.org/manual/en/latest/render/cameras.html
- Depth of field: controls focus plane and blur falloff; can be tied to focus distance and aperture settings. Source: https://docs.blender.org/manual/en/latest/render/cameras.html
- Camera framing scales and shot classes (wide, medium, close) in film grammar pedagogy. Source: https://www.khanacademy.org/computing/pixar/storytelling/film-grammar/a/glossary-grammar
- Camera motion intent (pan, tilt, dolly style movement as planning grammar; terminology scope marked as common practice in this layer).

## 3. Professional Definitions

- Cinematography for this system context: intentional camera/framing decisions that shape narrative meaning, readability, and emotional emphasis.
- Technical camera controls (lens, focus, sensor/framing proxies) are implementation parameters that should remain distinct from core production intent.

## 4. Typical Production Workflow

- Story and scene intent define emotional and narrative goals.
- Storyboards propose framing/motion strategies for each shot.
- Camera parameters are refined through previs/layout and reviewed in timing context.
- Editorial review validates whether cinematography supports story clarity and rhythm.

## 5. Roles and Responsibilities

- Director / cinematography leadership: author shot intention.
- Storyboard and previs artists: map intent to candidate framing/motion.
- Technical artists / pipeline operators: convert intent to executable parameters.
- Editorial/review stakeholders: evaluate result against narrative objectives.

## 6. Inputs

- Scene intent and beat context.
- Shot list and boarded framing references.
- Character and environment scale references.
- Technical camera options supported by target workflow/provider.

## 7. Outputs / Deliverables

- Shot-level cinematography intent package.
- Parameterized camera plans (when workflow requires numeric settings).
- Review notes tied to shots and revisions.

## 8. Production Records / Data

- Shot framing type.
- Lens/focal length targets where relevant. Source: https://docs.blender.org/manual/en/latest/render/cameras.html
- Focus/depth intent. Source: https://docs.blender.org/manual/en/latest/render/cameras.html
- Motion intent tags.
- Revision history and approval status.

## 9. Lifecycle / State Changes

- Initial framing idea -> boarded shot intent -> technical parameter proposal -> reviewed output -> revised/approved shot camera package.

## 10. Relationships to Other Production Concepts

- Scene and Storyboard: provide context and preliminary framing logic.
- Shot: primary unit where camera intent is attached.
- Continuity: camera decisions must remain coherent across shot transitions.
- QC: evaluates both narrative effectiveness and technical consistency.
- Generation workflow: adapter translates intent to provider/tool parameter schemas.

## 11. Stable Industry Concepts

- Framing and lensing materially affect story comprehension and emotional emphasis.
- Camera intent and technical parameterization are related but separable layers.
- Iterative review is required to validate cinematography decisions.

## 12. Studio-Specific or Variable Practices

- Exact lens kits, naming conventions, and motion taxonomy vary by studio.
- Some pipelines specify numeric camera values early; others remain qualitative until late stages.
- Provider/workflow-specific camera controls can diverge significantly from traditional camera rigs.

## 13. Research Findings

- Finding: Blender official camera documentation provides concrete lens, camera type, and depth-of-field control semantics useful for reproducible camera parameter modeling. Source: https://docs.blender.org/manual/en/latest/render/cameras.html
- Finding: Film grammar educational resources explicitly distinguish shot classes and visual storytelling function, grounding camera decisions in narrative intent. Source: https://www.khanacademy.org/computing/pixar/storytelling/film-grammar/a/glossary-grammar
- Finding: Storyboard-oriented workflows include camera and timing planning, indicating camera intent should exist before final generation/render. Source: https://docs.toonboom.com/help/storyboard-pro-27/storyboard/book/user-guide/about-user-guide.html

## 14. Research Principles

- Principle: Model cinematography as shot-level intent first, technical parameterization second.
- Principle: Preserve provider independence by translating intent via adapters.
- Principle: Store camera decision provenance for reproducibility and review.

## 15. Impact on AI Drama System

- Supports shot-centric camera intent schema.
- Supports intent-to-parameter translation boundaries in workflow adapters.
- Supports reproducible generation by preserving explicit camera settings when available.

## 16. Candidate Domain Concepts

- Candidate ShotCameraIntent
- Candidate LensIntent
- Candidate FocusIntent
- Candidate CameraMotionIntent
- Candidate CinematographyQCRecord

## 17. Candidate Requirements

- CANDIDATE: The system shall attach cinematography intent to Shot entities.
- CANDIDATE: The system shall preserve separation between qualitative camera intent and provider-specific numeric controls.
- CANDIDATE: The system shall maintain camera-related provenance in generation outputs where available.

## 18. Candidate ADRs

- CANDIDATE ADR: Use provider-agnostic camera intent vocabulary in domain; map to provider workflow schema in adapters.
- CANDIDATE ADR: Store optional numeric camera parameters as versioned execution metadata, not canonical story intent.

## 19. Open Questions

- What minimum camera intent vocabulary should be standardized for v1?
- Which camera parameters are mandatory for reproducibility claims?
- How should conflicting camera intents be resolved across storyboard revision branches?

## 20. Sources

- Blender Foundation, Blender Manual - Cameras, https://docs.blender.org/manual/en/latest/render/cameras.html, accessed 2026-07-28, source type: official software documentation.
- Khan Academy + Pixar, Glossary: Film Grammar, https://www.khanacademy.org/computing/pixar/storytelling/film-grammar/a/glossary-grammar, accessed 2026-07-28, source type: authoritative educational collaboration.
- Toon Boom Animation, Storyboard Pro 27 User Guide, https://docs.toonboom.com/help/storyboard-pro-27/storyboard/book/user-guide/about-user-guide.html, accessed 2026-07-28, source type: official software production documentation.
