# repository_index_spec_v0.1

Status: Draft

Version: v0.1

Last Updated: 2026-05-27


# Purpose

Define searchable repository metadata structure for SciForge-Edu.

This specification focuses on:

- repository index structure
- searchable metadata projection
- indexing philosophy
- future query scalability

This document does not define search engine implementation details.


# Design Philosophy

RepositoryIndex is a query projection layer.

RepositoryIndex is not a duplicate Question object.

The repository index should:

- support fast metadata lookup
- avoid loading full Question objects
- remain lightweight
- remain query-oriented

The repository index should not:

- duplicate complete question content
- contain full solution content
- contain complete statistics history
- become a secondary Question model


# Relationship with Question Model

Question remains the primary domain object.

RepositoryIndex represents:

- searchable metadata
- query-oriented projections
- lightweight retrieval structures

Question represents:

- complete assessment content
- full version history
- complete workflow metadata


# Index Categories


## Structural Metadata

Structural metadata represents intrinsic question structure.

Candidate fields:

- uuid
- label
- question_type
- subject
- chapter
- tags
- difficulty_level
- current_version


## Statistical Metadata

Statistical metadata represents observed assessment behavior.

Candidate fields:

- correct_rate
- difficulty_index
- discrimination_index
- sample_size

Important notes:

- index stores summary statistics only
- full statistics history remains in Question


## Provenance Metadata

Provenance metadata represents content origin information.

Candidate fields:

- source_type
- source_name
- created_by
- model_version
- confidence


## Usage Metadata

Usage metadata represents repository workflow activity.

Candidate fields:

- usage_count
- last_used
- last_modified
- indexed_at

Potential future fields:

- recommendation_score
- archive_status
- review_status


# Candidate RepositoryIndex Structure

Example candidate structure:

```text
RepositoryIndex
├── uuid
├── label
├── question_type
├── subject
├── chapter
├── tags
├── difficulty_level
├── correct_rate
├── source_type
├── created_by
├── usage_count
├── last_used
├── indexed_at
└── source_path
```


# Non-indexed Data

The following data should remain outside RepositoryIndex:

- full LaTeX content
- complete solution content
- complete analysis metadata
- full version history
- raw source files
- detailed statistics history

These remain inside Question or related models.


# Query Relationship

RepositoryIndex should support:

- structural filtering
- metadata filtering
- lightweight repository traversal
- future ranking systems

RepositoryIndex should avoid:

- semantic interpretation
- heavy content analysis
- full Question reconstruction


# Storage Considerations


## Current Direction

Current repository direction:

- filesystem-based repository
- JSON-based storage
- lightweight repository index


## Possible Future Directions

Possible future directions:

- sqlite-backed index
- hybrid metadata index
- semantic embedding index
- incremental indexing
- distributed repository search


# AI Collaboration Considerations

RepositoryIndex should remain AI-readable.

Index structures may later appear in:

- api_snapshot.md
- repository architecture snapshots
- AI repository context exports

Index structures should prioritize readability over storage optimization.


# Open Questions

Current unresolved questions:

- should statistics remain partially duplicated in index?
- should usage metadata become a separate model?
- should semantic embeddings remain external?
- should index updates remain synchronous?
- should repository indexing support ranking metadata?
