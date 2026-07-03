# Compliance Test Catalog

## Purpose

This catalog is the repository entry point for governance compliance test definitions in SciForge-Edu.

It organizes the compliance tests defined for the repository and provides a stable index for discovering individual test specifications.

The [AI Compliance Test Framework](../ai_compliance_test_framework.md) (ACTF) is the authoritative specification for compliance-test methodology, required structure, evidence requirements, evaluation procedures, and result states. This catalog applies that framework but does not redefine it.

## Authority Boundary

This document defines and indexes **compliance test definitions only**.

It is subordinate to the ACTF and does not replace, amend, or redefine:

- the AI Compliance Test Framework (ACTF);
- the Repository Governance Validation (RGV) philosophy;
- the Repository Governance Assurance Model (RGAM);
- the Engineering Contributor Guide;
- the repository engineering workflow.

## Test Definitions and Test Executions

This catalog contains only **test definitions**.

A test definition specifies:

- objective;
- evaluation procedure;
- expected behavior;
- required evidence.

Test execution is a separate activity.

Executing a compliance test produces observable evidence and exactly one ACTF result state. Execution evidence, observations, findings, and conclusions belong in an evaluation report created from the [Evaluation Report Template](../templates/evaluation_report_template.md).

The presence of a test definition in this catalog does **not** imply that the test has been executed or that any repository snapshot has passed or failed it.

## Organization and Identifier Convention

Each compliance test is maintained as an individual Markdown document in this directory.

Compliance test identifiers follow the format:

`CT-NNN`

where `NNN` is a zero-padded sequential identifier beginning with `001`.

Test definition files use the naming convention:

`CT-NNN-short-title.md`

New compliance tests shall be authored from the [Compliance Test Template](compliance_test_template.md) to ensure consistency with ACTF.

## Indexed Compliance Tests

| Identifier | Title | Evaluation Domain | Test Definition |
| :--- | :--- | :--- | :--- |
| CT-001 | Repository Discovery | Repository Discovery | [CT-001 Repository Discovery](CT-001-repository-discovery.md) |

## Long-term Evolution

This catalog is intended to evolve as repository governance matures.

New compliance tests may be introduced when additional governance capabilities require formal evaluation.

Every new compliance test shall:

- conform to the AI Compliance Test Framework (ACTF);
- be created from the Compliance Test Template;
- be added to this catalog after approval through the repository governance process.