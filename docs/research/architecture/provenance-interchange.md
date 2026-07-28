# RL-ARCH-PROV-001 - Provenance Interchange

## 1. Research Metadata

- Research ID: RL-ARCH-PROV-001
- Status: Research record (candidate-level only)
- Date: 2026-07-28
- Requested by: [docs/domain/shot.md](../../domain/shot.md) Section 28
- Scope: minimal provider-neutral provenance concepts across generation chain
- Constraint: W3C PROV and C2PA remain candidates (not adopted)

## 2. Research Question

What minimal provider-neutral provenance concepts could support:

Shot -> PromptInstance -> GenerationTask -> GenerationAttempt ->
GenerationResult -> Artifact

while distinguishing internal production provenance from external content
authenticity/verifiable provenance?

## 3. Standards Investigated

- W3C PROV family
  - PROV-Overview
  - PROV-DM
  - PROV-O
- C2PA specification and official ecosystem material

## 4. Findings

- [STANDARD-DEFINED] W3C PROV defines a core provenance model with Entity,
  Activity, Agent and relations such as used, wasGeneratedBy, wasDerivedFrom,
  wasAssociatedWith, wasAttributedTo, actedOnBehalfOf.
- [STANDARD-DEFINED] W3C PROV defines provenance as descriptions of entities,
  activities, and people/software involved in producing/influencing artifacts.
- [STANDARD-DEFINED] PROV supports qualification and bundles, enabling
  provenance-of-provenance and scoped records.
- [STANDARD-DEFINED] C2PA defines signed provenance manifests for content
  authenticity claims, assertions, ingredient lineage references, and validation
  outcomes within a trust model.
- [STANDARD-SPECIFIC] C2PA is focused on verifiable authenticity/credentialed
  assertions around content packages, not full internal production orchestration.
- [CROSS-STANDARD SUPPORT] Both PROV and C2PA support chain/lineage semantics,
  but with different primary goals (internal process semantics vs external
  verifiability and trust signaling).
- [INTERPRETATION] Internal generation workflow provenance maps naturally to PROV-
  like graph semantics; external publish/distribution authenticity maps naturally
  to C2PA-like signed assertion packaging.
- [OPEN QUESTION] Exact canonical identifier profile and cross-system ID binding
  policy remains unresolved.

## 5. Cross-standard Comparison

- W3C PROV:
  - Strength: neutral conceptual graph for process provenance and causality.
  - Limitation: does not by itself define cryptographic packaging/trust UX for
    external consumer verification workflows.
- C2PA:
  - Strength: signed manifest and verification status model for authenticity and
    tamper-evidence.
  - Limitation: does not by itself define full internal planning/task orchestration
    semantics of the Shot production lifecycle.
- Combined interpretation:
  - Internal provenance and external authenticity should be separated but linkable.

## 6. Stable Findings

- Stable finding A: Internal production provenance and external authenticity
  provenance are distinct concerns and should not be merged into one abstraction.
- Stable finding B: A minimal neutral internal model can be expressed with
  entity/activity/agent and typed relations across the generation chain.
- Stable finding C: External authenticity envelopes can remain optional,
  adapter-level outputs attached to selected artifacts.

## 7. Gaps

- Gap 1: Canonical internal identifier policy across Shot, task, attempt,
  artifact, and external manifest references.
- Gap 2: Required minimum retention/immutability policy for provenance records.
- Gap 3: Mapping policy between internal provenance graph fields and C2PA claim/
  assertion schema without leaking provider internals.

## 8. AI Drama System Implications

- Keep internal production provenance first-class and provider-neutral.
- Keep external authenticity credentials optional and profile-dependent.
- Preserve explicit boundary:
  AI Drama Domain -> Internal Contract -> Adapter/Interchange -> External Standard.
- Preserve generation chain traceability without forcing C2PA manifests for all
  internal artifacts.

## 9. Candidate Requirements

- CANDIDATE CR-ARCH-PROV-001: Define minimal internal provenance node/edge types
  for Shot, PromptInstance, GenerationTask, GenerationAttempt, GenerationResult,
  Artifact, and Actor roles.
- CANDIDATE CR-ARCH-PROV-002: Require immutable provenance event records for
  attempt/result transitions with timestamps and actor/process identity.
- CANDIDATE CR-ARCH-PROV-003: Support optional external authenticity packaging
  (for example C2PA-compatible export) as adapter output, not core domain shape.
- CANDIDATE CR-ARCH-PROV-004: Require bidirectional reference linking between
  internal artifact IDs and external manifest IDs when authenticity packaging is
  emitted.

## 10. Candidate ADR Questions

- CANDIDATE ADR-Q-ARCH-PROV-001: Should internal provenance be implemented as an
  explicit graph model or constrained relational event schema with graph views?
- CANDIDATE ADR-Q-ARCH-PROV-002: Which minimal fields are mandatory for
  reproducibility claims vs optional for compliance/audit profiles?
- CANDIDATE ADR-Q-ARCH-PROV-003: Under which product profiles is C2PA export
  mandatory, optional, or disallowed?

## 11. Open Questions

- How should revocation/update semantics for external authenticity manifests be
  reflected back into internal production review states?
- What is the minimum trust policy abstraction needed internally without coupling
  to one external trust framework?
- How should sensitive prompt/provider metadata be redacted while maintaining
  useful provenance explainability?

## 12. Official Sources

- W3C PROV Overview
  - Organization: World Wide Web Consortium (W3C)
  - URL: https://www.w3.org/TR/prov-overview/
  - Version: W3C Recommendation family overview
  - Accessed: 2026-07-28
- W3C PROV-DM
  - Organization: W3C
  - URL: https://www.w3.org/TR/prov-dm/
  - Version: W3C Recommendation
  - Accessed: 2026-07-28
- W3C PROV-O
  - Organization: W3C
  - URL: https://www.w3.org/TR/prov-o/
  - Version: W3C Recommendation
  - Accessed: 2026-07-28
- C2PA Specification
  - Organization: Coalition for Content Provenance and Authenticity (C2PA)
  - URL: https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html
  - Version: 2.2
  - Accessed: 2026-07-28
- Content Credentials overview
  - Organization: Content Credentials / C2PA ecosystem
  - URL: https://contentcredentials.org/
  - Version: N/A (overview site)
  - Accessed: 2026-07-28

Source-limit disclosure:
- This record does not claim that W3C PROV or C2PA is adopted by AI Drama System.
- All mappings are candidate interpretations requiring specification and ADR review.
