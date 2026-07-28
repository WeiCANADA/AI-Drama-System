# QC Domain Specification v1.0

## Document Status

- Status: Draft
- Research Blocker Status: Research-unblocked for drafting provider-neutral QC domain baseline; partially blocked for final closure on canonical QC target boundaries, ArtifactVersion attachment policy, and minimum cross-profile QC policy profile.
- ADR Blocker Status: No immediate ADR blocker for publishing this draft; targeted ADR review is likely required before freezing canonical QC target model, hard-fail semantics, and policy/evaluator versioning commitments.
- Specification Type: Domain Specification
- Domain: QC
- Version: 1.0
- Evidence Basis:
  - System constraints and invariants from docs/DEVELOPMENT_SPEC.md.
  - Domain boundary constraints from docs/domain/shot.md, docs/domain/storyboard.md, docs/domain/character.md, docs/domain/continuity.md, docs/domain/workflow.md, and docs/domain/artifact.md.
  - Cross-layer domain synthesis from docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md.
  - AI research synthesis from docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md.
  - Production synthesis from docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md.
  - Workflow architecture synthesis from docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md.
  - Supporting research records from docs/research/production/storyboarding.md, docs/research/production/continuity.md, docs/research/production/cinematography.md, docs/research/production/animation-production-pipeline.md, docs/research/architecture/workflow-observability.md, and docs/research/architecture/provenance-interchange.md.
- Related Specifications:
  - docs/DEVELOPMENT_SPEC.md
  - docs/domain/shot.md
  - docs/domain/storyboard.md
  - docs/domain/character.md
  - docs/domain/continuity.md
  - docs/domain/workflow.md
  - docs/domain/artifact.md
- Related Research:
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
  - docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md
  - docs/research/ai-papers/RL-AI-BOARD-001-story2board.md
  - docs/research/ai-papers/RL-AI-CHAR-001-storymaker.md
  - docs/research/ai-papers/RL-AI-CHAR-002-instantcharacter.md
  - docs/research/production/storyboarding.md
  - docs/research/production/continuity.md
  - docs/research/production/cinematography.md
  - docs/research/production/animation-production-pipeline.md
  - docs/research/architecture/workflow-observability.md
  - docs/research/architecture/provenance-interchange.md
- Related ADRs:
  - docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed)
  - docs/adr/ADR-0002-idempotency-contract.md (Proposed)

Unresolved architecture choices remain subject to ADR review and acceptance.
This document does not create or accept ADRs.

## Purpose

Define provider-neutral QC semantics for quality governance across automated
checks, human review, issue tracking, quality decisions, workflow-gate inputs,
and reproducible history.

QC is more than a simple pass/fail check because production quality is:

- multi-dimensional rather than single-score,
- partly automatable and partly human-judged,
- historically versioned rather than overwritten,
- linked to workflow review and rework rather than identical to workflow,
- necessary for reproducibility, auditability, and production governance.

## Domain Definition

QC is the production quality-governance domain that evaluates planned or
produced objects against explicit quality criteria, records findings and issues,
links human review with automated evidence, and produces decision inputs for
workflow policy.

Evaluated conceptual direction:

Production Object
-> QC Policy / Criteria
-> QC Evaluation
-> Findings / Issues
-> Decision / Review
-> Workflow Gate / Rework

Interpretation boundary:

- This direction is evidence-consistent.
- QC is a domain concern with strong workflow relationships.
- Workflow consumes QC outcomes but does not collapse into QC semantics.

## Terminology

- QC:
  - Production quality-governance domain for evaluating outputs and planning
    states against explicit quality expectations.
- QC Target:
  - The production object, version, representation, or state being evaluated.
- QC Policy:
  - Versioned quality-governance definition describing applicable criteria,
    decision rules, evaluator references, and review expectations.
- QC Criterion:
  - One quality dimension or evaluative question.
- QC Metric:
  - A measurement/output form used by an evaluator to produce evidence for one
    criterion.
- QC Evaluator:
  - The mechanism or reviewer producing evidence, score, classification, or
    judgment.
- QC Evaluation:
  - Immutable historical evaluation record tied to exact target, criterion,
    policy version, evaluator version, and produced result.
- QC Finding:
  - Observed result from evaluation, such as a score, discrepancy,
    classification, or uncertainty note.
