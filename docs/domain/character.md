# Character Asset Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for drafting a provider-independent Character domain baseline; partially blocked for final boundary closure on CharacterVersion, Wardrobe, and CharacterReference modeling details.
- ADR Blocker Status: No immediate ADR blocker for publishing this draft; targeted ADR review is likely required before freezing CharacterVersion and CharacterReference architecture policies.
- Specification Type: Domain Specification
- Domain: Character Asset
- Version: 1.0
- Evidence Basis:
  - System constraints and principles from docs/DEVELOPMENT_SPEC.md
  - Shot boundaries from docs/domain/shot.md
  - Storyboard boundaries from docs/domain/storyboard.md
  - Cross-layer synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - AI synthesis from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - AI paper records:
    - docs/research/ai-papers/RL-AI-CHAR-001-storymaker.md
    - docs/research/ai-papers/RL-AI-CHAR-002-instantcharacter.md
  - Production research records:
    - docs/research/production/character-bible.md
    - docs/research/production/continuity.md
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/domain/shot.md
  - docs/domain/storyboard.md
- Related Research:
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - docs/research/ai-papers/RL-AI-CHAR-001-storymaker.md
  - docs/research/ai-papers/RL-AI-CHAR-002-instantcharacter.md
  - docs/research/production/character-bible.md
  - docs/research/production/continuity.md
- Related ADRs:
  - No accepted ADR files were found under docs/adr/ in the current repository state.

Unresolved architecture choices remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

Define provider-independent Character production semantics for identity,
appearance-versioning, references, shot usage, continuity interaction,
and traceability.

## Domain Definition

Character is persistent production identity used across planning, generation,
review, and continuity stages.

Character is not defined as:

- face embedding
- prompt
- reference image binary
- LoRA
- model token
- generated portrait

Character remains a production-domain concept independent from provider-specific
identity implementations.

## Terminology

- Character:
  - Persistent production identity and narrative identity anchor.
- CharacterVersion:
  - Durable approved appearance/version state linked to Character identity.
- Appearance State:
  - Human-reviewable appearance context; may be durable (version-level) or
    transient (continuity/shot-level).
- CharacterReference:
  - Intentional production reference relationship for identity/appearance use.
- Wardrobe:
  - Clothing/costume appearance context potentially modeled at version and/or
    continuity layers depending on durability.
- Costume / Outfit:
  - Wardrobe expression used in production context.
- Hairstyle:
  - Appearance attribute that may be stable identity trait, versioned look,
    or transient continuity variation based on usage scope.
- Body Appearance:
  - Appearance attributes (shape, proportions, marks, silhouette cues)
    that may include stable and mutable layers.
- Accessory:
  - Item-level appearance context that may be reusable asset and/or version/
    continuity-linked appearance detail.
- Expression Reference:
  - Reference used for expression intent; not equivalent to transient shot
    performance state.
- Pose Reference:
  - Reference used for planning/visual guidance; not persistent identity.
- Character Artifact:
  - Generated/imported output related to character work with provenance.
- Continuity State:
  - Cross-stage tracked temporal state for moment-specific consistency.
- Provider Identity Representation:
  - Provider/model-specific mechanism outside core Character domain.

Term policy:

- This draft does not automatically promote every term into a separate entity.
- Entity boundaries remain candidate-level where evidence is not yet definitive.

## Persistent Identity

Persistent Character identity should include only sufficiently stable concerns,
for example:

- production identity and code-level identity anchor
- narrative identity and role context
- canonical identity description
- stable visual traits that persist across approved versions
- identity-level design references approved as baseline identity cues

Persistent identity should not absorb transient pose/action/scene state,
or provider-specific generation representations.

## Mutable Appearance / CharacterVersion

CharacterVersion is the candidate boundary for durable approved appearance
changes that should remain historically traceable, for example:

- costume/wardrobe set changes intended to persist
- hairstyle redesign intended to persist
- age presentation redesign
- injury or makeup state that persists over defined production spans
- accessory set intended to persist
- body presentation redesign

Important distinction:

