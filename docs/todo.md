# SciForge-Edu Development Backlog

Status: Active

Last Updated: 2026-05-29

# Priority 1

## Knowledge Point Architecture v0.1

Status:

Pending

Purpose:

Introduce curriculum-independent knowledge point identifiers.

Expected impact:

* Analysis
* RepositoryIndex
* Repository Query
* Canonical Repository Design
* AI Question Generation

Notes:

Must be designed before large-scale repository population.

## Physics Foundation Workflow Validation

Status:

Pending

Purpose:

Validate repository workflow using a canonical repository.

Validation targets:

* repository ergonomics
* persistence workflow
* index projection
* repository query behavior
* AI readability

# Priority 2

## Curriculum Mapping Architecture

Status:

Pending

Purpose:

Map questions to curriculum standards.

Candidate sources:

* 114 國中自然課程架構
* learning content codes

Examples:

* Da-IV-1
* Ea-IV-1
* Ja-IV-1

## Repository Query v2

Status:

Pending

Current gap:

RepositoryManager.search() currently supports:

* uuid
* question_type

Future support:

* subject
* chapter
* tags
* difficulty_level
* knowledge_codes
* curriculum_codes

# Priority 3

## Usage Metadata Architecture

Status:

Pending

## Assessment Statistics Architecture

Status:

Pending

## Repository Analytics

Status:

Pending

# Deferred

## Commit Suffix Automation

Status:

Deferred

Reason:

AI reconstruction relies on:

* docs/api_snapshot.md

Commit-message metadata is considered secondary.
