# AI Drama System

## Development Specification v0.2

**Document Status:** Draft
**Version:** 0.2
**Document Type:** System Architecture and Development Specification
**Purpose:** Define the product architecture, production model, domain boundaries, research governance, and development process for the AI Drama System.
**Primary Audience:** Developers, system architects, GitHub Copilot, AI coding agents, technical reviewers, and future production-tooling contributors.

---

# 1. Project Overview

## 1.1 Project Name

**AI Drama System**

---

## 1.2 Product Definition

AI Drama System is a production platform for creating AI-assisted drama, comic drama, animated drama, and short-form narrative video.

The system manages the structured production lifecycle from source narrative to final deliverable media.

The platform is **not** designed as a single-prompt image generator or single-prompt video generator.

Instead, the system treats AI media creation as a structured production process.

```text
Story
↓
Episode
↓
Scene
↓
Shot Planning
↓
Storyboard
↓
Asset Binding
↓
Prompt Construction
↓
Generation
↓
Quality Control
↓
Continuity Review
↓
Timeline Assembly
↓
Audio / Subtitle
↓
Export
```

The architecture MUST support:

```text
iterative production
reusable assets
research-grounded design
workflow versioning
provider abstraction
character consistency
visual continuity
generation provenance
quality control
human review
reproducibility
future automation
```

---

# 1.3 Product Vision

The long-term goal is not to build an AI generation interface.

The goal is to build an:

> AI-native narrative production system.

The system should progressively support the responsibilities normally distributed across:

```text
Writer
Screenwriter
Director
Storyboard Artist
Cinematographer
Production Designer
Character Designer
Prompt Engineer
AI Generation Operator
Continuity Supervisor
Editor
Sound Designer
QC Reviewer
Producer
```

AI agents may automate portions of these responsibilities in the future.

However, automation MUST operate against structured production data rather than uncontrolled free-form generation.

---

# 1.4 Architectural Principles

The system MUST follow the following architectural principles.

---

## 1.4.1 Model-Agnostic

Business and domain logic MUST NOT depend directly on a specific AI model or provider.

A production request should be capable of execution through multiple compatible providers.

Examples:

```text
LLM
├── OpenAI
├── Anthropic
├── Gemini
└── local models

Image
├── ComfyUI
├── FLUX-based workflows
├── Stable Diffusion ecosystems
├── cloud APIs
└── future providers

Video
├── Wan
├── Kling
├── Veo
├── local workflows
└── future providers

Audio
├── local TTS
├── cloud TTS
├── music generation systems
└── future providers
```

Provider-specific behavior MUST remain behind provider interfaces or adapters.

---

## 1.4.1A Reuse-First AI Capability Strategy

AI Drama System is primarily a production and orchestration platform around AI
capabilities, not a foundation-model training program.

Where practical, the system SHOULD prefer reuse of existing capabilities via:

```text
existing models
mature open-source libraries
official provider APIs
existing workflow ecosystems
local models where appropriate
replaceable provider adapters
configurable and versioned workflows
```

Custom/local model infrastructure is not prohibited.

Custom/local models MAY be introduced when a concrete system requirement cannot
reasonably be satisfied by existing capabilities, or when a documented strategic
reason justifies that investment.

Any such introduction SHOULD be justified through specification and ADR review
when architecturally significant.

---

## 1.4.2 Workflow-Driven

Generation behavior MUST be represented through configurable and versioned workflows.

Generation logic MUST NOT be permanently hard-coded inside:

```text
views
controllers
Django models
serializers
UI components
```

Recommended conceptual flow:

```text
Production Context
↓
GenerationRequest
↓
WorkflowVersion
↓
Provider
↓
GenerationTask
↓
GenerationAttempt
↓
GenerationResult
↓
Artifact
```

Workflow definitions should describe:

```text
inputs
required assets
provider
model
parameters
parameter mappings
execution steps
outputs
validation expectations
```

---

## 1.4.3 Asset-Centric

Reusable production elements MUST be represented as persistent assets.

Core asset categories include:

```text
Character
Location
Prop
Style
Voice
Reference Image
Reference Audio
```

Assets SHOULD support versioning where changes can affect generation output.

Assets may be reused across:

```text
Shots
Scenes
Episodes
Projects
```

where scope and permissions allow.

---

## 1.4.4 Shot-Based Production

The Shot is the primary audiovisual production unit.

A Shot represents one continuous camera presentation or equivalent generated visual unit.

Production artifacts SHOULD normally be traceable to a Shot.

Examples:

```text
storyboard image
generated image
generated video
dialogue audio
sound effect
prompt instance
continuity state
QC result
```

Not every artifact must originate directly from a Shot.

Project-level, Character-level, Scene-level, Episode-level, research, workflow, and reference artifacts may exist independently.

However, final production media should retain identifiable production context.

---

## 1.4.5 Reproducible

Every generated artifact MUST retain enough provenance to determine how it was created.

At minimum, provenance SHOULD include:

```text
production context
provider
model
model version if available
workflow version
prompt
input assets
asset versions
generation parameters
seed if available
task ID
attempt ID
timestamp
output artifact
```

Where provider capabilities allow deterministic generation, the system SHOULD support reproducing generation attempts.

---

## 1.4.6 Research-Grounded

Important architectural and domain decisions SHOULD be supported by a credible Source of Truth.

Preferred sources include:

```text
primary research papers
official technical documentation
formal standards
recognized production practices
authoritative industry references
well-maintained open-source implementations
```

Research MUST inform specifications.

Research SHOULD NOT be copied directly into implementation without translation into explicit system requirements.

Recommended process:

```text
Research
↓
Finding
↓
Requirement
↓
Specification
↓
ADR if architectural
↓
Domain Model
↓
Implementation
↓
Tests
```

---

## 1.4.7 Production-Oriented

The system MUST model AI drama as a media-production workflow rather than merely a sequence of AI API calls.

The following concepts are first-class architectural concerns:

```text
narrative structure
screenplay structure
scene planning
shot planning
cinematography
storyboarding
character consistency
continuity
asset management
review
editing
audio
subtitles
delivery
```

AI generation infrastructure exists to serve the production model.

The production model MUST NOT be redesigned merely around limitations of one generation provider.

---

## 1.4.8 Human-Reviewable

Important production decisions MUST remain inspectable and reviewable.

AI-generated outputs such as:

```text
episode breakdowns
scene plans
shot plans
prompts
storyboards
continuity changes
QC decisions
```

SHOULD support human review before becoming locked production truth.

---

## 1.4.9 Traceable Decisions

Important system decisions SHOULD be traceable to:

```text
source evidence
specification requirement
ADR
implementation
tests
```

The project SHOULD avoid major architectural decisions that exist only in chat history.

---

# 2. Product Scope

## 2.1 Primary Workflow

The primary production lifecycle is:

```text
Create Project
↓
Import or Write Story
↓
Adapt Story
↓
Create Episodes
↓
Create Scenes
↓
Plan Shots
↓
Generate / Design Storyboard
↓
Review Storyboard
↓
Bind Production Assets
↓
Construct Prompts
↓
Generate Images / Video
↓
Generate Dialogue / Audio
↓
Perform QC
↓
Review Continuity
↓
Assemble Timeline
↓
Add Subtitle / Audio Mix
↓
Export Episode
```

---

# 2.2 Target Users

Initial target user:

```text
Single creator / developer
```

Future users may include:

```text
Writer
Director
Storyboard Artist
Prompt Engineer
AI Generation Operator
Editor
Producer
QC Reviewer
Administrator
```

The initial implementation MAY operate as a single-user application.

The architecture SHOULD avoid decisions that make future workspace-based collaboration unnecessarily difficult.

---

# 2.3 MVP Scope

The first usable MVP MUST support the following capabilities.

---

## 2.3.1 Project Management

```text
Project creation
Project metadata
Project settings
Project status
Project-level default style
Project-level generation settings
```

---

## 2.3.2 Narrative Structure

```text
Story
Episode
Scene
Shot
```

The MVP MAY treat screenplay structures as lightweight fields or documents before introducing a dedicated screenplay domain.

---

## 2.3.3 Asset Management

Initial reusable assets:

```text
Character
Location
Prop
Style
Voice
```

Each asset SHOULD support versioning where output reproducibility requires it.

---

## 2.3.4 Shot Configuration

Each Shot SHOULD support structured production information including:

```text
characters
location
props
action
emotion
dialogue
camera
composition
lighting
time
weather where relevant
duration
continuity information
style
generation overrides
```

---

## 2.3.5 Storyboard

The MVP MUST support visual Shot planning.

Users should be able to view Storyboard Frames associated with Shots.

Storyboard functionality SHOULD support:

```text
draft
review
approve
reject
replace
regenerate
```

Storyboard MUST be treated as a production-planning stage, not only as a gallery.

---

## 2.3.6 Prompt Generation

Structured prompts SHOULD be constructed from:

```text
shot data
character assets
location assets
style assets
continuity state
production knowledge
prompt templates
workflow requirements
provider requirements
```

Prompt generation MUST remain separate from provider execution.

---

## 2.3.7 Generation Tasks

The system MUST support asynchronous generation jobs for:

```text
image
video
voice
audio
```

Later task classes may include:

```text
LLM planning
subtitle generation
QC
embedding extraction
reference preprocessing
```

---

## 2.3.8 ComfyUI Integration

ComfyUI SHOULD be the initial local image/video workflow execution provider.

However:

> ComfyUI MUST NOT become the domain architecture.

ComfyUI MUST be accessed through provider and workflow abstractions.

---

## 2.3.9 Basic QC

Users MUST be able to:

```text
approve
reject
retry
mark for review
```

generated media.

Structured QC metrics may initially be optional but the data architecture SHOULD support future automated scoring.

---

# 2.4 Out of Scope for Initial MVP

The initial MVP does not require:

```text
professional NLE replacement
real-time collaborative editing
mobile applications
public marketplace
social media publishing automation
multi-tenant SaaS billing
complex enterprise rights management
foundation-model training
distributed GPU cluster orchestration
full studio production-management replacement
```

These features may receive future extension points.

---

# 2.5 Future Capabilities

Potential later capabilities include:

```text
novel adaptation
screenplay generation
episode planning
automatic scene extraction
automatic shot planning
AI storyboard generation
character consistency scoring
continuity detection
prompt optimization
visual semantic QC
lip synchronization
voice cloning
music generation
sound design
automatic timeline assembly
automatic rough cut
multi-language dubbing
subtitle translation
AI Director
AI Cinematographer
AI Continuity Supervisor
AI Production Designer
production cost optimization
provider routing
GPU scheduling
collaborative workspaces
```

---

# 3. System Architecture

