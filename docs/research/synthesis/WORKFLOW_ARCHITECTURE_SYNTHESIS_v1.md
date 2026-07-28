# Workflow Architecture Synthesis v1

## 1. Scope

This synthesis consolidates Layer 4 Batch 2 research records into workflow
architecture implementation-planning guidance while preserving domain /
application / infrastructure boundaries.

In scope:

- WorkflowRun versus infrastructure execution boundaries.
- State semantics, retry semantics, event semantics, observability semantics.
- Cross-source agreements, unresolved questions, and ADR review queue.
- Consolidated candidate requirements across QUEUE / STATE / EVENT / OBS.

Out of scope:

- No code, no final state enum, no final state machine topology.
- No ADR acceptance.
- No technology selection.
- No event sourcing adoption.

## 2. Cross-Source Agreements

Agreement A

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: WorkflowRun is a domain/application concept, not an infrastructure
	task/runtime entity.
- Supporting records: workflow.md, RL-ARCH-QUEUE-001, RL-ARCH-STATE-001,
	RL-ARCH-EVENT-001, RL-ARCH-OBS-001.
- Confidence: High.
- Architectural implication: WorkflowRun identity and transitions must be
	modeled independently from queue task identity and runtime state.

Agreement B

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: WorkflowRun state semantics must remain separate from task/runtime
	state semantics.
- Supporting records: workflow.md, RL-ARCH-QUEUE-001, RL-ARCH-STATE-001,
	RL-ARCH-EVENT-001.
- Confidence: High.
- Architectural implication: Infrastructure state can trigger evaluation but
	cannot directly define authoritative domain state.

Agreement C

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: Retry, redelivery, domain new attempt, and human regeneration are
	distinct semantic classes.
- Supporting records: RL-ARCH-QUEUE-001, RL-ARCH-STATE-001,
	RL-ARCH-OBS-001.
- Confidence: High.
- Architectural implication: Execution and provenance models must classify these
	paths explicitly and avoid conflated counters/statuses.

Agreement D

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: Review/rework is business-level revision semantics and is not
	technical retry.
- Supporting records: workflow.md, RL-ARCH-STATE-001, RL-ARCH-EVENT-001,
	RL-ARCH-OBS-001.
- Confidence: High.
- Architectural implication: Review and rework need first-class workflow
	transition semantics and provenance representation.

Agreement E

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: Domain Event, Integration Event, Queue Message, and Telemetry Event
	are separate semantic objects.
- Supporting records: RL-ARCH-EVENT-001, RL-ARCH-OBS-001,
	RL-ARCH-QUEUE-001.
- Confidence: High.
- Architectural implication: Event architecture must define explicit boundaries
	and mapping rules without semantic collapse.

Agreement F

- Label: MODERATE CROSS-SOURCE SUPPORT
- Statement: Cancellation requires intent/confirmation/reconciliation semantics
	when partial side effects may exist.
- Supporting records: RL-ARCH-STATE-001, RL-ARCH-QUEUE-001,
	RL-ARCH-EVENT-001.
- Confidence: Medium-high.
- Architectural implication: Cancellation cannot be represented as a single
	runtime flag; reconciliation policy is required.

Agreement G

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: Idempotency ownership primarily belongs to application/domain
	operation semantics, not queue IDs.
- Supporting records: RL-ARCH-QUEUE-001, RL-ARCH-EVENT-001,
	RL-ARCH-OBS-001.
- Confidence: High.
- Architectural implication: Idempotency contracts must be domain-aware and
	auditable.

Agreement H

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: Domain identity must remain distinct from telemetry identity.
- Supporting records: RL-ARCH-OBS-001, RL-ARCH-EVENT-001,
	RL-ARCH-QUEUE-001.
- Confidence: High.
- Architectural implication: Correlation requires explicit linkage fields,
	not identity equivalence.

Agreement I

- Label: STRONG CROSS-SOURCE SUPPORT
- Statement: telemetry retention != provenance retention.
- Supporting records: RL-ARCH-OBS-001, RL-ARCH-EVENT-001,
	workflow.md principles.
- Confidence: High.
- Architectural implication: Historical reproducibility must rely on durable
	provenance records, not trace/log retention windows.

Agreement J

- Label: OPEN QUESTION
- Statement: Canonical minimum state vocabulary, attempt-boundary policy,
	correlation/causation metadata profile, and cancellation reconciliation rules
	are not yet accepted.
- Supporting records: RL-ARCH-STATE-001, RL-ARCH-QUEUE-001,
	RL-ARCH-EVENT-001, RL-ARCH-OBS-001.
