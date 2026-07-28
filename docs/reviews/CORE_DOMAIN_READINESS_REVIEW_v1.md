# Core Domain Readiness Review v1.0

## Review Metadata

- Review Type: Cross-domain architecture readiness review
- Review Date: 2026-07-28
- Review Scope:
  - docs/domain/scene.md
  - docs/domain/shot.md
  - docs/domain/storyboard.md
  - docs/domain/character.md
  - docs/domain/continuity.md
  - docs/domain/workflow.md
  - docs/domain/artifact.md
  - docs/domain/qc.md
- Supporting Context:
  - AGENTS.md
  - docs/DEVELOPMENT_SPEC.md
  - docs/adr/ADR-0001-generation-attempt-retry-semantics.md
  - docs/adr/ADR-0002-idempotency-contract.md
  - docs/research/synthesis/AI_DRAMA_DOMAIN_FOUNDATION_SYNTHESIS_v1.md
  - docs/research/synthesis/WORKFLOW_ARCHITECTURE_SYNTHESIS_v1.md
  - docs/research/synthesis/STANDARDS_ARCHITECTURE_SYNTHESIS_v1.md
  - docs/research/synthesis/PRODUCTION_KNOWLEDGE_SYNTHESIS_v1.md
- Review Discipline:
  - No redesign performed
  - No code written
  - No domain specification modified
  - Proposed ADRs treated as Proposed only
  - Research findings not treated as accepted architecture unless draft specs
    explicitly scoped them as draft-local decisions

## Executive Summary

Current core domain specifications are broadly coherent and preserve the
repository's primary architectural constraints:

- canonical hierarchy remains intact,
- Shot remains the primary production unit,
- provider-specific concepts are consistently kept out of core ontology,
- provenance and historical traceability are treated as first-class concerns,
- Storyboard, Continuity, Workflow, Artifact, and QC are distinct domains with
  mostly explicit boundaries.

No direct cross-domain definition conflict was found that would require
rewriting existing domain specifications.

However, the current set is not fully implementation-ready for a
generation-integrated first slice because one critical ownership gap remains:
GenerationTask, GenerationAttempt, and especially GenerationResult are used by
multiple domain specifications but are not yet governed by a dedicated domain
specification or equivalent authoritative cross-domain contract.

Issue counts in this review:

- BLOCKER: 1
- HIGH: 3
- MEDIUM: 5
- LOW: 0

Overall determination:

- Planning-layer implementation is ready in a narrow slice.
- Generation-integrated implementation is not yet ready.
- Workflow implementation is ADR-blocked where it depends on ADR-0001 and
  ADR-0002 acceptance.

## Canonical Hierarchy Assessment

Canonical hierarchy under review:

Project
-> Story
-> Episode
-> Scene
-> Shot

Assessment:

- Scene and Shot are consistently treated as distinct concepts.
- Shot remains the primary production unit across Scene, Shot, Storyboard,
  Workflow, Artifact, and QC specifications.
- Storyboard does not replace Shot; panels remain planning representations.
- Keyframes/anchors are consistently treated as auxiliary planning/generation
  aids and do not become hierarchy levels.
- No reviewed domain behaves as an undeclared canonical hierarchy replacement.

Findings:

- Scene -> Shot containment is consistently stated.
- Shot ordering ownership is consistently placed at Scene containment context.
- No hierarchy violation was found in current domain drafts.
- Project, Story, and Episode semantics are assumed from DEVELOPMENT_SPEC but do
  not yet have peer domain specifications in the reviewed set.

Assessment result:

- Canonical hierarchy consistency: CLEAR
- Canonical hierarchy completeness for implementation: PARTIAL

## Domain Ownership Matrix

