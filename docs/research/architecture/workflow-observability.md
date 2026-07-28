# Workflow Observability Research

## Research Metadata

- Research ID: RL-ARCH-OBS-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Scope: workflow observability semantics for AI Drama System orchestration
- Required context reviewed:
  - AGENTS.md
  - docs/domain/workflow.md
  - docs/domain/continuity.md
  - docs/research/architecture/task-queue-retry-idempotency.md
  - docs/research/architecture/workflow-state-machine.md
  - docs/research/architecture/event-architecture.md
- Constraints applied:
  - No vendor selection
  - No instrumentation code
  - No Django field design
  - No ADR creation
  - No change to docs/domain/workflow.md
  - No final telemetry schema
  - OpenTelemetry used as reference semantics, not domain ontology

## Research Question

What minimum provider-neutral observability semantics are needed to trace and
analyze WorkflowRun execution across workflow, generation, and provider layers
without converting telemetry constructs into domain constructs?

## OpenTelemetry Findings

- [OFFICIAL-DEFINED] OpenTelemetry separates signals (traces, metrics, logs)
  with shared context propagation, and treats them as cross-cutting concerns.
- [OFFICIAL-DEFINED] Trace identity is carried by TraceId/SpanId in SpanContext
  and propagated via W3C Trace Context (`traceparent`, `tracestate`).
- [OFFICIAL-DEFINED] Spans represent operations with timing, attributes, events,
  status, links, and parent/child or link-based relationships.
- [OFFICIAL-DEFINED] Sampling is expected; not every trace/span is retained.
- [OFFICIAL-DEFINED] Metrics model is aggregation-oriented (instruments,
  measurements, views, readers/exporters), with cardinality and temporality
  controls.
- [OFFICIAL-DEFINED] Logs data model can carry TraceId/SpanId/TraceFlags for
  correlation but remains a separate signal from traces.
- [OFFICIAL-DEFINED] Context is immutable and is the standard in-process
  propagation mechanism for trace and baggage data.
- [INTERPRETATION] OpenTelemetry semantics support operational observability and
  correlation, but do not define AI Drama business identity or business truth.

## Trace Model

Conceptual chain under analysis:

WorkflowRun
-> WorkflowStep
-> GenerationTask
-> GenerationAttempt
-> Provider Execution
-> Artifact

Candidate interpretation:

- [CANDIDATE-RULE] A trace should represent one causally connected execution
  path for a workflow run context, with links where strict parent/child is not
  semantically accurate.
- [CANDIDATE-RULE] WorkflowRun should be treated as business correlation context,
  not as trace identity itself.
- [CANDIDATE-RULE] Asynchronous fan-out/fan-in and deferred execution should use
  span links where causal relation exists without strict tree nesting.
- [CANDIDATE-RULE] Provider-side operations may continue outside local process;
  local traces should represent observed execution boundary and correlation data,
  not claim complete provider internals.

## Span Boundaries

Candidate boundary guidance (not final schema):

- [CANDIDATE-RULE] Workflow orchestration coordination step can be represented by
  orchestration spans.
- [CANDIDATE-RULE] WorkflowStep-level execution windows are natural candidate
  spans when they represent distinct business-stage work.
- [CANDIDATE-RULE] GenerationTask dispatch/coordination can be traced as
  orchestration spans distinct from provider runtime spans.
- [CANDIDATE-RULE] GenerationAttempt lifecycle (request preparation, submit,
  await, result handling) can be represented by multiple spans where useful.
- [CANDIDATE-RULE] Provider execution visibility may be represented by CLIENT /
  PRODUCER / CONSUMER style spans depending on call and async semantics.
- [CANDIDATE-RULE] Artifact persistence/materialization can be traced as explicit
  spans to support latency and failure diagnostics.

## Domain Identity vs Telemetry Identity

Preserved separation:

- Domain identity != Trace ID != Span ID != Infrastructure Task ID

Candidate interpretation:

- [CANDIDATE-RULE] Domain identities (WorkflowRun ID, WorkflowStep ID,
  GenerationTask ID, GenerationAttempt ID, Artifact ID) are business identities
  and must remain stable independently of telemetry systems.
- [CANDIDATE-RULE] TraceId/SpanId are observability transport identities used
  for correlation in telemetry pipelines.
- [CANDIDATE-RULE] Infrastructure task identifiers (queue delivery ID, worker
  execution ID) are execution-mechanism identities and must not be promoted to
  domain identity.
- [CANDIDATE-RULE] Correlation should be explicit via attributes/fields, not via
  identity collapse.

## Correlation

Cross-layer correlation target:

WorkflowRun <-> WorkflowStep <-> GenerationTask <-> GenerationAttempt
<-> provider execution <-> Artifact

Candidate rules:

- [CANDIDATE-RULE] Use domain IDs as correlation attributes on spans, metrics,
  and logs where policy permits.
