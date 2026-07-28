# PR-0001 Planning Domain Slice

## Status

- Status: Draft implementation plan
- Readiness: READY FOR IMPLEMENTATION
- Slice Type: Planning-domain implementation slice
- Scope Discipline:
  - no code in this document
  - no ADR creation
  - no modification to domain specifications

## Purpose

Define the smallest coherent implementation slice for:

Scene
-> Shot
-> Storyboard
-> StoryboardPanel

This slice converts the most stable current draft-domain semantics into a
reviewable implementation scope without introducing unresolved generation,
continuity, QC, or provider/runtime architecture.

The slice is intentionally planning-oriented.
It preserves Shot as the primary production unit while implementing Scene and
Storyboard as upstream planning and organization concepts.

## Source Specifications

Primary sources for this plan:

- docs/DEVELOPMENT_SPEC.md
- docs/reviews/CORE_DOMAIN_READINESS_REVIEW_v1.md
- docs/reviews/CORE_DOMAIN_READINESS_DELTA_REVIEW_v1.md
- docs/domain/scene.md
- docs/domain/shot.md
- docs/domain/storyboard.md
- docs/domain/character.md
- docs/domain/artifact.md

Planning conclusions adopted from reviewed specifications only:

- canonical hierarchy remains Project -> Story -> Episode -> Scene -> Shot
- Shot remains the primary production unit
- Scene contains ordered Shots
- a Shot may have zero, one, or multiple StoryboardPanels
- StoryboardPanel should prefer one primary Shot association
- one Panel representing multiple Shots remains unresolved and is excluded from
  PR-0001
- ordering must be explicit
- UUID identity remains primary direction
- human-readable codes remain separate from primary keys

## Scope

Included in PR-0001:

- Scene domain persistence and basic validation
- Shot domain persistence and basic validation
- Storyboard domain persistence and basic validation
- StoryboardPanel domain persistence and basic validation
- explicit Scene -> Shot ordering
- explicit StoryboardPanel ordering within Storyboard scope
- primary StoryboardPanel -> Shot association only
- minimal provenance-oriented created/updated references needed to preserve
  future traceability
- minimal revision-supporting fields only where current specifications are
  stable enough for this slice

Scope objective:

- implement coherent planning-domain data structures,
- preserve future traceability,
- avoid embedding unresolved workflow/generation/QC/continuity semantics.

## Explicitly Out of Scope

Explicitly excluded from PR-0001:

- Django app creation as committed code output
- migrations in this task document
- serializers
- REST API
- generation models
- workflow execution models
- QC models
- continuity models
- provider integrations
- provider prompts/payloads
- Artifact and ArtifactVersion models
- generic Asset models beyond opaque references if needed later
- multi-shot StoryboardPanel support
- generic versioning framework
- full storyboard revision history model if more closure is needed
- tests implementation in this task document

## Domain Objects

Objects included in the slice:

- Scene
- Shot
- Storyboard
- StoryboardPanel

Objects referenced but not implemented in PR-0001:

- Project
- Story
- Episode
- Character
- CharacterVersion
- Artifact
- Workflow
- Continuity

Reference policy for excluded upstream/downstream concepts:

- treat them as future linked concepts,
- avoid premature concrete schema for unresolved domains,
- only store minimal opaque parent/reference anchors where required for
  hierarchy integrity and planning linkage.

## Relationships

Stable relationships implemented in PR-0001:

- Episode -> Scene:
  - one Episode reference per Scene
  - Episode model itself is not implemented in this slice
- Scene -> Shot:
  - one Scene contains ordered Shots
  - one Shot belongs to exactly one Scene
- Storyboard -> StoryboardPanel:
  - one Storyboard contains ordered Panels
- StoryboardPanel -> Shot:
  - one Panel has one primary Shot association in PR-0001

Relationships intentionally deferred:

- one Panel representing multiple Shots
- full Storyboard-to-Scene and Storyboard-to-Shot scope flexibility beyond the
  primary planning path
- Character/CharacterVersion references
- Artifact provenance links
- Workflow references
- Continuity references

## Identity Strategy

Primary identity strategy:

- use UUID primary keys for all implemented models
- keep human-readable production codes separate from primary keys

Model identity direction:

- Scene:
  - stable UUID primary identity
  - optional human-readable scene code
- Shot:
  - stable UUID primary identity
  - optional human-readable shot code
- Storyboard:
  - stable UUID primary identity
- StoryboardPanel:
  - stable UUID primary identity

Identity separation rules:

- domain identity != database foreign key
- domain identity != provenance linkage
- StoryboardPanel identity != Shot identity
- human-readable code != primary key

