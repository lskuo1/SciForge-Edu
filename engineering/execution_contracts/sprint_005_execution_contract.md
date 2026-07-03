# Approved Execution Contract (Version 1.1.2)
# Sprint 005 — Repository Governance Validation Assets

## Document Metadata

* **Title**: Sprint 005 — Repository Governance Validation Assets Approved Execution Contract
* **Version**: 1.1.2
* **Status**: Approved
* **Based On**: `docs/sprints/sprint_005_architecture_proposal.md`
* **Governing Policy**: `docs/governance/engineering_change_governance_policy.md`
* **Contributor Workflow**: `docs/governance/engineering_contributor_guide.md`
* **Produced With**: OpenAI Codex
* **Approval Date**: 2026-07-01
* **Revision Date**: 2026-07-02
* **Previous Approved Version**: Version 1.0 at `engineering/execution_contracts/sprint_005_execution_contract.md`
* **Current Implementation Authority**: This document, `engineering/execution_contracts/sprint_005_execution_contract.md`

---

## Purpose

This document is the approved Execution Contract for the remaining Sprint 005 work.

Version 1.1.2 is a behavior-preserving refinement of Version 1.0. It clarifies execution dependencies, read-only authorities, stop-work conditions, and readiness evidence without changing Sprint 005 authority, scope, deliverables, TIA decisions, verification requirements, rollback rules, or acceptance criteria.

For Sprint 005 implementation, this document is the current implementation authority. Version 1.0 remains preserved as the previous approved baseline.

It records the Architecture Owner's approval and authorizes only the implementation activities defined below.

The plan defines the repository changes required to implement Phase B of the reviewed Sprint 005 Architecture Proposal: the initial Compliance Test Catalog, Compliance Test Template, CT-001 Repository Discovery test, and Evaluation Report Template.

Phase A governance-foundation artifacts already present in the repository are implementation inputs, not deliverables to be recreated by this plan. Runtime features, compliance automation, execution of CT-001, and production of an evaluation report are outside this plan.

Implementation shall strictly follow this contract. If implementation cannot follow this contract, implementation shall stop and request approval before introducing any deviation.

---

## 1. Repository Impact Analysis

* **Overall Repository Impact**: Adds the four documentation assets specified by Phase B of the Sprint 005 Architecture Proposal. These assets operationalize the existing governance architecture by defining a catalog entry point, a reusable compliance-test structure, one concrete repository-discovery test, and a reusable evaluation-report structure.
* **Runtime Impact**: None. No files under `src/`, runtime configuration, public API, data model, parser, renderer, repository query behavior, or executable tooling will change.
* **Documentation Impact**: Creates four Markdown files under the two directories already specified by the Sprint 005 Architecture Proposal. At sprint close, creates the required Sprint 005 retrospective. No existing governance artifact will be modified under this plan.
* **Test Impact**: No Python tests will be added or changed. The planned assets establish governance evaluation behavior that has no applicable executable test coverage in the current repository. Verification will therefore use the manual governance, consistency, structure, and cold-start checks defined in Section 5.
* **Governance Impact**: Introduces normative operational assets beneath the existing RGV → RGAM → ACTF architecture. The changes define observable evaluation procedures and evidence formats but do not amend the engineering workflow or the responsibilities of existing governance artifacts.
* **Scope Boundary**: This plan covers Phase B governance validation assets only. It excludes Phase A recreation, runtime implementation, validation scripts, hooks, CI changes, usage metadata, statistics features, repository implementation, ACTF modification, execution of a compliance evaluation, and Sprint 006 work.

---

## 2. Repository Changes

### Files to Create

1. **Compliance Test Catalog**
   * *Path*: `docs/governance/compliance_tests/compliance_test_index.md`
   * *Why*: Provides the authoritative catalog entry point, explains the relationship between ACTF and individual compliance tests, defines catalog organization and identifier conventions, and indexes CT-001 without duplicating ACTF responsibilities.

2. **Compliance Test Template**
   * *Path*: `docs/governance/compliance_tests/compliance_test_template.md`
   * *Why*: Provides a repeatable structure for individual compliance tests using every field required by ACTF: Identifier, Objective, Governance Property, Repository Artifacts, Initial Conditions, Evaluation Procedure, Expected Observable Behavior, Required Evidence, Pass Criteria, Failure Indicators, and Possible Inconclusive Conditions.

