# Storyboard Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for downstream domain specification (based on current Layer 1 and Layer 3 synthesis evidence)
- ADR Blocker Status: No immediate ADR blocker for this draft scope; selected policy gates may require future ADR review
- Specification Type: Domain Specification
- Domain: Storyboard
- Version: 1.0
- Evidence Basis:
  - Development constraints from docs/DEVELOPMENT_SPEC.md
  - Shot domain boundaries from docs/domain/shot.md
  - Cross-layer synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - AI research synthesis from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - Production record: docs/research/production/storyboarding.md
  - AI paper record: docs/research/ai-papers/RL-AI-BOARD-001-story2board.md
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/domain/shot.md
- Related ADRs:
  - No accepted ADR files were found under docs/adr/ in the current repository state.

Unresolved architectural decisions remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

This specification defines the provider-independent domain meaning, boundaries,
relationships, lifecycle, and conceptual information model for Storyboard in AI
Drama System.

This specification answers: What is Storyboard in AI Drama System and how does it
relate to Shot, panel planning, review, continuity, generation, and provenance?

This specification does not define Django models, SQL schemas, serializers,
APIs, or provider-specific generation methods.

## Domain Definition

Storyboard is a first-class production planning and review construct that
visualizes and iterates Shot-associated production intent before and across
generation stages.

Storyboard captures ordered visual planning representations (panels), contextual
annotations, review outcomes, and revision history.

Storyboard is not equivalent to Shot and is not equivalent to generated image
artifacts.

## Terminology

- Storyboard:
  - A lifecycle-managed planning and review construct associated with scene/shot
    production intent.
- Storyboard Panel:
  - An ordered visual planning representation associated with Shot intent.
- Storyboard Revision:
  - A historically traceable revision state of a storyboard and its panel set.
- Story Reel / Animatic:
  - A time-aware previsualization output derived from storyboard context;
    this may include audio/timing overlays and remains distinct from final
    production deliverables.
- Shot:
  - Canonical production unit in Project -> Story -> Episode -> Scene -> Shot.
- Keyframe / Anchor:
  - Workflow/generation aids that do not replace Shot and do not redefine
    Storyboard as provider-specific execution state.
- Artifact:
  - Generated or imported output with provenance; may visualize storyboard
    panels but is not identical to panel identity.

## Domain Responsibilities

Storyboard owns or anchors:

- Visual planning representation for scene/shot intent.
- Ordered panel sequencing for previsualization.
- Panel-level annotations relevant to storytelling and shot planning.
- Iterative review, feedback, and approval records.
- Revision history and historical planning traceability.
- Linkage between planning intent and downstream generation/review contexts.
- Optional derivation support for story reel/animatic planning outputs.

## Domain Boundaries

Storyboard does not own as core domain truth:

- Canonical Shot identity and Shot domain semantics.
- Provider execution payloads, workflow JSON, prompt embeddings, model tokens,
  or generation runtime internals.
- Generated binary image/video payloads themselves.
- Final editorial delivery structures as production truth.

Boundary rule:

- Storyboard represents planning/review state and visual intent articulation.
- Workflow/adapters translate selected storyboard context into provider-specific
  execution representations.

## Storyboard / Shot Relationship

Core distinction:

- Shot = canonical production intent and execution traceability unit.
- Storyboard = planning + visualization + review representation associated with
  Shot intent.

Rules:

- Storyboard must not replace Shot in canonical hierarchy.
- Storyboard panel identity must not be used as Shot identity.
- A storyboard may represent one or more shots depending on planning scope.
- A shot may be represented by zero, one, or multiple storyboard panels.
- A panel should have one primary shot association as the v1 conceptual
  direction.
- Whether one panel may intentionally represent multiple shots remains an open
  question and is not accepted as default v1 capability in this draft.
- Shot remains primary for generation-chain traceability
  (Shot -> PromptInstance -> GenerationTask -> GenerationAttempt ->
  GenerationResult -> Artifact).

## Storyboard Panel

Storyboard Panel is an ordered planning representation, not a binary image file.

Panel responsibilities include:

- Visualizing intended framing/composition/action context.
- Capturing planning annotations and review notes.
- Linking to one primary relevant shot-intent context.

Panel constraints:

