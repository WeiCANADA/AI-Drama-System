# ADR-0002: Idempotency Contract

## Status

Proposed

## Context

Distributed execution with queue delivery, worker retry, redelivery, and network
uncertainty creates a class of duplicate-risk scenarios that infrastructure
runtime semantics alone cannot safely resolve.

The system must handle repeated deliveries and repeated submissions without
accidentally producing additional domain effects.

ADR-0001 already established:

- GenerationAttempt is an application-level logical attempt identity.
- Infrastructure retry/redelivery does not automatically create a new
  GenerationAttempt.
- Infrastructure and provider execution identifiers are linked provenance
  identifiers, not domain attempt identity.

Therefore, queue/task identifiers cannot serve as authoritative idempotency
identity.

This ADR defines the minimum provider-neutral idempotency contract at the
application operation boundary, without reopening ADR-0001 decisions.

## Decision

After evaluating synthesis and research evidence, the proposed decision is:

1. Idempotency responsibility is owned at the application operation boundary,
   where business meaning and domain effect semantics are known.
2. Infrastructure execution identifiers and provider execution identifiers are
   diagnostic/provenance links only; they do not define logical-operation
   identity.
3. Operations that can create externally visible or durable side effects require
   duplicate-aware execution semantics.
4. Duplicate detection must use stable application-level logical-operation
   identity and normalized operation intent, not infrastructure task identity.
5. Repeated execution of the same infrastructure delivery path must not
   automatically create additional domain effects.
6. Deliberately created new GenerationAttempt remains distinct from duplicate
   execution of an existing attempt.
7. Human regeneration and workflow rework that intentionally create new
   execution intent must not be suppressed solely because prior inputs appear
   similar.
8. Ambiguous provider-side effects require reconciliation-oriented handling
   rather than blind replay assumptions.

Decision boundaries:

- This ADR does not redefine GenerationAttempt semantics from ADR-0001.
- This ADR does not finalize key composition, hashing, storage schema,
  or vendor-specific implementation.

## Idempotency Scope

Conceptual operation classes and required idempotency protection level:

- create GenerationTask: REQUIRED
  - Reason: creates durable request intent and scheduling consequences.
- start GenerationAttempt: REQUIRED
  - Reason: creates logical attempt lineage and downstream execution impact.
- submit provider generation request: REQUIRED
  - Reason: can trigger external side effects and uncertain provider execution.
- persist GenerationResult: REQUIRED
  - Reason: durable output state and downstream lineage effects.
- register Artifact: REQUIRED
  - Reason: durable production artifact lineage and review dependencies.
- record review decision: CONTEXT-DEPENDENT
  - Reason: often business-event-like and may require conflict/idempotent guard
    depending on decision model and command semantics.
- apply workflow transition: REQUIRED
  - Reason: changes authoritative workflow progression state.
- publish integration event: CONTEXT-DEPENDENT
  - Reason: duplicate-safe publication contract required, but exact mechanism
    remains implementation candidate.

Not in scope here:

- detailed database representation;
- signal-level observability schema;
- provider-specific retry configurations.

## Duplicate Classification

| Situation | Duplicate? | Same GenerationAttempt? | New Business Intent? | Expected Handling Direction |
|---|---:|---:|---:|---|
| broker redelivery | Yes | Yes | No | Treat as duplicate execution signal; avoid additional domain effects; reuse or reconcile existing operation state |
| worker retry | Usually yes at operation boundary | Yes by default | No | Retry within same logical operation context; suppress extra domain effects unless policy promotes new operation |
| repeated HTTP/application command | Candidate duplicate unless explicitly new intent | Usually yes unless explicit new intent token/policy | Usually no | Perform logical-operation duplicate check; return existing or in-progress state; reject conflicting duplicate |
| provider submit timeout followed by retry | Unknown until reconciled | Yes by default until deliberate new attempt decision | No by default | Enter uncertainty/reconciliation path before unsafe resubmission where possible |
| repeated callback/webhook | Yes in common delivery models | Usually yes | No | De-duplicate on logical operation/event context; make processing repeat-safe |
| deliberate new GenerationAttempt | No | No (new attempt by design) | Usually no new business intent, but new logical execution attempt intent | Allow explicit new logical operation; persist lineage linkage |
| human-requested regeneration | No | No | Yes or explicit re-run intent | Allow explicit new operation and preserve user-intent provenance |
| review-triggered regeneration | No | No | Yes | Allow new operation path tied to review decision lineage |
| workflow rework followed by new generation | Rework transition itself is not duplicate execution of prior generation operation | No for rework transition; new attempt when generation re-entry is deliberate | Yes | Preserve rework lineage, then create deliberate new generation operation at re-entry |

## Logical Operation Identity

Logical-operation identity means a stable application-level identity of one
intended operation instance for duplicate detection and replay safety.

Conceptual candidate contributors include:

- operation type;
- target domain identity;
- workflow context;
- GenerationTask identity;
- GenerationAttempt identity (when applicable);
- normalized operation intent;
- versioned input context.

Constraints:

- final idempotency-key composition is not decided here;
- hashing algorithm is not decided here;
- storage schema is not decided here.

## Duplicate Handling Semantics

Duplicate handling is operation-specific and cannot be reduced to one universal
response.

Valid handling outcomes include:

- return or reuse existing operation result;
- report operation as in progress;
- reconcile uncertain execution state;
- reject conflicting duplicate operation;
- allow explicit new logical operation when intent is deliberate and distinct.

Required rule:

- handling policy must be explicit per operation class and consistent with
  domain semantics and ADR-0001 attempt boundaries.

