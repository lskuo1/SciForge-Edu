# current_status

Status: Active

Last Updated: 2026-07-01


# Purpose

This document preserves active architectural working context across AI sessions.

This file is intended to support:

- AI-to-AI handoff
- multi-session continuity
- architectural focus preservation
- development direction continuity

This document is intentionally shorter and more dynamic than architectural specifications.


# Current Stable Foundations

The following architectural components are currently considered stable:

- Question model foundation
- Analysis metadata layer
- RepositoryManager persistence workflow
- RepositoryIndex projection architecture
- Structural repository query support
- Snapshot synchronization workflow
- Draft RFC governance structure
- Engineering Change Governance framework (Class A/Class B change classification & TIA-1 to TIA-5 workflows)
- Engineering Contributor Guide (repository navigation and contributor orientation)

Current stable repository projection flow:

```text
Question
↓
Analysis
↓
RepositoryIndex
↓
search()
```

RepositoryIndex is currently treated as:

```text
a searchable metadata projection layer
```

rather than a duplicate Question object.


# Current Active Focus

Current development focus areas:

- return focus to runtime implementation (e.g., sandbox compilation, usage/statistical metadata)
- validate real repository behavior
- maintain document-to-code consistency (api_snapshot.md and current_status.md)

The repository governance baseline is established. Future development focus returns to runtime implementation.


# Current Query System Status

Repository Query v1 is implemented.

Current supported structural queries:

- uuid
- question_type
- subject
- chapter
- difficulty_level
- tags

Current query behavior remains:

- deterministic
- explicit
- metadata-oriented
- filesystem-compatible


# Current Snapshot System Status

Snapshot workflow is operational.

Current snapshot behavior:

- generated automatically during commit workflow
- synchronized through pre-commit checks
- treated as system-state artifacts
- intended for AI-readable runtime reconstruction

Current governance observation:

- snapshot synchronization is stable
- snapshot auto-staging is stable
- commit suffix automation remains unresolved
- commit suffix automation is currently treated as a future enhancement
- AI reconstruction should rely on api_snapshot.md itself rather than commit-message metadata

Current snapshot source-of-truth:

```text
docs/api_snapshot.md
```


# Current Architectural Tensions

The following architectural questions remain intentionally unresolved:

- filesystem indexing vs sqlite indexing
- ownership of usage metadata
- statistical metadata storage boundaries
- semantic search transparency
- recommendation system inspectability
- workspace orchestration boundaries

These tensions should remain visible during future development.


# Current Architectural Direction

Current architectural direction prioritizes:

- inspectable systems
- deterministic workflows
- AI-readable architecture
- projection-based repository design
- explicit metadata structures

Current development intentionally avoids:

- opaque ranking systems
- hidden AI-only behavior
- premature semantic abstraction
- tightly coupled runtime systems


# Current Relevant Context Files

Core runtime snapshot:

- docs/api_snapshot.md

Current repository architecture specs:

- docs/draft/repository_query_spec_v0.1.md
- docs/draft/repository_index_spec_v0.1.md

Current architectural direction:

- docs/draft/architecture_direction_v0.1.md


# Handoff Guidance

New AI sessions should:

1. Read api_snapshot.md first
2. Read relevant local subsystem specs
3. Read architecture_direction_v0.1.md
4. Read current_status.md last

The goal is to reconstruct:

- runtime structure
- local subsystem philosophy
- global architectural direction
- current development focus

before proposing architectural changes.


# Near-term Expected Evolution

Likely near-term evolution areas:

- usage metadata layer and query support
- statistical query support and repository analytics
- sandbox compilation environment and LaTeX PDF compilation service
- repository workflow and parser validation

Current priority remains:

```text
validate repository workflow behavior and advance runtime implementation
```

# Current Governance Notes

Current governance decisions:

- [Sprint 004 Completed] The Engineering Contributor Guide has been finalized as the canonical entry point for contributors.
- The repository governance baseline is established. Future development focus returns to runtime implementation.
- commit suffix automation is currently deferred.

The repository currently treats:

- docs/api_snapshot.md

as the authoritative AI reconstruction signal.

Commit-message metadata is considered secondary.