- Confidence: High that unresolved status is real.
- Architectural implication: These require ADR review before final architecture
	lock-in.

## 3. Layer Boundary Model

Production Domain
-> Workflow Domain
-> Generation Application Layer
-> Infrastructure Execution
-> Provider Execution

Boundary intent:

- Production Domain: Story/scene/shot intent and production governance context.
- Workflow Domain: WorkflowDefinition/Version/Run semantics, gates, rework,
	cancellation, and business progression.
- Generation Application Layer: GenerationTask / GenerationAttempt planning,
	orchestration, and policy mapping between workflow and execution systems.
- Infrastructure Execution: queue delivery, worker execution, ack/retry,
	timeout/revoke, scheduling/transport mechanics.
- Provider Execution: provider-specific runtime operations and opaque external
	processing semantics.

Preserved separation constraints:

- WorkflowRun != Celery Task
- GenerationAttempt != infrastructure retry
- Domain Event != Queue Message
- Domain Identity != Trace ID

## 4. WorkflowRun / Infrastructure Task Boundary

Explicit answer to question 1 and 2:

- WorkflowRun is the authoritative domain/application representation of current
	workflow process state and business progression.
- Infrastructure task/runtime entities represent execution transport mechanics.
- Infrastructure events/states are input signals for policy evaluation, not
	direct domain truth.

Stable boundary principles:

- Domain transition decisions must be governed by workflow policy semantics.
- Runtime state changes (delivery/retry/redelivery/revoke) can be recorded for
	observability/provenance linkage but cannot replace WorkflowRun semantics.

## 5. Retry / Attempt / Regeneration Semantics

Explicit answer to question 3 and 5:

| Class | Semantic layer | Changes business intent? | Creates new domain identity? | Provenance requirement | Idempotency relevance |
|---|---|---|---|---|---|
| transport redelivery | Infrastructure execution | No | No | Record execution redelivery evidence linked to same business operation context | High, duplicate side effects risk |
| infrastructure retry | Infrastructure execution | No | No (domain-level not implied) | Record retry count, failure cause, and mapping to same domain operation context | High |
| workflow step retry | Workflow domain / generation application policy | Usually no (same intent) | Usually no new WorkflowRun identity; step-attempt lineage policy unresolved | Record policy-triggered retry reason and step lineage | High |
| new GenerationAttempt | Generation application + workflow semantics | Usually no intent change, but new execution attempt class | Yes, new GenerationAttempt identity | Durable attempt lineage with linkage to prior attempt(s) | High |
| workflow rework | Workflow domain (review/policy loop) | Yes (updated/clarified production intent or acceptance criteria) | Typically yes for revision lineage scope; exact identity policy unresolved | Durable business decision lineage, revision intent, and artifact lineage | High |
| human-requested regeneration | Workflow domain / user action | Yes or explicit re-run intent by human request | Yes (new domain action/attempt/run scope per policy) | Durable user intent and approval context | High |

Evidence limitation note:

- Final identity-creation rules for step-level retry versus new attempt remain
	unresolved and require ADR decision.

## 6. Idempotency Principles

Explicit answer to question 4:

- Idempotency responsibility belongs primarily to application/domain operation
	semantics, because infrastructure delivery is not exactly-once.
- Queue/runtime IDs are insufficient as sole idempotency basis because they are
	transport execution identities, not business operation identities.
- Duplicate handling must be based on domain-aware operation semantics and
	auditable classification of duplicate/no-op/effective execution.

Unresolved items:

- Final idempotency key composition.
- Cross-layer key propagation contract.
- Retry-class-specific idempotency enforcement boundaries.

## 7. Workflow State-Machine Direction

Explicit answer to question 2 and 6:

- WorkflowRun aggregate/state remains the authoritative current-state
	representation unless a future ADR changes that.
- Domain state and infrastructure execution state are distinct.
- Review/gate waiting and review outcomes are domain semantics, not runtime
	statuses.
- Recoverable failure versus terminal failure requires explicit policy mapping.
- Cancellation requires at least requested/confirmed/reconciled conceptual
	phases where side effects are possible.
- Direction favors canonical semantic core plus profile-specific extensions.

Not defined here:

- No final state enum.
- No final transition graph.

## 8. Review / Rework Semantics

Explicit answer to question 5:

- Review rejection / revision required / rework are business governance
	transitions driven by quality/policy decisions.
- Technical retry is an execution reliability mechanism for same business
	operation intent.
- Rework must remain visible as business provenance, including decision cause,
	revised intent context, and subsequent generation lineage.