- CharacterVersion = durable approved appearance state.
- Continuity state = transient moment-specific state across scenes/shots.

Not every temporary visual change should create a new CharacterVersion.

## Wardrobe Boundary

Evidence review against options:

- Option A: Wardrobe belongs inside CharacterVersion.
  - Pros: clear linkage to durable approved appearance variants.
  - Risks: may over-version temporary wardrobe continuity changes.
- Option B: Wardrobe is an independent reusable Asset referenced by CharacterVersion.
  - Pros: reuse and composability across characters/versions.
  - Risks: adds asset-boundary complexity.
- Option C: Wardrobe is Continuity state only.
  - Pros: handles transient changes naturally.
  - Risks: weak support for durable approved wardrobe packages.
- Option D: Hybrid approach.
  - Durable wardrobe design package at CharacterVersion/Asset boundary;
    transient wear/use state in Continuity.

Current classification:

- Candidate direction: Option D (hybrid) is most evidence-consistent.
- ADR question: yes, final CharacterVersion vs wardrobe-asset partition likely
  needs architecture decision.
- Open question: minimum v1 boundary that avoids over-modeling while preserving
  continuity and reproducibility.

## Character References

CharacterReference semantics are provider-neutral and intentional.

Reference purposes may include:

- face
- full body
- turnaround
- side view
- three-quarter view
- expression
- wardrobe
- pose
- silhouette
- color/design reference

CharacterReference should support conceptual attributes such as:

- stable identity
- purpose/type
- approval state
- version association
- provenance context

Provider embeddings/features are not CharacterReference semantics.

## CharacterReference vs Artifact

Required distinction:

- CharacterReference = intentional production reference relationship.
- Artifact = imported/generated output with provenance.

A given artifact may be used as CharacterReference input,
but artifact identity is not equivalent to CharacterReference semantics.

## Multi-Reference Support

Based on CR-004 and REQ-CHAR-002 evidence:

- Character should support multiple references across lifecycle needs.
- CharacterVersion should support multiple references for approved appearance
  variants.
- No fixed reference-count limit is defined by this draft.

## Shot Relationship

Shot should reference:

- Character identity
- selected appearance/version context when needed
- shot-specific participation state

Shot-specific pose/action/blocking/expression in a moment must not be silently
promoted into persistent Character identity.

## Storyboard Relationship

Storyboard/panel contexts may visualize character appearance and use references,
but Storyboard does not own persistent Character identity.

Storyboard references remain planning/review representations linked back to
Character identity/version/reference context.

## Continuity Relationship

Layered separation:

Persistent Character identity
-> Approved appearance/version
-> Continuity state for production moment
-> Shot-specific presentation

Example evaluation:

- same Character
  - winter wardrobe version
    - coat removed in Scene 3
      - blood stain introduced in Shot 12

Ownership interpretation:

- same Character: Character identity layer
- winter wardrobe version: CharacterVersion or wardrobe-asset association
  (durable layer)
- coat removed in Scene 3: Continuity state (transient span-level)
- blood stain introduced in Shot 12: continuity/shot-moment presentation state

This draft does not implement Continuity modeling details.

## Provider-Specific Identity Representations

Out of core Character domain:

- ArcFace embedding
- SigLIP feature
- DINOv2 feature
- CLIP embedding
- PPR representation
- LoRA
- identity token
- ControlNet input
- provider-specific reference ID

These may later appear in provider/workflow generation representations,
not as Character core domain identity.

## Versioning

Version semantics should preserve traceability for:

- persistent Character design revisions
- CharacterVersion revisions
- reference updates/replacements
- approval/supersession context

Historical generation must remain traceable to Character/CharacterVersion/
CharacterReference state used at generation time.

Approved historical references and versions must not be silently mutated.

## Lifecycle / Approval

Conceptual lifecycle vocabulary:

- Draft
- In Review
- Approved
- Superseded

Lifecycle status in this draft:

- Conceptual vocabulary accepted at draft scope.
- Formal global state machine and transition rules remain open and may require
  ADR for cross-profile policy standardization.

## Provenance

