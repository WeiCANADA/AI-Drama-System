# PR-0001 Planning Domain Slice

## Status

- Status: Draft implementation plan
- Readiness: READY FOR IMPLEMENTATION
- Implementation Status: IMPLEMENTED
- Implemented App: planning
- Migration: planning/migrations/0001_initial.py
- Validation Status:
  - cross-scene StoryboardPanel.primary_shot validation implemented via
    `StoryboardPanel.clean()`
- Test Result Summary:
  - `python manage.py check` passed
  - `python manage.py makemigrations --check --dry-run` reported no changes
  - `python manage.py migrate` applied `planning.0001_initial`
  - `python manage.py test` passed with 26 tests
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
- relational/domain integrity is preferred over opaque parent-ID substitutes

## Scope

Included in PR-0001:

- minimum Project/Story/Episode hierarchy skeleton required to support a real
  Scene parent relationship
- Scene domain persistence and basic validation
- Shot domain persistence and basic validation
- Storyboard domain persistence and basic validation
- StoryboardPanel domain persistence and basic validation
- explicit Scene -> Shot ordering
- explicit StoryboardPanel ordering within Storyboard scope
- primary StoryboardPanel -> Shot association only
- minimal provenance-oriented created/updated references needed to preserve
  future traceability
- minimal descriptive fields only where clearly useful and safely optional

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
- freezing storyboard lifecycle as a mandatory enum/state policy
- tests implementation in this task document

## Domain Objects

Objects included in the slice:

- Project
- Story
- Episode
- Scene
- Shot
- Storyboard
- StoryboardPanel

Objects referenced but not implemented in PR-0001:

- Character
- CharacterVersion
- Artifact
- Workflow
- Continuity

Reference policy for excluded upstream/downstream concepts:

- treat them as future linked concepts,
- avoid premature concrete schema for unresolved domains,
- do not use opaque UUID stand-ins for canonical hierarchy parent
  relationships.

## Relationships

Stable relationships implemented in PR-0001:

- Episode -> Scene:
  - one real Episode parent relationship per Scene
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

Hierarchy integrity options reviewed:

- Option A:
  - add the minimum Project/Story/Episode hierarchy skeleton required to give
    Scene a real canonical parent relationship.
- Option B:
  - defer Scene persistence until Episode exists, which would also force Shot
    persistence deferral because Shot requires Scene containment.

Recommendation:

- choose Option A.

Reason:

- it preserves canonical relational/domain integrity,
- it avoids opaque parent-ID substitution,
- it keeps the intended planning slice coherent,
- it is safer than deferring Scene and collapsing the whole slice.

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
- timestamps for creation/update only if they are part of repository-standard
  model baseline rather than planning-slice-specific architecture

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

- choose Option A: one production/planning app for Project, Story, Episode,
  Scene, Shot, Storyboard, and StoryboardPanel

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
| episode_id | Parent Episode relationship | docs/domain/scene.md `parent_episode_ref` | REQUIRED | Canonical hierarchy requires real Scene containment under Episode. |
| scene_order | Explicit ordering within Episode | docs/domain/scene.md `scene_order` | REQUIRED | Ordering ownership is stable and must not rely on insertion order. |
| scene_code | Human-readable scene identifier | docs/domain/scene.md `scene_code` | OPTIONAL | Useful production affordance while remaining separate from PK. |
| scene_purpose | Shared narrative purpose | docs/domain/scene.md `scene_purpose` | OPTIONAL | Useful planning context, but the source spec does not define it as a strict first-migration invariant. |
| dramatic_objective | Higher-level dramatic aim/change | docs/domain/scene.md `dramatic_objective` | OPTIONAL | Stable enough, but not required for the smallest coherent slice. |
| time_context_text | Shared temporal context summary | docs/domain/scene.md `time_context_ref` | OPTIONAL | Allows minimal time/place anchoring without inventing a Time domain. |
| location_context_text | Shared location/environment context summary | docs/domain/scene.md `location_context_ref` | OPTIONAL | Supports stable scene-level time/place semantics while generic Asset/Location domain is deferred. |

