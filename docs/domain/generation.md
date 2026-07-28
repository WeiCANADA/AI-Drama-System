# Generation Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for drafting provider-neutral Generation domain baseline; no additional research is currently blocking authoritative ownership of GenerationTask, GenerationAttempt, and GenerationResult at draft-spec level.
- ADR Blocker Status: No immediate ADR blocker for publishing this draft; implementation planning remains partially contingent on ADR-0001 and ADR-0002 acceptance for final attempt/retry and idempotency policy closure.
- Specification Type: Domain Specification
- Domain: Generation
- Version: 1.0
- Evidence Basis:
  - System constraints and generation-chain direction from docs/DEVELOPMENT_SPEC.md.
  - Cross-domain blocker analysis from docs/reviews/CORE_DOMAIN_READINESS_REVIEW_v1.md.
  - Domain boundary constraints from docs/domain/shot.md, docs/domain/workflow.md, docs/domain/artifact.md, docs/domain/qc.md, and docs/domain/continuity.md.
  - Workflow architecture synthesis from docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md.
  - Queue/retry/idempotency research from docs/research/architecture/task-queue-retry-idempotency.md.
  - Event boundary research from docs/research/architecture/event-architecture.md.
  - Observability boundary research from docs/research/architecture/workflow-observability.md.
  - Provenance research from docs/research/architecture/provenance-interchange.md.
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/reviews/CORE_DOMAIN_READINESS_REVIEW_v1.md
  - docs/domain/shot.md
  - docs/domain/workflow.md
  - docs/domain/artifact.md
  - docs/domain/qc.md
  - docs/domain/continuity.md
- Related Research:
  - docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md
  - docs/research/architecture/task-queue-retry-idempotency.md
  - docs/research/architecture/event-architecture.md
  - docs/research/architecture/workflow-observability.md
  - docs/research/architecture/provenance-interchange.md
- Related ADRs:
  - ADR-0001: docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed)
  - ADR-0002: docs/adr/ADR-0002-idempotency-contract.md (Proposed)

Unresolved architecture choices remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

Define Generation as the authoritative provider-neutral application/domain
boundary that owns generation request intent, logical attempt lineage, and
normalized execution outcomes.

Generation must exist as a separate domain boundary because:

- Workflow owns orchestration and stage/gate semantics, not generation request
  identity.
- provider adapters own provider-specific execution details, not product-level
  request/attempt/result meaning.
- infrastructure owns queue/runtime behavior, not application attempt identity.
- Artifact owns durable output identity, not generation execution outcome.
- QC owns evaluation and quality decisions, not execution truth.

## Domain Definition

Generation is the provider-neutral execution-request/outcome boundary between
production intent and generation-provider execution.

Evaluated conceptual direction:

Production Intent
-> Workflow
-> GenerationTask
-> GenerationAttempt
-> GenerationResult
-> Artifact

Interpretation boundary:

- Workflow may create or reference GenerationTask.
- Generation owns request intent, attempt lineage, and normalized result
  semantics.
- provider execution remains integration-layer behavior linked by provenance.
- Artifact remains the durable production output identity after generation
  outcome normalization.

## Terminology

- Generation:
  - Application/domain boundary owning generation request intent, execution
    attempts, and normalized outcome records.
- GenerationTask:
  - Application-level generation request intent for a specific production
    purpose and context.
- GenerationAttempt:
  - One application-defined logical execution attempt for a GenerationTask.
- GenerationResult:
  - Durable normalized execution-outcome record associated to one
    GenerationAttempt.
- Generation Request Intent:
  - Requested purpose, scope, and input context for one generation task.
- Provider Execution:
  - Provider-specific external execution activity or job outside core domain
    identity.
- Infrastructure Execution:
  - Queue/worker/runtime delivery and execution mechanics outside core domain
    identity.
- Provider Job:
  - Provider-side request/job/execution reference used for provenance and
    reconciliation.
- Partial Result:
  - Mixed execution/materialization outcome where some outputs/effects are
    available and others failed or remain uncertain.
- Failed Attempt:
  - Attempt whose normalized execution outcome is failure or unresolved failure
    state.
- Successful Attempt:
  - Attempt whose normalized execution outcome completed successfully, even if
    later QC rejects resulting media.
- Reconciliation:
  - Application-level resolution of uncertain provider-side effects or mixed
    execution/materialization state.
- Regeneration:
  - Deliberate new generation action distinct from infrastructure retry.

Term policy:

- names are conceptual and not binding class/table/API names.
- Provider Job and Infrastructure Task remain linked references, not domain
  identities.

## Domain Responsibilities

Generation owns or anchors:

- generation request intent,
- logical execution-attempt identity,
- execution outcome and result records,
- provider-independent execution provenance,
- task/attempt/result lineage,
- links to provider execution identifiers,
- links to resulting artifacts,
- conceptual reconciliation state for uncertain or partial outcomes.

Generation does not own:

- WorkflowRun lifecycle,
- Shot identity,
- Artifact identity,
- QC decision,
- Continuity truth,
- infrastructure queue/runtime state,
- provider-specific graph/token/prompt ontology,
- storage schema or artifact persistence implementation.

## Domain Boundaries

Required distinctions:

- GenerationTask != WorkflowStep
- GenerationTask != Infrastructure Task
- GenerationAttempt != Infrastructure Task
- GenerationAttempt != Provider Job
- GenerationResult != Artifact
- GenerationResult != QC Evaluation
- Provider Job ID != GenerationAttempt ID
- Infrastructure Task ID != GenerationAttempt ID

Interpretation:

- WorkflowStep is orchestration context; GenerationTask is request intent.
- Infrastructure tasks and provider jobs are execution references; they do not
  define task or attempt identity.
- GenerationResult is execution outcome truth; Artifact is durable production
  output identity.
- QC evaluates outputs and outcomes; it does not redefine generation history.

## GenerationTask

GenerationTask is application-level generation request intent.

GenerationTask responsibilities may include:

- target production context,
- requested generation purpose,
- bound input references,
- workflow context references,
- requested output expectations,
- provenance anchor for later attempts and results.

GenerationTask boundary rules:

- task identity must remain provider-independent,
- task identity must remain infrastructure-independent,
- provider payload shape must not be part of core task identity,
- task intent may outlive one provider submission or one infrastructure
  delivery.

## GenerationAttempt

GenerationAttempt is one application-defined logical execution attempt for a
GenerationTask.

Proposed ADR direction pending acceptance:

- infrastructure retry/redelivery does not automatically create a new attempt,
- provider calls/jobs do not automatically define attempt identity,
- deliberate application-level new execution creates a new attempt.

Interpretation at draft-spec level:

- GenerationAttempt is owned by Generation domain as the logical attempt
  identity concept.
- final retry-promotion policy remains contingent on ADR-0001 acceptance.
- attempt lineage must remain historically traceable regardless of provider or
  queue behavior.

## GenerationResult

GenerationResult is a durable normalized execution-outcome record for one
GenerationAttempt.

GenerationResult direction in this draft:

- result is not raw provider response shape,
- result is not Artifact identity,
- result records normalized outcome semantics,
- result may include produced output-set references,
- result may represent success, failure, partial success, or unresolved
  uncertainty,
- result is the authoritative generation-layer record of what the attempt
  produced or failed to produce.

Conceptual responsibilities may include:

- normalized attempt outcome classification,
- provider execution references and response/provenance links,
- output-set summary,
- materialization status summary,
- failure context,
- reconciliation context,
- artifact linkage where outputs are promoted or registered.

## Result vs Artifact

Required distinction:

- GenerationResult = execution outcome
- Artifact = durable production output identity

Examples:

- attempt succeeds and produces one usable image:
  - one Result -> one Artifact
- attempt succeeds and produces four candidate images:
  - one Result -> multiple Artifacts
- attempt succeeds technically but output is unusable:
  - Result exists; Artifact may be zero or not promoted/registered
- attempt fails before output:
  - failure Result may exist; zero Artifacts

Boundary rule:

- provider output presence does not automatically equal Artifact identity.
- artifact promotion/registration belongs to the Generation-to-Artifact
  boundary, not to provider response shape alone.

## Cardinality

GenerationTask -> GenerationAttempt

- classification: CLEAR
- direction:
  - one GenerationTask may have zero, one, or many GenerationAttempts over its
    lifecycle
  - each GenerationAttempt belongs to exactly one GenerationTask

GenerationAttempt -> GenerationResult

- classification: CANDIDATE
- direction:
  - one GenerationAttempt should usually have zero or one normalized terminal
    GenerationResult record
  - zero results may exist while execution is pending, cancelled before
    normalized outcome capture, or awaiting reconciliation
  - future need for multiple result records per attempt remains an open question
    if sub-result/event granularity is introduced

GenerationResult -> Artifact

- classification: CLEAR
- direction:
  - one GenerationResult may link to zero, one, or many Artifacts
  - each Artifact linkage represents durable promoted/registered output identity
    derived from that result context

## Input Context

Provider-neutral generation input references may include:

- Shot intent,
- Scene shared context,
- Character/CharacterVersion,
- Continuity context,
- Storyboard/reference artifacts,
- WorkflowDefinition/WorkflowVersion/WorkflowRun/WorkflowStep context,
- PromptInstance reference where available,
- source asset and artifact references.

Input-context rule:

- GenerationTask should reference input truth rather than duplicate domain truth
  unnecessarily.
- immutable snapshots may be required for reproducibility-sensitive execution,
  but full snapshot policy remains open.

## Provider Execution Relationship

Provider execution belongs behind adapter/integration boundary.

Provider references may include:

- provider name,
- provider model,
- provider request ID,
- provider job ID,
- provider execution timestamps/status.

Boundary rule:

- these are provenance and execution references.
- they are not GenerationAttempt identity.
- provider replacement must not invalidate GenerationTask/Attempt/Result domain
  identity semantics.

## Infrastructure Execution Relationship

Infrastructure may include:

- queue delivery,
- worker execution,
- retry,
- redelivery,
- timeout,
- scheduling.

Preserved distinction:

- Infrastructure execution state != GenerationAttempt state

Proposed ADR direction pending acceptance:

- infrastructure retry/redelivery does not automatically create a new
  GenerationAttempt.

Interpretation at draft-spec level:

- infrastructure execution is linked context for observability and provenance,
  not attempt identity truth.

## Retry / Regeneration / Rework

Generation must distinguish the following semantic classes:

- transport redelivery,
- infrastructure retry,
- provider transient retry,
- new GenerationAttempt,
- human regeneration,
- review-triggered regeneration,
- workflow rework.

Proposed ADR direction pending acceptance:

- transport/infrastructure behavior does not automatically create new
  GenerationAttempt,
- human regeneration is distinct from retry,
- workflow rework is distinct from retry and only creates a new attempt when
  deliberate generation re-entry occurs.

Generation draft-spec implication:

- Generation owns task/attempt/result lineage,
- Workflow owns rework and gate semantics,
- final promotion rules among retry classes remain ADR-0001 dependent.

## Idempotency Relationship

Proposed ADR direction pending acceptance:

- side-effectful generation operations require duplicate-aware execution
  semantics,
- infrastructure task IDs and provider request IDs do not define logical
  operation identity,
- provider-side uncertainty requires reconciliation before unsafe replay.

Generation interpretation:

- Generation operations are subject to duplicate-aware execution requirements,
- final idempotency-key composition is not defined here,
- this draft does not implement idempotency and does not select any storage or
  infrastructure mechanism.

## Partial Success

Partial success must be represented explicitly and separately from artifact
promotion or QC acceptance.

Representative cases:

- provider returns 4 outputs, only 2 materialize successfully,
- provider job succeeds but one artifact write fails,
- provider returns metadata but media retrieval fails,
- one multi-output attempt contains mixed usable/unusable outputs.

Separation rule:

- attempt execution outcome,
- result outcome,
- artifact materialization,
- QC acceptance

must remain distinct.

Candidate direction:

- GenerationResult may record mixed output/materialization state,
- zero or more artifacts may be linked from one partial-success result,
- QC may later reject outputs without changing execution success history.

## Failure Semantics

Generation must distinguish:

- provider failure,
- infrastructure failure,
- application normalization failure,
- result materialization failure,
- artifact persistence failure,
- QC failure.

Required distinction:

- QC failure != Generation failure

Interpretation:

- an attempt may succeed technically while later QC rejects outputs,
- an attempt may fail even when some provider-side effects occurred,
- artifact persistence failure does not erase the underlying execution attempt
  history.

## Cancellation / Uncertainty

Conceptual scenarios include:

- cancellation requested,
- provider already running,
- provider cancellation unknown,
- provider accepted request before timeout,
- partial side effects.

Required direction:

- cancellation and uncertainty require reconciliation and provenance,
- unknown provider execution outcomes must remain explicitly representable,
- this draft does not finalize cancellation policy.

Candidate interpretation:

- GenerationAttempt or GenerationResult may include reconciliation context for
  unknown/partial provider-side effects,
- provider cancellation uncertainty must not be flattened into simple success or
  failure without recorded reasoning.

## Versioning / Immutability

Records that must remain historically traceable include at minimum:

- GenerationTask intent,
- GenerationAttempt identity,
- GenerationResult outcome,
- provider/model reference,
- input references,
- parameters when available,
- result/artifact linkage.

Immutability direction:

- historical execution records must not be silently rewritten,
- later retries, reconciliations, or QC outcomes must append or link rather than
  replace prior generation history.

## Provenance

Minimum generation provenance linkage:

Shot / production context
-> Workflow context
-> GenerationTask
-> GenerationAttempt
-> provider execution references
-> GenerationResult
-> Artifact

