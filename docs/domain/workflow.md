# Workflow Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for drafting a provider-independent workflow domain baseline; retry/attempt and idempotency research blockers are resolved at Proposed ADR level, while implementation planning remains contingent on ADR acceptance.
- ADR Blocker Status: No immediate ADR blocker for publishing this draft; targeted ADR acceptance remains required before freezing retry/idempotency policy commitments.
- Specification Type: Domain Specification
- Domain: Workflow
- Version: 1.0
- Evidence Basis:
  - System constraints and principles from docs/DEVELOPMENT_SPEC.md
  - Shot boundaries from docs/domain/shot.md
  - Storyboard boundaries from docs/domain/storyboard.md
  - Character boundaries from docs/domain/character.md
  - Continuity boundaries from docs/domain/continuity.md
  - Cross-layer synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - Standards/architecture synthesis from docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - AI workflow findings from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - Production pipeline research from docs/research/production/animation-production-pipeline.md
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/domain/shot.md
  - docs/domain/storyboard.md
  - docs/domain/character.md
  - docs/domain/continuity.md
- Related Research:
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - docs/research/production/animation-production-pipeline.md
  - docs/research/official/README.md (planned source list only; no Celery/Redis technical record yet)
- Related ADRs:
  - docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed)
  - docs/adr/ADR-0002-idempotency-contract.md (Proposed)

Unresolved architecture choices remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

Define provider-independent workflow semantics for production-stage orchestration,
versioned workflow definitions, execution runs, review gates, rework loops,
failure/retry concepts, and traceability.

## Domain Definition

Workflow is the production-process domain that organizes how structured
production intent moves through planned stages, review decisions, generation
execution, and revision cycles.

Workflow is not:

- provider workflow graph
- ComfyUI node graph
- GenerationTask itself
- Celery task
- queue/broker message
- direct provider API request

Workflow is the broader orchestration/process definition around domain context.

Conceptual layering:

Production Intent
-> WorkflowDefinition
-> WorkflowVersion
-> WorkflowRun
-> Domain/Generation Steps
-> Provider Adapter Execution
-> Results / Artifacts / Review

## Terminology

- Workflow:
  - Domain concept representing orchestrated production process intent.
- WorkflowDefinition:
  - Stable workflow identity and purpose boundary.
- WorkflowVersion:
  - Immutable versioned workflow specification used by execution runs.
- WorkflowRun:
  - One execution instance of a specific WorkflowVersion against specific
    production context.
- Workflow Step:
  - A conceptual unit of work within WorkflowVersion stage/step structure.
- Production Stage:
  - Domain-level lifecycle segment (planning/review/generation/continuity/
    approval and related stage groups).
- Stage Gate:
  - Explicit review/decision checkpoint controlling transition across stages.
- Rework Loop:
  - Structured return path from review/gate outcome back to earlier stage(s).
- Step Attempt:
  - One attempt to execute or complete a workflow step in a run context.
- Retry:
  - Re-execution action at defined scope (attempt/step/subprocess) after failure
    or non-acceptance.
- Failure:
  - Unsuccessful workflow step/run outcome requiring retry, rework, or stop.
- Cancellation:
  - Intentional termination of pending/in-progress run scope.
- Provider Workflow:
  - Provider/runtime-specific execution graph or parameterized process outside
    core Workflow domain ontology.
- GenerationTask:
  - Generation-subsystem execution request linked to workflow steps but not
    equivalent to Workflow.

Term policy:

- Names are conceptual and not binding class/table/API names.
- This draft does not force implementation naming commitments.

## Domain Responsibilities

Workflow owns or anchors:

- Versioned workflow process definitions.
- Stage and step sequencing semantics.
- Review gate and transition decision semantics.
- Rework/revision loop semantics.
- Run-level execution tracking across stage/step outcomes.
- Run-level linkage to generation requests/tasks/results.
- Workflow provenance and reproducibility-oriented traceability.
- Context intake from Shot/Storyboard/Character/Continuity domains.

Workflow does not own:

- provider graph/node schemas
- queue runtime semantics
- worker execution internals
- transport/API mechanics
- generated artifact binary payload storage

