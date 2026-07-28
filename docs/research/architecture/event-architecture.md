# Event Architecture Research

## Research Metadata

- Research ID: RL-ARCH-EVENT-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Scope: event architecture semantics for workflow orchestration in AI Drama System
- Required context reviewed:
  - AGENTS.md
  - docs/domain/workflow.md
  - docs/domain/continuity.md
  - docs/research/architecture/task-queue-retry-idempotency.md
  - docs/research/architecture/workflow-state-machine.md
- Constraints applied:
  - No broker selection
  - No event-sourcing adoption
  - No code
  - No ADR creation
  - No modification to docs/domain/workflow.md
  - CloudEvents treated as interchange/envelope standard, not domain ontology

## Research Question

How should AI Drama System define event semantics and boundaries so that domain
workflow facts, cross-boundary integration contracts, and infrastructure transport
messages remain distinct while preserving traceability, deduplication safety,
and observability?

## CloudEvents Findings

- [OFFICIAL-DEFINED] CloudEvents is a vendor-neutral event format specification
  focused on interoperability of event description and transport representation.
- [OFFICIAL-DEFINED] CloudEvents required core attributes are `id`, `source`,
  `specversion`, and `type`.
- [OFFICIAL-DEFINED] Optional attributes include `subject`, `time`,
  `datacontenttype`, and `dataschema`.
- [OFFICIAL-DEFINED] `source` + `id` uniquely identify an event; consumers may
  treat same pair as duplicate delivery.
- [OFFICIAL-DEFINED] CloudEvents separates event metadata context from event data
  payload and supports extensions.
- [OFFICIAL-DEFINED] HTTP binding defines binary/structured/batched transport
  mappings and treats routing target as protocol concern.
- [OFFICIAL-DEFINED] CloudEvents does not define business semantics of event
  types; producer owns type semantics.
- [OFFICIAL-DEFINED] Distributed tracing extension (`traceparent`, `tracestate`)
  carries trace context when explicitly used, and is not a replacement for
  protocol-specific hop headers.
- [INTERPRETATION] CloudEvents is useful as envelope/interchange guidance for
  event identity and interoperability, while domain meaning must remain owned by
  AI Drama domain models.

## Domain Event Semantics

Question 1: What is a Domain Event?

- [INTERPRETATION] A Domain Event is an internal business fact that something of
  domain significance has happened in the workflow and production context.
- [CANDIDATE-RULE] Domain events describe business truth in terms of
  WorkflowRun/WorkflowStep/review/rework/continuity outcomes, not queue runtime
  mechanics.
- [CANDIDATE-RULE] Domain event naming and payload should be bounded-context
  semantic (workflow and continuity meaning first).
- [QUEUE-RESEARCH-CONSISTENT] Domain Event != queue message != Celery task state.

Example analysis (examples only, not accepted final catalog):

- WorkflowRunStarted:
  - candidate domain fact that run lifecycle entered active progression.
- WorkflowStepCompleted:
  - candidate domain fact that a business step completed according to workflow
    semantics, independent from internal retries.
- ReviewRequested / ReviewApproved / RevisionRequested:
  - candidate domain gate decision facts.
- ContinuityIssueRaised:
  - candidate domain fact from continuity bounded context.
- ArtifactProduced:
  - candidate domain fact that an artifact with provenance became available.
- WorkflowRunCancelled:
  - candidate domain terminal fact, potentially followed by reconciliation facts
    if partial side effects exist.

## Integration Event Semantics

Question 2: What is an Integration Event?

- [INTERPRETATION] An Integration Event is an explicit externalized contract
  event published across bounded/integration boundaries for other subsystems.
- [CANDIDATE-RULE] Integration Events are derived from domain facts, but shaped
  for interoperability and contract stability.
- [CANDIDATE-RULE] Integration Event schemas should be intentionally versioned and
  backward-compatibility managed independently from internal aggregate models.
- [CANDIDATE-RULE] Not every domain event must be externalized; externalization
  should be policy-driven.

Question 5: Which events should cross bounded/integration boundaries?

- [CANDIDATE-DIRECTION] Cross-boundary publication is most justified for events
  needed by other bounded contexts or platforms:
  - review lifecycle notifications,
  - continuity issue lifecycle notifications,
  - generation request/result handoff notifications,
  - artifact availability notifications,
  - run terminal outcome notifications.
- [CANDIDATE-DIRECTION] Highly internal orchestration noise (fine-grained retries,
  transient queue behavior) should generally stay internal.

## Queue / Infrastructure Message Semantics

Question 3: What is an infrastructure queue/message event?

- [OFFICIAL-DEFINED] Queue/infrastructure message artifacts represent transport
  and execution semantics (delivery, ack/redelivery, retry, revoke, timeout).