3. **CT-001 Repository Discovery**
   * *Path*: `docs/governance/compliance_tests/CT-001-repository-discovery.md`
   * *Why*: Defines the first concrete compliance test for evaluating whether a contributor can discover the repository's engineering entry points and governance artifacts from the repository snapshot alone.

4. **Evaluation Report Template**
   * *Path*: `docs/governance/templates/evaluation_report_template.md`
   * *Why*: Provides a reproducible evidence record for a compliance-test execution, including evaluation subject, snapshot, procedure observations, evidence, findings, and exactly one ACTF result state: PASS, FAIL, or INCONCLUSIVE.

5. **Sprint 005 Retrospective**
   * *Path*: `docs/retrospectives/retrospective_sprint_005.md`
   * *Why*: Satisfies the Contributor Guide's Sprint Close & Retrospective stage after implementation and verification. It will record outcomes, deviations, findings, and process improvements; it must not be created before those observations exist.

### Files to Modify

None planned.

If implementation or verification shows that an existing governance artifact must change, work must stop and the approved scope must be revised and re-approved before that modification occurs.

### Files to Delete

None.

---

## 3. Task Breakdown

### Task 1: Establish the Compliance Test Catalog

* **Objective**: Create the catalog entry point and define how independently maintained compliance tests are organized and discovered.
* **Affected Files**: `docs/governance/compliance_tests/compliance_test_index.md`
* **Expected Outcome**: Contributors can identify the catalog's purpose, governing framework, test naming convention, available tests, and boundary from evaluation reports.
* **Completion Criteria**:
  * The catalog identifies ACTF as the authority for compliance-test methodology and structure.
  * The catalog indexes CT-001 by identifier, title, evaluation domain, and relative link.
  * The catalog distinguishes test definitions from test executions and evaluation reports.
  * The catalog does not redefine RGV philosophy, RGAM properties, ACTF methodology, or the engineering workflow.

#### Testing Impact Analysis (TIA)

* **Triage**: Class B (Behavior-Changing)
* **TIA-1 (Behavior Change)**: The repository gains an authoritative operational entry point for discovering executable governance test definitions and their identifiers.
* **TIA-2 (Verification Context)**: No existing automated test verifies compliance-catalog discovery, indexing, authority boundaries, or links. Existing governance documents describe the intended architecture but do not test this new asset.
* **TIA-3 (Sufficiency)**: Existing tests are not sufficient.
* **TIA-4 (Insufficiency Details)**: The current Python suite verifies runtime behavior and cannot establish the semantic correctness, discoverability, or authority boundaries of a new governance catalog.
* **TIA-5 (Engineering Decision)**: *No applicable tests exist.*
  * *Rationale*: This change introduces a governance documentation contract rather than executable software behavior. Manual structural, link, authority, and cold-start validation in Section 5 is the applicable verification method.

---

### Task 2: Create the Compliance Test Template

* **Objective**: Translate ACTF's required compliance-test structure into a reusable authoring template without changing ACTF.
* **Affected Files**: `docs/governance/compliance_tests/compliance_test_template.md`
* **Expected Outcome**: Future compliance tests can be authored consistently and contain all evidence and result criteria required by ACTF.
* **Completion Criteria**:
  * Every field listed in ACTF's `Compliance Test Structure` is represented explicitly.
  * Instructions distinguish expected observable behavior, required evidence, pass criteria, failure indicators, and inconclusive conditions.
  * The template remains contributor-independent and repository-first.
  * The template does not introduce scoring or result states beyond PASS, FAIL, and INCONCLUSIVE.

#### Testing Impact Analysis (TIA)

* **Triage**: Class B (Behavior-Changing)
* **TIA-1 (Behavior Change)**: The repository gains a normative structure that governs how future compliance tests are specified and what evidence each test must request.
* **TIA-2 (Verification Context)**: No existing automated test checks the completeness or semantic alignment of compliance-test documents with ACTF.
* **TIA-3 (Sufficiency)**: Existing tests are not sufficient.
* **TIA-4 (Insufficiency Details)**: Runtime tests do not inspect governance document fields, contributor independence, or ACTF terminology.
* **TIA-5 (Engineering Decision)**: *No applicable tests exist.*
  * *Rationale*: Correctness depends on exact structural and semantic conformance to ACTF. The Section 5 traceability matrix and manual consistency review provide the applicable evidence.

