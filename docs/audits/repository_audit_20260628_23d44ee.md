# Repository Reality Audit

Version: 1.0

Status: Draft

---

# Purpose

This template defines the standard format for auditing a software repository.

The objective of a repository audit is to describe the current reality of the repository, identify gaps between the current state and the intended architecture, and recommend the next engineering priorities.

An audit records observations.

It should not directly modify the repository.

---

# Audit Metadata

Repository: SciForge-Edu

Audit Date: 2026-06-28

Repository Commit: 23d44eeb984e93df7193875da646d04f3e29928

Auditor: Antigravity AI Coding Assistant

Audit Version: 1.0

Knowledge Kernel Version: Gemini 3.5 Flash (Medium) / Antigravity 2.0

---

# 1. Executive Summary

Provide a concise summary of the repository.

Include:

* **Overall repository maturity**: Prototype/pre-MVP. The repository implements core Pydantic data models, a regex-based parser, local JSON repository database, score grouping, reference rewriting, and basic LaTeX export of student/teacher files, but lacks integration of core rendering modules, XeLaTeX PDF generation, GUI, and import capabilities.
* **Overall architectural quality**: Clean, decoupled, layered design. Data models (`src/models`) are centralized. Parser (`src/parser`), repository manager (`src/repository`), and rendering services (`src/renderer`) operate as distinct components. However, several modules (resource collector, asset packager, and export manager) are currently isolated and not integrated into the end-to-end compilation flow.
* **Overall documentation quality**: Poor to fair. There is an abundance of written specifications and draft design documents, but they are highly outdated, contradictory, and suffer from major implementation drift. Many specs are written as if features are already completed (e.g. GUI, PDF compilation, advanced search queries) which are completely absent in code.
* **Major strengths**: Robust Pydantic domain models; deterministic content-based question ID generation; clean LaTeX label and cross-reference rewriting pipeline; extensive unit test coverage (33 test files covering most implemented classes).
* **Major risks**: Broken packaging configuration (`pyproject.toml` is missing mandatory PEP 621 fields like `name` and `version`, failing editable installations); broken example script (`examples/sample_repository_workflow.py` uses obsolete APIs and throws runtime errors); massive documentation drift that can mislead new developers or AI agents.

---

# 2. Repository Purpose

Describe the current purpose of the repository.

Questions:

* **What problem is the repository solving?**
  The repository is designed to build a software system that manages educational question assets (LaTeX/Markdown question fragments, choices, solutions, provenance metadata) and generates formatted exams. It automates assigning temporary namespaces to question labels, rewriting internal references, grouping questions based on score rules, and exporting teacher and student LaTeX documents.
* **What development phase is it currently in?**
  The project is in the Prototype/Pre-MVP development phase. Work is actively occurring on the `exam/first-end-to-end-demo` branch.
* **Does the current implementation match the stated purpose?**
  Partially. The core data models and basic parser, repository search/persistence, score grouping, reference rewriting, and output rendering function end-to-end to export TeX files. However, the repository contains many specifications for a Tkinter GUI, sandbox PDF compilation, similarity detection, AI processing, and advanced metadata search filters, none of which exist in the current implementation.

---

# 3. Repository Structure

Describe the current repository organization.

Evaluate:

* **directory structure**: The repository is well-organized. The top-level folders include `src/` (production source code), `tests/` (unit and integration tests), `docs/` (architecture decisions, audits, and drafts), `examples/` (scripts demonstrating system workflows), `templates/` (base LaTeX template files), `scripts/` (development workflow utilities), and `build/` (generated export outputs).
* **naming consistency**: High naming consistency across the codebase. Test files in the `tests/` directory mirror the modules in `src/` (e.g., `tests/test_renderer_compiler.py` directly corresponds to `src/renderer/compiler.py`).
* **separation of concerns**: Strong separation of concerns. Production logic is separated into independent packages: `src/models` houses pure data schemas; `src/parser` handles raw text matching; `src/repository` implements persistence/indexing; `src/renderer` handles namespace assignments and TeX AST-like label rewriting; and `src/workspace` manages the actual export orchestration.
* **discoverability**: Discoverability is generally good due to logical module division. However, discoverability of active versus planned features is obscured because the `docs/draft/` folder contains dozens of proposed specifications mixed with active designs.

---

# 4. Documentation Reality

Review all important documentation.

Identify:

* **canonical documents**:
  - `docs/governance/environment_setup.md` (environment install steps)
  - `docs/api_snapshot.md` (Pydantic model fields snapshot)
  - `docs/architecture_decisions/ADR-DOC-001-documentation-must-be-ai-transferable.md` (ADR asserting documentation structure)
