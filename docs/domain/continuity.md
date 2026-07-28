# Continuity Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for drafting a provider-independent continuity domain baseline; partially blocked for final machine-checkable coverage policy and temporal alignment normalization detail.
- ADR Blocker Status: No immediate ADR blocker for publishing this draft; targeted ADR review may be required before freezing lifecycle/gating policy and state-representation commitments.
- Specification Type: Domain Specification
- Domain: Continuity
- Version: 1.0
- Evidence Basis:
  - System constraints and principles from docs/DEVELOPMENT_SPEC.md
  - Shot boundaries from docs/domain/shot.md
  - Storyboard boundaries from docs/domain/storyboard.md
  - Character boundaries from docs/domain/character.md
  - Cross-layer synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - AI synthesis continuity findings from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - Production continuity research from docs/research/production/continuity.md
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/domain/shot.md
  - docs/domain/storyboard.md
  - docs/domain/character.md
- Related Research:
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - docs/research/production/continuity.md
- Related ADRs:
  - No accepted ADR files were found under docs/adr/ in the current repository state.

Unresolved architecture choices remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

Define provider-independent continuity semantics for temporally scoped production
state across scenes/shots, including transition representation, issue tracking,
review/override concepts, and traceability to generation and artifacts.

## Domain Definition

Continuity is temporally scoped production state used to preserve narrative,
visual, spatial, and temporal coherence across shot/scene transitions.

Continuity is not:

- persistent Character identity
- durable CharacterVersion identity baseline
- local one-shot pose/action/blocking/expression moment
- provider prompt payload
- provider embeddings/tokens/attention features
- model/runtime hidden state

Layered distinction preserved:

- Character = persistent identity
- CharacterVersion = durable approved appearance state
- Continuity = temporally scoped production state across scenes/shots
- Shot-specific presentation = local moment expression within a shot
- Provider continuity mechanism = implementation detail

## Terminology

- Continuity State:
  - Temporally scoped production state used to carry relevant context across
    transitions.
- Transition:
  - Boundary relationship between adjacent or related production units where
    continuity is evaluated.
- Incoming Continuity State:
  - Relevant state expected at transition entry into a shot/scene span.
- Outgoing Continuity State:
  - Resulting state after a shot/scene span that may affect downstream units.
- Expected State:
  - Planned or approved continuity target for a transition context.
- Observed State:
  - State observed from storyboard/animatic/generated/reviewed artifact context.
- Continuity Discrepancy:
  - Material difference between expected and observed state.
- Intentional Change:
  - Deliberate approved deviation from prior continuity expectation.
- Continuity Issue:
  - Tracked discrepancy or unresolved risk requiring review/action/decision.
- Continuity Constraint:
  - Rule-like continuity expectation used for checking or review guidance.
- Continuity Review:
  - Human review action over continuity state/issue/transition context.
- Continuity Resolution:
  - Recorded handling outcome for continuity issue context.
- Continuity Scope:
  - Applicability range of continuity state (for example transition, scene span,
    project span).

Term policy:

- Terms are conceptual and do not force one table/entity per term.
- This draft avoids over-modeling while preserving explicit state semantics.

## Domain Responsibilities

Continuity owns or anchors:

- Explicit cross-shot/scene continuity state representation.
- Transition-based continuity comparison semantics.
- Continuity constraints as production-domain expectations.
- Continuity discrepancy and issue tracking.
- Human review and override decisions for continuity outcomes.
- Continuity state traceability over revisions and generation history.
- Linkage to storyboard planning continuity checks and generation context usage.

Continuity does not own:

- Character identity truth.
- CharacterVersion durable design ownership.
- Shot-local performance state unless temporally relevant beyond the shot.
- Provider-specific conditioning or model internals.

## Domain Boundaries

Boundary ownership summary:

- Character domain owns persistent identity.
- CharacterVersion owns durable approved appearance baseline.
- Shot domain owns shot-local pose/action/blocking/expression and shot intent.
- Continuity domain owns temporally scoped cross-shot/scene state and
  transition consistency tracking.
- Provider/workflow layers own provider-specific continuity implementation
  mechanisms.

Boundary rules:

- Continuity must not redefine Character identity.
- Continuity must not absorb all Shot-local state by default.
- Continuity stores only state with temporal relevance beyond a local moment.
- Not every temporary state change creates CharacterVersion.

## Continuity Scope

