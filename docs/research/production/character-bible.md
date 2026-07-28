# Character Bible / Character Design References

## Research Metadata

- Research ID: RL-PROD-CHAR-001
- Discipline: Character Development and Visual Continuity
- Source Type: Production education references and software documentation
- Status: Draft Archived
- Primary AI Drama Modules Affected: Character, Asset, Continuity, Storyboard, Prompt, QC
- Last Reviewed: 2026-07-28

## 1. Purpose

This record captures industry practices for maintaining consistent character identity across script, storyboard, and production outputs, without binding core design to any single AI identity technology.

## 2. Professional Terminology

- Character (story role): story agent with emotional state, goals, and arc contribution. Source: https://www.khanacademy.org/computing/pixar/storytelling/story-structure/v/piab-storystructure
- Character design references (production practice): persistent visual references used by art/story teams to keep identity stable across shots.
- Continuity references: records that track appearance consistency over time and scene transitions.
- Iterative feedback on character portrayal in board stages. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback

## 3. Professional Definitions

- Character bible (common studio term, variable format): curated reference package describing visual identity, personality cues, and usage constraints.
- Character reference set (stable concept): approved image/text references used by artists and downstream departments.
- Character continuity record (stable concept): change log across scenes/shots for wardrobe, silhouette, and other persistent traits.

This source set contains strong educational and tooling evidence for continuity and iterative review, but limited openly published studio-internal templates for full bible schemas.

## 4. Typical Production Workflow

- Story development defines character goals and emotional function. Source: https://www.khanacademy.org/computing/pixar/storytelling/story-structure/v/piab-storystructure
- Initial character references are prepared for board and visual planning.
- Storyboards expose character readability and consistency issues through review loops. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback
- Revisions update reference packages and continuity notes before downstream generation/animation.

## 5. Roles and Responsibilities

- Writer/director: define narrative role and performance intent.
- Character designer/art team: define visual identity and variant boundaries.
- Storyboard artists: validate readability and staging in context.
- Continuity/script supervision equivalents: track cross-scene consistency.
- Production management: ensure approved versions are used in active workflows.

## 6. Inputs

- Character narrative intent and arc notes.
- Visual concept art, expressions, pose references.
- Scene/shot context from script and storyboard.
- Feedback notes from reviews/pitches. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback

## 7. Outputs / Deliverables

- Character reference package (images + textual constraints).
- Versioned character variants for context-specific usage.
- Continuity checklists linked to scenes/shots.
- Review notes and approval states.

## 8. Production Records / Data

- Character IDs and version IDs.
- Reference artifact provenance (source image, date, owner, approval).
- Continuity deltas across scenes/shots.
- Storyboard-linked character issues and resolution logs.

## 9. Lifecycle / State Changes

- Candidate concept -> approved base character -> contextual variants -> in-production locked version -> post-review updates.

## 10. Relationships to Other Production Concepts

- Story: character choices must serve narrative beats.
- Scene/Shot: character references are validated in framing and continuity context.
- Storyboard: primary early-stage validation surface.
- Continuity: bridges appearance/performance across adjacent and non-adjacent shots.
- Asset: character should be modeled as reusable production asset identity separate from individual generated artifacts.

## 11. Stable Industry Concepts

- Character consistency is broader than face identity; it includes silhouette, wardrobe, and repeatable design cues.
- Iterative review is required to keep character portrayal coherent.
- Reference sets must remain accessible and current for all departments.

## 12. Studio-Specific or Variable Practices

- Character bible template fields vary significantly across studios.
- Some pipelines maintain strict turnarounds/expression sheets; others rely on lighter references.
- Granularity of version control differs by production scale and tooling maturity.

## 13. Research Findings

- Finding: Pixar-aligned educational material emphasizes iterative storyboard feedback, which includes character readability in story context. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback
- Finding: Story structure teaching reinforces that character intent is tied to story beat progression, implying design references must support narrative function, not only visual identity. Source: https://www.khanacademy.org/computing/pixar/storytelling/story-structure/v/piab-storystructure
- Finding: Production tracking tooling highlights version/review workflows needed for maintaining approved references over time. Source: https://help.autodesk.com/view/SGSUB/ENU/

## 14. Research Principles

- Principle: Character reference management should separate identity from version.
- Principle: Character consistency requires both narrative and visual continuity.
- Principle: Character reference records should be reviewable, versioned, and traceable across shot pipelines.

## 15. Impact on AI Drama System

- Supports Character as reusable Asset with explicit versioning and provenance.
- Supports continuity checks tied to Scene/Shot transitions.
- Supports provider-independent character intent layer before prompt/workflow translation.

## 16. Candidate Domain Concepts

- Candidate Character
- Candidate CharacterVersion
- Candidate CharacterReferenceSet
- Candidate CharacterContinuityRecord
- Candidate CharacterConstraintProfile

## 17. Candidate Requirements

- CANDIDATE: The system shall separate Character identity from CharacterVersion.
- CANDIDATE: The system shall support versioned character reference sets linked to Storyboard and Shot contexts.
- CANDIDATE: The system shall store continuity-relevant appearance constraints as structured, reviewable data.

## 18. Candidate ADRs

- CANDIDATE ADR: Character consistency is modeled as asset version governance plus continuity validation, not provider-specific embeddings.
- CANDIDATE ADR: Character reference artifacts are first-class and traceable to approvals and shot usage.

## 19. Open Questions

- What minimum schema for character bible fields should be standardized first?
- Which continuity attributes are mandatory vs optional by production type?
- How should conflicting character references be resolved when parallel revisions exist?

## 20. Sources

- Khan Academy + Pixar, Pitching and Feedback, https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback, accessed 2026-07-28, source type: authoritative educational collaboration.
- Khan Academy + Pixar, Story Structure, https://www.khanacademy.org/computing/pixar/storytelling/story-structure/v/piab-storystructure, accessed 2026-07-28, source type: authoritative educational collaboration.
- Autodesk, Flow Production Tracking Help Center, https://help.autodesk.com/view/SGSUB/ENU/, accessed 2026-07-28, source type: official production tracking documentation.
- Toon Boom Animation, Storyboard Pro 27 User Guide, https://docs.toonboom.com/help/storyboard-pro-27/storyboard/book/user-guide/about-user-guide.html, accessed 2026-07-28, source type: official software production documentation.
