# SciForge-Edu Repository Reality Check v1.0

| Field | Value |
|---|---|
| Audit Date | 2026-06-27 |
| Repository Name | SciForge-Edu |
| Git Branch | `exam/first-end-to-end-demo` |
| Git Commit SHA | `a439b226286ca722709ff65d9f5a5abd7c160da8` |
| Git Short SHA | `a439b22` |
| Analyzer | OpenAI Codex (GPT-5) |
| Audit Type | Repository Reality Check v1.0 |
| Status | Draft |

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Current Architecture](#2-current-architecture)
3. [Documentation Accuracy](#3-documentation-accuracy)
4. [Documentation Inconsistencies](#4-documentation-inconsistencies)
5. [Code vs Documentation Mismatches](#5-code-vs-documentation-mismatches)
6. [Undocumented Implementations](#6-undocumented-implementations)
7. [Documented but Missing Implementations](#7-documented-but-missing-implementations)
8. [Tests vs Documentation](#8-tests-vs-documentation)
9. [Documentation Technical Debt](#9-documentation-technical-debt)
10. [Documentation Synchronization Priorities](#10-documentation-synchronization-priorities)
11. [Executive Findings](#11-executive-findings)

## Audit Scope and Method

The audit inventoried all repository files visible at the audited commit and inspected all substantive text/source artifacts: current Python sources, 33 test files, scripts, examples, LaTeX source and generated examples, configuration, IDE/cache metadata, every Markdown file, and the legacy application manifest and relevant application sources inside `archive/legacy/ExamGenerationSystem_v0.6.zip`. Compiled bytecode, PDFs, compressed sync data, Git internals, and vendored environment files were identified as generated/binary artifacts rather than interpreted as source. The current `src/` implementation is treated as primary evidence. The ZIP is treated as a separate legacy application, not as importable current runtime code.

Fresh test execution was attempted but was not possible in the available environment: `python` was absent and `/usr/bin/python3 -m pytest -q` failed because `pytest` was not installed. `.pytest_cache/v/cache/nodeids` records 103 previously collected node IDs, but this cache is not evidence of a current passing run. Conclusions about behavior therefore rely on source and test inspection unless explicitly identified as cached evidence.

Evidence citations use repository-relative `path:line` notation. Line references describe the audited commit.

## 1. Executive Summary

SciForge-Edu is currently a small Python library and prototype workflow for turning structured LaTeX question fragments into Pydantic domain objects, persisting those objects in a filesystem/JSON repository, and exporting student and teacher LaTeX documents. It is no longer only in a specification phase: core models, a permissive regex parser, deterministic content-derived IDs, repository persistence/indexing, exam composition primitives, renderer preprocessing, TeX rendering, and TeX file export are implemented (`src/parser/question_parser.py:67-301`, `src/repository/manager.py:31-263`, `src/renderer/exam_render_service.py:32-90`, `src/workspace/exam_export.py:22-63`).

Maturity is prototype/pre-MVP rather than production. The implementation has a broad unit-test surface and an end-to-end TeX demo, but packaging metadata is incomplete, no fresh tests could be run in this environment, several subsystems are skeletal or disconnected, and generated output can retain unresolved template tokens (`pyproject.toml:1-10`, `templates/midterm_base.tex:46`, `build/student.tex:46`). GUI, importer, diagnostics, PDF compilation, answer tables, sandboxing, version lifecycle operations, usage persistence, and knowledge-point functionality are not implemented in current `src/`; their packages are empty or absent beyond data models/specifications (`src/gui/__init__.py`, `src/importer/__init__.py`, `src/diagnostics/__init__.py`).

The implemented architecture is a direct, layered pipeline:

```text
LaTeX question fragments
  -> QuestionParser
  -> Question/Choice/Solution domain models
  -> optional RepositoryManager JSON persistence/index projection
  -> RenderPipeline (temporary namespaces + label/ref rewriting)
  -> ExamPackageRenderer
  -> ExamExport
  -> student.tex + teacher.tex
```

Asset discovery/copying, export-bundle modeling, and template discovery exist as isolated components, but they are not integrated into that end-to-end path (`src/renderer/resource_collector.py:51-114`, `src/renderer/asset_packager.py:33-93`, `src/renderer/export_manager.py:29-71`). The legacy ZIP contains a separate Tk/Jinja2/XeLaTeX application with answer balancing and PDF generation; those legacy capabilities must not be attributed to the current package.

## 2. Current Architecture

### 2.1 Major modules and responsibilities

| Module | Implemented responsibility | Key dependencies and evidence |
|---|---|---|
| `src.models` | Pydantic question aggregate (`Question`, `Choice`, `Solution`, `Analysis`, provenance, source, version, statistics, group) plus dataclass exam composition models | `Question` composes `Choice`, `Solution`, `Analysis`, `Version`, and `Source` (`src/models/question.py:19-81`). `ExamQuestionInstance` wraps a `Question` without mutating it (`src/models/exam_question_instance.py:23-50`). |
| `src.utils` | Deterministic 16-character SHA-256-derived question IDs; whitespace and choice-order normalization | `src/utils/question_id.py:36-106` |
| `src.parser` | Regex-based, permissive parsing of one or many `\question` blocks; legacy inline and environment choices/solutions; optional source path | `src/parser/question_parser.py:67-301`. It always constructs `single_choice`, assigns `points=0`, and does no formal validation (`:150-165`). |
| `src.repository` | Filesystem JSON save/load, synchronous JSON index projection, linear filtering by UUID and question type; usage data structures | `src/repository/manager.py:42-263`; `src/repository/index.py:25-57`; `src/repository/usage.py:27-46` |
| `src.composer` | Group exam question instances globally by effective points | `src/composer/score_grouping.py:17-64` |
| `src.renderer` | Temporary namespace assignment, LaTeX label/reference rewriting, question/section rendering, simple token replacement, basic template discovery, resource discovery/copying, and output-path modeling | Main integrated path: `RenderPipeline` -> `ExamPackageRenderer` (`src/renderer/exam_render_service.py:42-90`). Standalone components: `TemplateManager`, `ResourceCollector`, `AssetPackager`, `ExportManager`, `ExamCompiler`. |
| `src.workspace` | Workspace-draft data model and writing `student.tex`/`teacher.tex` | `src/workspace/draft.py:26-45`; `src/workspace/exam_export.py:22-63` |
| `scripts` | Pydantic-only API snapshot generation and a custom pre-commit test/snapshot workflow | `scripts/generate_snapshot.py:43-215`; `scripts/pre_commit_check.py:33-93`; `.git/hooks/pre-commit:1-3` |
| `src.gui`, `src.importer`, `src.diagnostics` | Package placeholders only | Each contains only an empty `__init__.py`. |

### 2.2 Dependency relationships

The domain models are central. Parser and repository construct/consume `Question`; composer wraps it in exam instances/sections; renderer consumes it and creates copied questions for rewritten references. Repository does not depend on renderer. Renderer does not depend on repository. Workspace export depends directly on the high-level render service. This separation is visible in imports (`src/parser/question_parser.py:58-64`, `src/repository/manager.py:27-28`, `src/renderer/exam_render_service.py:22-29`, `src/workspace/exam_export.py:16-19`).

The integrated renderer is narrower than the renderer directory suggests. `RenderPipeline.run()` only assigns namespaces and rewrites labels/references; it does not call `ResourceCollector` or `AssetPackager`, and returns empty resource/asset collections by default (`src/renderer/render_pipeline.py:42-76`, `src/renderer/render_context.py:50-60`). `ExamExport` directly writes two TeX files and does not use `ExportManager`, `OutputBundle`, `TemplateManager`, `ExamCompiler`, or asset components (`src/workspace/exam_export.py:27-63`).

Two template mechanisms coexist:

- `ExamCompiler` uses Python `str.format()` with `{name}` syntax (`src/renderer/compiler.py:25-56`).
- `ExamPackageRenderer` uses repeated literal replacement of `[[ key ]]` tokens and has no loop/condition parser (`src/renderer/exam_package_renderer.py:111-147`).

The shipped `midterm_base.tex` uses the second mechanism. Unknown placeholders are left unchanged, as demonstrated by the committed generated `build/student.tex:46`.

### 2.3 Legacy boundary

`archive/legacy/ExamGenerationSystem_v0.6.zip` contains its own `main.py`, `core/parser.py`, `core/compiler.py`, and `ui/` tree. Its compiler invokes XeLaTeX twice and copies figures; its UI performs score assignment, answer balancing, answer-table generation, and PDF production. No current `src/` module imports that archive. Therefore it is historical evidence and a possible feature source, not current SciForge runtime architecture.

## 3. Documentation Accuracy

Classification concerns accuracy relative to the audited current repository. A document explicitly framed as historical, policy, or future design is judged within that frame. The generated pytest-cache README is included because the requested scope is every Markdown document.

| Document | Classification | Evidence-based assessment |
|---|---|---|
| `.pytest_cache/README.md` | Accurate | Standard cache explanation; it makes no SciForge behavior claims. The cache exists and contains node IDs. |
| `CHANGELOG.md` | Partially Outdated | Correct for early model work (`:3-20`) but omits all parser, repository, composer, renderer, export, identity, and group work now present. Its `Unreleased` source-model entry (`:37-43`) describes already-committed code. |
| `README.md` | Seriously Outdated | Says “Core engine: not implemented” (`:27-39`), while working core modules occupy `src/models`, `src/parser`, `src/repository`, `src/renderer`, and `src/workspace`. Its install command depends on incomplete PEP 621 metadata (`pyproject.toml:1-10`). |
| `docs/api_snapshot.md` | Mostly Accurate | Its Pydantic model fields match current model declarations (`:5-144`). It is not a full API snapshot: the generator scans only `src/models` Pydantic subclasses (`scripts/generate_snapshot.py:39-89`), so dataclass models and all services/functions are excluded. |
| `docs/architecture_decisions/ADR-DOC-001-documentation-must-be-ai-transferable.md` | Accurate | An accepted documentation decision, not a runtime feature claim. The repository contains the stated layered design documentation and snapshot artifacts. |
| `docs/authoring/ai_prompt_library_v1.md` | Partially Outdated | Single-question syntax is parseable, but prompts require exactly one correct choice (`:59-65`) while parser/tests permit multiple; group prompts (`:112-163`) target unsupported parser behavior (`src/parser/question_parser.py:50-52`). |
| `docs/authoring/question_authoring_spec_v1.md` | Partially Outdated | Claims Question Group support (`:44-53`) and mandatory solutions (`:84-89`, `:166-182`); current parser does not parse groups and explicitly permits no solution (`tests/test_parser_question_parser_v2.py:56-70`). It also does not enforce two choices or exactly one correct choice. |
| `docs/current_status.md` | Seriously Outdated | Claims six implemented query filters (`:68-80`); `RepositoryManager.search()` accepts only `uuid` and `question_type` (`src/repository/manager.py:211-261`). It omits the extensive renderer/composer/export implementation and retains a May 27 focus/status. |
| `docs/current_system_audit_v0.1.md` | Mostly Accurate | Explicitly marked historical/superseded (`:3-10`) and broadly matches the legacy ZIP. Its recommendation is historical opinion rather than current implementation evidence. |
| `docs/current_system_audit_v0.2.md` | Mostly Accurate | Explicitly audits the inherited legacy system (`:10-15`); the archived source supports parser, Tk GUI, Jinja2, XeLaTeX, answer balancing, scores, and answer output claims. “Production-ready” (`:78-81`) is not independently verifiable from repository evidence. |
| `docs/current_system_audit_v0.3.md` | Partially Outdated | Correctly distinguishes legacy/SciForge, but its matrix marks score override, score grouping, and figure copying absent (`:32-48`) despite `ExamQuestionInstance`, `group_by_points`, and `AssetPackager`; it calls explicit section/instance models future (`:201-218`) although they exist. |
| `docs/draft/architecture_direction_v0.1.md` | Mostly Accurate | Clearly long-term/draft. Its filesystem-first, projection-based direction matches current repository code (`:76-111`), but “runtime snapshot” language overstates the model-only snapshot. |
| `docs/draft/architecture_map_v1.0.md` | Seriously Outdated | Presents lexer, validator, diagnostic engine, similarity, GUI, sandbox, and PDF outputs as architecture (`:20-75`, `:104-130`); most are absent. Actual runtime is simpler and includes renderer/composer components not represented. |
| `docs/draft/architecture_map_v1.1.md` | Partially Outdated | TeX-first artifact policy aligns with export, and asset copying exists in isolation. `answers_table.tex`, automatic image-path rewriting, and a fully self-contained integrated package do not exist (`:6-25`). |
| `docs/draft/change_policy_v0.1.md` | Mostly Accurate | A draft process policy, not a status report. Its source-of-truth ordering (`:19-46`) conflicts with this audit’s implementation-first mandate but is accurately stated as policy. |
| `docs/draft/coding_policy_v0.2.md` | Partially Outdated | Snapshot auto-update/stage is implemented (`:167-191`; `scripts/pre_commit_check.py:48-88`), but the requested commit suffix is only printed, not appended. Much current code visibly violates its anti-vertical-spacing examples. |
| `docs/draft/data_model_spec_v1.0.md` | Partially Outdated | General aggregate design remains recognizable, but names/types differ (`type`, `solution_tex`, `QuestionAnalysis`, `QuestionVersion`, `SourceInfo`, `GroupQuestion` vs current fields/classes at `:47-174`). Exam models are mostly absent; current `QuestionGroup` has no UUID/assets/points. |
| `docs/draft/development_roadmap_v0.1.md` | Seriously Outdated | Labels parser and renderer “Planned” (`:27-48`) despite both being implemented and tested. Phase 2’s generic search claim is only narrow UUID/type filtering. |
| `docs/draft/development_workflow_v0.1.md` | Accurate | Generic Git/PyCharm notes; no material current-runtime claim. |
| `docs/draft/documentation_policy_v1.0.md` | Mostly Accurate | Accurately records a draft documentation policy. In practice, required update records (`:156-181`) and consistency goals are not followed across many documents, so the policy is not an accurate description of repository compliance. |
| `docs/draft/documentation_policy_v1.1.md` | Partially Outdated | `student.tex` and `teacher.tex` are outputs, but `answers_table.tex` is not generated (`:6-20`; `src/workspace/exam_export.py:45-63`). |
| `docs/draft/exam_composition_spec_v1.0.md` | Partially Outdated | Instance score override, global score grouping, and conditional section generation exist. `ExamPaper`, instructions/layout options, question ranges, answer table, and editable summary range are absent; implementation calls the source field `points`, not `default_points` (`:89-160`, `:204-299`). |
| `docs/draft/gui_workflow_spec_v1.0.md` | Seriously Outdated | Entire GUI workflow is design-only; current GUI package is empty. Autosave, repository browser, editing modes, restore, and GUI export options are not implemented. |
| `docs/draft/implementation_roadmap_v1.0.md` | Partially Outdated | Still useful as an aspirational sequence, but lacks current phase statuses and lists already-existing parser, repository, workspace draft, renderer, asset copy, and template manager work as future (`:55-184`). |
| `docs/draft/import_pipeline_spec_v1.0.md` | Seriously Outdated | Describes PDF/DOCX/CSV import, normalization, similarity, AI analysis, and review pipeline (`:20-79`); current importer package is empty. Only LaTeX question parsing exists elsewhere. |
| `docs/draft/knowledge_point_architecture_v0.1.md` | Mostly Accurate | Explicit proposal/future direction. It correctly presents future fields and queries (`:205-228`); neither `Analysis` nor `Question` currently has knowledge/curriculum codes. |
| `docs/draft/parser_grammar_spec_v1.0.md` | Seriously Outdated | Specifies fail-rather-than-guess, lexer/AST/validator/diagnostics, metadata, groups, and exactly one correct choice (`:6-49`, `:66-235`). Actual parser is permissive regex, ignores metadata/groups, and permits zero/multiple correct choices. Filename says v1.0 while body says v1.1 (`:2-4`). |
| `docs/draft/provenance_spec_v1.0.md` | Mostly Accurate | Fields/source literals align with `Provenance`/`Revision` (`:39-70`; `src/models/provenance.py:25-80`). Several documented fields are optional in code, and lifecycle/GUI/repository integration is not implemented. |
| `docs/draft/question_grammar_v0.1.md` | Partially Outdated | Basic questions, choices, solutions, images/tables as raw TeX are supported. Group/GroupStem support (`:70-80`, `:200-314`) and correctness cardinality validation (`:120-164`) are absent. |
| `docs/draft/question_group_spec_v1.0.md` | Partially Outdated | `QuestionGroup` container, shared stem, boxed hint, child list minimum, and non-nesting by type are modeled (`src/models/question_group.py:26-41`). Its parser, renderer, GUI, asset, drag/drop, and AI validation requirements are absent. Its LaTeX syntax also differs from `question_grammar_v0.1.md`. |
| `docs/draft/question_identity_v0.1.md` | Accurate | Identity fields, excluded fields, whitespace normalization, choice-order independence, deterministic generation, and separate render namespace match `src/utils/question_id.py:36-106` and `src/renderer/namespace_assigner.py:28-53`. Absolute no-collision wording cannot be guaranteed by a truncated hash, but no implementation contradiction was found. |
| `docs/draft/question_source_format_v0.1.md` | Seriously Outdated | File is empty, so it cannot document the implemented source format or current behavior. |
| `docs/draft/renderer_architecture_v0.1.md` | Seriously Outdated | Claims current XeLaTeX compilation, answer-sheet generation, and output bundles (`:19-68`); current compiler only formats text and no PDF service exists. Superseded concepts also remain unmarked. |
| `docs/draft/renderer_architecture_v0.2.md` | Partially Outdated | Correctly describes implemented namespace, resource, asset, rewrite, rendering, and bundle components. Its pipeline falsely implies those components are integrated and that XeLaTeX/answer table/PDF are supported (`:64-73`, `:182-210`); module names also differ (`ReferenceRewriter` combines label/ref). |
| `docs/draft/repository_index_spec_v0.1.md` | Mostly Accurate | Correctly frames the index as a lightweight projection and current JSON/filesystem direction (`:24-60`, `:182-202`). Many listed statistical/provenance/usage fields are explicitly candidates/future, not implemented. |
| `docs/draft/repository_query_spec_v0.1.md` | Mostly Accurate | Correctly says current filtering is limited and linear (`:150-170`) and frames broader categories as goals. It conflicts with `current_status.md`, not with implementation. |
| `docs/draft/repository_spec_v1.0.md` | Partially Outdated | Save/load/index concepts align, but similarity, meaningful version operations, usage persistence, import normalization, GUI workflow, and origin metadata are absent. “Question source files remain primary assets” (`:22-24`) conflicts with JSON `Question` persistence. |
| `docs/draft/repository_spec_v1.1.md` | Partially Outdated | `AssetPackager` can create names in the shown style and `ExportManager` can make an assets directory, but current exam export does not integrate them or produce `answers_table.tex`; self-containment is not ensured (`:6-25`). |
| `docs/draft/repository_storage_spec_v0.1.md` | Partially Outdated | `questions/<uuid>/question.json` and `index/repository_index.json` are implemented (`:17-68`, `:95-105`). `usage.json` and repository-managed `resources/` are not created; `save_question` contains an explicit usage-file TODO (`src/repository/manager.py:47-53`). |
| `docs/draft/sandbox_compile_spec_v1.0.md` | Seriously Outdated | No sandbox, compiler subprocess, resource limits, compile diagnostics, path rewrite, or PDF output exists in current `src/`. |
| `docs/draft/sciforge_api_snapshot_draft_v1.md` | Partially Outdated | Correct for early models/repository/workspace, but `Question.points` is float, `source_path` is omitted, and composer/renderer/export/identity/group APIs are absent from the draft (`:41-176`). |
| `docs/draft/template_api_spec_v1.0.md` | Seriously Outdated | No template manifests, packages, built-ins, render view models, conditions, loops, components, validator, or answer-table export exists. Current renderer exposes `Question` directly and does literal token replacement, contrary to `:85-221`. |
| `docs/draft/template_audit_v1.md` | Partially Outdated | Correctly describes QuestionParser -> ExamPackageRenderer -> student/teacher TeX and `exam.cls` answer visibility (`:26-178`). It then shows XeLaTeX/PDF as current pipeline although current code never compiles, and the shipped template leaves an unresolved token. |
| `docs/exam_composer_roadmap_v0.1.md` | Seriously Outdated | Treats legacy v0.6 features as the “current baseline” and plans versions unrelated to current package status (`:3-25`). Current model/template/repository work does not align with these version milestones. |
| `docs/governance/environment_setup.md` | Partially Outdated | Requirements and pytest command are conventional, but `pip install -e .[dev]` (`:37-46`) is not supported by the current incomplete `[project]` table, which lacks required package name/version (`pyproject.toml:1-10`). The audited environment also lacks pytest. |
| `docs/todo.md` | Mostly Accurate | Correctly records only UUID/type search as current (`:132-152`) and many missing features. “Exam Generation MVP Pending” understates that student/teacher TeX export exists, but answer sheets, solutions-as-separate-output, and PDF remain absent. |
| `examples/repositories/physics_foundation/README.md` | Seriously Outdated | Claims `questions/`, `metadata/`, and `index/` structure and curated questions (`:22-63`), but the example repository contains only this README. |

## 4. Documentation Inconsistencies

1. **README vs implementation and roadmaps.** `README.md:31-39` says core engine is not implemented. `docs/draft/development_roadmap_v0.1.md:3-24` says core models and repository are complete, while current sources additionally implement parser and renderer. These cannot all describe current status.

2. **Current status vs query spec/TODO/code.** `docs/current_status.md:68-80` says UUID, type, subject, chapter, difficulty, and tags are implemented. `docs/todo.md:132-152` and `docs/draft/repository_query_spec_v0.1.md:163-170` say filtering is limited; the latter two agree with `RepositoryManager.search()`.

3. **Parser strictness conflict.** `docs/draft/parser_grammar_spec_v1.0.md:31-34` says fail rather than guess, while the parser module explicitly says permissive and missing optional metadata should not fail (`src/parser/question_parser.py:17-25`). The authoring/grammar docs demand exactly one correct choice, but tests deliberately accept two (`tests/test_parser_question_parser_v2.py:73-92`).

4. **Solution requirement conflict.** `docs/authoring/question_authoring_spec_v1.md:84-89` says required; `docs/draft/question_grammar_v0.1.md:168-196` and `docs/authoring/ai_prompt_library_v1.md:59-65` say optional. Implementation says optional (`Question.solution`) and tests verify missing solution.

5. **Question-group grammar conflict.** `question_grammar_v0.1.md:206-221` uses `\begin{groupstem}...`; `question_group_spec_v1.0.md:57-87` uses `\groupstem{...}` inside a `questions` environment; `question_authoring_spec_v1.md:100-140` puts the shared text directly inside `questiongroup`. None is implemented by the parser.

6. **Current-system audits conflict over absorbed composition features.** `current_system_audit_v0.3.md:42-46` says score override/grouping/figure copying are not yet in SciForge, while the current branch implements all three as discrete units. The same document later calls explicit `ExamSection` a future target (`:201-218`) although it exists.

7. **Renderer architecture vs actual pipeline.** `renderer_architecture_v0.2.md:182-210` presents resource collection, asset packaging, rewriting, template rendering, XeLaTeX, and output bundle as one pipeline. Actual `RenderPipeline` performs only namespaces/reference rewriting, and `ExamExport` bypasses the other components.

8. **Template architecture conflict.** `template_api_spec_v1.0.md` specifies view models and a custom condition/loop language; `ExamCompiler` uses `{}`/`str.format`, while `ExamPackageRenderer` uses literal `[[ key ]]` replacement. The shipped template embeds LaTeX conditionals rather than specified template-language conditionals.

9. **Output filename inconsistency.** Documents alternate between `answer_table.tex` and `answers_table.tex` (`renderer_architecture_v0.2.md:302-316`; `architecture_map_v1.1.md:8-16`; `template_api_spec_v1.0.md:193-205`). `OutputBundle` uses singular `answer_table.tex` (`src/renderer/export_manager.py:67-70`), but no answer table is written.

10. **Source of truth conflict.** `architecture_map_v1.0.md:134-145` says `Question` is the only source of truth and LaTeX is import/export; `repository_spec_v1.0.md:22-24` says question source files remain primary assets; `change_policy_v0.1.md:30-46` prioritizes model code over specs/tests, while documentation policy says implementation must follow documentation (`documentation_policy_v1.0.md:230-235`).

11. **Example vs active status.** `sample_repository_workflow.py` calls subject/tags queries and uses obsolete model constructors, matching the false `current_status.md` claim rather than current code. The TODO correctly records the narrower API.

12. **Template audit vs generated artifact.** `template_audit_v1.md:97-118` says content is injected once, but `midterm_base.tex:52-62` contains `[[ questions_content ]]` in both branches, and literal replacement duplicates content into both branches in each generated file (`build/student.tex:52-110`). LaTeX conditionals select one at compile time, but textual injection occurs twice.

## 5. Code vs Documentation Mismatches

| # | Affected document(s) | Affected source/test/config | Mismatch | Severity | Supporting evidence |
|---:|---|---|---|---|---|
| 1 | `README.md` | All `src/` subsystems | Core engine is said to be unimplemented. | High | README `:31-39`; concrete end-to-end export in `src/workspace/exam_export.py:27-63`. |
| 2 | `current_status.md` | `src/repository/manager.py` | Six query filters claimed; only two accepted. Calls with others raise `TypeError`. | High | Status `:68-80`; method signature `:211-215`. |
| 3 | `sample_repository_workflow.py` (executable documentation) | Current Pydantic models and repository API | Example uses missing required provenance fields, obsolete `Choice(key, content)`, `Solution(answer, explanation)`, `Source(source_type, source_name)`, missing `Question.points/stem_tex`, and unsupported `search(subject/tags)`. | High | Example `:90-202`, `:284-311`; model fields in `src/models/choice.py:22-31`, `solution.py:22-31`, `source.py:23-30`, `question.py:41-81`. |
| 4 | Parser/authoring/grammar specs | `src/parser/question_parser.py`; parser tests | Specs require strict validation and exactly one correct answer; implementation is permissive and accepts multiple. | High | Parser spec `:117-120`, `:183-235`; test `test_parser_question_parser_v2.py:73-92`. |
| 5 | Question-group specs/prompts | Parser and renderer | `QuestionGroup` data model exists, but no group source parsing or rendering exists. | High | Parser explicitly excludes it (`question_parser.py:50-52`); renderer accepts `Question`/`ExamSection`, not groups (`exam_renderer.py:33-151`). |
| 6 | Renderer architecture v0.1/v0.2; sandbox spec | `src/renderer/compiler.py` | “Compiler” only applies `str.format` and writes a file; it never invokes XeLaTeX or produces PDF/diagnostics/sandboxing. | High | Compiler `:25-56`; renderer v0.2 `:64-73`, sandbox spec `:108-195`. |
| 7 | Template API | `exam_package_renderer.py`, `compiler.py` | No view models, manifest/package system, conditions, loops, components, or validator; two incompatible substitution mechanisms exist. | High | Template spec `:39-221`; sources `exam_package_renderer.py:111-147`, `compiler.py:40-55`. |
| 8 | Renderer architecture v0.2; repository spec v1.1 | `render_pipeline.py`, `exam_export.py`, asset modules | Resource discovery/copying is not integrated; image paths are not rewritten, so exports are not guaranteed self-contained. | High | Document pipeline `:182-210`; actual pipeline `render_pipeline.py:42-76`; export `exam_export.py:27-63`. |
| 9 | Output policies and GUI/template docs | `ExamExport`, `OutputBundle` | Answer-table path is modeled but no answer table is rendered/written. Naming also varies. | High | `output_bundle.py:28-42`; `exam_export.py:45-63`; docs cited in inconsistency 9. |
| 10 | Environment setup/README Quick Start | `pyproject.toml` | Editable install instructions rely on a `[project]` table with no `name` or `version`. | High | Setup `:37-46`; config `pyproject.toml:1-10`. Conclusion is based on packaging metadata inspection; install was not attempted because this audit avoids external dependency changes. |
| 11 | Exam composition spec | `ExamPackageRenderer`, composition models | Instance overrides are implemented but full-package rendering accepts raw `Question` only, so overrides, display order, inclusion, choice order, and paper version do not participate in export. | High | Spec `:89-160`; renderer signature `exam_package_renderer.py:40-69`; instances are reconstructed from raw questions `:87-101`. |
| 12 | Exam composition spec/current audit v0.3 | `ExamSection`/`SectionRenderer` | Document promises question range/count/points/total; implementation summary outputs only points per question and total. `title` is ignored. | Medium | Spec `:220-246`; model `exam_section.py:90-111`; renderer `section_renderer.py:19-28`. |
| 13 | Repository storage/spec | `RepositoryManager`/usage models | Usage model exists, but repository never creates or reads `usage.json`. | Medium | Storage spec `:71-91`; explicit TODO `repository/manager.py:47-53`. |
| 14 | Repository spec | Repository code | Version history models exist, but save overwrites `question.json` and no versioning operation is performed. | High | Repository spec `:188-203`; save opens with `"w"` (`manager.py:66-85`). |
| 15 | Provenance spec | `Question`, `Solution`, `Analysis` | Provenance is present on `Solution` and optional `Analysis`, but not directly on `Question`; repository/workspace do not maintain revision lifecycle. | Medium | Spec integration list `:84-92`; model fields `question.py:41-81`, `solution.py:22-31`, `analysis.py:25-54`. |
| 16 | Data model spec/API snapshot draft | Current models | Numerous names/types differ: `Question.points` is float, `question_type` replaces `type`, `Solution` replaces `solution_tex`, and current source/group shapes differ. | Medium | Data spec `:47-174`; current snapshot `docs/api_snapshot.md:21-140`. |
| 17 | `api_snapshot.md`, current status snapshot claims | Snapshot generator | “API snapshot” covers only Pydantic models in `src/models`, omitting dataclasses, repository/parser/renderer/workspace APIs, and empty/non-Pydantic packages. | Medium | Generator `:39-89`, `:159-191`; snapshot content `:1-144`. |
| 18 | Physics foundation README | Example directory | Documented repository structure/content does not exist. | Medium | README `:22-63`; repository inventory contains only that README under the directory. |
| 19 | Template audit/current demo | Shipped template and build outputs | `full_instruction_content` is never supplied by `examples/generate_exam.py` and remains unresolved in both committed outputs. | Medium | Template `:46`; demo metadata `examples/generate_exam.py:91-99`; generated output `build/student.tex:46`, `build/teacher.tex:46`. |
| 20 | Changelog/roadmaps/current status | Current source tree | Later implementation is absent from change/status tracking, producing contradictory maturity signals. | Medium | `CHANGELOG.md` ends with early source/repository-era entries; renderer integration is the audited commit subject, yet not recorded. |
| 21 | Renderer architecture | `NamespaceAssigner` | Namespace map keyed by UUID silently collapses duplicate UUIDs; pipeline then gives duplicates the same final namespace. No documentation records this precondition. | Medium | `namespace_assigner.py:34-53`; map used by UUID in `render_pipeline.py:58-70`. Evidence is static; no duplicate-ID test exists. |
| 22 | Identity spec | `generate_question_id` | Spec describes stable question identity, but the parser derives UUID from content each parse. Any identity-field edit creates a new UUID; no persistent UUID/version reconciliation exists. | Medium | Identity spec `:59-72`, `:93-121`; parser generation `question_parser.py:150-165`. This is consistent with hash rules but conflicts with repository version-evolution expectations. |
| 23 | Repository index docs | `RepositoryManager.update_index` | Index model has `current_version` and `usage_count`, but projection never copies either from question/usage and always uses defaults. | Low | Model `repository/index.py:50-57`; construction `repository/manager.py:151-186`. |
| 24 | Renderer self-containment docs | `AssetPackager` | Mapping is keyed only by source path. Reusing one source for two question namespaces copies twice but retains only the final mapping entry. This behavior is undocumented. | Low | `asset_packager.py:51-93`. No test covers shared identical source paths. |

## 6. Undocumented Implementations

“Undocumented” means absent or materially underrepresented in current top-level/status/API documentation, even if a dedicated draft mentions the concept.

1. **Integrated high-level render service.** `ExamRenderService` runs preprocessing before student/teacher rendering (`src/renderer/exam_render_service.py:32-90`), but `README.md`, `current_status.md`, and `api_snapshot.md` do not mention it.

2. **Actual current end-to-end TeX demo.** `examples/generate_exam.py:63-123` parses sample questions and writes student/teacher TeX. The README has no usage example or command for it.

3. **Conditional score section generation.** `ExamPackageRenderer` avoids sections when all scores match and globally groups when scores differ (`src/renderer/exam_package_renderer.py:71-109`). This is covered in a draft composition spec and tests but absent from active status/API documentation.

4. **Reference rewriting breadth.** `ReferenceRewriter` processes labels plus `ref`, `pageref`, `autoref`, and `eqref` in stems, choices, and solutions without mutating the original (`src/renderer/reference_rewriter.py:35-100`, `:146-190`). Active docs do not expose this implemented API.

5. **Renderer composition models.** `ExamQuestionInstance` and `ExamSection` are current code with tests, but the generated API snapshot cannot discover dataclasses and active status omits them (`src/models/exam_question_instance.py:23-50`, `exam_section.py:30-123`).

6. **Template manager and output-bundle utilities.** These implemented classes are absent from current API/status docs (`src/renderer/template_manager.py:26-88`, `export_manager.py:29-71`, `output_bundle.py:28-42`).

7. **Resource collection edge behavior.** Collector supports image references in stems, choices, solutions, optional `includegraphics` options, subdirectories, and parent paths (`src/renderer/resource_collector.py:56-114`; `tests/test_renderer_resource_collector.py`). Dedicated renderer draft describes the component generally but not this tested behavior.

8. **Deterministic ID details.** The dedicated identity draft is accurate, but active API/status docs omit the public helper and its 16-character SHA-256 format (`src/utils/question_id.py:89-106`).

9. **Legacy syntax migration support.** Parser supports inline `\choice` and `\solution` in addition to environments (`question_parser.py:193-221`, `:258-287`). Canonical authoring docs discuss only environment syntax.

10. **Committed generated outputs as observable behavior.** `build/student.tex` and `build/teacher.tex` show the exact current demo output, including duplicated conditional question bodies and unresolved instruction token. No document identifies them as generated snapshots or warns that they are ignored by `.gitignore` except for already-tracked files.

## 7. Documented but Missing Implementations

The following could not be found in current `src/`. Some exist only inside the legacy ZIP; those are explicitly marked.

| Documented capability | Current implementation finding | Evidence / uncertainty |
|---|---|---|
| GUI exam builder/repository manager/import tool | Missing; `src/gui/__init__.py` is empty. | GUI spec throughout. Legacy ZIP has a Tk GUI, but it is not current runtime code. |
| Importers for PDF, DOCX, CSV, OCR/plain text | Missing; `src/importer/__init__.py` is empty. | Import spec `:20-31`. |
| Lexer, AST, validator, diagnostic engine and diagnostic objects | Missing; only regex `QuestionParser` exists and diagnostics package is empty. | Parser spec `:37-49`, `:159-235`. |
| QuestionGroup/GroupStem source parsing and rendering | Missing. A Pydantic container model exists only. | Parser explicitly declares groups outside scope (`question_parser.py:50-52`). |
| Template manifests/packages/view models/loops/conditions/validator | Missing. | Template spec `:39-221`; no matching files/classes. |
| XeLaTeX/PDF compilation in current package | Missing. | Current `ExamCompiler` has no subprocess. Legacy ZIP implements it. |
| Compilation sandbox, limits, diagnostics, timeouts | Missing. | Sandbox spec `:20-195`. |
| Answer table/sheet generation | Missing in current package; only a path field exists. | Legacy ZIP implements `answers.tex`; current export writes only two files. |
| Answer balancing and choice shuffling | Missing in current package. | Legacy ZIP implements answer swapping/balancing. `ExamQuestionInstance.choice_order` is stored but unused. |
| A/B exam generation | Missing. | `paper_version` field exists but is unused (`exam_question_instance.py:38`). |
| Full exam model (`ExamPaper`/`Exam`) | Missing. | Composition/data specs define it; current code uses lists of `Question`. |
| Workspace autosave/restore/copy/version-save workflow | Missing beyond `WorkspaceDraft` data fields. | No workspace persistence service exists. |
| Repository version management | Missing beyond data fields; save overwrites current JSON. | No version service/method exists. |
| Similarity/duplicate detection | Missing. | Identity hashing is not similarity detection (`question_id.py:23-26`). |
| Usage persistence/prevention of repeated questions | Missing beyond models. | `save_question` TODO confirms absent usage file. |
| Statistical queries/repository analytics | Missing. | Statistics model exists, but search cannot filter it. |
| Subject/chapter/tag/difficulty queries | Missing from method signature despite status claim. | `manager.py:211-261`. |
| Knowledge point/curriculum models and queries | Missing; documents clearly frame much of this as future/proposed. | `Analysis` has no such fields (`analysis.py:25-54`). |
| Resource path rewriting and integrated self-contained packages | Missing. Collector/copy utilities exist, but TeX `\includegraphics` paths are never rewritten and utilities are not called by export. | This conclusion is certain for the current call graph. |
| Template extraction and AI features | Missing. | Only provenance literal `template_extractor` exists. |
| OMR/assessment import | Missing. | Roadmap-only. |

## 8. Tests vs Documentation

### 8.1 Tests that contradict documentation

1. `test_parse_multiple_correct_choices` expects two `CorrectChoice` markers to parse successfully (`tests/test_parser_question_parser_v2.py:73-92`). Parser grammar and authoring documents call this invalid and require exactly one (`parser_grammar_spec_v1.0.md:117-120`; `question_authoring_spec_v1.md:84-89`). The test is the clearest executable behavior statement: the current parser is permissive.

2. `test_parse_missing_solution` expects a valid question with `solution is None` (`test_parser_question_parser_v2.py:56-70`). That conflicts with the authoring spec’s mandatory-solution rule (`question_authoring_spec_v1.md:166-182`) but agrees with `question_grammar_v0.1.md` and the AI prompt library.

3. Renderer tests establish implemented score grouping, score override, section summaries, asset copying, and section rendering (`test_composer_score_grouping.py`, `test_models_exam_question_instance.py`, `test_models_exam_section.py`, `test_renderer_asset_packager.py`). `current_system_audit_v0.3.md:42-45` labels these absent from SciForge.

4. Repository manager tests cover only UUID/type search (`tests/test_repository_manager.py:107-166`). There are no tests for the additional filters claimed in `current_status.md`, consistent with their absence from code.

5. Exam export test requires only `student.tex` and `teacher.tex` (`tests/test_exam_export.py:9-41`). No test expects the answer-table/PDF outputs promised by multiple docs.

### 8.2 Tests that confirm documentation

- Identity tests confirm stable same-content IDs, changes for stem/choice/correctness, order independence, and whitespace normalization (`tests/test_utils_question_id.py:15-172`), aligning with `question_identity_v0.1.md`.
- Reference-rewriter tests confirm supported commands, cross-block rewriting, normalization, missing-reference tolerance, multiple labels, and source immutability (`tests/test_renderer_reference_rewriter.py`), broadly aligning with renderer v0.2.
- Resource and asset tests confirm relative path resolution, missing-file reporting, filename collision avoidance across namespaces, and mapping generation (`tests/test_renderer_resource_collector.py`, `test_renderer_asset_packager.py`), aligning with the discrete component descriptions.
- Exam package tests confirm no section for one score and automatic sections for multiple scores (`tests/test_renderer_exam_package_renderer.py:82-145`), aligning with the corresponding composition-spec rule.

### 8.3 Coverage gaps relevant to documentation claims

No tests were found for GUI, importer, diagnostics, PDF compilation, sandboxing, answer tables, A/B papers, usage persistence, version lifecycle, similarity, workspace persistence, knowledge points, template manifests/view models/validation, integrated asset packaging/path rewriting, packaging/install, or the two examples as executable programs. Therefore no test evidence supports those documented capabilities.

No test covers duplicate question UUIDs in one render, shared identical asset sources across namespaces, malformed existing repository index entries, atomic/concurrent repository writes, unresolved template placeholders, or actual TeX compilation. Conclusions about these edge cases are uncertain beyond static code behavior.

## 9. Documentation Technical Debt

1. **No authoritative current-state document.** README, current status, TODO, audits, roadmaps, and API snapshots report different maturity levels. The file named `current_status.md` contains one of the most consequential false claims.

2. **Aspirational specifications read as implemented contracts.** Many drafts use “supports,” “shall,” and current-scope language without an implementation-status marker per feature. This is acute for parser, renderer, GUI, template, import, and sandbox documents.

3. **Legacy and current systems are easy to conflate.** Three “current system” audits discuss the archived Gemini application, while the repository’s current `src/` system has a different architecture. v0.3 partially distinguishes them but is itself stale.

4. **Duplicated and conflicting grammar.** At least four documents define question/group syntax with incompatible requirements: authoring spec, AI prompt library, question grammar, and question-group spec.

5. **Duplicated roadmap/status layers.** `README`, `current_status`, `todo`, two development/implementation roadmaps, exam-composer roadmap, and system audits all encode status with no synchronized source.

6. **Version suffix files are change summaries rather than complete specifications.** `architecture_map_v1.1.md`, `documentation_policy_v1.1.md`, and `repository_spec_v1.1.md` cannot stand alone and do not explicitly declare which earlier content remains authoritative.

7. **Snapshot scope is mislabeled.** `api_snapshot.md` is accurately generated but is only a Pydantic-model snapshot. Calling it the authoritative runtime reconstruction signal (`current_status.md:209-213`) hides parser/repository/renderer/workspace APIs and dataclasses.

8. **Executable documentation is broken.** `examples/sample_repository_workflow.py` calls obsolete constructors/APIs. Because it labels itself canonical executable documentation (`:1-34`), it is a high-risk onboarding artifact.

9. **Empty canonical-looking document.** `question_source_format_v0.1.md` is zero bytes, yet its name implies source-format guidance.

10. **Generated artifacts expose undocumented incompleteness.** Committed TeX outputs preserve `[[ full_instruction_content ]]`; documentation neither acknowledges the unresolved placeholder nor defines placeholder failure behavior.

11. **Policy compliance drift.** Documentation policy requires version/date/author/reason/affected-file records, but most updates do not contain them. Coding policy says snapshots always reflect project state, but the snapshot intentionally excludes most public APIs.

12. **Terminology drift.** `answer_table` vs `answers_table`, `QuestionAnalysis` vs `Analysis`, `QuestionVersion` vs `Version`, `SourceInfo` vs `Source`, `GroupQuestion` vs `QuestionGroup`, `default_points` vs `points`, and compiler/template-renderer meanings vary across documents and code.

13. **Changelog has stopped tracking implementation reality.** It ends around early models/source work although the repository now has a significant parser/renderer/composition stack.

14. **Historical files lack consistent supersession metadata.** Audit v0.1 points to v0.2; v0.2 does not point to v0.3; renderer v0.1 is not explicitly superseded; old architecture/spec versions remain in the same draft namespace.

## 10. Documentation Synchronization Priorities

These are synchronization priorities only; they do not prescribe architecture changes or rewrite content.

| Priority | Document(s) to synchronize | Why first |
|---|---|---|
| High | `README.md`, `docs/current_status.md` | They are the primary onboarding/current-state surfaces and currently make false core/query claims. |
| High | `examples/sample_repository_workflow.py` as executable documentation | It is labeled canonical but cannot construct current models or call current search APIs. It will mislead or immediately fail for users. |
| High | Parser contract set: `parser_grammar_spec_v1.0.md`, `question_grammar_v0.1.md`, `question_authoring_spec_v1.md`, `ai_prompt_library_v1.md`, `question_group_spec_v1.0.md` | These disagree on strictness, solutions, groups, and syntax; generated content can therefore be invalid for the actual parser. |
| High | Renderer/output set: `renderer_architecture_v0.2.md`, `template_api_spec_v1.0.md`, `sandbox_compile_spec_v1.0.md`, `repository_spec_v1.1.md` | These overstate integrated assets, templates, answer tables, self-containment, and PDF compilation—the boundary between working TeX export and missing production output. |
| High | `docs/governance/environment_setup.md` and README Quick Start | The installation path is foundational and current packaging metadata does not substantiate it. |
| Medium | `docs/api_snapshot.md` description and `current_status.md` snapshot claims | Snapshot content itself matches models, but its stated role/scope is broader than generation. |
| Medium | `docs/current_system_audit_v0.3.md` and prior audit supersession metadata | Needed to clearly separate legacy ZIP capabilities from current package capabilities and record absorbed features accurately. |
| Medium | Composition/data model docs | Much of the design is partly implemented, but names, effective-score flow, summary fields, and absent `ExamPaper` need status alignment. |
| Medium | Repository specs/status/TODO | Save/load/index behavior is real, while versioning, usage, resource persistence, and broader queries are not. These boundaries should agree. |
| Medium | `CHANGELOG.md` and roadmap status documents | They should reflect the already-implemented parser/renderer/composer/export milestones so repository history is reconstructable. |
| Low | Architecture direction, ADR, Git workflow, knowledge-point draft | These are mostly policy/future-direction documents and create less immediate behavioral risk. |
| Low | Historical/empty/generated-document housekeeping | Supersession labels, the empty source-format draft, answer-table naming, and generated-output status matter, but follow current contract surfaces. |

## 11. Executive Findings

1. **The repository is implemented well beyond “specification draft,” but primary onboarding says otherwise.** This matters because maintainers may overlook working parser, repository, renderer, and export code or plan duplicate work.

2. **`current_status.md` falsely reports six repository query filters; code supports two.** This is a direct API-contract error likely to cause runtime `TypeError` and is repeated by the canonical example.

3. **The canonical repository workflow example is incompatible with nearly every current model signature it uses.** This makes executable onboarding fail before demonstrating the repository and strongly suggests documentation/model drift.

4. **Current output stops at student/teacher TeX; current-package PDF, sandbox, and answer-table claims are unsupported.** The legacy ZIP has these features, but they are not integrated current functionality.

5. **Renderer components exist but do not form the documented full pipeline.** Namespaces/reference rewriting are integrated; asset collection/copying, output bundles, template management, and path rewriting are disconnected. Self-contained export is therefore not established.

6. **Parser behavior is permissive while the formal grammar describes a strict validated architecture.** Tests explicitly accept multiple correct answers and missing solutions, so authoring tools following the docs and consumers relying on validation have incompatible expectations.

7. **QuestionGroup is a model, not an end-to-end capability.** It cannot be parsed, rendered, composed, or edited through a GUI despite multiple documents/prompts describing those workflows.

8. **The shipped install/quick-start contract is not supported by current packaging metadata.** Missing project name/version and unavailable test dependencies in the audited environment prevent this audit from validating the documented setup path.

9. **The API snapshot is accurate but materially incomplete as a runtime reconstruction artifact.** It covers Pydantic model fields only and omits the very parser/repository/renderer APIs that define current behavior.

10. **The repository has extensive unit-test source evidence but no fresh verified test result for this audit.** Cached metadata lists 103 tests, yet the available interpreter lacks pytest. Current correctness should therefore not be inferred from cache artifacts or test presence alone.