- QC Issue:
  - Production-significant quality problem requiring tracking, correction,
    review, or accepted exception handling.
- QC Decision:
  - Quality-governance conclusion derived from findings, policy, and/or review.
- Review:
  - Human examination of target quality, findings, issues, or decisions.
- Approval:
  - Positive review decision allowing a target or stage to proceed under policy.
- Threshold:
  - Policy-scoped boundary used in interpreting evaluator outputs.
- Severity:
  - Quality impact classification for issues or findings.
- Confidence:
  - Degree of certainty associated with evaluator output or review judgment.
- Manual Override:
  - Human decision that explicitly diverges from automated result or default
    policy interpretation while preserving rationale.

Term policy:

- Conceptual names are not binding class/table/API names.
- QC Criterion != QC Metric.
- QC Evaluation != QC Decision.
- QC Decision != Workflow Gate.
- QC Finding != QC Issue.
- Human Review != Automated Score.

## Domain Responsibilities

QC owns or anchors:

- quality-evaluation intent and governance semantics,
- versioned policies and criteria,
- evaluation history and historical traceability,
- findings and quality-issue interpretation,
- human review linkage and override rationale,
- quality decision rationale,
- workflow-gate input semantics,
- reproducibility of quality decisions through versioned evidence.

QC does not own:

- Shot production intent,
- Storyboard planning identity,
- Character identity truth,
- Continuity state truth,
- Artifact identity and version lineage,
- Workflow gate execution,
- provider/model-specific evaluator implementation,
- telemetry pipeline implementation.

## Domain Boundaries

Required distinctions:

- QC != Workflow:
  - QC evaluates quality and records evidence; Workflow orchestrates production
    progression.
- QC != Workflow Gate:
  - gate is workflow transition control; QC provides evidence or decision input.
- QC != Continuity:
  - Continuity owns expected temporal production state; QC evaluates outputs or
    plans against continuity expectations.
- QC != Artifact:
  - Artifact is durable production output identity; QC evaluates artifact
    quality.
- QC != GenerationResult:
  - GenerationResult records execution outcome; QC records quality evaluation.
- QC != Provider Evaluator:
  - evaluator implementation is one evidence source, not QC domain ontology.
- QC Metric != domain quality truth:
  - metric output is evidence for a criterion, not the criterion itself.
- QC Evaluation != QC Decision:
  - evaluation captures evidence; decision interprets evidence under policy.
- Automated score != human approval:
  - human review may confirm, override, contextualize, or reject automated
    output.

## QC Target

QC may evaluate multiple target categories, including:

- Shot production intent
- Storyboard
- Storyboard Panel
- Character appearance/reference context
- Continuity state
- Artifact
- ArtifactVersion
- GenerationResult
- scene-level or multi-shot sequence
- audio/subtitle output
- composite or delivery artifact

Target policy:

- no single universal target type is required.
- QC target selection depends on production stage, review purpose, and policy.

Concrete-media evaluation direction:

- concrete media-quality evaluations usually attach to exact ArtifactVersion or
  exact Representation evaluated.
- higher-level planning or governance evaluations may attach to Shot,
  Storyboard, Continuity state, or workflow-stage outputs.

## Artifact / ArtifactVersion Relationship

This boundary is critical and currently best treated conservatively.

Evaluated direction:

Artifact
-> ArtifactVersion
-> QC Evaluation

Candidate interpretation:

- concrete media-quality evaluations normally reference exact ArtifactVersion.
- when representation details materially affect quality judgment, evaluation may
  also reference the specific Representation examined.
- logical Artifact may support summary or latest-known QC interpretation, but
  historical QC evidence must remain attached to exact evaluated version.

Implications:

- Artifact != ArtifactVersion remains preserved.
- QC history should not migrate from one artifact version to another by
  overwrite.
- evaluator upgrades or threshold changes should trigger new evaluations rather
  than mutation of historical results.

Blocker assessment:

- this relationship is sufficiently clear for QC draft scope.
- final policy for new Artifact versus new ArtifactVersion remains an Artifact
  domain question and may affect implementation detail, but it does not block QC
  baseline semantics.

## Shot Relationship

QC may evaluate shot-related concerns such as:

- framing
- cinematography intent alignment
- narrative alignment
- shot completeness
- character participation coherence
- continuity compliance

Boundary rule:

- Shot remains production intent/context, not media payload.
- shot-level QC may evaluate planned intent, observed output, or both.

