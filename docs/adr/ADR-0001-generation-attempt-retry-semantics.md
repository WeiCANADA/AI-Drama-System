# ADR-0001: Generation Attempt and Retry Semantics

## Status

Proposed

## Context

Layer 4 Batch 2 synthesis identifies a specific blocking boundary: the system
needs a stable architectural distinction between application-level generation
attempt semantics and infrastructure runtime retry/redelivery semantics before
implementation planning can proceed for GenerationTask / GenerationAttempt.

Cross-source evidence shows that queue/runtime behavior (delivery, retry,
redelivery, revoke, timeout) is infrastructure execution semantics, while
WorkflowRun and generation intent semantics remain domain/application concerns.
Therefore, runtime retry behavior cannot by itself define GenerationAttempt
identity.

This ADR resolves the minimum architecture decision needed to unblock planning
for GenerationAttempt semantics, while deferring separate idempotency-contract
closure to a follow-up ADR.

## Decision

After evaluating the research and synthesis, the proposed decision is:

1. GenerationTask represents one application-level generation request intent in
   a workflow context.
2. GenerationAttempt represents one application-defined logical execution
   attempt for that request intent.
3. Infrastructure delivery/redelivery/retry events do not automatically create a
   new GenerationAttempt.
4. A new GenerationAttempt is created only when the application layer
   deliberately starts a new logical attempt under workflow/application policy.
5. Human-requested regeneration is a distinct business action and must remain
   distinguishable from infrastructure retry/redelivery.
6. Workflow rework is a business-governance transition and must remain
   distinguishable from retry.
7. Infrastructure execution IDs and provider execution IDs are linked
   provenance/diagnostic identifiers, not GenerationAttempt identity.

Decision rationale:

- Aligns with domain/infrastructure separation principles.
- Avoids false attempt inflation from transport/runtime instability.
- Preserves auditability and reproducibility by separating logical attempt
  lineage from runtime delivery mechanics.
- Keeps provider/queue choices replaceable and outside domain truth.

Scope of this decision:

- Defines identity and semantic boundary only.
- Does not finalize idempotency key composition, cancellation policy details,
  event schema, or observability schema.

## Semantic Classification

| Situation | Layer | New GenerationAttempt? | New Business Intent? | Provenance Requirement |
|---|---|---:|---:|---|
| broker redelivery | Infrastructure execution | No | No | Record redelivery occurrence and link to same logical attempt context |
| infrastructure retry | Infrastructure execution | No | No | Record retry counters/reasons linked to same logical attempt context |
| provider transient retry | Infrastructure execution or provider adapter execution | No by default; policy boundary if adapter promotes to new logical attempt | No by default | Record provider retry signal, uncertainty window, and linkage to logical attempt |
| application-requested new attempt | Generation application layer | Yes | Usually no (same request intent, new logical execution attempt) | Record deliberate new-attempt decision and attempt lineage linkage |
| workflow step retry | Workflow domain + generation application policy | Not automatically; policy-defined | Usually no | Record policy-triggered retry class and mapping decision |
| review-triggered regeneration | Workflow domain (gate/review outcome) | Yes | Yes (acceptance/revision semantics changed) | Record review decision cause and revised execution lineage |
| human-requested regeneration | Workflow domain / user action | Yes | Yes or explicit re-run intent | Record user intent/authorization context and lineage |
| workflow rework | Workflow domain | No for rework state transition itself; Yes when reworked intent deliberately re-enters generation execution | Yes | Record rework decision, revised intent context, and downstream generation-entry attempt lineage |

Policy-boundary note:

- Where evidence is insufficient for universal behavior (for example, provider
  transient retry classification in all adapters), this ADR sets a boundary:
  implicit infrastructure/runtime retries do not auto-create new
  GenerationAttempt unless application policy explicitly promotes them.

## Identity Boundary

The following identities remain independent and linkable:

- GenerationTask ID: identity of one generation request intent.
- GenerationAttempt ID: identity of one application-level logical execution
  attempt.
- WorkflowRun ID: workflow execution context identity.
- WorkflowStep identity: step-level execution/governance context identity.
- Infrastructure task ID: queue/worker runtime execution identity.
- Provider request/job ID: provider-side execution/request identity.

Boundary rule:

- None of these identifiers are aliases of each other.
- Mappings are explicit lineage/provenance links, not identity collapse.

Clarification on provider calls:

- One provider API call is not guaranteed to equal one GenerationAttempt in all
  failure scenarios. For example, submit timeout may leave uncertain provider
  side effects; reconciliation and provenance linkage are required before any
  policy-driven new attempt decision.

## Failure and Partial Side Effects

Infrastructure/runtime failure can occur after provider-side effects may already
have happened (for example, request accepted but response/ack path failed).

This ADR requires:

- explicit uncertainty handling and reconciliation before assuming safe replay;
- provenance linkage of ambiguous outcomes to the originating logical attempt;
- policy-based classification of whether subsequent execution remains the same
  attempt context or becomes a deliberately new attempt.

This ADR does not define the full cancellation policy.

## Idempotency Boundary

This ADR requires only the following idempotency boundary:

- infrastructure retry/redelivery safety depends on idempotent or
  duplicate-aware application operations;
- duplicate detection cannot depend solely on infrastructure task IDs;
- final idempotency contract and key composition are deferred to ADR-0002.

This ADR does not define final idempotency key composition.

## Alternatives Considered

### A. One GenerationAttempt per infrastructure task ID

- Pros:
  - Simple to model in runtime-centric systems.
- Cons:
  - Couples domain identity to infrastructure/runtime mechanics.
  - Inflates attempts under redelivery/retry instability.
  - Weak portability across providers/queues.
- Decision:
  - Rejected.

### B. One GenerationAttempt spanning all infrastructure retries/redeliveries

- Pros:
  - Preserves logical-attempt continuity under transport/runtime instability.
  - Better alignment with domain/application intent.
- Cons:
  - Requires explicit policy boundaries for when to promote to new attempt.
- Decision:
  - Accepted as default boundary direction, with policy-governed exceptions.

### C. Application-defined GenerationAttempt identity independent from
infrastructure task identity

- Pros:
  - Preserves domain/application authority and provider independence.
  - Enables explicit provenance linking across heterogeneous runtimes.
- Cons:
  - Requires explicit mapping and lineage discipline.
- Decision:
  - Accepted.

### D. Every retry creates a new GenerationAttempt

- Pros:
  - Clear counting semantics at first glance.
- Cons:
  - Conflates transport/runtime noise with logical attempt boundaries.
  - Distorts business metrics and provenance interpretation.
- Decision:
  - Rejected.

## Consequences

### Positive

- Unblocks GenerationAttempt implementation planning with clear semantic
  boundary.
- Preserves provider/queue replaceability.
- Improves auditability of retry/redelivery versus true new attempts.

### Negative

- Requires explicit policy/mapping logic rather than naive runtime-state mapping.
- Introduces reconciliation complexity in ambiguous provider-side effect cases.

### Operational

- Runtime observability must capture infrastructure and provider execution
  identifiers as linked context to logical attempts.
- Retry handling flows require explicit classification events/records.

### Provenance

- Provenance must preserve separate identities and explicit lineage links among
  request intent, logical attempts, runtime executions, and provider jobs.
- Historical reconstruction improves because identity collapse is prohibited.

### Testing

- Tests must cover redelivery/retry paths that do not create new attempts.
- Tests must cover deliberate new-attempt creation paths.
- Tests must cover ambiguous provider-side-effect scenarios requiring
  reconciliation behavior.

## Non-Goals

This ADR does not decide:

- queue provider selection;
- Celery configuration;
- Redis configuration;
- final idempotency-key schema;
- cancellation policy;
- event schema;
- observability schema;
- Django model design.

## Evidence

Primary synthesis and research basis:

- docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md
- docs/research/architecture/task-queue-retry-idempotency.md
- docs/research/architecture/workflow-state-machine.md
- docs/research/architecture/event-architecture.md
- docs/research/architecture/workflow-observability.md

Evidence summary alignment:

- Queue/runtime retry semantics are infrastructure-level.
- Domain/application logical attempt semantics require explicit ownership.
- Rework/human regeneration are business-semantic paths and must stay separate
  from technical retry.
- Identity separation is required for provenance and observability integrity.

## Follow-Up Decisions

- ADR-0002 - Idempotency Contract (required):
  - responsible layer boundaries;
  - required idempotency coverage classes;
  - duplicate classification policy;
  - key-composition constraints without premature overfitting.

Potential later ADRs only if needed by scope pressure:

- cancellation reconciliation contract;
- event metadata minimum profile;
- minimum observability contract profile.