| Domain | Owns | Explicitly Does Not Own | Assessment |
|---|---|---|---|
| Scene | Shared narrative and production context above Shot; Scene -> Shot containment; scene-level revision/provenance | Shot-local execution detail; continuity truth; workflow semantics; artifact identity | CLEAR |
| Shot | Primary production intent/execution context; shot-local action, framing, spatial and cinematography intent; shot-linked provenance | Scene-wide narrative truth; provider payloads; artifact payloads | CLEAR |
| Storyboard | Planning/review lifecycle; panel ordering; feedback and approval history | Shot identity; provider runtime; final artifact truth | CLEAR |
| Character | Persistent identity; CharacterVersion baseline; reference semantics | provider identity representations; transient shot state; continuity-moment truth | PARTIAL |
| Continuity | Expected/observed continuity state; transitions; discrepancy; issue; review; resolution | Character identity; full shot-local state; provider continuity payloads | CLEAR |
| Workflow | WorkflowDefinition/Version/Run; stage/step/gate/rework semantics | provider runtime; queue semantics; artifact payloads | PARTIAL |
| Artifact | Durable artifact identity; lineage; derivation; provenance linkage; representation boundary | storage backend truth; provider runtime; asset identity | PARTIAL |
| QC | quality policy/criterion/evaluation/finding/issue/decision semantics; review linkage | workflow gate execution; continuity truth; artifact identity | PARTIAL |

Ownership review conclusions:

- Scene vs Shot: clear separation, no conflict.
- Scene vs Continuity: clear separation, but inheritance-to-continuity handoff
  contract is still partial.
- Shot vs Storyboard Panel: clear separation, no conflict.
- CharacterVersion vs Continuity state: not conflicting, but boundary remains
  partially unresolved for wardrobe and other persistent-versus-transient
  appearance changes.
- Artifact vs Asset: clear conceptual separation, but generic Asset domain
  outside Character is not yet specified.
- Artifact vs GenerationResult: Artifact boundary is explicit, but GenerationResult
  ownership is missing outside scattered references.
- Workflow vs GenerationTask: boundary is stated, but generation-side ownership
  remains incomplete.
- Workflow review gate vs QC Decision: explicit separation is present.
- Continuity Issue vs QC Issue: conceptually separable, but escalation/handoff
  contract is missing.
- Storyboard approval vs Workflow approval: distinct in meaning, but integration
  contract remains partial.

## Identity Boundary Matrix

| Identity | Current Owning Source | Stability | Notes |
|---|---|---|---|
| Scene identity | Scene spec | STABLE | Stable scene identity is explicit; revision identity is partial. |
| Shot identity | Shot spec | STABLE | Stable machine identity explicitly required. |
| Storyboard identity | Storyboard spec | STABLE | Stable storyboard identity explicit. |
| StoryboardPanel identity | Storyboard spec | STABLE | Stable panel identity explicit and distinct from artifacts. |
| Character identity | Character spec | STABLE | Persistent identity explicit. |
| CharacterVersion identity | Character spec | PARTIAL | Durable version identity explicit; scope boundaries unresolved. |
| CharacterReference identity | Character spec | PARTIAL | Stable reference identity implied; modeling shape still open. |
| Continuity context identity | Continuity spec | STABLE | Stable continuity context anchor explicit. |
| Continuity issue identity | Continuity spec | STABLE | Stable issue identity explicit in conceptual model. |
| WorkflowDefinition identity | Workflow spec | STABLE | Explicit stable identity. |
| WorkflowVersion identity | Workflow spec | STABLE | Explicit immutable version identity. |
| WorkflowRun identity | Workflow spec | STABLE | Explicit run identity. |
| WorkflowStep identity | Workflow spec | PARTIAL | Conceptual only; no stronger contract yet. |
| GenerationTask identity | Workflow spec + ADR-0001 | PARTIAL | Stable concept exists, but no dedicated generation specification. |
| GenerationAttempt identity | Proposed ADR-0001 + Workflow draft wording | PARTIAL | Semantics are only Proposed ADR direction, not accepted architecture. |
| GenerationResult identity | Cross-domain references only | AMBIGUOUS | No authoritative domain owner/specification in current set. |
| Artifact identity | Artifact spec | STABLE | Durable identity distinct from storage/runtime identifiers. |
| ArtifactVersion identity | Artifact spec | PARTIAL | Candidate-level version identity exists; policy boundary unresolved. |
| QC policy identity | QC spec | PARTIAL | Conceptually stable, but policy versioning strategy remains open. |
| QC evaluation identity | QC spec | STABLE | Immutable historical evaluation identity explicit. |
| QC issue identity | QC spec | PARTIAL | Semantics clear; cross-domain issue integration unresolved. |

