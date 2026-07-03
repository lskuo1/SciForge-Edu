# Compliance Test Template

## Purpose

This document provides the standard template for authoring individual governance compliance tests in SciForge-Edu.

Every compliance test shall use this structure to ensure consistency with the [AI Compliance Test Framework](../ai_compliance_test_framework.md) (ACTF), which is authoritative for compliance-test methodology, observable behavior, evidence requirements, evaluation procedures, and result states.

## Identifier

`CT-NNN`

Assign the next available compliance test identifier defined by the Compliance Test Catalog.

## Objective

State the bounded repository governance capability being evaluated.

The objective shall evaluate repository governance rather than contributor intelligence or implementation quality.

## Governance Property

Identify the applicable governance property or properties defined by the [Repository Governance Assurance Model](../repository_governance_assurance_model.md) (RGAM).

## Repository Artifacts

List the repository artifacts that establish the governing expectations for this evaluation.

Use repository-relative links whenever applicable and distinguish authoritative artifacts from supporting references.

## Initial Conditions

Define the repository snapshot, evaluation environment, available tools, permitted inputs, and starting context.

Exclude hidden conversation history, unpublished repository knowledge, prompt engineering, or any information unavailable from the repository itself.

## Evaluation Procedure

Provide an ordered, reproducible evaluation procedure.

Each step shall specify observable evaluator actions and recorded observations.

Do not request, record, or evaluate internal reasoning.

## Expected Observable Behavior

Describe the externally observable behavior expected from a compliant contributor.

Examples include:

- discovering governing artifacts;
- selecting the appropriate authorities;
- reconstructing the required workflow;
- producing required repository artifacts;
- collecting required evidence.

Do not describe hidden reasoning or internal decision processes.

## Required Evidence

List the concrete, reproducible evidence required to evaluate the test.

Evidence may include:

- consulted repository artifacts;
- generated repository artifacts;
- contributor responses;
- observable actions;
- repository modifications;
- environment events.

Evidence shall be reviewable without access to internal reasoning.

## Pass Criteria

List the objective conditions that must all be satisfied for the evaluation result to be `PASS`.

Each condition shall be traceable to the expected observable behavior and the governing repository artifacts.

## Failure Indicators

List the observable violations that result in a `FAIL`.

Include actions, omissions, or contradictions that demonstrate non-compliance with repository governance.

Distinguish demonstrated violations from missing or unusable evidence.

## Possible Inconclusive Conditions

List the conditions under which available evidence is insufficient to determine compliance.

Typical examples include:

- missing required repository artifacts;
- incomplete evaluation records;
- environment failures;
- unavailable required tools.

An inconclusive evaluation is neither success nor failure.

Every execution shall produce exactly one ACTF result state:

- `PASS`
- `FAIL`
- `INCONCLUSIVE`