---

### Task 3: Define CT-001 Repository Discovery

* **Objective**: Define a bounded, reproducible compliance test for repository discovery using observable contributor behavior.
* **Affected Files**: `docs/governance/compliance_tests/CT-001-repository-discovery.md`
* **Expected Outcome**: CT-001 can be independently executed against a defined repository snapshot to evaluate discoverability and produce reproducible evidence.
* **Completion Criteria**:
  * CT-001 conforms to every required field in the Compliance Test Template and ACTF.
  * The test maps explicitly to RGAM GP-001 Discoverability and identifies supporting governance artifacts.
  * Initial conditions exclude hidden conversation history and unpublished repository knowledge.
  * The procedure evaluates observable discovery behavior and does not attempt to evaluate internal reasoning or model intelligence.
  * Required evidence is concrete and reproducible.
  * PASS, FAIL, and INCONCLUSIVE conditions are mutually distinguishable and consistent with ACTF.
  * The test remains a definition only; it is not executed during Sprint 005.

#### Testing Impact Analysis (TIA)

* **Triage**: Class B (Behavior-Changing)
* **TIA-1 (Behavior Change)**: The repository gains its first operational governance test, including a procedure and normative criteria for determining repository-discovery compliance.
* **TIA-2 (Verification Context)**: No existing automated test verifies CT-001 because the compliance test and its evaluation criteria do not yet exist. RGV, RGAM, and ACTF provide design constraints rather than executable coverage.
* **TIA-3 (Sufficiency)**: Existing tests are not sufficient.
* **TIA-4 (Insufficiency Details)**: Existing tests cannot validate whether CT-001 is reproducible, contributor-independent, based only on observable behavior, or correctly mapped to GP-001.
* **TIA-5 (Engineering Decision)**: *No applicable tests exist.*
  * *Rationale*: CT-001 is itself a governance test definition, not runtime code. Template conformance, governance traceability, scenario walkthrough, and cold-start review are the applicable verification methods.

---

### Task 4: Create the Evaluation Report Template

* **Objective**: Define a reusable record for compliance-test execution evidence, results, and governance findings.
* **Affected Files**: `docs/governance/templates/evaluation_report_template.md`
* **Expected Outcome**: Independent evaluators can record enough context and evidence to reproduce and review a compliance result.
* **Completion Criteria**:
  * The template records repository snapshot, governance artifact versions, evaluation task, contributor type, and evaluation environment.
  * The template records procedure observations and evidence without requiring hidden reasoning.
  * The result requires exactly one ACTF state: PASS, FAIL, or INCONCLUSIVE.
  * The template provides fields for criterion-level analysis, governance findings, limitations, and follow-up without redefining finding management.
  * The template is usable with CT-001 and remains generic enough for later catalog tests.

#### Testing Impact Analysis (TIA)

* **Triage**: Class B (Behavior-Changing)
* **TIA-1 (Behavior Change)**: The repository gains a normative evidence and reporting format for governance compliance evaluations.
* **TIA-2 (Verification Context)**: No existing automated test verifies governance evaluation reports or their alignment with ACTF's evaluation-subject, evidence, and result requirements.
* **TIA-3 (Sufficiency)**: Existing tests are not sufficient.
* **TIA-4 (Insufficiency Details)**: Runtime tests cannot establish whether a report template captures sufficient reproducibility context or preserves ACTF result semantics.
* **TIA-5 (Engineering Decision)**: *No applicable tests exist.*
  * *Rationale*: Manual field traceability and a dry walkthrough using CT-001 are the applicable verification methods. The walkthrough must not be recorded as an actual CT-001 evaluation.

---

### Task 5: Verify the Governance Asset Set

* **Objective**: Verify the four Phase B assets as one internally consistent governance system before sprint close.
* **Affected Files**: No repository files are changed by verification. The four created governance assets are inspected as verification inputs.
* **Expected Outcome**: Recorded verification evidence demonstrates architectural alignment, structural completeness, valid links, scope compliance, and cold-start usability.
* **Completion Criteria**:
  * Every validation check in Section 5 has an explicit pass/fail result.
  * All four Phase B success criteria in the Architecture Proposal are satisfied.
  * No runtime or out-of-scope file has changed.
  * Any failed check is resolved within approved scope or raised for plan revision and re-approval.

