# AI Drama System Research Library

This directory archives research evidence used to inform architecture discussions for the AI Drama System.

## Purpose

The Research Library preserves traceable links between primary research sources, internal research interpretation, and architecture governance.

The Research Library exists to provide evidence for designing and evolving the
AI Drama System as an AI-native narrative production and orchestration system.

Research papers do not directly define the AI Drama System architecture.

Paper-specific model implementations remain replaceable technology candidates unless promoted through architecture review.

Research is not an end in itself.

The quantity of research documents is not a project objective.

Research effort should be proportional to likely production-system impact.

## Reuse-First Direction

AI Drama System should normally integrate and orchestrate existing AI
capabilities before building custom AI infrastructure.

Typical execution mechanisms include provider APIs, open-source workflows,
ComfyUI ecosystems, local models, and other replaceable adapters.

These mechanisms are typically Technology Candidates, provider
implementations, workflow components, or adapter dependencies.

They are not core domain concepts unless accepted through specification and
architecture review.

This direction does not prohibit future custom/local models when a concrete
product or system requirement justifies them.

## Research Priority Model

### A. Production-System Research (High Priority)

Research is high priority when it can materially influence architecture, domain
modeling, production workflows, provider integration, production intent,
continuity, QC, provenance, reproducibility, human review, or production
automation.

Examples include story/episode/scene/shot decomposition, storyboard workflows,
asset/character continuity, prompt construction, provider abstraction,
workflow orchestration/versioning, generation retries/failure handling,
artifact traceability, QC, editorial assembly, audio/TTS/subtitle integration.

### B. Supporting Technical Background (Useful)

Research that helps explain provider capabilities and limitations, without
directly defining architecture, remains useful as supporting background.

### C. Model-Internal Research (Normally Lower Priority)

Research focused on foundation-model internals or large-scale model training is
normally lower priority unless tied to a concrete production-system question.

It is not forbidden, but should not become an ongoing track solely because it
is technically interesting.

## Research Entry Gate

Before beginning substantial research, ask:

Could this result materially affect AI Drama System architecture, domain
modeling, workflow design, provider selection/integration, production intent,
continuity, QC, provenance, reproducibility, or another concrete
production-system requirement?

- If yes: research may proceed.
- If no: keep effort small or skip substantial effort.
- If uncertain: prefer a short exploratory note before a large research track.

This is a prioritization rule, not a heavy approval process.

## Research Exit / Promotion Rule

When evidence is sufficient to support a production-system conclusion, move
toward:

```text
Research Finding
    ↓
Cross-Source Synthesis
    ↓
Research Principle
    ↓
Candidate Requirement
    ↓
Specification
    ↓
ADR (when required)
    ↓
Domain Model / Architecture
    ↓
Small Implementation Increment
```

Do not continue collecting sources only to increase source count once the
relevant system question is sufficiently answered.

Additional research should have a concrete reason such as conflict resolution,
specification gap closure, technology candidate evaluation, provider limitation
analysis, ADR question support, or production requirement validation.

## Research Library and Runtime Knowledge

Research Library and runtime/product knowledge are distinct concerns.

```text
Research Library
    = evidence used to design the system

Runtime Knowledge DB
    = runtime/product capability used during production
```

Research documents do not automatically become runtime RAG context,
embeddings, vector-index records, or production prompt context.

## Evidence Flow

```text
Primary Source
    ↓
Research Record
    ↓
Cross-Source Synthesis
    ↓
Research Principle
    ↓
Candidate Requirement
    ↓
Architecture Review
    ↓
ADR / Specification
    ↓
Implementation
```

## Library Index

| ID | Source | Category | Primary Impact | Status |
|---|---|---|---|---|
| RL-AI-CHAR-001 | [StoryMaker: Towards Holistic Consistent Characters in Text-to-Image Generation](ai-papers/RL-AI-CHAR-001-storymaker.md) | Character Consistency | Holistic multi-dimensional character consistency | Archived (Layer 1) |
| RL-AI-CHAR-002 | [InstantCharacter: Personalize Any Characters with a Scalable Diffusion Transformer Framework](ai-papers/RL-AI-CHAR-002-instantcharacter.md) | Character Personalization | Identity preservation with controllable edits | Archived (Layer 1) |
| RL-AI-VIDEO-001 | [MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences](ai-papers/RL-AI-VIDEO-001-moviedreamer.md) | Long-Form Video Coherence | Hierarchical decomposition and drift control | Archived (Layer 1) |
| RL-AI-BOARD-001 | [Story2Board: A Training-Free Approach for Expressive Storyboard Generation](ai-papers/RL-AI-BOARD-001-story2board.md) | Storyboard Generation | Multi-objective storyboard quality and diversity | Archived (Layer 1) |

## Synthesis

- [AI Drama Core Research Synthesis v1.0](synthesis/AI_DRAMA_CORE_RESEARCH_SYNTHESIS_v1.md)

## Layering

- `ai-papers/`: normalized records for primary research papers
- `synthesis/`: cross-source synthesis documents
- `official/`: official engineering source records (Layer 2 placeholder)