Conceptual continuity scope levels:

- Character scope:
  - transient character state relevant across transitions
  - examples: coat on/off, fresh blood stain persists, injury progression,
    temporary hairstyle change during sequence
- Asset/Prop scope:
  - carrying/placement/use state across shots
  - example: prop carried in right hand entering next shot
- Location/Environment scope:
  - evolving environment state
  - examples: broken window persists, door now open, weather/wet ground change
- Shot-transition scope:
  - direct boundary expectations from shot A to shot B
  - examples: screen direction continuity, carry state continuity
- Scene-span scope:
  - continuity expectations across multiple ordered shots in one scene
  - examples: time-of-day progression, sustained injury visibility
- Project-span scope:
  - longer-range continuity expectations
  - examples: persistent scars after injury arc, environment damage across scenes

Scope policy:

- The minimum required continuity scope in early milestones should center on
  shot-transition and scene-span contexts.
- Character/project-span continuity remains conceptually supported but can be
  introduced incrementally.

## Character Relationship

Character relationship rule:

- Continuity references Character identity but does not own or redefine it.

Allowed continuity use:

- link continuity state to Character identity for temporal tracking
- compare expected vs observed continuity state involving a character

Disallowed continuity use:

- rewriting Character canonical identity traits
- storing provider identity embeddings/features as continuity truth

## CharacterVersion Relationship

CharacterVersion relationship rule:

- Continuity may reference CharacterVersion as baseline appearance context.
- Continuity captures temporary or transition-scoped deviations around that
  baseline.

Examples:

- CharacterVersion baseline hairstyle is long braid.
- Continuity scene-span note: braid becomes loose after chase and remains loose
  through next two shots.

Important boundary:

- Temporary deviations do not automatically create new CharacterVersion.
- Durable approved appearance redesign belongs to CharacterVersion lifecycle.

## Shot Relationship

Shot relationship rule:

- Continuity attaches to shot transitions and shot-span temporal effects.
- Shot retains local moment performance ownership.

Temporal relevance filter:

- if local shot state has no expected downstream impact, keep it shot-local.
- if local shot state affects later continuity expectations, capture it as
  outgoing continuity state.

Examples:

- local smile expression in one shot: usually shot-local only.
- blood stain introduced in shot 12 and visible in shot 13: continuity state.
- screen direction established in shot 5 and expected in shot 6: continuity
  constraint/state.

## Storyboard Relationship

Storyboard is a planning/review surface for continuity, not continuity domain
replacement.

Storyboard interactions:

- continuity checks can begin at panel/reel/animatic stages.
- storyboard continuity notes/issues can map to continuity issue records.
- storyboard revisions can update expected continuity state before generation.

Boundary:

- storyboard owns planning artifacts and revision lifecycle.
- continuity owns continuity state/issues/transition semantics.

## State Representation

Continuity state representation principles:

- state must be explicit and structured enough for traceable comparison.
- state must avoid becoming one unstructured global JSON blob.
- state should support typed segments by scope (character/prop/environment/
  transition/scene span), without forcing each segment into separate entities.

State mutation models considered:

- Snapshot-only model:
  - Pros: simple current-state access.
  - Risks: weak explainability of how state changed over time.
- Delta/event-only model:
  - Pros: rich transition history.
  - Risks: may overcomplicate early milestones and create heavy replay burden.
- Hybrid model (candidate direction):
  - Maintain reviewable state snapshots for key boundaries/stages.
  - Record bounded transition deltas for traceable change intent.

Current classification:

- Candidate direction: hybrid snapshot + bounded delta representation.
- Rationale: aligns with traceability and review needs without requiring full
  event-sourcing architecture.
- Constraint: do not introduce full event-sourcing model at this stage.

## Incoming / Outgoing State

Incoming continuity state:

- expected state entering a shot/scene boundary derived from prior approved
  outgoing state and applicable constraints.
- may include character, prop, environment, temporal, and directional context.

Outgoing continuity state:

- resulting continuity-relevant state after shot/scene completion and review.
- supplies candidate baseline for downstream incoming state.

Examples:

- coat on/off
  - incoming: coat on
  - observed: coat off without planned change
  - result: discrepancy unless intentional change approved
- blood stain appears
  - outgoing from shot 12: stain present on jacket left sleeve
  - incoming to shot 13 expected to include stain unless resolved in story action