#### Testing Impact Analysis (TIA)

* **Triage**: Class A (Behavior-Preserving)
* **Engineering Rationale**: This task observes and records whether planned assets conform to their approved requirements; it does not itself modify repository behavior. Existing runtime tests remain sufficient for confirming that verification activity introduces no runtime change, while the manual checks in Section 5 assess the governance assets.

---

### Task 6: Complete the Sprint 005 Retrospective

* **Objective**: Record implementation outcomes, verification results, deviations, governance findings, and process improvements after all implementation and verification work is complete.
* **Affected Files**: `docs/retrospectives/retrospective_sprint_005.md`
* **Expected Outcome**: Sprint 005 closes with a durable retrospective record as required by the Contributor Guide.
* **Completion Criteria**:
  * The retrospective is created only after verification is complete.
  * It records actual outcomes rather than restating planned outcomes.
  * It identifies deviations from the approved authorization, or explicitly records that none occurred.
  * It records unresolved findings and recommended follow-up ownership without expanding Sprint 005 scope.

#### Testing Impact Analysis (TIA)

* **Triage**: Class A (Behavior-Preserving)
* **Engineering Rationale**: The retrospective records completed engineering observations and does not alter runtime behavior, governance rules, or compliance criteria. Existing tests are sufficient; manual review verifies factual consistency with the completed sprint evidence.

---

## 4. Task Dependencies

| Task | Depends On | Dependency Rationale |
| :--- | :--- | :--- |
| Task 1 — Catalog | Sprint 005 Execution Contract | This canonical contract authorizes the task. |
| Task 2 — Test Template | Sprint 005 Execution Contract | ACTF already supplies the structural source; this canonical contract authorizes the task to proceed independently of Task 1. |
| Task 3 — CT-001 | Tasks 1 and 2 | CT-001 must use the approved template and be indexed by the catalog. |
| Task 4 — Report Template | Task 2 | The report must align with the evidence and result concepts used by compliance tests. |
| Task 5 — Verification | Tasks 1–4 | The complete asset set must exist before integrated validation. |
| Task 6 — Retrospective | Task 5 | Retrospective observations require completed verification evidence. |

```text
Canonical Sprint 005 Execution Contract
       ┌─────┴─────┐
       ↓           ↓
Task 1: Catalog  Task 2: Test Template
       └─────┬─────┘
             ↓
        Task 3: CT-001
             │
Task 2 ─────→ Task 4: Report Template
             │
             ↓
    Task 5: Integrated Verification
             ↓
       Task 6: Retrospective
```

Tasks 1 and 2 may be implemented independently after authorization. No other task may violate the dependencies above.

---

## 5. Validation Plan

### 5.1 Documentation Consistency

1. Cross-check the catalog and Compliance Test Template against ACTF's `Compliance Test Structure` and `Compliance States` sections.
2. Cross-check CT-001 against RGV's repository-first, observable-behavior, reproducibility, and controlled-workflow principles.
3. Cross-check CT-001's governance-property mapping against RGAM GP-001 Discoverability.
4. Cross-check all four assets against the artifact responsibilities and layer boundaries in `governance_architecture.md`.
5. Confirm terminology is consistent across RGV, RGAM, ACTF, the catalog, CT-001, and the Evaluation Report Template.
6. Confirm the new assets reference existing authorities rather than duplicating or silently modifying them.

### 5.2 Structural and Repository Validation

1. Confirm that exactly these Phase B assets exist at the proposal-defined paths:
   * `docs/governance/compliance_tests/compliance_test_index.md`
   * `docs/governance/compliance_tests/compliance_test_template.md`
   * `docs/governance/compliance_tests/CT-001-repository-discovery.md`
   * `docs/governance/templates/evaluation_report_template.md`
2. Verify relative Markdown links in all new assets resolve to repository files.
3. Verify CT-001 contains every field required by ACTF and the Compliance Test Template.
4. Verify the Evaluation Report Template covers every ACTF evaluation-subject field, evidence recording, and exactly one result state.
5. Inspect the repository diff and confirm no `src/`, `tests/`, scripts, CI, API snapshot, runtime configuration, or unrelated documentation changed.
6. Run the existing `pytest` suite as a regression baseline, as required by the Contributor Guide, while recognizing that it does not establish semantic correctness of the governance documents.