### Project / Story / Episode Skeleton

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| project.id | Stable project identity | docs/DEVELOPMENT_SPEC.md canonical hierarchy | REQUIRED | Required to support real canonical parentage rather than opaque stand-ins. |
| story.id | Stable story identity | docs/DEVELOPMENT_SPEC.md canonical hierarchy | REQUIRED | Required to preserve Story under Project. |
| story.project_id | Canonical parent relationship | docs/DEVELOPMENT_SPEC.md canonical hierarchy | REQUIRED | Required for real hierarchy integrity. |
| episode.id | Stable episode identity | docs/DEVELOPMENT_SPEC.md canonical hierarchy | REQUIRED | Scene requires real Episode parentage. |
| episode.story_id | Canonical parent relationship | docs/DEVELOPMENT_SPEC.md canonical hierarchy | REQUIRED | Required for real hierarchy integrity. |
| episode_order | Explicit ordering within Story | docs/DEVELOPMENT_SPEC.md canonical hierarchy; ordering principles reflected across current domain specs | REQUIRED | Episode is an ordered child in the canonical hierarchy and must not rely on insertion order. |
| episode_code | Human-readable episode identifier | docs/DEVELOPMENT_SPEC.md canonical hierarchy | OPTIONAL | Useful only if repository conventions want readable hierarchy labels this early. |

### Shot

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable shot identity | docs/domain/shot.md `shot_id` | REQUIRED | Shot is the primary production unit. |
| scene_id | Canonical containment in Scene | docs/domain/shot.md `scene_reference` | REQUIRED | Stable one-Scene-per-Shot relationship is core to this slice. |
| shot_order | Explicit order within Scene | docs/domain/shot.md `shot_order` | REQUIRED | Ordering is explicit and stable. |
| shot_code | Human-readable shot code | docs/domain/shot.md `shot_code` | OPTIONAL | Valuable for production readability while remaining separate from PK. |
| narrative_purpose | Local dramatic purpose | docs/domain/shot.md `narrative_purpose` | OPTIONAL | Useful planning context, but not a stable NOT NULL invariant from current spec. |
| action_intent | Visual action target | docs/domain/shot.md `action_intent` | OPTIONAL | Useful planning context, but not part of the minimum containment/order contract. |
| subject_focus | Primary subject emphasis | docs/domain/shot.md `subject_focus` | OPTIONAL | Helpful but not necessary to achieve minimal slice integrity. |

### Storyboard

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable storyboard identity | docs/domain/storyboard.md `storyboard_id` | REQUIRED | Storyboard is a first-class planning/review construct. |
| scene_id | Primary planning scope linkage to Scene | docs/domain/storyboard.md `storyboard_scope_ref`; docs/domain/scene.md storyboard linkage | REQUIRED | Minimal planning slice needs a stable scene-scoped storyboard anchor. |
| title | Human-readable storyboard label | implied planning identity convenience | OPTIONAL | Useful for operator readability without changing architecture. |

Implementation note:

- PR-0001 should scope Storyboard to one Scene to stay conservative.
- broader storyboard scope patterns remain deferred.
- Storyboard lifecycle remains conceptual in the source specification and should
  not be frozen into a required status enum in the first migration.
- A primary Shot association remains the preferred v1 direction, but PR-0001
  should not encode that preference as a hard NOT NULL invariant.

### StoryboardPanel

| Field Name | Conceptual Purpose | Source Specification | REQUIRED or OPTIONAL for PR-0001 | Why It Belongs in First Slice |
|---|---|---|---|---|
| id | Stable panel identity | docs/domain/storyboard.md `panel_id` | REQUIRED | Panel identity must remain distinct from Shot and Artifact. |
| storyboard_id | Parent storyboard linkage | docs/domain/storyboard.md panel containment | REQUIRED | Stable ordered panel scope requires explicit parent. |
| panel_order | Explicit order within Storyboard | docs/domain/storyboard.md `panel_order` | REQUIRED | Ordering is stable and explicit in spec. |
| primary_shot_id | Preferred one primary Shot association | docs/domain/storyboard.md `panel_primary_shot_ref` | OPTIONAL | The spec establishes a preferred v1 direction, but does not clearly make unbound Panels invalid as a database-level invariant in the first migration. |
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

