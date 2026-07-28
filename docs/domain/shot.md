# Shot Domain Specification v1.0

## 1. Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for downstream domain specification (Layer 4 Batch 1 outcomes recorded at candidate level)
- Specification Type: Domain Specification
- Domain: Shot
- Version: 1.0
- Evidence Basis:
  - Development specification constraints and invariants from docs/DEVELOPMENT_SPEC.md.
  - Cross-layer synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md.
  - AI research synthesis from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md.
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md.
  - Production research records:
    - docs/research/production/scene-shot-terminology.md
    - docs/research/production/cinematography.md
    - docs/research/production/storyboarding.md
    - docs/research/production/continuity.md
    - docs/research/production/animation-production-pipeline.md
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - No pre-existing shot domain specification found in docs/domain/ at draft time.
- Related Research:
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - docs/research/production/scene-shot-terminology.md
  - docs/research/production/cinematography.md
  - docs/research/production/storyboarding.md
  - docs/research/production/continuity.md
  - docs/research/production/animation-production-pipeline.md
  - docs/research/architecture/camera-spatial-interchange.md
  - docs/research/architecture/provenance-interchange.md
  - docs/research/architecture/temporal-editorial-interchange.md
- Related ADRs:
  - No accepted ADR files were found under docs/adr/ in the current repository state.

Unresolved architectural decisions in this specification remain subject to ADR review and acceptance. This document does not accept ADRs.

## 2. Purpose

This specification defines the provider-independent production meaning, responsibilities, boundaries, relationships, and minimum conceptual information model for Shot in AI Drama System.

This specification answers: What is a Shot in AI Drama System?

This specification does not define Django storage details, ORM classes, SQL schemas, provider APIs, or model-specific generation logic.

## 3. Domain Definition

A Shot is the primary audiovisual production unit under a Scene, representing one intentional visual presentation of narrative action with explicit production intent, continuity context, and traceable linkage to downstream generation and review artifacts.

Concept distinctions:

- Scene:
  - A higher-level narrative unit anchored in time/place and dramatic objective.
  - A Scene contains ordered Shots.
- Shot:
  - The canonical execution and traceability unit for visual production intent.
  - A Shot is not replaced by panels, keyframes, takes, or workflow nodes.
- Storyboard Panel:
  - A planning/review representation that may illustrate all or part of Shot intent.
  - A panel is not equivalent to the Shot entity.
- Generation Artifact:
  - A produced output (image/video/audio/other media record) linked by provenance.
  - Artifacts are outputs related to Shot, not the Shot itself.
- Video Segment:
  - A rendering/output segment used in a specific workflow or edit context.
  - Segment boundaries do not redefine Shot boundaries.
- Keyframe / Anchor:
  - A planning or generation aid for drift control, continuity, or rendering strategy.
  - Anchors are adjunct references to Shot workflows, not a replacement domain unit.

## 4. Domain Responsibilities

Shot owns or anchors the following conceptual responsibilities:

- Production intent for a single visual unit.
- Narrative purpose at shot granularity (beat-level intent, not whole-scene narrative ownership).
- Action intent (what changes or is revealed in this visual unit).
- Participating subject references (characters and other assets relevant to the shot).
- Cinematography intent (framing, angle, movement intent, etc.) in provider-neutral terms.
- Spatial intent among participating subjects and environment.
- Continuity context linkage at transitions.
- Storyboard linkage for planning/review iterations.
- Generation context linkage (Shot -> PromptInstance -> GenerationTask chain).
- Result linkage to artifacts, QC outcomes, and review decisions through provenance.

Note: responsibility ownership here is conceptual and does not imply one field per concept.

## 5. Domain Boundaries

Shot does not own the following concerns as core domain truth:

- Provider-specific prompts, embeddings, LoRA references, model tokens.
- ComfyUI nodes, provider workflow JSON, or engine-specific parameter graphs.
- Generated binary file payloads themselves.
- Global Character identity authoring (owned by Character domain).
- Full Scene-level narrative state and scene-wide dramatic scope.
- Provider runtime logic (request submission, polling, retry implementation).

Boundary rule:

- Shot stores or references production intent.
- Adapters/workflows translate intent into provider-specific execution representations.

## 6. Shot Relationships

Domain relationships (conceptual):