## Domain Boundaries

Core separation rules:

- Production Workflow != Provider Workflow.
- Production Workflow != ComfyUI Graph.
- Workflow != GenerationTask.
- Workflow != Celery Task.
- Workflow != API Request.

Boundary ownership summary:

- Workflow domain owns process intent, stage semantics, gates, and run lineage.
- Generation subsystem owns generation task/attempt/result execution details.
- Provider adapters own provider-specific graph/parameter translation.
- Infrastructure layer owns queueing, worker scheduling, retries at runtime,
  and transport concerns.

## Workflow Definition

Candidate definition:

- WorkflowDefinition is the stable identity/purpose envelope of a workflow
  family, independent from mutable implementation evolution.

Expected responsibilities:

- stable semantic purpose (for example storyboard-previs, shot-image generation,
  continuity-check pass, composite production profile)
- compatibility scope and domain applicability metadata
- version lineage anchor

Boundary:

- WorkflowDefinition does not store mutable run-time step outcomes.
- WorkflowDefinition does not carry provider-specific graph payloads.

Evidence assessment:

- This definition is consistent with cross-layer requirements for versioned,
  traceable, provider-neutral workflows and stage-gated pipeline modeling.

## Workflow Version

Candidate definition:

- WorkflowVersion is an immutable, executable/configurable version of
  WorkflowDefinition used by WorkflowRun.

WorkflowVersion characteristics:

- explicit version identity
- stage/step structure snapshot
- gate configuration snapshot (at conceptual policy level)
- input contract and required context declarations
- mapping contract to generation/provider adapter layers

Immutability rule:

- Historical runs must remain traceable to exact WorkflowVersion.
- WorkflowVersion used by completed/in-progress historical runs must not be
  silently mutated.

Revision rule:

- Behavioral changes require a new WorkflowVersion.

## Workflow Run / Execution

WorkflowRun definition:

- One run instance binds a specific WorkflowVersion to specific production
  context and records step outcomes, decisions, retries, rework transitions,
  and terminal state.

WorkflowRun should conceptually include:

- run identity
- bound workflow version reference
- bound production context references
- stage/step progress and outcome lineage
- review gate outcomes
- failure/retry history
- cancellation context when applicable
- provenance metadata and linked generation/artifact references

WorkflowRun boundary:

- WorkflowRun is not equivalent to one GenerationTask.
- A run may include zero/one/many generation-related steps depending on
  workflow purpose.

## Production Stage Model

Production-stage evidence supports stage-based lifecycle with review/rework
loops, while preserving profile-specific flexibility.

Candidate stage model (conceptual):

- Planning Stage
- Context/Asset Binding Stage
- Previsualization/Storyboard Stage
- Generation Preparation Stage
- Generation Stage
- Review/QC/Continuity Evaluation Stage
- Approval/Release-to-next-stage Stage

Stage policy:

- Not all stages are mandatory for all project profiles.
- Mandatory/optional stage sets are policy/profile concerns, not hard-coded
  global ontology in this draft.

## Step Semantics

Workflow steps are conceptual units inside stages.

Step semantics should support:

- declared intent and expected outputs
- declared required context
- dependency order/precedence constraints
- outcome statuses and attempt lineage
- optional generation substep linkage
- gate preconditions/postconditions

Step scope levels (conceptual):

- domain planning/review steps
- generation invocation steps
- continuity/review decision steps
- approval transition steps

This draft does not enforce one universal status taxonomy.

## Input Context

Workflow consumes structured production context, not free-form provider payloads.

Input context categories (conceptual):

- narrative and production scope context
- shot intent and ordering context
- storyboard planning/revision context
- character identity/version/reference context
- continuity incoming/outgoing state and issue context
- optional style/location/asset context
- prior run/revision context when rework occurs

Context selection rule:

- relevant context should be selected intentionally, not by blindly passing all
  historical outputs.

## Shot Relationship

Workflow and Shot relationship:

- Shot remains primary production execution unit and traceability anchor.
- Workflow steps may operate at shot scope or multi-shot scope.
- Workflow must not redefine Shot ontology.

Expected linkage:

- workflow step context references shot identity/intent
- generation steps may produce shot-linked GenerationTasks and artifacts

## Storyboard Relationship

Workflow and Storyboard relationship:

- storyboard-related workflows support planning/review/revision loops.
- storyboard outputs and approvals may feed downstream generation stages.
- storyboard remains planning/review domain, not provider execution definition.

## Character Relationship

Workflow and Character relationship:

- workflows consume Character identity and CharacterVersion context.
- workflows must preserve Character/CharacterVersion boundary semantics.
- provider-specific identity mechanisms remain outside workflow domain truth.

## Continuity Relationship

Workflow and Continuity relationship:

- workflows consume continuity state/constraints/issues for relevant stages.
- review stages may produce continuity review outcomes and rework triggers.
- continuity domain remains owner of continuity state semantics.

## GenerationTask Relationship

Required separation:

- Workflow is broader orchestration and lifecycle context.
- GenerationTask is generation-subsystem execution request.

Relationship semantics:

- workflow generation step may create or reference GenerationTask(s).
- one workflow run may involve multiple GenerationTasks.
- one GenerationTask can be retried/attempted without redefining workflow
  identity.
- workflow-level rework can trigger new GenerationTasks in later cycles.

Proposed ADR direction (pending acceptance of ADR-0001):

- GenerationTask represents generation request intent.
- GenerationAttempt represents an application-defined logical execution
  attempt.
- infrastructure retry/redelivery does not automatically create a new
  GenerationAttempt.
- rework transition itself does not create a GenerationAttempt.
- a new GenerationAttempt is created when the application deliberately
  re-enters generation execution.
- human-requested regeneration remains distinct from infrastructure retry.

## Provider Workflow Relationship

Provider workflow semantics (out of core domain):

- ComfyUI graphs/nodes
- provider parameter mappings
- provider API call plans
- runtime execution graph details

Production Workflow semantics (core domain):

- stage/step intent
- review gates
- rework loops
- context contracts
- provenance and version traceability

Boundary rule:

- Production Workflow describes what/why/when in production process terms.
- Provider workflow describes how a specific provider executes substeps.

## Review Gates

Review gates are explicit decision checkpoints between stages/step groups.

Gate outcomes (conceptual):

- pass/approved
- revision required
- blocked/pending
- conditionally approved

Gate policy constraints:

- gate rules can vary by project profile.
- this draft does not make all gates globally mandatory.
- gate outcomes should preserve provenance and rationale context.

## Rework / Revision Loops

Rework loops are first-class workflow semantics.

Rework loop behavior (conceptual):

- review/gate outcomes can route run flow back to earlier steps/stages.
- rework should preserve historical lineage, not overwrite prior outcomes.
- multiple rework cycles may exist in one run lifecycle.

Common rework triggers:

- storyboard revision requested
- continuity discrepancy unresolved
- generation output fails review expectations
- approval criteria not met

## Failure / Retry Semantics

Retry/failure distinctions must remain explicit.

Conceptual distinctions:

- transport redelivery:
  - broker/runtime delivery repetition for the same underlying operation
    context
- infrastructure retry:
  - infrastructure/runtime-level re-execution for reliability without automatic
    new business intent
- workflow step retry:
  - workflow-level re-run of a specific step in run lineage under policy
- GenerationAttempt:
  - application-defined logical generation execution attempt associated to
    GenerationTask intent
- workflow rework loop:
  - stage-level or multi-step return path after review/gate outcome
- human-requested regeneration:
  - deliberate user/business re-run intent, distinct from runtime reliability
    retry

Failure representations (conceptual):

- step failure
- gate failure/non-approval
- run terminal failure
- partial failure with recoverable path

This draft does not finalize implementation-level retry/idempotency mechanics.

Proposed ADR direction (pending acceptance of ADR-0001):

- infrastructure retry/redelivery does not automatically create a new
  GenerationAttempt.
- rework itself does not create a GenerationAttempt.
- deliberate re-entry into generation execution can create a new
  GenerationAttempt.
- human regeneration remains distinct from infrastructure retry and from
  transport redelivery.

## Idempotency Boundary

Proposed ADR direction (pending acceptance of ADR-0002):

