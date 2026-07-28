# Scene Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for drafting provider-neutral Scene domain baseline; partially blocked for final closure on Scene revision granularity and minimum shared-context inheritance policy.
- ADR Blocker Status: No immediate ADR blocker for publishing this draft; targeted ADR review is likely required before freezing Scene revision semantics, shared-context inheritance policy, and any profile-specific planning metadata commitments.
- Specification Type: Domain Specification
- Domain: Scene
- Version: 1.0
- Evidence Basis:
  - System constraints and invariants from docs/DEVELOPMENT_SPEC.md.
  - Domain boundary constraints from docs/domain/shot.md, docs/domain/storyboard.md, docs/domain/character.md, docs/domain/continuity.md, docs/domain/workflow.md, docs/domain/artifact.md, and docs/domain/qc.md.
  - Cross-layer domain synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md.
  - AI research synthesis from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md.
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md.
  - Supporting production research from docs/research/production/scene-shot-terminology.md, docs/research/production/storyboarding.md, docs/research/production/continuity.md, docs/research/production/cinematography.md, and docs/research/production/animation-production-pipeline.md.
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/domain/shot.md
  - docs/domain/storyboard.md
  - docs/domain/character.md
  - docs/domain/continuity.md
  - docs/domain/workflow.md
  - docs/domain/artifact.md
  - docs/domain/qc.md
- Related Research:
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - docs/research/production/scene-shot-terminology.md
  - docs/research/production/storyboarding.md
  - docs/research/production/continuity.md
  - docs/research/production/cinematography.md
  - docs/research/production/animation-production-pipeline.md
- Related ADRs:
  - docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed)
  - docs/adr/ADR-0002-idempotency-contract.md (Proposed)

Unresolved architecture choices remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

Define the smallest stable, provider-neutral Scene semantics for AI Drama
System.

Scene is needed as a first-class domain concept because production planning,
narrative structure, storyboard context, continuity expectations, and shot-group
coordination all require a stable unit above Shot but below Episode.

Scene is not introduced to replace Shot as execution unit.
Instead, Scene provides shared narrative and production context for an ordered
set of Shots while preserving Shot as the primary production unit for detailed
execution, generation, review, and traceability.

## Domain Definition

A Scene is a narrative and production-planning unit within an Episode that
anchors a coherent time/place/dramatic context and contains an ordered set of
related Shots.

Stable conceptual direction:

Story
-> Episode
-> Scene
-> Shot

Scene meaning in this draft:

- Scene is a context and containment unit.
- Scene is not the primary execution unit for generation.
- Scene organizes shared context that multiple Shots may reference.
- Scene may be visualized, reviewed, revised, and traced through Storyboard,
  Workflow, Artifact, Continuity, and QC relationships without collapsing into
  any of those domains.

## Terminology

- Scene:
  - Narrative and production-planning unit tied to a coherent time/place/
    dramatic context and containing ordered Shots.
- Scene Identity:
  - Stable domain identity of one scene in canonical hierarchy.
- Scene Context:
  - Shared narrative or production context applicable across one or more Shots
    in the scene.
- Scene Intent:
  - Provider-neutral description of what the scene is trying to achieve at a
    narrative and production level.
- Scene Participants:
  - Referenced characters or other relevant entities involved in the scene
    context without redefining their identity.
- Scene Location Context:
  - Shared location or environment context relevant to the scene.
- Scene Time Context:
  - Shared time-of-day, temporal setting, or chronology context relevant to the
    scene.
- Scene Dramatic Objective:
  - Higher-level dramatic purpose or change associated with the scene.
- Scene Revision:
  - Historically traceable revision state of scene-level planning intent.
- Scene-Level Shared Context:
  - Context that Shots may inherit/reference rather than duplicate.
- Shot Override:
  - Deliberate shot-level divergence from inherited scene context.

Term policy:

- These names are conceptual and do not commit class/table/API names.
- This draft does not promote beat, sequence, setup, take, insert, or cutaway
  into canonical hierarchy units.

## Domain Responsibilities

Scene owns or anchors:

- scene identity within canonical hierarchy,
- shared narrative context above Shot,
- shared production context that spans multiple Shots,
- explicit ordered Scene -> Shot containment semantics,
- scene-level references to reusable assets and participants,
- scene-level dramatic objective and contextual framing,
- revision/history of scene-level planning intent,
- provenance linking scene intent to storyboard, workflow, continuity, QC, and
  artifact outputs.

Scene does not own:

- shot-local framing, action, blocking, or detailed cinematography intent,
- provider-specific prompts, embeddings, conditioning, or execution payloads,
- Storyboard lifecycle ownership,
- Continuity state truth,
- Workflow stage or gate semantics,
- Artifact identity or version lineage,
- generation task/attempt/result execution semantics,
- provider runtime or infrastructure behavior.

## Domain Boundaries

Required distinctions:

- Scene != Shot:
  - Scene is a higher-level narrative/planning context; Shot is the primary
    execution and traceability unit.
- Scene != Storyboard:
  - Scene is production-domain context; Storyboard is planning/review
    representation.
- Scene != generated image/video:
  - Scene is intent/context, not produced media payload.
- Scene != provider prompt:
  - prompts may be derived from scene and shot context, but prompt text is not
    scene ontology.
- Scene != workflow stage:
  - Scene is production content context; workflow stages are process semantics.
- Scene != continuity state:
  - Scene may frame continuity scope or expectations, but continuity owns
    tracked temporal state.
- Scene context must not duplicate Character identity truth:
  - Scene references Character/CharacterVersion context; it does not redefine
    identity.
- Scene must not absorb provider/model-specific concepts:
  - model tokens, workflow nodes, embeddings, and similar concepts remain
    outside core ontology.
- keyframes must not replace Shot:
  - auxiliary planning or generation aids do not redefine Scene or Shot.

## Scene / Episode Relationship

Scene relationship to Episode:

- Episode contains ordered Scenes.
- Scene is the immediate canonical child of Episode.
- Scene identity and ordering are explicit within Episode context.

Episode-level context may provide larger narrative arc or sequencing context,
while Scene narrows that into one time/place/dramatic unit.

Boundary rule:

- Scene must not absorb full Episode-level narrative ownership.
- Episode-to-Scene decomposition remains part of canonical hierarchy rather than
  provider/workflow-specific planning.

## Scene / Shot Relationship

Core relationship:

- Scene contains ordered Shots.
- Shot remains the primary production unit.
- Scene provides shared context that Shots reference, inherit, or deliberately
  override.

Evidence-consistent direction:

- Scene groups related beats and shot decisions.
- Shot expresses the detailed visual execution of that scene context.
- One Scene may contain one or many Shots.
- Every Shot belongs to one Scene in canonical hierarchy context.

Boundary rule:

- Scene must not become a surrogate Shot record.
- Shot-local action, framing, and detailed execution remain at Shot scope.

## Shot Ordering

Shot ordering within Scene must be:

- explicit,
- deterministic,
- independent of insertion order,
- historically traceable when reordered in meaningful planning revisions.

Ordering semantics:

- ordering belongs to Scene containment context,
- order changes are deliberate production actions,
- reordering does not collapse Shot identity.

This draft defines ordering semantics only, not implementation mechanism.

## Narrative Context

Scene-level narrative context is the smallest stable shared narrative layer above
Shot.

Stable candidate scene-level narrative concerns:

- scene purpose in story progression,
- dramatic objective or dramatic change,
- shared time/place context,
- shared narrative premise or interaction context,
- major participating characters or entities,
- high-level tension, conflict, or informational purpose,
- scene-level continuity-relevant setup when it spans multiple shots.

Boundary with Shot:

- Scene owns shared context across multiple Shots.
- Shot owns local beat emphasis, local visual action, focal framing, and exact
  execution details.

## Production Context

Scene-level production context may include:

- planned setting or environment context,
- participating asset context,
- scene-wide staging assumptions,
- scene-wide tone or mood references,
- scene-wide constraints relevant to multiple Shots,
- storyboard and workflow references associated with scene planning.

Direction in this draft:

- keep scene context reference-oriented where possible,
- avoid duplicating asset/character/continuity/domain truth inside Scene.

## Location Relationship

Scene may own or reference shared location context because time/place anchoring
is strongly supported by screenplay and planning evidence.

Scene location semantics:

- Scene may reference one primary location context.
- Scene may also reference additional location/environment context when the
  scene legitimately spans subareas or transitions within one narrative unit.

Boundary rule:

- reusable Location identity belongs to Asset domain, not Scene.
- Scene stores contextual linkage or usage, not location truth ownership.

## Character / Participant Relationship

Scene relationship to Character should remain reference-based.

Scene may reference:

- participating Character identities,
- relevant CharacterVersion or appearance context when shared across multiple
  shots,
- scene-level participation importance or presence context.

Scene must not:

- duplicate Character identity truth,
- redefine CharacterVersion boundaries,
- absorb shot-local pose/action/expression state.

Participant interpretation:

