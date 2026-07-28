# AI Drama Domain Foundation Synthesis v1

## 1. Scope

This document synthesizes two evidence layers:
- AI generation research (Layer 1)
- Real film/animation production knowledge (Layer 3)

Its purpose is to define a shared domain foundation for future specifications.

Status policy:
- This is a research synthesis artifact.
- This document does not define accepted architecture.
- This document does not accept ADRs.
- This document does not auto-promote candidate requirements.

Sources synthesized:
- `docs/research/synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md`
- `docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md`

## 2. Cross-Layer Agreements

### CLA-001: Scene and Shot remain distinct concepts

Evidence from Layer 1:
- Research preserves canonical `Story -> Episode -> Scene -> Shot` and treats Shot semantics separately from higher narrative units.

Evidence from Layer 3:
- Production synthesis explicitly states strong support for scene/shot separation from screenplay and film-grammar references.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Keep Scene and Shot as separate domain concepts in future Scene and Shot specifications.

### CLA-002: Shot remains the primary production unit

Evidence from Layer 1:
- Candidate ADR set explicitly preserves Shot as canonical audiovisual unit, including when keyframes/anchors are used.

Evidence from Layer 3:
- Cross-record principles keep Shot as primary execution unit in production pipeline framing.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future workflow and generation specs should attach execution/review/provenance primarily at Shot scope (while permitting higher-level planning scopes).

### CLA-003: Storyboard is a first-class planning/review stage

Evidence from Layer 1:
- Storyboard is treated as planning and QC stage; candidate requirements include dedicated storyboard workflow and multi-objective storyboard QC.

Evidence from Layer 3:
- Strong production evidence supports storyboard lifecycle, revision, pitch/review, and approval flows.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future Storyboard specification should model lifecycle state and review provenance, not only generated panel artifacts.

### CLA-004: Character identity must be distinct from mutable appearance

Evidence from Layer 1:
- Stable principles and candidate requirements separate persistent Character identity from mutable CharacterVersion/appearance state and support multi-reference assets.

Evidence from Layer 3:
- Production synthesis identifies character identity/version separation as candidate direction tied to continuity and reference governance.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future Character Asset specification should separate identity, version, and contextual appearance constraints.

### CLA-005: Production intent must stay separate from provider implementation

Evidence from Layer 1:
- Candidate ADRs and principles require provider-agnostic production intent and adapter-level translation.

Evidence from Layer 3:
- Cross-record principles and candidate ADRs explicitly separate domain intent from workflow/provider execution detail.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future Workflow and Shot specs should define neutral intent contracts, with provider-specific mappings outside core domain entities.

### CLA-006: Continuity must be represented explicitly as tracked state

Evidence from Layer 1:
- Continuity requirements include historical context transfer and drift-control support across shots/segments.

Evidence from Layer 3:
- Continuity is treated as explicit cross-stage tracked process with issue/status/provenance expectations.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future Continuity specification should define explicit continuity entities/records rather than implicit prompt-only continuity.

### CLA-007: Generation and production should be hierarchical and staged

Evidence from Layer 1:
- Hierarchical decomposition and staged planning/rendering are central findings for long-form coherence.

Evidence from Layer 3:
- Stage-based pipeline model with iterative review/rework loops is strongly supported.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future Workflow and Production specifications should encode stage boundaries and controlled transitions.

### CLA-008: Workflow stages require review, provenance, and version history

Evidence from Layer 1:
- Candidate requirements and principles emphasize continuity/QC traceability and workflow context/routing.

Evidence from Layer 3:
- Candidate requirements explicitly require stage gates, review records, and artifact/workflow provenance.

Combined confidence:
- STRONG CROSS-LAYER SUPPORT

Architecture implication:
- Future Artifact & Provenance and Workflow specifications should define immutable historical records and reviewable state transitions.

### CLA-009: Multi-dimensional QC is preferred over single-score QC

Evidence from Layer 1:
- Storyboard/character QC findings reject single-metric consistency optimization.

Evidence from Layer 3:
- Production evidence supports combining structured checks with human review and continuity context.

Combined confidence:
- MODERATE CROSS-LAYER SUPPORT

Architecture implication:
- Future QC specification should support multiple dimensions and explicit aggregation policy, not one global score.