## 9. Event Architecture

Explicit answer to question 7:

- Domain Event: durable fact/evidence of business-significant transition in
	workflow or related domain context.
- Integration Event: externalized contract derived from domain facts for
	cross-boundary interoperability.
- Queue Message: transport/execution artifact used by infrastructure.
- Telemetry Event: observability signal in tracing/logging pipelines.

Relationship rule:

- Domain events are durable facts/evidence of business-significant transitions,
	but this synthesis does NOT adopt event sourcing.

## 10. Event Identity / Correlation / Causation

Explicit answer to question 8:

- Event identity, aggregate identity, queue task identity, and trace identity
	must remain separate.
- Correlation groups related activities within a process/run context.
- Causation references immediate triggering predecessor event/action.
- Correlation and causation metadata should be explicit and queryable, not
	inferred from one identity namespace.

Evidence usage boundary:

- CloudEvents may inform envelope/interchange semantics only.
- OpenTelemetry and W3C may inform telemetry propagation/correlation semantics
	only.

## 11. Ordering / Duplicate Handling

Explicit answer to question 9:

Stable principles with cross-source support:

- Assume duplicate delivery can occur.
- Do not depend on strict global ordering for correctness.
- Enforce idempotent business operation handling.
- Use event identity + scoped source/correlation context for duplicate
	classification.
- Apply aggregate version/precondition checks for out-of-order safety where
	appropriate.

Not fixed here:

- No single final reconciliation algorithm is selected.

## 12. Observability Contract

Explicit answer to question 10 and 11:

Minimum conceptual observability needs by entity:

- WorkflowRun: run lifecycle transitions, gate outcomes, terminal reason class,
	cancellation phases, correlation IDs.
- WorkflowStep: step start/end/outcome, dependency or block reason class,
	retry/rework classification.
- GenerationTask: dispatch, scheduling/queue lag, execution handoff markers,
	failure category.
- GenerationAttempt: attempt ordinal/class, execution durations, error class,
	relation to prior attempt/rework decision.
- Provider execution: request/response boundary timing, provider-visible
	operation status class, partial visibility markers.
- Artifact: materialization status, lineage linkage, approval/provisional class.

Signal separation:

- traces: causal execution paths and timing structure.
- metrics: aggregate rates/latency/failure/retry/rework distributions.
- logs: detailed diagnostics and structured incident context.
- domain events: business-significant transition facts.
- provenance records: durable reproducibility lineage.

## 13. Provenance vs Observability

Explicit answer to question 12:

- telemetry retention != provenance retention

Mandatory synthesis conclusion:

- Historical reproducibility must not depend on trace/log retention.
- Provenance durability requirements must be specified independently from
	telemetry sampling/retention policy.

## 14. Stable Architecture Principles

- WAP-001: Keep WorkflowRun semantics independent from infrastructure runtime
	semantics.
- WAP-002: Keep domain state authoritative for current workflow business state.
- WAP-003: Preserve semantic separation among retry/redelivery/rework/new
	attempt/human regeneration.
- WAP-004: Keep review/rework as business-governance semantics distinct from
	technical retry.
- WAP-005: Preserve separation among Domain Event, Integration Event,
	Queue Message, and Telemetry Event.
- WAP-006: Keep event identity, aggregate identity, queue identity, and trace
	identity separate.
- WAP-007: Design for duplicate and out-of-order resilience using idempotency
	and explicit precondition checks.
- WAP-008: Treat provenance and observability as linked but non-equivalent;
	reproducibility cannot rely solely on telemetry retention.
- WAP-009: Maintain canonical workflow semantic core with profile-specific
	extension capability.

## 15. Consolidated Candidate Requirements

Consolidated (de-duplicated) set across QUEUE / STATE / EVENT / OBS:

- CCR-WF-001: Define formal boundary contract between WorkflowRun state and
	infrastructure execution state (QUEUE+STATE).
- CCR-WF-002: Define retry taxonomy and mapping contract that distinguishes
	transport redelivery, infrastructure retry, workflow retry, new
	GenerationAttempt, rework, and human regeneration (QUEUE+STATE+OBS).
- CCR-WF-003: Define idempotency contract for side-effectful generation
	operations with auditable duplicate handling policy (QUEUE+EVENT+OBS).
- CCR-WF-004: Define canonical WorkflowRun semantic core and profile-specific
	extension governance (STATE).
- CCR-WF-005: Define cancellation semantics and reconciliation contract for
	partial side effects/artifacts (STATE+QUEUE+EVENT).