- prop carried between shots
  - outgoing shot A: prop in right hand
  - incoming shot B expected: prop remains carried unless transition explains drop

## Transition Semantics

Transition representation should support:

- source context and target context linkage (for example shot A -> shot B).
- applicable continuity scopes (character, prop, environment, temporal,
  directional).
- expected state and observed state comparison basis.
- outcome classification (consistent, intentional change, discrepancy, pending).
- provenance of who/when/how transition assessment was recorded.

Transition context may include:

- adjacent shot transitions
- non-adjacent but linked narrative transitions
- scene-entry or scene-exit transitions

## Continuity Constraints

Continuity constraints are production-domain expectations, not provider features.

Constraint categories (conceptual):

- Character appearance continuity:
  - coat on/off, hairstyle continuity, injury persistence across relevant span
- Prop continuity:
  - carry state, placement state, hand assignment continuity
- Environment continuity:
  - damage persistence, object arrangement persistence, weather/wetness state
- Temporal continuity:
  - time-of-day progression consistency and declared transition coherence
- Spatial/screen-direction continuity:
  - left-right orientation coherence, movement direction continuity
- Narrative cause/effect continuity:
  - state changes must be explainable by prior or current narrative action

Constraint policy:

- constraints can be machine-checkable, human-reviewed, or both.
- constraints remain provider-independent at domain level.
- provider/workflow adapters may translate constraints into execution checks.

## Continuity Issues

ContinuityIssue concept:

- A tracked record of unresolved continuity discrepancy or risk linked to
  transition/state evidence and review provenance.

Conceptual distinction:

- expected continuity state:
  - approved/planned target continuity state
- observed/generated state:
  - state seen in planning or generation outputs
- continuity discrepancy:
  - mismatch between expected and observed states
- accepted intentional change:
  - mismatch accepted as deliberate narrative/production decision
- unresolved issue:
  - discrepancy not yet accepted or corrected

Issue attributes (conceptual):

- scope and affected entities/references
- expected vs observed summary
- issue significance/severity context
- review/provenance context
- resolution status context

## Human Review / Override

Human review is mandatory conceptually for non-trivial continuity decisions.

Review outcome vocabulary (conceptual, non-final):

- confirmed
- intentional deviation
- needs correction
- unresolved

Review semantics:

- confirmed:
  - expected and observed continuity considered acceptable
- intentional deviation:
  - change is accepted deliberate production decision
- needs correction:
  - discrepancy should trigger corrective planning/generation action
- unresolved:
  - insufficient evidence or decision pending

Override semantics:

- reviewers can explicitly accept intentional deviation with rationale.
- overrides must preserve provenance and must not silently erase discrepancy
  history.

## Lifecycle

Candidate continuity lifecycle vocabulary (conceptual):

- State Planned
- State Evaluated
- Issue Raised
- Issue Reviewed
- Issue Resolved
- Issue Reopened
- Transition Approved

Lifecycle status in this draft:

- Conceptual lifecycle vocabulary accepted into draft scope.
- Formal state machine, severity-to-gate mapping, and mandatory transition
  policy remain open and may require ADR/policy work.

## Versioning / History

Continuity history requirements:

- continuity-relevant state changes must be historically traceable.
- issue state transitions must preserve revision lineage.
- approved historical continuity records must not be silently overwritten.
- later generation must be traceable to continuity context in effect at run
  time.

History model note:

- this draft does not require full event sourcing.
- a bounded hybrid history approach is sufficient for v1 candidate direction.

## Provenance

Continuity provenance should support:

- reviewer identity or responsible actor context
- timestamps
- linked storyboard/animatic/generation artifact references
- transition boundary references
- rationale for intentional deviations or approvals

Traceability chain (conceptual):

Character/CharacterVersion baseline
-> Continuity expected state
-> Transition evaluation
-> Continuity issue/review outcome
-> Generation context consumption
-> Generated artifact

## Machine-Checkable vs Human-Reviewed

Machine-checkable candidate core (early milestones):

- explicit carry-state continuity for selected props
- obvious binary appearance continuity flags (for example coat on/off)
- simple injury persistence flag where required by continuity span
- explicit screen-direction consistency checks in constrained contexts
- declared time-of-day progression consistency where structured metadata exists

Primarily human-reviewed or mixed:

- nuanced narrative cause/effect coherence
- complex blocking/composition continuity interpretation
- subtle appearance drift judgments
- intentional stylistic deviations requiring director/producer judgment