- Project -> Story -> Episode -> Scene -> Shot: canonical containment chain.
- Scene -> Shot: Scene contains ordered Shots.
- Shot -> Character: Shot references participating character identity.
- Shot -> CharacterVersion or appearance context: Shot may reference appearance state relevant to this instance.
- Shot -> Location, Prop, Style: Shot references production assets needed to express intent.
- Shot -> Storyboard: Shot links to planning/review representations.
- Shot -> Continuity: Shot participates in incoming/outgoing continuity tracking.
- Shot -> PromptInstance: Prompt instances consume Shot production intent.
- Shot -> GenerationTask: tasks execute generation requests for shot-linked intent.
- Shot -> Artifact: produced artifacts are linked with provenance to shot context.
- Shot -> QC: quality/review records evaluate shot outputs and planning artifacts.

Implementation note:

- These are domain relationships, not mandatory direct foreign key requirements for every concept.
- Indirect linkage via task/provenance records is valid when it preserves traceability.

## 7. Shot Identity

Shot identity requirements:

- Stable machine identity (UUID recommended per project-wide identity rule).
- Human-readable production code allowed (for example EP01_SC03_SH012).
- Human-readable code must not be the database primary key.
- Identity must remain stable across revisions unless intentionally superseded by defined lifecycle/version process.

## 8. Shot Ordering

Shot ordering requirements within a Scene:

- Ordering must be explicit and deterministic.
- Ordering must not depend on insertion order.
- Reordering must be a deliberate production action with preserved historical traceability when required by review/provenance needs.

This specification defines ordering semantics only, not ORM implementation details.

## 9. Narrative Intent

Minimum narrative intent expected at Shot level:

- Purpose: why this shot exists in the scene progression.
- Action: what visual/narrative action is conveyed.
- Dramatic beat relevance: local dramatic function of the shot.
- Subject focus: who or what is visually prioritized.
- Dialogue relationship (if applicable): how spoken content maps to visual intent.

Boundary:

- Shot-level narrative intent must not duplicate full screenplay or scene-level narrative ownership.

## 10. Character Participation

Shot character participation should distinguish:

- Character identity:
  - Persistent production identity of participants.
- Character appearance/version context:
  - Mutable visual state or reference selection relevant for this shot.
- Shot-specific state:
  - Per-shot participation context (for example stance, focus role, action relevance) without redefining Character identity.

Provider-specific identity representation mechanisms remain out of core Shot domain.

## 11. Spatial Intent

Provider-neutral spatial intent for Shot should support:

- Subject position intent.
- Relative position among subjects.
- Foreground/midground/background layering intent.
- Relative scale intent.
- Orientation and blocking intent.
- Spatial relationship significance (for example confrontation distance, isolation, grouping).

Representation constraints:

- Spatial intent should be machine-usable but provider-neutral.
- This spec does not lock a coordinate system.
- Coordinate schema standardization is an open question (see Open Questions and Layer 4 requests).

## 12. Cinematography Intent

Shot-level cinematography intent categories:

- CORE:
  - shot size intent
  - framing intent
  - camera angle intent
  - screen direction intent
- OPTIONAL:
  - camera height intent
  - camera movement intent
  - perspective intent
  - composition intent
  - lighting intent
- DEFERRED:
  - lens/focal-length numeric standardization
  - focus/depth-of-field numeric standardization
- OPEN QUESTION:
  - minimum neutral vocabulary and schema required for cross-provider portability

Important constraints:

- Not every cinematography concept is mandatory on every shot.
- Qualitative intent remains primary.
- Numeric technical values may exist as execution metadata when available, but do not define Shot ontology.

## 13. Continuity Context

Shot must participate in explicit continuity tracking by supporting:

- Incoming continuity context (state entering shot).
- Outgoing continuity context (state leaving shot).
- Continuity constraints relevant to transitions.
- Continuity issues and review outcomes linkage.

This does not fully design the Continuity domain or impose a continuity algorithm.

## 14. Storyboard Relationship

Shot and Storyboard relationship rules:

- Storyboard is a first-class planning/review stage.
- Shot is not equal to Storyboard Panel.
- A Shot may have zero, one, or multiple associated panels across lifecycle stages.
- Panel revisions and storyboard review history must remain traceable to shot intent.

Open cardinality question:

- Whether specific production profiles should enforce at least one panel before generation remains unresolved.

## 15. Generation Relationship

The conceptual generation chain is preserved:

- Shot -> PromptInstance -> GenerationTask -> GenerationAttempt -> GenerationResult -> Artifact

Rules:

- Shot must not directly contain provider execution logic.
- Generation systems consume structured shot production intent.
- Provider-specific translation occurs in workflow/provider adapters.

## 16. Keyframes / Anchors

Keyframes/anchors are defined as possible:

- planning artifacts
- generation artifacts
- workflow-specific references
- continuity anchors

Rules:

- Keyframes/anchors must not redefine Shot.
- No independent Keyframe domain entity is accepted in this specification.
- If formalized later, keyframe modeling requires separate justification and likely ADR review.

## 17. Lifecycle

Production lifecycle concept candidates for Shot (not accepted state machine):

- Draft
- Planned
- Storyboarded
- Ready for Generation
- In Generation
- Review
- Approved
- Locked

Status of lifecycle definition in this draft:

- Lifecycle concept: ACCEPT INTO DRAFT SPEC as conceptual staging vocabulary.
- Formal state machine, transitions, and gating policy: OPEN QUESTION / REQUIRES ADR.

## 18. Versioning

Version/history semantics required at shot scope:

- Shot intent changes should be historically traceable when they materially impact generation output.
- Storyboard revisions should remain linked to the relevant shot intent context.
- Generation history is preserved through GenerationTask/Attempt/Result records.
- Approval and review history must remain inspectable.
- Continuity issue/resolution history must remain linked.

This specification does not require full Shot entity versioning at v1, but requires traceability sufficient for reproducibility.

## 19. Provenance

Shot-level provenance requirements (conceptual):

- Trace from shot planning intent to prompt instance(s).
- Trace from prompt instance(s) to generation task/attempt/result.
- Trace from generation result to artifact(s).
- Preserve enough context to explain why an artifact exists and which shot intent it corresponds to.

This section complements, but does not replace, detailed Artifact provenance specification.

## 20. Validation / Invariants

Domain invariants supported by current evidence:

- A Shot belongs to exactly one Scene in canonical hierarchy context.
- Shot identity is stable and independent from display code.
- Shot ordering within Scene is deterministic and explicit.
- Provider-specific execution details do not define Shot.
- Historical generation provenance remains traceable to shot-linked intent.
- Scene and Shot remain distinct domain concepts.
- Keyframes/anchors may assist workflows but do not replace Shot.

## 21. Candidate Information Model

This is a conceptual model, not a Django schema.

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| shot_id | Stable machine identity | CORE DOMAIN | Yes | UUID-style identity recommended by project rule. |
| shot_code | Human production-readable identifier | OPTIONAL DOMAIN | No | Must not be primary key. |
| scene_reference | Canonical containment in Scene | CORE DOMAIN | Yes | Scene and Shot remain distinct. |
| shot_order | Deterministic order in scene | CORE DOMAIN | Yes | Must be explicit, not insertion-derived. |
| narrative_purpose | Local dramatic purpose | CORE DOMAIN | Yes | Shot-level intent, not full scene narrative. |
| action_intent | Visual action target | CORE DOMAIN | Yes | Supports planning and prompt construction. |
| subject_focus | Primary subject emphasis | OPTIONAL DOMAIN | No | Helps composition and QC interpretation. |
| character_participation | Participating characters and shot context | CORE DOMAIN | Yes | Distinguish identity from appearance/state. |
| appearance_context_refs | Mutable appearance/version references | REFERENCE | No | Links to character/version or continuity context. |
| location_ref | Spatial setting reference | REFERENCE | Usually | Required when scene rules need explicit location binding. |
| prop_refs | Prop participation | OPTIONAL DOMAIN | No | Depends on shot content. |
| style_ref | Style intent linkage | OPTIONAL DOMAIN | No | May inherit from higher scope. |
| spatial_intent | Neutral spatial relations | CORE DOMAIN | Yes | Schema detail deferred (Q5). |
| cinematography_intent | Neutral camera/framing intent | CORE DOMAIN | Yes | Contains core + optional sub-concepts. |
| continuity_in_ref | Incoming continuity linkage | REFERENCE | No | Explicit when continuity tracking active. |
| continuity_out_ref | Outgoing continuity linkage | REFERENCE | No | Explicit when continuity tracking active. |
| storyboard_links | Planning/review linkage | REFERENCE | No | Zero/one/many panel/revision possibilities. |
| generation_context_link | Link to prompt/task chain | REFERENCE | No | Supports end-to-end traceability. |
| review_status_context | Human review/QC state context | DERIVED | No | May be computed from review records. |
| provider_execution_payload | Provider runtime details | PROVIDER-SPECIFIC | No | Out of core shot domain; keep in workflow/execution records. |
| binary_artifact_payload | Raw file content | WORKFLOW-SPECIFIC | No | Stored/managed by artifact/storage systems. |

