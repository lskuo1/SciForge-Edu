# Governance Finding Registry

## Purpose

The Governance Finding Registry is the canonical index of all Governance Findings maintained by the SciForge-Edu repository.

Governance Findings record repository-level engineering observations discovered during architecture reviews, governance validation, engineering activities, implementation, verification, or retrospectives.

Unlike Sprint Retrospectives, Governance Findings are intended to persist across multiple sprints and may become inputs to future Architecture Proposals, Implementation Plans, Execution Contracts, governance improvements, or repository engineering decisions.

A Governance Finding documents:

- an observed repository governance issue or insight;
- supporting evidence;
- engineering impact;
- recommendations;
- lifecycle status.

A Governance Finding is **not**:

- a defect report;
- an implementation task;
- an Architecture Decision Record (ADR);
- an Architecture Proposal;
- an Execution Contract;
- a Sprint Retrospective.

---

## Lifecycle

Observation

↓

Governance Finding

↓

Referenced by future repository artifacts

↓

Addressed by a future Sprint (if applicable)

↓

Resolved

↓

Closed

---

## Maintenance

This registry is the canonical index of all Governance Findings.

The registry shall be updated whenever:

- a new Governance Finding is introduced;
- a Governance Finding is renamed;
- the status of a Governance Finding changes;
- a Governance Finding is resolved;
- a Governance Finding is closed.

The contributor introducing or modifying a Governance Finding is responsible for keeping this registry synchronized.

The registry and all Governance Finding documents shall always remain consistent.

Repository artifacts referencing Governance Findings should reference the corresponding Finding identifier rather than duplicating the Finding contents.

---

## Finding Status

| Finding | Title | Status | Introduced | Resolved |
|----------|-------|--------|------------|----------|
| GF-005-001 | Repository Rediscovery significantly improves AI repository alignment | Open | Sprint 005 | — |
| GF-005-002 | Engineering Execution Proposal lacks a well-defined repository boundary | Open | Sprint 005 | — |
| GF-005-003 | Repository architecture changes require explicit authorization | Open | Sprint 005 | — |

---

## Relationship to Other Governance Artifacts

Governance Findings complement the existing repository governance artifacts.

Governance Findings may be referenced by:

- Architecture Proposals;
- Implementation Plans;
- Execution Contracts;
- Sprint Retrospectives;
- Repository Governance Validation (RGV);
- Repository Governance Assurance Model (RGAM);
- AI Compliance Test Framework (ACTF).

Governance Findings do not replace these artifacts.

Instead, they preserve repository-level engineering knowledge that may remain relevant across multiple sprints.