## Ordering Strategy

Ordering must be explicit.

PR-0001 ordering scope:

- Scene ordering within Episode
- Shot ordering within Scene
- StoryboardPanel ordering within Storyboard

Ordering rules:

- do not rely on insertion order
- ordering fields are required in the first slice wherever containment order is
  stable and explicit in source specs
- ordering uniqueness should be enforced within parent scope only where the
  source specifications clearly support it

## Revision / Versioning Scope

PR-0001 takes the narrowest versioning approach consistent with current specs.

Included:

- fields and structure that allow later traceability of planning changes
- explicit model identities that remain stable across edits
- no destructive assumption that revisions overwrite identity

Deferred:

- generic versioning framework
- full SceneVersion model
- full ShotVersion model
- full StoryboardRevision model as independent implementation entity unless
  later design work decides it is required
- historical panel lineage implementation beyond preserving stable panel
  identity and explicit ordering

Reason for deferral:

- Storyboard revision semantics are conceptually stronger than Scene/Shot
  revision semantics, but a dedicated revision model is not strictly required
  for the smallest coherent implementation slice.
- The source specifications permit lightweight traceability first.

## Provenance Scope

Minimal provenance scope for PR-0001:

- stable domain identities
- stable parent/containment relationships
- explicit ordering fields
- optional human-readable codes
- timestamps for creation/update if project conventions require them in model
  baseline

Deferred provenance:

- artifact provenance
- workflow provenance
- generation provenance
- QC provenance
- continuity provenance
- actor/rationale review chains

Rationale:

- PR-0001 needs enough structure to preserve future traceability of planning
  records, but not a full provenance subsystem.

## Candidate Django App Boundary

Option A:

- one production/planning app containing Scene, Shot, Storyboard,
  StoryboardPanel

Evaluation:

- cohesion: high
- coupling: low to moderate inside planning scope
- migration complexity: lowest
- future extensibility: good for early slice because all included objects are
  planning-oriented and tightly related
- risk: later split may be needed when Storyboard grows broader lifecycle/API
  concerns

Option B:

- separate apps based on current domain documents
  - scene app
  - shot app
  - storyboard app

Evaluation:

- cohesion: theoretically high per domain, but weak for the smallest first slice
- coupling: early cross-app foreign keys and migrations would be heavier
- migration complexity: higher
- future extensibility: strong long-term possibility, but introduces overhead
  before cross-domain APIs and services exist
- risk: early fragmentation before stable app-level conventions are proven

Recommendation for PR-0001:

- choose Option A: one production/planning app for Scene, Shot, Storyboard,
  StoryboardPanel

Reason:

- strongest cohesion for the chosen slice
- lowest migration and relationship overhead
- avoids premature app-boundary fragmentation
- keeps future extraction possible once workflow/generation/qc/continuity
  integrations mature

## Candidate Model Mapping

### Scene

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable scene identity anchor | docs/domain/scene.md `scene_id` | REQUIRED | Core domain identity is required immediately. |
| episode_id | Parent Episode opaque reference | docs/domain/scene.md `parent_episode_ref` | REQUIRED | Canonical hierarchy requires Scene under Episode even if Episode model is deferred. |
| scene_order | Explicit ordering within Episode | docs/domain/scene.md `scene_order` | REQUIRED | Ordering ownership is stable and must not rely on insertion order. |
| scene_code | Human-readable scene identifier | docs/domain/scene.md `scene_code` | OPTIONAL | Useful production affordance while remaining separate from PK. |
| scene_purpose | Shared narrative purpose | docs/domain/scene.md `scene_purpose` | REQUIRED | Stable shared narrative context is core Scene semantics. |
| dramatic_objective | Higher-level dramatic aim/change | docs/domain/scene.md `dramatic_objective` | OPTIONAL | Stable enough, but not required for the smallest coherent slice. |
| time_context_text | Shared temporal context summary | docs/domain/scene.md `time_context_ref` | OPTIONAL | Allows minimal time/place anchoring without inventing a Time domain. |
| location_context_text | Shared location/environment context summary | docs/domain/scene.md `location_context_ref` | OPTIONAL | Supports stable scene-level time/place semantics while generic Asset/Location domain is deferred. |

