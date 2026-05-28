# architecture_direction_v0.1

Status: Draft

Version: v0.1

Last Updated: 2026-05-27


# Purpose

Define the long-term architectural direction of SciForge-Edu.

This document exists to preserve:

- architectural intent
- design philosophy
- long-term system direction
- AI collaboration continuity

This document is intentionally broader than subsystem specifications.


# Vision

SciForge-Edu aims to become:

```text
an AI-native educational repository and authoring system
```

The system is designed to support:

- structured educational content
- repository-based assessment workflows
- AI-assisted authoring
- deterministic educational tooling
- inspectable repository evolution

SciForge-Edu is not intended to become:

- a black-box AI content generator
- an opaque recommendation engine
- an AI-only workflow system


# Core Architectural Philosophy


## Deterministic Systems

Core repository behavior should remain:

- deterministic
- inspectable
- reproducible

Repository operations should avoid hidden behavior whenever possible.


## AI-readable Architecture

System architecture should remain understandable to both:

- human developers
- AI collaborators

This motivates:

- api_snapshot.md
- explicit repository structures
- readable metadata models
- architecture-oriented documentation


## Projection-based Repository Design

SciForge-Edu separates:

```text
Question
↓
Analysis
↓
RepositoryIndex
```

Question remains the primary domain object.

RepositoryIndex exists as a searchable metadata projection layer.

This separation allows:

- lightweight repository traversal
- scalable query evolution
- future indexing expansion
- semantic search integration


## Filesystem-first Evolution

Current repository design prioritizes:

- readability
- portability
- inspectability
- explicit structure

Filesystem-based storage is intentionally preferred during early evolution.

Future database-backed indexing may later coexist with filesystem storage.


# Why Snapshot Exists

api_snapshot.md exists to support:

- AI collaboration continuity
- architecture reconstruction
- runtime visibility
- repository onboarding

The snapshot system is intended to reduce:

- repeated architecture explanation
- context reconstruction cost
- hidden runtime drift

Snapshot files are treated as:

```text
system state artifacts
```

rather than user-authored documentation.


# Repository Philosophy

SciForge-Edu treats educational content as:

```text
structured repository entities
```

rather than isolated files.

Repository architecture prioritizes:

- reusable questions
- metadata-aware search
- provenance tracking
- version-aware evolution
- future analytics support


# Query Philosophy

Repository queries should remain:

- explicit
- deterministic
- inspectable
- metadata-oriented

Current repository search intentionally avoids:

- opaque ranking
- hidden recommendation scoring
- non-reproducible semantic ordering

These constraints may evolve carefully over time.


# AI Collaboration Philosophy

AI is treated as:

```text
an architectural collaborator
```

not merely a code generator.

The repository is intentionally designed to support:

- multi-session continuity
- AI-to-AI handoff
- architecture reconstruction
- design intent preservation

This motivates:

- draft RFC documents
- snapshot systems
- explicit repository philosophy
- architectural governance


# Long-term Evolution Direction

Potential future directions include:

- semantic repository search
- recommendation systems
- usage analytics
- AI-assisted authoring workflows
- repository graph analysis
- curriculum-aware search
- assessment analytics
- workspace orchestration

These should evolve without sacrificing:

- inspectability
- determinism
- architecture readability


# Architectural Non-goals

SciForge-Edu intentionally avoids prioritizing:

- opaque AI-only workflows
- hidden ranking systems
- non-inspectable repository behavior
- purely prompt-driven architecture
- tightly coupled runtime systems
- unreadable storage formats


# Documentation Philosophy

SciForge-Edu documentation is divided into layers:

```text
Runtime Layer
    api_snapshot.md

Subsystem Design Layer
    repository_query_spec
    repository_index_spec
    parser_grammar_spec
    ...

Architectural Direction Layer
    architecture_direction_v0.1.md

Working Context Layer
    current_status.md
```

This layered structure exists to support:

- architecture continuity
- AI collaboration
- long-term repository evolution


# Open Questions

Current unresolved architectural questions include:

- long-term indexing architecture
- semantic search integration strategy
- usage metadata ownership
- recommendation system transparency
- workspace orchestration boundaries
- repository scaling strategy