## Storyboard Relationship

Storyboard QC may evaluate:

- narrative alignment
- shot coverage
- composition
- scene diversity
- continuity
- character consistency

Preserved distinction:

- Storyboard Panel != Artifact

Interpretation:

- a panel planning evaluation is not identical to evaluation of a visualization
  artifact associated with that panel.
- storyboard QC may examine planning clarity, pacing, coverage, and continuity
  before final generation.

## Character Relationship

Character-related QC may evaluate:

- identity consistency
- holistic appearance consistency
- wardrobe/version alignment
- reference conformity

Boundary rule:

- Character and CharacterVersion remain domain identities and appearance
  baselines.
- model-specific techniques such as ArcFace, DreamSim, SigLIP, DINOv2, CLIP, or
  similar tools remain evaluator or technology candidates, not Character or QC
  core ontology.

## Continuity Relationship

Required distinction:

- Continuity domain owns expected temporal production state.
- QC evaluates planned, observed, or generated outputs against relevant
  continuity expectations.

Interpretation:

- QC may raise continuity-related findings or issues.
- QC does not replace Continuity state ownership or continuity-resolution truth.

## Workflow Relationship

QC provides evidence and outcomes that workflow review gates may consume.

Preserved distinction:

- QC Evaluation != Workflow Gate

Workflow relationship semantics:

- workflow policy decides what QC result is sufficient to proceed.
- not every QC failure automatically blocks workflow globally.
- rework or approval transitions remain workflow decisions, even when strongly
  informed by QC outcomes.

## QC Policy

QC Policy is a conceptual, versionable quality-governance definition.

Candidate responsibilities:

- applicable target scope
- criteria set
- evaluator references
- threshold and decision interpretation policy
- human-review requirements
- severity interpretation rules
- production-profile applicability

Historical rule:

- every historical QC evaluation must remain traceable to exact policy version
  used.

This draft defines semantics only, not schema.

## QC Criterion

QC Criterion is one quality dimension or evaluative question.

Examples include:

- character identity consistency
- wardrobe consistency
- continuity compliance
- prompt or narrative alignment
- composition diversity
- framing intent
- artifact technical validity
- dialogue or subtitle alignment
- audio quality

These examples are not a frozen enum.

## QC Metric / Evaluator

Required distinction:

- QC Criterion = what is being judged
- QC Metric or QC Evaluator = how evidence is produced

Evaluator candidates may include:

- DreamSim
- CLIP similarity
- VQAScore
- face similarity methods
- diversity heuristics
- LLM judge
- human reviewer

Boundary rule:

- these remain evaluator or technology candidates.
- they must not be promoted into core QC domain semantics without separate
  architecture acceptance.

## Automated Evaluation

Automated evaluation conceptually includes:

- evaluator identity and version
- output score or classification
- confidence
- raw evidence reference when available
- target reference
- policy and criterion reference
- timestamp

Scale policy:

- this draft does not define one universal numeric scale.
- different evaluators may produce different evidence forms.

## Human Review

Human review is independent from automated evaluation.

Human review may:

- confirm automated result
- disagree with automated result
- mark intentional deviation
- require correction
- approve despite low automated score
- reject despite high automated score

Historical rule:

- reviewer rationale and history must remain preserved.

## QC Evaluation

QC Evaluation is an immutable historical evaluation event or record tied to:

- exact target and target version when applicable
- exact QC policy and policy version
- exact criterion
- evaluator identity and evaluator version
- produced result
- evidence context
- time

Historical rule:

- old evaluations must not be destructively overwritten after evaluator
  upgrades, threshold changes, or policy revisions.

## Findings

QC Finding is observed evaluation result.

Possible forms:

- numeric score
- categorical finding
- detected discrepancy
- evidence annotation
- uncertainty statement

Required distinction:

- finding does not automatically equal issue.

## QC Issue

QC Issue is a production-significant quality problem requiring tracking,
review, correction, or accepted exception handling.

Interpretive relationship:

Finding
-> policy and review interpretation
-> Issue

QC Issue may include:

- severity
- target
- criterion
- evidence
- status
- resolution context
- intentional-deviation flag

Status policy:

- this draft does not freeze final statuses.

Required distinction:

- QC Finding != QC Issue

## QC Decision

QC Decision is quality-governance conclusion derived from evidence and policy.

