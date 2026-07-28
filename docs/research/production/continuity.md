# Continuity

## Research Metadata

- Research ID: RL-PROD-CONT-001
- Discipline: Script Supervision, Editorial Continuity, Visual Consistency
- Source Type: Production education references and production tracking/tool documentation
- Status: Draft Archived
- Primary AI Drama Modules Affected: Continuity, Story, Scene, Shot, Character, Asset, Edit, QC
- Last Reviewed: 2026-07-28

## 1. Purpose

Continuity ensures coherent narrative, spatial, temporal, and character consistency across scenes and shots.

## 2. Professional Terminology

- Continuity (general production practice): maintaining consistency across cuts and scenes.
- Screen direction / 180-degree rule context: orientation and left-right coherence in shot progression. Source: https://www.khanacademy.org/computing/pixar/storytelling/film-grammar/a/glossary-grammar
- Story reel / animatic review: early continuity checkpoint via rough cut assembly. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/a/glossary-pitch
- Timecode context for alignment/sync workflows. Source: https://www.smpte.org/time-code and https://www.smpte.org/standards-overview

## 3. Professional Definitions

- Continuity includes visual continuity (costume/prop/appearance), spatial continuity (blocking/screen direction), temporal continuity (time progression), and narrative continuity (cause/effect coherence).
- Continuity review is iterative and starts before final production using boards and animatics. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback

## 4. Typical Production Workflow

- Continuity intent begins in script/story structure stages.
- Storyboard and story reel expose continuity risks early. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/a/glossary-pitch
- Editorial/prod tracking systems log review outcomes and pending fixes. Source: https://help.autodesk.com/view/SGSUB/ENU/
- Final continuity checks occur through cut review and versioned approvals.

## 5. Roles and Responsibilities

- Writer/director: narrative continuity intent.
- Storyboard and editorial: visual-temporal continuity validation.
- Script supervision equivalents and coordinators: issue logging and fix tracking.
- Production tracking stakeholders: version state and handoff control. Source: https://help.autodesk.com/view/SGSUB/ENU/

## 6. Inputs

- Script scene ordering and time/place markers. Source: https://www.finaldraft.com/learn/screenplay-formatting-elements/
- Storyboards and animatic timing. Source: https://docs.toonboom.com/help/storyboard-pro-27/storyboard/getting-started/animatic.html
- Character and asset reference versions.
- Editorial review notes and timestamps.

## 7. Outputs / Deliverables

- Continuity issue logs.
- Continuity-approved shot/scene revisions.
- Updated character/asset usage notes.
- Final continuity status in review pipelines.

## 8. Production Records / Data

- Continuity checklists per scene/shot.
- Timecode-aware review references where applicable. Source: https://www.smpte.org/time-code
- Versioned notes with owner/status.
- Linkages to source storyboard/animatic/cut artifacts.

## 9. Lifecycle / State Changes

- Potential continuity concern -> triaged issue -> assigned correction -> validated in updated board/cut -> closed or reopened.

## 10. Relationships to Other Production Concepts

- Scene/Shot: continuity is measured at transition boundaries.
- Character/Asset: consistent versions are prerequisite for continuity.
- Storyboard: first major continuity validation surface.
- Edit: final coherence is tested in sequence playback.
- QC: continuity is both subjective (story feel) and objective (recorded constraint checks).

## 11. Stable Industry Concepts

- Continuity is cross-departmental, not isolated to one role.
- Earlier detection (board/animatic) reduces downstream production cost.
- Continuity requires both structured logs and qualitative review.

## 12. Studio-Specific or Variable Practices

- Continuity checklist templates vary across studios.
- Strictness of temporal/spatial constraints can vary by genre and style.
- Tooling depth (from spreadsheets to integrated trackers) differs by pipeline maturity.

## 13. Research Findings

- Finding: Film grammar educational resources explicitly include shot relation concepts such as 180-degree context relevant to continuity. Source: https://www.khanacademy.org/computing/pixar/storytelling/film-grammar/a/glossary-grammar
- Finding: Storyboarding and story reel practices emphasize iterative feedback and revision before final output, functioning as continuity control stages. Source: https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback and https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/a/glossary-pitch
- Finding: Production tracking systems provide workflow state and review infrastructure needed to maintain continuity records. Source: https://help.autodesk.com/view/SGSUB/ENU/
- Finding: SMPTE material indicates broad standards context and timecode importance for media synchronization references. Source: https://www.smpte.org/time-code and https://www.smpte.org/standards-overview

## 14. Research Principles

- Principle: Continuity should be represented as explicit tracked state across shot transitions.
- Principle: Continuity validation must begin in planning artifacts, not only final outputs.
- Principle: Temporal alignment references (including timecode where needed) improve review traceability.

## 15. Impact on AI Drama System

- Supports dedicated Continuity module/function across storyboard and generation flows.
- Supports structured continuity issue records linked to shot-level provenance.
- Supports QC workflows that combine rule checks and human review.

## 16. Candidate Domain Concepts

- Candidate ContinuityConstraint
- Candidate ContinuityIssue
- Candidate ContinuityReview
- Candidate ContinuityResolution
- Candidate TransitionConstraint

## 17. Candidate Requirements

- CANDIDATE: The system shall track continuity issues at Shot transition boundaries with explicit status.
- CANDIDATE: The system shall support continuity checks on storyboard/animatic artifacts before final generation.
- CANDIDATE: The system shall preserve continuity review provenance (reviewer, timestamp, referenced artifact/version).

## 18. Candidate ADRs

- CANDIDATE ADR: Continuity is implemented as cross-stage service with structured issue tracking, not ad hoc comments only.
- CANDIDATE ADR: Continuity constraints are domain-level and translated into provider/workflow checks by adapters.

## 19. Open Questions

- Which continuity constraints should be machine-checkable in v1 versus human-review only?
- How should continuity severity be modeled for gating decisions?
- What minimal timecode/temporal alignment model is needed for multi-artifact review?

## 20. Sources

- Khan Academy + Pixar, Glossary: Film Grammar, https://www.khanacademy.org/computing/pixar/storytelling/film-grammar/a/glossary-grammar, accessed 2026-07-28, source type: authoritative educational collaboration.
- Khan Academy + Pixar, Pitching and Feedback, https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/v/pitching-feedback, accessed 2026-07-28, source type: authoritative educational collaboration.
- Khan Academy + Pixar, Glossary: Pitching, https://www.khanacademy.org/computing/pixar/storytelling/storyboard-your-film/a/glossary-pitch, accessed 2026-07-28, source type: authoritative educational collaboration.
- Final Draft, Screenplay Formatting and Elements, https://www.finaldraft.com/learn/screenplay-formatting-elements/, accessed 2026-07-28, source type: official software educational documentation.
- Toon Boom Animation, Storyboard Pro 27 Animatic Guidance, https://docs.toonboom.com/help/storyboard-pro-27/storyboard/getting-started/animatic.html, accessed 2026-07-28, source type: official software production documentation.
- Autodesk, Flow Production Tracking Help Center, https://help.autodesk.com/view/SGSUB/ENU/, accessed 2026-07-28, source type: official production tracking documentation.
- SMPTE, Time Code, https://www.smpte.org/time-code, accessed 2026-07-28, source type: standards body overview documentation.
- SMPTE, Standards Overview, https://www.smpte.org/standards-overview, accessed 2026-07-28, source type: standards body overview documentation.