Policy note:

- exact machine-checkable coverage remains open question Q4 and should be
  expanded incrementally with evidence.

## Validation / Invariants

Evidence-supported invariants in this draft:

- Continuity is explicit tracked state, not implicit prompt-only memory.
- Continuity state is distinct from Character persistent identity.
- Continuity state is distinct from CharacterVersion durable approved baseline.
- Continuity state is distinct from shot-local moment state unless temporal
  relevance extends beyond local shot context.
- Continuity issues are transition/state discrepancies with explicit review
  provenance.
- Provider-specific continuity representations do not define continuity domain
  ontology.
- Historical continuity context used by generation remains traceable.

## Candidate Information Model

Conceptual only (no Django schema).

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| continuity_context_id | Stable continuity context identity | CORE DOMAIN | Yes | Provider-independent continuity identity anchor. |
| continuity_scope_type | Scope classification for state applicability | CORE DOMAIN | Yes | Character, asset/prop, environment, transition, scene span, project span. |
| scope_target_refs | References to scoped subjects/assets/locations | REFERENCE | Usually | Supports scoped continuity tracking without forcing one entity per example. |
| transition_ref | Source-target boundary linkage | CORE DOMAIN | Usually | Shot/scene transition context for evaluation. |
| expected_state_summary | Planned/approved continuity expectation | CORE DOMAIN | Yes | Structured summary, not provider payload. |
| observed_state_summary | Observed continuity evidence summary | CORE DOMAIN | Usually | Derived from storyboard/animatic/generated artifact review. |
| outgoing_state_summary | State emitted for downstream continuity context | CORE DOMAIN | Usually | Baseline candidate for next incoming state. |
| incoming_state_summary | State expected at transition entry | CORE DOMAIN | Usually | Derived from prior outgoing + approved changes. |
| state_representation_mode | Snapshot/delta/hybrid declaration | CORE DOMAIN | Yes | Candidate direction is hybrid; no full event sourcing commitment. |
| continuity_constraint_refs | Applicable continuity expectations | REFERENCE | No | Links to constraint concepts/rules. |
| continuity_issue_id | Stable issue identity | ISSUE DOMAIN | No | Present when discrepancy/risk exists. |
| discrepancy_summary | Expected-vs-observed mismatch summary | ISSUE DOMAIN | No | Required for issue records. |
| issue_status_context | Issue progression state | ISSUE DOMAIN | No | Conceptual state vocabulary only in this draft. |
| issue_resolution_context | Resolution/override context | ISSUE DOMAIN | No | Distinguishes correction vs intentional deviation acceptance. |
| review_outcome_context | Human review outcome | REVIEW DOMAIN | No | confirmed / intentional deviation / needs correction / unresolved (conceptual). |
| review_rationale | Human decision rationale | REVIEW DOMAIN | No | Important for intentional deviations. |
| provenance_context | Reviewer/time/source evidence context | CORE DOMAIN | Yes | Supports audit/reproducibility. |
| storyboard_link_refs | Linkage to storyboard panels/revisions | REFERENCE | No | Continuity checks begin in planning artifacts. |
| generation_context_refs | Linkage to generation tasks/attempts/results | REFERENCE | No | Supports continuity-to-generation traceability. |
| provider_continuity_payload_ref | Link to provider-specific continuity mechanisms | PROVIDER-SPECIFIC | No | Explicitly out of core continuity ontology. |

## Candidate Requirements

Review of continuity-relevant requirements:

| Requirement | Classification in this draft | Rationale |
|---|---|---|
| CR-006: Represent continuity explicitly with structured state/issues at shot transitions, including status and review provenance | ACCEPT INTO DRAFT SPEC | Strong cross-layer support from domain foundation and production continuity synthesis. |
| REQ-CONT-001: Long-form generation should support stable reference context across multiple production segments | ACCEPT INTO DRAFT SPEC | Supported by AI synthesis and continuity-as-production-state findings. |
| REQ-CONT-002: Later generation should be able to receive relevant historical production context | ACCEPT INTO DRAFT SPEC | Supported by AI synthesis; aligns with traceability and context selection needs. |
| DP-006: Explicit continuity state as stable domain principle | ACCEPT INTO DRAFT SPEC | Cross-layer synthesis indicates strong support for explicit continuity representation. |

Interpretation rule:

- Accept into draft scope means accepted in this continuity draft context only.
- It does not automatically accept project-wide architecture or ADR decisions.