### 5.3 Governance Verification

1. Perform an artifact-responsibility review proving that:
   * RGV remains the statement of why governance is validated.
   * RGAM remains the statement of what governance qualities are assured.
   * ACTF remains the statement of how governance is evaluated.
   * The catalog contains individual test definitions.
   * The report template records evaluation evidence and results.
2. Perform a dry structural walkthrough of CT-001 with the Evaluation Report Template. This checks field compatibility only and must not be represented as execution of CT-001.
3. Perform a cold-start review to determine whether an independent contributor can locate the catalog, understand CT-001, identify its authorities, and determine the required evidence without hidden context.
4. Verify that all Class B TIA-1 through TIA-5 entries remain valid for the implementation actually performed.
5. Verify implementation remained within the approved Execution Contract; any deviation requires stop, revision, and re-approval before continuation.

### 5.4 Verification Closure

1. Preserve the completed verification checklist, final repository diff, `pytest` result, review observations, and governance findings as Sprint 005 verification evidence.
2. Require the Sprint 005 Retrospective to reference the preserved verification evidence and summarize the verification outcome.
3. Resolve governance findings that block the approved Sprint 005 acceptance criteria before closure.
4. Carry unresolved non-blocking governance findings forward according to the repository governance workflow, recording their status and follow-up ownership in the Sprint 005 Retrospective without expanding Sprint 005 scope.

### 5.5 Acceptance Evidence

Architecture Review requires the implementation phase to preserve:

* A completed checklist or review record for every validation item above.
* The final repository diff showing only authorized paths.
* The `pytest` command and result.
* Any governance findings raised during verification, including their resolution or carry-forward status.
* The Sprint 005 Retrospective, including references to the verification evidence, after verification completes.

---

## 6. Rollback Plan

* **Level 1: Revert a Single Task**: Remove only the new file created by the failed task, remove any catalog link that depends on it, and rerun all validation checks affected by that dependency. No existing governance authority is modified by this plan.
* **Level 2: Revert Sprint 005 Phase B**: Remove the four Phase B governance assets and the Sprint 005 retrospective through a reviewed version-control revert. Confirm that the Phase A governance foundation remains unchanged and that no broken references remain.
* **Level 3: Decommissioning / Adoption Rollback**: If the asset model proves architecturally unsuitable after adoption, suspend use of the catalog and report template, record a governance finding, and obtain a new approved plan before replacement. Existing RGV, RGAM, ACTF, Governance Architecture, Governance Policy, and Contributor Guide remain authoritative.

Rollback must use reviewed version-control changes. Destructive working-tree reset commands are not part of this plan.

---

## 7. Risk Assessment

| Risk Type | Description | Rank | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| Governance authority | New assets could duplicate or contradict RGV, RGAM, ACTF, or the Contributor Guide. | High | Treat existing artifacts as authorities; perform the responsibility and terminology cross-checks in Section 5. |
| Scope expansion | Implementation could drift into runtime features, automation, CI enforcement, governance rewrites, or actual Sprint 006 evaluation. | High | Enforce the explicit scope boundary and authorized path list; stop and seek re-approval for deviations. |
| Classification error | Treating operational governance documents as harmless documentation could omit required TIA reasoning. | Medium | Classify Tasks 1–4 as Class B and retain complete TIA-1 through TIA-5 analysis. |
| Test semantics | CT-001 criteria could be subjective, non-reproducible, or dependent on hidden context. | High | Require observable behavior, concrete evidence, explicit initial conditions, and distinct PASS/FAIL/INCONCLUSIVE conditions. |
| Template divergence | CT-001 or later tests could omit ACTF-required fields or use incompatible terminology. | Medium | Maintain a field-level traceability check from ACTF to the template and CT-001. |
| Report insufficiency | The Evaluation Report Template could omit snapshot or environment context needed to reproduce results. | High | Require all ACTF evaluation-subject fields and validate the template through a dry CT-001 structural walkthrough. |
| False validation claim | A template walkthrough could be misrepresented as an executed compliance evaluation. | Medium | Label it explicitly as structural verification; defer actual execution and reports to Sprint 006. |
| Link and naming drift | File names or links could differ from the reviewed Architecture Proposal. | Medium | Use the exact proposal-defined paths and run link and case-sensitivity checks. |
| Runtime regression | Unintended files could be modified even though runtime work is excluded. | Low | Inspect the final diff, prohibit runtime paths, and run the existing `pytest` suite as a regression baseline. |
| Unauthorized deviation | Implementation could depart from the approved scope or task controls. | High | Stop work, revise the contract, and obtain Architecture Owner re-approval before introducing any deviation. |