- Project:
  - no additional stable constraints beyond primary identity in PR-0001
- Story:
  - `project_id` required
- Episode:
  - `story_id` required
  - `episode_order` required
  - unique `(story_id, episode_order)`
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
  - no required lifecycle-status constraint in PR-0001
- StoryboardPanel:
  - `storyboard_id` required
  - `panel_order` required
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

- Project/Story/Episode skeleton must provide real canonical parent chain for
  Scene.
- Episode must have explicit order within Story.
- Scene must have real parent Episode relationship.
- Scene must have explicit order within Episode.
- Shot must belong to exactly one Scene.
- Shot must have explicit order within Scene.
- Storyboard must link to one Scene in PR-0001 scope.
- StoryboardPanel must belong to one Storyboard.
- if `primary_shot_id` is present, it must belong to the same Scene as the
  Storyboard in PR-0001 scope.
- human-readable codes, if present, must not be treated as primary identity.

Lifecycle-policy note:

- PR-0001 does not treat unbound StoryboardPanels as ideal planning state.
- It simply avoids encoding "must have primary shot before persistence" as a
  first-migration database invariant.

Validation rules explicitly deferred:

- scene-wide inheritance/override resolution
- storyboard lifecycle/gating rules
- revision approval policy
- continuity validation
- QC validation

## Test Plan

Model tests:

- Project/Story/Episode skeleton creation with real parent relationships
- Episode creation with required explicit order within Story
- Scene creation with required identity, real Episode parent, and ordering
  fields
- Shot creation with required parent Scene and order
- Storyboard creation scoped to Scene
- StoryboardPanel creation with required parent Storyboard and optional primary
  Shot

Ordering tests:

- two Episodes under same Story cannot share same `episode_order`
- two Scenes under same Episode cannot share same `scene_order`
- two Shots under same Scene cannot share same `shot_order`
- two Panels under same Storyboard cannot share same `panel_order`
- ordering queries return deterministic sequence by explicit order field

Relationship/cardinality tests:

- Scene cannot exist without real Episode parent relationship
- Shot cannot exist without Scene
- Panel cannot exist without Storyboard
- one Panel may exist without primary Shot in the first migration
- one Shot may have zero panels
- one Shot may have multiple panels
- panel-to-multiple-shots is not supported in PR-0001
- if panel primary Shot is present, it must belong to same Scene as its
  Storyboard

Constraint tests:

- required parent relationships enforced
- required order fields enforced
- uniqueness constraints within parent scope enforced

Deletion/protection behavior tests:

- Project -> Story deletion policy: CONSERVATIVE DEFAULT
  - deleting Project with existing Stories should be protected
- Story -> Episode deletion policy: CONSERVATIVE DEFAULT
  - deleting Story with existing Episodes should be protected
- Episode -> Scene deletion policy: CONSERVATIVE DEFAULT
  - deleting Episode with existing Scenes should be protected
- Scene -> Shot deletion policy: CONSERVATIVE DEFAULT
  - deleting Scene with existing Shots should be protected
- Scene -> Storyboard deletion policy: CONSERVATIVE DEFAULT
  - deleting Scene with existing Storyboards should be protected
- Storyboard -> StoryboardPanel deletion policy: CONSERVATIVE DEFAULT
  - deleting Storyboard with existing Panels should be protected
- Shot -> StoryboardPanel deletion policy: CONSERVATIVE DEFAULT
  - deleting Shot referenced by StoryboardPanels should be protected

Preferred deletion policy for PR-0001:

- Project -> Story: PROTECT
- Story -> Episode: PROTECT
- Episode -> Scene: PROTECT
- Scene -> Shot: PROTECT
- Scene -> Storyboard: PROTECT
- Storyboard -> StoryboardPanel: PROTECT
- Shot -> StoryboardPanel: PROTECT

Deletion-policy note:

- this is a conservative first-slice implementation policy.
- it is not a permanent archive/soft-delete architecture decision.
- it exists to avoid destructive cascade loss of production planning history.

