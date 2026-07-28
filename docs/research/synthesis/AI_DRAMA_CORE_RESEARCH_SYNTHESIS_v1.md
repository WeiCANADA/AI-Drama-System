# AI Drama Core Research Synthesis v1.0

**Document Status:** Draft — Architecture Reviewed  
**Purpose:** Cross-source synthesis of four core AI drama research papers to derive stable research principles, candidate system requirements, technology candidates, and open architecture questions for the AI Drama System.

## 1. Source Set

This synthesis is based on four primary research sources:

1. **StoryMaker: Towards Holistic Consistent Characters in Text-to-Image Generation**
2. **InstantCharacter: Personalize Any Characters with a Scalable Diffusion Transformer Framework**
3. **MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences**
4. **Story2Board: A Training-Free Approach for Expressive Storyboard Generation**

The purpose of this synthesis is **not** to copy paper-specific model designs directly into the AI Drama System.  
Its purpose is to extract stable, provider-independent architectural principles and identify where evidence is still too weak for a system-level decision.

---

# 2. Evidence Classification

This document uses the following evidence levels:

- **STRONG EVIDENCE** — supported directly by multiple sources and relevant to the AI Drama System at the architectural level.
- **MODERATE EVIDENCE** — supported by multiple sources, but implementation details or scope differ.
- **SINGLE-SOURCE EVIDENCE** — supported meaningfully by only one source in the current source set.
- **TECHNOLOGY CANDIDATE** — an implementation approach worth testing, but not a system architecture requirement.
- **OPEN QUESTION** — insufficient evidence for a decision.
- **CANDIDATE REQUIREMENT** — a possible system requirement derived from evidence, pending domain-spec review.
- **CANDIDATE ADR** — a possible architecture decision worth formal evaluation, not yet accepted.

---

# 3. Findings Supported by Multiple Papers

## 3.1 Character Consistency Extends Beyond Facial Identity

**Evidence Level:** STRONG EVIDENCE

StoryMaker explicitly demonstrates that narrative-ready character consistency includes not only face identity, but also clothing, hairstyle, and body appearance. InstantCharacter independently reinforces the importance of preserving fine-grained character appearance while retaining text-driven editability. MovieDreamer further shows that face identity alone is insufficient for long-form visual continuity.

### Research Principle RP-CHAR-001

> Character consistency in narrative production must be treated as a multi-dimensional visual identity problem rather than a face-matching problem.

Relevant dimensions may include:

- face identity
- hairstyle
- body appearance
- wardrobe
- accessories
- distinctive visual features
- visual reference assets

### Candidate Requirement

**REQ-CHAR-001 — CANDIDATE**

The Character domain SHOULD support multiple forms of persistent and versioned visual identity information beyond facial identity.

---

## 3.2 Identity Must Be Decoupled from Pose, Action, and Composition

**Evidence Level:** STRONG EVIDENCE

StoryMaker explicitly trains with pose conditioning to decouple identity from the reference pose. InstantCharacter demonstrates the need to preserve identity while enabling changes in action, scene, and style. Story2Board shows that visual storytelling requires large variation in pose, framing, scale, and position while preserving recognizability.

### Research Principle RP-CHAR-002

> Character identity should remain stable while pose, action, composition, environment, and style remain independently editable.

### Candidate Requirement

**REQ-SHOT-001 — CANDIDATE**

Shot pose, action, framing, and composition SHOULD be represented separately from Character identity.

---

## 3.3 Structured Narrative Decomposition Is Useful for Generation Planning

**Evidence Level:** MODERATE–STRONG EVIDENCE

Story2Board uses an LLM-based Director step to convert free-form narrative into scene-level prompts. MovieDreamer conditions generation on a structured multimodal script containing plot, scene elements, character descriptions, and identity information.

The evidence supports **structured language-based decomposition**, but does not prove that a specific LLM implementation is universally optimal.

### Research Principle RP-STORY-001

> Free-form narrative should be transformed into structured generation-oriented production context before visual generation.

### Candidate Requirement

**REQ-PLAN-001 — CANDIDATE**

The system SHOULD support an AI-assisted planning stage that transforms narrative content into structured scene-, shot-, or panel-level generation instructions.

---

## 3.4 Long-Form Narrative Generation Benefits from Hierarchical Decomposition

**Evidence Level:** MODERATE EVIDENCE

MovieDreamer explicitly factorizes long-form generation into higher-level narrative prediction and local visual rendering. Story2Board similarly decomposes stories into panel-level generation instructions.