---

## 8. Acceptance Criteria

Sprint 005 Phase B is acceptable for closure only when all of the following are true:

1. The Architecture Owner approved the Implementation Plan, and implementation was performed only under the current approved Sprint 005 Execution Contract, Version 1.1.2, at `engineering/execution_contracts/sprint_005_execution_contract.md`.
2. The four Phase B governance assets exist at the exact paths specified by the Sprint 005 Architecture Proposal.
3. The Compliance Test Catalog clearly indexes CT-001 and preserves the authority boundary between ACTF, test definitions, and evaluation reports.
4. The Compliance Test Template contains every field required by ACTF.
5. CT-001 conforms to the template, maps to GP-001, uses repository-only initial conditions, evaluates observable behavior, requires reproducible evidence, and defines distinct PASS, FAIL, and INCONCLUSIVE conditions.
6. The Evaluation Report Template records all ACTF evaluation-subject fields, evidence, criterion analysis, findings, limitations, and exactly one ACTF result state.
7. Cross-document review finds no contradictory terminology, duplicated governance responsibility, circular authority, or broken repository link.
8. The final diff contains no runtime implementation, automation, test-suite modification, or other out-of-scope change.
9. The existing `pytest` suite completes successfully, or any environment-related inability to execute it is explicitly recorded and resolved according to the approved authorization.
10. Verification evidence is preserved and referenced by the Sprint 005 Retrospective; all blocking findings are resolved, and unresolved non-blocking governance findings are carried forward according to the repository governance workflow.
11. No compliance evaluation is claimed to have been executed and no evaluation report is produced as part of Sprint 005.

---

## Architecture Review

* **Independent Architecture Reviews**: Completed
* **Architecture Owner**: Approved
* **Architecture Owner Approval**: Granted
* **Approval Date**: 2026-07-01
* **Revision Date**: 2026-07-02
* **Previous Approved Version**: Version 1.0 at `engineering/execution_contracts/sprint_005_execution_contract.md`
* **Current Implementation Authority**: This document, `engineering/execution_contracts/sprint_005_execution_contract.md`
* **Required Revisions**: Completed; no outstanding revisions

This approved Version 1.1.2 document is the official Sprint 005 Execution Contract and the current canonical authorization for Sprint 005 implementation. Any deviation requires implementation to stop and the contract to be revised and re-approved before work continues.


---

# Appendix A — Execution Dependency

```text
Sprint 005 Execution Contract
       ┌─────┴─────┐
       ↓           ↓
Task 1: Compliance Test Catalog
Task 2: Compliance Test Template
       └─────┬─────┘
             ↓
Task 3: CT-001 Repository Discovery
             │
Task 2 ─────→ Task 4: Evaluation Report Template
             │
             ↓
Task 5: Integrated Verification
             ↓
Task 6: Sprint 005 Retrospective
```

# Appendix B — Execution Constraints

## Read-only Authorities

- Engineering Governance Policy
- Engineering Contributor Guide
- Governance Architecture
- Repository Governance Validation (RGV)
- Repository Governance Assurance Model (RGAM)
- AI Compliance Test Framework (ACTF)

## Authorized Paths

Implementation is limited to the five deliverables authorized by this Execution Contract.

## Stop-work Conditions

Implementation shall stop immediately if:
- an existing governance authority requires modification;
- a new repository artifact becomes necessary;
- an approved completion criterion cannot be satisfied;
- implementation exceeds the approved scope.

Work may resume only after the issue has been documented, the Execution Contract has been revised if required, and the revised contract has been formally re-approved by the Architecture Owner.

# Appendix C — Engineering Readiness

An independent Engineering Readiness Review may be performed before implementation as a verification activity. Any review outcome is informative evidence only and does not introduce additional contractual requirements or alter implementation authorization.

These appendices refine implementation guidance only. They do not alter Sprint 005 authority, scope, deliverables, TIA decisions, verification requirements, rollback rules, acceptance criteria, or implementation behavior.