- scene-level participant list can indicate who is materially involved in the
  scene context,
- exact visual participation details remain Shot-level when they vary per shot.

## Asset Relationship

Scene relationship to reusable assets should favor references over duplication.

Scene may reference:

- Location,
- Prop,
- Style,
- Voice,
- other reusable creative assets relevant to scene-wide context.

Boundary rule:

- Scene describes scene-specific usage context.
- Asset domain owns reusable asset identity and asset-version semantics.

## Continuity Relationship

Scene relationship to Continuity:

- Scene may frame a continuity span or contextual envelope across multiple
  Shots.
- Continuity domain owns expected/observed temporal state and issue tracking.
- Scene may provide shared context used by continuity review, but Scene is not
  continuity state truth.

Important distinction:

- scene-level time/place/participant context may inform continuity,
- cross-shot state tracking, discrepancy, and resolution belong to Continuity.

## Storyboard Relationship

Scene relationship to Storyboard:

- Storyboard visualizes scene intent through ordered panels and planning
  artifacts.
- Storyboard may organize or represent scene-to-shot decomposition.
- Scene remains production-domain context independent of storyboard lifecycle.

Boundary rule:

- Scene != Storyboard.
- Scene != Storyboard Panel.
- storyboard revisions do not automatically redefine Scene identity.

## Workflow Relationship

Scene relationship to Workflow:

- workflows may operate at Scene scope, Shot scope, or broader scopes depending
  on production profile.
- workflow input context may include scene intent, scene ordering context,
  scene participant context, and scene-level asset references.
- Scene is not a workflow stage or workflow state machine.

Boundary rule:

- Workflow owns process/gate/run semantics.
- Scene owns content/planning context.

## QC Relationship

Scene relationship to QC:

- QC may evaluate scene-level concerns such as narrative coherence, shot
  coverage, pacing at storyboard/animatic level, participant consistency across
  shots, or scene-level continuity concerns.
- Scene may be a QC target for planning-level review.
- concrete media-quality checks usually still attach to exact ArtifactVersion or
  Shot-level outputs rather than to Scene alone.

Boundary rule:

- QC owns evaluation, findings, issues, and decisions.
- Scene provides target context and provenance linkage.

## Generation Relationship

Scene relationship to generation is contextual rather than execution-centric.

Conceptual chain preserved:

Story
-> Episode
-> Scene
-> Shot
-> PromptInstance
-> GenerationTask
-> GenerationAttempt
-> GenerationResult
-> Artifact

Scene may influence:

- structured planning context,
- shot decomposition,
- participant and location context,
- continuity-relevant shared context.

Scene must not own:

- provider execution logic,
- prompts as core ontology,
- task/attempt/result semantics.

## Revision / Versioning

Scene-level revisions should preserve historical planning intent when changes
materially affect downstream planning, storyboarding, continuity, or generation.

Conservative draft direction:

- Scene identity remains stable across normal planning revisions.
- scene-level intent changes should be historically traceable.
- approved historical scene planning state must not be silently overwritten when
  materially changed.

Open policy boundary:

- this draft does not require full SceneVersion architecture.
- versioning may be lightweight at first if traceability is preserved.

## Inheritance / Override Semantics

Scene-level shared context may be inherited or referenced by Shots when it is
stable across multiple shots.

Examples of likely inheritable/reference context:

- location context,
- time-of-day or shared temporal setting,
- shared participant set,
- scene-level dramatic objective,
- scene-wide environment assumptions,
- scene-wide continuity-relevant setup.

Rules:

- inherited context should be referenced rather than copied when practical.
- Shot may intentionally override Scene-level context.
- override must be explicit and historically traceable where it materially
  affects continuity, planning, or reproducibility.
- Shot override does not invalidate Scene identity; it narrows or diverges from
  shared context for that shot.

## Provenance

Scene provenance should support:

- linkage from Story/Episode context to Scene intent,
- linkage from Scene to ordered Shots,
- linkage from Scene planning context to Storyboard revisions,
- linkage from Scene context to WorkflowRun inputs where applicable,
- linkage from Scene context to continuity review context,
- linkage from Scene context to generated artifacts through Shot and workflow
  provenance chains,
- historical traceability of scene revisions and overrides.

Boundary rule:

- Scene provenance is production-domain traceability, not operational telemetry.

## Validation / Invariants

Evidence-supported candidate invariants:

- Scene and Shot are distinct domain concepts.
- Shot remains the primary production unit.
- Scene identity remains separate from Storyboard, Workflow, Continuity,
  Artifact, and provider execution identifiers.