## ADR Review Points

Potential architecture questions (no ADR accepted here):

- Whether continuity lifecycle should be standardized as a strict state machine
  versus profile-specific policy.
- How strict continuity issue severity should map to production gates.
- Final commitment level for hybrid state model details (snapshot cadence,
  delta granularity, retention policy).
- Minimum temporal alignment model (including optional timecode references)
  for cross-artifact continuity review reproducibility.

## Open Questions

Required open questions:

- Q4: Which continuity constraints are machine-checkable in early milestones
  versus human-review-only?
- Q10: What minimum temporal/synchronization schema is needed for reproducible
  cross-provider review alignment?

Additional continuity-focused questions:

- What minimal hybrid state representation should be mandatory at v1 to avoid
  both opaque blobs and over-complex event replay?
- Which continuity scopes are mandatory in v1 (transition, scene span) versus
  optional extensions (project span)?
- How should unresolved continuity issues influence downstream generation gates
  under different production profiles?

## Out of Scope

Explicitly out of scope in this document:

- Django models, serializers, migrations, and SQL schema design.
- Workflow orchestration implementation and gate engine logic.
- QC algorithm implementation or scoring thresholds.
- Provider/model-specific continuity payload design.
- Embeddings, attention maps, history tokens, or model internals as domain
  continuity concepts.
- Final Artifact/Provenance schema implementation details.
- Acceptance of architecture decisions through ADRs.

## Traceability

| Candidate decision / boundary | Evidence source | Evidence status |
|---|---|---|
| Continuity as explicit tracked cross-stage state | docs/research/production/continuity.md principles; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CLA-006 and DP-006; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md finding 4 | Strong candidate-level support |
| Continuity issue tracking at shot transitions with status/provenance | docs/research/production/continuity.md candidate requirements; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CR-006; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md consolidated candidate requirements | Strong support |
| Continuity begins in storyboard/animatic review, not only final outputs | docs/research/production/continuity.md workflow and principles; docs/domain/storyboard.md continuity relationship | Moderate to strong support |
| Continuity distinct from Character identity and CharacterVersion durable baseline | docs/domain/character.md layering and invariants; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md DP-004 and Q1 | Strong support |
| Continuity distinct from Shot-local moment presentation unless temporally relevant | docs/domain/shot.md shot-specific state boundary and continuity linkage; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md RP-002 and continuity implications | Strong support |
| Continuity context should be consumable by later generation steps | docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md REQ-CONT-001 and REQ-CONT-002 | Strong candidate-level support |
| Provider-specific continuity mechanisms remain outside core continuity ontology | AGENTS.md technology-candidate governance; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md section 10 and section 14 | Strong governance support |
| Historical continuity context used by generation must remain traceable | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CLA-008 and CR-008 direction; docs/research/production/continuity.md production records guidance | Moderate to strong support |

## Specification Readiness

Stable in this draft:

- Continuity meaning as explicit cross-shot/scene tracked production state.
- Layered boundary separation across Character, CharacterVersion, Continuity,
  Shot-local presentation, and provider mechanisms.
- Incoming/outgoing state semantics and transition-centered evaluation model.
- Continuity issue concept and expected/observed/discrepancy/intentional-change/
  unresolved distinctions.
- Human review and override outcomes represented conceptually with provenance.
- Historical continuity traceability requirements for generation context usage.

Ambiguous or unresolved:

- Exact mandatory continuity scope set for initial implementation profile.
- Exact hybrid representation mechanics (snapshot cadence and delta depth).
- Exact severity-to-gate policy and final lifecycle state machine.
- Exact minimal temporal alignment schema for cross-provider reproducibility.

Likely ADR-needed before architecture freeze:

- Lifecycle/gating policy standardization level.
- Severity-to-gate mapping policy.
- Temporal alignment policy strictness.

Research-unblocked determination:

- Continuity domain is research-unblocked for draft specification and
  incremental implementation planning.
- Final architecture closure remains partially blocked by policy commitments,
  not by absence of baseline continuity evidence.

## Layer 4 Research Requests

Current determination:

- No new blocking Layer 4 standards/software-architecture research request is
  required to establish this continuity draft.

Potential non-blocking future candidate topic:

- Comparative temporal alignment/interchange profiling for continuity review
  portability, if future cross-tool interoperability becomes a concrete
  implementation requirement.