Identity review conclusion:

- Most domain identities are coherently separated.
- The largest identity ambiguity is GenerationResult ownership.
- The most important candidate-level identities still needing architecture
  closure are GenerationAttempt, ArtifactVersion, CharacterVersion, and
  scene-level revision identity.

## Versioning / Revision Matrix

| Domain | Classification | Review |
|---|---|---|
| Scene | Partial | Historical revision trace required; no full SceneVersion decision. |
| Shot | Partial | Traceability required; full entity versioning intentionally deferred. |
| Storyboard | Stable | Revision history and approval lineage are well defined conceptually. |
| Character | Partial | CharacterVersion is defined, but final boundary and wardrobe partition remain open. |
| Continuity | Partial | History and issue lineage are defined; explicit version entity not required. |
| Workflow | Stable for Definition/Version/Run, Partial overall | WorkflowDefinition/Version/Run boundaries are clear; stage/state strictness remains open. |
| Artifact | Partial | Artifact versus ArtifactVersion distinction is useful but still policy-level open. |
| QC | Partial | Historical evaluation immutability is strong; policy/evaluator versioning contract remains incomplete. |

Versioning review conclusions:

- Storyboard is the strongest revisioned domain in the current set.
- Workflow is strong where it covers WorkflowDefinition/Version/Run.
- Historical reproducibility before implementation most clearly requires:
  - WorkflowVersion stability
  - Storyboard revision history
  - CharacterVersion traceability
  - Artifact lineage and version traceability
  - QC evaluation immutability
  - Continuity issue/review history
- Full entity versioning is not uniformly required before first implementation.

## Cross-Domain Relationship Matrix

| Relationship | Status | Notes |
|---|---|---|
| Episode -> Scene | PARTIAL | Scene spec defines parent_episode_ref and ordering, but Episode spec is absent. |
| Scene -> Shot | CLEAR | Containment and ordering are explicit. |
| Scene -> Character | CLEAR | Reference-oriented; no identity duplication. |
| Scene -> Asset | PARTIAL | Reference-oriented, but generic asset contract is not yet specified. |
| Scene -> Continuity | PARTIAL | Scene frames span/context; continuity ownership clear; handoff detail open. |
| Scene -> Storyboard | CLEAR | Scene distinct from storyboard lifecycle; linkage explicit. |
| Shot -> Storyboard Panel | PARTIAL | One primary panel-to-shot direction preferred; broader cardinality remains open. |
| Shot -> Continuity | CLEAR | Shot owns local state, continuity owns cross-shot temporal state. |
| Shot -> Generation | PARTIAL | Chain is clear, but generation domain itself is not specified. |
| Workflow -> GenerationTask | PARTIAL | Workflow boundary explicit; task ownership incomplete without generation spec. |
| GenerationResult -> Artifact | PARTIAL | Relationship direction is explicit; GenerationResult ownership is missing. |
| Artifact -> ArtifactVersion | PARTIAL | Conceptual distinction exists; transformation policy unresolved. |
| ArtifactVersion -> QC Evaluation | PARTIAL | Strong direction, not yet universal rule. |
| QC Decision -> Workflow Gate | CLEAR | Explicitly separated; workflow consumes QC evidence under policy. |
| Continuity -> QC | PARTIAL | QC can evaluate continuity expectations, but issue handoff remains unspecified. |
| CharacterVersion -> Shot/Scene context | PARTIAL | Allowed by reference, but wardrobe/transient-state boundary unresolved. |