## 3.1 High-Level Architecture

```text
                    AI DRAMA SYSTEM
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼

 RESEARCH LAYER      PRODUCTION KNOWLEDGE    ASSET SYSTEM
        │                  │                  │
 Papers              Screenwriting           Character
 Official Docs       Cinematography          Location
 Standards           Storyboard Rules        Prop
 Production Refs     Continuity Rules        Style
 Open Source         QC Knowledge            Voice
 Benchmarks          Prompt Knowledge        References

        │                  │                  │
        └──────────────┬───┴──────────────────┘
                       ▼

                 PRODUCTION DOMAIN
                       │
                Project / Story
                       │
                    Episode
                       │
                     Scene
                       │
                 Shot Planning
                       │
                  Storyboard
                       │
                      Shot

                       │
                       ▼

                PROMPT / PLANNING
                       │
                Prompt Templates
                Prompt Instances
                Agent Planning
                Context Assembly

                       │
                       ▼

              AI ORCHESTRATION LAYER
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
           LLM       Image       Video
            │          │          │
            └──────────┼──────────┘
                       ▼
                  Voice / Audio

                       │
                       ▼

                 WORKFLOW ENGINE
                       │
                 Workflow
                 Version
                 Parameter Map
                 Generation Task
                 Attempt
                 Retry
                 State Machine

                       │
                       ▼

                  PROVIDER LAYER
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
    ComfyUI         Cloud API        Local AI

                       │
                       ▼

                    ARTIFACTS
                       │
                Storage Metadata
                Provenance
                Relationships

                       │
                       ▼

                    QC ENGINE
                       │
                Character QC
                Style QC
                Continuity QC
                Prompt Alignment
                Technical Quality

                       │
                       ▼

                 DELIVERY LAYER
                       │
                  Timeline
                  Subtitle
                  Audio
                  Export
```

---

# 3.2 Research Layer

The Research Layer contains engineering and production sources used to design the system.

The Research Layer is primarily a **development-time knowledge system**.

It is distinct from runtime Production Knowledge.

Categories include:

```text
AI Research Papers
Official Technical Documentation
Film Production Standards
Animation Production References
Open Source Projects
Benchmarks and Datasets
Architecture References
```

Research findings SHOULD influence:

```text
Development Specifications
Domain Specifications
ADRs
QC definitions
data models
provider architecture
workflow architecture
tests
```

The initial Research Library SHOULD reside primarily in repository documentation.

Recommended location:

```text
docs/research/
```

---

# 3.3 Production Knowledge Layer

Production Knowledge represents reusable domain knowledge needed during runtime or AI-assisted planning.

Examples:

```text
screenwriting rules
shot terminology
camera conventions
storyboard principles
composition guidance
continuity rules
prompt guidance
QC criteria
```

Production Knowledge MAY later be exposed through:

```text
retrieval
structured templates
knowledge records
agent context
LLM tools
```

Research Library and Production Knowledge MUST remain conceptually distinct.

```text
Research Library
    informs system design

Production Knowledge
    informs production behavior
```

---

# 3.4 Asset Layer

The Asset Layer manages reusable production identity and references.

Initial asset categories:

```text
Character
Location
Prop
Style
Voice
```

Potential later categories:

```text
Wardrobe
Vehicle
Creature
Environment
Set
Lighting Preset
Camera Preset
Pose Reference
Expression Reference
Music Theme
Sound Profile
```

Assets SHOULD support stable identity plus explicit versions.

---

# 3.5 Production Layer

The Production Layer models what is being created.

Primary hierarchy:

```text
Project
└── Story
    └── Episode
        └── Scene
            └── Shot
```

Planning structures may exist between narrative levels and final production entities.

Example:

```text
Scene
↓
Shot Planning
↓
Storyboard
↓
Approved Shot
```

---

# 3.6 AI Orchestration Layer

The AI Orchestration Layer translates production intent into model execution.

Responsibilities include:

```text
context assembly
prompt construction
workflow selection
provider selection
model selection
generation requests
parameter resolution
reference asset resolution
```

The orchestration layer SHOULD not contain provider-specific networking or SDK behavior.

---

# 3.7 Workflow Layer

The Workflow Layer defines executable AI procedures.

Responsibilities:

```text
workflow definition
workflow versioning
input contracts
parameter mapping
task creation
queueing
execution
retry
failure management
state transitions
output registration
```

A workflow may represent:

```text
image generation
video generation
voice generation
storyboard generation
character reference generation
upscaling
face refinement
lip sync
QC
```

---

# 3.8 Provider Layer

Providers represent executable AI engines or external services.

Conceptual interfaces may include:

```python
class LLMProvider:
    def execute(self, request):
        ...

class ImageProvider:
    def execute(self, request):
        ...

class VideoProvider:
    def execute(self, request):
        ...

class AudioProvider:
    def execute(self, request):
        ...
```

Exact Python interfaces MUST be defined in later technical specifications.

Domain models MUST NOT import provider implementation code.

---

# 3.9 Artifact Layer

Files MUST NOT be represented only as arbitrary local paths.

Generated or imported production media SHOULD be represented through an Artifact entity.

Artifact responsibilities include:

```text
storage identity
file type
metadata
checksum
dimensions
duration
provenance
relationships
generation origin
```

Storage systems MAY include:

```text
local filesystem during development
MinIO
AWS S3
Cloudflare R2
other S3-compatible storage
```

---