- idempotency is owned at the application operation boundary.
- infrastructure task IDs and provider request IDs do not define logical
  operation identity.
- duplicate-aware handling is required for side-effectful execution.
- deliberate new GenerationAttempt or regeneration must not be suppressed as
  accidental duplicate execution.
- provider-side uncertainty requires reconciliation before unsafe replay.

This draft does not define idempotency key composition, hashing, database
schema, Redis locking, or Celery configuration.

## Cancellation

Cancellation semantics (conceptual):

- run cancellation:
  - intentional stop of pending/in-progress workflow run
- step cancellation:
  - intentional stop of a specific step scope
- downstream cancellation propagation policy:
  - open design question, policy/profile dependent

Cancellation records should preserve:

- actor/request context
- timestamp
- affected scope
- rationale

## Lifecycle

Candidate workflow lifecycle vocabulary (conceptual):

- Draft Definition
- Active Definition
- Superseded Definition
- Run Created
- Run In Progress
- Run Awaiting Review
- Run In Rework
- Run Completed
- Run Failed
- Run Cancelled

Lifecycle status in this draft:

- conceptual lifecycle vocabulary accepted into draft scope
- formal state machine and transition policy remain open and may require ADR
  for cross-profile standardization

## Versioning / Immutability

Versioning rules:

- WorkflowDefinition identity is stable across versions.
- WorkflowVersion is immutable once used by a run.
- run history must reference exact workflow version identity.
- revisions produce new version records rather than mutating historical ones.

Immutability boundaries:

- immutable: versioned process structure and declared contracts used by runs
- mutable via new version: stage/step structure, gate policy configuration,
  context contract details

## Provenance

Workflow provenance should support:

- trace from production context to workflow version and run
- step/gate outcomes with actor/time/rationale context
- linkage from workflow steps to generation tasks/attempts/results
- linkage from run outcomes to artifacts and review decisions
- reproducibility analysis across reruns/revisions

Conceptual provenance chain:

Production Context
-> WorkflowDefinition
-> WorkflowVersion
-> WorkflowRun
-> Step/Gate Outcomes
-> GenerationTask/Attempt/Result (where applicable)
-> Artifact/Review Outcomes

## Validation / Invariants

Evidence-supported invariants in this draft:

- Workflow is distinct from provider workflow runtime details.
- Workflow is distinct from GenerationTask.
- Workflow versions used by historical runs are immutable and traceable.
- Stage-based process with review/rework semantics is explicit.
- Provider-specific graphs/parameters are outside core Workflow ontology.
- Rework and retry history must preserve lineage rather than destructive
  overwrite.
- Shot remains canonical production unit even when workflows span multiple shots.

## Candidate Information Model

Conceptual only (no Django schema).

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| workflow_definition_id | Stable workflow identity anchor | CORE DOMAIN | Yes | Represents workflow family/purpose identity. |
| workflow_definition_purpose | Production purpose description | CORE DOMAIN | Yes | Planning/review/generation orchestration intent. |
| workflow_definition_scope | Applicable production scope/profile context | CORE DOMAIN | Usually | Supports profile-aware stage/gate interpretation. |
| workflow_version_id | Immutable executable version identity | VERSIONED DOMAIN | Yes | Must be traceable from every run. |
| workflow_version_semantics | Versioned stage/step contract snapshot | VERSIONED DOMAIN | Yes | Conceptual process structure. |
| workflow_version_gate_policy_ref | Versioned gate policy reference | VERSIONED DOMAIN | Usually | Policy profile dependent. |
| workflow_version_input_contract | Declared required input context | VERSIONED DOMAIN | Yes | Shot/storyboard/character/continuity context expectations. |
| workflow_run_id | Run instance identity | RUN DOMAIN | Yes | One execution instance of specific version. |
| run_bound_version_ref | Bound WorkflowVersion reference | RUN DOMAIN | Yes | Immutable relationship for traceability. |
| run_context_refs | References to production context | RUN DOMAIN | Yes | Shot/scene/storyboard/asset/continuity context links. |
| run_stage_progress | Stage-level progress/outcome lineage | RUN DOMAIN | Usually | Supports stage-gated lifecycle visibility. |
| step_execution_records | Step attempts/outcomes and timestamps | RUN DOMAIN | Usually | Includes retry/rework lineage context. |
| gate_decision_records | Review gate outcomes and rationale | REVIEW DOMAIN | No | Pass/revise/block context with provenance. |
| rework_cycle_refs | Rework loop lineage markers | RUN DOMAIN | No | Supports iterative cycle traceability. |
| failure_records | Failure context and classification | RUN DOMAIN | No | Recoverable vs terminal context. |
| retry_records | Retry action lineage context | RUN DOMAIN | No | Distinguish step retry vs generation attempt context. |
| cancellation_record | Cancellation context | RUN DOMAIN | No | Actor/time/reason/scope. |
| generation_task_links | Links to generation subsystem execution | REFERENCE | No | Workflow != GenerationTask; linkage only. |
| artifact_outcome_links | Links to resulting artifacts/reviews | REFERENCE | No | Supports end-to-end traceability. |
| provider_execution_ref | Reference to provider runtime payload/graph | PROVIDER-SPECIFIC | No | Out of core workflow ontology. |
| provenance_context | Traceability metadata | CORE DOMAIN | Yes | Actor/time/source/rationale linkage. |