- [CANDIDATE-RULE] Preserve causation and correlation as distinct concepts:
  correlation groups related activity; causation identifies triggering parent
  fact or action.
- [CANDIDATE-RULE] For async boundaries, carry trace context where available and
  attach business correlation keys so analysis does not depend on trace
  continuity alone.
- [CANDIDATE-RULE] Domain event references and telemetry context should be linked
  but not treated as interchangeable identifiers.

## Retry / Redelivery Observability

Explicit retry chain:

GenerationAttempt
-> infrastructure task execution
   - delivery
   - retry
   - redelivery

Candidate interpretation:

- [QUEUE-RESEARCH-CONSISTENT] Infrastructure retry/redelivery is normal execution
  behavior and must be observable.
- [CANDIDATE-RULE] Infrastructure retry/redelivery must not automatically imply
  creation of new domain GenerationAttempt.
- [CANDIDATE-RULE] Observability should distinguish:
  - domain attempt ordinal/lifecycle,
  - infrastructure execution count/delivery count,
  - terminal failure classification.
- [CANDIDATE-RULE] Retry telemetry should support diagnosing queue, worker,
  timeout, and transient provider issues without rewriting domain semantics.

## Review / Rework Observability

Explicit rework chain:

Review decision
-> Rework
-> new/updated production intent
-> new generation execution

Candidate interpretation:

- [CANDIDATE-RULE] Rework must be visible as business provenance and business
  transition sequence, not merely as technical retry noise.
- [CANDIDATE-RULE] Review gate decisions and rework triggers should be
  observable as domain-significant milestones with explicit correlation to prior
  outputs and decisions.
- [CANDIDATE-RULE] New generation execution initiated by rework should be
  distinguishable from infrastructure retries of the same attempt.

## Metrics

Candidate metric categories (conceptual only):

- [CANDIDATE-RULE] Workflow lifecycle metrics:
  - run throughput, stage latency, terminal outcome rates.
- [CANDIDATE-RULE] Generation pipeline metrics:
  - task queue wait time, attempt latency distribution, provider response/error
    distribution.
- [CANDIDATE-RULE] Retry behavior metrics:
  - redelivery counts, retry counts by failure class.
- [CANDIDATE-RULE] Review/rework metrics:
  - review turnaround, rework rate, rework cycle count.
- [CANDIDATE-RULE] Cardinality governance is required; high-cardinality domain
  identifiers should be applied with caution and explicit policy.

## Logs / Events

Candidate role separation:

- [CANDIDATE-RULE] Logs should capture diagnostic detail and execution context,
  including structured fields for domain correlation and infrastructure status.
- [CANDIDATE-RULE] Telemetry events (span events/log records) can capture
  time-point incidents (timeout, retry scheduled, provider warning, artifact
  write failure).
- [CANDIDATE-RULE] Log records with TraceId/SpanId support correlation but are
  not equivalent to domain events.

## Domain Event vs Telemetry Event

Preserved separation:

- Domain Event != Telemetry Event != Log Record

Candidate interpretation:

- [CANDIDATE-RULE] Domain events represent business facts in domain language.
- [CANDIDATE-RULE] Telemetry events are instrumentation-level time-point records
  attached to traces/log pipelines.
- [CANDIDATE-RULE] Log records are diagnostic records with flexible structure,
  severity, and optional trace context.
- [CANDIDATE-RULE] Correlation among the three should be explicit and
  queryable, but semantic layers must remain distinct.

## Reproducibility vs Operational Diagnosis

Critical distinction:

- telemetry retention != provenance retention

Candidate interpretation:

- [CANDIDATE-RULE] Operational diagnosis can rely heavily on traces/metrics/logs
  within retention windows.
- [CANDIDATE-RULE] Historical reproducibility must rely on durable domain
  provenance records (inputs, decisions, versions, parameters, artifact
  lineage), not solely on telemetry retention.
- [CANDIDATE-RULE] Sampling, downsampling, and telemetry expiration are expected
  observability properties and must not break reproducibility guarantees.

## Provenance Relationship

- [INTERPRETATION] Observability and provenance are complementary but distinct.
- [CANDIDATE-RULE] Provenance should capture business lineage and reproducibility
  evidence; observability should capture runtime behavior and diagnosis signals.
- [CANDIDATE-RULE] Cross-linking should exist between provenance records and
  telemetry context when available, while tolerating missing/expired telemetry.

## Stable Findings

- Stable finding A: OpenTelemetry provides strong vendor-neutral semantics for
  trace/metric/log modeling and context propagation.
- Stable finding B: Domain identity and telemetry identity must remain separate.
- Stable finding C: Infrastructure retry/redelivery must be observable without
  redefining domain attempt semantics.
- Stable finding D: Review/rework must be modeled as business-observable
  provenance transitions, not just technical retries.
- Stable finding E: Domain events, telemetry events, and log records are
  distinct semantic objects.