Examples may include:

- acceptable
- needs review
- needs revision
- rejected
- accepted exception

Decision may be:

- automated policy outcome
- human decision
- combined decision

Required distinctions:

- QC Evaluation != QC Decision
- QC Decision != Workflow Gate

State policy:

- this draft does not freeze final decision enum.

## Thresholds

Threshold rules:

- thresholds are policy-version scoped.
- thresholds are evaluator-aware where relevant.
- thresholds must be historically traceable.

This draft does not define global thresholds such as one mandatory score
boundary for all evaluators or profiles.

## Multi-Dimensional QC

QC must support multiple quality dimensions rather than one universal score.

Candidate dimensions include:

- identity consistency
- holistic appearance
- continuity
- narrative or text alignment
- composition or cinematography
- scene diversity
- temporal coherence
- technical media validity
- audio or subtitle quality

Aggregation rule:

- multi-dimensional evidence may remain partially independent.
- no requirement exists here for one global score.

## Aggregation

Evaluation results may be aggregated at multiple levels, such as:

- criterion
- target
- Shot
- Scene
- Workflow gate input

Boundary rule:

- this draft does not define final weighting or aggregation algorithm.
- low aggregate scores must not hide critical hard-fail issues.

## Severity / Criticality

Severity is distinct from raw metric score.

Interpretation examples:

- small aesthetic variation may be low severity
- wrong character identity may be high severity even if some scores look strong

This draft does not freeze final severity enum.

## Overrides / Intentional Deviations

Production may intentionally violate a QC criterion.

Examples:

- deliberate continuity break
- stylized framing
- intentional wardrobe change
- creative distortion

Required rule:

- allow review or override with rationale rather than modifying historical QC
  evidence.

## Versioning

Version semantics should cover:

- QC Policy
- Criterion definition
- Evaluator or model version
- threshold configuration
- human-review policy

Historical rule:

- evaluations must reference exact versions used at evaluation time.

## Provenance

QC history should remain traceable to:

- target object and target version
- production context
- workflow run when relevant
- QC policy and version
- evaluator and version
- evaluation result
- human reviewer or decision
- resulting issue or rework linkage
- timestamp

Boundary rule:

- QC provenance must not depend solely on telemetry retention.

## Review / Rework Relationship

Conceptual sequence:

QC Finding
-> QC Decision
-> Workflow gate
-> Rework

Boundary rule:

- QC does not execute workflow transition itself unless workflow policy
  explicitly consumes QC decision as input.
- review and rework remain business-governance transitions in workflow.

## Lifecycle

Conceptual lifecycle concerns exist for:

- evaluation
- issue
- review or decision

Draft-scope rule:

- lifecycle concepts are valid in draft scope.
- final global state machines or enums remain out of scope.

## Validation / Invariants

Evidence-supported candidate invariants:

- Historical QC evaluations are immutable and traceable.
- Evaluator upgrades do not rewrite prior evaluation results.
- QC Evaluation is tied to exact target and target version when applicable.
- QC Metric or Evaluator does not define criterion meaning.
- Automated result does not automatically equal human approval.
- QC Issue remains distinct from raw Finding.
- QC Decision remains distinct from Workflow Gate.
- QC provenance survives telemetry expiry requirements.
- Multi-dimensional QC is preferred over single-score reduction.

## Candidate Information Model

Conceptual only.