- Scene contains explicitly ordered Shots.
- Scene-level context must not duplicate Character identity truth.
- Scene-level production intent remains provider-neutral.
- Historical scene planning changes must remain traceable when materially
  changed.
- keyframes or other auxiliary generation aids do not replace Shot.

## Candidate Information Model

Conceptual only.

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| scene_id | Stable scene identity anchor | CORE DOMAIN | Yes | Canonical hierarchy identity; not provider/runtime identity. |
| scene_code | Human-readable scene identifier | CORE DOMAIN | Usually | Must not replace machine identity. |
| parent_episode_ref | Episode containment reference | REFERENCE | Yes | Preserves canonical hierarchy. |
| scene_order | Explicit ordering within Episode | CORE DOMAIN | Yes | Deterministic ordering; not insertion-order dependent. |
| scene_purpose | Shared narrative purpose | CORE DOMAIN | Usually | Why this scene exists in progression. |
| dramatic_objective | Higher-level dramatic aim/change | CORE DOMAIN | No | Keep lightweight and provider-neutral. |
| time_context_ref | Shared temporal setting/context | REFERENCE | No | Time-of-day or chronology context. |
| location_context_ref | Shared location/environment reference | REFERENCE | No | Location identity belongs outside Scene. |
| participant_refs | Participating character/entity references | REFERENCE | No | Must not duplicate character truth. |
| asset_context_refs | Shared asset usage references | REFERENCE | No | Props, styles, voices, environment assets. |
| scene_constraint_notes | Shared production constraints | CORE DOMAIN | No | Use only when stable across multiple shots. |
| shot_refs | Ordered shot membership | CORE DOMAIN | Yes | Scene contains ordered Shots. |
| storyboard_refs | Linked storyboard/revision references | REFERENCE | No | Scene != Storyboard. |
| workflow_context_refs | Workflow linkage context | WORKFLOW CONCERN | No | Scene may inform workflow, not own it. |
| qc_context_refs | QC linkage context | REFERENCE | No | Scene may be target or shared context for QC. |
| continuity_context_refs | Continuity linkage context | REFERENCE | No | Scene may frame span; does not own continuity truth. |
| revision_context | Historical planning revision linkage | VERSIONED DOMAIN | No | Lightweight traceability without forcing full SceneVersion entity. |
| provenance_context | Scene-level traceability context | CORE DOMAIN | Yes | Supports reproducibility and review history. |
| beat_or_sequence_tags | Optional planning-scale labels | OPEN QUESTION | No | Must not replace canonical hierarchy. |

## Candidate Requirements

Classification policy in this section:

- ACCEPT INTO DRAFT SPEC: accepted only into this draft scope.
- KEEP AS CANDIDATE: evidence supports direction but architecture is not yet
  frozen.
- DEFER: not blocking this draft.
- REJECT FOR CORE DOMAIN: excluded from core Scene semantics.

Requirement set:

- CR-SCENE-001: Preserve separate Scene and Shot concepts in canonical
  Story -> Episode -> Scene -> Shot hierarchy.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: strong cross-layer and production evidence.

- CR-SCENE-002: Keep Shot as the primary production unit while using Scene as
  shared narrative and production context.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: domain foundation synthesis and shot specification.

- CR-SCENE-003: Represent Scene as time/place/dramatic-context unit with
  ordered Shots.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: screenplay and film-grammar terminology research.

- CR-SCENE-004: Support explicit shot ordering within each Scene.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: production planning and shot specification evidence.

- CR-SCENE-005: Prefer references to reusable assets and characters over
  duplicated embedded truth in Scene.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: asset-centric architecture and character-boundary rules.

- CR-SCENE-006: Allow scene-level shared context inheritance with explicit
  shot-level override capability.
  - Classification: KEEP AS CANDIDATE
  - Basis: strong planning logic, but final inheritance policy remains open.

- CR-SCENE-007: Support optional beat/sequence annotations without changing the
  canonical hierarchy.
  - Classification: KEEP AS CANDIDATE
  - Basis: terminology research supports them as planning labels, not canonical
    units.

- CR-SCENE-008: Require full SceneVersion architecture in v1.
  - Classification: DEFER
  - Basis: historical traceability is required, but full versioning policy is
    not yet proven necessary for v1.

- CR-SCENE-009: Store provider prompts, embeddings, or workflow payloads as core
  Scene ontology.
  - Classification: REJECT FOR CORE DOMAIN
  - Basis: provider-neutral boundary constraints.

## ADR Review Points

Potential architecture decisions likely to require ADR review:

