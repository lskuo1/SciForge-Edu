# SciForge-Edu

Educational Question Asset Management
and Exam Generation System

## Quick Start

Environment setup:

See: docs/governance/environment_setup.md

Basic workflow:

1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run tests
5. Run example walkthroughs

```bash
# Setup and install packages
pip install -e .[dev]

# Execute test suite
pytest

# Run repository manager walkthrough
python examples/sample_repository_workflow.py

# Run end-to-end exam generation and TeX export walkthrough
python examples/generate_exam.py
```

---

## Project Status

Current stage:

Prototype/Pre-MVP Phase

Status:

- Architecture: Core design established (Parser -> Models -> Repository -> Renderer -> Export)
- Documentation: Core walkthroughs documented; detailed specification drafts in progress
- Core Engine: Implemented & Validated (Core schemas, parser, local database, reference rewriter, and text renderer are operational; validated in Sprint 002)
- GUI: Planned (Not implemented; package placeholders only)
- AI Features: Planned (Not implemented; conceptual specs only)

---

## Engineering Governance

The repository contains engineering documentation tracking developmental work and project status:

- **Contributor Guide** (`docs/governance/engineering_contributor_guide.md`): The canonical entry point for repository orientation, discovery, and navigation mapping.
- **Repository Audits** (`docs/audits/`): Reports documenting observations, architecture mismatches, and compliance audits (e.g. Sprint 001 audit).
- **Sprint Plans** (`docs/sprints/`): Documents outlining sprint goals, deliverables, and implementation schedules (e.g. Sprint 002 planning).
- **Change Governance** (`docs/governance/engineering_change_governance_policy.md`): Defines change classification tiers (Class A vs. Class B) and canonical Testing Impact Analysis (TIA-1 to TIA-5) required for behavior changes.
- **Templates** (`docs/templates/`): Standardization templates (e.g., `implementation_plan_template.md`) used to structure engineering change contracts.

### Change Classification Model

Every repository change must be triaged into one of two tiers:

* **Class A: Behavior-Preserving Change**
  * **When to use**: Applied when the externally observable behavior of the repository remains completely unchanged.
  * **Examples**: Documentation, code comments, formatting, typo corrections, or internal refactoring with zero contract or logic output changes.
  * **Requirement**: Record a brief engineering rationale explaining why behavior is preserved.
* **Class B: Behavior-Changing Change**
  * **When to use**: Applied when the externally observable behavior of the repository may change.
  * **Examples**: Public API changes, parser regex behavior changes, repository workflow modifications, data model schema changes, user-visible output format changes, and semantic logic adjustments.
  * **Requirement**: Perform a complete, canonical Testing Impact Analysis (TIA) before implementation.

### Testing Impact Analysis (TIA)

The purpose of Testing Impact Analysis (TIA) is to ensure that every behavior-changing (Class B) modification is explicitly analyzed from a testing perspective prior to implementation. By forcing contributors to explicitly map new behaviors to test coverage, we avoid untested code paths, prevent silent regressions, and make engineering decisions regarding tests explicit rather than implicit.

All Class B changes must answer the five canonical TIA questions:
1. **TIA-1**: What behavior is changing?
2. **TIA-2**: Which existing tests currently verify this behavior?
3. **TIA-3**: Are the existing tests sufficient?
4. **TIA-4**: If not, why are they insufficient?
5. **TIA-5**: **Engineering Decision** (Choose exactly one: *Existing tests are sufficient*, *Existing tests require modification*, *New tests are required*, or *No applicable tests exist*) with an explicit engineering rationale.

### Contributor Governance Workflow

Every repository contribution must progress through the following sequential stages:

1. **Sprint Planning**: The sprint goals, scope, and deliverables are defined in a Sprint Plan document (within `docs/sprints/`).
2. **Execution Contract (Implementation Plan)**: Before writing code, the contributor creates an Implementation Plan using the template in `docs/templates/implementation_plan_template.md`. For each task, the contributor triages the change class (Class A or Class B) and documents the corresponding rationale or TIA answers. This document is reviewed and approved as the Execution Contract.
3. **Implementation**: The contributor writes the code and tests in strict compliance with the approved Execution Contract. If deviations are necessary, coding stops, and the contract must be revised and re-approved before proceeding.
4. **Verification**: Independent or automated validation (such as running the test suite via `pytest` and auditing document consistency) is performed to confirm correctness and ensure no regression has occurred.
5. **Retrospective**: After implementation is verified and merged, a retrospective is conducted to capture learnings and address any process improvements or gaps.

---

## Project Philosophy

System may:

- suggest
- analyze
- prepare

Human must:

- review
- approve
- decide

Generated content must preserve provenance.

Implementation follows architecture.

---

## Repository Structure

project/

├── README.md
├── CHANGELOG.md
├── docs/
├── src/
├── templates/
├── assets/
└── tests/

---

## Documentation Reading Order

Current draft documents:

1. docs/draft/documentation_policy_*.md

2. docs/draft/architecture_map_*.md

3. docs/draft/data_model_spec_*.md

4. docs/draft/provenance_spec_*.md

5. docs/draft/repository_spec_*.md

6. docs/draft/parser_grammar_spec_*.md

7. docs/draft/gui_workflow_spec_*.md

8. docs/draft/template_api_spec_*.md

9. docs/draft/import_pipeline_spec_*.md

10. docs/draft/sandbox_compile_spec_*.md

11. docs/draft/implementation_roadmap_*.md

---

## Development Order

Architecture

↓

Core Engine

↓

Workflow

↓

GUI

↓

AI

Never reverse this order.

---

## Current Phase

Phase 1: Core Data Engine & Basic Compilers

Implemented & Validated:
- Question, Choice, Solution, Provenance, and Source Pydantic models
- Local repository manager and JSON index projections (validated via workflow roundtrip)
- Exam composer (Score grouping primitives)
- Renderer pipeline (Namespace assigner, reference rewriter, and template manager)
- Workspace exporter (student/teacher TeX documents export)

Planned:
- LaTeX PDF compilation service
- Sandbox compilation environment
- QuestionGroup source parsing and rendering
- UI/GUI exam builder and repository browser