## 22. Candidate Requirements

Candidate requirements reviewed from AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md:

| Candidate Requirement | Decision in This Draft Spec | Rationale |
|---|---|---|
| CR-001: Scene and Shot remain distinct in canonical hierarchy | ACCEPT INTO DRAFT SPEC | Strong cross-layer support and aligns with development invariants. |
| CR-002: Shot is primary execution unit; anchors/keyframes do not replace it | ACCEPT INTO DRAFT SPEC | Strong cross-layer support; aligns with production and AI synthesis boundaries. |
| CR-005: Production intent remains provider-neutral; adapters translate | ACCEPT INTO DRAFT SPEC | Core architectural principle and required for provider independence. |
| CR-006: Continuity explicitly tracked at shot transitions | ACCEPT INTO DRAFT SPEC | Supported by continuity and production pipeline evidence; detailed continuity model remains separate. |
| CR-009: Provider-neutral camera/spatial intent attached to Shot | ACCEPT INTO DRAFT SPEC with OPEN QUESTION | Accepted direction with unresolved schema detail (Q5). Formal schema choice may require ADR. |

Interpretation rule:

- Accept into Draft Spec means accepted into this draft document scope only.
- It does not automatically accept project architecture or replace ADR governance.

## 23. ADR Review Points

Architectural decision points that may require ADR review:

- Whether Shot is permanently fixed as primary production execution unit across all production profiles.
- Whether a formal shared provider-neutral camera/spatial schema is required at architecture level.
- Whether Shot lifecycle should be standardized as a strict state machine and stage-gate policy.
- How keyframes/anchors should be modeled (artifact-linked, workflow state, or separate planning structure).

No ADR is created or accepted in this specification.

## 24. Open Questions

- Q5 (High): What provider-neutral camera/spatial schema should be standardized for v1 interoperability?
- Q6 (Medium): Should keyframes/anchors be modeled primarily as shot-linked artifacts, workflow state, or optional planning records?
- Should at least one storyboard panel be mandatory for selected project profiles before generation tasks can start?
- Which continuity constraints are machine-checkable in v1 versus human-review only?
- Which subset of cinematography intent should be mandatory at Ready for Generation stage, if any?

## 25. Out of Scope for v1

Explicitly out of scope in this document:

- Django models, serializers, migrations, and SQL schema design.
- Provider API implementations and workflow engine runtime details.
- ComfyUI workflow JSON and any model-specific conditioning representation.
- Embedding formats, identity tokens, LoRA/adapter internals.
- Rendering algorithms and final video encoding architecture.
- Detailed QC algorithm definitions and metric thresholds.
- Full Continuity domain design.
- Acceptance of architectural decisions through ADRs.

## 26. Traceability

| Specification Decision / Candidate | Evidence Source | Evidence Status |
|---|---|---|
| Preserve Scene vs Shot distinction and canonical hierarchy | docs/DEVELOPMENT_SPEC.md; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/production/scene-shot-terminology.md | Strong support; synthesis candidate promoted only to draft-spec scope |
| Keep Shot as primary production unit | docs/DEVELOPMENT_SPEC.md; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md | Strong support |
| Keep intent provider-neutral and adapter-translated | docs/DEVELOPMENT_SPEC.md; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md | Strong support |
| Separate Shot intent from provider payload details | docs/DEVELOPMENT_SPEC.md; docs/research/production/cinematography.md; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md | Strong to moderate support |
| Attach spatial/camera intent to Shot in neutral form | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md; docs/research/production/cinematography.md | Moderate support; schema unresolved |
| Storyboard is planning/review stage linked to Shot | docs/DEVELOPMENT_SPEC.md; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md; docs/research/production/storyboarding.md | Strong support |
| Explicit continuity linkage at shot transitions | docs/DEVELOPMENT_SPEC.md; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/production/continuity.md | Moderate to strong support |
| Preserve generation chain and shot-linked provenance | docs/DEVELOPMENT_SPEC.md; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/production/animation-production-pipeline.md | Strong support |
| Keyframes/anchors do not replace Shot | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md | Strong support; modeling details open |

