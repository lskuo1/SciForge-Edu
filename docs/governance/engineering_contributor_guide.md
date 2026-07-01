# Engineering Contributor Guide

Status: Accepted

---

## 1. Repository Orientation

SciForge-Edu is an educational question asset management and exam generation system. It leverages structured data models, regex parsers, and LaTeX compilation logic to manage question repositories and compose exams.

The repository is organized into the following primary directories:
- [src/](../../src/): Core source code containing all implementation modules.
- [tests/](../../tests/): Python test files corresponding to the implementation modules.
- [docs/](../): Project documentation, specification drafts, sprint logs, retrospectives, and templates.
- [examples/](../../examples/): Interactive python scripts demonstrating the repository manager workflow and end-to-end exam generation.

To configure your development environment, install dependencies, and run the test suite, refer to [environment_setup.md](environment_setup.md).

---

## 2. Repository Discovery

Contributors—including human developers and AI sessions—should locate context and understand system status using the following assets:
- **Core Data Model Layout**: Reference [api_snapshot.md](../api_snapshot.md) for the layout, fields, and definitions of core question and assessment models.
- **Active Working Context**: Consult [current_status.md](../current_status.md) to discover the stable foundations, current focus areas, unresolved architectural tensions, and recommended reading order.
- **Subsystem Architecture**: Read the documents in the [docs/draft/](../draft/) directory to review the design plans and RFCs for specific components.
- **Test Executions**: Run `pytest` to inspect baseline requirements and explore test assertions under [tests/](../../tests/).

---

## 3. Engineering Knowledge Model

The repository operates on a structured knowledge model that preserves engineering context across development sessions and AI handoffs:
- **Active Context**: Kept in [current_status.md](../current_status.md) for transient task tracking, session continuity, and immediate priorities.
- **Model Schemas**: Maintained in [api_snapshot.md](../api_snapshot.md) as the active fields and schemas of the core data models.
- **Design Specifications**: Preserved in [docs/draft/](../draft/) as draft RFCs detailing system capabilities.
- **Sprint Records**: Saved under [docs/sprints/](../sprints/) to record the plans and outcomes of past sprints.
- **Sprint Retrospectives**: Saved under [docs/retrospectives/](../retrospectives/) to track observations and process improvements.
- **Governance Findings**: Maintained in [finding_registry.md](finding_registry.md) and [docs/governance/findings/](findings/) to preserve repository-level governance knowledge, engineering observations, and lessons learned across multiple sprints.

---

## 4. Engineering Navigation

Contributors can locate the specifications, implementation code, and test coverage for each repository package via the following navigation index:

| Subsystem / Package | Draft / Specification Document | Implementation Location | Test Suite Location |
| :--- | :--- | :--- | :--- |
| **Core Models** | [data_model_spec_v1.0.md](../draft/data_model_spec_v1.0.md)<br>[provenance_spec_v1.0.md](../draft/provenance_spec_v1.0.md)<br>[question_identity_v0.1.md](../draft/question_identity_v0.1.md) | [src/models/](../../src/models/) | [test_question.py](../../tests/test_question.py)<br>[test_choice.py](../../tests/test_choice.py)<br>[test_solution.py](../../tests/test_solution.py)<br>[test_provenance.py](../../tests/test_provenance.py)<br>[test_source.py](../../tests/test_source.py)<br>[test_question_group.py](../../tests/test_question_group.py)<br>[test_usage.py](../../tests/test_usage.py) |
| **Parser & Grammar** | [parser_grammar_spec_v1.0.md](../draft/parser_grammar_spec_v1.0.md)<br>[question_grammar_v0.1.md](../draft/question_grammar_v0.1.md) | [src/parser/](../../src/parser/) | [test_parser_question_parser.py](../../tests/test_parser_question_parser.py)<br>[test_parser_question_parser_v2.py](../../tests/test_parser_question_parser_v2.py) |
| **Repository Persistence** | [repository_spec_v1.0.md](../draft/repository_spec_v1.0.md)<br>[repository_index_spec_v0.1.md](../draft/repository_index_spec_v0.1.md)<br>[repository_query_spec_v0.1.md](../draft/repository_query_spec_v0.1.md)<br>[repository_storage_spec_v0.1.md](../draft/repository_storage_spec_v0.1.md) | [src/repository/](../../src/repository/) | [test_repository_index.py](../../tests/test_repository_index.py)<br>[test_repository_manager.py](../../tests/test_repository_manager.py) |
| **Exam Composer** | [exam_composition_spec_v1.0.md](../draft/exam_composition_spec_v1.0.md) | [src/composer/](../../src/composer/) | [test_composer_score_grouping.py](../../tests/test_composer_score_grouping.py)<br>[test_models_exam_section.py](../../tests/test_models_exam_section.py)<br>[test_models_exam_question_instance.py](../../tests/test_models_exam_question_instance.py) |
| **Render Pipeline** | [renderer_architecture_v0.2.md](../draft/renderer_architecture_v0.2.md)<br>[template_api_spec_v1.0.md](../draft/template_api_spec_v1.0.md) | [src/renderer/](../../src/renderer/) | [test_renderer_compiler.py](../../tests/test_renderer_compiler.py)<br>[test_renderer_reference_rewriter.py](../../tests/test_renderer_reference_rewriter.py)<br>[test_renderer_template_manager.py](../../tests/test_renderer_template_manager.py)<br>[test_renderer_exam_renderer.py](../../tests/test_renderer_exam_renderer.py)<br>[test_renderer_exam_render_service.py](../../tests/test_renderer_exam_render_service.py)<br>[test_renderer_exam_package_renderer.py](../../tests/test_renderer_exam_package_renderer.py)<br>[test_renderer_namespace_assigner.py](../../tests/test_renderer_namespace_assigner.py) |
| **Workspace Export** | N/A | [src/workspace/](../../src/workspace/) | [test_exam_export.py](../../tests/test_exam_export.py)<br>[test_workspace_draft.py](../../tests/test_workspace_draft.py) |
| **Importer** | [import_pipeline_spec_v1.0.md](../draft/import_pipeline_spec_v1.0.md) | [src/importer/](../../src/importer/) | N/A |
| **Sandbox Environment** | [sandbox_compile_spec_v1.0.md](../draft/sandbox_compile_spec_v1.0.md) | (Planned) | N/A |
| **GUI Subsystem** | [gui_workflow_spec_v1.0.md](../draft/gui_workflow_spec_v1.0.md) | [src/gui/](../../src/gui/) | N/A |