This supports hierarchical planning, but does **not** imply that the AI Drama System should replace its production hierarchy with MovieDreamer-specific keyframe logic.

### Research Principle RP-PROD-001

> Long-form AI drama production should be decomposed into manageable narrative and production units rather than treated as a single end-to-end generation task.

The AI Drama System canonical production hierarchy remains:

```text
Story
→ Episode
→ Scene
→ Shot
```

Keyframes are a **generation strategy**, not a replacement for Shot.

### Candidate Requirement

**REQ-PROD-001 — CANDIDATE**

The system SHOULD support provider-specific anchor frames or keyframes within generation workflows without changing Shot as the canonical audiovisual production unit.

---

## 3.5 Structured Generation Context Should Be Multimodal

**Evidence Level:** MODERATE EVIDENCE

MovieDreamer combines plot, scene information, character descriptions, face embeddings, and historical context. StoryMaker combines face identity features, portrait features, pose information, masks, and text. InstantCharacter combines reference-image features with textual control.

### Research Principle RP-GEN-001

> Generation context should be capable of combining structured narrative data with visual and identity references.

### Candidate Requirement

**REQ-GEN-001 — CANDIDATE**

Generation planning SHOULD support structured multimodal context containing narrative, character, environment, style, continuity, and reference information.

This does **not** imply that the domain model should store ArcFace, SigLIP, CLIP, DINOv2, PPR, or other model-specific representations directly.

---

## 3.6 Storyboard Quality Is Multi-Objective

**Evidence Level:** STRONG EVIDENCE

Story2Board directly demonstrates that high identity consistency can coexist with poor cinematic variety when a model collapses toward repetitive compositions. StoryMaker and InstantCharacter also expose trade-offs between consistency and controllability/editability.

### Research Principle RP-BOARD-001

> Storyboard quality must balance character consistency with prompt alignment, scene diversity, composition, environmental grounding, and narrative expressiveness.

### Candidate Requirement

**REQ-QC-001 — CANDIDATE**

Storyboard QC SHOULD evaluate multiple independent dimensions rather than rely on a single consistency score.

Potential dimensions:

- character consistency
- prompt / story alignment
- scene diversity
- framing diversity
- character scale variation
- character position variation
- background richness
- composition quality
- narrative grounding

---

## 3.7 Long Sequences Require Drift-Control Mechanisms

**Evidence Level:** MODERATE EVIDENCE

MovieDreamer identifies progressive error accumulation when video generation repeatedly extends from previous output frames, and introduces anchor-based mechanisms to reduce drift. Other papers also reinforce the need to preserve stable references across multiple outputs.

### Research Principle RP-CONT-001

> Long-form generation requires explicit mechanisms for preserving relevant identity and context over time and limiting progressive visual drift.

### Candidate Requirement

**REQ-CONT-001 — CANDIDATE**

The Continuity and Generation layers SHOULD support stable reference context across multiple Shots or generation segments.

The exact mechanism remains provider-specific.

---

# 4. Findings Supported Primarily by One Paper

The following are valuable, but should not become system-wide architecture requirements without further validation.

## 4.1 AR + Diffusion for Ultra-Long Generation

**Evidence Level:** SINGLE-SOURCE EVIDENCE  
**Primary Source:** MovieDreamer

MovieDreamer uses autoregressive modeling for long-term sequence prediction and diffusion for visual rendering.

### Classification

**Technology / Architecture Candidate**

Possible future evaluation:

```text
Narrative / visual sequence planner
        ↓
Anchor / keyframe prediction
        ↓
Diffusion or video rendering
```

The AI Drama System SHOULD remain compatible with such a design, but MUST NOT hard-code AR + Diffusion as the only generation architecture.

---

## 4.2 SigLIP + DINOv2 Feature Fusion

**Evidence Level:** SINGLE-SOURCE EVIDENCE  
**Primary Source:** InstantCharacter

InstantCharacter reports benefits from combining SigLIP and DINOv2 for fine-grained and robust character representation.

### Classification

**Technology Candidate**

This belongs to provider/workflow experimentation, not Character domain architecture.

---

## 4.3 Reciprocal Attention Value Mixing

**Evidence Level:** SINGLE-SOURCE EVIDENCE  
**Primary Source:** Story2Board

RAVM is a promising training-free mechanism for improving inter-panel consistency while preserving layout diversity.

### Classification

**Technology Candidate**

Potential use:

- training-free storyboard workflow
- consistency-preserving storyboard provider
- experimental ComfyUI node/workflow

