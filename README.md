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

- **Repository Audits** (`docs/audits/`): Reports documenting observations, architecture mismatches, and compliance audits (e.g. Sprint 001 audit).
- **Sprint Plans** (`docs/sprints/`): Documents outlining sprint goals, deliverables, and implementation schedules (e.g. Sprint 002 planning).

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