## Candidate Requirements

Review of workflow-relevant requirements:

| Requirement | Classification in this draft | Rationale |
|---|---|---|
| CR-007: Support hierarchical, stage-based production and generation workflows with explicit review gates and rework loops | ACCEPT INTO DRAFT SPEC | Strong cross-layer support from domain-foundation and production pipeline synthesis. |
| CR-008: Preserve workflow/artifact provenance and version history for reproducibility and auditability | ACCEPT INTO DRAFT SPEC | Strong support across development principles and synthesis evidence. |
| CR-005: Keep production intent provider-neutral and map provider execution through adapters | ACCEPT INTO DRAFT SPEC | Core architectural boundary and provider-independence requirement. |
| REQ-WF-001: Workflow selection may consider production context | ACCEPT INTO DRAFT SPEC | Supported by AI synthesis workflow context findings. |
| REQ-WF-002: Workflows should support specialization by context (for example character count/complexity) | ACCEPT INTO DRAFT SPEC | Supported by AI synthesis; remains policy/configuration concern. |
| REQ-WF-BOARD-001: Support fast previsualization-oriented storyboard workflows | ACCEPT INTO DRAFT SPEC | Supported by storyboard-first planning evidence and AI synthesis candidate requirement. |

Interpretation rule:

- Accept into draft scope means accepted in this workflow draft context only.
- It does not automatically accept project-wide architecture or ADR decisions.

## ADR Review Points

Potential architecture questions (no ADR accepted here):

- Should there be one global workflow run state machine or profile-specific
  state machine variants?
- Which stage gates are mandatory by production profile (short-form, episodic,
  feature-like)?
- How should retry/idempotency policy be standardized across workflow and
  generation boundaries?
- What minimum observability contract is required for workflow-run diagnostics?
- How strict should cancellation propagation semantics be across linked steps
  and generation requests?

## Open Questions

Key open questions:

- Q6: Should auxiliary anchors/keyframes be modeled as workflow state,
  shot-linked artifacts, or constrained planning references?
- Q9: Which stage gates are mandatory versus optional by project profile?
- OQ-007 continuity from AI synthesis: how should historical context selection
  be optimized for later workflow/generation stages without overloading context?

Additional workflow questions:

- What minimum run-state taxonomy is required for v1 interoperability between
  workflow orchestration and generation subsystem?
- What minimum policy model is needed to represent human-requested regeneration
  distinctly from automatic retry behavior?
- How should partial-failure recovery paths be represented for multi-step runs?

## Out of Scope

Explicitly out of scope in this document:

- Django models, serializers, migrations, and SQL schema design.
- Celery task definitions, worker code, and queue/broker runtime behavior.
- Redis key/data structure design.
- Provider-specific workflow graphs, ComfyUI JSON, and provider API payloads.
- Runtime orchestration implementation details.
- Final QC scoring and gate algorithms.
- Acceptance of architecture decisions through ADRs.