It should not become a mandatory Storyboard domain requirement.

---

## 4.4 Attention-Mask Regularization

**Evidence Level:** SINGLE-SOURCE EVIDENCE  
**Primary Source:** StoryMaker

StoryMaker uses segmentation-mask-based attention loss to reduce subject/background feature mixing.

### Classification

**Technology Candidate**

Potential use:

- multi-character generation workflows
- provider-specific subject isolation
- experimental QC / mask-guided generation

---

## 4.5 Anchor-Feature Video Extension

**Evidence Level:** SINGLE-SOURCE EVIDENCE  
**Primary Source:** MovieDreamer

Using stable anchor features rather than recursively conditioning only on the most recent output reduces error accumulation.

### Classification

**Technology Candidate**

The system requirement should be broader:

> generation workflows may preserve stable reference anchors across long sequences.

---

# 5. Trade-offs Identified Across Sources

## 5.1 Consistency vs. Editability

StoryMaker and InstantCharacter emphasize strong character preservation. Story2Board demonstrates that excessive consistency can suppress pose, composition, and environmental diversity.

### Architecture Implication

The system must avoid defining “consistency” as “minimal visual change.”

Consistency should preserve identity while allowing intentional production changes.

---

## 5.2 Training-Free vs. Specialized Adaptation

Story2Board demonstrates advantages of training-free approaches for rapid, expressive previsualization.

StoryMaker and InstantCharacter show the advantages of specialized adapters and training for high-fidelity identity preservation.

### Architecture Implication

The AI Drama System SHOULD support multiple workflow classes:

```text
Fast / Training-Free
        ↓
Storyboard / Previsualization

High-Fidelity / Specialized
        ↓
Final Asset / Production Generation
```

This is a workflow-routing concern, not a reason to choose one approach globally.

---

## 5.3 Fidelity vs. Context Compression

MovieDreamer compresses visual and textual representations to scale to long sequences.

InstantCharacter invests more computation in rich visual features for fidelity.

### Architecture Implication

Different production stages may require different context/fidelity trade-offs.

The system should not impose a single representation strategy across planning, storyboard, image, and video generation.

---

# 6. Character Architecture Implications

## 6.1 Stable Character Identity vs. Mutable Appearance

Evidence suggests the system should distinguish:

```text
Character
    persistent identity

CharacterVersion / Appearance State
    mutable visual presentation
```

Potential future sub-concepts:

- wardrobe
- hairstyle
- injury state
- age state
- accessories
- body appearance
- visual references

Exact entity boundaries require the Character Asset Specification.

---

## 6.2 Multiple Character References

**REQ-CHAR-002 — CANDIDATE**

Character or CharacterVersion SHOULD support multiple reference assets.

Possible references:

- face portrait
- full body
- side view
- three-quarter view
- wardrobe
- expression
- pose
- style-neutral reference

Provider-specific embeddings SHOULD remain outside the stable domain model.

---

## 6.3 Provider-Specific Identity Representations

Possible implementations may use:

- face embeddings
- visual encoders
- adapter embeddings
- LoRA
- identity tokens
- model-specific references

### Architecture Rule

These should be modeled as provider/workflow-specific generation representations, not as the definition of Character itself.

---

# 7. Story / Scene / Shot Architecture Implications

## 7.1 Preserve Canonical Production Hierarchy

```text
Story
→ Episode
→ Scene
→ Shot
```

The research supports hierarchical decomposition but does not justify replacing this production model.

---

## 7.2 Keyframes Are Generation Artifacts or Planning Anchors

Keyframes may be associated with:

- Shot
- video generation segment
- storyboard
- continuity anchor
- provider workflow

They should not automatically become a new top-level narrative entity.

---

## 7.3 Shot Spatial Information

**REQ-SHOT-002 — CANDIDATE**

Shot planning SHOULD be able to represent structured spatial information for characters.

Possible concepts:

- frame position
- relative scale
- pose intent
- action
- spatial relation to other characters
- foreground/background placement

The representation must remain provider-independent.

---

# 8. Storyboard Architecture Implications

## 8.1 Storyboard Is a Planning Stage

Research strongly supports Storyboard as more than a preview-image gallery.

Storyboard should help validate:

- narrative coverage
- framing
- visual pacing
- scene diversity
- environment
- character placement
- continuity
- production feasibility

---

## 8.2 Training-Free Storyboard Workflow

**REQ-WF-BOARD-001 — CANDIDATE**