## Cardinality Assessment

Stable or near-stable cardinalities:

- Episode -> Scene:
  - ordered one-to-many implied, but Episode spec absent
  - Assessment: PARTIAL
- Scene -> Shot:
  - one Scene contains one or many Shots; each Shot belongs to one Scene
  - Assessment: CLEAR
- Shot -> Storyboard Panel:
  - zero/one/many panels per Shot explicitly allowed
  - Assessment: CLEAR
- Storyboard -> Shot:
  - storyboard may represent one or more Shots depending on scope
  - Assessment: PARTIAL
- Character -> CharacterVersion:
  - one Character may have multiple CharacterVersions implied
  - Assessment: PARTIAL
- Artifact -> ArtifactVersion:
  - one Artifact may have one or more versions as candidate model
  - Assessment: PARTIAL
- ArtifactVersion -> QC Evaluation:
  - one version may have many evaluations implied
  - Assessment: PARTIAL
- WorkflowDefinition -> WorkflowVersion:
  - one definition to many versions
  - Assessment: CLEAR
- WorkflowVersion -> WorkflowRun:
  - one version to many runs
  - Assessment: CLEAR

Cardinality conclusions:

- No explicit cardinality contradiction was found.
- Most unresolved cardinalities are intentionally deferred rather than hidden.
- The most implementation-sensitive unresolved cardinalities are:
  - Storyboard <-> Shot planning scope patterns
  - Character -> CharacterVersion details
  - Artifact -> ArtifactVersion policy
  - QC targeting at version/representation level

## Continuity Boundary Assessment

Continuity domain currently owns, with good clarity:

- expected state,
- observed state,
- transition,
- discrepancy,
- issue,
- resolution.

Boundary review:

- Continuity does not become a duplicate state store for Character identity.
- Continuity does not replace Scene context, though it may use scene-span scope.
- Continuity does not replace Shot local performance state.
- Continuity does not replace Artifact identity.
- Continuity does not replace Workflow semantics.

Main gap:

- QC can raise continuity-related findings or issues, but the repository does
  not yet define whether and how a QC continuity finding becomes, links to, or
  remains distinct from a ContinuityIssue.

Assessment:

- Continuity ownership model: CLEAR
- Continuity-to-QC integration contract: PARTIAL

## Workflow Boundary Assessment

Stable specification-level workflow semantics:

- WorkflowDefinition, WorkflowVersion, WorkflowRun, stage/step/gate/rework
  semantics are clearly scoped to Workflow.
- WorkflowRun is distinct from infrastructure runtime state.
- Review/rework is business governance, not technical retry.

Proposed ADR direction only:

- GenerationAttempt identity and retry semantics from ADR-0001 remain Proposed.
- Idempotency boundary from ADR-0002 remains Proposed.
- workflow.md reflects both as Proposed ADR direction rather than accepted
  architecture.

Boundary conclusions:

- No accidental promotion of ADR-0001 or ADR-0002 to accepted architecture was
  found.
- Workflow spec is internally disciplined about the status split.
- Workflow still lacks a dedicated peer Generation specification defining
  GenerationTask / GenerationAttempt / GenerationResult ownership outside
  Workflow-facing references.

Assessment:

- Workflow domain semantics: CLEAR
- Workflow-generation contract completeness: BLOCKED
- Workflow implementation readiness for generation-integrated work: ADR BLOCKED

## Artifact / Provenance Assessment

Confirmed separations:

- Artifact != Asset
- Artifact != GenerationResult
- Artifact != storage object
- internal provenance != external authenticity
- provenance != telemetry

Strengths:

- artifact identity/storage split is strong,
- lineage/derivation is explicitly preserved,
- provenance outliving telemetry retention is explicit,
- external standards remain candidates only.

Main gaps:

- ArtifactVersion semantics are useful but still policy-level partial,
- generic asset domain outside Character is not yet specified,
- cross-domain generation provenance depends on missing GenerationResult owner.