Boundary rules:

- provider-neutral identity boundaries must remain intact,
- telemetry identity must not replace domain identity,
- external authenticity standards remain outside core Generation ontology.

## QC Relationship

Generation relationship to QC:

- QC may evaluate GenerationResult as execution/outcome target in selected
  cases,
- concrete media-quality QC will usually evaluate ArtifactVersion or
  Representation,
- QC rejection does not rewrite generation execution history.

Required distinction:

- GenerationResult != QC Evaluation
- QC failure != Generation failure

## Workflow Relationship

Workflow may create or reference GenerationTasks.

Boundary rules:

- Generation does not own Workflow stages, gates, or rework policy,
- Workflow does not own GenerationTask/Attempt/Result identity semantics,
- WorkflowRun provides context; Generation provides execution-request and
  outcome semantics.

## Artifact Relationship

GenerationResult may produce, register, or link Artifacts.

Boundary rules:

- Artifact domain owns durable production artifact identity/version/lineage,
- Generation domain owns execution outcome semantics and links to artifacts,
- artifact review/revision after generation does not redefine prior
  GenerationResult identity.

## Continuity Relationship

Generation consumes continuity context where relevant.

Boundary rules:

- Generation does not own continuity state truth,
- continuity context may influence GenerationTask input references,
- later generation must remain traceable to continuity context in effect at
  execution time.

## Validation / Invariants

Evidence-supported candidate invariants:

- GenerationTask identity is provider-independent.
- GenerationAttempt identity is independent from infrastructure/provider IDs.
- GenerationResult identity is distinct from Artifact identity.
- Historical attempts/results remain traceable.
- Provider/runtime identifiers never replace domain identities.
- QC rejection does not rewrite generation execution history.
- Infrastructure retry/redelivery must not automatically redefine attempt
  identity in draft semantics aligned to Proposed ADR direction.

## Candidate Information Model

Conceptual only.

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| generation_task_id | Stable task identity | CORE DOMAIN | Yes | Provider/infrastructure independent request-intent identity. |
| generation_task_intent | Requested generation purpose | CORE DOMAIN | Yes | Why this task exists in production context. |
| production_context_refs | Linked production references | REFERENCE | Yes | Shot/Scene/Character/Continuity/Artifact inputs as needed. |
| workflow_context_ref | Linked workflow context | REFERENCE | No | Workflow context is linked, not owned. |
| requested_output_expectations | Expected output class/count/purpose | CORE DOMAIN | No | Keeps intent separate from actual result. |
| generation_attempt_id | Stable logical attempt identity | CORE DOMAIN | Yes | Distinct from provider and infrastructure IDs. |
| attempt_ordinal | Attempt lineage order marker | CORE DOMAIN | Usually | Useful for traceability without defining policy by count alone. |
| attempt_input_snapshot_ref | Snapshot/reference linkage for reproducibility | REFERENCE | No | Snapshot policy remains open. |
| provider_execution_refs | Provider request/job linkage | PROVIDER CONCERN | No | Provenance only; not identity truth. |
| infrastructure_execution_refs | Queue/worker execution linkage | PROVIDER CONCERN | No | Execution context only; not identity truth. |
| generation_result_id | Stable result identity | CORE DOMAIN | Usually | Durable normalized outcome record identity. |
| result_outcome | Normalized success/failure/partial/uncertain outcome | CORE DOMAIN | Yes | No final enum fixed in this draft. |
| result_payload_refs | References to normalized output payloads/metadata | REFERENCE | No | Provider response shape not promoted to ontology. |
| artifact_refs | Linked durable artifact identities | REFERENCE | No | Zero/one/many possible. |
| failure_context | Failure classification linkage | CORE DOMAIN | No | Distinguish provider/infra/materialization/etc. |
| reconciliation_context | Uncertainty/partial-side-effect handling context | CORE DOMAIN | No | Required when outcome is ambiguous or mixed. |
| provenance_context | Historical traceability context | CORE DOMAIN | Yes | Must support reproducibility beyond telemetry retention. |

## Candidate Requirements

Classification policy:

- ACCEPT INTO DRAFT SPEC
- KEEP AS CANDIDATE
- DEFER
- REJECT FOR CORE DOMAIN

Requirement set:

- CR-GEN-001: Generation domain owns authoritative provider-neutral semantics
  for GenerationTask, GenerationAttempt, and GenerationResult.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: direct blocker identified in CORE_DOMAIN_READINESS_REVIEW_v1.md.

- CR-GEN-002: GenerationTask represents generation request intent independent
  from WorkflowStep and infrastructure task identity.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: DEVELOPMENT_SPEC generation chain and workflow boundary rules.