# 3.10 QC Layer

QC validates planned and generated production outputs.

QC categories may include:

```text
character consistency
wardrobe consistency
style consistency
continuity
composition quality
prompt alignment
storyboard diversity
technical image quality
artifact detection
motion quality
audio quality
subtitle quality
```

QC may use:

```text
manual review
rules
computer vision
embeddings
vision-language models
audio analysis
automated metrics
```

QC metrics MUST have explicit semantics.

Where possible, a metric SHOULD define:

```text
name
description
measurement method
range
threshold
target
applicable artifact type
automated/manual
source or rationale
```

---

# 3.11 Delivery Layer

The Delivery Layer transforms approved production assets into final outputs.

Capabilities may include:

```text
timeline assembly
video sequencing
audio track placement
subtitle generation
subtitle placement
audio mixing
episode export
project export
delivery packaging
```

---

# 4. Proposed Technology Architecture

## 4.1 Backend

Initial recommended stack:

```text
Python
Django
Django REST Framework
PostgreSQL
Redis
Celery
pgvector
S3-compatible object storage
```

---

# 4.2 Local Development

Initial development SHOULD support:

```text
PostgreSQL
Redis
Celery worker
MinIO
ComfyUI
Django development server
```

Docker Compose MAY later be used to standardize development services.

---

# 4.3 Frontend

Initial frontend MAY use:

```text
Django Templates
Bootstrap 5
JavaScript
```

The backend domain architecture MUST NOT depend on Bootstrap or server-rendered templates.

A separate SPA or other frontend SHOULD remain possible later.

---

# 4.4 Proposed Repository Structure

```text
AI-Drama-System/
│
├── README.md
├── AGENTS.md
├── .gitignore
│
├── .github/
│   ├── copilot-instructions.md
│   └── instructions/
│       ├── django.instructions.md
│       ├── tests.instructions.md
│       ├── providers.instructions.md
│       └── docs.instructions.md
│
├── docs/
│   │
│   ├── DEVELOPMENT_SPEC.md
│   ├── ROADMAP.md
│   │
│   ├── architecture/
│   │   ├── system-overview.md
│   │   ├── domain-architecture.md
│   │   ├── generation-architecture.md
│   │   ├── workflow-architecture.md
│   │   └── storage-architecture.md
│   │
│   ├── domain/
│   │   ├── project.md
│   │   ├── story.md
│   │   ├── episode.md
│   │   ├── scene.md
│   │   ├── shot.md
│   │   ├── character.md
│   │   ├── location.md
│   │   └── artifact.md
│   │
│   ├── adr/
│   │
│   ├── research/
│   │   ├── README.md
│   │   ├── ai-papers/
│   │   ├── official-docs/
│   │   ├── film-production/
│   │   ├── animation-production/
│   │   ├── open-source/
│   │   ├── benchmarks/
│   │   └── architecture/
│   │
│   └── specifications/
│
├── backend/
│   │
│   ├── config/
│   │
│   ├── apps/
│   │   ├── projects/
│   │   ├── stories/
│   │   ├── production/
│   │   ├── assets/
│   │   ├── knowledge/
│   │   ├── prompts/
│   │   ├── workflows/
│   │   ├── generation/
│   │   ├── continuity/
│   │   ├── qc/
│   │   └── exports/
│   │
│   ├── providers/
│   │   ├── llm/
│   │   ├── image/
│   │   ├── video/
│   │   └── audio/
│   │
│   ├── services/
│   ├── workers/
│   ├── common/
│   └── tests/
│
└── frontend/
```

Exact Django application boundaries MAY change after domain specifications are completed.

---

# 5. Domain Architecture

## 5.1 Domain Groups

The system initially contains the following conceptual domains:

```text
Project Domain
Narrative Domain
Production Domain
Asset Domain
Generation Domain
Workflow Domain
Continuity Domain
Quality Domain
Artifact Domain
Knowledge Domain
```

These are conceptual boundaries and do not require a one-to-one mapping to Django apps.

---

# 5.2 Project Domain

Primary entity:

```text
Project
```

A Project acts as the top-level production container.

A Project may contain:

```text
story
episodes
assets
project settings
style defaults
knowledge overrides
workflows
generation configuration
exports
```

Potential future extensions:

```text
seasons
alternate cuts
multiple stories
workspace ownership
collaborators
```

---

# 5.3 Narrative Domain

Primary entities:

```text
Story
Episode
Scene
```

Narrative entities represent dramatic meaning and organization.

The Shot belongs to the boundary between narrative and production planning.

---

# 5.4 Production Domain

Primary entities currently include:

```text
Shot
Timeline
```

Potential planning entities MAY later include:

```text
ShotPlan
Storyboard
StoryboardFrame
ProductionPlan
```

These entities MUST NOT be finalized until the corresponding domain specifications are researched and written.

---

# 5.5 Asset Domain

Initial entities:

```text
Character
CharacterVersion

Location
LocationVersion

Prop
PropVersion

Style
StyleVersion

Voice
VoiceVersion
```

Asset definition and asset version SHOULD remain conceptually separate.

Example:

```text
Character
└── Grace

CharacterVersion
├── Grace v1
├── Grace v2
└── Grace Winter Costume
```

A newer CharacterVersion MUST NOT silently change historical Shots or generation results.

---

# 5.6 Character Architecture Principle

Character consistency must be treated as broader than facial identity.

Future Character specifications SHOULD evaluate:

```text
face identity
hair
body appearance
body proportions
wardrobe
accessories
distinctive features
expression references
pose references
multi-view references
generation references
provider-specific identity mechanisms
```

The exact database schema is intentionally deferred.

Before implementation, the Character Domain MUST receive a dedicated:

```text
Character Asset Specification
```

supported by:

```text
character-consistency research
production Character Bible practices
provider capabilities
workflow requirements
```

---

# 5.7 Generation Domain

Core conceptual entities:

```text
PromptTemplate
PromptTemplateVersion
PromptInstance

GenerationTask
GenerationAttempt
GenerationResult
```

Conceptual relationship:

```text
Production Context
↓
PromptInstance
↓
GenerationTask
↓
GenerationAttempt
↓
GenerationResult
↓
Artifact
```

One task MAY contain several attempts.

One successful attempt MAY produce one or more artifacts.

---

# 5.8 Workflow Domain

Core entities:

```text
Workflow
WorkflowVersion
```

Workflow represents logical generation intent.

WorkflowVersion represents an immutable executable definition.

GenerationTask MUST reference the exact WorkflowVersion used.

---

# 5.9 Continuity Domain

Primary conceptual entity:

```text
ContinuityState
```

ContinuityState describes relevant world state before, during, or after production units.

Possible information:

```text
character wardrobe
character position
character emotion
character injuries
held props
object placement
location condition
weather
time
lighting
environmental changes
```

Example:

```text
Shot 20
↓
Ending Continuity State
↓
Shot 21
```

Continuity MAY later be represented with more granular structured entities.

---

# 5.10 Quality Domain

Core entities:

```text
QCMetric
QCResult
ReviewDecision
```

Potential metrics:

```text
character_consistency
wardrobe_consistency
style_consistency
continuity
prompt_alignment
composition
visual_quality
artifact_detection
storyboard_diversity
motion_quality
audio_quality
```

A QCResult SHOULD identify:

```text
artifact
metric
score or result
method
model if automated
threshold
decision
timestamp
reviewer if manual
```

---

# 5.11 Artifact Domain

Conceptual structure:

```text
Artifact
├── id
├── type
├── storage_key
├── mime_type
├── size
├── checksum
├── width
├── height
├── duration
├── metadata
├── created_at
└── provenance
```

Potential artifact types:

```text
source_document
reference_image
character_reference
location_reference
storyboard_image
generated_image
generated_video
voice_audio
music
sound_effect
subtitle
workflow_file
prompt_export
QC_report
episode_export
project_export
```

Artifact taxonomy SHOULD remain extensible.

---

# 5.12 Entity Identity

Database identity SHOULD use UUIDs.

Human-readable production identifiers SHOULD exist separately.

Example:

```text
Database ID:
550e8400-e29b-41d4-a716-446655440000

Production Code:
EP01_SC03_SH012
```

Production codes MUST NOT serve as database primary keys.

---

# 5.13 Versioning Principle

Any object that materially changes AI output SHOULD be considered for versioning.

Examples:

```text
CharacterVersion
LocationVersion
StyleVersion
VoiceVersion
PromptTemplateVersion
WorkflowVersion
```

Generation records MUST preserve the exact versions used during execution.

---

# 6. Production Hierarchy

## 6.1 Canonical Hierarchy

The initial canonical hierarchy is:

```text
Project
└── Story
    └── Episode
        └── Scene
            └── Shot
```

This hierarchy represents production ownership.

Additional planning layers MAY exist without changing this canonical structure.

---

# 6.2 Story

Story represents the canonical narrative source.

Possible sources:

```text
original writing
novel
short story
screenplay
outline
AI-generated story
imported source material
```

Story may contain:

```text
title
summary
genre
theme
world setting
main conflict
source content
adaptation settings
```

---

# 6.3 Episode

Episode represents a distributable narrative unit.

Possible fields:

```text
title
episode number
summary
target duration
opening hook
ending hook
status
```

---

# 6.4 Scene

Scene represents a coherent dramatic unit.

A Scene generally maintains continuity of:

```text
location
time
dramatic objective
participating characters
```

Example:

```text
EP01_SC03

Location:
School hallway

Time:
Night

Purpose:
The protagonist discovers the hidden letter.
```

---

# 6.5 Scene Planning

A Scene MAY exist before its final Shots exist.

The planning process SHOULD support:

```text
Scene
↓
Scene Interpretation
↓
Dramatic Beats
↓
Shot Planning
↓
Storyboard
↓
Human Review
↓
Approved Shot List
```

AI agents may assist this process in future versions.

---

# 6.6 Shot

Shot is the primary audiovisual production unit.

A Shot represents one continuous camera presentation.

Conceptually:

```text
Shot
├── Narrative Intent
├── Characters
├── Environment
├── Action
├── Composition
├── Camera
├── Dialogue
├── Audio Intent
├── Continuity
├── Prompt Context
├── Generation
└── QC
```

---

# 6.7 Shot Responsibilities

A Shot SHOULD contain or reference enough structured information to support independent production.

Minimum conceptual information:

```text
scene
shot order
action
characters
location
camera
duration
```

Extended information may include:

```text
emotion
dialogue
props
lighting
weather
time
composition
camera movement
visual style
continuity
audio intent
generation overrides
```

---

# 6.8 Camera Data

Camera-related data may include:

```text
shot size
camera angle
camera height
camera movement
lens intent
focal length where appropriate
framing
subject placement
depth of field intent
focus target
```

Camera terminology SHOULD eventually be normalized through a dedicated Cinematography / Shot Specification.

---

# 6.9 Conceptual Shot Example

```json
{
  "code": "EP01_SC03_SH012",

  "characters": [
    {
      "character": "CHAR_001",
      "version": "v3",
      "position": "frame_left",
      "emotion": "shocked"
    }
  ],

  "location": {
    "id": "LOC_004",
    "version": "v2"
  },

  "action": "The protagonist slowly turns toward the door.",

  "camera": {
    "shot_size": "medium_close_up",
    "angle": "eye_level",
    "movement": "slow_push_in",
    "lens_mm": 50
  },

  "lighting": {
    "type": "warm_sunset",
    "direction": "window_left"
  },

  "dialogue": "Who is there?",

  "duration_seconds": 4.2,

  "continuity": {
    "previous_shot": "EP01_SC03_SH011"
  }
}
```

This is an architectural example only.

It is NOT the final API schema.

Final definitions require dedicated:

```text
Django Models
Pydantic Schemas if required
DRF Serializers
JSON Schema
API Contracts
```

---

# 7. Storyboard Architecture

## 7.1 Storyboard Role

Storyboard is a first-class planning and review stage.

Storyboard MUST NOT be treated only as generated preview images.

The storyboard stage helps validate:

```text
shot selection
composition
camera language
character placement
scene coverage
visual diversity
continuity
narrative clarity
production feasibility
```

---

# 7.2 Storyboard Pipeline

Recommended conceptual pipeline:

```text
Scene
↓
Scene Analysis
↓
Shot Plan
↓
Storyboard Plan
↓
Storyboard Generation
↓
Storyboard QC
↓
Human Review
↓
Approved Storyboard
↓
Production Generation
```

---

# 7.3 Storyboard Data

Future storyboard structures may require:

```text
Storyboard
StoryboardVersion
StoryboardFrame
ShotPlan
ShotPlanVersion
```

These names are provisional.

A dedicated Storyboard Specification MUST determine the final domain model.

---

# 7.4 Storyboard QC

Potential storyboard quality criteria include:

```text
narrative coverage
scene diversity
camera diversity
composition quality
character consistency
location consistency
action clarity
continuity
shot redundancy
prompt alignment
```

Research benchmarks MAY influence the final definitions.

---

# 8. Prompt Architecture

## 8.1 Prompt Construction

Prompts SHOULD be assembled from structured system information.

Example:

```text
Shot Data
+
Character Version
+
Location Version
+
Style Version
+
Continuity State
+
Production Knowledge
+
Prompt Template Version
+
Workflow Requirements
+
Provider Requirements
↓
PromptInstance
```

Prompt text SHOULD NOT be treated as the primary source of truth for production intent.

Structured production data remains authoritative.

---

# 8.2 PromptTemplate

PromptTemplate describes reusable prompt construction rules.

PromptTemplate SHOULD be versionable.

---

# 8.3 PromptInstance

PromptInstance represents the resolved prompt used for a specific generation request.

It SHOULD preserve:

```text
template version
resolved values
rendered prompt
negative prompt if applicable
production context
creation timestamp
```

---

# 9. Workflow Architecture

## 9.1 Workflow

Workflow represents a logical production procedure.

Examples:

```text
Character Concept Generation
Character Reference Generation
Storyboard Image Generation
Final Image Generation
Image-to-Video Generation
Voice Generation
Upscale
Lip Sync
QC Evaluation
```

---

# 9.2 WorkflowVersion

WorkflowVersion represents an immutable executable workflow definition.

It SHOULD contain or reference:

```text
workflow configuration
provider
input schema
parameter mappings
output definitions
model requirements
validation rules
```

---

# 9.3 Workflow Immutability

A WorkflowVersion used by a GenerationTask MUST NOT be silently modified.

Changes require a new version.

---

# 10. Generation Architecture

## 10.1 GenerationTask

GenerationTask represents requested work.

Possible task states:

```text
PENDING
QUEUED
RUNNING
SUCCEEDED
FAILED
CANCELLED
```

Exact state definitions require a later Generation Specification.

---

# 10.2 GenerationAttempt

GenerationAttempt represents one execution attempt.

Retrying a task SHOULD create a distinct attempt record.

This enables:

```text
debugging
error analysis
provider comparison
retry history
cost tracking
performance analysis
```

---

# 10.3 GenerationResult

GenerationResult describes the outcome of an attempt.

A result MAY reference:

```text
one artifact
multiple artifacts
provider metadata
execution metrics
error details
```

---

# 11. Provider Architecture

## 11.1 Provider Boundary

Provider code MUST isolate vendor-specific or engine-specific implementation.

Example:

```text
Domain / Application Layer
        ↓
Provider Interface
        ↓
ComfyUIProvider
OpenAIProvider
KlingProvider
VeoProvider
LocalProvider
```

---

# 11.2 Provider Responsibilities

A provider may handle:

```text
authentication
request formatting
workflow submission
job polling
provider errors
response normalization
artifact download
provider metadata
```

Providers SHOULD NOT decide narrative intent or production semantics.

---

# 12. Continuity Architecture

## 12.1 Purpose

Continuity ensures that changes between Shots are intentional.

Continuity includes:

```text
character identity
wardrobe
hair
props
injuries
character position
object placement
environment
lighting
weather
time
scene damage
```