## 27. Specification Readiness

Sufficiently defined in this draft:

- Shot meaning, ownership boundary, and distinction from Scene/panel/artifact/keyframe.
- Canonical placement in Project -> Story -> Episode -> Scene -> Shot.
- Core responsibilities and invariants for shot-level production intent and traceability.
- Provider-neutral boundary with adapter-based translation expectation.
- Relationship to storyboard, continuity, generation chain, artifacts, and QC.

Blocked or partially defined:

- Formal neutral schema details for camera/spatial representation (Q5).
- Formal keyframe/anchor modeling strategy (Q6).
- Lifecycle transition/state-machine governance and mandatory gates by profile.

Requires ADR review (not accepted here):

- Camera/spatial shared schema commitment level.
- Formal lifecycle state machine and mandatory gates.
- Long-term keyframe/anchor domain placement strategy.

Layer 4 standards/software-architecture research status:

- Layer 4 Batch 1 requested by this specification is completed and recorded in:
  - docs/research/architecture/camera-spatial-interchange.md
  - docs/research/architecture/provenance-interchange.md
  - docs/research/architecture/temporal-editorial-interchange.md
  - docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
- Result: Shot v1 conceptual scope is research-unblocked for downstream domain specification work.
- Remaining follow-on research is focused on implementation-depth interoperability decisions, not on Shot v1 conceptual validity.

Recommended next specifications after this draft:

- Storyboard domain specification (cardinality/lifecycle alignment with Shot).
- Character asset specification (identity/version/appearance boundary clarity for shot participation).
- Continuity specification (machine-checkable core and issue workflow).
- Artifact and provenance specification (detailed immutable traceability contract).

## 28. Layer 4 Research Outcomes (Batch 1)

Status note:
- Research completed for all three Layer 4 requests identified by this specification.
- Standards and technologies remain candidates.
- No standards adoption decision is made in this specification.

1. Request: Provider-neutral camera/spatial intent contract pattern (RL-ARCH-CAMERA-001)
- Research completed: Yes.
- Relevant research record: docs/research/architecture/camera-spatial-interchange.md
- Synthesis conclusion: docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - Preferred direction is a provider-neutral internal contract for camera/spatial intent.
  - glTF, OTIO, and SMPTE remain interchange/reference candidates.
  - Final internal field/schema standardization remains unresolved.
- Blocking status:
  - Non-blocking for Shot v1 conceptual scope.
  - Potentially blocking for strict cross-provider interoperability implementation decisions.
- Remaining question:
  - What minimum shared internal camera/spatial field set should be mandatory vs optional by production profile?

2. Request: Minimal provenance identifier contract for shot-to-artifact traceability (RL-ARCH-PROV-001)
- Research completed: Yes.
- Relevant research record: docs/research/architecture/provenance-interchange.md
- Synthesis conclusion: docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - Internal production provenance and external authenticity/verifiable provenance are separate concerns.
  - W3C PROV and C2PA remain candidates.
  - Detailed provenance data model design is deferred to future Artifact & Provenance specification work.
- Blocking status:
  - Non-blocking for Shot v1 conceptual scope.
  - Potentially blocking for interoperability-heavy provenance implementation profiles.
- Remaining question:
  - What canonical internal identifier and retention/redaction policy is required for reproducibility and cross-tool exchange?

3. Request: Neutral temporal/editorial metadata for continuity and editorial traceability (RL-ARCH-TIME-001)
- Research completed: Yes.
- Relevant research record: docs/research/architecture/temporal-editorial-interchange.md
- Synthesis conclusion: docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - Shot identity remains separate from timeline placement, media duration, generated segment, and editorial clip.
  - OTIO and SMPTE remain interchange/reference candidates.
  - Detailed time-base and normalization policy is deferred to future timeline/editorial specification work.
- Blocking status:
  - Non-blocking for Shot v1 conceptual scope.
  - Potentially blocking for advanced editorial round-trip interoperability implementation.
- Remaining question:
  - What canonical mixed-frame-rate and drop-frame normalization policy should govern timeline/editorial interoperability?