Assessment:

- Artifact identity/provenance boundary: CLEAR
- ArtifactVersion policy: PARTIAL
- Reproducibility linkage completeness: PARTIAL

## QC Boundary Assessment

Confirmed separations:

- QC Policy != QC Criterion != QC Metric/Evaluator
- QC Evaluation != QC Decision
- QC Decision != Workflow Gate
- QC Finding != QC Issue
- Human Review != Automated Score

Strengths:

- QC domain is semantically well separated from workflow and evaluators,
- multi-dimensional QC is consistently preserved,
- historical QC evaluations are immutable and traceable,
- concrete artifact QC usually attaching to ArtifactVersion is stated carefully
  as direction, not accepted absolute rule.

Main gaps:

- QC target model is heterogeneous and not fully normalized,
- continuity-related QC issue handoff is undefined,
- hard-fail versus soft-score semantics remain open,
- ArtifactVersion/Representation targeting policy is not yet final.

Assessment:

- QC conceptual boundary: CLEAR
- QC target contract: PARTIAL
- QC implementation readiness for artifact-heavy media review: PARTIAL

## Terminology Consistency

Consistent across reviewed specifications:

- Scene and Shot remain separate.
- Shot remains the canonical production unit.
- Storyboard Panel is a planning representation, not a Shot or Artifact.
- Character identity is distinct from mutable appearance.
- Continuity is explicit state, not prompt memory.
- Workflow stage/gate semantics are distinct from QC and domain object identity.
- Artifact provenance and telemetry remain distinct.

Partially inconsistent or still loose:

- version, revision, supersession, and approval are consistently separated at a
  high level, but not normalized identically across all domains,
- scene-wide shared context versus continuity scene-span state is conceptually
  separated, but terminology may still require tighter implementation contract,
- generic Asset terminology is relied on broadly without a dedicated Asset spec.

Assessment:

- Terminology consistency overall: GOOD
- Terminology normalization completeness: PARTIAL

## Research-to-Architecture Status Audit

Audit result:

- No direct case was found where a research finding was silently treated as
  accepted architecture.
- No direct case was found where ADR-0001 or ADR-0002 Proposed decisions were
  silently treated as Accepted.
- Multiple specs explicitly preserve the progression:
  Research -> Proposed ADR -> Accepted ADR -> Implementation.
- Draft-local acceptance language such as ACCEPT INTO DRAFT SPEC is usually
  scoped clearly enough to avoid accidental repository-wide promotion.

Caution areas to monitor later:

- Workflow spec depends on Proposed ADR directions for attempt/idempotency.
- QC and Artifact drafts depend on candidate-level ArtifactVersion policy.
- Character draft depends on candidate-level CharacterVersion/Wardrobe policy.

Assessment:

- Accidental promotion found: none
- Status discipline quality: strong

## Conflicts Found

No direct contradictory domain-definition conflict was found.

No reviewed specification redefines:

- Shot as anything other than primary production unit,
- Storyboard Panel as a canonical hierarchy element,
- Continuity as Character identity,
- Workflow gate as QC decision,
- Artifact as GenerationResult or storage object.

Review conclusion for this section:

- Direct semantic conflicts: none found
- Primary problems are contract gaps and ambiguity, not contradictory ownership

## Ambiguities Found

1. HIGH | OWNERSHIP AMBIGUITY / ADR REQUIRED
- CharacterVersion versus Continuity transient state boundary remains only
  partially resolved, especially for wardrobe and similar appearance changes.

2. HIGH | VERSIONING GAP
- Artifact versus ArtifactVersion boundary is conceptually useful but not yet
  policy-stable enough for broad media transformation handling.

3. MEDIUM | CONTRACT GAP
- Scene-to-Shot inheritance/override semantics are directionally clear but not
  fully normalized for implementation.

4. MEDIUM | CARDINALITY AMBIGUITY
- Storyboard and Shot cardinality patterns remain intentionally open beyond the
  preferred primary panel-to-shot direction.