### CLA-010: Provider-neutral camera/shot intent is a valid domain direction

Evidence from Layer 1:
- Shot spatial representation is required to be provider-neutral.

Evidence from Layer 3:
- Cinematography findings separate intent from technical parameterization and recommend adapter translation.

Combined confidence:
- MODERATE CROSS-LAYER SUPPORT

Architecture implication:
- Future Shot specification should define camera/spatial intent vocabulary independently of model-specific controls.

## 3. Cross-Layer Differences

### D-001: AI keyframes/anchors vs production Shot units

- AI layer emphasizes anchor/keyframe strategies for long-form drift control.
- Production layer centers canonical planning/execution around Shot.
- Domain stability rule: represent keyframes/anchors as workflow or artifact-level adjuncts to Shot, not replacement units.

### D-002: Identity embeddings vs production character references

- AI layer discusses embeddings/encoders/adapters as technique choices.
- Production layer emphasizes approved reference sets, versions, and continuity logs.
- Domain stability rule: core Character model should store identity/version/reference intent; embedding mechanisms remain provider/workflow implementation details.

### D-003: AI consistency metrics vs production continuity review

- AI layer emphasizes quantitative consistency/diversity/quality metrics.
- Production layer emphasizes cross-stage human review plus explicit issue tracking.
- Domain stability rule: QC should combine machine metrics and human review provenance.

### D-004: Generated storyboard panels vs storyboard lifecycle governance

- AI layer often frames storyboard as generation output and optimization target.
- Production layer frames storyboard as iterative planning/review lifecycle artifact.
- Domain stability rule: model storyboard as stateful planning process with generated panels as one artifact type within that lifecycle.

### D-005: Model-specific camera controls vs cinematography intent

- AI layer references provider-specific parameter/control spaces.
- Production layer emphasizes narrative camera intent (framing, focus, motion purpose).
- Domain stability rule: preserve provider-neutral intent schema and map to provider parameters through adapters.

## 4. Stable Domain Principles

- DP-001 Canonical Production Hierarchy: Preserve `Story -> Episode -> Scene -> Shot` as canonical production hierarchy.
- DP-002 Shot as Primary Production Unit: Treat Shot as primary execution and traceability unit.
- DP-003 Production Intent / Provider Separation: Keep domain intent independent from provider/workflow implementation.
- DP-004 Persistent Identity / Mutable Appearance Separation: Separate Character identity from mutable versions/appearance states.
- DP-005 Storyboard as Planning and Review: Model storyboard as lifecycle-managed planning/review stage.
- DP-006 Explicit Continuity State: Represent continuity as explicit, tracked, cross-stage state.
- DP-007 Versioned and Traceable Production Assets: Require version and provenance traceability across workflow and artifacts.
- DP-008 Multi-Stage Production Lifecycle: Model stage-gated iterative lifecycle with review/rework transitions.
- DP-009 Multi-Dimensional QC: Evaluate quality via multiple dimensions with explicit decision criteria.

## 5. Consolidated Candidate Requirements

### CR-001

- Candidate Requirement ID: CR-001
- Statement: Preserve Scene and Shot as distinct concepts inside canonical `Story -> Episode -> Scene -> Shot` hierarchy.
- Supporting Layer 1 evidence: Canonical hierarchy preservation and Shot-level architecture implications.
- Supporting Layer 3 evidence: Strong production finding for Scene/Shot distinction and hierarchy preservation.
- Affected future specification: Scene Specification; Shot Specification
- Status: CANDIDATE

### CR-002

- Candidate Requirement ID: CR-002
- Statement: Keep Shot as the primary production execution unit, while allowing auxiliary planning/generation artifacts (for example anchors/keyframes) without redefining canonical units.
- Supporting Layer 1 evidence: `REQ-PROD-001` and keyframe-not-replacement guidance.
- Supporting Layer 3 evidence: Principle A (Shot primary execution unit).
- Affected future specification: Shot Specification; Workflow Specification
- Status: CANDIDATE

### CR-003

- Candidate Requirement ID: CR-003
- Statement: Model Storyboard as first-class lifecycle state (draft/review/revision/approval) with feedback provenance.
- Supporting Layer 1 evidence: Storyboard planning-stage implications and `REQ-WF-BOARD-001`.
- Supporting Layer 3 evidence: Storyboard lifecycle candidate requirement and strong iterative-review evidence.
- Affected future specification: Storyboard Specification; Workflow Specification
- Status: CANDIDATE