## Traceability

| Candidate decision / boundary | Evidence source | Evidence status |
|---|---|---|
| Workflow as explicit stage-based process with review/rework loops | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CLA-007, CLA-008, CR-007; docs/research/production/animation-production-pipeline.md principles and candidates; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md finding 6 | Strong candidate-level support |
| Workflow/artifact provenance and version history requirements | docs/DEVELOPMENT_SPEC.md reproducibility/provenance principles; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CR-008; docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md provenance findings | Strong support |
| Production workflow separated from provider workflow execution detail | docs/DEVELOPMENT_SPEC.md model-agnostic and workflow-driven principles; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md DP-003; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md Principle C | Strong support |
| Workflow distinct from GenerationTask | docs/DEVELOPMENT_SPEC.md conceptual generation flow; docs/domain/shot.md generation chain linkage; docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md workflow context findings | Moderate to strong support |
| Workflow consumes structured multimodal production context | docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md REQ-GEN-001 and RP-004; docs/domain/shot.md and docs/domain/continuity.md context boundaries | Strong candidate-level support |
| Profile-specific gate flexibility rather than globally mandatory stages | docs/research/production/animation-production-pipeline.md variability findings; docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md open question on mandatory gates | Moderate support |
| Historical runs must trace to exact WorkflowVersion and remain non-mutated | docs/DEVELOPMENT_SPEC.md workflow versioning and reproducibility principles; docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md CLA-008/CR-008 | Strong support |
| Celery/Redis details remain implementation-level and outside domain spec | docs/research/official/README.md shows planned sources only, with no accepted engineering record; AGENTS.md boundary discipline | Governance support |
| GenerationTask/GenerationAttempt and retry/redelivery/rework distinctions in this draft are aligned with current proposed architecture direction only | docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed); docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md | Proposed ADR alignment |
| Provider-neutral application-boundary idempotency direction in this draft is aligned with current proposed architecture direction only | docs/adr/ADR-0002-idempotency-contract.md (Proposed); docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md | Proposed ADR alignment |

Status progression for these boundaries is explicitly:

Research
-> Proposed ADR
-> Accepted ADR
-> Implementation

## Specification Readiness

Stable in this draft:

- Workflow meaning as production-process orchestration domain.
- WorkflowDefinition vs WorkflowVersion conceptual separation.
- WorkflowRun semantics and explicit separation from GenerationTask.
- Stage-based model with review gates and rework loops.
- Provider workflow separation from production workflow.
- Versioning/immutability and provenance traceability requirements.

Ambiguous or unresolved:

- exact global versus profile-specific lifecycle state machine commitment
- final retry/idempotency policy acceptance and implementation detail closure
- exact gate policy strictness per profile
- exact cancellation propagation semantics for linked execution scopes
- event metadata profile and observability detail level unless implementation
  scope requires immediate closure

Likely ADR-needed before architecture freeze:

- global gate policy vs profile-policy architecture
- strict state machine standardization level
- acceptance of workflow-generation retry/attempt semantics and idempotency
  contract currently documented as Proposed ADR direction

Research-unblocked determination:

- Workflow domain is research-unblocked for draft specification and incremental
  implementation planning.
- GenerationAttempt/retry and idempotency research blockers are resolved at
  Proposed ADR level.
- Implementation planning for these boundaries remains contingent on ADR
  acceptance.
- Cancellation, event metadata, and observability details remain deferrable
  unless implementation scope requires immediate closure.

## Layer 4 Research Status

Completed workflow architecture research:

- RL-ARCH-QUEUE-001: task queue, retry, and idempotency
- RL-ARCH-STATE-001: workflow state-machine semantics
- RL-ARCH-EVENT-001: event architecture
- RL-ARCH-OBS-001: workflow observability
- WORKFLOW_ARCHITECTURE_SYNTHESIS_v1: cross-record synthesis

These research topics are no longer blockers for the Workflow domain draft.

ADR-0001 and ADR-0002 capture the first architecture decisions derived from
this research and remain Proposed pending acceptance.

Cancellation, integration-event reliability, and observability implementation
profiles remain deferrable unless required by implementation scope.
