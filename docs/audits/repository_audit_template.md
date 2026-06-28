# Repository Reality Audit Template

Version: 0.1

Status: Draft

---

# Purpose

This template defines the standard format for auditing a software repository.

The objective of a repository audit is to describe the current reality of the repository, identify gaps between the current state and the intended architecture, and recommend the next engineering priorities.

An audit records observations.

It should not directly modify the repository.

---

# Audit Metadata

Repository:

Audit Date:

Repository Commit:

Auditor:

Audit Version:

Knowledge Kernel Version:

---

# 1. Executive Summary

Provide a concise summary of the repository.

Include:

* Overall repository maturity
* Overall architectural quality
* Overall documentation quality
* Major strengths
* Major risks

---

# 2. Repository Purpose

Describe the current purpose of the repository.

Questions:

* What problem is the repository solving?
* What development phase is it currently in?
* Does the current implementation match the stated purpose?

---

# 3. Repository Structure

Describe the current repository organization.

Evaluate:

* directory structure
* naming consistency
* separation of concerns
* discoverability

---

# 4. Documentation Reality

Review all important documentation.

Identify:

* canonical documents
* duplicated documents
* outdated documents
* missing documents

Do not recommend solutions in this section.

---

# 5. Implementation Reality

Describe the current implementation.

Examples:

* implemented modules
* experimental modules
* unfinished components
* deprecated components

---

# 6. Documentation Drift

Identify differences between:

Documentation

↓

Implementation

Examples include:

* outdated documentation
* undocumented implementation
* conflicting descriptions

---

# 7. Architecture Gaps

Identify architectural weaknesses.

Examples:

* missing models
* missing specifications
* missing governance
* duplicated responsibilities
* unclear ownership

---

# 8. Knowledge Gaps

Identify engineering knowledge that is currently not preserved inside the repository.

Examples:

* design decisions
* architectural rationale
* workflow knowledge
* AI conversation knowledge

---

# 9. Priority Recommendations

Classify recommendations.

## P0

Critical.

Must be addressed immediately.

---

## P1

Important.

Should be addressed in the next sprint.

---

## P2

Long-term improvements.

---

# 10. Recommended Next Sprint

Define:

Sprint Goal

Deliverables

Expected Validation

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