Conceptual traceability chain:

Character
-> Version/Appearance
-> Reference
-> Shot usage
-> Prompt/Generation
-> Artifact

This specification does not duplicate detailed Artifact provenance design.

## Validation / Invariants

Evidence-supported invariants in this draft:

- Character identity is distinct from provider-specific embeddings/features/tokens.
- Character identity is distinct from transient shot-specific pose/action state.
- Character identity is distinct from continuity-moment state.
- CharacterReference identity/semantics is distinct from Artifact identity.
- Historical approved CharacterVersion and CharacterReference state is traceable
  and must not be silently overwritten.
- Provider-specific identity representations do not define Character ontology.

## Candidate Information Model

Conceptual only (no Django schema).

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| character_id | Stable persistent identity | CORE DOMAIN | Yes | Provider-independent production identity anchor. |
| character_code_or_name | Human production identity marker | CORE DOMAIN | Usually | Human-readable identity context; not implying DB design. |
| narrative_identity_context | Story-role identity semantics | CORE DOMAIN | Yes | Narrative role/identity context. |
| canonical_identity_traits | Stable identity traits | CORE DOMAIN | Yes | Stable cues, not transient shot state. |
| character_status | Lifecycle approval context | VERSIONED DOMAIN | Usually | Draft/review/approved/superseded context. |
| character_version_id | Durable approved appearance version identity | VERSIONED DOMAIN | Usually | Distinct from Character identity. |
| character_version_scope | Durable appearance boundary context | VERSIONED DOMAIN | Usually | Defines when version is intended to apply. |
| appearance_attributes | Mutable approved appearance details | VERSIONED DOMAIN | Usually | Wardrobe/hair/body/accessory durable layer where applicable. |
| wardrobe_context | Wardrobe boundary marker | DEFERRED | No | Candidate hybrid boundary with continuity/asset interplay. |
| character_reference_id | Stable reference relationship identity | REFERENCE | Usually | Distinct from artifact identity. |
| reference_purpose | Reference intent type | REFERENCE | Usually | Face/body/turnaround/expression/pose/wardrobe/silhouette etc. |
| reference_source_artifact_ref | Optional artifact linkage | REFERENCE | No | Artifact may back a reference; semantics remain distinct. |
| reference_version_links | Linkage to Character/CharacterVersion | REFERENCE | Usually | Supports multi-reference and version traceability. |
| reference_approval_state | Review/approval for reference use | REFERENCE | Usually | Human-reviewable production governance. |
| continuity_overlay_ref | Link to transient continuity state | CONTINUITY-OWNED | No | Continuity owns temporal/transient state. |
| shot_usage_ref | Link to shot-specific usage/presentation context | SHOT-OWNED | No | Shot owns moment-specific participation state. |
| provider_identity_payload_ref | Link to provider-specific identity representations | PROVIDER-SPECIFIC | No | Out of core Character ontology. |
| derived_qc_identity_summary | Derived consistency summary context | DERIVED | No | Does not redefine identity truth. |

## Candidate Requirements

Review of cross-layer requirements relevant to Character domain:

| Requirement | Classification in this draft | Rationale |
|---|---|---|
| CR-004: Separate Character identity from CharacterVersion/appearance state and support multi-reference character context | ACCEPT INTO DRAFT SPEC | Strong cross-layer support and direct Character domain relevance. |
| REQ-CHAR-001: Character identity should support multiple visual dimensions beyond face identity | ACCEPT INTO DRAFT SPEC | Supported by StoryMaker/InstantCharacter synthesis and production character consistency evidence. |
| REQ-CHAR-002: Character or CharacterVersion should support multiple reference assets | ACCEPT INTO DRAFT SPEC | Supported at candidate level; exact attachment boundary remains open but capability direction is evidence-supported. |

Interpretation rule:

- Accept into draft scope means accepted in this draft specification context only.
- It does not automatically accept project architecture or ADR decisions.

## ADR Review Points

Potential architecture questions (no ADR accepted here):

