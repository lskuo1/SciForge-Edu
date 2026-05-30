# SciForge-Edu Development Backlog

Status: Active

Last Updated: 2026-05-29

# Priority 1

## Exam Generation MVP v0.1

Status:

Pending

Purpose:

Enable practical exam generation before large-scale repository architecture is completed.

Deliverables:

- Question storage
- Image storage
- Exam template system
- Answer sheet generation
- Solution generation
- XeLaTeX PDF generation

Success Criteria:

Question Repository
→ Template
→ Exam.tex
→ Answer.tex
→ Solution.tex
→ PDF

Notes:

Knowledge Points are optional metadata and must not block exam generation.

## Curriculum → Knowledge Point Mapping v0.1

Status:

Pending

Purpose:

Define how curriculum structures are transformed into Knowledge Points.

Expected impact:

- Knowledge Point Architecture
- Repository Design
- Curriculum Alignment
- AI Knowledge Extraction

Notes:

Curriculum is the source of truth.

Knowledge Points are derived artifacts.

## Knowledge Point Architecture v0.1

Status:

Draft Established

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

Dependency:

- Curriculum → Knowledge Point Mapping v0.1
- Knowledge Point Architecture v0.1

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


# Completed

## Documentation Architecture Standard

Status:

Completed

Purpose:

Ensure architectural intent survives AI handoff across:

- ChatGPT
- Gemini
- Claude
- DeepSeek
- future AI systems

Reference:

- ADR-DOC-001 Documentation Must Be AI-Transferable

Outcome:

Future architectural documents should include:

- Purpose
- Context
- Decision
- Rationale
- Examples
- Counter Examples
- Implications
- Open Questions


# Deferred

## Commit Suffix Automation

Status:

Deferred

Reason:

AI reconstruction relies on:

* docs/api_snapshot.md

Commit-message metadata is considered secondary.
