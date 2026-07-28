# AGENTS.md

## Purpose

This repository uses documentation-driven, research-informed, incremental development.

Before making architectural, domain-level, or substantial implementation changes,
agents MUST read the relevant repository documentation.

The normal development process is:

Research / Evidence
→ Research Synthesis
→ Development Specification
→ ADR when required
→ Domain Specification
→ Small Pull Request
→ Tests
→ Review
→ Documentation Update
→ Next Specification

Do not attempt to implement the entire AI Drama System in one change.

Prefer the smallest coherent, reviewable increment.

---

## Source of Truth

The repository is the authoritative source of truth for the project.

Do not assume that ideas discussed in ChatGPT, Copilot, issues, comments,
or other conversations have been implemented or accepted unless the
repository records them.

Source code and tests are authoritative for current runtime behavior.

Accepted specifications and ADRs are authoritative for intended architecture.

Research documents provide evidence and rationale but do not automatically
define architecture.

If documentation and implementation conflict, identify the discrepancy
rather than silently choosing one.

---

## Decision Status Rules

Agents MUST distinguish between:

- Existing Implementation
- Existing Specification
- Accepted ADR
- Research Finding
- Research Principle
- Candidate Requirement
- Candidate ADR
- Proposed Design
- Technology Candidate
- Experimental Idea
- Future Roadmap

Never silently promote one status into another.

In particular:

Research Finding
!= Requirement

Candidate Requirement
!= Accepted Requirement

Candidate ADR
!= Accepted ADR

Technology Candidate
!= Selected Technology

A technique appearing in a research paper does not make that technique
part of the AI Drama System architecture.

---

## Required Reading Order

Before making significant changes, inspect the relevant repository
documentation approximately in this order:

1. `AGENTS.md`
2. `docs/DEVELOPMENT_SPEC.md`
3. Relevant accepted ADRs under `docs/adr/`
4. Relevant domain specifications under `docs/domain/`
5. Relevant architecture documentation under `docs/architecture/`
6. Relevant research synthesis under `docs/research/synthesis/`
7. Relevant individual research records under `docs/research/`
8. `docs/development/coding-standards.md`
9. `docs/development/testing.md`
10. `docs/ROADMAP.md`
11. `README.md`
12. Relevant source code and tests

This order is contextual rather than absolute.

Source code and tests must always be inspected when determining what
the current system actually does.

Research informs architecture but does not override an accepted
specification or ADR.

---

## Core Architectural Principles

The AI Drama System is:

- model-agnostic
- workflow-driven
- asset-centric
- shot-based
- reproducible
- traceable
- provider-independent where practical

These principles are architectural constraints, not suggestions,
unless deliberately changed through specification and ADR.

Prefer:

- loose coupling
- high cohesion
- explicit domain boundaries
- replaceable provider integrations
- deterministic orchestration around non-deterministic AI operations
- persistent generation state
- retryable generation jobs
- artifact provenance
- observable workflows
- human-reviewable production stages

Avoid premature abstraction and unnecessary complexity.

---

## Primary Production Hierarchy

The canonical production hierarchy is:

Project
→ Story
→ Episode
→ Scene
→ Shot

`Shot` is the primary production unit.

Do not introduce an alternative production hierarchy without an approved
architectural decision.

Provider-specific or research-specific concepts such as:

- keyframes
- latent panels
- model tokens
- embeddings
- attention maps
- workflow nodes
- conditioning formats

must not silently replace canonical production-domain concepts.

These concepts may support a Shot or generation workflow without redefining
the core production hierarchy.

---

## Research Rules

The formal Research Library lives under:

`docs/research/`

Research should normally follow:

Primary Source
→ Research Record
→ Cross-Source Synthesis
→ Research Principle
→ Candidate Requirement
→ Specification
→ ADR when required
→ Domain Model
→ Implementation

Prefer sources approximately in this order:

1. Primary research papers
2. Official technical documentation
3. Official standards and specifications
4. Official repositories
5. Authoritative film and animation production references
6. High-quality engineering references
7. Secondary commentary when primary sources are unavailable

Research supports architecture but does not automatically define it.

Important research conclusions that may influence architecture should be
recorded in the repository rather than left only in conversations.

---

## Research Interpretation Rules

Research records MUST distinguish where practical between:

### Research Finding

What a source actually demonstrates, proposes, evaluates, or documents.

### Research Interpretation

What that evidence may mean for AI Drama System.

### Research Principle

A stable higher-level principle supported by sufficient evidence.

### Candidate Requirement

A possible system requirement requiring specification review.

### Technology Candidate

A possible implementation technique that remains replaceable.

### Candidate ADR

A possible architectural decision that has not yet been accepted.

Do not convert paper-specific implementations directly into system requirements.

Examples of technology-specific concepts include:

- PPR
- RAVM
- Latent Panel Anchoring
- SigLIP
- DINOv2
- ArcFace
- CLIP
- ControlNet
- LoRA
- attention-mask regularization
- autoregressive visual tokens
- diffusion autoencoders

These remain Technology Candidates unless deliberately promoted through
architecture review.

---

## Architecture Rules