- Stable finding F: Reproducibility cannot depend solely on telemetry retention.

## Gaps

- No accepted minimum observability contract document yet for WorkflowRun and
  WorkflowStep.
- No accepted correlation key policy across traces, logs, metrics, and domain
  events.
- No accepted retry/redelivery observability profile across queue providers.
- No accepted review/rework observability vocabulary tied to continuity and
  approval workflows.
- No accepted boundary policy for high-cardinality identifiers in metrics.

## AI Drama System Implications

- Workflow architecture should define explicit observability contracts at
  orchestration boundaries while preserving domain model independence.
- Generation pipeline should expose retry and redelivery behavior clearly without
  conflating it with new domain attempts.
- Review/rework flows should emit business-meaningful observability signals that
  support auditability and continuity analysis.
- Provenance architecture should be designed to outlive telemetry retention
  windows.

## Candidate Requirements

- CANDIDATE CR-ARCH-OBS-001: Define a minimum observability contract for
  WorkflowRun/WorkflowStep lifecycle execution.
- CANDIDATE CR-ARCH-OBS-002: Define conceptual trace/span boundary guidance for
  workflow, generation, provider, and artifact stages.
- CANDIDATE CR-ARCH-OBS-003: Define mandatory identity-separation rules between
  domain IDs, trace/span IDs, and infrastructure execution IDs.
- CANDIDATE CR-ARCH-OBS-004: Define correlation and causation metadata policy
  across traces, metrics, logs, and domain events.
- CANDIDATE CR-ARCH-OBS-005: Define retry/redelivery observability requirements
  that do not auto-create domain attempts.
- CANDIDATE CR-ARCH-OBS-006: Define review/rework observability requirements as
  business provenance transitions.
- CANDIDATE CR-ARCH-OBS-007: Define telemetry-vs-provenance retention policy so
  reproducibility does not depend solely on telemetry.
- CANDIDATE CR-ARCH-OBS-008: Define cardinality and sensitivity policy for
  observability attributes.

## Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-OBS-001: What is the canonical minimum observability
  contract for workflow orchestration across bounded contexts?
- CANDIDATE ADR-Q-ARCH-OBS-002: Which execution boundaries must be parent/child
  spans versus linked spans in async orchestration?
- CANDIDATE ADR-Q-ARCH-OBS-003: Which domain identifiers are mandatory,
  optional, or prohibited in each telemetry signal?
- CANDIDATE ADR-Q-ARCH-OBS-004: How should queue-provider-specific retry
  semantics be normalized in observability without leaking provider ontology
  into domain architecture?
- CANDIDATE ADR-Q-ARCH-OBS-005: What retention and linkage policy is required
  between durable provenance and expiring telemetry?

## Open Questions

- Should WorkflowRun-level traces be single long-lived traces, segmented traces,
  or hybrid with explicit links for long-running operations?
- Which correlation attributes are required at every stage versus profile-
  specific extensions?
- How should observability represent partial provider visibility where provider
  internals are opaque?
- What minimum signal set is required for operational SLO diagnosis versus deep
  incident forensics?
- How should review/rework observability be standardized across continuity-heavy
  and continuity-light workflow profiles?

## Sources

- AGENTS.md
- docs/domain/workflow.md
- docs/domain/continuity.md
- docs/research/architecture/task-queue-retry-idempotency.md
- docs/research/architecture/workflow-state-machine.md
- docs/research/architecture/event-architecture.md
- OpenTelemetry Specification Overview
  - URL: https://opentelemetry.io/docs/specs/otel/overview/
  - Accessed: 2026-07-28
- OpenTelemetry Trace API
  - URL: https://opentelemetry.io/docs/specs/otel/trace/api/
  - Accessed: 2026-07-28
- OpenTelemetry Trace SDK
  - URL: https://opentelemetry.io/docs/specs/otel/trace/sdk/
  - Accessed: 2026-07-28
- OpenTelemetry Metrics API
  - URL: https://opentelemetry.io/docs/specs/otel/metrics/api/
  - Accessed: 2026-07-28
- OpenTelemetry Metrics SDK
  - URL: https://opentelemetry.io/docs/specs/otel/metrics/sdk/
  - Accessed: 2026-07-28
- OpenTelemetry Logs Data Model
  - URL: https://opentelemetry.io/docs/specs/otel/logs/data-model/
  - Accessed: 2026-07-28
- OpenTelemetry Context Specification
  - URL: https://opentelemetry.io/docs/specs/otel/context/
  - Accessed: 2026-07-28
- W3C Trace Context Recommendation
  - URL: https://www.w3.org/TR/trace-context/
  - Accessed: 2026-07-28

Source-limit disclosure:

- This research derives observability semantics from OpenTelemetry and W3C Trace
  Context official documents.
- AI Drama workflow-specific observability boundaries remain candidate
  interpretation.
- All requirements and ADR questions in this document are CANDIDATE only.
