# Workflow State-Machine Research

## Research Metadata

- Research ID: RL-ARCH-STATE-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Scope: workflow state-machine semantics for AI Drama System
- Required context reviewed:
  - AGENTS.md
  - docs/domain/workflow.md
  - docs/domain/continuity.md
  - docs/domain/storyboard.md
  - docs/research/architecture/task-queue-retry-idempotency.md
- Constraints applied:
  - No final state machine design
  - No enums or code
  - No ADR creation
  - No modification of docs/domain/workflow.md
  - No direct copying of Celery task states into domain ontology

## Research Question

What boundary and semantics should govern WorkflowRun state so that production
workflow meaning stays independent from queue/worker/provider execution state,
while still enabling review gates, rework, failure recovery, cancellation, and
profile-specific workflow variation?

## Domain State vs Infrastructure State

- [EXISTING-SPEC-CONSISTENT] docs/domain/workflow.md defines Workflow as
  production orchestration intent and explicitly separates it from queue tasks,
  provider graphs, and API transport.
- [QUEUE-RESEARCH-CONSISTENT] RL-ARCH-QUEUE-001 established that infrastructure
  retry/redelivery semantics are not equivalent to domain attempts or workflow
  transitions.
- [OFFICIAL-DEFINED] Celery and Step Functions document runtime execution states,
  retry/catch behavior, and delivery/retry mechanics as infrastructure execution
  semantics.
- [OFFICIAL-DEFINED] Temporal documents workflow execution outcomes and replay
  constraints, but these statuses still reflect execution system behavior.
- [INTERPRETATION] Domain state should represent production meaning and business
  progression; infrastructure state should represent task dispatch and execution
  transport behavior.

Preserved distinction:

- Workflow domain state != Celery task state
- Workflow domain state != GenerationAttempt state
- Workflow domain state != provider execution state

## WorkflowRun State Semantics

Question 1: What should WorkflowRun domain state represent?

- [EXISTING-SPEC-CONSISTENT] WorkflowRun is the run-level business object bound
  to WorkflowVersion and production context.
- [INTERPRETATION] WorkflowRun state should represent where production process
  intent stands: awaiting decision, progressing, blocked by review/policy,
  under rework, terminated, or complete.
- [CANDIDATE-RULE] WorkflowRun state should answer business questions first:
  - Can production proceed?
  - Is human decision required?
  - Is revision required?
  - Is the run terminal, and why?

Question 2: What remains infrastructure execution state?

- [OFFICIAL-DEFINED] Queue acknowledgement timing, redelivery, worker retry,
  timeout heartbeat, and broker delivery metadata remain infrastructure state.
- [QUEUE-RESEARCH-CONSISTENT] Infrastructure retry/redelivery is execution
  mechanics and must not automatically create new WorkflowRun transitions.
- [CANDIDATE-RULE] Infrastructure outcomes may emit events that trigger domain
  evaluation, but domain transition requires explicit workflow policy mapping.

## Review / Gate States

Question 3: How should review/gate states differ from technical task states?

- [EXISTING-SPEC-CONSISTENT] docs/domain/storyboard.md and
  docs/domain/continuity.md both require human review and revision/approval
  semantics.
- [PRIMARY-RESEARCH] Workflow Patterns milestone/state-based constructs support
  explicit decision control points separate from execution completion.
- [INTERPRETATION] Review/gate state captures production acceptability decision,
  not technical runtime result.
- [CANDIDATE-RULE] Technical success must not imply gate pass.
- [CANDIDATE-RULE] Gate outcomes can route to rework even when infrastructure
  execution succeeded.

## Failure / Recovery States

Question 5: How should recoverable failure differ from terminal failure?

- [OFFICIAL-DEFINED] SCXML and Step Functions distinguish transitionable error
  paths from terminal completion/fail conditions.
- [OFFICIAL-DEFINED] Temporal distinguishes closed terminal outcomes from
  in-progress execution.
- [INTERPRETATION] Recoverable failure means business intent can still proceed via
  retry/rework/escalation path under policy.
- [INTERPRETATION] Terminal failure means run cannot proceed without a new run or
  explicit restart policy.