| Concept | Purpose | Classification | Required? | Notes |
|---|---|---|---|---|
| qc_policy_identity | Stable QC policy anchor | CORE DOMAIN | Yes | Governs applicable quality interpretation scope. |
| qc_policy_version | Historical policy version reference | VERSIONED DOMAIN | Yes | Historical evaluations must pin exact version. |
| qc_criterion_identity | Stable quality-dimension anchor | CORE DOMAIN | Yes | Criterion meaning remains distinct from evaluator. |
| evaluator_reference | Evaluator identity reference | EVALUATOR LINK | Usually | May be automated tool or human reviewer role. |
| evaluator_version | Evaluator version/procedure reference | EVALUATOR LINK | Usually | Prevents silent rewriting after evaluator changes. |
| qc_target_reference | Evaluated target linkage | TARGET LINK | Yes | May point to Shot, Panel, ArtifactVersion, Continuity state, etc. |
| qc_target_version_ref | Exact version/representation linkage | TARGET LINK | No | Especially important for concrete media QC. |
| qc_evaluation_identity | Historical evaluation anchor | EVALUATION DOMAIN | Yes | Immutable evidence record identity. |
| score_or_result | Produced evidence output | EVALUATION DOMAIN | Usually | Numeric or categorical; no universal scale required. |
| confidence | Certainty/strength qualifier | EVALUATION DOMAIN | No | Evaluator-specific interpretation. |
| evidence_refs | Raw evidence or annotation linkage | EVIDENCE LINK | No | Optional supporting artifacts or notes. |
| finding_record | Observed evaluation finding | EVALUATION DOMAIN | Usually | Finding != issue by rule. |
| issue_refs | Quality issue linkage | ISSUE LINK | No | Only when production-significant. |
| human_review_refs | Human review linkage | REVIEW LINK | No | Supports override/approval provenance. |
| decision_record | Quality decision linkage | DECISION LINK | No | Decision != evaluation, gate, or target identity. |
| workflow_linkage | Workflow gate/run context linkage | WORKFLOW LINK | No | QC informs workflow without becoming workflow. |
| provenance_context | Durable traceability context | CORE DOMAIN | Yes | Must outlive telemetry retention windows. |

## Candidate Requirements

Classification policy in this section:

- ACCEPT INTO DRAFT SPEC: accepted only into this draft scope.
- KEEP AS CANDIDATE: evidence supports direction but architecture is not yet
  frozen.
- DEFER: not blocking this draft.
- REJECT FOR CORE DOMAIN: excluded from core QC semantics.

Requirement set:

- CR-QC-001: Support multi-dimensional QC rather than one universal score.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: AI and domain-foundation synthesis strongly support multi-objective
    storyboard and character QC.

- CR-QC-002: Preserve explicit separation among criterion, metric/evaluator,
  evaluation, finding, issue, decision, and workflow gate.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: required for provider neutrality and historical traceability.

- CR-QC-003: Keep human review as first-class quality-governance input rather
  than treating automated score as final truth.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: production review evidence and continuity/review provenance
    principles.

- CR-QC-004: Preserve historical evaluations under exact target/version,
  policy/version, and evaluator/version context.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: reproducibility and provenance requirements across workflow and
    artifacts.

- CR-QC-005: Support storyboard QC dimensions including alignment,
  composition, scene diversity, and consistency as candidate policy concerns.
  - Classification: KEEP AS CANDIDATE
  - Basis: research supports them strongly, but mandatory profile policy is not
    settled.

- CR-QC-006: Support continuity-related QC findings/issues linked to explicit
  continuity expectations.
  - Classification: ACCEPT INTO DRAFT SPEC
  - Basis: continuity research and synthesis support explicit issue tracking.

- CR-QC-007: Require all concrete artifact-quality evaluations to target
  ArtifactVersion or Representation.
  - Classification: KEEP AS CANDIDATE
  - Basis: strong semantic direction, but final artifact version policy remains
    open.

- CR-QC-008: Define mandatory global thresholds for selected evaluator tools.
  - Classification: REJECT FOR CORE DOMAIN
  - Basis: thresholds are policy-version and evaluator-context dependent.

- CR-QC-009: Define mandatory DreamSim, CLIP, VQAScore, face-recognition, or
  LLM-judge adoption for core QC.
  - Classification: REJECT FOR CORE DOMAIN
  - Basis: evaluator technologies remain candidates, not accepted architecture.

- CR-QC-010: Define final workflow blocking semantics for all QC failures.
  - Classification: DEFER
  - Basis: workflow policy remains profile-specific and may require ADR review.

## ADR Review Points

Potential architecture decisions likely to require ADR review:

- canonical QC target model across planning objects, artifacts, and sequences,
- ArtifactVersion versus Representation attachment policy for concrete media QC,
- policy/evaluator versioning strategy and minimum immutable QC evidence
  contract,
- hard-fail versus soft-score semantics,
- cross-domain QC issue representation and ownership boundaries,
- aggregation policy for multi-dimensional quality outcomes.

No ADR is created or accepted by this document.

## Open Questions

- Should concrete artifact QC always target ArtifactVersion?
- Can QC target a Representation directly?
- How should one QC Evaluation cover multiple Shots or artifacts?
- What minimum QC dimensions are required for v1?
- Which criteria are mandatory by production profile?
- How should human override affect workflow gates?
- How should evaluator confidence be interpreted?
- How should critical issues override aggregate scores?
- What happens when evaluator or model versions change?
- What QC data is needed for reproducibility versus analytics?