- Final Character vs CharacterVersion boundary policy.
- Wardrobe modeling boundary:
  - CharacterVersion-internal
  - independent wardrobe asset reference
  - hybrid model.
- CharacterReference modeling strategy:
  - dedicated entity
  - typed Artifact relation
  - hybrid approach.
- Identity/version/reference immutability and supersession policy guarantees for
  reproducibility-sensitive workflows.

## Open Questions

Minimum required questions:

- Q1: Character / CharacterVersion / Wardrobe boundary
  - What minimum v1 partition preserves reproducibility and continuity without
    over-modeling?
- Q2: CharacterReference modeling
  - Dedicated entity, typed Artifact relation, or hybrid?
- Q7: Multi-character representation impact
  - What Character-domain constraints are needed for scenes with three or more
    characters, without embedding provider workflow logic into Character?

Additional question:

- Does Continuity specification need to be prioritized next to resolve temporary
  appearance-state ownership (for example injury/wear/momentary outfit changes)?

## Out of Scope

Explicitly out of scope in this document:

- Django models, migrations, serializers, and SQL schema design.
- Embeddings, LoRA/adapters, and provider/model internals.
- Provider APIs and workflow implementation design.
- Prompt construction design.
- Final continuity implementation/state machine.
- Image generation algorithms or face-recognition implementation.
- Final QC algorithms and metric thresholds.

## Traceability

| Candidate decision / boundary | Evidence source | Evidence status |
|---|---|---|
| Character is persistent production identity, not provider representation | docs/DEVELOPMENT_SPEC.md principles; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CLA-004 and DP-004; docs/research/production/character-bible.md | Strong candidate-level support |
| Character identity separate from mutable appearance/version | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CR-004; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md RP-001 and RP-002 | Strong support |
| Multi-reference support for Character or CharacterVersion | docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md REQ-CHAR-002; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CR-004; docs/research/production/character-bible.md | Strong candidate-level support |
| CharacterReference must remain distinct from Artifact identity | docs/domain/shot.md artifact/provenance distinctions; docs/domain/storyboard.md panel vs artifact distinction; docs/research/production/character-bible.md | Moderate to strong support |
| Shot-specific pose/action state remains outside persistent identity | docs/domain/shot.md character participation and shot-specific state boundary; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md REQ-SHOT-001 and RP-002 | Strong support |
| Continuity remains conceptually separate from persistent identity | docs/research/production/continuity.md principles; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CLA-006 and Q1 | Strong candidate-level support |
| Provider-specific identity mechanisms remain out of core Character domain | AGENTS.md research/technology candidate governance; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md section 14 | Strong governance support |

## Specification Readiness

Stable in this draft:

- Character as provider-independent persistent production identity.
- Separation between persistent identity and mutable approved appearance state.
- Separation between CharacterReference semantics and Artifact identity.
- Multi-reference support direction without fixed reference count.
- Separation between persistent identity, shot-specific state, and continuity
  state.

Ambiguous or unresolved:

- Final CharacterVersion boundary granularity.
- Wardrobe ownership boundary (version, asset, continuity, or hybrid details).
- CharacterReference modeling shape (entity vs typed relation vs hybrid).

Likely ADR-needed before architecture freeze:

- CharacterVersion and Wardrobe boundary commitment.
- CharacterReference architectural modeling commitment.
- Immutability/supersession policy strictness level.

Likely Continuity-spec dependency:

- Temporary appearance-state ownership and transition semantics.

Research-unblocked determination:

- Character domain is research-unblocked for draft specification and incremental
  implementation planning.
- Final architecture closure remains partially blocked by boundary decisions,
  not by absence of baseline research evidence.

Need for new Layer 4 research:

- No new mandatory Layer 4 standards/software-architecture research is required
  to establish the current conceptual Character model.
- Potential future interoperability research may be useful later, but it is not
  a blocker for this draft.

## Layer 4 Research Requests

Current determination:

- No new blocking Layer 4 research request is introduced by this Character
  draft.

Potential non-blocking future candidate topic:

- Cross-tool character reference interchange semantics for optional integration
  profiles, if future implementation requires strict interoperability guarantees.