* **duplicated documents**:
  - *LaTeX Question Grammar*: `docs/authoring/question_authoring_spec_v1.md`, `docs/draft/question_grammar_v0.1.md`, `docs/draft/question_group_spec_v1.0.md`, and `docs/authoring/ai_prompt_library_v1.md` all duplicate and conflict on LaTeX syntax definitions and constraints.
  - *Audits & Status*: `docs/current_system_audit_v0.1.md`, `docs/current_system_audit_v0.2.md`, and `docs/current_system_audit_v0.3.md` duplicate review notes, often conflating the legacy system with the current package.
  - *Roadmaps*: `docs/draft/implementation_roadmap_v1.0.md` and `docs/draft/development_roadmap_v0.1.md` provide overlapping and contradictory timelines.
  - *Policies*: `docs/draft/documentation_policy_v1.0.md` and `docs/draft/documentation_policy_v1.1.md`.
* **outdated documents**:
  - `README.md` (claims "Core engine: not implemented", when it is implemented).
  - `docs/current_status.md` (claims query v1 is implemented with filters `subject`, `chapter`, `difficulty_level`, and `tags`, none of which are supported in code. Last updated May 27, 2026).
  - `CHANGELOG.md` (stops at early model commits, omitting all parser, repository, renderer, and export updates).
  - `docs/draft/parser_grammar_spec_v1.0.md` (describes an AST/lexer parser with strict validation that doesn't match the regex parser).
* **missing documents**:
  - Missing build and compiler dependencies instructions (e.g. XeLaTeX installation and requirements).
  - Missing guidelines on how to run and validate the end-to-end rendering pipeline.
  - `docs/draft/question_source_format_v0.1.md` is empty (0 bytes).

---

# 5. Implementation Reality

Describe the current implementation.

Examples:

* **implemented modules**:
  - `src/models/`: `question.py`, `choice.py`, `solution.py`, `analysis.py`, `version.py`, `source.py`, `provenance.py`, `question_group.py`, `exam_question_instance.py`, and `exam_section.py`.
  - `src/parser/question_parser.py`: Regex-based parser to extract question items, choices, solutions.
  - `src/repository/`: local filesystem database persistence (`manager.py`, `index.py`).
  - `src/renderer/`: namespace assigner (`namespace_assigner.py`), label/reference rewriter (`reference_rewriter.py`), template text replacement engine (`exam_package_renderer.py`).
  - `src/utils/question_id.py`: deterministic 16-character SHA-256 ID generator.
* **experimental/isolated modules** (implemented but not integrated into main flow):
  - `src/renderer/asset_packager.py` and `src/renderer/resource_collector.py` (models and copy operations for assets but not called by `RenderPipeline` or `ExamExport`).
  - `src/renderer/compiler.py` (performs formatting using `str.format()` but does not execute external LaTeX compilation).
  - `src/renderer/export_manager.py` (models output bundles but bypassed by `ExamExport`).
  - `src/repository/usage.py` (usage models exist but are never loaded/saved).
* **unfinished components** (placeholders only):
  - `src/gui/__init__.py` (empty)
  - `src/importer/__init__.py` (empty)
  - `src/diagnostics/__init__.py` (empty)
* **deprecated components**:
  - Legacy Tkinter desktop app and LaTeX/XeLaTeX generation code exist only in `archive/legacy/ExamGenerationSystem_v0.6.zip`.

---

# 6. Documentation Drift

Identify differences between:

Documentation

↓

Implementation

Examples include:

* **outdated documentation**:
  - `README.md` states the core engine is unimplemented.
  - `docs/current_status.md` states the query system supports searching by `subject`, `chapter`, `difficulty_level`, and `tags`, whereas `RepositoryManager.search` strictly accepts only `uuid` and `question_type`.
  - `CHANGELOG.md` fails to log any renderer, parser, repository, or export work.
* **undocumented implementation**:
  - The high-level orchestration pipeline `ExamRenderService` and `examples/generate_exam.py` are completely undocumented.
  - Composition models like `ExamQuestionInstance` and `ExamSection`, along with score grouping logic, are not documented in top-level files.
* **conflicting descriptions**:
  - **Parser Strictness**: `docs/draft/parser_grammar_spec_v1.0.md` requires strict validation and failing on errors. However, the parser is implemented using permissive regexes and explicitly tested to accept multiple correct choices (`test_parse_multiple_correct_choices`) and missing solutions (`test_parse_missing_solution`), violating the grammar constraints.
  - **QuestionGroup Syntax**: `question_grammar_v0.1.md` and `question_group_spec_v1.0.md` define conflicting LaTeX environments for question groups (e.g. `\begin{groupstem}` vs `\groupstem{}`), neither of which is implemented in `QuestionParser`.
  - **Onboarding Executable**: `examples/sample_repository_workflow.py` uses obsolete constructors like `Choice(key, content)` and queries like `search(subject="physics")`, causing instant runtime failures when executed.
  - **Template placeholders**: The base template `templates/midterm_base.tex` has a placeholder `[[ full_instruction_content ]]` which is never replaced by the export logic and remains unresolved in output files.

---

# 7. Architecture Gaps

Identify architectural weaknesses.

Examples:

* **missing models**: A high-level `Exam` or `ExamPaper` model that controls layout options, instruction content, and version settings (A/B papers) is absent; code passes raw lists of questions.
* **missing specifications**: Lack of an integrated specification for how assets, image resources, templates, and compilation subprocesses are orchestrated into a single compiled artifact.
* **missing governance**: The pre-commit check script prints formatting/suffix warnings but does not enforce compliance or prevent committing; lacks CI configuration (e.g., GitHub Actions).
* **duplicated responsibilities**: The repository implements two disconnected templating mechanisms: `ExamCompiler` uses Python's `{}` formatting, while `ExamPackageRenderer` uses literal `[[ key ]]` replacement.
* **unclear ownership**: The boundary between resource copying (`ResourceCollector` in renderer) and workspace management (`ExamExport`) is unclear, leaving resource packaging unused.

---

# 8. Knowledge Gaps

Identify engineering knowledge that is currently not preserved inside the repository.

Examples:

* **design decisions**: No record explaining why a regex-based parser was chosen over a formal lexer/parser, or why `[[ token ]]` text substitution was favored over a standard templating engine like Jinja2.
* **architectural rationale**: No explanation for why critical components like `ResourceCollector` and `AssetPackager` remain disconnected from the core rendering pipeline.
* **workflow knowledge**: No documentation regarding XeLaTeX/PDF compiler requirements, or instructions on how to compile exported TeX files locally.
* **AI conversation knowledge**: Prompts inside `docs/authoring/ai_prompt_library_v1.md` assume unimplemented features (like question groups and strict validation), indicating that the AI assistant's context is out-of-sync with the actual codebase.

---

# 9. Priority Recommendations

Classify recommendations.

## P0

Critical.

Must be addressed immediately.

1. **Fix pyproject.toml**: Add mandatory `name` and `version` fields under `[project]` to restore support for editable installations (`pip install -e .[dev]`).
2. **Fix onboarding script**: Refactor `examples/sample_repository_workflow.py` to use correct constructors (e.g., `Choice(text_tex="...", is_correct=True)`) and query methods, ensuring developer onboarding is functional.
3. **Update README.md**: Align the "Project Status" section to indicate that the core engine, parser, repository, and renderer are implemented.
4. **Correct current_status.md**: Remove false claims regarding the active search filters in the query system.

---

## P1

Important.

Should be addressed in the next sprint.

1. **Implement missing search filters**: Add support for `subject`, `chapter`, `difficulty_level`, and `tags` queries inside `RepositoryManager.search` to align the code with documentation.
2. **Integrate asset and resource collection**: Update `RenderPipeline` and `ExamExport` to invoke `ResourceCollector` and `AssetPackager` to ensure exported exams package their referenced images.
3. **Unify templating mechanisms**: Standardize on a single template class/engine instead of having duplicate mechanisms in `ExamCompiler` and `ExamPackageRenderer`.
4. **Implement basic QuestionGroup parsing**: Add support to `QuestionParser` to parse shared stems and child questions.

---

## P2

Long-term improvements.

1. **Add XeLaTeX PDF compilation**: Implement a local compiler service to compile exported TeX files into PDFs.
2. **Implement sandbox compilation**: Build a secure execution sandbox for compiling student/teacher TeX documents.
3. **Implement answer table generation**: Add logic to generate student and teacher answer keys/sheets (`answers_table.tex`).

---

# 10. Recommended Next Sprint

Define:

**Sprint Goal**: Stabilize environment installation, restore onboarding workflow compatibility, and resolve critical query/template documentation drift.

**Deliverables**:

1. Valid PEP 621-compliant `pyproject.toml`.
2. Fully executable `examples/sample_repository_workflow.py` matching current API.
3. Updated `README.md` and `docs/current_status.md` indicating accurate status.
4. Merged template substitute classes in `src/renderer`.

**Expected Validation**:

- Run `pip install -e .[dev]` successfully.
- Run `python examples/sample_repository_workflow.py` without errors.
- Verify `pytest` command runs and passes all tests.

---

# Audit Principles

A repository audit shall:

* describe reality rather than assumptions;
* distinguish observations from recommendations;
* avoid speculative conclusions;
* identify knowledge gaps explicitly;
* remain reproducible by different auditors.

---

# Output Naming

Audit instances should follow:

repository_audit_<YYYYMMDD>_<commit>.md

Example:

repository_audit_20260628_a439b22.md