### Shot

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable shot identity | docs/domain/shot.md `shot_id` | REQUIRED | Shot is the primary production unit. |
| scene_id | Canonical containment in Scene | docs/domain/shot.md `scene_reference` | REQUIRED | Stable one-Scene-per-Shot relationship is core to this slice. |
| shot_order | Explicit order within Scene | docs/domain/shot.md `shot_order` | REQUIRED | Ordering is explicit and stable. |
| shot_code | Human-readable shot code | docs/domain/shot.md `shot_code` | OPTIONAL | Valuable for production readability while remaining separate from PK. |
| narrative_purpose | Local dramatic purpose | docs/domain/shot.md `narrative_purpose` | REQUIRED | Core shot intent in planning slice. |
| action_intent | Visual action target | docs/domain/shot.md `action_intent` | REQUIRED | Stable and central to shot planning. |
| subject_focus | Primary subject emphasis | docs/domain/shot.md `subject_focus` | OPTIONAL | Helpful but not necessary to achieve minimal slice integrity. |

### Storyboard

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable storyboard identity | docs/domain/storyboard.md `storyboard_id` | REQUIRED | Storyboard is a first-class planning/review construct. |
| scene_id | Primary planning scope linkage to Scene | docs/domain/storyboard.md `storyboard_scope_ref`; docs/domain/scene.md storyboard linkage | REQUIRED | Minimal planning slice needs a stable scene-scoped storyboard anchor. |
| status | Planning/review lifecycle context | docs/domain/storyboard.md `storyboard_status` | REQUIRED | Lifecycle state is part of current stable storyboard semantics. |
| title | Human-readable storyboard label | implied planning identity convenience | OPTIONAL | Useful for operator readability without changing architecture. |

Implementation note:

- PR-0001 should scope Storyboard to one Scene to stay conservative.
- broader storyboard scope patterns remain deferred.

### StoryboardPanel

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable panel identity | docs/domain/storyboard.md `panel_id` | REQUIRED | Panel identity must remain distinct from Shot and Artifact. |
| storyboard_id | Parent storyboard linkage | docs/domain/storyboard.md panel containment | REQUIRED | Stable ordered panel scope requires explicit parent. |
| panel_order | Explicit order within Storyboard | docs/domain/storyboard.md `panel_order` | REQUIRED | Ordering is stable and explicit in spec. |
| primary_shot_id | Preferred one primary Shot association | docs/domain/storyboard.md `panel_primary_shot_ref` | REQUIRED | PR-0001 intentionally implements only the stable preferred cardinality direction. |
| panel_notes | Planning annotations/notes | docs/domain/storyboard.md `panel_annotations` | OPTIONAL | Preserves basic planning utility without inventing heavy annotation schema. |

Field exclusions for PR-0001:

- multi-shot panel secondary associations
- panel visualization artifact references
- continuity note objects
- cinematography structured sub-schema
- character/asset typed reference sets
- review feedback item structures
- revision lineage structures beyond stable identities and ordering

## Database Constraints

Only stable invariants should become constraints in PR-0001.

Candidate constraints:

- Scene:
  - `episode_id` required
  - `scene_order` required
  - unique `(episode_id, scene_order)`
  - `scene_code` not required to be globally unique unless a later spec decides
    code format policy
- Shot:
  - `scene_id` required
  - `shot_order` required
  - unique `(scene_id, shot_order)`
- Storyboard:
  - `scene_id` required
  - no global uniqueness requirement for status/title
- StoryboardPanel:
  - `storyboard_id` required
  - `panel_order` required
  - `primary_shot_id` required
  - unique `(storyboard_id, panel_order)`

Constraints intentionally excluded:

- one storyboard per scene
- at least one panel per shot
- at least one panel before generation
- multi-shot panel support
- generic lifecycle-state restrictions beyond field validity
- cross-domain provider/generation/QC/continuity constraints

## Validation Rules

PR-0001 validation rules:

- Scene must have parent Episode reference.
- Scene must have explicit order within Episode.
- Shot must belong to exactly one Scene.
- Shot must have explicit order within Scene.
- Storyboard must link to one Scene in PR-0001 scope.
- StoryboardPanel must belong to one Storyboard.
- StoryboardPanel must have one primary Shot.
- StoryboardPanel primary Shot should belong to the same Scene as the
  Storyboard in PR-0001 scope.
- human-readable codes, if present, must not be treated as primary identity.

Validation rules explicitly deferred:

- scene-wide inheritance/override resolution
- storyboard gating rules
- revision approval policy
- continuity validation
- QC validation

## Test Plan

Model tests:

- Scene creation with required identity and ordering fields
- Shot creation with required parent Scene and order
- Storyboard creation scoped to Scene
- StoryboardPanel creation with required parent Storyboard and primary Shot

Ordering tests:

- two Scenes under same Episode cannot share same `scene_order`
- two Shots under same Scene cannot share same `shot_order`
- two Panels under same Storyboard cannot share same `panel_order`
- ordering queries return deterministic sequence by explicit order field