5. MEDIUM | CONTRACT GAP
- ContinuityIssue and QC Issue linkage/escalation semantics are not yet defined.

6. MEDIUM | CONTRACT GAP
- Storyboard approval, QC decision, and Workflow gate interplay is only
  partially specified.

7. MEDIUM | CONTRACT GAP
- Project, Story, and Episode remain hierarchy anchors from DEVELOPMENT_SPEC,
  but only Scene and Shot are currently specified in the hierarchy-focused set.

## Missing Contracts

1. BLOCKER | CONTRACT GAP
- No dedicated Generation domain specification currently owns GenerationTask,
  GenerationAttempt, and GenerationResult semantics across Workflow, Artifact,
  Shot, and QC.
- Why it matters:
  - workflow references these concepts,
  - artifact provenance depends on them,
  - QC references GenerationResult as a target,
  - ADR-0001/0002 only partially cover attempt/idempotency semantics.

2. HIGH | CONTRACT GAP
- Generic Asset domain contract is missing for non-character reusable assets
  such as Location, Prop, Style, and Voice, despite multiple domains referencing
  them.

3. MEDIUM | CONTRACT GAP
- Continuity-to-QC escalation contract is missing.

4. MEDIUM | CONTRACT GAP
- Storyboard approval to Workflow gate consumption contract is missing.

5. MEDIUM | CONTRACT GAP
- Scene shared-context inheritance resolution rules are missing.

## ADR Candidates

Likely ADR-required topics emerging from cross-domain review:

1. Generation domain ownership and minimum contract boundary for GenerationTask,
   GenerationAttempt, and GenerationResult.
2. CharacterVersion versus Continuity transient-state partition, especially for
   wardrobe and similar durable/transient appearance boundaries.
3. Artifact versus ArtifactVersion transformation policy.
4. Scene-to-Shot inheritance/override policy.
5. QC hard-fail versus soft-score semantics and ArtifactVersion versus
   Representation targeting policy.

Status note:

- This section identifies likely ADR topics only.
- No ADR is created or accepted by this review.

## Research Gaps

Blocking research gaps:

- none identified for the current review scope.

Non-blocking research gaps:

- deeper guild/production terminology references for setup/take/insert/cutaway,
- future production-tracking references for scene revision/versioning patterns,
- future evaluator benchmarking or threshold-calibration research for QC,
- future standards-depth work for editorial/time-base interoperability.

Review determination:

- Most current obstacles are specification/contract gaps, not missing research.

## Implementation Readiness Matrix

| Domain | Classification | Basis |
|---|---|---|
| Scene | READY WITH MINOR OPEN QUESTIONS | Coherent boundaries, explicit Scene -> Shot ordering, no immediate ADR blocker. |
| Shot | READY WITH MINOR OPEN QUESTIONS | Strong core semantics; camera schema and anchor policy remain open but non-blocking for narrow implementation. |
| Storyboard | READY WITH MINOR OPEN QUESTIONS | Clear planning/review ownership; panel-shot cardinality and gating policy remain open. |
| Character | READY WITH MINOR OPEN QUESTIONS | Stable identity core is strong; CharacterVersion/Wardrobe/Reference architecture still open. |
| Continuity | READY WITH MINOR OPEN QUESTIONS | Clear ownership of state/transition/discrepancy/issue/resolution; machine-checkable scope remains open. |
| Workflow | ADR BLOCKED | Core workflow semantics are good, but generation-attempt and idempotency boundaries remain Proposed ADR direction and generation contract is incomplete. |
| Artifact | READY WITH MINOR OPEN QUESTIONS | Strong identity/provenance boundary; ArtifactVersion policy remains partial. |
| QC | READY WITH MINOR OPEN QUESTIONS | Strong separation and immutability semantics; target normalization and ArtifactVersion policy remain partial. |

## Blocking Issues