## Provider-Side Uncertainty

Critical scenario:

Application
-> Provider submit
-> provider may accept request
-> network timeout before response
-> application cannot confirm side effect status

Required behavior direction:

- Do not automatically conclude first submit failed.
- Do not automatically create a new GenerationAttempt.
- Do not automatically assume replay is safe.
- Require reconciliation strategy based on available application/provider
  capabilities before unsafe resubmission where possible.

Identity separation must be preserved:

- GenerationAttempt ID
- Provider Job or Request ID
- Infrastructure Task ID
- Idempotency identity

None of these are aliases.

## Idempotency Record

Minimum conceptual responsibilities of an idempotency record:

- logical operation identity;
- operation classification;
- execution status;
- linked domain context;
- linked GenerationAttempt (when applicable);
- known provider execution references;
- result reference when available;
- uncertainty or reconciliation state;
- creation and completion timestamps;
- conflict evidence.

These are conceptual responsibilities only.

## Concurrency

Concurrent duplicate requests must be handled with atomic or otherwise
concurrency-safe protection at the application persistence boundary.

Required boundary:

- duplicate classification and claim/commit behavior must be safe under
  concurrent submissions.

Not decided here:

- locking primitive;
- database-specific isolation strategy;
- Redis or broker coordination design.

## Retention and Provenance

Distinct concerns:

- idempotency retention
- operational telemetry retention
- production provenance retention

Preserved principle:

- telemetry retention != provenance retention

Retention decision boundaries:

- idempotency records do not need infinite retention by default;
- idempotency/runtime-data expiration must not destroy required production
  provenance needed for reproducibility and auditability.

## Event Publication Boundary

Integration-event publication must be duplicate-safe at the conceptual
application boundary.

Required direction:

- repeated publication triggers should not produce uncontrolled duplicate
  integration effects;
- publication reliability semantics must be defined in a later decision.

Not adopted by this ADR:

- transactional outbox as mandatory architecture;
- event sourcing;
- broker-specific solution.

## Alternatives Considered

### A. Infrastructure task ID as idempotency key

Advantages:

- simple runtime correlation.

Problems:

- ties business duplicate semantics to transport/runtime mechanics;
- fragile under redelivery/requeue/model changes;
- conflicts with ADR-0001 identity separation.

Decision:

- Rejected.

### B. Provider request ID as idempotency authority

Advantages:

- useful provider-side diagnostic linkage.

Problems:

- provider ID may be absent/late/ambiguous in timeout scenarios;
- couples core idempotency semantics to provider behavior;
- cannot cover pre-submit duplicate classes.

Decision:

- Rejected as authority; retained as linked reference.

### C. Application-owned logical-operation idempotency

Advantages:

- preserves domain meaning at operation boundary;
- supports provider/queue independence;
- aligns with retry/redelivery uncertainty handling.

Problems:

- requires explicit operation classification and policy rigor.

Decision:

- Accepted.

### D. No persistent idempotency contract; rely on retries/provider behavior

Advantages:

- low short-term implementation effort.

Problems:

- high risk of duplicate domain effects;
- weak reproducibility/auditability;
- inconsistent behavior across providers and runtime paths.

Decision:

- Rejected.

### E. Content or input hash alone defines duplicate identity

Advantages:

- simple conceptual signal for similarity detection.

Problems:

- semantically distinct operations can have similar inputs;
- intent, workflow context, and operation type can differ;
- cannot safely distinguish deliberate new attempts/regeneration paths.

Decision:

- Rejected as sole authority; may participate as one candidate signal in a
  future key-design decision.

## Consequences

### Positive

- Defines clear provider-neutral idempotency ownership boundary.
- Reduces duplicate side-effect risk under retries/redeliveries.
- Preserves ADR-0001 identity semantics and attempt lineage integrity.

### Negative

- Requires operation-by-operation policy definitions.
- Adds reconciliation complexity for uncertain provider-side effects.

### Operational

- Requires explicit duplicate classification and status handling paths.
- Requires concurrency-safe operation claim/commit behavior.

### Provenance

- Improves traceability by linking operation identity with attempt and provider
  references without identity collapse.
- Protects reproducibility by preventing accidental duplicate effects.

### Testing

- Must test redelivery/retry duplicate suppression.
- Must test uncertain submit timeout reconciliation path.
- Must test explicit new intent paths (new attempt, regeneration, rework).
- Must test concurrent duplicate request handling.

## Non-Goals

This ADR does not decide:

- final idempotency-key composition;
- hashing algorithm;
- database schema;
- Django model design;
- Redis locking design;
- Celery configuration;
- broker selection;
- provider-specific retry configuration;
- event sourcing;
- transactional outbox adoption;
- final cancellation policy;
- observability implementation.

## Evidence

- docs/adr/ADR-0001-generation-attempt-retry-semantics.md
- docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md
- docs/research/architecture/task-queue-retry-idempotency.md
- docs/research/architecture/workflow-state-machine.md
- docs/research/architecture/event-architecture.md
- docs/research/architecture/workflow-observability.md

Alignment summary:

- Queue/runtime retry and redelivery are infrastructure semantics.
- Domain/application operation meaning defines idempotency boundaries.
- Duplicate safety must preserve attempt identity boundaries from ADR-0001.
- Provenance and observability require linked but separate identities.

## Follow-Up Decisions

Genuinely unresolved architectural topics after this ADR:

- cancellation reconciliation contract for uncertain/partial side effects;
- integration-event publication reliability contract;
- minimum observability profile contract.

ADR-0002 does not create these follow-up ADRs now.