---

# 12.2 Continuity Flow

Conceptual relationship:

```text
Shot N
↓
Ending State
↓
Continuity Transition
↓
Shot N+1 Starting State
```

---

# 12.3 Future Continuity Automation

Later systems may support:

```text
continuity extraction
continuity comparison
visual continuity detection
continuity warnings
automatic continuity prompts
```

---

# 13. Artifact and Provenance Architecture

## 13.1 Fundamental Rule

> A generated production artifact must never exist without identifiable provenance.

The system MUST be able to determine, where applicable:

```text
what was generated
why it was generated
which production object requested it
which assets were used
which asset versions were used
which prompt was used
which workflow version was used
which provider was used
which model was used
which parameters were used
which attempt created it
when it was generated
```

---

# 13.2 Purpose of Provenance

Provenance enables:

```text
debugging
regeneration
QC
workflow comparison
model comparison
cost analysis
production auditing
research
performance analysis
```

---

# 13.3 Imported Artifacts

Imported media MUST also record origin where available.

Possible origin types:

```text
uploaded
generated
derived
external_reference
exported
```

---

# 14. Research Library

## 14.1 Purpose

The Research Library exists to prevent architectural design from relying only on intuition or chat history.

It serves as the research foundation for:

```text
domain design
AI architecture
production modeling
workflow architecture
QC design
provider design
data structures
future automation
```

---

# 14.2 Research Categories

```text
AI Research Papers
Official Technical Docs
Film Production Standards
Animation Production
Open Source Projects
Benchmarks & Datasets
Architecture References
```

---

# 14.3 Research Source Record

Each significant source SHOULD eventually receive a structured research note.

Recommended format:

```text
Source
├── Title
├── Authors / Organization
├── Date
├── URL / Identifier
├── Source Type
├── Reliability Tier
├── Problem
├── Method
├── Data Structure
├── Pipeline
├── Evaluation Metrics
├── Limitations
├── Relevant Findings
├── What We Can Reuse
├── What We Should Not Copy
├── Impact on AI Drama System
└── Related Specifications / ADRs
```

---

# 14.4 Source Tiers

## Tier A — Primary / Authoritative

Examples:

```text
primary research papers
official documentation
standards
official technical specifications
```

Tier A SHOULD be preferred for important technical decisions.

---

## Tier B — Professional / Industry

Examples:

```text
professional production documentation
recognized film-production references
recognized animation pipelines
established engineering references
vendor architecture guides
```

Tier B MAY support architecture and domain modeling.

---

## Tier C — Supporting / Exploratory

Examples:

```text
engineering blogs
tutorials
conference notes
community discussions
Reddit
secondary analysis
videos
```

Tier C is useful for discovery and practical experience.

Tier C SHOULD NOT normally be the sole source for critical architectural decisions.

---

# 14.5 Research Library v1.0 Target

The first Research Library SHOULD contain approximately:

```text
20–30 high-quality sources
```

distributed across:

```text
AI narrative generation
character consistency
storyboard generation
long-form visual consistency
cinematography
storyboarding
animation pipeline
AI workflow engineering
official backend documentation
open-source AI production tools
benchmarks
```

---

# 15. Source of Truth Policy

## 15.1 Principle

Important architectural design SHOULD have an identifiable Source of Truth.

This does not mean every field requires an academic citation.

It means significant decisions SHOULD be defensible.

---

# 15.2 Preferred Evidence Order

When evaluating an architectural decision:

```text
Official Standard / Official Documentation
        ↓
Primary Research
        ↓
Established Production Practice
        ↓
Maintained Open-Source Implementation
        ↓
Professional Engineering Reference
        ↓
Community Experience
        ↓
Unverified Opinion
```

The order may differ depending on the question.

---

# 15.3 Research Does Not Override Product Requirements

External research informs the system.

It does not automatically dictate the system.

The final decision must consider:

```text
product requirements
technical constraints
MVP scope
maintainability
provider limitations
cost
development capacity
future extensibility
```

---

# 16. Architecture Decision Records

## 16.1 ADR Requirement

Important decisions SHOULD receive an Architecture Decision Record.

Examples:

```text
Why Shot is the main production unit
Why assets are versioned
Why ComfyUI is behind a provider abstraction
Why object storage is used
Why UUIDs are database identities
Why Celery is used
Why Storyboard is a separate planning stage
```

---

# 16.2 ADR Structure

Recommended ADR format:

```text
Title
Status
Date
Context
Decision
Alternatives Considered
Rationale
Consequences
Sources
Related Specifications
```

---

# 16.3 ADR Lifecycle

Possible ADR states:

```text
Proposed
Accepted
Superseded
Deprecated
Rejected
```

Accepted ADRs SHOULD NOT be silently rewritten to represent a new decision.

A new decision should supersede the previous ADR.

---

# 17. Research-to-Implementation Traceability

The preferred chain is:

```text
Source
↓
Research Note
↓
Finding
↓
Requirement
↓
Domain Specification
↓
ADR where required
↓
Implementation
↓
Tests
```

Example:

```text
Character consistency research
↓
Characters require stable identity and versioned references
↓
Character Asset Specification
↓
ADR: Character identity/version architecture
↓
Django models
↓
Generation workflow
↓
Consistency tests
```

---

# 18. Development Process

## 18.1 Documentation-Driven Development

The project SHOULD use documentation-driven development.

Recommended cycle:

```text
Development Specification
        ↓
Research
        ↓
Domain Specification
        ↓
ADR
        ↓
Small Implementation PR
        ↓
Tests
        ↓
Review
        ↓
Update Documentation
        ↓
Next Specification
```

---

# 18.2 Small PR Principle

AI coding agents SHOULD work through small, reviewable changes.

A PR SHOULD generally solve one coherent technical objective.

Avoid:

```text
implement whole backend
create every model
build entire provider layer
complete entire frontend
```

Prefer:

```text
Create Project domain model
Add Project API
Add Project tests
Add Project documentation
```

then continue.

---

# 18.3 Specification Before Implementation

For important domains:

```text
Research
↓
Specification
↓
ADR if necessary
↓
Implementation
```

Examples that SHOULD receive dedicated specifications:

```text
Character Asset
Location Asset
Shot
Storyboard
Continuity
Generation Task
Workflow
Artifact
QC
Prompt Engine
Knowledge DB
```

---

# 18.4 Chat Is Not the Source of Truth

Important decisions SHOULD be moved from conversational discussion into the repository.

The repository SHOULD become the durable project memory.

Preferred locations:

```text
DEVELOPMENT_SPEC.md
domain specifications
ADRs
research notes
README
AGENTS.md
Copilot instructions
tests
code
```

---

# 19. Agent and Copilot Development Rules

## 19.1 AGENTS.md

`AGENTS.md` SHOULD define project-wide rules for human and AI contributors.

It may contain:

```text
architecture principles
development workflow
coding expectations
testing rules
documentation requirements
forbidden shortcuts
provider abstraction requirements
```

---

# 19.2 Repository Copilot Instructions

Repository-wide Copilot instructions SHOULD be placed in:

```text
.github/copilot-instructions.md
```

Path-specific instructions MAY be placed under:

```text
.github/instructions/
```

Possible files:

```text
django.instructions.md
tests.instructions.md
providers.instructions.md
docs.instructions.md
```

---

# 19.3 AI Agent Rule

Coding agents MUST NOT invent major domain structures without checking the relevant specification.

When a specification does not exist for a significant domain concept, the preferred action is:

```text
identify missing specification
↓
research
↓
write specification
↓
implement
```

rather than silently inventing architecture inside a PR.

---

# 20. Architectural Invariants

The following rules are considered system invariants unless superseded through an ADR.

### Invariant 1

Business logic MUST NOT depend directly on specific AI providers.

### Invariant 2

Generation workflows MUST be versionable.

### Invariant 3

Generated production artifacts MUST retain provenance.

### Invariant 4

Assets that materially influence generation SHOULD be versionable.

### Invariant 5

Historical generation records MUST NOT silently change when assets or workflows are updated.

### Invariant 6

Production intent SHOULD exist as structured domain data rather than only inside prompts.

### Invariant 7

Storyboard is a production-planning and review stage.

### Invariant 8

Research Library and runtime Production Knowledge are separate concepts.

### Invariant 9

Important architectural decisions SHOULD be captured in repository documentation.

### Invariant 10

AI agents MUST work against explicit specifications rather than using chat history as the only architectural source.

---

# 21. Immediate Specification Roadmap

Following Development Specification v0.2, recommended specification order is:

```text
01. Research Library Specification
        ↓
02. Project Domain Specification
        ↓
03. Story / Episode / Scene Specification
        ↓
04. Character Asset Specification
        ↓
05. Shot Specification
        ↓
06. Storyboard Specification
        ↓
07. Artifact & Provenance Specification
        ↓
08. Workflow Specification
        ↓
09. Generation Task Specification
        ↓
10. Provider Architecture Specification
        ↓
11. Continuity Specification
        ↓
12. QC Specification
        ↓
13. Prompt Engine Specification
        ↓
14. Knowledge DB Specification
```

Some specifications MAY be reordered if implementation dependencies require it.

---

# 22. Recommended First Research Themes

Before finalizing several domain models, Research Library v1.0 SHOULD investigate:

```text
Character consistency
Character reference representation
Long-form visual consistency
Storyboard generation
Storyboard evaluation
Story-to-shot decomposition
Film scene and shot terminology
Character Bible design
Continuity tracking
Animation production pipeline
Asset management
AI workflow versioning
Generation provenance
AI QC metrics
```

---

# 23. Definition of Architectural Maturity

A domain is considered ready for implementation when the project has enough clarity around:

```text
Purpose
Responsibilities
Boundaries
Core entities
Relationships
Lifecycle
Versioning
Provenance
External dependencies
Research basis
Open questions
Testable requirements
```

Not every field must be known before implementation.

However, core identity and ownership boundaries SHOULD be understood before database models become difficult to change.

---

# 24. Final Architectural Position

AI Drama System should evolve according to the following relationship:

```text
Research
        ↓
Production Knowledge
        ↓
Development Specification
        ↓
Domain Specifications
        ↓
Architecture Decisions
        ↓
Structured Domain Model
        ↓
Workflow / Provider Infrastructure
        ↓
AI Generation
        ↓
QC
        ↓
Delivery
```

The central architectural idea is:

> AI generation is one component of the production system, not the production system itself.

The system should therefore prioritize:

```text
structured production data
reusable assets
versioned workflows
traceable generation
continuity
reviewability
research-grounded design
provider independence
```

over short-term convenience tied to a specific AI model.

---

# End of Development Specification v0.2