- [QUEUE-RESEARCH-CONSISTENT] Celery task identity and runtime state are
  infrastructure mechanics and not equivalent to WorkflowRun state transitions.
- [INTERPRETATION] Queue messages can carry commands or event payloads, but their
  identity/lifecycle remains transport-level artifact semantics.

Preserved distinctions:

- Domain Event != Integration Event
- Domain Event != Queue Message
- Domain Event != Celery Task
- Domain Event != WorkflowRun State

## Event Identity

Question 6 (part): How should event identity, source, subject, type, time, and
version be represented conceptually?

- [OFFICIAL-DEFINED] CloudEvents offers a useful conceptual baseline:
  - `id`: event identifier
  - `source`: producing context identity
  - `type`: event semantic classifier
  - `subject`: entity or sub-resource within source scope
  - `time`: occurrence or producer-assigned time
  - `specversion`: envelope/spec interpretation
  - `dataschema`: optional payload schema locator
- [CANDIDATE-RULE] AI Drama should maintain separate identities for:
  - event identity,
  - domain aggregate identity (e.g., WorkflowRun),
  - infrastructure message/task identity.
- [CANDIDATE-RULE] Event identity should support duplicate detection but should
  not be overloaded as business aggregate identity.

## Correlation and Causation

Question 6 (part): How should correlation and causation be represented?

- [INTERPRETATION] Correlation and causation are not equivalent:
  - correlation links related events in the same business process instance,
  - causation links an event to the immediate triggering prior event/action.
- [OFFICIAL-DEFINED] CloudEvents core does not mandate dedicated causation or
  correlation attributes; extension attributes are expected for additional
  metadata needs.
- [OFFICIAL-DEFINED] CloudEvents distributed tracing extension references W3C
  Trace Context fields (`traceparent`, `tracestate`) for trace linkage when used.
- [CANDIDATE-RULE] AI Drama should conceptually preserve at least:
  - workflow correlation identity (run-level/process-level),
  - direct causation pointer (triggering event/action),
  - optional transport trace context for observability.

## Ordering / Duplication

Question 7: How should duplicate delivery and ordering uncertainty be handled?

- [OFFICIAL-DEFINED] CloudEvents does not guarantee delivery order or exactly-once
  behavior; transport/protocol concerns remain outside core event semantics.
- [QUEUE-RESEARCH-CONSISTENT] Retry/redelivery and duplicate delivery are normal
  infrastructure realities.
- [CANDIDATE-RULE] Consumers should treat duplicate delivery as expected and
  enforce idempotent handling by business operation semantics.
- [CANDIDATE-RULE] Event processing should not depend on strict global ordering;
  policy should rely on aggregate version checks, state preconditions, and
  causation/correlation metadata.
- [CANDIDATE-RULE] Duplicate detection should use event identity plus scoped
  source context, not queue task ID alone.

## Versioning

Question 6 (part) and question 8 support concern: version representation and
semantics evolution.

- [OFFICIAL-DEFINED] CloudEvents `type` and `dataschema` are key versioning
  surfaces; spec does not enforce a single versioning scheme.
- [CANDIDATE-RULE] Distinguish:
  - envelope/spec version (interchange layer),
  - event contract version (integration layer),
  - domain model version (internal business model evolution).
- [CANDIDATE-RULE] Breaking contract changes should produce explicit new
  integration event versioning strategy.

## Event vs State

Question 8: Should events be authoritative state, derived notifications, or vary
by event class?

- [INTERPRETATION] Event classes should vary in authority role:
  - domain events: authoritative record of business facts that occurred,
  - integration events: externalized notifications/contracts derived from domain
    facts,
  - queue messages: transport artifacts carrying commands/events.
- [CANDIDATE-RULE] WorkflowRun state remains authoritative current state in its
  bounded context; events are fact records and transition evidence, not
  replacement of aggregate state model by default.
- [CANDIDATE-RULE] This research does not adopt full event sourcing.

## Provenance Relationship

Question 9 (part): How should events relate to provenance?

- [EXISTING-SPEC-CONSISTENT] Workflow and generation architecture emphasize
  reproducibility and traceability.
- [INTERPRETATION] Event records should contribute provenance graph edges between:
  - business action/decision,
  - generation request/attempt/result,
  - produced artifacts,
  - review and continuity decisions.
- [CANDIDATE-RULE] Provenance should preserve separation of domain fact lineage
  and infrastructure execution lineage while maintaining explicit linkage.

## Observability Relationship

Question 9 (part): How should events relate to observability?

- [INTERPRETATION] Observability requires linking logs/metrics/traces with event
  facts and workflow identities without collapsing semantic layers.
- [OFFICIAL-DEFINED] W3C Trace Context plus CloudEvents tracing extension provide
  a standards-based way to propagate trace linkage metadata.
- [CANDIDATE-RULE] Observability data should include event identity,
  correlation/causation references, and trace context where available.