- CR-GEN-003: GenerationResult remains distinct from Artifact and records
  normalized execution outcome.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: artifact specification boundary and cross-domain ownership gap.

- CR-GEN-004: Historical task/attempt/result lineage must remain traceable and
  not be silently rewritten.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: reproducibility and provenance requirements across repository.

- CR-GEN-005: Infrastructure retry/redelivery does not automatically create a
  new GenerationAttempt.
  - Classification: KEEP AS CANDIDATE
  - Basis: Proposed ADR-0001 direction only; not accepted architecture yet.

- CR-GEN-006: Generation operations with side effects require duplicate-aware
  execution semantics.
  - Classification: KEEP AS CANDIDATE
  - Basis: Proposed ADR-0002 direction only; final contract not accepted.

- CR-GEN-007: One GenerationAttempt should produce at most one normalized
  terminal GenerationResult.
  - Classification: KEEP AS CANDIDATE
  - Basis: coherent normalization direction, but sub-result granularity remains
    open.

- CR-GEN-008: QC rejection should change generation execution status.
  - Classification: REJECT FOR CORE DOMAIN
  - Basis: QC failure must remain distinct from generation failure.

- CR-GEN-009: Provider response schema should define GenerationResult ontology.
  - Classification: REJECT FOR CORE DOMAIN
  - Basis: provider-neutral boundary constraint.

- CR-GEN-010: Final idempotency-key composition and storage mechanism should be
  decided here.
  - Classification: DEFER
  - Basis: explicitly out of scope and ADR-0002 remains Proposed.

## ADR Review Points

Genuine architectural decisions likely to require ADR review:

- acceptance of ADR-0001,
- acceptance of ADR-0002,
- GenerationResult identity/cardinality policy,
- partial-success normalization policy,
- cancellation/reconciliation contract.

No ADR is created by this specification.

## Open Questions

- Can one GenerationAttempt create multiple GenerationResults?
- Should a failed attempt always have a GenerationResult record?
- Is GenerationResult one normalized outcome or one output item?
- When is provider output promoted to Artifact?
- Can one Result map to multiple Artifacts?
- How are partial outputs represented?
- How should unknown provider execution outcomes be reconciled?
- Which generation inputs require immutable snapshots versus references?

## Out of Scope

Explicitly out of scope:

- Django models
- provider adapters
- Celery implementation
- Redis
- provider API schema
- prompt-engine implementation
- artifact storage
- QC algorithms
- event sourcing
- final cancellation implementation
- final idempotency key design
- storage schema

## Traceability

Important boundary mapping:

- Development Spec:
  - provider-neutral generation chain and reproducibility expectations
- Core Domain Readiness Review:
  - identified missing Generation ownership as primary blocker
- Workflow Spec:
  - Workflow != GenerationTask and WorkflowRun context linkage
- Artifact Spec:
  - GenerationResult != Artifact and artifact provenance linkage
- QC Spec:
  - QC may target GenerationResult in some cases, but concrete media QC usually
    targets ArtifactVersion/Representation
- ADR-0001 Proposed:
  - attempt identity and retry/redelivery boundary
- ADR-0002 Proposed:
  - application-boundary idempotency direction
- Workflow Architecture Synthesis:
  - identity separation, retry taxonomy, provenance-versus-telemetry boundary

Status progression preserved:

Research
-> Draft Specification
-> Proposed ADR
-> Accepted ADR
-> Implementation

## Specification Readiness

Generation blocker from CORE_DOMAIN_READINESS_REVIEW_v1.md:

- resolved at Draft-spec ownership level: YES

Classification of core Generation areas:

- GenerationTask ownership: STABLE
- GenerationAttempt ownership: STABLE
- GenerationResult ownership: STABLE
- cardinality: PARTIAL
- provenance: STABLE
- retry boundary: ADR BLOCKED
- artifact boundary: STABLE
- QC boundary: STABLE

Interpretation:

- this draft resolves the missing authoritative owner for GenerationTask,
  GenerationAttempt, and GenerationResult.
- implementation of final retry/idempotency policy remains contingent on
  Proposed ADR acceptance.
- cardinality and partial-success normalization are sufficient for draft scope
  but not fully closed.

## Layer 4 Research Requests

Current determination:

- no new Layer 4 research request is genuinely blocking this draft.

Potential future non-blocking topics only if implementation scope demands them:

- deeper cancellation/reconciliation patterns across provider classes,
- output-set normalization patterns for multi-result provider workflows,
- snapshot-versus-reference provenance policy for reproducibility-sensitive
  generation inputs.