- Panel does not redefine Shot boundaries.
- Panel does not become equivalent to generated artifact payload.
- Multiple visualization artifacts may correspond to one panel across revisions.

## Panel Ordering

Panel ordering requirements:

- Ordering must be explicit and deterministic within a storyboard revision.
- Ordering must not depend on insertion order.
- Reordering is a deliberate production action and should preserve revision
  provenance where required.

Cross-scope notes:

- Ordering semantics may apply within Scene context and/or storyboard segment
  context without redefining canonical hierarchy.

## Panel Annotations

Storyboard panel annotations should support provider-neutral planning context,
such as:

- Narrative beat intent
- Action intent notes
- Composition/framing notes
- Camera movement intent notes
- Character/asset placement notes
- Continuity concerns or transition notes
- Dialogue/audio placeholder notes
- Review comments and change requests

Annotation policy:

- Qualitative planning semantics are primary.
- Numeric details may appear when useful, but numeric provider parameters are
  not required as core storyboard ontology.

## Cinematography Relationship

Storyboard should visualize and communicate cinematography intent associated with
Shot planning, including:

- Shot size/framing intent
- Angle and screen-direction intent
- Composition and staging intent
- Optional movement/pacing intent

Cinematography domain boundary:

- Storyboard captures planning/review representation of intent.
- Shot retains canonical intent ownership.
- Provider-specific camera controls remain adapter/workflow concerns.

## Character / Asset Relationship

Storyboard should reference relevant production identities where available:

- Character identity references
- Location references
- Prop references
- Style references

Rules:

- Storyboard references should align with Character/Asset identity boundaries.
- Provider-specific embeddings/features are not storyboard core domain concepts.
- Storyboard may capture appearance/context notes without redefining Character
  identity/version architecture.

## Continuity Relationship

Storyboard participates in continuity planning and review by:

- Recording continuity-sensitive transitions between adjacent planned shots/panels.
- Capturing continuity issues identified during storyboard review.
- Linking continuity observations to shot-level continuity context where relevant.

Continuity boundary:

- Storyboard supports continuity representation.
- Full continuity state machine/service remains a separate domain concern.

## Revision / Versioning

Storyboard revisions must preserve historical planning state:

- Revision changes must be traceable (panel additions, replacements, reorder,
  annotation updates, approval changes).
- Approved historical planning states must not be silently overwritten.
- Revision history should remain inspectable for reproducibility and review audit.

Revision relations:

- Storyboard revisions may reflect Shot-intent revisions but are not always
  one-to-one with shot revisions.
- Panel replacement is revisioned planning change, not artifact overwrite.

## Review / Approval

Storyboard review should support explicit human-in-the-loop evaluation:

- Drafting
- Review feedback
- Revision
- Approval / Re-approval when materially changed

Approval semantics:

- Approval pertains to planning/review suitability, not final render quality.
- Profile-specific policy may decide whether storyboard approval gates certain
  downstream generation steps.
- Gating policy is configuration/policy, not intrinsic storyboard ontology.

## Generation Relationship

Storyboard-to-generation relationship:

- Storyboard informs prompt/planning and workflow context.
- Storyboard may be used to derive or constrain generation plans.
- Storyboard panels may have associated visualization artifacts used in review.

Boundary:

- Storyboard does not own provider execution logic.
- Storyboard does not define model/provider selection.
- Paper-specific methods (for example LPA/RAVM/training-free workflow details)
  remain technology candidates and are not core Storyboard architecture.

## Keyframes / Anchors

Keyframes/anchors may appear as planning or workflow aids related to storyboard
activities.

Rules:

- Keyframes/anchors must not replace Shot as canonical production unit.
- Keyframes/anchors must not redefine storyboard core meaning.
- Keyframes/anchors are workflow/artifact-level adjuncts unless separately
  specified and accepted.

## Lifecycle

Candidate storyboard lifecycle vocabulary (conceptual):

- Draft
- In Review
- Revision Requested
- Revised
- Approved
- Superseded

Lifecycle status in this draft:

- Conceptual lifecycle vocabulary: accepted into this draft scope.
- Formal state machine transitions and mandatory gate policy: open question,
  may require ADR depending on production profile policy scope.

## Provenance

Storyboard provenance should support:

- Who changed what and when for panel/revision/review states.
- Linkage from storyboard planning context to associated shot intent context.
- Linkage from panel visualization representations to artifact records.
- Traceability for approval and revision history.

Provenance boundary:

- Detailed global provenance data model remains under future Artifact &
  Provenance specification scope.

## Validation / Invariants

Domain invariants supported by current evidence:

- Scene, Shot, Storyboard, and Storyboard Panel are distinct concepts.
- Storyboard Panel is not equivalent to Shot.
- Storyboard Panel is not equivalent to generated binary artifact payload.
- One Shot may be represented by zero, one, or multiple Storyboard Panels.
- Panel ordering is explicit and deterministic within a revision scope.
- Storyboard revisions preserve historical planning state.
- Storyboard review/approval state is explicit when review workflow is active.
- Keyframes/anchors may assist planning/generation but do not replace Shot.

## Candidate Information Model

This is conceptual only (not Django schema).

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| storyboard_id | Stable storyboard identity | CORE DOMAIN | Yes | Stable identity independent from panel/artifact IDs. |
| storyboard_scope_ref | Planning scope linkage (scene/shot context) | REFERENCE | Yes | Scope expression must not redefine canonical hierarchy. |
| storyboard_status | Planning/review lifecycle state | CORE DOMAIN | Yes | Conceptual state vocabulary in this draft. |
| storyboard_revision_ref | Current revision linkage | REFERENCE | Yes | Revision history must remain inspectable. |
| storyboard_revision_history | Historical revision lineage | CORE DOMAIN | Yes | Supports traceability and non-destructive change management. |
| panel_id | Stable panel identity | CORE DOMAIN | Yes | Distinct from artifact identity. |
| panel_order | Deterministic order within revision | CORE DOMAIN | Yes | Explicit ordering required. |
| panel_primary_shot_ref | Primary association to one shot intent context | REFERENCE | Usually | Preferred v1 conceptual direction for panel-to-shot association. |
| panel_secondary_shot_refs | Additional shot associations | REFERENCE | No | Optional and unresolved; one-panel-to-multiple-shots remains open question in this draft. |
| panel_annotations | Planning and review annotations | CORE DOMAIN | Yes | Provider-neutral representation. |
| panel_visualization_refs | Links to visualization artifacts | REFERENCE | No | Artifact payloads remain external to panel identity. |
| cinematography_notes | Panel-level cinematography planning context | OPTIONAL DOMAIN | No | Represents visualization of shot intent, not provider controls. |
| character_asset_refs | Character/location/prop/style references | REFERENCE | No | Supports planning consistency. |
| continuity_notes | Continuity observations/constraints | OPTIONAL DOMAIN | No | Full continuity domain remains separate. |
| review_feedback_items | Structured review feedback linkage | REFERENCE | No | Human review provenance. |
| approval_context | Approval/rejection status context | DERIVED/REFERENCE | No | Policy-driven gating possible by profile. |
| generation_context_links | Linkage to planning/prompt/task contexts | REFERENCE | No | Supports planning-to-execution traceability. |
| provenance_context | Change/actor/timestamp context | CORE DOMAIN | Yes | Detailed global model deferred. |

## Candidate Requirements

- CANDIDATE: Model Storyboard as first-class planning/review stage, not only as
  generated image output.
- CANDIDATE: Preserve explicit distinction among Shot, Storyboard, and
  Storyboard Panel.
- CANDIDATE: Support zero/one/multiple panels per shot based on production
  context, without enforcing one global cardinality rule.
- CANDIDATE: Preserve storyboard revision lineage and approval history without
  destructive overwrite of approved historical planning state.
- CANDIDATE: Keep panel identity separate from generated artifact identity.
- CANDIDATE: Support storyboard-level multi-dimensional QC concepts
  (for example narrative alignment, composition diversity,
  character consistency, continuity, cinematography intent alignment).
- CANDIDATE: Keep provider/model/method-specific mechanisms outside core
  storyboard ontology.

## ADR Review Points

Potential future ADR review points (not accepted here):

- Whether storyboard approval is mandatory generation gate for specific
  production profiles.
- Whether a standardized storyboard lifecycle state machine and gate policy
  should be enforced globally versus profile-specific configuration.
- Whether canonical minimum storyboard metadata is required before certain
  downstream workflow transitions.