- whether Scene requires explicit version entity or lighter revision history,
- canonical inheritance versus reference resolution policy for scene-to-shot
  shared context,
- minimum mandatory scene-level context set across production profiles,
- optional beat/sequence planning labels and normalization policy,
- cross-domain override provenance requirements when Shot diverges from Scene.

No ADR is created or accepted by this document.

## Open Questions

- What minimum scene-level context is mandatory across all production profiles?
- When does a material scene revision require formal versioning rather than
  simple revision trace?
- Which scene-level context should be inherited by reference versus resolved at
  shot scope?
- How should scene-level context interact with scenes that intentionally change
  location or time within one dramatic unit?
- How should optional beat/sequence labels be normalized without becoming
  canonical hierarchy replacements?
- What provenance is minimally required when storyboard and shot planning evolve
  asynchronously from scene text?
- How should scene-level QC and continuity references attach when one scene has
  many shots and partial rework?

## Out of Scope

Explicitly out of scope in this document:

- Django models
- database schema
- serializers
- REST API
- provider prompt design
- generation workflow implementation
- QC algorithms
- continuity algorithm implementation
- storage implementation
- provider/model selection
- keyframe domain redesign
- final lifecycle state machine

## Traceability

Status interpretation rule preserved:

- Research Finding != Candidate Requirement
- Candidate Requirement != Proposed ADR
- Proposed ADR != Accepted ADR
- Accepted ADR != Implementation

| Candidate decision / boundary | Evidence source | Evidence status |
|---|---|---|
| Scene and Shot remain distinct concepts | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (CLA-001); docs/research/production/scene-shot-terminology.md | Strong candidate-level support |
| Shot remains the primary production unit | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (CLA-002); docs/domain/shot.md | Existing specification + strong support |
| Scene is a time/place narrative unit above Shot | docs/research/production/scene-shot-terminology.md; docs/DEVELOPMENT_SPEC.md hierarchy | Strong research support |
| Scene should provide shared context while detailed execution remains at Shot | docs/domain/shot.md; docs/research/production/storyboarding.md; docs/research/production/cinematography.md | Existing specification + candidate-level support |
| Scene should reference characters/assets without duplicating identity truth | docs/domain/character.md; docs/domain/artifact.md asset boundary; docs/DEVELOPMENT_SPEC.md asset-centric principle | Existing specification + strong support |
| Scene relates to continuity as context/span but does not own continuity truth | docs/domain/continuity.md; docs/research/production/continuity.md | Existing specification + candidate-level support |
| Scene relates to storyboard as source planning context but remains distinct from storyboard lifecycle | docs/domain/storyboard.md; docs/research/production/storyboarding.md | Existing specification + strong support |
| Scene can inform workflow and QC without becoming workflow stage or QC record | docs/domain/workflow.md; docs/domain/qc.md; docs/research/production/animation-production-pipeline.md | Existing specification + candidate-level support |
| ADR-0001 and ADR-0002 remain Proposed surrounding context only | docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed); docs/adr/ADR-0002-idempotency-contract.md (Proposed) | Proposed ADR status only |

Status progression for architecture closure:

Research
-> Proposed ADR
-> Accepted ADR
-> Implementation

## Specification Readiness

Stable in this draft:

- Scene as distinct canonical domain concept above Shot.
- Scene as shared time/place/dramatic-context unit.
- explicit Scene -> Shot containment and shot ordering semantics.
- reference-oriented links to characters, assets, continuity, storyboard,
  workflow, QC, and artifacts.
- provider-neutral production intent boundary.
- Shot remains the primary production unit.

Ambiguous or unresolved:

- minimum mandatory scene-context set across production profiles,
- exact inheritance versus explicit reference-resolution policy,
- formal SceneVersion versus lighter revision-trace policy,
- optional beat/sequence tagging normalization,
- scene-level handling of intra-scene location/time shifts.

Research blocking determination:

- no additional research is required to publish this draft.
- Scene is research-unblocked for downstream domain modeling.

Likely ADR-needed before implementation freeze:

- scene revision/versioning policy,
- inheritance/override policy between Scene and Shot,
- minimum mandatory scene-context contract by production profile,
- optional planning-label normalization policy if made product-wide.

## Layer 4 Research Requests

Current determination:

- no new blocking Layer 4 research request is required for this draft.

Potential future non-blocking topics only if implementation scope demands them:

- scene revision/versioning patterns in production-tracking systems,
- screenplay-to-scene structured metadata normalization across writing tools,
- cross-discipline terminology normalization for setup/take/insert/cutaway.
