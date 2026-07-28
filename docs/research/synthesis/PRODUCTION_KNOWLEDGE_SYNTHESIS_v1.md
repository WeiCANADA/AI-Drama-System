# Production Knowledge Synthesis v1

## Scope

This synthesis summarizes Layer 3 production knowledge records and translates evidence into research principles, candidate requirements, and candidate ADRs.

Status policy:
- This document contains research synthesis and candidate implications only.
- It does not define accepted architecture or accepted requirements.

Covered records:
- RL-PROD-SHOT-001 Scene / Shot Terminology
- RL-PROD-BOARD-001 Storyboarding
- RL-PROD-CHAR-001 Character Bible / Character Design References
- RL-PROD-CONT-001 Continuity
- RL-PROD-CINE-001 Cinematography
- RL-PROD-PIPE-001 Animation Production Pipeline

## Evidence Labels

- STRONG PRODUCTION EVIDENCE: directly supported by multiple authoritative production references in this layer.
- MODERATE PRODUCTION EVIDENCE: supported but narrower, often from limited open sources.
- DISCIPLINE-SPECIFIC: valid in one discipline context and may not be universal.
- STUDIO-SPECIFIC: heavily influenced by specific tooling or studio process.
- OPEN QUESTION: unresolved in current evidence set.

## Synthesis Findings

1. Canonical Scene/Shot separation is strongly supported.
- Evidence label: STRONG PRODUCTION EVIDENCE
- Basis: screenplay scene structuring and film grammar shot distinctions (Final Draft + Khan/Pixar).
- Implication: preserve Story -> Episode -> Scene -> Shot hierarchy without replacement.

2. Storyboarding is a first-class iterative planning and review stage.
- Evidence label: STRONG PRODUCTION EVIDENCE
- Basis: Pixar/Khan storyboarding feedback loops and Toon Boom timing/camera workflows.
- Implication: storyboard lifecycle and review provenance should be represented explicitly.

3. Character consistency should include narrative and visual dimensions.
- Evidence label: MODERATE PRODUCTION EVIDENCE
- Basis: educational story/board references plus tracking/versioning practice.
- Implication: character identity/version separation is a reasonable candidate direction.

4. Continuity should be explicit cross-stage tracked state.
- Evidence label: MODERATE PRODUCTION EVIDENCE
- Basis: storyboard/animatic review loops, film grammar continuity cues, production tracking workflows.
- Implication: continuity issue tracking at shot transition level is a candidate requirement.

5. Cinematography intent and technical parameters should be separated.
- Evidence label: STRONG PRODUCTION EVIDENCE
- Basis: camera grammar intent + official camera control semantics (Blender docs).
- Implication: provider-agnostic shot camera intent with adapter-level parameter mapping.

6. Production pipelines are stage-based with iterative rework and versioned approvals.
- Evidence label: STRONG PRODUCTION EVIDENCE
- Basis: production tracking documentation and previsualization practice references.
- Implication: explicit stage states, review gates, and provenance are candidate architecture constraints.

7. Tool terminology requires careful normalization.
- Evidence label: STUDIO-SPECIFIC
- Basis: Toon Boom and tracking tool vocabularies are practical but not universal ontology.
- Implication: software-specific terms should remain adapter/metadata level unless cross-validated.

8. Timecode/synchronization references are important but underspecified for domain schema.
- Evidence label: OPEN QUESTION
- Basis: SMPTE overview resources provide context, but not a full schema mapping for this system yet.
- Implication: defer strict temporal schema decisions pending deeper standards-level research.

## Cross-Record Principles

- Principle A: Preserve canonical production hierarchy and keep Shot as primary execution unit.
- Principle B: Represent planning artifacts (especially storyboard and story reel) as lifecycle-managed records, not disposable intermediate files.
- Principle C: Separate production intent from provider/workflow execution detail.
- Principle D: Treat continuity and review as explicit tracked processes with provenance.
- Principle E: Distinguish universal concepts from discipline-specific and studio-specific conventions.

## Candidate Requirements (Consolidated)

- CANDIDATE: Keep Scene and Shot as distinct domain concepts and preserve canonical hierarchy.
- CANDIDATE: Model storyboard lifecycle states, revisions, feedback, and approvals.
- CANDIDATE: Track continuity issues at shot transition boundaries with structured status and provenance.
- CANDIDATE: Attach cinematography intent to Shot entities using provider-agnostic vocabulary.
- CANDIDATE: Separate Character identity from CharacterVersion and maintain continuity-ready references.
- CANDIDATE: Represent stage-based pipeline state with explicit review gates and historical rework visibility.
- CANDIDATE: Preserve workflow and artifact provenance sufficient for debugging and reproducibility claims.

## Candidate ADRs (Consolidated)

- CANDIDATE ADR: Canonical hierarchy remains fixed; auxiliary terminology (sequence, beat, setup, take) is metadata/tagging only.
- CANDIDATE ADR: Storyboard is treated as a first-class planning/review stage for selected project profiles.
- CANDIDATE ADR: Continuity is implemented as cross-stage service with structured issue management.
- CANDIDATE ADR: Domain stores provider-agnostic camera/production intent; adapters perform provider-specific translation.
- CANDIDATE ADR: Pipeline lifecycle is stage-gated with explicit version/review provenance.

## Risks and Limits

- Openly accessible sources underrepresent studio-internal templates (especially character bible schema and continuity sheets).
- Some terminology appears in educational contexts and should not be treated as strict universal standards without additional guild/standard references.
- Tool documentation is operationally useful but can encode product-specific assumptions.

## Open Questions

- OPEN QUESTION: What authoritative guild-level references should be added for take/setup/master shot/insert/cutaway normalization?
- OPEN QUESTION: Which storyboard metadata fields are minimum-required before shot generation tasks can start?
- OPEN QUESTION: What continuity constraints should be machine-checkable in initial milestones?
- OPEN QUESTION: What minimum cross-provider temporal/sync schema is needed for reproducible editorial alignment?
- OPEN QUESTION: Which stage gates are mandatory for different production profiles (short-form, episodic, feature-like)?

## Recommended Next Research Increments

- Add one standards/guild-focused terminology record for camera and set language.
- Add one dedicated continuity form/schema comparison record across at least two production documentation sources.
- Add one production tracking schema mapping record that compares two tools and extracts neutral domain terms.

## Source Coverage (Layer 3)

Primary source families used:
- Final Draft screenplay/structure guidance
- Khan Academy + Pixar storytelling and storyboard education
- Toon Boom Storyboard Pro official documentation
- Blender official camera documentation
- Autodesk Flow Production Tracking help documentation
- SMPTE standards/timecode overview pages

Coverage note:
- This synthesis is sufficient for candidate-level domain grounding.
- Additional primary references are still needed before freezing production-domain specifications.
