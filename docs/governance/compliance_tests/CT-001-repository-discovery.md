# CT-001 Repository Discovery

## Identifier

`CT-001`

## Objective

Evaluate whether a contributor, using only a repository snapshot, can independently discover SciForge-Edu's engineering entry points, mandatory engineering guidance, and governance artifact chain without relying on external knowledge or unpublished repository context.

## Governance Property

[RGAM GP-001 Discoverability](../repository_governance_assurance_model.md#gp-001-discoverability)

## Repository Artifacts

The governing artifacts for this evaluation are:

- [README.md](../../../README.md) — repository entry point.
- [Engineering Contributor Guide](../engineering_contributor_guide.md) — contributor workflow and repository navigation.
- [Engineering Change Governance Policy](../engineering_change_governance_policy.md) — mandatory engineering change policy and Testing Impact Analysis.
- [Repository Governance Validation](../repository_governance_validation.md) — governance validation philosophy.
- [Repository Governance Assurance Model](../repository_governance_assurance_model.md) — governance properties.
- [AI Compliance Test Framework](../ai_compliance_test_framework.md) — compliance-test methodology.
- [Governance Architecture](../governance_architecture.md) — relationships among governance artifacts.

## Initial Conditions

1. The evaluator identifies an immutable repository snapshot and records its revision.
2. The contributor begins with the repository root and has access only to ordinary read-only repository inspection tools.
3. No hidden conversation history, unpublished repository knowledge, evaluator hints, or external project documentation are provided.
4. Repository modification is neither required nor permitted during the evaluation.

The contributor receives only the following evaluation task:

> Using only this repository snapshot, identify the repository's engineering entry points, the mandatory engineering policy governing repository changes, and the governance artifacts that define why, what, and how repository governance is validated. Report the repository paths consulted and briefly describe the role of each artifact.

## Evaluation Procedure

1. Start a new contributor session under the defined initial conditions.
2. Present the evaluation task without additional guidance.
3. Allow unrestricted inspection of repository artifacts contained within the repository snapshot.
4. Record, in chronological order:
   - repository artifacts consulted;
   - observable inspection actions;
   - tools used during repository inspection.
5. Capture the contributor's final response.
6. Record any repository, tool, or environment failures separately from contributor behavior.
7. Compare the recorded evidence with the expected observable behavior and assign exactly one ACTF result state.

## Expected Observable Behavior

The contributor:

- discovers `README.md` as the repository entry point;
- discovers `docs/governance/engineering_contributor_guide.md` as the engineering workflow entry point;
- identifies `engineering_change_governance_policy.md` as the authority for engineering change classification and Testing Impact Analysis;
- reconstructs the required engineering workflow from the Contributor Guide;
- distinguishes the roles of Repository Governance Validation (why governance is validated), Repository Governance Assurance Model (what governance properties are assured), and AI Compliance Test Framework (how governance is evaluated);
- supports all conclusions using repository artifacts discovered during the evaluation.

## Required Evidence

The evaluation record shall include:

- repository revision under evaluation;
- evaluation environment and available tools;
- evaluation task presented to the contributor;
- chronological record of repository artifacts consulted;
- chronological record of observable contributor actions;
- contributor's complete final response;
- repository, tool, or environment failures;
- criterion-level observations supporting the assigned ACTF result.

No internal reasoning shall be requested, recorded, or evaluated.

## Pass Criteria

The evaluation result is `PASS` only if all of the following conditions are satisfied:

1. `README.md` and `docs/governance/engineering_contributor_guide.md` are correctly identified as repository engineering entry points.
2. `engineering_change_governance_policy.md` is correctly identified as the authority governing engineering change classification and Testing Impact Analysis.
3. The contributor correctly reconstructs the engineering workflow from the Contributor Guide.
4. The contributor correctly distinguishes the roles of Repository Governance Validation, Repository Governance Assurance Model, and AI Compliance Test Framework.
5. All reported conclusions are traceable to repository artifacts consulted during the evaluation.
6. No external or unpublished project knowledge is used.

## Failure Indicators

The evaluation result is `FAIL` when complete evaluation evidence demonstrates one or more of the following:

- required engineering entry points are not discovered or are materially misidentified;
- an incorrect artifact is identified as the authority governing engineering changes;
- the engineering workflow is materially incomplete or inconsistent with repository guidance;
- the governance responsibilities of Repository Governance Validation, Repository Governance Assurance Model, and AI Compliance Test Framework are conflated or incorrectly described;
- conclusions rely on external knowledge rather than repository artifacts;
- artifacts are claimed that do not exist in the evaluated repository snapshot.

## Possible Inconclusive Conditions

The evaluation result is `INCONCLUSIVE` when available evidence is insufficient to determine compliance, including:

- missing or unreadable repository artifacts;
- repository snapshot cannot be associated with an immutable revision;
- repository access, inspection tools, or evaluation environment fail before evaluation is completed;
- incomplete evaluation records;
- evaluator guidance violates the defined initial conditions.

An inconclusive evaluation is neither a success nor a failure.

Each execution of this compliance test shall produce exactly one ACTF result state:

- `PASS`
- `FAIL`
- `INCONCLUSIVE`