### CR-004

- Candidate Requirement ID: CR-004
- Statement: Separate Character identity from CharacterVersion/appearance state and support multi-reference character context.
- Supporting Layer 1 evidence: `REQ-CHAR-001`, `REQ-CHAR-002`, identity/appearance separation principles.
- Supporting Layer 3 evidence: Candidate requirement for Character vs CharacterVersion separation and continuity-ready references.
- Affected future specification: Character Asset Specification
- Status: CANDIDATE

### CR-005

- Candidate Requirement ID: CR-005
- Statement: Keep production intent provider-neutral and map to provider-specific execution through adapters.
- Supporting Layer 1 evidence: Candidate ADRs on intent-conditioning separation and provider independence.
- Supporting Layer 3 evidence: Candidate ADR and principles on intent-vs-execution separation.
- Affected future specification: Shot Specification; Workflow Specification
- Status: CANDIDATE

### CR-006

- Candidate Requirement ID: CR-006
- Statement: Represent continuity explicitly with structured state/issues at shot transitions, including status and review provenance.
- Supporting Layer 1 evidence: `REQ-CONT-001`, `REQ-CONT-002` and continuity-as-production-state implications.
- Supporting Layer 3 evidence: Continuity candidate requirements for shot-transition issue tracking and review provenance.
- Affected future specification: Continuity Specification; Shot Specification
- Status: CANDIDATE

### CR-007

- Candidate Requirement ID: CR-007
- Statement: Support hierarchical, stage-based production and generation workflows with explicit review gates and rework loops.
- Supporting Layer 1 evidence: Hierarchical decomposition findings; workflow context/specialization candidates (`REQ-WF-001`, `REQ-WF-002`).
- Supporting Layer 3 evidence: Stage-gated pipeline candidate requirements and review-cycle evidence.
- Affected future specification: Workflow Specification
- Status: CANDIDATE

### CR-008

- Candidate Requirement ID: CR-008
- Statement: Preserve artifact/workflow provenance and version history sufficient for reproducibility and auditability.
- Supporting Layer 1 evidence: Workflow/context/QC traceability direction across requirements and principles.
- Supporting Layer 3 evidence: Candidate requirement for workflow/artifact provenance and versioned review records.
- Affected future specification: Artifact & Provenance Specification; Workflow Specification
- Status: CANDIDATE

### CR-009

- Candidate Requirement ID: CR-009
- Statement: Attach provider-neutral camera/spatial intent to Shot and translate to provider-specific parameters via adapters.
- Supporting Layer 1 evidence: `REQ-SHOT-002` provider-neutral spatial representation requirement.
- Supporting Layer 3 evidence: Cinematography candidate requirements and adapter-based mapping principle.
- Affected future specification: Shot Specification
- Status: CANDIDATE

### CR-010

- Candidate Requirement ID: CR-010
- Statement: Use multi-dimensional QC (identity, alignment, continuity, diversity/composition, technical quality) with explicit decision policy.
- Supporting Layer 1 evidence: `REQ-QC-001` and multi-objective storyboard/character QC findings.
- Supporting Layer 3 evidence: Production synthesis continuity/QC principles combining structured checks and review.
- Affected future specification: QC Specification; Storyboard Specification
- Status: CANDIDATE

## 6. Candidate ADR Review Queue

No ADR is accepted in this document.

### HIGH PRIORITY

- Preserve `Story -> Episode -> Scene -> Shot` as canonical hierarchy.
- Keep Shot as primary production unit while allowing auxiliary workflow artifacts.
- Separate production intent from provider-specific execution.
- Separate Character identity from mutable appearance/version state.
- Treat Storyboard as first-class planning/review stage.

### MEDIUM PRIORITY

- Treat Continuity as explicit tracked production state/service across stages.
- Adopt stage-gated workflow lifecycle with versioned review/provenance records.
- Define provider-neutral camera/spatial intent contracts with adapter translation.

### DEFER

- Formal policy for optional auxiliary terminology metadata (sequence/beat/setup/take) pending additional guild-standard evidence.
- Strict temporal/timecode domain schema standardization pending deeper standards-level research.

