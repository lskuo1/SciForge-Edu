# Compliance Evaluation Report Template

## Purpose

This template records one execution of a compliance test defined in the [Compliance Test Catalog](../compliance_tests/compliance_test_index.md).

The [AI Compliance Test Framework](../ai_compliance_test_framework.md) (ACTF) is authoritative for evaluation methodology, evidence requirements, findings, and compliance states.

A completed evaluation report records only observable evidence and evaluation results. It shall not request, record, or evaluate internal reasoning.

## Report Identification

- **Report Identifier**:
- **Compliance Test Identifier**:
- **Compliance Test Revision**:
- **Evaluator**:
- **Evaluation Date and Time**:

## Evaluation Subject

- **Repository Snapshot**:
- **Governance Artifact Versions**:
- **Evaluation Task**:
- **Contributor Type**:
- **Evaluation Environment**:

## Initial Conditions

Record how the initial conditions defined by the compliance test were established.

Include:

- repository revision;
- permitted context;
- starting location;
- available tools;
- permitted inputs;
- any deviations from the test definition.

## Procedure Observations

Record observable contributor behavior in chronological order.

Do not infer or record internal reasoning.

| Step / Time | Observable Action or Output | Evidence ID | Environment Event or Deviation |
| :--- | :--- | :--- | :--- |
| | | | |

## Evidence

Record all evidence required for independent review and reproduction.

| Evidence ID | Evidence Type | Description or Repository Location | Collection Method |
| :--- | :--- | :--- | :--- |
| | | | |

Evidence may include:

- repository artifacts consulted;
- contributor responses;
- observable actions;
- command results;
- repository modifications;
- environment events.

## Criterion-Level Analysis

Evaluate every pass criterion and applicable failure indicator defined by the compliance test.

Use only:

- `Satisfied`
- `Not Satisfied`
- `Undetermined`

for criterion-level observations.

| Criterion or Indicator | Observation | Evidence ID(s) | Criterion Status |
| :--- | :--- | :--- | :--- |
| | | | |

Criterion observations are not ACTF result states.

## Result

- **ACTF Compliance State**:
  - `PASS`
  - `FAIL`
  - `INCONCLUSIVE`

- **Result Rationale**:

Exactly one ACTF compliance state shall be assigned.

`INCONCLUSIVE` is neither success nor failure.

No additional result states, scores, or partial-credit evaluations are permitted.

## Governance Findings

Record governance findings identified during the evaluation.

Use the repository's established finding management process.

| Finding Reference | Observation | Supporting Evidence | Status or Tracking Reference |
| :--- | :--- | :--- | :--- |
| | | | |

## Limitations

Record evidence gaps, environmental constraints, scope boundaries, or other factors affecting interpretation or reproducibility.

## Follow-Up

Record recommended follow-up actions without redefining repository governance or finding management.

| Action | Owner | Tracking Reference |
| :--- | :--- | :--- |
| | | | |