Business logic MUST NOT be placed directly in Django views.

Provider-specific AI logic MUST NOT be placed directly in:

- Django models
- serializers
- views
- domain entities

External AI integrations must be isolated behind provider, workflow,
or adapter interfaces.

Do not tightly couple the system to:

- ComfyUI
- OpenAI
- Anthropic
- Gemini
- FLUX
- Stable Diffusion
- Wan
- Kling
- Veo
- any other specific AI provider or model

Specific providers and models are implementations, not domain concepts.

---

## Production Intent Separation

Maintain a clear conceptual separation between:

Production Intent
→ Structured Domain Data
→ Generation Plan
→ Workflow / Provider Translation
→ Provider-Specific Prompt / Conditioning
→ Generated Artifact

Core production intent must remain independent from the implementation
details required by a particular generation provider.

Do not store provider-specific prompts, embeddings, model tokens,
workflow nodes, attention structures, or conditioning formats as core
domain concepts unless an accepted specification or ADR explicitly
requires it.

---

## Domain Modeling Rules

Treat domain concepts as first-class design elements.

Consider where appropriate:

- Entity
- Value Object
- Aggregate
- Domain Service
- Application Service
- Repository
- Domain Event

Do not force DDD patterns where they provide no practical value.

Domain terminology should remain consistent across:

- specifications
- ADRs
- code
- APIs
- prompts
- workflows
- UI

Use UUIDs for primary keys unless a specification explicitly says otherwise.

Human-readable codes such as:

`EP01_SC03_SH012`

must be separate fields and MUST NOT be database primary keys.

Ordered domain objects must use explicit ordering fields.

Do not depend on database insertion order.

Entities that materially affect generation reproducibility should support
explicit versioning where required by specification.

Examples may include:

- Character
- Location
- Style
- Prompt Template
- Workflow

Do not mutate historical generation inputs in ways that make previous
outputs impossible to trace.

---

## Shot Rules

Do not over-design the Shot model without an approved Shot specification.

The Shot model should evolve incrementally.

Do not add speculative fields merely because they may be useful later.

Every generated production artifact should eventually be traceable to
a Shot or another explicitly defined production context.

Research concepts such as storyboard panels or video keyframes may attach
to Shot-level workflows but must not redefine Shot without architectural review.

---

## Generation Rules

Generation follows the conceptual architecture:

Shot
→ PromptInstance
→ GenerationTask
→ GenerationAttempt
→ GenerationResult
→ Artifact

Changes to this conceptual chain require specification and, when
architecturally significant, an ADR.

Do not bypass the generation task system by calling AI providers directly
from views or templates.

All generated artifacts must retain provenance information sufficient
for debugging and reproduction.

Expected provenance may include:

- provider
- model
- workflow version
- prompt
- source assets
- parameters
- seed
- task identifier
- timestamps

Generation workflows should make failure states explicit.

AI calls should be retryable where practical without losing generation history.

---

## Asset Rules

Reusable creative elements must be modeled as assets where defined by
the domain specification.

Examples may include:

- Character
- Location
- Prop
- Style
- Voice

Asset identity must remain separate from asset versions when versioning
is required.

Do not silently replace an older asset version referenced by an existing
generation task.

Generated files are not automatically equivalent to production assets.

An Artifact represents a generated or imported output with provenance.
A reusable production Asset represents intentional production identity.

Do not confuse these concepts.

---

## Character and Continuity Rules

Research indicates that character consistency may extend beyond facial identity
to characteristics such as:

- hairstyle
- clothing
- body appearance
- visual identity
- contextual continuity

However, research findings do not automatically define the Character domain.

Do not finalize Character, CharacterVersion, wardrobe, reference-image,
identity-embedding, or continuity structures without the relevant
domain specification.

Provider-specific identity mechanisms must remain replaceable.

---

## Storyboard Rules

Storyboard is a production planning and review concern, not merely a
collection of generated images.

Storyboard architecture should remain distinct from:

- final image generation
- final video generation
- provider-specific latent representations

Research metrics such as character consistency, prompt alignment,
composition quality, or scene diversity may inform QC design but must
not automatically become accepted product requirements.

---

## Workflow Rules

Generation workflows must be configurable and versionable where required.

Do not hard-code ComfyUI workflow JSON or equivalent provider workflows
into domain models or views.

Workflow-specific parameter mappings belong in workflow/provider integration code.

The domain should describe production intent.

Workflow adapters should translate production intent into provider-specific
execution structures.

---

## Knowledge Rules

Knowledge DB content may include:

- story rules
- screenwriting rules
- storyboard rules
- cinematography rules
- camera rules
- prompt rules
- continuity rules
- QC rules

Do not implement embeddings, RAG, or vector search unless required by
the current specification.

Avoid premature infrastructure.

Research Library and Knowledge DB are separate concerns.

The Research Library stores evidence used to design the system.

The Knowledge DB is a runtime/product capability for supporting production
knowledge when defined by specification.

Do not treat research documents automatically as runtime Knowledge DB content.

---

## AI Production Concerns

Treat the following as distinct concerns where appropriate:

- Story / script
- Character / assets
- Scene / shot planning
- Storyboard
- Prompt construction
- Image generation
- Video generation
- Audio / voice
- Workflow orchestration
- Provider integration
- Continuity
- QC
- Artifact provenance
- Delivery

Do not design AI Drama System as merely a wrapper around generation APIs.

---

## Development Style

Prefer small, reviewable changes.

Each task should:

1. identify the relevant specification
2. inspect relevant research when required
3. identify affected domain boundaries
4. implement only the requested scope
5. add or update tests
6. inspect the resulting diff
7. update documentation when behavior or architecture changes

Do not perform unrelated refactors.

Do not add dependencies without a clear requirement.

Do not create placeholder abstractions that have no current use.

Prefer simple, explicit, maintainable code.

---

## Django Rules

Follow Django best practices and current project conventions.

Keep application boundaries clear.

Avoid circular dependencies between Django apps.

Use services for application/business operations when appropriate.

Models should primarily represent domain state and invariants.

Views should coordinate HTTP behavior rather than contain business workflows.

Serializers should not become a substitute for application services.

Do not make framework convenience more important than domain boundaries.

---

## Configuration and Secrets

Use environment variables or an approved secrets-management mechanism
for configuration and secrets.

Never commit:

- API keys
- access tokens
- passwords
- cloud credentials
- private certificates

Local development must not require external AI providers unless the
active milestone explicitly requires them.

---

## Testing

Every implemented behavior must have appropriate tests.

Use where appropriate:

- unit tests
- model tests
- service tests
- API tests
- integration tests

External AI providers should be mocked or replaced with test adapters
unless the test is specifically an integration test.

Tests should verify domain behavior rather than provider implementation
details whenever possible.

A task is not complete when implementation works manually but tests fail.

---

## Documentation Rules

Architecture decisions with long-term impact should be documented using ADRs.

Use:

`docs/adr/ADR-XXXX-description.md`

Do not rewrite historical ADRs to pretend a previous decision never existed.

If a decision changes:

1. create a new ADR
2. mark the previous ADR as superseded where appropriate

Domain behavior belongs under:

`docs/domain/`

System-level architecture belongs under:

`docs/architecture/`

Research evidence belongs under:

`docs/research/`

Implementation and contributor rules belong under:

`docs/development/`

Research synthesis must not be presented as an accepted ADR unless the
decision has gone through architecture review.

---

## Agent / Copilot Working Rules

Repository-local coding agents should primarily perform:

- documentation updates
- implementation
- tests
- refactoring
- small PR execution

Architecture and research tasks may use agents for mechanical work, but
agents must not silently make architectural decisions.

For substantial tasks, agents MUST first inspect committed repository
instructions and relevant specifications.

Do not implement architecture based only on chat context.

Do not assume a proposed design has been accepted unless repository
documentation records that decision.

When using research:

1. identify the source
2. distinguish source fact from interpretation
3. identify whether the conclusion is already accepted
4. preserve Technology Candidate status where appropriate

Before completing a repository task:

1. inspect the diff
2. verify scope
3. run relevant tests or validation
4. confirm no unrelated changes
5. report files created or modified
6. report documentation impact

---

## Change Discipline

Before implementing a major new feature, determine whether the current
documentation defines it.

If not, prefer:

Research when required
→ Specification
→ Review
→ ADR when required
→ Implementation

rather than inventing architecture inside the code.

When requirements are ambiguous, preserve existing architectural boundaries
and implement the smallest reasonable change.

Do not redesign unrelated parts of the system while implementing a
localized requirement.

---

## Conflict Handling

When sources conflict:

### Implementation vs Specification

Identify the discrepancy.

Do not silently rewrite one to match the other.

### Specification vs ADR

Inspect ADR status and chronology.

Accepted architecture decisions must be deliberately superseded.

### Research vs Accepted ADR

The accepted ADR governs current architecture until deliberately revisited.

New research may justify reviewing the ADR but does not silently override it.

### Current Official Documentation vs Old Research Record

Flag potential version drift and update the research record when appropriate.

### Chat Discussion vs Repository

The repository is authoritative unless the repository is intentionally
being revised as part of the current task.

---

## Definition of Done

A change is complete only when:

- the requested behavior or documentation change is complete
- the requested scope is respected
- relevant tests or validation pass
- migrations are valid when applicable
- no architectural rule is violated
- documentation is updated when required
- research status is represented correctly when applicable
- no Candidate ADR is presented as accepted
- no Technology Candidate is presented as selected without a decision
- no secrets are committed
- unrelated functionality is not changed
- the final diff has been reviewed

---

## Long-Term Goal

Build a maintainable and extensible AI-native production system capable
of turning structured creative concepts into reusable production assets
and eventually complete AI-generated drama/video content.

New models, providers, workflows, asset types, QC methods, and production
stages should be addable without major rewrites of the core domain.

---

## Core Rule

Do not confuse:

- research with decisions
- candidate requirements with accepted requirements
- technology candidates with selected technologies
- providers with domain concepts
- prompts with production intent
- generated files with production assets
- research representations with runtime domain models
- conversation history with repository truth