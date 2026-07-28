# RL-ARCH-QUEUE-001 - Task Queue, Retry, and Idempotency Semantics

## Research Metadata

- Research ID: RL-ARCH-QUEUE-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Scope: official semantics for task identity, retry, acknowledgment, redelivery,
  and idempotency boundaries relevant to queue-backed generation orchestration
- Constraints:
  - Official/primary sources only
  - No implementation, configuration, or ADR decision in this record
  - No automatic promotion from finding to accepted requirement

## Research Question

What are the official semantics of task queue retry and idempotency behavior,
and how should those semantics be separated from AI Drama domain/application
concepts such as WorkflowRun, GenerationTask, and GenerationAttempt?

## Official Sources

### Celery (official documentation)

- Tasks user guide
  - URL: https://docs.celeryq.dev/en/stable/userguide/tasks.html
  - Accessed: 2026-07-28
- Calling API (message send/retry policy)
  - URL: https://docs.celeryq.dev/en/stable/userguide/calling.html
  - Accessed: 2026-07-28
- Workers guide (revoke/cancel/worker behavior)
  - URL: https://docs.celeryq.dev/en/stable/userguide/workers.html
  - Accessed: 2026-07-28
- Configuration guide
  - URL: https://docs.celeryq.dev/en/stable/userguide/configuration.html
  - Accessed: 2026-07-28
- Backends and brokers overview
  - URL: https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html
  - Accessed: 2026-07-28

### Redis (official documentation)

- Redis Streams overview
  - URL: https://redis.io/docs/latest/develop/data-types/streams/
  - Accessed: 2026-07-28
- XREADGROUP command reference
  - URL: https://redis.io/docs/latest/commands/xreadgroup/
  - Accessed: 2026-07-28
- XPENDING command reference
  - URL: https://redis.io/docs/latest/commands/xpending/
  - Accessed: 2026-07-28
- XACK command reference
  - URL: https://redis.io/docs/latest/commands/xack/
  - Accessed: 2026-07-28
- Pub/Sub semantics (contrast model)
  - URL: https://redis.io/docs/latest/develop/pubsub/
  - Accessed: 2026-07-28

## Celery Semantics

### Task Identity and Request Metadata

- [OFFICIAL-DEFINED] Each Celery task execution has a unique task ID and request
  metadata available to the task context (including id/correlation_id/retries and
  delivery metadata fields).
- [OFFICIAL-DEFINED] Result/state APIs are task-ID keyed and reflect worker-side
  execution lifecycle.

### Lifecycle States

- [OFFICIAL-DEFINED] Built-in task states include at least: PENDING, STARTED,
  SUCCESS, FAILURE, RETRY, REVOKED.
- [OFFICIAL-DEFINED] RETRY is a first-class state in Celery's state model.

### Retry Behavior

- [OFFICIAL-DEFINED] `Task.retry()` re-queues execution by publishing a new
  message and records retry state.
- [OFFICIAL-DEFINED] Celery documents that retry uses the same task ID for the
  retried task execution message (logical continuity of one task identity).
- [OFFICIAL-DEFINED] Automatic retry controls are documented (`autoretry_for`,
  retry backoff/jitter, max retries).

### Acknowledgment, Redelivery, and Duplicate-Execution Risk

- [OFFICIAL-DEFINED] Acknowledgment timing is configurable conceptually as
  early-ack vs late-ack behavior.
- [OFFICIAL-DEFINED] Celery explicitly warns that late acknowledgment and worker/
  connection failure scenarios can lead to redelivery and therefore duplicate
  execution attempts.
- [OFFICIAL-DEFINED] Celery guidance explicitly recommends idempotent task
  functions for safe operation under retry/redelivery conditions.

### Publish-Side Retry

- [OFFICIAL-DEFINED] Sending a task message can itself use retry policy
  (publication retry with bounded policy controls).
- [OFFICIAL-DEFINED] Publish retry semantics are separate from worker execution
  retry semantics.

### Revocation and Cancellation Semantics

- [OFFICIAL-DEFINED] Celery supports revocation semantics and worker control
  paths that may prevent future execution or attempt termination.
- [OFFICIAL-DEFINED] Revocation does not imply that domain-level work was never
  partially executed; interpretation requires application/domain reconciliation.

## Redis-Relevant Semantics

### Why Redis Semantics Matter Here

- [INTERPRETATION] Celery may use Redis in broker/backend roles; therefore Redis
  delivery/ack/visibility behavior can influence observable retry/redelivery
  effects at infrastructure level.

### Streams and Consumer-Group Reliability Model

- [OFFICIAL-DEFINED] Redis Streams consumer groups track pending entries (PEL),
  require explicit acknowledgment (`XACK`) for completion, and expose pending
  inspection (`XPENDING`).
- [OFFICIAL-DEFINED] Streams support message claiming/reclaim workflows for
  consumer-failure recovery.
- [OFFICIAL-DEFINED] Delivery counters and idle time are explicit observability
  signals in pending-entry workflows.

### Pub/Sub Contrast

- [OFFICIAL-DEFINED] Redis Pub/Sub is at-most-once and does not retain messages
  for later recovery.
- [INTERPRETATION] Pub/Sub semantics are not an appropriate baseline model for
  recoverable generation-task orchestration.

### Persistence/Replication Caveat

- [OFFICIAL-DEFINED] Redis durability and replication behavior depend on chosen
  persistence/replication setup; failover can involve best-effort tradeoffs.