- CCR-WF-006: Define event architecture boundary contract for Domain Event,
	Integration Event, Queue Message, and Telemetry Event (EVENT+OBS).
- CCR-WF-007: Define event identity/correlation/causation metadata policy with
	explicit layer separation (EVENT+OBS).
- CCR-WF-008: Define duplicate/out-of-order processing principles and
	reconciliation policy boundaries (EVENT+QUEUE+STATE).
- CCR-WF-009: Define minimum observability contract across WorkflowRun,
	WorkflowStep, GenerationTask, GenerationAttempt, provider execution,
	and artifact lifecycle (OBS).
- CCR-WF-010: Define provenance-versus-telemetry retention boundary so
	reproducibility guarantees do not depend on telemetry retention (OBS+EVENT).
- CCR-WF-011: Define provenance record minimum linkage to domain transitions,
	attempt lineage, and artifact lineage without identity collapse (QUEUE+EVENT+
	OBS).

## 16. Candidate ADR Review Queue

HIGH PRIORITY

- GenerationAttempt vs infrastructure task identity mapping.
- Retry / attempt boundary policy (when new attempt identity is mandatory).
- Idempotency contract and duplicate classification policy.
- Canonical WorkflowRun semantic core and profile-extension governance.
- Cancellation reconciliation contract for partial side effects.

MEDIUM PRIORITY

- Event envelope/profile strategy for integration boundaries.
- Correlation/causation metadata minimum profile.
- Observability minimum contract and high-cardinality policy.

DEFER

- Detailed telemetry schema shape.
- Signal-specific optimization patterns (sampling profiles, exporter-level
	policies).
- Profile-specific naming vocabularies beyond canonical core.

Note:

- This is a candidate ADR review queue only; no ADR is accepted here.

## 17. Open Questions

- What exact rule differentiates policy-level step retry from required new
	GenerationAttempt creation?
- Which WorkflowRun semantic states are mandatory core versus profile aliases?
- What minimum causation/correlation fields are required across all event
	classes?
- Which domain events must be externalized as integration contracts?
- How should cancellation reconciliation represent partially materialized
	artifacts across profiles?
- What minimum retention and linkage guarantees are required for provenance data
	independent of telemetry retention?

## 18. Workflow Implementation Readiness

A. Workflow domain model

- Readiness: implementation-planning-ready.
- Blocking ADRs: canonical core semantic vocabulary scope.
- Deferrable issues: profile-specific naming and optional extension details.

B. GenerationTask / Attempt execution semantics

- Readiness: partially blocked.
- Blocking ADRs: attempt-vs-retry identity boundary mapping.
- Deferrable issues: provider-specific execution detail normalization.

C. Retry/idempotency

- Readiness: partially blocked.
- Blocking ADRs: final idempotency contract and duplicate classification policy.
- Deferrable issues: key composition optimizations and operational tuning.

D. Event architecture

- Readiness: implementation-planning-ready.
- Blocking ADRs: integration externalization policy and minimum metadata profile.
- Deferrable issues: envelope/profile formatting conventions.

E. Observability

- Readiness: partially blocked.
- Blocking ADRs: minimum mandatory contract and high-cardinality governance.
- Deferrable issues: signal-level schema refinement and retention tuning.

F. Cancellation

- Readiness: partially blocked.
- Blocking ADRs: cancellation reconciliation contract across partial side
	effects.
- Deferrable issues: profile-level UX/status wording and analytics decoration.

Overall assessment:

- Workflow architecture is partially blocked, with clear planning path and
	bounded ADR set.

## 19. Recommended Next Step

Smallest next step:

- Draft one focused candidate ADR package for the highest-priority blocker set:
	GenerationAttempt identity mapping + retry/attempt boundary + idempotency
	contract, because these three decisions unblock downstream state/event/
	observability implementation planning without forcing technology selection.

## 20. Conclusion

Layer 4 Batch 2 research provides coherent implementation-planning guidance for
workflow architecture boundaries, state semantics, retry semantics, event
semantics, and observability/provenance separation.

Research synthesis informs architecture.
It does not itself accept architecture decisions.

Interpretation boundaries preserved:

- WorkflowRun aggregate/state remains authoritative current-state
	representation unless a future ADR changes that.
- Domain events are durable facts/evidence of business-significant transitions,
	but this synthesis does NOT adopt event sourcing.
- CloudEvents may inform envelope/interchange semantics only.
- OpenTelemetry may inform telemetry semantics only.
- Celery/Redis remain infrastructure candidates, not domain architecture.