- [CANDIDATE-RULE] Recoverability must be modeled in domain terms, not inferred
  solely from queue-level retriability.

## Retry vs Rework

Question 4: How should rework differ from retry?

- [QUEUE-RESEARCH-CONSISTENT] RL-ARCH-QUEUE-001: infra retry/redelivery is
  infrastructure execution semantics.
- [INTERPRETATION] Retry is usually same business intent execution retried due to
  technical/transient error.
- [INTERPRETATION] Rework is business-level revision loop triggered by review,
  policy, or quality mismatch; inputs or acceptance criteria may change.
- [CANDIDATE-RULE] Human regeneration must remain separate from infrastructure
  retry.
- [CANDIDATE-RULE] WorkflowRun transition to rework should carry decision cause,
  revision intent, and provenance references.

## Cancellation Semantics

Question 6: How should cancellation be represented when underlying work may have
already partially executed?

- [PRIMARY-RESEARCH] Workflow Patterns includes cancellation constructs
  (cancel task/case/region), supporting cancellation as first-class process
  semantics.
- [OFFICIAL-DEFINED] Step Functions and Temporal separate canceled outcomes from
  other terminal outcomes.
- [QUEUE-RESEARCH-CONSISTENT] Infrastructure cancel/revoke does not guarantee no
  side effects occurred.
- [INTERPRETATION] Domain cancellation should separate:
  - cancel requested
  - cancel confirmed (no further progression)
  - post-cancel reconciliation (partial work/artifacts present)
- [CANDIDATE-RULE] Cancellation representation should include reason, scope, and
  residual side-effect reconciliation status.

## Terminal vs Non-Terminal States

Explicit example analysis requested by task (without final vocabulary lock-in):

- Awaiting Review:
  - [INTERPRETATION] non-terminal domain gate-waiting state.
  - not equivalent to queue waiting or task pending.
- Revision Required:
  - [INTERPRETATION] non-terminal decision outcome indicating quality/policy gap.
  - implies rework path availability.
- In Rework:
  - [INTERPRETATION] non-terminal domain progression state under revision loop.
  - distinct from infrastructure retry.
- Blocked:
  - [INTERPRETATION] non-terminal hold caused by dependency, policy, or review
    missing information.
  - requires unblock condition semantics.
- Failed:
  - [INTERPRETATION] ambiguous without subtype; can be recoverable or terminal
    depending on policy and remaining allowed actions.
- Cancel Requested:
  - [INTERPRETATION] non-terminal intent state until cancellation resolution is
    reconciled.
- Cancelled:
  - [INTERPRETATION] terminal domain outcome for further progression of that run,
    while still permitting artifact reconciliation.
- Completed:
  - [INTERPRETATION] terminal successful domain outcome.

No final fixed vocabulary is accepted in this record.

## Global vs Profile-Specific State

Question 7: One global vocabulary, profile-specific states, or canonical core
plus extensions?

- [EXISTING-SPEC-CONSISTENT] docs/domain/workflow.md avoids forcing one rigid
  universal stage sequence across all profiles.
- [PRIMARY-RESEARCH] Workflow Patterns indicates control semantics vary by process
  context; variant patterns are normal.
- [INTERPRETATION] Small canonical semantic core plus profile-specific
  extensions is a strong candidate direction.
- [CANDIDATE-RULE] Canonical core should define invariants and interoperability
  semantics; profile layers define concrete stage labels and branch detail.

## Stable Findings

- Stable finding A: WorkflowRun state should represent production workflow
  semantics, not execution transport mechanics.
- Stable finding B: Infrastructure retry/redelivery remains infrastructure
  semantics and must not be equated with domain transition.
- Stable finding C: Review/gate outcomes are domain decisions and remain separate
  from technical task status.
- Stable finding D: Rework and retry are distinct semantics and need explicit
  separation.
- Stable finding E: Cancellation requires intent/confirmation/reconciliation
  distinction when partial execution is possible.
- Stable finding F: A canonical core plus profile-specific extensions is
  preferable to a single rigid global vocabulary candidate.

## Gaps