- [INTERPRETATION] Queue-level guarantees must be treated as infrastructure
  semantics, not domain-level business completion guarantees.

## Semantic Boundary Clarification

### Distinct Layers (Candidate Interpretation)

- [CANDIDATE-INTERPRETATION] WorkflowRun/WorkflowStep are production orchestration
  concepts (application/domain layer), not queue transport entities.
- [CANDIDATE-INTERPRETATION] GenerationTask/GenerationAttempt represent product
  intent and traceable generation history, not raw broker messages.
- [CANDIDATE-INTERPRETATION] Celery task execution is infrastructure execution
  mechanism that may support one or more application attempts depending on
  policy.

### Non-Equivalence Rules (Candidate)

- [CANDIDATE-RULE] One Celery task ID must not be assumed equivalent to one
  GenerationAttempt without an explicit mapping policy.
- [CANDIDATE-RULE] One infrastructure retry (same Celery task ID) must not be
  silently treated as one new domain-level regeneration attempt.
- [CANDIDATE-RULE] Human-requested regeneration must remain distinguishable from
  infrastructure retry/redelivery.

## Retry Taxonomy (Candidate)

- [CANDIDATE-TYPE] Transport or infra redelivery of an in-flight execution due to
  ack/failure conditions.
- [CANDIDATE-TYPE] Celery logical retry within same task identity.
- [CANDIDATE-TYPE] Application-level retry policy that may create a new
  GenerationAttempt record.
- [CANDIDATE-TYPE] Human-initiated regeneration as a separate production action.

## Idempotency Ownership (Candidate)

- [CANDIDATE-PRINCIPLE] Infrastructure layer provides at-least-once-style failure
  handling behavior in multiple scenarios; therefore idempotency responsibility
  primarily belongs to application/domain operation design.
- [CANDIDATE-PRINCIPLE] Idempotency keys/fingerprints should be domain-aware
  (shot context, workflow version, normalized intent, and attempt class), not
  only queue-message identifiers.
- [CANDIDATE-PRINCIPLE] “Already done” detection must be explicit and auditable,
  not inferred only from queue state.

## Traceability and Reproducibility Implications

- [CANDIDATE-IMPLICATION] Trace records should separate:
  - domain operation identity
  - queue task identity
  - retry/redelivery counters and timestamps
  - terminal domain outcome
- [CANDIDATE-IMPLICATION] Reproducibility claims should reference immutable
  generation inputs and attempt lineage, independent of whether queue transport
  performed internal retries.
- [CANDIDATE-IMPLICATION] Operational observability should preserve distinctions
  between RETRY, FAILURE, REVOKED, and domain-level canceled/superseded states.

## Risks and Failure Modes (Candidate)

- [CANDIDATE-RISK] Duplicate side effects under redelivery when handlers are not
  idempotent.
- [CANDIDATE-RISK] False “new attempt” counting if infrastructure retries are
  conflated with domain attempts.
- [CANDIDATE-RISK] Lost-causality audit trails when queue IDs are used as sole
  provenance identifiers.
- [CANDIDATE-RISK] Ambiguous cancellation semantics if revocation is interpreted
  as guaranteed non-execution.

## Candidate Requirements

- CANDIDATE CR-ARCH-QUEUE-001: Define explicit mapping between domain-level
  GenerationAttempt identity and infrastructure task identity, including
  one-to-many/many-to-one edge cases.
- CANDIDATE CR-ARCH-QUEUE-002: Define a retry taxonomy and event schema that
  distinguishes infra redelivery, Celery retry, application retry, and
  human-regeneration.
- CANDIDATE CR-ARCH-QUEUE-003: Require idempotency safeguards for all generation
  operations with side effects, including deterministic duplicate detection
  strategy and audit fields.
- CANDIDATE CR-ARCH-QUEUE-004: Require provenance logs to include both queue
  execution context and domain orchestration context without collapsing them.
- CANDIDATE CR-ARCH-QUEUE-005: Require explicit terminal-state reconciliation
  rules between Celery state machine and domain state machine.

## Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-QUEUE-001: Should one domain GenerationAttempt map to one
  Celery task ID, or can it span multiple IDs under selected retry policies?
- CANDIDATE ADR-Q-ARCH-QUEUE-002: Which retry classes are allowed to remain
  within one GenerationAttempt versus forcing a new GenerationAttempt?
- CANDIDATE ADR-Q-ARCH-QUEUE-003: What minimum idempotency key composition is
  required for reproducible and safe generation operations?
- CANDIDATE ADR-Q-ARCH-QUEUE-004: How should revocation/cancel semantics map to
  user-facing production statuses when partial execution may have occurred?

## Open Questions

- How should long-running multi-step generation pipelines encode partial side
  effects so replay/retry can be selective rather than all-or-nothing?
- Which invariants must hold for cross-provider retry portability under a shared
  workflow abstraction?
- What retention window is required for queue-level telemetry to support
  reproducibility and incident forensics?

## Source-Limit Disclosure

- This record captures official Celery and Redis semantics relevant to retry and
  idempotency boundaries, but it does not by itself select one production
  infrastructure profile.
- Celery behavior can vary by broker/backend and runtime policy selection; this
  document intentionally records semantic capabilities and cautions rather than
  an implementation choice.
- All implications, requirements, and ADR items in this file are candidates.