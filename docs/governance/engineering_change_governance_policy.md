# Engineering Change Governance Policy

## 1. Purpose

This document establishes the repository-level Engineering Change Governance policy for SciForge-Edu. Its goal is to ensure that every behavior-changing modification is explicitly analyzed from a testing perspective prior to implementation.

---

## 2. Context

SciForge-Edu is an educational question asset management and exam generation system that relies on robust data models, regex parsers, and LaTeX compilation logic. 

Historically, passing existing unit tests demonstrated that existing functionality was not broken, but it did not prove that newly introduced behaviors had been consciously analyzed from a testing perspective. To prevent untested code paths, silent regression of undocumented behaviors, and technical debt, every modification must undergo Testing Impact Analysis (TIA).

---

## 3. Decision

All changes to the repository must be triaged under the canonical Change Classification model and follow the canonical Testing Impact Analysis workflow.

### Change Classification Model

Every repository modification shall be classified into exactly one of the following categories:

#### Class A: Behavior-Preserving Change
* **Definition**: Externally observable behavior of the repository remains completely unchanged.
* **Examples**: Documentation updates, code comments, formatting edits, internal refactorings with zero contract or logic output changes, and typo corrections.
* **Requirement**: Record a brief engineering rationale explaining why behavior is preserved. Existing tests are considered sufficient.

#### Class B: Behavior-Changing Change
* **Definition**: Externally observable behavior of the repository may change.
* **Examples**: Public API changes, parser regex behavior changes, repository workflow modifications, data model schema changes, user-visible output format changes, and semantic logic adjustments.
* **Requirement**: Perform a complete canonical Testing Impact Analysis (TIA) before implementation begins.

---

### Canonical Testing Impact Analysis (TIA) Workflow

Every Class B change must explicitly answer the following five questions in its implementation plan before code is written:

1. **TIA-1**: What behavior is changing?
2. **TIA-2**: Which existing tests currently verify this behavior?
3. **TIA-3**: Are the existing tests sufficient?
4. **TIA-4**: If not, why are they insufficient?
5. **TIA-5**: **Engineering Decision** — Choose exactly one of the following options and provide an explicit engineering rationale:
   * *Existing tests are sufficient.*
   * *Existing tests require modification.*
   * *New tests are required.*
   * *No applicable tests exist.*

---

## 4. Rationale

Testing is an active design phase, not a passive completion gate. By forcing contributors to explicitly classify changes and evaluate testing impact *before* writing code, the repository ensures that:
* New behavior is consciously mapped to test assertions.
* Code review quality is improved, as reviewers can verify testing intent.
* Metrics-driven bureaucracy is avoided in favor of high-quality engineering reasoning.

---

## 5. Examples

### Class A Change Example
* **Action**: Fixing a spelling error in a comment within `src/models/question.py`.
* **Rationale**: The execution logic is unchanged. No new tests are needed.

### Class B Change Example
* **Action**: Adding a new metadata search filter to `RepositoryManager.search()`.
* **TIA-5 Decision**: *New tests are required.*
* **Rationale**: Adding search options introduces new observable search behaviors. A new test suite is needed to assert correct filtering on the new parameters.

---

## 6. Counter Examples

### Invalid Class A Triage
* **Action**: Changing a default parameter value in `src/renderer/compiler.py` but classifying it as Class A because "all tests still pass".
* **Rationale**: This is incorrect. Changing default parameters alters the observable compiler output, which makes it a Class B change requiring a full TIA.

### Incomplete Class B TIA-5
* **Action**: Recording a TIA-5 decision of "Existing tests are sufficient" without any rationale.
* **Rationale**: This is incorrect. Every decision must record a clear, explicit rationale explaining why existing tests are structurally sufficient to assert the new behavior.

---

## 7. Implications

* **PR Review Gate**: Pull Request reviewers must reject changes that lack completed Class A rationales or Class B TIAs in their plans.
* **Engineering Velocity**: Minor changes (Class A) remain fast and lightweight. Complex changes (Class B) require conscious thought before coding.
* **AI Collaboration**: AI coding assistants can read this policy to reconstruct and comply with the testing standards of the codebase during multi-session handoffs.

---

## 8. Open Questions

* There are currently no open questions blocking the execution of this governance policy.