Relationship/cardinality tests:

- Shot cannot exist without Scene
- Panel cannot exist without Storyboard
- Panel cannot exist without primary Shot
- one Shot may have zero panels
- one Shot may have multiple panels
- panel-to-multiple-shots is not supported in PR-0001
- panel primary Shot must belong to same Scene as its Storyboard

Constraint tests:

- required parent relationships enforced
- required order fields enforced
- uniqueness constraints within parent scope enforced

Deletion/protection behavior tests:

- deleting Scene with existing Shots should be protected
- deleting Shot referenced by StoryboardPanels should be protected
- deleting Storyboard with Panels should cascade to Panels or be protected,
  but policy must be chosen consistently before code

Preferred deletion policy for PR-0001:

- protect Scene from deletion while Shots exist
- protect Shot from deletion while Panels exist
- allow Storyboard deletion to cascade to Panels if Storyboard is treated as
  planning-container owner

## Migration Plan

Migration scope for PR-0001 implementation phase should be incremental:

1. create planning app models for Scene and Shot first
2. apply ordering and parent constraints for Scene/Shot
3. create Storyboard and StoryboardPanel models
4. apply panel ordering and primary-shot constraints
5. add minimal indexes supporting ordered retrieval by parent scope

Migration discipline:

- no speculative fields
- no workflow/generation foreign keys
- no artifact/qc/continuity schema in this PR

## Implementation Sequence

1. Decide and create one planning-domain app boundary.
2. Implement Scene model with stable identity, parent Episode reference,
   ordering, and minimal narrative fields.
3. Implement Shot model with stable identity, Scene parent, ordering, and core
   shot intent fields.
4. Implement Storyboard model scoped conservatively to Scene.
5. Implement StoryboardPanel model with ordered parent Storyboard linkage and
   one primary Shot association.
6. Add admin/model-level validation or equivalent domain-safe validation for
   scene/storyboard/panel scope alignment.
7. Add model and constraint tests for identity, ordering, containment, and
   deletion behavior.

## Definition of Done

PR-0001 is done when:

- Scene, Shot, Storyboard, and StoryboardPanel persistence models exist
- UUID primary identity is used consistently
- human-readable codes remain separate from PKs
- Scene -> Shot ordering is explicit and constrained
- StoryboardPanel ordering is explicit and constrained
- Shot remains the primary production unit in code structure and naming
- StoryboardPanel does not become a hierarchy substitute
- one primary Shot association per Panel is implemented
- multi-shot panel semantics remain deferred
- required tests pass for identity, ordering, containment, and deletion policy
- no generation/workflow/qc/continuity/provider implementation leaks into the
  slice

## Open Questions

Questions that do not block PR-0001:

- should `scene_code` and `shot_code` follow a standardized formatting policy in
  a later PR?
- should Storyboard have more than one allowed scope shape in later iterations?
- should Storyboard deletion cascade or be protected by review policy?
- when should full storyboard revision modeling become necessary?

Questions explicitly deferred because they need more architecture closure:

- scene-to-shot inheritance/override implementation
- storyboard gating into workflow
- character/asset typed relation modeling
- continuity and QC integration

## ADR Check

Assessment:

- PR-0001 does not require a new ADR

Reason:

- it implements the smallest planning-domain slice already recommended by the
  readiness reviews
- it avoids workflow runtime, generation attempt semantics, idempotency, QC, and
  continuity-policy questions
- ADR-0001 and ADR-0002 are runtime-generation ADRs and do not block this slice

## Risks

- Risk: using opaque Episode references before Episode model exists may require
  later migration refinement.
- Risk: a minimal Storyboard model may later need revision-specific extraction.
- Risk: keeping location context as free text in this slice may need refactor
  once generic Asset domain is specified.
- Risk: deletion policy needs careful choice to avoid destroying planning
  history unintentionally.

Risk level overall:

- low to moderate for this slice because it intentionally excludes the most
  architecture-sensitive runtime concerns.

## Review Checklist

- canonical hierarchy preserved
- Shot remains primary production unit
- StoryboardPanel is not an alternative hierarchy level
- UUID identity used as primary direction
- human-readable codes separated from PKs
- explicit ordering fields included
- no speculative fields added
- multi-shot panel semantics deferred
- revision framework not over-designed
- provenance limited to minimal future traceability support
- no generation/workflow/QC/continuity/provider implementation introduced
- app-boundary recommendation justified
- database constraints limited to stable invariants
- test scope aligned to implemented slice only
- no ADR required
- READY FOR IMPLEMENTATION