- [CANDIDATE-RULE] Infrastructure telemetry (retry count, redelivery, queue lag)
  should remain infrastructure observability signals, not direct domain state.

## Stable Findings

- Stable finding A: Domain Event, Integration Event, and Queue Message are
  different semantic objects and must remain distinct.
- Stable finding B: CloudEvents is best used as envelope/interchange guidance,
  not as core domain ontology.
- Stable finding C: WorkflowRun state transitions are domain semantics and must
  not be inferred directly from queue/task runtime events.
- Stable finding D: Correlation and causation need explicit conceptual treatment
  beyond core CloudEvents required attributes.
- Stable finding E: Duplicate delivery and ordering uncertainty must be assumed;
  idempotent business operations are required.
- Stable finding F: Event records should reinforce provenance and observability
  while preserving layer separation.

## Gaps

- No accepted canonical event taxonomy yet for AI Drama bounded contexts.
- No accepted policy for which domain events must be externalized as integration
  contracts.
- No accepted causation/correlation attribute profile for internal events.
- No accepted event contract versioning policy across profile-specific workflows.
- No accepted reconciliation policy for late/duplicate/out-of-order event
  processing in every workflow stage.

## AI Drama System Implications

- Workflow orchestration should emit business-semantic domain events at key run,
  step, review, continuity, and cancellation transitions.
- Integration boundaries should use explicit, stable event contracts derived from
  domain facts.
- Generation and queue infrastructure should emit operational signals that are
  linked, but not conflated, with domain event streams.
- Provenance and observability models should include event-correlation structure
  to support reproducibility and incident analysis.

## Candidate Requirements

- CANDIDATE CR-ARCH-EVENT-001: Define explicit semantic separation among domain
  events, integration events, and infrastructure messages.
- CANDIDATE CR-ARCH-EVENT-002: Define which WorkflowRun and WorkflowStep changes
  produce domain events and which are internal-only transitions.
- CANDIDATE CR-ARCH-EVENT-003: Define policy for promoting domain events into
  integration event contracts.
- CANDIDATE CR-ARCH-EVENT-004: Define conceptual event identity and metadata
  minimum set including id/source/type/time and optional subject/schema.
- CANDIDATE CR-ARCH-EVENT-005: Define correlation and causation representation
  rules, including compatibility with trace-context propagation.
- CANDIDATE CR-ARCH-EVENT-006: Require duplicate-tolerant event consumption and
  idempotent business operation handling.
- CANDIDATE CR-ARCH-EVENT-007: Define event contract versioning policy distinct
  from domain model and transport spec versions.
- CANDIDATE CR-ARCH-EVENT-008: Define provenance/observability linkage model that
  preserves domain vs infrastructure semantic boundaries.

## Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-EVENT-001: What is the minimal canonical internal domain
  event vocabulary for WorkflowRun lifecycle and gate decisions?
- CANDIDATE ADR-Q-ARCH-EVENT-002: Which example events should be domain-only,
  which should be integration contracts, and under what policy gates?
- CANDIDATE ADR-Q-ARCH-EVENT-003: What causation/correlation metadata profile is
  mandatory for internal and cross-boundary events?
- CANDIDATE ADR-Q-ARCH-EVENT-004: How should out-of-order and duplicate events be
  reconciled for review/rework/cancellation-sensitive workflows?
- CANDIDATE ADR-Q-ARCH-EVENT-005: How should event versioning interact with
  profile-specific workflow extensions?

## Open Questions

- Should AI Drama define one shared event envelope profile for all internal
  bounded contexts, or allow bounded-context-specific profiles under a core rule
  set?
- Should causation point to immediate predecessor only, or allow multi-cause
  representation for merged decisions?
- Which continuity and review events require guaranteed external publication, and
  which remain internal observability signals?
- How should artifact lifecycle events distinguish between provisional outputs
  and approved production assets at integration boundaries?

## Sources

- AGENTS.md
- docs/domain/workflow.md
- docs/domain/continuity.md
- docs/research/architecture/task-queue-retry-idempotency.md
- docs/research/architecture/workflow-state-machine.md
- CloudEvents core specification
  - URL: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
  - Accessed: 2026-07-28
- CloudEvents primer
  - URL: https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md
  - Accessed: 2026-07-28
- CloudEvents HTTP protocol binding
  - URL: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md
  - Accessed: 2026-07-28
- CloudEvents distributed tracing extension
  - URL: https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/distributed-tracing.md
  - Accessed: 2026-07-28
- W3C Trace Context Recommendation
  - URL: https://www.w3.org/TR/trace-context/
  - Accessed: 2026-07-28

Source-limit disclosure:

- This research uses CloudEvents as primary source for event envelope semantics.
- Business event meaning remains candidate interpretation for AI Drama domain.
- All requirements and ADR items above are CANDIDATE only.