---

## 5. Workflow Stages

Engineering modifications progress through the following stages:
1. **Planning**: Copy the [implementation_plan_template.md](../templates/implementation_plan_template.md) to create an Implementation Plan for the proposed task.
2. **Triage**: Classify the proposed tasks into Class A (Behavior-Preserving) or Class B (Behavior-Changing) per the [engineering_change_governance_policy.md](engineering_change_governance_policy.md). Document the rationales or complete the Testing Impact Analysis (TIA-1 through TIA-5) for Class B changes.
3. **Approval**: Submit the Implementation Plan for review. Development begins after the plan is approved by the architecture owner.
4. **Implementation**: Modify codebase files and write associated tests based on the approved Implementation Plan. If implementation details deviate from the plan, update the plan and seek re-approval.
5. **Verification**: Run `pytest` and execute the validation checks outlined in the approved plan to verify correctness.
6. **Sprint Close & Retrospective**: Conclude the task by resolving findings and documenting retrospective observations in [docs/retrospectives/](../retrospectives/).

---

## 6. Repository Documents

Contributors refer to the following canonical repository documents:
- [README.md](../../README.md): High-level system entry, architecture layout, and reading order.
- [engineering_change_governance_policy.md](engineering_change_governance_policy.md): Canonical policy governing testing impact requirements.
- [environment_setup.md](environment_setup.md): Guides configuration of python environments and verification commands.
- [implementation_plan_template.md](../templates/implementation_plan_template.md): Template for creating Sprint Implementation Plans.
- [api_snapshot.md](../api_snapshot.md): Core data models and schema snapshot reference.
- [current_status.md](../current_status.md): Repository focus guidelines, tensions, and handoff instructions.
- [finding_registry.md](finding_registry.md): Canonical index of Governance Findings and their lifecycle status.

---

## 7. Contributor Rules

- **Repository-First**: The existing repository organization is the authoritative engineering source. Avoid inventing files, structures, or policies not defined in the repository.

- **Single Responsibility**: This document focuses on navigation and contributor orientation; it does not define or duplicate governance policies.

- **Obedience to Approved Plans**: Development is guided by the approved Implementation Plan. If the implementation details deviate, update the plan and seek re-approval.

- **Change Triage Compliance**: Classify tasks according to the change classification model. Behavior-changing changes require completing the TIA framework in the Implementation Plan.

- **Repository Knowledge Consistency**: Keep repository knowledge synchronized. Whenever an engineering change affects the accuracy, authority, lifecycle, or discoverability of repository knowledge, update the corresponding repository artifacts as part of the same engineering change. Repository indexes and registries shall remain consistent with the artifacts they reference.

- **Verification Completion**: Run tests and complete validation checklists to verify implementation correctness before concluding a task.

- **AI Handoff Preservation**: Ensure repository knowledge remains sufficient for subsequent engineering sessions, including independent AI contributors starting from a cold session.