The workflow system SHOULD be capable of supporting fast, training-free storyboard generation for previsualization.

This does not require Story2Board/RAVM specifically.

---

## 8.3 Storyboard QC

Potential QC metrics:

- prompt alignment
- character consistency
- scene diversity
- background richness
- composition
- shot redundancy
- narrative coverage

Story2Board metrics are candidates for implementation experiments, not yet system standards.

---

# 9. Generation and Workflow Implications

## 9.1 Workflow Context Awareness

**REQ-WF-001 — CANDIDATE**

Workflow selection MAY consider production context such as:

- artifact type
- character count
- storyboard vs. final generation
- quality target
- speed target
- reference availability
- continuity requirements

---

## 9.2 Multi-Character Complexity

StoryMaker explicitly identifies increasing difficulty at three or more characters.

### Candidate Requirement

**REQ-WF-002 — CANDIDATE**

Generation workflows SHOULD be able to specialize by character count or scene complexity.

Example:

```text
single-character workflow
two-character workflow
complex multi-character workflow
```

No exact routing rule is accepted yet.

---

# 10. Continuity Implications

## 10.1 Continuity Is a Production-State Problem

The research supports holistic visual continuity, but provider-specific mechanisms such as background embeddings or attention masks should not define the Continuity domain.

Continuity should represent production truth such as:

- wardrobe
- hairstyle
- injury
- held props
- location state
- lighting
- time
- environment changes

Generation workflows then use that state as context.

---

## 10.2 Historical Context

**REQ-CONT-002 — CANDIDATE**

Generation of later Shots SHOULD be capable of receiving relevant prior production context.

The system should decide which context is relevant rather than blindly passing all previous outputs.

---

# 11. QC Implications

## 11.1 Multi-Dimensional Character QC

Potential dimensions:

- face similarity
- overall appearance similarity
- wardrobe consistency
- hairstyle consistency
- body consistency
- prompt alignment

No single metric should represent all aspects of character consistency.

---

## 11.2 Storyboard QC

Story2Board suggests useful candidate metrics:

- VQAScore
- DreamSim
- Scene Diversity

These should be experimentally validated before becoming production thresholds.

---

# 12. Stable Research Principles v1.0

The current four-paper evidence supports the following relatively stable principles.

## RP-001 — Holistic Character Consistency

Character consistency is broader than facial identity.

## RP-002 — Identity / Pose Separation

Character identity should remain independent from pose, action, framing, environment, and style.

## RP-003 — Hierarchical Production Decomposition

Long-form narrative generation benefits from decomposition into manageable production units.

## RP-004 — Structured Multimodal Generation Context

Generation benefits from structured narrative context combined with visual and identity references.

## RP-005 — Multi-Objective Storyboard Quality

Storyboard quality requires balancing consistency with composition, scene diversity, prompt alignment, and narrative grounding.

## RP-006 — Long-Term Drift Control

Long sequences require stable historical/reference context and explicit drift-control mechanisms.

---

# 13. Candidate Requirements Registry

Current candidates:

```text
REQ-CHAR-001
Character identity SHOULD support multiple visual dimensions beyond face identity.

REQ-CHAR-002
Character or CharacterVersion SHOULD support multiple reference assets.

REQ-SHOT-001
Pose, action, framing, and composition SHOULD remain separate from Character identity.

REQ-SHOT-002
Shot planning SHOULD support structured character spatial information.

REQ-PLAN-001
The system SHOULD support AI-assisted transformation of narrative into structured production instructions.

REQ-PROD-001
Provider-specific keyframes or anchors MAY be used without replacing Shot as the canonical production unit.

REQ-GEN-001
Generation context SHOULD support structured multimodal production information.

REQ-CONT-001
Long-form generation SHOULD support stable reference context across multiple production segments.

REQ-CONT-002
Later generation SHOULD be able to receive relevant historical production context.

REQ-QC-001
Storyboard QC SHOULD evaluate multiple dimensions rather than consistency alone.

REQ-WF-001
Workflow selection MAY consider production context.

REQ-WF-002
Generation workflows SHOULD be capable of specialization by character count or scene complexity.

REQ-WF-BOARD-001
The system SHOULD support fast previsualization-oriented storyboard workflows.
```

These requirements are **not yet accepted implementation requirements**.

They must be reviewed during the relevant domain specifications.

---

# 14. Technology Candidates

The following techniques are worth experimentation but should remain outside stable domain architecture:

```text
StoryMaker
- PPR
- attention-mask regularization
- face + portrait feature fusion
- ControlNet pose decoupling

InstantCharacter
- SigLIP + DINOv2
- scalable transformer adapter
- timestep-aware Q-former
- staged training

MovieDreamer
- AR visual-token prediction
- diffusion autoencoder
- multimodal script compression
- ID-preserving diffusion renderer
- anchor-feature video extension

Story2Board
- Latent Panel Anchoring
- Reciprocal Attention Value Mixing
- training-free storyboard consistency
- Scene Diversity metric
```

These belong under:

```text
Provider Experiments
Workflow Experiments
Model Evaluation
QC Experiments
```

not directly in the core domain model.

---

# 15. Candidate ADRs Worth Evaluating

The current evidence is strong enough to justify evaluating the following architectural decisions.

## ADR Candidate A

**Separate production domain from generation implementation.**

Research methods should not dictate stable domain entities.

---

## ADR Candidate B

**Separate persistent Character identity from mutable visual appearance/version state.**

---

## ADR Candidate C

**Treat Storyboard as a first-class planning and QC stage.**

---

## ADR Candidate D

**Keep structured production intent separate from rendered prompts and provider-specific conditioning.**

---

## ADR Candidate E

**Preserve Shot as the canonical audiovisual production unit while allowing provider-specific keyframe/anchor strategies.**

---

No ADR is accepted by this document.

---

# 16. Open Architectural Questions

## OQ-001 — Multi-Character Scaling

How should the system represent and generate scenes with three or more characters without identity blending or attention entanglement?

---

## OQ-002 — Wardrobe Modeling

Should Wardrobe be:

- part of CharacterVersion
- an independent reusable Asset
- Continuity state
- or a combination of these?

---

## OQ-003 — Hair / Body / Appearance State

Which character attributes belong to persistent identity versus mutable appearance?

---

## OQ-004 — CharacterReference Modeling

Should CharacterReference be:

- a dedicated entity
- an Artifact relationship
- or a typed relation between CharacterVersion and Artifact?

---

## OQ-005 — Keyframe Modeling

Should keyframes exist as:

- Artifact subtype
- Shot planning data
- Video workflow state
- or a dedicated production entity?

---

## OQ-006 — Multi-Objective QC

How should the system balance:

- consistency
- prompt alignment
- scene diversity
- narrative expressiveness
- technical quality

without over-optimizing one metric?

---

## OQ-007 — Context Selection

How should long-form generation determine which historical context should be passed to a later Shot?

---

## OQ-008 — Provider-Neutral Spatial Representation

How should Shot-level spatial relationships be represented independently of masks, attention maps, bounding boxes, or a specific generation model?

---

# 17. Research Confidence Summary

| Area | Evidence Strength | Architecture Readiness |
|---|---|---|
| Holistic character consistency | Strong | High |
| Identity / pose separation | Strong | High |
| Narrative decomposition | Moderate–Strong | Medium–High |
| Storyboard diversity | Strong | High |
| Multimodal generation context | Moderate | Medium |
| Long-term drift control | Moderate | Medium |
| AR + Diffusion architecture | Single-source | Low |
| SigLIP + DINOv2 | Single-source | Low |
| RAVM | Single-source | Low |
| Attention-mask regularization | Single-source | Low |

---

# 18. Research Conclusion

The four papers jointly support a clear architectural direction for the AI Drama System:

```text
Production Intent
        ↓
Structured Narrative / Shot Planning
        ↓
Versioned Character + Asset Context
        ↓
Storyboard / Previsualization
        ↓
Workflow Selection
        ↓
Provider-Specific Generation
        ↓
Artifact + Provenance
        ↓
Multi-Dimensional QC
        ↓
Continuity / Delivery
```

The strongest cross-source conclusion is that AI drama generation should not be designed around a single model architecture.

The stable system must represent production intent independently from model-specific mechanisms such as:

```text
ArcFace
SigLIP
DINOv2
CLIP
PPR
RAVM
ControlNet
LoRA
AR visual tokens
Diffusion Autoencoders
```

Those technologies should remain replaceable workflow/provider implementations.

The next architecture step should therefore be:

```text
AI Drama Core Research Synthesis v1.0
        ↓
Character Research Synthesis
        ↓
Character Asset Specification v1.0
        ↓
Shot Specification
        ↓
Storyboard Specification
```

No Django model should be finalized solely from these four papers.

---

**Document Status:** Architecture Reviewed — Ready for Domain-Specific Research Expansion