## Migration Plan

Migration scope for PR-0001 implementation phase should be incremental:

1. create minimal Project/Story/Episode hierarchy skeleton sufficient for real
  Scene parent relationship
2. apply ordering and parent constraints for hierarchy, including explicit
  Episode ordering within Story
3. create planning app models for Scene and Shot
4. apply ordering and parent constraints for Scene and Shot
5. create Storyboard and StoryboardPanel models
6. apply panel ordering and optional primary-shot relation constraints
7. add minimal indexes supporting ordered retrieval by parent scope

Migration discipline:

- no speculative fields
- no workflow/generation foreign keys
- no artifact/qc/continuity schema in this PR

## Implementation Sequence

1. Decide and create one planning-domain app boundary.
2. Implement minimal Project/Story/Episode hierarchy skeleton needed for real
  Scene containment.
3. Implement explicit Episode ordering within Story.
4. Implement Scene model with stable identity, real Episode parent,
  ordering, and only optional descriptive fields.
5. Implement Shot model with stable identity, Scene parent, ordering, and only
  optional descriptive fields.
6. Implement Storyboard model scoped conservatively to Scene without freezing a
  mandatory lifecycle-status contract.
7. Implement StoryboardPanel model with ordered parent Storyboard linkage and
  optional primary Shot association.
8. Add admin/model-level validation or equivalent domain-safe validation for
   scene/storyboard/panel scope alignment.
9. Add model and constraint tests for identity, ordering, containment, and
  deletion behavior.

## Definition of Done

PR-0001 is done when:

- minimal Project/Story/Episode hierarchy skeleton exists to support real Scene
  parentage
- Scene, Shot, Storyboard, and StoryboardPanel persistence models exist
- UUID primary identity is used consistently
- human-readable codes remain separate from PKs
- Episode ordering within Story is explicit and constrained
- Scene -> Shot ordering is explicit and constrained
- StoryboardPanel ordering is explicit and constrained
- Shot remains the primary production unit in code structure and naming
- StoryboardPanel does not become a hierarchy substitute
- one primary Shot association per Panel is supported without implementing
  multi-shot semantics
- multi-shot panel semantics remain deferred
- descriptive planning fields are optional unless clearly supported as stable
  invariants
- Storyboard lifecycle policy is not prematurely frozen as a required enum
- all first-slice hierarchy/planning foreign keys use conservative PROTECT
  deletion behavior
- required tests pass for identity, ordering, containment, and deletion policy
- no generation/workflow/qc/continuity/provider implementation leaks into the
  slice

## Open Questions

Questions that do not block PR-0001 once the hierarchy skeleton is included:

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

- Risk: introducing minimal Project/Story/Episode skeleton broadens the first
  migration slightly, even though it is safer than using opaque parent IDs.
- Risk: a minimal Storyboard model may later need revision-specific extraction.
- Risk: keeping descriptive planning fields optional may reduce early data
  richness until later PRs add more planning content.
- Risk: deletion policy needs conservative defaults to avoid destroying
  planning history unintentionally.
- Risk: optional `primary_shot_id` allows temporarily unbound Panels, so later
  review/approval or downstream-generation policy must decide when binding
  becomes mandatory.

Risk level overall:

- low to moderate for this slice because it intentionally excludes the most
  architecture-sensitive runtime concerns.

## Readiness

Hierarchy integrity reassessment:

- Option A is recommended.
- Option B is rejected for PR-0001 because deferring Scene would also undermine
  Shot and collapse the intended slice.

Implementation readiness depends on one exact condition:

- PR-0001 must include the minimum Project/Story/Episode hierarchy skeleton
  needed for a real Scene parent relationship.
- PR-0001 must implement conservative PROTECT deletion behavior for all
  first-slice hierarchy/planning foreign keys.

Implementation-contract status after cleanup:

- no unresolved choice remains that Django model implementation must make
  implicitly for hierarchy parentage, deletion behavior, storyboard lifecycle
  requiredness, or panel primary-shot requiredness.

Final determination:

- READY FOR IMPLEMENTATION

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