1. BLOCKER | CONTRACT GAP
- Missing Generation domain contract/specification.
- Prevents a coherent first generation-integrated implementation across
  Workflow, Artifact, and QC because the system lacks one authoritative owner of
  GenerationTask / GenerationAttempt / GenerationResult semantics.
- Must resolve before first generation-linked domain implementation.

## Non-Blocking Issues

1. HIGH | CONTRACT GAP
- Missing generic Asset domain contract for Location/Prop/Style/Voice.
- Must resolve before asset-heavy feature implementation.

2. HIGH | OWNERSHIP AMBIGUITY / ADR REQUIRED
- CharacterVersion versus Continuity state boundary remains open.
- Must resolve before full character-continuity implementation.

3. HIGH | VERSIONING GAP
- Artifact versus ArtifactVersion policy remains partial.
- Must resolve before revision-heavy artifact processing and QC-on-media history.

4. MEDIUM | CONTRACT GAP
- Scene-to-Shot inheritance/override contract is incomplete.
- Safe to defer for first planning slice if overrides are excluded.

5. MEDIUM | CARDINALITY AMBIGUITY
- Storyboard <-> Shot cardinality beyond primary-shot-per-panel direction
  remains open.
- Safe to defer if one primary shot per panel is used as convention.

6. MEDIUM | CONTRACT GAP
- ContinuityIssue versus QC Issue handoff remains unspecified.
- Must resolve before continuity-heavy QC automation.

7. MEDIUM | CONTRACT GAP
- Storyboard approval / QC decision / Workflow gate integration contract remains
  partial.
- Must resolve before policy-driven gated workflow rollout.

8. MEDIUM | CONTRACT GAP
- Project/Story/Episode domain specifications are absent from the reviewed core
  set.
- Safe to defer if early slices use opaque parent references.

## Recommended Resolution Order

1. Define authoritative Generation domain ownership contract or specification.
2. Define minimal generic Asset domain contract for non-character reusable
   assets.
3. Resolve CharacterVersion versus Continuity transient-state boundary.
4. Resolve Artifact versus ArtifactVersion policy.
5. Resolve Scene-to-Shot inheritance/override policy.
6. Resolve QC-to-Continuity and Storyboard/QC-to-Workflow gate handoff
   contracts.
7. Add Project/Story/Episode domain specifications if broader hierarchy
   implementation is needed.

## Smallest Safe Implementation Slice

Recommended slice:

- Scene
- Shot
- Storyboard
- StoryboardPanel
- ordering and revision/provenance links among those concepts

Explicitly excluded:

- Workflow execution semantics
- GenerationTask / GenerationAttempt / GenerationResult
- Artifact and ArtifactVersion implementation
- QC evaluation and issue workflows
- Continuity state machine or issue workflows
- CharacterVersion / Wardrobe boundary enforcement
- generic Asset modeling beyond opaque references

Prerequisite ADR/spec decisions:

- none beyond existing draft specifications
- no acceptance of ADR-0001 or ADR-0002 required for this slice

Why this slice is safe:

- hierarchy and ownership are coherent,
- Shot remains the primary production unit,
- planning-layer semantics do not depend on unresolved generation contracts,
- storyboard and scene/shot ordering/revision boundaries are already strong
  enough for incremental implementation,
- it avoids the current Generation domain blocker.

What later work it enables:

- continuity integration at shot transitions,
- QC on storyboard planning outputs,
- workflow input-context assembly,
- later artifact and generation provenance linkage.

## Final Readiness Determination

The current core domain drafts form a coherent conceptual foundation, but they
are not yet fully implementation-ready as one integrated generation-capable
core.

Final determination:

- Core domain coherence: YES
- Domain foundation suitable for narrow first implementation slice: YES
- Fully generation-integrated implementation-ready foundation: NO
- Primary blocking cause:
  - missing Generation domain ownership contract/specification
- Shot remains the primary production unit: YES
- Research-unblocked for downstream domain modeling overall: YES
- Main remaining work is specification/ADR closure, not broad new research