- Missing accepted policy for exact recoverable-vs-terminal decision boundaries.
- Missing accepted mapping contract from infrastructure events to domain
  transition triggers.
- Missing accepted blocked-state taxonomy and unblock criteria.
- Missing accepted cancellation reconciliation procedure for partial side effects.
- Missing accepted profile-extension governance rules.

## AI Drama System Implications

- WorkflowRun lifecycle design should prioritize production decision semantics and
  human review loops.
- GenerationAttempt lifecycle should remain related but separate from WorkflowRun
  state machine.
- Infrastructure adapter/event layer should expose retry/redelivery/cancel facts
  as input signals, not domain truth.
- Provenance and reproducibility should preserve both domain transitions and
  infrastructure execution traces without collapsing identities.

## Candidate Requirements

- CANDIDATE CR-ARCH-STATE-001: Define formal boundary contract between WorkflowRun
  domain state and infrastructure execution state.
- CANDIDATE CR-ARCH-STATE-002: Define explicit domain semantics for review waiting,
  revision required, rework, blocked, cancellation intent, cancellation outcome,
  completion, and failure categories.
- CANDIDATE CR-ARCH-STATE-003: Require explicit policy mapping from
  infrastructure events (retry/redelivery/timeout/revoke) to domain transition
  decisions.
- CANDIDATE CR-ARCH-STATE-004: Require explicit separation of retry vs rework in
  domain records and audit trails.
- CANDIDATE CR-ARCH-STATE-005: Require cancellation semantics to include
  requested/confirmed/reconciled phases where applicable.
- CANDIDATE CR-ARCH-STATE-006: Define canonical core plus profile-specific
  extension rules for workflow vocabularies.

## Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-STATE-001: What minimum canonical WorkflowRun semantic
  classes are mandatory across profiles?
- CANDIDATE ADR-Q-ARCH-STATE-002: Which example states should be core semantics
  versus profile-level aliases?
- CANDIDATE ADR-Q-ARCH-STATE-003: What reconciliation policy determines when
  infrastructure failure becomes domain rework versus technical retry?
- CANDIDATE ADR-Q-ARCH-STATE-004: What governance model should profile-specific
  state extensions follow to preserve interoperability?
- CANDIDATE ADR-Q-ARCH-STATE-005: What is the canonical cancellation
  reconciliation contract for partial artifacts and side effects?

## Open Questions

- Should WorkflowRun expose one combined failed state with metadata, or multiple
  failure categories as first-class domain states?
- Should blocked always require human action, or can policy allow automatic
  unblocking conditions?
- What evidence threshold is required to move from recoverable failure back to
  active progression without human review?
- Should cancellation reconciliation be mandatory for all profiles or only those
  with side-effectful generation stages?

## Sources

- AGENTS.md
- docs/domain/workflow.md
- docs/domain/continuity.md
- docs/domain/storyboard.md
- docs/research/architecture/task-queue-retry-idempotency.md
- W3C SCXML 1.0 Recommendation
  - URL: https://www.w3.org/TR/scxml/
  - Accessed: 2026-07-28
- Workflow Patterns Initiative
  - URL: http://www.workflowpatterns.com/
  - URL: http://www.workflowpatterns.com/patterns/control/index.php
  - Accessed: 2026-07-28
- Temporal official documentation
  - URL: https://docs.temporal.io/workflow-definition
  - URL: https://docs.temporal.io/workflow-execution
  - Accessed: 2026-07-28
- AWS Step Functions official documentation
  - URL: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html
  - URL: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html
  - Accessed: 2026-07-28
- Celery official documentation (infrastructure contrast only)
  - URL: https://docs.celeryq.dev/en/stable/userguide/tasks.html
  - URL: https://docs.celeryq.dev/en/stable/userguide/workers.html
  - URL: https://docs.celeryq.dev/en/stable/userguide/calling.html
  - Accessed: 2026-07-28
- OMG BPMN 2.0 specification index
  - URL: https://www.omg.org/spec/BPMN/2.0/
  - Accessed: 2026-07-28

Source-limit disclosure:

- All requirements and ADR items above are candidate only.
- This record intentionally avoids accepting a final state vocabulary or
  state-machine topology.