## Out of Scope

Explicitly out of scope in this document:

- Django models
- serializers
- migrations
- API design
- final QC algorithms
- model selection
- evaluator service implementation
- threshold tuning
- ML training
- vector embeddings
- workflow orchestration implementation
- final state machines
- UI implementation

## Traceability

Status interpretation rule preserved:

- Research Finding != Candidate Requirement
- Candidate Requirement != Proposed ADR
- Proposed ADR != Accepted ADR

| Candidate decision / boundary | Evidence source | Evidence status |
|---|---|---|
| QC is a first-class production quality-governance concern linked to workflow but distinct from workflow | docs/DEVELOPMENT_SPEC.md; docs/research/production/animation-production-pipeline.md; docs/domain/workflow.md | Existing specification + strong research support |
| QC should support multi-dimensional evaluation rather than one universal score | docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md (REQ-QC-001, RP-005); docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (CLA-009) | Strong candidate-level support |
| Human review and issue tracking remain essential alongside automated scoring | docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md (D-003, CLA-009); docs/research/production/continuity.md; docs/research/production/storyboarding.md | Strong candidate-level support |
| QC targeting often needs exact ArtifactVersion or Representation for concrete media | docs/domain/artifact.md; docs/research/production/animation-production-pipeline.md; docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md | Existing specification + candidate-level support |
| QC evaluates continuity expectations but does not own continuity truth | docs/domain/continuity.md; docs/research/production/continuity.md | Existing specification + strong support |
| QC evaluates cinematography/alignment/coverage as quality dimensions without making camera parameters core QC ontology | docs/domain/shot.md; docs/research/production/cinematography.md; docs/research/production/storyboarding.md | Existing specification + candidate-level support |
| QC provenance must outlive telemetry retention and remain historically traceable | docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md; docs/research/architecture/workflow-observability.md; docs/domain/artifact.md | Strong candidate-level support |
| ADR-0001 and ADR-0002 remain Proposed and are relevant only as surrounding workflow-generation context | docs/adr/ADR-0001-generation-attempt-retry-semantics.md (Proposed); docs/adr/ADR-0002-idempotency-contract.md (Proposed) | Proposed ADR status only |

Status progression for architecture closure:

Research
-> Proposed ADR
-> Accepted ADR
-> Implementation

## Specification Readiness

Stable in this draft:

- QC as first-class provider-neutral quality-governance domain.
- Explicit separation between QC and workflow gates.
- Explicit separation between criterion and metric/evaluator.
- Explicit separation between evaluation, finding, issue, and decision.
- Human review as independent and historically traceable input.
- Multi-dimensional QC direction.
- QC provenance and historical immutability direction.

Ambiguous or unresolved:

- canonical QC target attachment policy across ArtifactVersion,
  Representation, and multi-target evaluation,
- minimum mandatory QC dimensions by profile,
- global versus profile-specific hard-fail semantics,
- minimum immutable QC evidence profile,
- aggregation policy for mixed automated and human evidence.

ArtifactVersion relationship assessment:

- ArtifactVersion relationship is clearer after artifact.md.
- concrete media QC should usually attach to exact ArtifactVersion and possibly
  exact Representation.
- final universal rule is not yet accepted and may still require ADR review.

Research blocking determination:

- no additional blocking research is required for this draft.
- existing research is sufficient for baseline QC semantics.

Likely ADR-needed before implementation freeze:

- canonical QC target and attachment model,
- ArtifactVersion versus Representation evaluation policy,
- hard-fail versus soft-score semantics,
- minimum immutable QC evidence contract,
- aggregation policy for multi-dimensional QC outcomes.

## Layer 4 Research Requests

Current determination:

- no new blocking Layer 4 research request is required for this QC draft.

Relevant completed research already covers:

- multi-dimensional storyboard QC and scene-diversity evidence,
- character-consistency evidence beyond face similarity,
- continuity review and issue-tracking evidence,
- workflow review/rework and provenance boundaries,
- provenance-versus-telemetry separation.

Additional research should be requested only when implementation scope requires
narrower evaluator benchmarking, threshold calibration, or cross-profile gate
policy closure.