Technology candidates excluded from ADR queue by policy:
- PPR, RAVM, SigLIP, DINOv2, ControlNet, LoRA, AR visual tokens (and similar model techniques).

## 7. Open Domain Questions

Priority is based on impact to near-term domain specifications.

### Q1 (High): Character boundary model
- How should Character, CharacterVersion, Wardrobe, and appearance-state boundaries be partitioned?
- Should wardrobe/injury/hair live in CharacterVersion, Continuity state, or both via typed linkage?

### Q2 (High): CharacterReference modeling
- Should CharacterReference be a dedicated entity, a typed Artifact relation, or hybrid structure?

### Q3 (High): Storyboard minimum metadata
- What minimum storyboard fields are required before downstream shot generation can start?

### Q4 (High): Continuity machine-checkable core
- Which continuity constraints are machine-checkable in early milestones vs human-review-only?

### Q5 (High): Shot camera/spatial neutral schema
- What provider-neutral representation should encode camera intent and spatial relations?

### Q6 (Medium): Keyframe-to-Shot relationship
- Should keyframes/anchors be modeled as Shot-linked artifacts, workflow state, or dedicated planning entities?

### Q7 (Medium): Multi-character scene representation
- How should scenes with three or more characters be represented to reduce identity drift/entanglement risk?

### Q8 (Medium): QC metric aggregation policy
- How should multi-dimensional metrics be aggregated into review decisions without over-optimizing one dimension?

### Q9 (Medium): Stage-gate policy by project profile
- Which stage gates are mandatory vs optional for short-form, episodic, and feature-like profiles?

### Q10 (Defer): Cross-provider temporal alignment schema
- What minimum timecode/synchronization structure is needed for reproducible editorial alignment?

## 8. Specification Readiness Matrix

| Domain | Evidence Readiness | Blocking Questions | Recommended Next Action |
|---|---|---|---|
| Character | MEDIUM | Q1, Q2, Q7 | Draft Character identity/version/reference boundary options and decide minimum v1 schema. |
| Scene | MEDIUM | Q9 | Define Scene intent boundaries and links to Shot decomposition with minimal mandatory fields. |
| Shot | HIGH | Q5, Q6 | Draft Shot core schema with provider-neutral camera/spatial intent and auxiliary anchor linkage strategy. |
| Storyboard | HIGH | Q3 | Specify storyboard lifecycle states, required metadata, and review transitions. |
| Continuity | MEDIUM | Q4, Q10 | Define continuity record model with machine-checkable core plus human review fields. |
| Artifact | MEDIUM | Q2, Q10 | Define artifact typing, provenance minimum, and optional temporal alignment fields. |
| Workflow | HIGH | Q6, Q9 | Define stage-gated workflow state machine, revision history, and adapter boundaries. |
| QC | MEDIUM | Q8, Q4 | Define multi-dimensional metric registry and decision/approval policy. |

## 9. Recommended Specification Order

Based on evidence maturity and dependency flow, the smallest reasonable sequence is:

1. Shot Specification
2. Storyboard Specification
3. Character Asset Specification
4. Continuity Specification
5. Workflow Specification
6. Artifact & Provenance Specification
7. QC Specification
8. Scene Specification

Rationale:
- Shot + Storyboard have strongest cross-layer support and define planning/execution backbone.
- Character and Continuity define core consistency semantics needed by Workflow.
- Workflow then formalizes staged orchestration and review history.
- Artifact/Provenance and QC finalize traceability/decision systems across prior domains.
- Scene specification is intentionally last in this sequence to crystallize boundaries after Shot/Storyboard decomposition semantics are explicit.

## 10. Conclusion

Cross-layer synthesis indicates strong alignment between AI research direction and production-practice constraints, but:

research synthesis
is not equal to
accepted domain architecture.

Next governance step:
- domain specifications first
- ADRs only where architectural decisions are required
- no technology-candidate promotion without explicit review

Final validation checklist:
- Source syntheses modified: NO
- `DEVELOPMENT_SPEC.md` modified: NO
- Application code changed: NO
- ADR accepted: NO
- Technology candidate promoted: NO
- Duplicated candidate requirements consolidated: YES
- Git diff reviewed: YES
- Files changed in this task:
  - `docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md`
