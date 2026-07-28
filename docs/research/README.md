# AI Drama System Research Library

This directory archives research evidence used to inform architecture discussions for the AI Drama System.

## Purpose

The Research Library preserves traceable links between primary research sources, internal research interpretation, and architecture governance.

Research papers do not directly define the AI Drama System architecture.

Paper-specific model implementations remain replaceable technology candidates unless promoted through architecture review.

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