No ADR is created or accepted in this specification.

## Open Questions

- What minimum storyboard metadata set is required before selected downstream
  generation stages can begin?
- Should storyboard gating be mandatory for some profiles and optional for
  others, and where should that policy live?
- What storyboard-to-shot cardinality patterns should be recommended as default
  conventions per production profile?
- Should one panel ever intentionally represent multiple shots, and if so,
  under what constrained planning scenarios without weakening Shot boundaries?
- Which storyboard-level QC dimensions should be required in early milestones,
  and which remain advisory?
- How should story reel/animatic semantics be formally partitioned relative to
  storyboard core domain versus editorial/timeline domains?

## Out of Scope

Explicitly out of scope in this document:

- Django models, serializers, migrations, and SQL schemas.
- API contracts and implementation details.
- Provider/model selection or workflow engine execution internals.
- Adoption of paper-specific methods such as LPA, RAVM, or training-free
  generation as architecture requirements.
- Final QC algorithms, metric thresholds, and scoring implementations.
- Timeline/editorial final domain design.
- Acceptance of architecture decisions through ADRs.

## Traceability

| Specification Decision / Candidate | Evidence Source | Evidence Status |
|---|---|---|
| Storyboard is first-class planning/review stage | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (CLA-003); docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md finding 2; docs/research/production/storyboarding.md principles | Strong candidate-level support |
| Shot remains canonical production unit; storyboard does not replace Shot | docs/domain/shot.md; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (CLA-002, D-001) | Strong support |
| Primary one-panel-to-one-shot association is preferred v1 conceptual direction; one-panel-to-multiple-shots remains open | docs/domain/shot.md (Shot as canonical unit); docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (CLA-002, D-004); docs/research/production/storyboarding.md | Candidate-level direction; insufficient evidence for accepted invariant |
| Storyboard panel is distinct from generated artifact | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (D-004); docs/research/production/storyboarding.md | Moderate to strong support |
| Storyboard revision/review provenance must be explicit | docs/research/production/storyboarding.md; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md findings 2 and 6 | Strong candidate-level support |
| Storyboard-level QC should be multi-dimensional | docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md (RP-BOARD-001, REQ-QC-001 candidate); docs/research/ai-papers/RL-AI-BOARD-001-story2board.md | Strong candidate-level support |
| Paper-specific storyboard generation mechanisms remain technology candidates | docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md section 4.3; docs/research/ai-papers/RL-AI-BOARD-001-story2board.md sections 6 and 13; AGENTS.md research interpretation rules | Strong governance support |

## Specification Readiness

Sufficiently defined in this draft:

- Storyboard meaning, boundary, and distinction from Shot, panel, and artifact.
- Storyboard lifecycle/revision/review concepts at conceptual level.
- Planning relationships to Shot, continuity, generation, and provenance.
- Cardinality framing at conceptual level:
  - zero/one/multiple Panels per Shot
  - one primary Shot association per Panel as the preferred v1 direction
  - multi-Shot Panel remains unresolved

Partially defined / deferred:

- Formal global lifecycle state machine and mandatory generation-gate policy.
- Minimum required storyboard metadata by production profile.
- QC dimension requirements and enforcement policy per milestone/profile.
- Detailed provenance and timeline/editorial integration schema.

Research blocker determination for this draft:

- Storyboard domain draft is research-unblocked for downstream specification work
  at conceptual level.
- Remaining blockers are primarily policy/architecture finalization and detailed
  implementation contracts, not absence of baseline research evidence.

ADR blocker determination for this draft:

- No immediate ADR blocker for publishing this draft.
- Future ADR review may be needed for cross-profile mandatory gating/lifecycle
  policy standardization.

## Layer 4 Research Requests

Current determination:

- No new mandatory Layer 4 research request is introduced by this draft as a
  blocker for conceptual Storyboard domain definition.

Potential future Layer 4 candidate research topics (non-blocking):

- Interchange contract for storyboard-to-editorial exchange semantics when
  timeline/editorial specification reaches implementation-depth interoperability.
- Cross-tool storyboard review/provenance interoperability contract for
  production tracking integrations.

These are potential follow-on architecture/interoperability topics and are not
required to accept this Storyboard draft specification.
